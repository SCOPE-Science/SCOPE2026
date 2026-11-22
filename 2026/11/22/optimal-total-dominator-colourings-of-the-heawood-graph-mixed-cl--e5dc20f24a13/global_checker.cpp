// Exhaustive labelled-vertex partition enumerator for total-dominator colourings
// of the Fano point-line incidence graph. C++17, no nonstandard libraries.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int V=14, FULL=(1<<V)-1;
array<int,V> adj{};
array<int,8> blocks{};
array<int,V> class_of{};
map<int,long long> valid_by_k;
vector<array<uint16_t,8>> optimum;

bool is_tdc(int k){
  for(int u=0;u<V;++u){
    bool dominated=false;
    for(int j=0;j<k;++j){
      if((blocks[j]&adj[u])==blocks[j]){dominated=true;break;}
    }
    if(!dominated)return false;
  }
  return true;
}
void enumerate_partitions(int x,int k,int target){
  if(k>target||k+(V-x)<target)return;
  if(x==V){
    if(k!=target||!is_tdc(k))return;
    valid_by_k[k]++;
    if(k==8){
      array<uint16_t,8> z{};
      for(int i=0;i<8;i++)z[i]=(uint16_t)blocks[i];
      sort(z.begin(),z.end());
      optimum.push_back(z);
    }
    return;
  }
  for(int j=0;j<=k&&j<target;++j){
    if(j<k && (adj[x]&blocks[j]))continue;
    blocks[j]|=1<<x;
    enumerate_partitions(x+1,max(k,j+1),target);
    blocks[j]^=1<<x;
  }
}
int main(){
  for(int j=0;j<7;++j){
    for(int d: {0,1,3}){
      int i=(j+d)%7;
      adj[i]|=1<<(j+7);
      adj[j+7]|=1<<i;
    }
  }
  for(int k=1;k<=8;++k){enumerate_partitions(0,0,k);}
  assert(valid_by_k.size()==1&&valid_by_k[8]==2751);
  assert(optimum.size()==2751);
  map<array<uint16_t,8>,int> lookup;
  for(int i=0;i<(int)optimum.size();++i)assert(lookup.emplace(optimum[i],i).second);
  array<int,3> mixed={};
  vector<set<int>> edges(optimum.size());
  for(int i=0;i<(int)optimum.size();++i){
    auto z=optimum[i];
    int m=0;
    for(int c=0;c<8;++c){
      if((z[c]&127)&&(z[c]>>7))++m;
      if(__builtin_popcount(z[c])<=1)continue;
      for(int v=0;v<V;++v){
        if(!(z[c]&(1<<v)))continue;
        for(int d=0;d<8;++d){
          if(c==d)continue;
          auto zz=z;
          zz[c]^=1<<v;
          zz[d]|=1<<v;
          sort(zz.begin(),zz.end());
          auto jt=lookup.find(zz);
          if(jt!=lookup.end())edges[i].insert(jt->second);
        }
      }
    }
    assert(m<=2);mixed[m]++;
  }
  assert(mixed[0]==2401 && mixed[1]==322 && mixed[2]==28);
  long long e=0;map<int,int> degrees;
  for(int i=0;i<(int)optimum.size();++i){
    for(int j:edges[i])assert(edges[j].count(i)==1);
    e+=(int)edges[i].size();degrees[(int)edges[i].size()]++;
  }
  assert(e%2==0);e/=2;
  assert(e==11662);
  vector<int> visited(optimum.size());map<int,int> components;
  for(int i=0;i<(int)optimum.size();++i){
    if(visited[i])continue;
    queue<int> q;q.push(i);visited[i]=1;int z=0;
    while(!q.empty()){
      int u=q.front();q.pop();++z;
      for(int w:edges[u])if(!visited[w]){visited[w]=1;q.push(w);}
    }
    components[z]++;
  }
  assert((components==map<int,int>({{1,21},{966,1},{1764,1}})));
  assert((degrees==map<int,int>({{0,21},{2,56},{5,224},{6,476},{7,168},{10,1806}})));
  cout<<"No total-dominator partitions with <=7 nonempty colors.\n";
  cout<<"8-color partitions = "<<optimum.size()<<", mixed-class distribution = "
      <<mixed[0]<<","<<mixed[1]<<","<<mixed[2]<<"\n";
  cout<<"Single-vertex moves = "<<e<<"; components:";
  for(auto [sz,count]:components)cout<<" ("<<sz<<" x "<<count<<")";
  cout<<"\nDegrees:";
  for(auto [d,count]:degrees)cout<<" ("<<d<<":"<<count<<")";
  cout<<"\nPASS\n";
}
