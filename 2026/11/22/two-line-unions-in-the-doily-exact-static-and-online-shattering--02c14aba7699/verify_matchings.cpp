// Exhaustive independent K6 perfect-matching realization of the doily.
// Build: c++ -O2 -std=c++17 verify_matchings.cpp -o verify_matchings
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using Mask=uint32_t;
using Wide=__uint128_t;

int pop(Mask x){return __builtin_popcount(x);}
template<size_t N> int gf2rank(vector<bitset<N>> cols){
 array<bitset<N>,N> piv{}; int rank=0;
 for(auto x:cols)for(int j=(int)N-1;j>=0;--j)if(x[j]){
  if(piv[j].any()) x ^= piv[j];
  else {piv[j]=x; ++rank; break;}
 }
 return rank;
}

int main(){
 vector<array<int,3>> matchings;
 function<void(vector<int>,vector<int>)> rec=[&](vector<int> free,vector<int> edges){
  if(free.empty()){
   sort(edges.begin(),edges.end());
   matchings.push_back({edges[0],edges[1],edges[2]});return;
  }
  int a=free.front();
  for(size_t j=1;j<free.size();++j){
   int b=free[j];int e=0;
   for(int x=0;x<a;++x)e+=5-x;
   e+=b-a-1;
   auto rem=free;rem.erase(rem.begin()+j);rem.erase(rem.begin());
   auto next=edges;next.push_back(e);rec(rem,next);
  }
 };
 rec({0,1,2,3,4,5},{});
 sort(matchings.begin(),matchings.end());
 assert(matchings.size()==15);
 vector<Mask> lines(15,0);
 for(int i=0;i<15;++i)for(int e:matchings[i])lines[e]|=1u<<i;
 for(auto x:lines)assert(pop(x)==3);
 set<Mask> uniq;
 for(int a=0;a<15;++a)for(int b=a+1;b<15;++b) uniq.insert(lines[a]|lines[b]);
 vector<Mask> concepts(uniq.begin(),uniq.end());assert(concepts.size()==105);
 map<int,vector<Mask>> f;
 for(Mask s=0;s<(1u<<15);++s){
  int k=pop(s);if(k>5)continue;
  set<Mask> patterns;
  for(auto c:concepts)patterns.insert(c&s);
  if((int)patterns.size()==(1<<k))f[k].push_back(s);
 }
 int expected[]={1,15,105,375,495,0};
 for(int k=0;k<=5;++k)assert((int)f[k].size()==expected[k]);
 int triangle_facets=0;
 for(auto t:f[3]){
  bool ext=false;for(auto s:f[4])if((s&t)==t){ext=true;break;}
  if(!ext)++triangle_facets;
 }
 assert(triangle_facets==15);
 // Boundary matrices indexed by faces of size k, coefficients in GF(2).
 vector<bitset<15>> b1;
 for(auto s:f[2]){
  bitset<15> col;
  for(int i=0;i<15;++i)if(s&(1u<<i))col.flip(i);
  b1.push_back(col);
 }
 int r1=gf2rank(b1);
 map<Mask,int> idx2,idx3;
 for(int i=0;i<(int)f[2].size();++i)idx2[f[2][i]]=i;
 for(int i=0;i<(int)f[3].size();++i)idx3[f[3][i]]=i;
 vector<bitset<105>> b2;
 for(auto s:f[3]){
  bitset<105> col;
  for(int i=0;i<15;++i)if(s&(1u<<i))col.flip(idx2.at(s^(1u<<i)));
  b2.push_back(col);
 }
 int r2=gf2rank(b2);
 vector<bitset<375>> b3;
 for(auto s:f[4]){
  bitset<375> col;
  for(int i=0;i<15;++i)if(s&(1u<<i))col.flip(idx3.at(s^(1u<<i)));
  b3.push_back(col);
 }
 int r3=gf2rank(b3);
 assert(r1==14 && r2==91 && r3==269);
 assert(105-r1-r2==0 && 375-r2-r3==15 && 495-r3==226);
 // Exact Littlestone recurrence on 105-bit masks of remaining hypotheses.
 vector<Wide> yes(15,0);
 for(int j=0;j<105;++j)for(int i=0;i<15;++i)
  if(concepts[j]&(1u<<i))yes[i] |= (Wide(1)<<j);
 map<Wide,int> memo;
 function<int(Wide)> depth=[&](Wide h)->int{
  auto it=memo.find(h);if(it!=memo.end())return it->second;
  int best=0;
  for(int i=0;i<15;++i){
   Wide a=h&yes[i],b=h^a;
   if(a&&b)best=max(best,1+min(depth(a),depth(b)));
  }
  memo[h]=best;return best;
 };
 Wide all=(Wide(1)<<105)-1;
 int d=depth(all);
 assert(d==5);
 cout<<"PASS: 15 points, 105 double-line concepts; polynomial 1+15z+105z^2+375z^3+495z^4; "
     <<"15 isolated maximal triangles; boundary ranks (14,91,269); Betti (0,0,15,226); "
     <<"Littlestone 5; DP states "<<memo.size()<<"\n";
}
