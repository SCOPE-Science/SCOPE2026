// Exact finite distance certificate for switch reconfiguration of perfect matchings
// in the nine-by-nine crown graph.
// Build: c++ -std=c++17 -O3 verify_crown_switch.cpp -o verify_crown_switch
// Run: ./verify_crown_switch
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
static constexpr int N=9;
using Perm=array<unsigned char,N>;
static uint64_t key(const Perm &p){uint64_t r=0;for(int x:p)r=(r<<4)|x;return r;}
static string cycle_type(const Perm &p){
  array<int,N> visited{};vector<int> sizes;
  for(int i=0;i<N;i++)if(!visited[i]){
    int j=i,len=0;do{visited[j]=1;++len;j=p[j];}while(!visited[j]);sizes.push_back(len);
  }
  sort(sizes.begin(),sizes.end());string name;
  for(int x:sizes){if(!name.empty())name+='.';name+=to_string(x);}return name;
}
static Perm inverse(const Perm&p){Perm q{};for(int i=0;i<N;i++)q[p[i]]=i;return q;}
int main(){
  vector<Perm>states;Perm p{};iota(p.begin(),p.end(),0);
  do{bool deranged=true;for(int i=0;i<N;i++)if(p[i]==i){deranged=false;break;}if(deranged)states.push_back(p);}while(next_permutation(p.begin(),p.end()));
  assert(states.size()==133496);
  unordered_map<uint64_t,int>index;index.reserve(states.size()*2);
  for(int i=0;i<(int)states.size();i++)assert(index.emplace(key(states[i]),i).second);
  vector<vector<int>>adj(states.size());map<int,int>degrees;long long degree_sum=0;
  map<string,int>rep,cycle_count;
  for(int i=0;i<(int)states.size();i++){
    const auto ty=cycle_type(states[i]);if(!rep.count(ty))rep[ty]=i;cycle_count[ty]++;
    Perm q=states[i];for(int a=0;a<N;a++)for(int b=a+1;b<N;b++){
      swap(q[a],q[b]);
      if(q[a]!=a&&q[b]!=b){auto it=index.find(key(q));assert(it!=index.end());adj[i].push_back(it->second);}
      swap(q[a],q[b]);
    }
    sort(adj[i].begin(),adj[i].end());assert(unique(adj[i].begin(),adj[i].end())==adj[i].end());
    degrees[adj[i].size()]++;degree_sum+=adj[i].size();
    int twos=0;for(size_t t=0;t<ty.size();t++)if(ty[t]=='2'&&(t==0||ty[t-1]=='.'))twos++;
    assert((int)adj[i].size()==27+twos);
  }
  for(int i=0;i<(int)adj.size();i++)for(int j:adj[i]) assert(binary_search(adj[j].begin(),adj[j].end(),i));
  assert(degree_sum==3671136);
  assert((degrees==map<int,int>{{27,80864},{28,41040},{29,9072},{30,2520}}));
  struct Expected {int count,degree,ecc,opposite;};
  const map<string,Expected> expected={
    {"2.2.2.3",{2520,30,9,0}},
    {"2.2.5",{9072,29,8,0}},
    {"2.3.4",{15120,28,9,0}},
    {"2.7",{25920,28,8,0}},
    {"3.3.3",{2240,27,10,1}},
    {"3.6",{20160,27,9,0}},
    {"4.5",{18144,27,8,0}},
    {"9",{40320,27,8,0}}
  };
  assert(rep.size()==expected.size());
  int all_visited=0;long long diametral_pairs=0;
  cout<<"states="<<states.size()<<" edges="<<degree_sum/2<<"\n";
  for(auto [ty,start]:rep){
    auto e=expected.at(ty);assert(cycle_count[ty]==e.count);
    assert((int)adj[start].size()==e.degree);
    vector<int>distance(states.size(),-1);queue<int>q;q.push(start);distance[start]=0;
    int reached=0,ecc=0,antipodes=0;vector<int>shell(16);
    while(!q.empty()){
      int u=q.front();q.pop();++reached;++shell[distance[u]];ecc=max(ecc,distance[u]);
      for(int v:adj[u])if(distance[v]<0){distance[v]=distance[u]+1;q.push(v);}
    }
    assert(reached==(int)states.size());all_visited++;
    assert(ecc==e.ecc);
    for(int d:distance)if(d==10){++antipodes;}
    assert(antipodes==e.opposite);
    if(e.opposite==1){int target=index.at(key(inverse(states[start])));assert(distance[target]==10);diametral_pairs=e.count/2;}
    cout<<ty<<" count="<<e.count<<" degree="<<e.degree<<" ecc="<<ecc<<" distance10="<<antipodes<<" shells=";
    for(int i=0;i<=ecc;i++)cout<<(i?",":"")<<shell[i];cout<<"\n";
  }
  assert(all_visited==8&&diametral_pairs==1120);
  cout<<"radius=8 diameter=10 diametral_pairs=1120 all_checks_passed\n";
}
