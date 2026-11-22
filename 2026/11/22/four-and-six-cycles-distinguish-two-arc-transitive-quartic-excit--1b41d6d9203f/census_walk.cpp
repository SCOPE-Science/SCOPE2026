#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <map>
#include <string>
#include <utility>
#include <vector>
using namespace std;
const int N=12, S=531441;
int pw[N+1];
vector<int> cubo[12], circ[12];
void add(vector<int> *g, int a, int b){g[a].push_back(b);g[b].push_back(a);}
void graphs(){
 vector<pair<int,int>> e;
 for(int u=0;u<8;u++)for(int k=0;k<3;k++)if(!(u>>k&1))e.push_back({u,u|(1<<k)});
 assert(e.size()==12);
 for(int i=0;i<12;i++)for(int j=i+1;j<12;j++)if(e[i].first==e[j].first||e[i].first==e[j].second||e[i].second==e[j].first||e[i].second==e[j].second)add(cubo,i,j);
 for(int i=0;i<12;i++)for(int d:{1,5})add(circ,i,(i+d)%12);
 for(auto g:{cubo,circ}){int ec=0;for(int i=0;i<12;i++){assert(g[i].size()==4);ec+=g[i].size();}assert(ec==48);}
}
void run(vector<int> *g,string name){
 vector<int> dest(S);int vals[N];
 for(int st=0;st<S;st++){
  int t=st;for(int i=0;i<N;i++){vals[i]=t%3;t/=3;}
  int out=0;
  for(int i=0;i<N;i++){
   int y;
   if(vals[i]==1)y=2;else if(vals[i]==2)y=0;else{
    int c=0;for(int j:g[i])c+=vals[j]==1;
    y=(c>=2?1:0);
   }
   out+=pw[i]*y;
  }
  dest[st]=out;
 }
 vector<int> status(S,-1),dep(S,-1),period(S,0),orbit(S,-1);
 vector<int> lengths, basin, counts;
 vector<int> route, visit(S,-1),pos(S,-1); int root=0;
 for(int s=0;s<S;s++)if(status[s]==-1){
  route.clear();int v=s;
  while(status[v]==-1 && visit[v]!=s){visit[v]=s;pos[v]=route.size();route.push_back(v);v=dest[v];}
  int steps=0,cycid=-1;
  if(status[v]==-1){int p=route.size()-pos[v];cycid=lengths.size();lengths.push_back(p);basin.push_back(0);
   for(int k=pos[v];k<(int)route.size();k++){int z=route[k];dep[z]=0;period[z]=p;orbit[z]=cycid;status[z]=1;basin[cycid]++;}
   route.resize(pos[v]);
  }
  for(int k=(int)route.size()-1;k>=0;k--){int z=route[k];status[z]=1;dep[z]=dep[dest[z]]+1;period[z]=period[dest[z]];orbit[z]=orbit[dest[z]];basin[orbit[z]]++;}
 }
 map<pair<int,int>,long long> tab;map<int,int> orbits;map<pair<int,int>,int> basin_hist;long long allnonzero=0;
 int maxdep=0;for(int s=0;s<S;s++){tab[{dep[s],period[s]}]++;maxdep=max(maxdep,dep[s]);if(period[s]>1)allnonzero++;}
 for(int o=0;o<(int)lengths.size();o++){orbits[lengths[o]]++;basin_hist[{lengths[o],basin[o]}]++;}
 printf("GRAPH %s S=%d maxdep=%d recurrent=%lld oscillation=%lld\n",name.c_str(),S,maxdep,tab[{0,1}]+([&]{long long c=0;for(auto [k,v]:tab)if(k.first==0&&k.second>1)c+=v;return c;})(),allnonzero);
 printf("orbits:");for(auto[k,v]:orbits)printf(" p%d:%d",k,v);puts("");
 printf("table:");for(auto[k,v]:tab)printf(" (%d,%d)=%lld",k.first,k.second,v);puts("");
 printf("basins:");for(auto [k,v]:basin_hist)printf(" (%d,%d):%d",k.first,k.second,v);puts("");
 printf("checksum ");unsigned long long h=1469598103934665603ull;for(int s=0;s<S;s++){h=(h^(unsigned)dest[s])*1099511628211ull;}printf("%llu\n",h);
}
int main(){pw[0]=1;for(int i=1;i<=N;i++)pw[i]=pw[i-1]*3;graphs();run(cubo,"cubo");run(circ,"circulant");}
