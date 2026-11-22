#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
int main(){
  // The 21 flags of the Fano plane form the vertices of its Levi line graph.
  vector<pair<int,int>> edges;
  for(int j=0;j<7;j++){
    for(int p : {j,(j+1)%7,(j+3)%7}) edges.push_back({p,7+j});
  }
  assert(edges.size()==21);
  array<uint32_t,21> neighbours{};
  for(int i=0;i<21;i++) for(int j=0;j<21;j++){
    if(i!=j && (edges[i].first==edges[j].first || edges[i].second==edges[j].second))
      neighbours[i]|=1u<<j;
  }
  for(auto n:neighbours) assert(__builtin_popcount(n)==4);
  array<int,22> successes{};map<pair<int,int>,int> rounds;
  array<int,7> triple_time{}; // rounds 0..6 for 3-site successes
  const uint32_t FULL=(1u<<21)-1;
  for(uint32_t s=0;s<=FULL;s++){
    uint32_t state=s;int t=0;
    for(;;){
      uint32_t next=0;
      for(int i=0;i<21;i++){
        if(!(state&(1u<<i)) && __builtin_popcount(state&neighbours[i])>=2)
          next|=1u<<i;
      }
      if(!next) break;
      state|=next;t++;
      assert(t<=21);
    }
    if(state==FULL){
      int k=__builtin_popcount(s);successes[k]++;rounds[{k,t}]++;
      if(k==3){assert(t>=0 && t<=6);triple_time[t]++;}
    }
    if(s==FULL) break;
  }
  cout<<"3-seed times:";
  for(int i=0;i<7;i++) cout<<' '<<triple_time[i];
  cout<<"\nsuccess-by-cardinality:";
  for(int k=0;k<=21;k++) cout<<' '<<successes[k];
  cout<<"\nmax-rounds:";
  int max_t=0;for(auto [p,num]:rounds) max_t=max(max_t,p.second);
  cout<<max_t<<'\n';
  return 0;
}
