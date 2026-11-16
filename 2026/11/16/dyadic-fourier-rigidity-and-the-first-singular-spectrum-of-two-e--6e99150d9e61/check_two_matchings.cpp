// Exact Walsh census for the size-two matching orbit of the complete graph K_8.
// Requires only a C++17 compiler; output is deterministic and uses integer arithmetic.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
using Histogram=map<int,uint64_t>;
constexpr int n=8,N=28,B=27;
using Edge=pair<int,int>;
array<Edge,N> all_edges(){
 array<Edge,N> e{};int k=0;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)e[k++]={i,j};
 return e;
}
// All 210 unordered pairs of vertex-disjoint edges.
vector<pair<int,int>> all_matchings(const array<Edge,N>& e){
 vector<pair<int,int>> m;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++){
  auto [i,j]=e[a];auto [k,l]=e[b];
  if(i!=k&&i!=l&&j!=k&&j!=l)m.push_back({a,b});
 }
 return m;
}
int direct_sum(uint32_t neg,const vector<pair<int,int>>& m){
 int ans=0;
 for(auto [a,b]:m)ans+=((neg>>a)&1)==((neg>>b)&1)?1:-1;
 return ans;
}
// Algorithm A: update global signed edge sum and sum of squared signed degrees.
Histogram census_degrees(const array<Edge,N>& e){
 Histogram h;
 int d[n];for(int &v:d)v=n-1;
 int S=N,Q=n*(n-1)*(n-1);
 uint32_t neg=0;
 for(uint32_t k=0;k<(1u<<B);k++){
  int numer=S*S-Q+N;
  if(numer&1)throw runtime_error("nonintegral Fourier coefficient");
  int W=numer/2;
  h[W]+=2; // Opposite global signings have the same degree-two multiplier.
  if(k+1==(1u<<B))break;
  int a=__builtin_ctz(k+1)+1; // edge zero remains positive
  auto [u,v]=e[a];
  int old=(neg&(1u<<a))?-1:1;
  int change=-2*old;
  Q+=2*change*(d[u]+d[v])+2*change*change;
  d[u]+=change;d[v]+=change;S+=change;
  neg^=1u<<a;
 }
 return h;
}
// Algorithm B: update negative-edge count and pairs of disjoint negative edges.
Histogram census_negative_pairs(const array<Edge,N>& e){
 Histogram h;
 int t=0,q=0,degree[n]={};
 uint32_t neg=0;
 for(uint32_t k=0;k<(1u<<B);k++){
  int W=210-30*t+4*q; // 210 2-matchings; each edge has 15 disjoint partners.
  h[W]+=2;
  if(k+1==(1u<<B))break;
  int a=__builtin_ctz(k+1)+1;
  auto [u,v]=e[a];
  if(!(neg&(1u<<a))){
   q+=t-degree[u]-degree[v];
   ++degree[u];++degree[v];++t;
  }else{
   q-=t-degree[u]-degree[v]+1;
   --degree[u];--degree[v];--t;
  }
  neg^=1u<<a;
 }
 return h;
}
void check_samples(const array<Edge,N>& e){
 auto match=all_matchings(e);
 if(match.size()!=210)throw runtime_error("wrong matching count");
 uint32_t mask=0x9e3779b9u;
 for(int k=0;k<2048;k++){
  mask=mask*1664525u+1013904223u;
  uint32_t neg=mask&((1u<<N)-1);
  int deg[n]={},S=0;
  for(int a=0;a<N;a++){
   int v=(neg&(1u<<a))?-1:1;
   auto [u,w]=e[a];deg[u]+=v;deg[w]+=v;S+=v;
  }
  int Q=0;for(int v:deg)Q+=v*v;
  if(direct_sum(neg,match)!=(S*S-Q+N)/2)throw runtime_error("direct mismatch");
 }
}
int main(){
 try{
  auto e=all_edges();check_samples(e);
  auto h=census_degrees(e),g=census_negative_pairs(e);
  if(h!=g)throw runtime_error("independent census mismatch");
  uint64_t total=0,energy=0;int gcd=0,minpos=999999,maxabs=0;
  for(auto [w,count]:h){
   total+=count;energy+=uint64_t(w*w)*count;
   if(w){int a=abs(w);gcd=std::gcd(gcd,a);if(a<minpos)minpos=a;if(a>maxabs)maxabs=a;}
  }
  if(total!=(1ull<<N)||energy!=uint64_t(210)*(1ull<<N)
     ||h[0]!=20467680 ||minpos!=2 ||maxabs!=210 ||gcd!=2)
   throw runtime_error("aggregate certificate mismatch");
  cout<<"TWO_EDGE_MATCHINGS_K8_PASS total="<<total<<" zeros="<<h[0]
      <<" rank="<<total-h[0]<<" min_nonzero="<<minpos
      <<" max="<<maxabs<<" levels="<<h.size()<<"\n";
  cout<<"value,count\n";
  for(auto [w,count]:h)cout<<w<<','<<count<<'\n';
 }catch(const exception& e){cerr<<e.what()<<'\n';return 1;}
}
