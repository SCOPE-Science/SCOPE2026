#include <bits/stdc++.h>
using namespace std;
static uint16_t a[65536];
static uint16_t nbr[16];
static uint64_t shells[90][91]={},total=0,maxd=0,missing=0;
static map<uint32_t,uint64_t> basins;
static map<uint32_t,uint64_t> cylength;
static uint32_t exemplar[90]={};
static uint64_t progress=0;
static inline uint32_t nxt(uint32_t x){
  uint32_t E=x&65535u,R=x>>16;
  uint32_t NewE=(uint32_t)a[E] & (~(E|R))&65535u;
  return NewE | (E<<16);
}
static inline void check(uint32_t initial){
  uint32_t h[90];h[0]=initial;
  if(initial==0){++shells[0][1];++basins[0];++total;return;}
  for(int i=1;i<88;++i){
    uint32_t state=nxt(h[i-1]);h[i]=state;
    if(state==0){++shells[i][1];++basins[0];if(i>maxd){maxd=i;exemplar[i]=initial;}++total;return;}
    for(int j=0;j<i;++j){
      if(h[j]==state){
        int period=i-j;
        if(period>90){++missing;return;}
        uint32_t can=h[j];for(int k=j+1;k<i;++k)can=min(can,h[k]);
        ++shells[j][period];++basins[can];cylength[can]=period;
        if(j>maxd){maxd=j;exemplar[j]=initial;}
        ++total;return;
      }
    }
  }
  ++missing;
}
static void gen(int v,uint16_t E,uint16_t R){
 if(v==16){check((uint32_t)E|((uint32_t)R<<16));return;}
 gen(v+1,E,R);gen(v+1,E|(1u<<v),R);gen(v+1,E,R|(1u<<v));
}
int main(){
 auto start=chrono::steady_clock::now();
 for(int v=0;v<16;++v){for(int i=0;i<4;++i) nbr[v]|=(1u<<(v^(1<<i))); nbr[v]|=1u<<(v^15);}
 for(int m=0;m<65536;++m){uint16_t a2=0;for(int v=0;v<16;++v) if(__builtin_popcount((unsigned)(nbr[v]&m))>=2)a2|=1u<<v;a[m]=a2;}
 gen(0,0,0);
 cout<<"TOTAL "<<total<<" MISSING "<<missing<<" MAXD "<<maxd<<"\n";
 for(int t=0;t<90;++t)for(int p=1;p<91;++p)if(shells[t][p])cout<<"SHELL "<<t<<' '<<p<<' '<<shells[t][p]<<'\n';
 cout<<"CYCLES "<<basins.size()<<'\n';
 map<pair<int,uint64_t>,uint64_t> hist;
 for(auto [c,n]:basins)hist[{cylength.count(c)?cylength[c]:1,n}]++;
 for(auto [ps,count]:hist) cout<<"BASIN "<<ps.first<<' '<<ps.second<<' '<<count<<'\n';
 for(auto [c,n]:basins)if(c) cout<<"CYCLE "<<c<<' '<<cylength[c]<<' '<<n<<'\n';
 cout<<"WITNESS "<<exemplar[maxd]<<'\n';
 cout<<"SECONDS "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<'\n';
}
