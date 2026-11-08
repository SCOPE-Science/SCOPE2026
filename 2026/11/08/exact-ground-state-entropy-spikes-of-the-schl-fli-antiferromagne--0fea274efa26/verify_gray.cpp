// Exhaustive Gray-code enumeration of cut maxima and their multiplicities.
// Compile with: c++ -O3 -std=c++17 verify_gray.cpp -o verify_gray
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
struct Vertex {int t,a,b;};
int main(){
 vector<Vertex> v;
 for(int i=0;i<6;++i) v.push_back({0,i,-1});
 for(int i=0;i<6;++i) for(int j=i+1;j<6;++j) v.push_back({1,i,j});
 for(int i=0;i<6;++i) v.push_back({2,i,-1});
 auto intersect=[](Vertex x,Vertex y){
  if(x.t>y.t) swap(x,y);
  if(x.t==0 && y.t==0) return false;
  if(x.t==0 && y.t==1) return x.a==y.a || x.a==y.b;
  if(x.t==0 && y.t==2) return x.a!=y.a;
  if(x.t==1 && y.t==1) return x.a!=y.a && x.a!=y.b && x.b!=y.a && x.b!=y.b;
  if(x.t==1 && y.t==2) return x.a==y.a || x.b==y.a;
  return false;
 };
 vector<int> nbrs[27];
 for(int i=0;i<27;++i) for(int j=i+1;j<27;++j)
  if(!intersect(v[i],v[j])){nbrs[i].push_back(j);nbrs[j].push_back(i);}
 for(int i=0;i<27;++i) if(nbrs[i].size()!=16) return 2;
 int k=0,cut=0,neighbors_in_set[27]={},is_in_set[27]={};
 int best[28]; fill(best,best+28,-1);
 uint64_t multiplicity[28]={};
 auto count=[&](){if(cut>best[k]){best[k]=cut; multiplicity[k]=1;}
                 else if(cut==best[k]) ++multiplicity[k];};
 count();
 // Gray order: g(t)=t xor (t>>1), successive words toggle ctz(t).
 for(uint32_t t=1;t<(1u<<27);++t){
  int u=__builtin_ctz(t),sign=is_in_set[u]?-1:1;
  cut+=sign*(16-2*neighbors_in_set[u]);
  is_in_set[u]^=1;k+=sign;
  for(int w:nbrs[u]) neighbors_in_set[w]+=sign;
  count();
 }
 for(int j=0;j<=27;++j) cout<<j<<" "<<best[j]<<" "<<multiplicity[j]<<"\n";
}
