// Independent direct-forward three-color trajectory verifier for the sixteen-vertex Boolean cube.
#include <bits/stdc++.h>
using namespace std;
constexpr uint32_t B=6561, N=43046721;
uint16_t ex[6561], refra[6561], activate[65536];
static void init(){
    for(uint32_t s=0;s<B;s++){
        uint32_t w=s;for(int v=0;v<8;v++){uint32_t c=w%3;w/=3;if(c==1)ex[s]|=1u<<v;else if(c==2)refra[s]|=1u<<v;}
    }
    for(uint32_t e=0;e<65536;e++){
        uint16_t a=0;
        for(int v=0;v<16;v++){
            int cnt=0;
            for(int axis=0;axis<4;axis++)cnt+=(e>>(v^(1<<axis)))&1u;
            if(cnt>=2)a|=uint16_t(1u<<v);
        }
        activate[e]=a;
    }
}
static inline uint32_t go(uint32_t s){
    uint16_t e=(uint16_t)s,r=(uint16_t)(s>>16);
    uint16_t ne=activate[e]&~(e|r);
    return uint32_t(ne)|(uint32_t(e)<<16);
}
int main(){init();
    uint64_t hist[20][20]{};
    map<uint32_t,uint64_t> basins;
    uint32_t a[24];
    uint32_t maxdepth=0,example=0,maxperiod=0;
    for(uint32_t s=0;s<N;s++){
        uint32_t x=uint32_t(ex[s%B])|(uint32_t(ex[s/B])<<8) | (uint32_t(refra[s%B])<<16)|(uint32_t(refra[s/B])<<24);
        int d=0,p=0, t;
        for(t=0;t<24;t++){
            int at=-1;
            for(int j=0;j<t;j++)if(a[j]==x){at=j;break;}
            if(at>=0){d=at;p=t-at;break;}
            a[t]=x;x=go(x);
        }
        if(t==24||d>=20||p>=20){cerr<<"ERROR long trajectory "<<s<<"\n";return 1;}
        hist[d][p]++;
        if(uint32_t(d)>maxdepth){maxdepth=d;example=s;}
        maxperiod=max(maxperiod,uint32_t(p));
        uint32_t key=*min_element(a+d,a+t);
        basins[key]++;
    }
    cout<<"TOTAL "<<N<<" BASINS "<<basins.size()<<" MAXDEP "<<maxdepth<<" EXAMPLE "<<example<<" MAXPER "<<maxperiod<<"\n";
    for(int d=0;d<20;d++)for(int p=0;p<20;p++)if(hist[d][p])cout<<"HIST "<<d<<" "<<p<<" "<<hist[d][p]<<"\n";
    map<pair<uint32_t,uint64_t>,int> sizes;
    for(auto [rep,count]:basins){uint32_t x=go(rep),p=1;while(x!=rep){x=go(x);p++;if(p>=20)return 2;}sizes[{p,count}]++;}
    for(auto [key,mult]:sizes)cout<<"BASIN "<<key.first<<" "<<key.second<<" "<<mult<<"\n";
    for(auto [key,count]:basins)if(key)cout<<"CYCLE "<<key<<" "<<count<<"\n";
}
