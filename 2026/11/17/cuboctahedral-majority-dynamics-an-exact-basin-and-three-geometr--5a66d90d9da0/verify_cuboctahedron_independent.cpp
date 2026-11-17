// Exhaustive finite-state verification for tie-retaining majority on L(Q3).
// Independent adjacency-mask and functional-map calculation; no external dependencies.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
static constexpr int N = 12, STATES = 1<<N;
static constexpr array<uint16_t,N> mask = {30,101,771,177,1289,202,2594,3112,1556,2372,2448,1728};
int main() {
  array<pair<int,int>,12> cube_edges{};
  int t=0;
  for (int v=0;v<8;v++) for(int b=0;b<3;b++) {
    int w=v^(1<<b);if(v<w) cube_edges[t++]={v,w};
  }
  assert(t==12);
  for(int i=0;i<N;i++) {
    uint16_t actual=0;
    for(int j=0;j<N;j++) if(i!=j) {
      auto [a,b]=cube_edges[i];auto [c,d]=cube_edges[j];
      if (a==c || a==d || b==c || b==d) actual|=(1u<<j);
    }
    assert(mask[i]==actual && __builtin_popcount(actual)==4);
  }
  vector<int> successor(STATES),indegree(STATES),entrance(STATES,-1),future_period(STATES,-1);
  for(int x=0;x<STATES;x++) {
    int y=0;
    for(int v=0;v<N;v++) {
      int n=__builtin_popcount((unsigned)(x&mask[v]));
      bool bit=(x>>v)&1;
      bool nxt=(n==4 || n==3 || (n==2 && bit));
      if(nxt)y|=(1<<v);
    }
    successor[x]=y;indegree[y]++;
  }
  auto F=[&](int x){return successor[x];};
  int fixed=0,pair_states=0;
  map<pair<int,int>,int> by_time_period;
  map< vector<int>, int > basins;
  int max_entrance=-1;
  for(int x=0;x<STATES;x++) {
    bool periodic=(F(F(x))==x);
    if(periodic){if(F(x)==x)fixed++; else pair_states++;}
    int cur=x,depth=0;
    while(F(F(cur))!=cur) {
      cur=F(cur);depth++;
      assert(depth<=4);
    }
    int p=(F(cur)==cur?1:2);
    by_time_period[{depth,p}]++;
    vector<int> orbit{cur};
    if(p==2)orbit.push_back(F(cur));
    sort(orbit.begin(),orbit.end());
    basins[orbit]++;
    entrance[x]=depth;future_period[x]=p;
    max_entrance=max(max_entrance,depth);
    assert(F(F(F(F(F(F(x))))))==F(F(F(F(x)))));
  }
  assert(fixed==146 && pair_states==40 && max_entrance==4);
  assert(by_time_period[make_pair(0,1)]==146);
  assert(by_time_period[make_pair(0,2)]==40);
  assert(by_time_period[make_pair(1,1)]==1606);
  assert(by_time_period[make_pair(2,1)]==1200);
  assert(by_time_period[make_pair(3,1)]==1008);
  assert(by_time_period[make_pair(4,1)]==96);
  assert(by_time_period.size()==6);
  map<int,int> fixed_basin_sizes, two_basin_sizes;
  for(auto& [key,count]:basins){
    if(key.size()==1)fixed_basin_sizes[count]++;
    else{
      assert(key.size()==2 && count==2);
      two_basin_sizes[count]++;
      assert(indegree[key[0]]==1 && indegree[key[1]]==1);
    }
  }
  assert((fixed_basin_sizes==map<int,int>{{1,8},{5,12},{6,24},{8,48},{10,24},{11,12},{64,16},{1032,2}}));
  assert(two_basin_sizes[2]==20 && two_basin_sizes.size()==1);
  int w=348;assert(entrance[w]==4);
  cout<<"EDGE_MASKS_FROM_LQ3_VALID=YES\n";
  cout<<"TESTED_ALL_4096_STATES=YES FIXED="<<fixed<<" PRIMITIVE_2="<<pair_states/2<<"\n";
  cout<<"TIME_PERIOD_CELLS:";
  for (auto [k,c]:by_time_period)cout<<" ("<<k.first<<","<<k.second<<")="<<c;
  cout<<"\nFIXED_BASINS:";for(auto [k,c]:fixed_basin_sizes)cout<<" "<<k<<":"<<c;
  cout<<"\nTWO_CYCLE_BASINS:";for(auto [k,c]:two_basin_sizes)cout<<" "<<k<<":"<<c;
  cout<<"\nF6_EQUALS_F4=YES MAX_ENTRANCE="<<max_entrance<<" T4_WITNESS="<<w<<"\n";
  cout<<"ALL_TWO_CYCLE_STATES_INDEGREE_ONE=YES\nINDEPENDENT_CENSUS_PASS\n";
}
