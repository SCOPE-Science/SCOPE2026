// Exhaustive independent mask-based verification of Heawood metric-basis mobility.
#include <bits/stdc++.h>
using namespace std;
int main(){
  const int N=14, ALL=1<<N; int adj[N]={}, dist[N][N];
  for(int p=0;p<7;++p)for(int r:{0,1,3}){int l=7+(p-r+7)%7;adj[p]|=1<<l;adj[l]|=1<<p;}
  for(int u=0;u<N;++u){for(int v=0;v<N;++v)dist[u][v]=(u==v?0:99);queue<int>q;q.push(u);while(!q.empty()){int v=q.front();q.pop();for(int w=0;w<N;++w)if((adj[v]>>w&1)&&dist[u][w]>dist[u][v]+1){dist[u][w]=dist[u][v]+1;q.push(w);}}}
  auto resolves=[&](int mask){for(int u=0;u<N;++u)for(int v=u+1;v<N;++v){bool separated=false;for(int w=0;w<N;++w)if((mask>>w&1)&&dist[u][w]!=dist[v][w]){separated=true;break;}if(!separated)return false;}return true;};
  vector<int>B;int fours=0; for(int m=0;m<ALL;++m){int k=__builtin_popcount((unsigned)m);if(k==4&&resolves(m))++fours;if(k==5&&resolves(m))B.push_back(m);}assert(fours==0&&B.size()==168);
  int oct=0;set<int>oct_masks;
  for(int m=0;m<ALL;++m)if(__builtin_popcount((unsigned)m)==8){bool regular=true;int seed=-1;for(int v=0;v<N;++v)if(m>>v&1){if(seed<0)seed=v;if(__builtin_popcount((unsigned)(m&adj[v]))!=2){regular=false;break;}}if(!regular)continue;
  int seen=1<<seed; for(int i=0;i<8;++i){int reached=seen;for(int v=0;v<N;++v)if(seen>>v&1)reached|=adj[v]&m;seen=reached;}if(seen==m){++oct;oct_masks.insert(m);}}
  assert(oct==21);
  int sz=B.size();vector<vector<int>>sl(sz),jp(sz);
  for(int i=0;i<sz;++i)for(int j=i+1;j<sz;++j){int x=B[i]^B[j];if(__builtin_popcount((unsigned)x)!=2)continue;jp[i].push_back(j);jp[j].push_back(i);int u=__builtin_ctz((unsigned)(B[i]&x));int v=__builtin_ctz((unsigned)(B[j]&x));if(adj[u]>>v&1){sl[i].push_back(j);sl[j].push_back(i);}}
  auto verify=[&](const vector<vector<int>>&g,int degree,int edges,int numcomp,int compsize,int ecc){int edgecount=0;for(auto z:g){assert((int)z.size()==degree);edgecount+=(int)z.size();}assert(edgecount/2==edges);vector<int>distances(sz);int components=0;set<int>unseen;for(int i=0;i<sz;++i)unseen.insert(i);vector<int>unions;
    while(!unseen.empty()){int start=*unseen.begin();queue<int>q;q.push(start);unseen.erase(start);int size=0, unionmask=0;while(!q.empty()){int u=q.front();q.pop();++size;unionmask|=B[u];for(int v:g[u])if(unseen.erase(v))q.push(v);}assert(size==compsize);unions.push_back(unionmask);++components;}
    assert(components==numcomp);
    for(int start=0;start<sz;++start){fill(distances.begin(),distances.end(),-1);distances[start]=0;queue<int>q;q.push(start);while(!q.empty()){int u=q.front();q.pop();for(int v:g[u])if(distances[v]<0){distances[v]=distances[u]+1;q.push(v);}}int mx=0;for(int v=0;v<sz;++v)if(distances[v]>=0)mx=max(mx,distances[v]);assert(mx==ecc);}
    if(compsize==8){set<int>z(unions.begin(),unions.end());assert(z==oct_masks);}
  };
  verify(sl,2,168,21,8,4);verify(jp,5,420,1,168,5);
  printf("CHECK_OK checker=cpp graph14 four_sets=1001 five_sets=2002 metric_bases=168 induced_octagons=%d\n",oct);
  puts("slide_edges=168 slide_components=21:C8 slide_degree=2 slide_component_diameter=4");
  puts("jump_edges=420 jump_components=1 jump_degree=5 jump_diameter=5");
  puts("slide_component_unions_equal_induced_octagons=yes");
}
