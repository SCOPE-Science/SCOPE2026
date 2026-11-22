// Standalone exhaustive check using the conventional Pappus LCF presentation.
// Compile: c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
constexpr int V=18;
using Edge=pair<int,int>;
int main(){
  int shift[6]={5,7,-7,7,-7,-5};
  vector<Edge> ed;
  auto add=[&](int a,int b){if(a>b)swap(a,b); if(a!=b) ed.push_back({a,b});};
  for(int i=0;i<V;++i){add(i,(i+1)%V);add(i,(i+shift[i%6]+V)%V);}
  sort(ed.begin(),ed.end());ed.erase(unique(ed.begin(),ed.end()),ed.end());
  assert(ed.size()==27);
  array<uint32_t,V> adj{};
  for(auto [a,b]:ed){adj[a]|=1u<<b;adj[b]|=1u<<a;}
  for(auto x:adj)assert(__builtin_popcount(x)==3);
  vector<array<int,5>> combs;
  for(int a=0;a<V;++a)for(int b=a+1;b<V;++b)for(int c=b+1;c<V;++c)
  for(int d=c+1;d<V;++d)for(int e=d+1;e<V;++e)combs.push_back({a,b,c,d,e});
  assert(combs.size()==8568);
  auto count_dominating=[&](const vector<int>& removed){
    auto alive=adj;
    for(int j:removed){auto [a,b]=ed[j];alive[a]&=~(1u<<b);alive[b]&=~(1u<<a);}
    uint32_t close[V];for(int i=0;i<V;++i)close[i]=alive[i]|(1u<<i);
    int n=0;for(const auto &s:combs){
      if((close[s[0]]|close[s[1]]|close[s[2]]|close[s[3]]|close[s[4]])==((1u<<V)-1))++n;
    }return n;
  };
  assert(count_dominating({})==18);
  int counts[4]={0,0,0,0};int stars=0,matchings=0;
  for(int a=0;a<27;++a){if(count_dominating({a})==0)++counts[1];
    for(int b=a+1;b<27;++b){if(count_dominating({a,b})==0)++counts[2];
      for(int c=b+1;c<27;++c){if(count_dominating({a,b,c})!=0)continue;
        ++counts[3];int degree[V]={};
        for(int j:{a,b,c}){degree[ed[j].first]++;degree[ed[j].second]++;}
        int maximum=*max_element(degree,degree+V);
        if(maximum==3)++stars;
        else {assert(maximum==1);++matchings;}
      }
    }
  }
  assert(counts[1]==0 && counts[2]==0 && counts[3]==171);
  assert(stars==18 && matchings==153);
  cout<<"vertices=18 edges=27 gamma=5 min_dom_sets=18\n"
      <<"bondage_1=0 bondage_2=0 bondage_3=171\n"
      <<"stars=18 disjoint_three_edge_matchings=153\n";
}
