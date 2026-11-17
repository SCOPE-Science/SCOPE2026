#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
// Direct 20-vertex full-state evolution, using three-bit neighbor masks.
// This implementation does not use the two-shore factorization.
constexpr int n=10, V=20, STATES=1<<V;
vector<unsigned> masks(int k){
 vector<unsigned> m(V,0);
 for(int i=0;i<n;++i){
   m[i]=(1u<<((i+1)%n)) | (1u<<((i+n-1)%n)) | (1u<<(n+i));
   m[n+i]=(1u<<i) | (1u<<(n+(i+k)%n)) | (1u<<(n+(i+n-k)%n));
 }
 for(auto b:m)assert(__builtin_popcount(b)==3);
 return m;
}
int next_state(int x, const vector<unsigned>& m){
 int y=0;
 for(int j=0;j<V;++j)if(__builtin_popcount((unsigned)x&m[j])>=2)y|=1<<j;
 return y;
}
int main(){
 for(int k:{1,3}){
  auto m=masks(k);
  vector<int> nxt(STATES);
  for(int s=0;s<STATES;++s)nxt[s]=next_state(s,m);
  map<pair<int,int>,int64_t> histogram;
  map<int,int64_t> weights,flips;
  for(int s=0;s<STATES;++s){
    int y=s,depth=0;
    while(nxt[nxt[y]]!=y){y=nxt[y];depth++;assert(depth<20);}
    int period=(nxt[y]==y ? 1:2);
    histogram[{depth,period}]++;
    if(nxt[s]==s)weights[__builtin_popcount((unsigned)s)]++;
    else if(nxt[nxt[s]]==s)
       flips[__builtin_popcount((unsigned)(s^nxt[s]))]++;
  }
  int64_t nf=0,nb=0;int depth=0;
  for(auto [a,num]:histogram){if(a.second==1)nb+=num; if(a.first==0&&a.second==1)nf=num;depth=max(depth,a.first);}
  int64_t prim=0;for(auto [f,num]:flips){assert(num%2==0);prim+=num/2;}
  cout<<"GP(10,"<<k<<") fixed="<<nf<<" primitive_two="<<prim
      <<" fixed_basin="<<nb<<" two_basin="<<STATES-nb<<" max_entry="<<depth<<"\n";
  cout<<" fixed_weight";for(auto [w,v]:weights)cout<<" "<<w<<":"<<v;cout<<"\n";
  cout<<" two_flip_orbits";for(auto [w,v]:flips)cout<<" "<<w<<":"<<v/2;cout<<"\n";
  cout<<" entry_period";for(auto [p,v]:histogram)cout<<" ("<<p.first<<","<<p.second<<"):"<<v;cout<<"\n";
  assert(nf==124&&prim==7626&&depth==4);
 }
}
