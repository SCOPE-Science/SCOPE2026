#include <vector>
#include <array>
#include <algorithm>
#include <cassert>
#include <map>
#include <cstdio>
using namespace std;
const int V=12,N=531441;
struct Sys {vector<int> nxt,depth,period,cycle; map<int,int> orbit;map<pair<int,int>,int> hist;int maxdep=0;};
array<array<int,3>,V> adj; int power[13];
void build(){int lcf[V]={-5,-2,-4,2,5,-2,2,5,-2,-5,4,2};power[0]=1;for(int i=1;i<=V;i++)power[i]=power[i-1]*3;
for(int i=0;i<V;i++){adj[i]={ (i+11)%12,(i+1)%12,(i+lcf[i]+120)%12 };sort(adj[i].begin(),adj[i].end());assert(adj[i][0]!=adj[i][1]&&adj[i][1]!=adj[i][2]);}
for(int i=0;i<V;i++)for(int j:adj[i]) assert(find(adj[j].begin(),adj[j].end(),i)!=adj[j].end());}
Sys run(bool ghm){Sys a;a.nxt.resize(N);a.depth.assign(N,-1);a.period.assign(N,0);a.cycle.assign(N,-1);int x[V];
for(int s=0;s<N;s++){int m=s;for(int i=0;i<V;i++){x[i]=m%3;m/=3;}
int t=0;for(int i=0;i<V;i++){
int c=x[i],v=c;
if(ghm){if(c>0)v=(c+1)%3;else for(int j:adj[i])if(x[j]==1){v=1;break;}}
else{int want=(c+1)%3;for(int j:adj[i])if(x[j]==want){v=want;break;}}
t+=power[i]*v;}
a.nxt[s]=t;}
vector<char> color(N,0);vector<int> path;int ncycles=0;
for(int root=0;root<N;root++){
 if(color[root]==2)continue;
 int u=root;path.clear();
 while(color[u]==0){color[u]=1;path.push_back(u);u=a.nxt[u];}
 int end=(int)path.size()-1;
 if(color[u]==1){int k=0;while(path[k]!=u)k++;int p=(int)path.size()-k;int id=ncycles++;
 a.orbit[p]++;for(int j=k;j<(int)path.size();j++){int v=path[j];a.depth[v]=0;a.period[v]=p;a.cycle[v]=id;color[v]=2;}end=k-1;}
 for(int j=end;j>=0;j--){int v=path[j],w=a.nxt[v];assert(color[w]==2);a.depth[v]=a.depth[w]+1;a.period[v]=a.period[w];a.cycle[v]=a.cycle[w];color[v]=2;}
}
for(int s=0;s<N;s++){assert(color[s]==2);a.hist[{a.depth[s],a.period[s]}]++;a.maxdep=max(a.maxdep,a.depth[s]);}
return a;}
int main(){build();Sys c=run(false),g=run(true);printf("CCA cycles:");for(auto [p,n]:c.orbit)printf(" %d:%d",p,n);printf("; max=%d\n",c.maxdep);
printf("GHM cycles:");for(auto [p,n]:g.orbit)printf(" %d:%d",p,n);printf("; max=%d\n",g.maxdep);
map<pair<int,int>,int> joint;map<pair<int,int>,int> delay;map<int,int> delta;map<pair<int,int>,int> both;int disagree=0;
for(int s=0;s<N;s++){
 joint[{c.period[s],g.period[s]}]++;delay[{c.depth[s],g.depth[s]}]++;
 if(c.period[s]!=g.period[s]){disagree++;delta[c.period[s]-g.period[s]]++;}
}
printf("JOINT PERIOD:");for(auto [pg,n]:joint)printf(" C%d/G%d:%d",pg.first,pg.second,n);printf("; total=%d disagree=%d\n",N,disagree);
printf("DELAY long:");for(auto [dg,n]:delay)if(dg.first>=15||dg.second>=18)printf(" C%d/G%d:%d",dg.first,dg.second,n);puts("");
for(auto [label,sys]:vector<pair<const char*,Sys*>>{{"CCA",&c},{"GHM",&g}}){printf("%s period-basin:",label);map<int,int> b;for(auto [key,n]:sys->hist)b[key.second]+=n;for(auto [p,n]:b)printf(" %d:%d",p,n);puts("");}
}
