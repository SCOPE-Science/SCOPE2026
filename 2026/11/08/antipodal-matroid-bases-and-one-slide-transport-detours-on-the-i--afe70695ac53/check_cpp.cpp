#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <numeric>
#include <queue>
#include <vector>
#include <map>
#include <set>
using namespace std;
const vector<pair<int,int>> E = {{0,1}, {0,5}, {0,7}, {0,8}, {0,11}, {1,2}, {1,5}, {1,6}, {1,8}, {2,3}, {2,6}, {2,8}, {2,9}, {3,4}, {3,6}, {3,9}, {3,10}, {4,5}, {4,6}, {4,10}, {4,11}, {5,6}, {5,11}, {7,8}, {7,9}, {7,10}, {7,11}, {8,9}, {9,10}, {10,11}};
vector<int> bfs(const vector<vector<int>>&g,int s){
  vector<int> d(g.size(),-1);queue<int> q;q.push(s);d[s]=0;
  while(!q.empty()){int a=q.front();q.pop();for(int b:g[a])
    if(d[b]<0){d[b]=d[a]+1;q.push(b);}}
  return d;
}
int main(){
  vector<vector<int>> g(12);
  for(auto [a,b]:E){g[a].push_back(b);g[b].push_back(a);}
  for(auto &x:g)assert(x.size()==5);
  vector<vector<int>> dist;
  for(int a=0;a<12;a++)dist.push_back(bfs(g,a));
  vector<int> anti(12,-1);
  for(int a=0;a<12;a++){for(int b=0;b<12;b++)if(dist[a][b]==3){
    assert(anti[a]<0);anti[a]=b;} assert(anti[a]>=0);}
  vector<int> bases;
  for(int s=0;s<(1<<12);s++)if(__builtin_popcount((unsigned)s)==3){
    vector<int> ss;
    for(int i=0;i<12;i++)if(s>>i&1)ss.push_back(i);
    set<array<int,3>> signs;
    for(int v=0;v<12;v++)signs.insert({dist[v][ss[0]],dist[v][ss[1]],dist[v][ss[2]]});
    bool resolves=(signs.size()==12);
    bool admissible=true;
    for(int i=0;i<3;i++)for(int j=i+1;j<3;j++) if(anti[ss[i]]==ss[j])admissible=false;
    assert(resolves==admissible);
    if(resolves)bases.push_back(s);
  }
  assert(bases.size()==160);
  vector<vector<int>> ts(160),tj(160);
  for(int a=0;a<160;a++)for(int b=a+1;b<160;b++){
    int x=bases[a]^bases[b];
    if(__builtin_popcount((unsigned)x)!=2)continue;
    tj[a].push_back(b); tj[b].push_back(a);
    int from=bases[a]&x, to=bases[b]&x;
    int u=__builtin_ctz((unsigned)from),v=__builtin_ctz((unsigned)to);
    if(dist[u][v]==1){ts[a].push_back(b);ts[b].push_back(a);}
  }
  for(int i=0;i<160;i++){assert(ts[i].size()==9);assert(tj[i].size()==21);}
  map<int,int> ecc, ecc_jump, hist,detours;
  vector<int> t(3),v(3);
  for(int a=0;a<160;a++){
    vector<int> da=bfs(ts,a),db=bfs(tj,a);
    assert(*min_element(da.begin(),da.end())==0);
    assert(*max_element(db.begin(),db.end())==3);
    ecc[*max_element(da.begin(),da.end())]++;
    ecc_jump[*max_element(db.begin(),db.end())]++;
    int m=0;for(int x=0;x<12;x++)if(bases[a]>>x&1)t[m++]=x;
    for(int b=a+1;b<160;b++){
      int z=0;for(int x=0;x<12;x++)if(bases[b]>>x&1)v[z++]=x;
      vector<int> order={0,1,2};
      int W=100;
      do{int cost=0;for(int i=0;i<3;i++)cost+=dist[t[i]][v[order[i]]];W=min(W,cost);}
      while(next_permutation(order.begin(),order.end()));
      assert(da[b]>=W && da[b]<=W+1);
      hist[da[b]]++;detours[da[b]-W]++;
      int intersect=__builtin_popcount((unsigned)(bases[a]&bases[b]));
      assert(db[b]==3-intersect);
    }
  }
  assert((ecc==map<int,int>({{4,20},{5,120},{6,20}})));
  assert((ecc_jump==map<int,int>({{3,160}})));
  assert((hist==map<int,int>({{1,720},{2,2730},{3,4960},{4,3490},{5,810},{6,10}})));
  assert((detours==map<int,int>({{0,12110},{1,610}})));
  cout<<"PASS C++17: 160 bases; exact independent graph reconstruction; slide 9-regular 720 edges, jump 21-regular 1680 edges\n";
  cout<<"eccentricities: 4:20 5:120 6:20, jump diameter 3; 610 one-slide transport detours among 12720 pairs\n";
  return 0;
}
