// Exact finite classification of coherent-triple singleton-type grade profiles.
// Compile: c++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
static int pc(unsigned x){return __builtin_popcount(x);}
using Poly=vector<int>;
struct GraphSystem {
 int n,m,k,G,M;vector<pair<int,int>> edges;vector<unsigned> cut;
 GraphSystem(int n):n(n),m(n-1),k(m*(m-1)/2),G(1<<k),M(1<<m) {
  for(int i=0;i<m;i++)for(int j=i+1;j<m;j++)edges.push_back({i,j});
  cut.resize(M);
  for(int s=0;s<M;s++)for(int j=0;j<k;j++)
   if(((s>>edges[j].first)^(s>>edges[j].second))&1)cut[s]|=1u<<j;
 }
 Poly polynomial(unsigned g) const {
  Poly p(n*(n-1)/2+1);
  for(int s=0;s<M;s++)p[pc((unsigned)s)+pc(g^cut[s])]++;
  return p;
 }
 vector<int> triple_degrees(unsigned g) const {
  int a[8][8]{}; for(int j=0;j<k;j++){
   auto [u,v]=edges[j];a[u+1][v+1]=a[v+1][u+1]=(g>>j)&1;
  }
  vector<int> deg(n);
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int h=j+1;h<n;h++){
   if(a[i][j]^a[i][h]^a[j][h]){deg[i]++;deg[j]++;deg[h]++;}
  }
  sort(deg.begin(),deg.end());return deg;
 }
 void mark_orbit(unsigned g,vector<uint8_t>&seen) const {
  int a[8][8]{};
  for(int j=0;j<k;j++){auto[u,v]=edges[j];a[u+1][v+1]=a[v+1][u+1]=(g>>j)&1;}
  for(int root=0;root<n;root++){
   vector<int> rest;
   for(int v=0;v<n;v++)if(v!=root)rest.push_back(v);
   do{
    unsigned code=0;int bit=0;
    for(int i=0;i<m;i++)for(int j=i+1;j<m;j++,bit++){
     int u=rest[i],v=rest[j];
     code|=(unsigned)(a[u][v]^a[root][u]^a[root][v])<<bit;
    }
    seen[code]=1;
   }while(next_permutation(rest.begin(),rest.end()));
  }
 }
};
int main(){
 const int expectedClasses[]={1,1,1,2,3,7,16,54,243};
 const int expectedPoly[]={1,1,1,2,3,7,16,54,219};
 for(int n=1;n<=8;n++){
  GraphSystem X(n);vector<uint8_t> seen(X.G);
  map<Poly,vector<unsigned>> groups;
  int classes=0;
  for(int g=0;g<X.G;g++)if(!seen[g]){
   ++classes;auto p=X.polynomial(g);
   assert(accumulate(p.begin(),p.end(),0)==X.M);
   groups[p].push_back(g);
   X.mark_orbit(g,seen);
  }
  assert(all_of(seen.begin(),seen.end(),[](uint8_t x){return x==1;}));
  assert(classes==expectedClasses[n]);
  assert((int)groups.size()==expectedPoly[n]);
  map<int,int> sizes;int collisions=0;
  for(auto const&[p,reps]:groups){
   sizes[(int)reps.size()]++;
   if(reps.size()>1){
    ++collisions;
    set<vector<int>> degrees;
    for(unsigned g:reps)degrees.insert(X.triple_degrees(g));
    assert(degrees.size()==reps.size());
   }
  }
  if(n<=7)assert(collisions==0);
  else {assert(sizes[1]==198&&sizes[2]==18&&sizes[3]==3&&collisions==21);}
  cout<<"N="<<n<<" classes="<<classes<<" polys="<<groups.size()<<" collision_groups="<<collisions<<"\n";
  if(n==8){
   const unsigned witness[]={39516,39527,43885};
   auto p=X.polynomial(witness[0]);
   set<vector<int>> degree_sets;
   for(unsigned w:witness){
    assert(X.polynomial(w)==p);
    degree_sets.insert(X.triple_degrees(w));
    cout<<"WITNESS="<<w<<" deg=";
    for(int d:X.triple_degrees(w))cout<<d<<",";
    cout<<"\n";
   }
   assert(degree_sets.size()==3);
   int triples=0;
   for(auto const&[p2,reps]:groups)if(reps.size()==3)triples++;
   assert(triples==3);
   cout<<"WITNESS_POLY=";
   for(int i=0;i<(int)p.size();i++)if(p[i])cout<<i<<":"<<p[i]<<",";
   cout<<"\n";
  }
 }
 cout<<"VERIFY_OK\n";
}
