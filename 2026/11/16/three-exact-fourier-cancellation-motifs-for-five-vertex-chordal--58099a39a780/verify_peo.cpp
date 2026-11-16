#include <bits/stdc++.h>
using namespace std;
// Independent recognition via repeated simplicial elimination.
bool chordal(uint32_t bits,int n, const vector<pair<int,int>>& ed){
 uint16_t adj[9]={0};for(size_t e=0;e<ed.size();++e) if(bits & (1u<<e)){auto [u,v]=ed[e];adj[u]|=1<<v;adj[v]|=1<<u;}
 uint16_t rem=(1<<n)-1;
 while(rem){bool good=false;for(int v=0;v<n;v++) if(rem & (1<<v)){
  uint16_t nb=adj[v]&rem;bool clique=true;
  for(int w=0;w<n;w++) if(nb&(1<<w)) if(((adj[w] & nb) != (nb & ~(1<<w)))){clique=false;break;}
  if(clique){rem &= ~(1<<v);good=true;break;}
 }if(!good)return false;
 }return true;
}
int main(int argc,char**argv){int n=argc>1?atoi(argv[1]):6;vector<pair<int,int>>ed;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)ed.emplace_back(i,j);
 int m=ed.size(); if(m>23)return 2;uint32_t N=1u<<m;vector<int32_t>f(N);int64_t cnt=0,edge0=0,edgesum=0;
 for(uint32_t mask=0;mask<N;mask++) if(chordal(mask,n,ed)){f[mask]=1;cnt++;edge0+=(mask&1u)!=0;edgesum+=__builtin_popcount(mask);}
 cout<<"n="<<n<<" chordal="<<cnt<<" edge0="<<edge0<<" edge_sum="<<edgesum<<"\n";
 for(uint32_t len=1;len<N;len<<=1)for(uint32_t k=0;k<N;k+=(len<<1))for(uint32_t j=0;j<len;j++){int32_t x=f[k+j],y=f[k+j+len];f[k+j]=x+y;f[k+j+len]=x-y;}
 map<int32_t,int64_t>vals; map<int,int64_t>zbyweight,positive;int32_t minmag=INT32_MAX,maxmag=0;int32_t minindex=-1;
 for(uint32_t k=0;k<N;k++){int32_t x=f[k],a=abs(x);if(n==6 && (x%4+4)%4!=2){cerr<<"mod-four certificate failed at "<<k<<"\n";return 3;}vals[a]++; if(!x)zbyweight[__builtin_popcount(k)]++; else{positive[__builtin_popcount(k)]++;if(a<minmag){minmag=a;minindex=k;}}maxmag=max(maxmag,a);}
 cout<<"zeros="<<vals[0]<<" minmag="<<minmag<<" minindex="<<minindex<<" maxmag="<<maxmag<<"\n";
 cout<<"zero_by_weight:";for(auto [k,v]:zbyweight)cout<<" "<<k<<":"<<v;cout<<"\n";
 cout<<"abs_values:";for(auto [k,v]:vals)cout<<" "<<k<<":"<<v;cout<<"\n";
 int64_t square=0;for(auto [k,v]:vals)square+=int64_t(k)*k*v;cout<<"parseval="<<square<<" expected="<<int64_t(N)*cnt<<"\n";
 if(square!=int64_t(N)*cnt)return 4;
 if(n==5 && !(cnt==822 && vals[0]==120 && minmag==2))return 5;
 if(n==6 && !(cnt==18154 && edge0==8524 && vals[0]==0 && minmag==2 && f[639]==2))return 6;
}
