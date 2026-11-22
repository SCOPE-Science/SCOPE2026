// Direct edge-geodesic exhaustive verification for one-edge-deleted complete bipartite graphs.
// C++17: g++ -O3 -std=c++17 direct_checker.cpp -o checker && ./checker
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
using Hist=map<int,U>;
U choose(int n,int k){ if(k<0||k>n) return 0;U z=1;for(int i=1;i<=k;i++)z=z*(n-i+1)/i;return z; }
void check(int m,int n){
  int N=m+n; vector<pair<int,int>> edges; vector<vector<int>> adj(N,vector<int>(N,-1));
  for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(i!=0||j!=0){int id=edges.size();edges.push_back({i,m+j});adj[i][m+j]=adj[m+j][i]=id;}
  int E=edges.size();if(E>24) throw runtime_error("Bounded direct check only");
  vector<vector<int>> dist(N,vector<int>(N,10000));
  for(int i=0;i<N;i++){dist[i][i]=0;for(int j=0;j<N;j++)if(adj[i][j]>=0)dist[i][j]=1;}
  for(int k=0;k<N;k++)for(int i=0;i<N;i++)for(int j=0;j<N;j++)dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j]);
  set<U> forbidden;
  for(int a=0;a<N;a++)for(int d=0;d<N;d++)if(dist[a][d]==3)
   for(int b=0;b<N;b++)if(adj[a][b]>=0)
    for(int c=0;c<N;c++)if(adj[b][c]>=0&&adj[c][d]>=0&&a!=c&&b!=d){
       U f=(U(1)<<adj[a][b])|(U(1)<<adj[b][c])|(U(1)<<adj[c][d]);
       if(__builtin_popcountll(f)==3)forbidden.insert(f);
    }
  U full=(U(1)<<E)-1;Hist actual,facets;
  for(U z=0;z<=full;z++){
    bool legal=true;for(U f:forbidden) if((z&f)==f){legal=false;break;}if(!legal)continue;
    int weight=__builtin_popcountll(z);actual[weight]++;
    bool maximal=true;
    for(int e=0;e<E&&maximal;e++)if(!(z&(U(1)<<e))){
      U ext=z|(U(1)<<e);bool still=true;
      for(U f:forbidden)if((ext&f)==f){still=false;break;}
      if(still)maximal=false;
    }
    if(maximal)facets[weight]++;
  }
  int r=m-1,s=n-1;Hist pred,facepred;
  for(int a=0;a<=s;a++)for(int b=0;b<=r;b++){
    U mult=choose(s,a)*choose(r,b);
    for(int k=0;k<=r*s-a*b;k++)pred[a+b+k]+=mult*choose(r*s-a*b,k);
    if(a&&b)facepred[r*s+a+b-a*b]+=mult;
  }
  facepred[r*s+r]++;facepred[r*s+s]++;
  if(actual!=pred||facets!=facepred){cerr<<"FAIL "<<m<<","<<n<<"\n";exit(1);}
  U num=0,nface=0;for(auto [k,v]:actual)num+=v;for(auto [k,v]:facets)nface+=v;
  cout<<"OK "<<m<<"x"<<n<<" edges="<<E<<" geodesic-triples="<<forbidden.size()<<" sets="<<num<<" facets="<<nface<<" max="<<actual.rbegin()->first<<"\n";
}
int main(){for(auto [m,n]:vector<pair<int,int>>{{3,3},{3,4},{4,4},{4,5},{5,5}})check(m,n);cout<<"DIRECT_CERTIFICATE_OK\n";}
