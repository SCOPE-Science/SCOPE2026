#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
  constexpr int n=24;
  array<set<int>,n> edges{};
  const array<int,3> offset={12,7,-7};
  for(int i=0;i<n;i++) {
    int j=(i+1)%n;
    edges[i].insert(j);edges[j].insert(i);
    j=(i+offset[i%3]+n)%n;
    edges[i].insert(j);edges[j].insert(i);
  }
  array<uint32_t,n> closed{};
  int edgeCount=0;
  for(int i=0;i<n;i++) {
    assert(edges[i].size()==3);
    closed[i]=1u<<i;
    for(int v:edges[i]) closed[i]|=1u<<v;
    edgeCount+=int(edges[i].size());
  }
  assert(edgeCount/2==36);
  // Full search of the only cardinality layers not excluded by 5k>=48.
  array<int,2> counts={0,0};
  vector<uint32_t> codes;
  for(uint32_t c=0;c<(1u<<n);c++) {
    int k=__builtin_popcount(c);
    if(k!=10 && k!=11)continue;
    bool valid=true;
    array<uint32_t,n> sig{};
    for(int v=0;v<n;v++) {
      sig[v]=c&closed[v];
      if(!sig[v]) {valid=false;break;}
      for(int u=0;u<v;u++) if(sig[u]==sig[v]) {valid=false;break;}
      if(!valid)break;
    }
    if(valid) {
      counts[k-10]++;
      if(k==11)codes.push_back(c);
    }
  }
  assert(counts[0]==0 && counts[1]==384);
  unordered_map<uint32_t,int> index;
  for(int i=0;i<(int)codes.size();i++)index[codes[i]]=i;
  vector<set<int>> jump(codes.size()), slide(codes.size());
  for(int a=0;a<(int)codes.size();a++) {
    uint32_t c=codes[a];
    for(int i=0;i<n;i++)if((c>>i)&1u)
      for(int j=0;j<n;j++)if(!((c>>j)&1u)) {
        auto it=index.find(c^(1u<<i)^(1u<<j));
        if(it==index.end()) continue;
        int b=it->second;
        jump[a].insert(b);
        if(edges[i].count(j))slide[a].insert(b);
      }
  }
  auto profile=[&](const vector<set<int>>& graph) {
    map<int,int> componentSizes;
    map<pair<int,int>,int> sizeEdgeDistribution;
    map<int,int> degreeDistribution;
    int edgeTotal=0;
    vector<char> seen(graph.size(),false);
    for(int i=0;i<(int)graph.size();i++) {
      degreeDistribution[(int)graph[i].size()]++;
      edgeTotal+=graph[i].size();
      if(seen[i])continue;
      vector<int> component={i};seen[i]=true;
      for(int k=0;k<(int)component.size();k++) {
        for(int j:graph[component[k]])if(!seen[j]) {
          seen[j]=true;component.push_back(j);
        }
      }
      int edgeSum=0;
      for(int v:component)edgeSum+=graph[v].size();
      int sz=component.size();
      componentSizes[sz]++;
      sizeEdgeDistribution[{sz,edgeSum/2}]++;
    }
    return make_tuple(componentSizes,sizeEdgeDistribution,degreeDistribution,edgeTotal/2);
  };
  auto [jsz, jse, jdeg, jedges]=profile(jump);
  auto [ssz, sse, sdeg, sedges]=profile(slide);
  assert((jsz==map<int,int>({{1,176},{2,16},{11,16}})));
  assert((jse==map<pair<int,int>,int>({{{1,0},176},{{2,1},16},{{11,16},16}})));
  assert((jdeg==map<int,int>({{0,176},{1,96},{3,32},{4,64},{6,16}})));
  assert(jedges==272);
  assert((ssz==map<int,int>({{1,320},{2,32}})));
  assert((sse==map<pair<int,int>,int>({{{1,0},320},{{2,1},32}})));
  assert((sdeg==map<int,int>({{0,320},{1,64}})));
  assert(sedges==32);
  cout<<"VERIFY_OK mcgee_identifying_minimum=11 codes=384 jump_edges=272 jump_components=208 jump_component_types=176K1+16K2+16H11 slide_edges=32 slide_components=352 slide_component_types=320K1+32K2\n";
}
