// Exhaustive finite verification of synchronous tie-retaining majority on
// the Fano incidence graph with zero, one or two edges removed.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra check_all_defects.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
constexpr int N=14, TOTAL=1<<N;
struct Edge {int u,v;};
vector<Edge> edges(){
  vector<Edge> out;
  const int lines[7][3]={{1,2,3},{1,4,5},{1,6,7},{2,4,6},{2,5,7},{3,4,7},{3,5,6}};
  for(int j=0;j<7;j++) for(int k=0;k<3;k++) out.push_back({lines[j][k]-1,j+7});
  sort(out.begin(),out.end(),[](Edge a,Edge b){return tie(a.u,a.v)<tie(b.u,b.v);});
  assert(out.size()==21);return out;
}
struct Outcome {int fixed=0, cycles=0, consensus=0, maxdepth=0, gained=0, lost=0;
  array<int,30> entry{}; vector<unsigned char> basin;vector<int> next;
};
Outcome examine(const vector<Edge>& es, const vector<int>& removed){
 array<unsigned, N> masks{};array<int,N> deg{};
 for(int j=0;j<(int)es.size();j++){
   if(find(removed.begin(), removed.end(), j)!=removed.end()) continue;
   auto [u,v]=es[j];masks[u]|=1u<<v;masks[v]|=1u<<u;deg[u]++;deg[v]++;
 }
 Outcome o;o.basin.resize(TOTAL);o.next.resize(TOTAL);
 for(int s=0;s<TOTAL;s++){
   unsigned out=0;
   for(int v=0;v<N;v++){
     int ones=__builtin_popcount((unsigned)s & masks[v]);
     int val=2*ones>deg[v] ? 1 : (2*ones<deg[v] ? 0 : ((s>>v)&1));
     out|=(unsigned)val<<v;
   }o.next[s]=(int)out;
 }
 for(int s=0;s<TOTAL;s++){
   if(o.next[s]==s)o.fixed++;
   else if(o.next[o.next[s]]==s)o.cycles++;
   int q=s,d=0;
   while(o.next[o.next[q]]!=q){q=o.next[q];++d;assert(d<29);}
   assert(d<30);o.entry[d]++;o.maxdepth=max(o.maxdepth,d);
   o.basin[s]=(q==0||q==TOTAL-1);
   if(o.basin[s])o.consensus++;
 }
 assert(o.cycles%2==0);o.cycles/=2;
 return o;
}
int pair_type(Edge a,Edge b){
 if(a.u==b.u||a.v==b.v) return 1; // share endpoint
 // pair is disjoint; cross incidence is checked by full edge list externally
 return 2;
}
string label(int t){return t==0?"intact":t==1?"single":t==2?"adjacent":t==3?"cross": "separated";}
struct Stats {int count=0; array<int,6> values{};array<int,30> entry{};};
int main(){
 auto es=edges();
 // Graph is the incidence graph of PG(2,2). Its automorphisms
 // permute the 21 incidence edges, yielding the 1 + 3 geometry types.
 auto base=examine(es,{});
 map<int,Stats> summaries;
 auto collect=[&](int group,Outcome&& r){
  int added=0, removed=0;
  for(int s=0;s<TOTAL;s++){
   if(r.basin[s]&&!base.basin[s])added++;
   if(base.basin[s]&&!r.basin[s])removed++;
  }
  r.gained=added;r.lost=removed;
  array<int,6> tuple={r.fixed,r.cycles,r.consensus,r.maxdepth,r.gained,r.lost};
  auto &v=summaries[group];
  if(v.count==0){v.values=tuple;v.entry=r.entry;}
  else{assert(v.values==tuple); assert(v.entry==r.entry);}
  v.count++;
  return r;
 };
 base=collect(0,std::move(base));
 for(int i=0;i<21;i++) collect(1,examine(es,{i}));
 // Exactly three kinds of unordered incidence-edge pairs.
 int showwitness[5]={0};
 for(int i=0;i<21;i++)for(int j=i+1;j<21;j++){
   auto a=es[i],b=es[j];
   int type;
   if(pair_type(a,b)==1) type=2;
   else{
     // Since the Fano incidence graph has girth six, at most one cross edge exists.
     bool cross=false;
     for(auto e:es) if((e.u==a.u&&e.v==b.v)||(e.u==b.u&&e.v==a.v))cross=true;
     type=cross?3:4;
   }
   auto r=collect(type,examine(es,{i,j}));
   if(!showwitness[type]&&r.lost){
      for(int s=0;s<TOTAL;s++)if(base.basin[s]&&!r.basin[s]){
        cout<<"lost_witness "<<label(type)<<" deleted ("<<a.u<<","<<a.v<<") ("<<b.u<<","<<b.v<<") state "<<s<<"\n";
        showwitness[type]=1;break;
      }
   }
 }
 const array<int,5> expectedCount={1,21,42,84,84};
 const array<array<int,6>,5> expected={{{58,1653,2592,2,0,0},{66,777,3744,6,1152,0},
 {58,533,4960,11,2368,0},{90,376,4032,8,1736,296},{86,427,4512,6,2048,128}}};
 for(int t=0;t<5;t++){
  auto z=summaries[t];assert(z.count==expectedCount[t]);assert(z.values==expected[t]);
  cout<<label(t)<<" cases="<<z.count<<" fixed="<<z.values[0]<<" p2orbits="<<z.values[1]
   <<" consensus="<<z.values[2]<<" maxentry="<<z.values[3]<<" newly_consensus="<<z.values[4]
   <<" consensus_lost="<<z.values[5]<<" entry=[";
  for(int i=0;i<=z.values[3];i++){ cout<<(i?",":"")<<z.entry[i]; }
  cout<<"]\n";
 }
 cout<<"ASSERTIONS PASSED: all 232 graph cases, all 16384 states each, complete consensus-inclusion cutoff\n";
}
