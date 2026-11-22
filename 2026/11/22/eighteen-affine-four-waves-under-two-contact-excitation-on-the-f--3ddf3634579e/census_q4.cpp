#include <bits/stdc++.h>
using namespace std;
static constexpr uint32_t POW=6561, N=43046721;
static uint16_t ex[POW],rf[POW],decode[65536];
static void setup(){
    for(uint32_t s=0;s<POW;s++){
        uint32_t t=s; uint16_t a=0,b=0;
        for(int i=0;i<8;i++){auto c=t%3;t/=3;if(c==1)a|=uint16_t(1u<<i);if(c==2)b|=uint16_t(1u<<i);}
        ex[s]=a;rf[s]=b;decode[a|(b<<8)]=s;
    }
}
static inline uint32_t step(uint32_t s){
    uint32_t lo=s%POW,hi=s/POW;
    uint16_t e=ex[lo]|(ex[hi]<<8),r=rf[lo]|(rf[hi]<<8);
    uint16_t b0=((e&0x5555)<<1)|((e&0xaaaa)>>1);
    uint16_t b1=((e&0x3333)<<2)|((e&0xcccc)>>2);
    uint16_t b2=((e&0x0f0f)<<4)|((e&0xf0f0)>>4);
    uint16_t b3=((e&0x00ff)<<8)|((e&0xff00)>>8);
    uint16_t two=(b0&b1)|(b0&b2)|(b0&b3)|(b1&b2)|(b1&b3)|(b2&b3);
    uint16_t ne=(~(e|r))&two;
    return decode[(ne&255)|((e&255)<<8)] + POW*decode[(ne>>8)|((e>>8)<<8)];
}
int main(){setup();
    vector<uint8_t> status(N,0),depth(N,0),period(N,0);
    vector<uint32_t> basin(N,0);vector<uint32_t> path; path.reserve(64);
    vector<uint32_t> reps;vector<uint32_t> bsize;
    uint64_t hist[256][20]{}; uint64_t total=0, cycles=0;
    for(uint32_t start=0;start<N;start++){
        if(status[start]==2)continue;
        path.clear();uint32_t s=start;
        while(status[s]==0){status[s]=1;path.push_back(s);s=step(s);}
        int i=(int)path.size()-1;
        if(status[s]==1){
            auto it=find(path.begin(),path.end(),s);
            if(it==path.end()){cerr<<"INVALID path";return 1;}
            size_t ci=it-path.begin();uint32_t p=path.size()-ci;
            if(p>=20){cerr<<"LARGE PERIOD "<<p;return 2;}
            uint32_t id=reps.size();
            uint32_t rep=*min_element(path.begin()+ci,path.end());
            reps.push_back(rep);bsize.push_back(0);cycles++;
            for(size_t j=ci;j<path.size();j++){
                uint32_t x=path[j];status[x]=2;depth[x]=0;period[x]=p;basin[x]=id;
                hist[0][p]++;bsize[id]++;total++;
            }
            i=(int)ci-1;
        }
        for(;i>=0;i--){
            uint32_t x=path[i],nx=step(x);
            if(status[nx]!=2){cerr<<"INVALID successor";return 3;}
            uint8_t d=depth[nx]+1; if(d==255){cerr<<"DEPTH OVERFLOW";return 4;}
            uint32_t id=basin[nx];
            status[x]=2;depth[x]=d;period[x]=period[nx];basin[x]=id;
            hist[d][period[x]]++;bsize[id]++;total++;
        }
        if(start%5000000==0)cerr<<"checkpoint "<<start<<" cycles "<<cycles<<"\n";
    }
    if(total!=N){cerr<<"INCOMPLETE "<<total;return 5;}
    cout<<"TOTAL "<<total<<" CYCLES "<<cycles<<"\n";
    for(int d=0;d<256;d++)for(int p=0;p<20;p++)if(hist[d][p])cout<<"HIST "<<d<<" "<<p<<" "<<hist[d][p]<<"\n";
    map<pair<uint8_t,uint32_t>,uint32_t> bh;
    for(size_t i=0;i<reps.size();i++){ bh[{period[reps[i]],bsize[i]}]++; }
    for(auto &[k,v]:bh)cout<<"BASIN "<<int(k.first)<<" "<<k.second<<" "<<v<<"\n";
    for(size_t i=0;i<reps.size();i++) if(period[reps[i]]>1)cout<<"CYCLE "<<reps[i]<<" "<<int(period[reps[i]])<<" "<<bsize[i]<<"\n";
    uint32_t maxdep=0,example=0;for(uint32_t s=0;s<N;s++)if(depth[s]>maxdep){maxdep=depth[s];example=s;}
    cout<<"MAXDEP "<<maxdep<<" EXAMPLE "<<example<<"\n";
    return 0;
}
