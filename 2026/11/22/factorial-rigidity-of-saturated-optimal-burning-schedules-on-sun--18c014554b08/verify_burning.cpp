#include <iostream>
#include <vector>
#include <array>
#include <queue>
#include <cstdint>
#include <cassert>
using namespace std;
struct Case {
 int n,k,N; vector<vector<int>> distance; vector<vector<uint64_t>> ball;
 uint64_t full; unsigned long long count=0; array<int,8> seq{};
 Case(int n_,int k_):n(n_),k(k_),N(2*n_),distance(N,vector<int>(N,1000)),ball(k_,vector<uint64_t>(N,0)),full((1ULL<<N)-1){
  vector<vector<int>> adj(N);auto edge=[&](int u,int v){adj[u].push_back(v);adj[v].push_back(u);};
  for(int i=0;i<n;i++){edge(i,(i+1)%n);edge(i,n+i);}
  for(int u=0;u<N;u++){queue<int> Q; Q.push(u);distance[u][u]=0;
   while(!Q.empty()){int x=Q.front();Q.pop();for(int y:adj[x])if(distance[u][y]==1000){distance[u][y]=distance[u][x]+1;Q.push(y);}}
  }
  for(int t=0;t<k;t++)for(int u=0;u<N;u++)for(int v=0;v<N;v++)if(distance[u][v]<=k-1-t)ball[t][u]|=1ULL<<v;
 }
 void dfs(int t,uint64_t covered){
  if(t==k){if(covered==full)count++;return;}
  for(int v=0;v<N;v++){
   bool ok=true;for(int j=0;j<t;j++)if(distance[seq[j]][v]<t-j){ok=false;break;}
   if(!ok)continue;
   seq[t]=v;dfs(t+1,covered|ball[t][v]);
  }
 }
};
int main(){
 for(auto [n,k,expected]:{array<int,3>{5,3,20},{10,4,120},{17,5,816}}){
  Case c(n,k);c.dfs(0,0);cout<<"n="<<n<<" k="<<k<<" full-schedule-count="<<c.count<<" target="<<expected<<"\n";
  if(c.count!=(unsigned)expected)return 1;
 }
}
