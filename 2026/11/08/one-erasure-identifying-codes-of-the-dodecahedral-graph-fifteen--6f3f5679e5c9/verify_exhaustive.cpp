#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
// Exhaustive enumeration of the 2^20 subsets of the labeled GP(10,2).
int main(){
 array<unsigned,20> adj{};
 auto add=[&](int a,int b){adj[a]|=1u<<b;adj[b]|=1u<<a;};
 for(int i=0;i<10;i++){
  add(i,(i+1)%10);add(i,i+10);add(i+10,10+(i+2)%10);
 }
 vector<unsigned> conditions;
 array<unsigned,20> closed{};
 for(int i=0;i<20;i++){closed[i]=adj[i]|(1u<<i);conditions.push_back(closed[i]);}
 for(int i=0;i<20;i++)for(int j=i+1;j<20;j++)conditions.push_back(closed[i]^closed[j]);
 assert(conditions.size()==210);
 int best=21;vector<unsigned> codes;
 for(unsigned m=0;m<(1u<<20);m++){
  int s=__builtin_popcount(m);
  if(s>best)continue;
  bool qualifies=true;
  for(unsigned condition:conditions){if(__builtin_popcount(m&condition)<2){qualifies=false;break;}}
  if(!qualifies)continue;
  if(s<best){best=s;codes.clear();}
  codes.push_back(m);
 }
 assert(best==12 && codes.size()==15);
 map<int,int> intersections;
 for(unsigned i=0;i<codes.size();i++)for(unsigned j=i+1;j<codes.size();j++)intersections[__builtin_popcount(codes[i]&codes[j])]++;
 assert(intersections[6]==60 && intersections[8]==45 && intersections.size()==2);
 const array<pair<int,int>,15> labels={{{0,1},{2,3},{3,5},{0,4},{2,5},{1,4},{3,4},{1,5},{0,5},{2,4},{1,2},{4,5},{0,2},{0,3},{1,3}}};
 for(int i=0;i<15;i++)for(int j=i+1;j<15;j++){
  bool disjoint=labels[i].first!=labels[j].first&&labels[i].first!=labels[j].second&&labels[i].second!=labels[j].first&&labels[i].second!=labels[j].second;
  assert((__builtin_popcount(codes[i]&codes[j])==8)==disjoint);
 }
 cout<<"minimum_one_erasure_identifying_size="<<best<<"\n";
 cout<<"number_optimal_codes="<<codes.size()<<"\n";
 cout<<"intersection_spectrum: 6->60 8->45\n";
 cout<<"intersection_8_graph=KG(6,2); one_token_jumps=0\n";
 cout<<"complete_2power20_enumeration=PASS\n";
}
