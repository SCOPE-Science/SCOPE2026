// Construct the integral finite-state dual potential and inspect tight cycles.
#include<bits/stdc++.h>
using namespace std;
struct Edge{int u,v,c;};
int main(){const int B=9, S=B*B*B*B;vector<Edge> edges;edges.reserve(S*B);
 for(int u=0;u<S;u++){
  int a[4];int m=u;for(int i=3;i>=0;i--){a[i]=m%9;m/=9;}
  for(int z=0;z<B;z++){
   int b[5]={a[0],a[1],a[2],a[3],z};
   auto outer=[](int s){return s/3;};auto inner=[](int s){return s%3;};
   int vi=outer(b[2]), ui=inner(b[2]);
   if(vi==0 && outer(b[1])!=2 && outer(b[3])!=2 && ui!=2)continue;
   if(ui==0 && inner(b[0])!=2 && inner(b[4])!=2 && vi!=2)continue;
   int v=(u%729)*9+z;
   edges.push_back({u,v,7*(vi+ui)-8});
  }
 }
 cerr<<"states "<<S<<" edges "<<edges.size()<<"\n";
 vector<int> h(S,0);int iterations=0,change=0;
 for(int it=0;it<=S;it++){
  int updates=0;
  for(auto e:edges)if(h[e.v]>h[e.u]+e.c){h[e.v]=h[e.u]+e.c;updates++;}
  if(it<40 || (it%50==0))cerr<<"iter "<<it<<" updates "<<updates<<" h_min "<<*min_element(h.begin(),h.end())<<"\n";
  iterations++;
  if(!updates){change=0;break;}change=updates;
 }
 if(change){cerr<<"NEGATIVE CYCLE!\n";return 1;}
 vector<vector<int>> G(S),RG(S);
 long long tight=0;for(auto e:edges)if(h[e.v]==h[e.u]+e.c){G[e.u].push_back(e.v);RG[e.v].push_back(e.u);tight++;}
 vector<char> vis(S);vector<int> order;function<void(int)> dfs=[&](int v){vis[v]=1;for(int w:G[v])if(!vis[w])dfs(w);order.push_back(v);};for(int i=0;i<S;i++)if(!vis[i])dfs(i);
 fill(vis.begin(),vis.end(),0);vector<vector<int>> scc;function<void(int,vector<int>&)> rdfs=[&](int v,vector<int>&cc){vis[v]=1;cc.push_back(v);for(int w:RG[v])if(!vis[w])rdfs(w,cc);};for(int k=S-1;k>=0;k--){int v=order[k];if(!vis[v]){scc.emplace_back();rdfs(v,scc.back());}}
 map<int,int> sizes;int recurrent=0;
 for(auto &cc:scc)if(cc.size()>1 || (cc.size()==1 && find(G[cc[0]].begin(),G[cc[0]].end(),cc[0])!=G[cc[0]].end())){
 recurrent++;sizes[cc.size()]++;
 if(cc.size()<30){cerr<<"SCC ";for(int u:cc){int a[4],m=u;for(int i=3;i>=0;i--){a[i]=m%9;m/=9;}cerr<<"["<<a[0]<<","<<a[1]<<","<<a[2]<<","<<a[3]<<"] ";}cerr<<"\n";}
 }
 cerr<<"iterations "<<iterations<<" tight "<<tight<<" recurrent "<<recurrent<<" sizes ";for(auto [k,v]:sizes)cerr<<k<<":"<<v<<",";cerr<<"\n";
 for(int v=0;v<S;v++)cout<<h[v]<<"\n";
}
