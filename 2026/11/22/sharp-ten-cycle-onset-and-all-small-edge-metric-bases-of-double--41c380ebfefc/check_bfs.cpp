// Exhaustive finite certificate for edge-to-vertex resolving sets in DP(n,1).
// Uses breadth-first shortest paths and pairwise edge-signature collisions.
// Compile: g++ -std=c++17 -O2 check_bfs.cpp -o check_bfs
// Run: ./check_bfs
#include <algorithm>
#include <array>
#include <iostream>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;

int main() {
  cout << "n\tvertices\tedges\tpairs\ttriples\tquadruples\n";
  for (int n=3; n<=12; ++n) {
    const int N=4*n;
    set<pair<int,int>> edge_set;
    auto add=[&](int a,int b){if(a>b) swap(a,b);edge_set.insert({a,b});};
    // Consecutive blocks x_0..x_{n-1}, u_0.., v_0.., y_0...
    for (int i=0;i<n;++i) {
      int j=(i+1)%n;
      add(i,j);add(3*n+i,3*n+j);
      add(i,n+i);add(2*n+i,3*n+i);
      add(n+i,2*n+j);add(2*n+i,n+j);
    }
    vector<pair<int,int>> E(edge_set.begin(),edge_set.end());
    if ((int)E.size()!=6*n) return 2;
    vector<vector<int>> adj(N);
    for(auto [u,v]:E){adj[u].push_back(v);adj[v].push_back(u);}
    for(auto &a:adj) if(a.size()!=3) return 3;
    vector<vector<int>> D(N,vector<int>(N,N+1));
    for(int s=0;s<N;++s){
      queue<int> q;D[s][s]=0;q.push(s);
      while(!q.empty()){
        int u=q.front();q.pop();
        for(int v:adj[u]) if(D[s][v]>D[s][u]+1){D[s][v]=D[s][u]+1;q.push(v);}
      }
      for(int v=0;v<N;++v) if(D[s][v]>N)return 4;
    }
    vector<vector<int>> code(N,vector<int>(E.size()));
    for(int s=0;s<N;++s) for(int j=0;j<(int)E.size();++j){
      auto [a,b]=E[j];code[s][j]=min(D[s][a],D[s][b]);
    }
    auto resolves=[&](int a,int b,int c,int d){
      for(int i=0;i<(int)E.size();++i) for(int j=i+1;j<(int)E.size();++j){
        if (code[a][i]!=code[a][j] || code[b][i]!=code[b][j]) continue;
        if (c>=0 && code[c][i]!=code[c][j])continue;
        if (d>=0 && code[d][i]!=code[d][j])continue;
        return false;
      }
      return true;
    };
    long long pairs=0,triples=0,quads=0;
    for(int a=0;a<N;++a) for(int b=a+1;b<N;++b){
      pairs+=resolves(a,b,-1,-1);
      for(int c=b+1;c<N;++c){
        triples+=resolves(a,b,c,-1);
        for(int d=c+1;d<N;++d)quads+=resolves(a,b,c,d);
      }
    }
    cout<<n<<'\t'<<N<<'\t'<<E.size()<<'\t'<<pairs<<'\t'<<triples<<'\t'<<quads<<'\n';
  }
}
