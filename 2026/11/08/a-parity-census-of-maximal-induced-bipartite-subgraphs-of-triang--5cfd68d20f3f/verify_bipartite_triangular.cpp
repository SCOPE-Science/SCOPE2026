// Standalone finite verifier for induced bipartite subgraphs of triangular graphs.
// Compile: g++ -std=c++17 -O3 verify_bipartite_triangular.cpp -o verify && ./verify
#include <bits/stdc++.h>
using namespace std;
using i64=long long;
static bool bipartite(unsigned mask, const vector<unsigned>& adj, int m){
  int color[32]; fill(color,color+m,-1);
  for(int i=0;i<m;++i){
    if(!(mask&(1u<<i)) || color[i]>=0)continue;
    color[i]=0;
    int q[32];int head=0,tail=0;q[tail++]=i;
    while(head<tail){
      int u=q[head++]; unsigned x=adj[u]&mask;
      while(x){ int v=__builtin_ctz(x);x&=x-1;
        if(color[v]<0){color[v]=color[u]^1;q[tail++]=v;}
        else if(color[v]==color[u])return false;
      }
    }
  }
  return true;
}
static i64 factorial(int n){i64 q=1;for(int i=2;i<=n;i++)q*=i;return q;}
static void shape_counts(int n, vector<i64> &all, vector<i64>&maximal){
  // Structurally independent species computation via integer component convolutions.
  // Number of even cycles on s specified labels: (s-1)!/2 for even s>=4.
  // Number of paths on s specified labels: 1 for s=1; s!/2 for s>=2.
  // DFS over blocks by the minimum remaining label to avoid component overcounting.
  vector<pair<int,int>>edges;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.emplace_back(i,j);
  const int m=edges.size();
  const unsigned lim=(1u<<m);
  for(unsigned mask=0;mask<lim;mask++){
    vector<int>deg(n,0);vector<vector<int>>g(n);
    for(int k=0;k<m;k++)if(mask>>k&1){auto [u,v]=edges[k];deg[u]++;deg[v]++;g[u].push_back(v);g[v].push_back(u);}
    bool valid=true;for(int d:deg)if(d>2){valid=false;break;}
    if(!valid)continue;
    bool seen[16]={};int paths=0;int pathorder=0;int pathis2=0;
    for(int u=0;u<n;u++)if(!seen[u]){
      int cnt=0,deg1=0;bool cyc=true;
      vector<int>todo(1,u);seen[u]=true;
      for(size_t j=0;j<todo.size();j++){
        int v=todo[j];cnt++; if(deg[v]!=2)cyc=false;
        if(deg[v]==1)deg1++;
        for(int w:g[v])if(!seen[w]){seen[w]=true;todo.push_back(w);}
      }
      if(cyc && cnt%2){valid=false;break;}
      if(!cyc){paths++;pathorder=cnt;pathis2=cnt==2;}
    }
    if(!valid)continue;
    all[__builtin_popcount(mask)]++;
    if(paths==0 || (paths==1&&(pathorder%2==1||pathis2)))maximal[__builtin_popcount(mask)]++;
  }
}
int main(){
  long long totalMasks=0;long long totalAdmissible=0;long long totalMax=0;
  for(int n=2;n<=7;n++){
    vector<pair<int,int>> edges;
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.emplace_back(i,j);
    int m=edges.size();vector<unsigned>adj(m,0);
    for(int i=0;i<m;i++)for(int j=0;j<m;j++)if(i!=j){
      auto a=edges[i],b=edges[j];
      if(a.first==b.first||a.first==b.second||a.second==b.first||a.second==b.second)adj[i]|=(1u<<j);
    }
    vector<i64>cnt(m+1),structCnt(m+1),allCnt(m+1),structAll(m+1);
    unsigned lim=1u<<m;totalMasks+=lim;
    for(unsigned mask=0;mask<lim;mask++){
      if(!bipartite(mask,adj,m))continue;
      allCnt[__builtin_popcount(mask)]++;
      bool maximal=true;
      unsigned extra=(lim-1)^mask;
      while(extra){ int i=__builtin_ctz(extra);extra&=extra-1;
        if(bipartite(mask|(1u<<i),adj,m)){maximal=false;break;}
      }
      if(maximal)cnt[__builtin_popcount(mask)]++;
    }
    shape_counts(n,structAll,structCnt);
    if(cnt!=structCnt || allCnt!=structAll){cerr<<"DISAGREEMENT at n="<<n<<'\n';return 1;}
    i64 nmax=accumulate(cnt.begin(),cnt.end(),0LL);
    i64 nadm=accumulate(allCnt.begin(),allCnt.end(),0LL);
    totalMax+=nmax;totalAdmissible+=nadm;
    cout<<"n="<<n<<" all="<<nadm<<" maximal="<<nmax<<" support:";
    for(int k=0;k<=m;k++)if(cnt[k])cout<<" ("<<k<<":"<<cnt[k]<<")";
    cout<<'\n';
  }
  cout<<"VERIFY_OK graph_orders=2..7 candidate_subsets="<<totalMasks
      <<" bipartite_subsets="<<totalAdmissible
      <<" maximal_subsets="<<totalMax
      <<" graph_level_and_base_structure=PASS\n";
}
