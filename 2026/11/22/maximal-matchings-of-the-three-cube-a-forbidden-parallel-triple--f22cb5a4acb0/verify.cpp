// Exhaustive independent implementation for the maximal-matching trace complex of Q3.
// Build: c++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
int main(){
 vector<pair<int,int>> E;
 for(int v=0;v<8;v++)for(int b=0;b<3;b++){
  int u=v^(1<<b);if(v<u)E.emplace_back(v,u);
 }
 sort(E.begin(),E.end()); assert(E.size()==12);
 vector<int> concepts;
 for(int mask=0;mask<4096;mask++){
  int vertex_used=0;bool matching=true;
  for(int i=0;i<12;i++)if(mask&(1<<i)){
   int e=(1<<E[i].first)|(1<<E[i].second);
   if(e&vertex_used)matching=false;
   vertex_used|=e;
  }
  if(!matching)continue;
  bool maximal=true;
  for(int i=0;i<12;i++)if(!(mask&(1<<i))){
   if(!(vertex_used&(1<<E[i].first)) && !(vertex_used&(1<<E[i].second))) maximal=false;
  }
  if(maximal)concepts.push_back(mask);
 }
 assert(concepts.size()==17);
 map<int,int> concept_hist;
 for(int x:concepts)concept_hist[__builtin_popcount((unsigned)x)]++;
 assert(concept_hist[3]==8 && concept_hist[4]==9);
 vector<int> faces;set<int> face_set;
 map<int,int> fvector;
 for(int s=0;s<4096;s++){
  set<int> traces;
  for(int x:concepts)traces.insert(x&s);
  if(traces.size()==(1u<<__builtin_popcount((unsigned)s))){
   faces.push_back(s);face_set.insert(s);fvector[__builtin_popcount((unsigned)s)]++;
  }
 }
 assert(fvector[0]==1 && fvector[1]==12 && fvector[2]==42 && fvector[3]==32 && fvector.size()==4);
 map<int,int> facet_hist;
 for(int s:faces){
  bool maximal=true;
  for(int i=0;i<12;i++)if(!(s&(1<<i)) && face_set.count(s|(1<<i)))maximal=false;
  if(maximal)facet_hist[__builtin_popcount((unsigned)s)]++;
 }
 assert(facet_hist[2]==6 && facet_hist[3]==32 && facet_hist.size()==2);
 // Structural law: shattering iff matching of <=3 edges with no 3 parallel edges.
 for(int s=0;s<4096;s++){
  int used=0; bool match=true;int dir[3]={0,0,0};
  for(int i=0;i<12;i++)if(s>>i&1){
   int e=(1<<E[i].first)|(1<<E[i].second);
   if(e&used)match=false;
   used|=e;
   for(int b=0;b<3;b++)if((E[i].first^E[i].second)==(1<<b))dir[b]++;
  }
  bool predicted=match && __builtin_popcount((unsigned)s)<=3 && max({dir[0],dir[1],dir[2]})<=2;
  assert((face_set.count(s)!=0)==predicted);
 }
 vector<int> pairs,triples;
 for(int x:faces){
  if(__builtin_popcount((unsigned)x)==2)pairs.push_back(x);
  if(__builtin_popcount((unsigned)x)==3)triples.push_back(x);
 }
 map<int,int> pos;for(int i=0;i<(int)pairs.size();i++)pos[pairs[i]]=i;
 vector<uint64_t> columns;
 for(int t:triples){
  uint64_t boundary=0;
  for(int i=0;i<12;i++)if(t>>i&1)boundary^=(uint64_t(1)<<pos.at(t^(1<<i)));
  columns.push_back(boundary);
 }
 uint64_t pivot[42]={};int rank=0;
 for(auto col:columns){
  uint64_t x=col;
  while(x){
   int j=63-__builtin_clzll(x);
   if(pivot[j])x^=pivot[j];
   else{pivot[j]=x;rank++;break;}
  }
 }
 assert(rank==25);
 cout<<"cube_edges=12 maximal_matchings=17 sizes=(3:8,4:9)\n";
 cout<<"shattered_coefficients=1,12,42,32; facets=(2:6,3:32)\n";
 cout<<"structural_test_all_4096_supports=PASS boundary2_F2_rank=25\n";
}
