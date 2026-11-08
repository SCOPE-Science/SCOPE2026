// Direct cyclic Gray-code enumeration and subsequence inversions for Q4.
// Build: g++ -O2 -std=c++17 check_inversions.cpp -o check_inversions
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stdexcept>
#include <unordered_map>
#include <vector>
using namespace std;
using U=uint64_t;
array<array<int,16>,16> edgeNo;
vector<array<int,16>> paths;
vector<U> masks;
array<int,16> path_{};
void dfs(int k,int seen){
  if(k==16){
    if (__builtin_popcount((unsigned)(path_[15]^path_[0]))!=1) return;
    if(path_[1]>path_[15]) return; // One of two orientations at start zero.
    paths.push_back(path_);
    U mask=0;
    for(int i=0;i<16;i++) mask|=U(1)<<edgeNo[path_[i]][path_[(i+1)%16]];
    masks.push_back(mask);
    return;
  }
  for(int bit=0;bit<4;bit++){
    int v=path_[k-1]^(1<<bit);
    if(!(seen>>v&1)){
      path_[k]=v;dfs(k+1,seen|(1<<v));
    }
  }
}
int main(){
  for(auto& a:edgeNo)a.fill(-1);
  int e=0;
  for(int v=0;v<16;v++)for(int bit=0;bit<4;bit++){
    int w=v^(1<<bit);if(v<w){edgeNo[v][w]=edgeNo[w][v]=e++;}
  }
  if(e!=32)throw runtime_error("edges");
  path_[0]=0;dfs(1,1);
  map<U,int> id;
  for(int i=0;i<(int)masks.size();i++)if(!id.emplace(masks[i],i).second)throw runtime_error("duplicate cycle");
  if(id.size()!=1344)throw runtime_error("cycle count");
  vector<set<int>> g(masks.size());
  for(size_t ix=0;ix<paths.size();ix++){
    auto p=paths[ix];
    for(int i=0;i<16;i++)for(int j=i+2;j<16;j++){
      if(i==0&&j==15)continue;
      int a=p[i],b=p[i+1],c=p[j],d=p[(j+1)%16];
      if(__builtin_popcount((unsigned)(a^c))!=1||__builtin_popcount((unsigned)(b^d))!=1)continue;
      // Two removed opposite face edges; the new edges reconnect one cycle.
      if((a^b)!=(c^d)||(a^c)!=(b^d))continue;
      U nxt=masks[ix];
      int old1=edgeNo[a][b],old2=edgeNo[c][d],new1=edgeNo[a][c],new2=edgeNo[b][d];
      nxt ^= (U(1)<<old1)|(U(1)<<old2)|(U(1)<<new1)|(U(1)<<new2);
      auto it=id.find(nxt);
      if(it==id.end())throw runtime_error("inversion missing from Hamilton cycles");
      g[ix].insert(it->second);
    }
  }
  for(int i=0;i<(int)g.size();i++)for(auto j:g[i])if(!g[j].count(i))throw runtime_error("asymmetric flip");
  map<int,int> degdist,comps,eccdist;
  long long degree_sum=0;
  for(const auto& v:g){degdist[int(v.size())]++;degree_sum+=v.size();}
  vector<char> seen(g.size(),0);int rad=100,diam=0;
  for(int s=0;s<(int)g.size();s++)if(!seen[s]){
    vector<int> comp; queue<int> q;q.push(s);seen[s]=1;
    while(!q.empty()){
      int v=q.front();q.pop();comp.push_back(v);
      for(int w:g[v])if(!seen[w])seen[w]=1,q.push(w);
    }
    comps[int(comp.size())]++;
    if(comp.size()==1)continue;
    for(int v:comp){
      vector<int> dist(g.size(),-1);dist[v]=0;queue<int> z;z.push(v);int far=0,cnt=0;
      while(!z.empty()){
        int u=z.front();z.pop();cnt++;far=max(far,dist[u]);
        for(int w:g[u])if(dist[w]<0)dist[w]=dist[u]+1,z.push(w);
      }
      if(cnt!=(int)comp.size())throw runtime_error("BFS incomplete");
      eccdist[far]++;rad=min(rad,far);diam=max(diam,far);
    }
  }
  auto print=[](const char* title, const map<int,int>& dict){
    cout<<title<<" ";for(auto [k,v]:dict)cout<<k<<":"<<v<<" ";cout<<"\n";
  };
  cout<<"hamilton_cycles "<<masks.size()<<"\n";
  cout<<"switch_edges "<<degree_sum/2<<"\n";
  print("degree_histogram",degdist);print("component_histogram",comps);
  cout<<"giant_radius "<<rad<<"\n"<<"giant_diameter "<<diam<<"\n";
  print("eccentricity_histogram",eccdist);
  if(degree_sum!=3840 || comps!=map<int,int>{{1,240},{1104,1}} || rad!=10 || diam!=12 || eccdist!=map<int,int>{{10,96},{11,192},{12,816}})
    throw runtime_error("unanticipated census");
}
