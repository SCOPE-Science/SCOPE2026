// Independent exhaustive zero-field three-color Potts check on finite Apollonian networks.
// All vertex 0 colors are equivalent by global relabeling; multiply counts by three.
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
struct Graph {vector<vector<int>> adj; int edges=0;};
Graph make_graph(int depth) {
  Graph g; g.adj.resize(3);
  vector<array<int,3>> faces{{0,1,2}};
  auto add_edge=[&](int a,int b){g.adj[a].push_back(b);g.adj[b].push_back(a);++g.edges;};
  add_edge(0,1);add_edge(1,2);add_edge(2,0);
  for(int r=0;r<depth;r++){
    vector<array<int,3>> future;
    for(auto f:faces){
      int v=(int)g.adj.size();g.adj.emplace_back();
      for(int u:f)add_edge(v,u);
      future.push_back({f[0],f[1],v});future.push_back({f[1],f[2],v});future.push_back({f[2],f[0],v});
    }
    faces=move(future);
  }
  return g;
}
void exhaustive(int depth){
 auto g=make_graph(depth);int n=(int)g.adj.size();
 if(n>16)throw runtime_error("depth exceeds exhaustive limit");
 vector<int> s(n,0);
 uint64_t states=1;
 for(int i=1;i<n;i++)states*=3;
 int energy=g.edges,minE=energy;
 uint64_t count=0;
 for(uint64_t z=0;z<states;z++){
  if(energy<minE){minE=energy;count=1;}else if(energy==minE)count++;
  if(z+1==states)break;
  for(int u=n-1;u>=1;u--){
   int old=s[u],next=(old+1)%3;
   for(int v:g.adj[u])energy+=int(next==s[v])-int(old==s[v]);
   s[u]=next;
   if(next!=0)break;
  }
 }
 cout<<"depth="<<depth<<" vertices="<<n<<" edges="<<g.edges
  <<" inspected="<<states*3<<" minimum="<<minE<<" degeneracy="<<count*3<<"\n";
 if(depth==0 && (minE!=0||count*3!=6))throw runtime_error("depth 0 mismatch");
 if(depth==1 && (minE!=1||count*3!=36))throw runtime_error("depth 1 mismatch");
 if(depth==2 && (minE!=2||count*3!=72))throw runtime_error("depth 2 mismatch");
 if(depth==3 && (minE!=5||count*3!=216))throw runtime_error("depth 3 mismatch");
}
int main(){for(int d=0;d<=3;d++)exhaustive(d);cout<<"ALL_EXHAUSTIVE_CHECKS_PASS\n";}
