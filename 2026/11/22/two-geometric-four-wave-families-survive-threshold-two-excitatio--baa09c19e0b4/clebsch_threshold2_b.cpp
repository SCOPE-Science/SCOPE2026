// Independent finite functional-digraph enumeration by ternary indexing.
#include <bits/stdc++.h>
using namespace std;
constexpr uint32_t N=43046721; // 3^16
constexpr int H=6561; // 3^8
static uint16_t e8[H],r8[H],neighbor[16];
static uint32_t pow3[17], weight[65536];
int main(){
  auto start=chrono::steady_clock::now();
  pow3[0]=1;for(int i=1;i<=16;++i)pow3[i]=pow3[i-1]*3;
  for(int x=0;x<H;++x){int t=x;for(int i=0;i<8;++i){int digit=t%3;t/=3;if(digit==1)e8[x]|=1u<<i;if(digit==2)r8[x]|=1u<<i;}}
  for(int m=1;m<65536;++m){int bit=__builtin_ctz((unsigned)m);weight[m]=weight[m^(1<<bit)]+pow3[bit];}
  for(int v=0;v<16;++v){for(int i=0;i<4;++i)neighbor[v]|=1u<<(v^(1<<i));neighbor[v]|=1u<<(v^15);}
  vector<uint32_t> nx(N),indeg(N,0);
  for(uint32_t code=0;code<N;++code){
    uint32_t lo=code%H,hi=code/H;
    unsigned E=e8[lo]|(e8[hi]<<8),R=r8[lo]|(r8[hi]<<8), fresh=0;
    for(int v=0;v<16;++v){
      unsigned k=1u<<v;
      if(!(k&(E|R)) && __builtin_popcount(neighbor[v]&E)>=2)fresh|=k;
    }
    uint32_t dst=weight[fresh]+2*weight[E];
    nx[code]=dst;++indeg[dst];
  }
  vector<uint32_t> peeled;peeled.reserve(N);
  for(uint32_t code=0;code<N;++code)if(indeg[code]==0)peeled.push_back(code);
  for(size_t h=0;h<peeled.size();++h){uint32_t dst=nx[peeled[h]];if(--indeg[dst]==0)peeled.push_back(dst);}
  vector<uint32_t> root(N,UINT_MAX);
  vector<uint16_t> depth(N,65535);
  map<pair<uint32_t,int>,uint64_t> primitive;
  map<uint32_t,int> period;
  for(uint32_t x=0;x<N;++x)if(indeg[x] && root[x]==UINT_MAX){
    uint32_t u=x,can=x;int p=0;
    do{can=min(can,u);u=nx[u];++p;}while(u!=x);
    u=x;do{root[u]=can;depth[u]=0;u=nx[u];}while(u!=x);
    period[can]=p;
  }
  for(auto it=peeled.rbegin();it!=peeled.rend();++it){uint32_t x=*it; if(root[nx[x]]==UINT_MAX || depth[nx[x]]>=65534){cerr<<"UNRESOLVED_OR_DEPTH_OVERFLOW\n";return 3;} root[x]=root[nx[x]];depth[x]=depth[nx[x]]+1;}
  if(peeled.size()+361!=N || period.size()!=91){cerr<<"BAD_PERIODIC_CENSUS\n";return 2;}
  map<pair<int,int>,uint64_t> shells;
  map<uint32_t,uint64_t> sizes;
  uint32_t maxd=0,example=0;
  for(uint32_t x=0;x<N;++x){
    int d=depth[x],p=period[root[x]];
    ++shells[{d,p}];++sizes[root[x]];
    if(d>maxd){maxd=d;example=x;}
  }
  map<pair<int,uint64_t>,uint64_t> hist;
  for(auto [r,n]:sizes)++hist[{period[r],n}];
  cout<<"TOTAL "<<N<<" PEELED "<<peeled.size()<<" CYCLES "<<sizes.size()<<" MAXD "<<maxd<<" WITNESS_ID "<<example<<"\n";
  for(auto [k,n]:shells)cout<<"SHELL "<<k.first<<' '<<k.second<<' '<<n<<'\n';
  for(auto [k,n]:hist)cout<<"BASIN "<<k.first<<' '<<k.second<<' '<<n<<'\n';
  cout<<"SECONDS "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}
