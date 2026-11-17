// Reproducible independent full-state comparison of two three-color excitable maps.
// The fourteen vertices are nonzero binary vectors 1,...,7 on each of two shores.
// Adjacency is zero F_2 dot-product. No shared incidence list or functional-graph peeling.
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <vector>
#include <tuple>
using namespace std;
constexpr int K=14, N=4782969;
using Int = uint32_t;
array<array<int,3>,K> adj{};
array<Int,K+1> pow3{};
Int step(Int code,int kind) {
 unsigned char digit[K];
 for(int v=0;v<K;++v){digit[v]=code%3;code/=3;}
 Int ans=0;
 for(int v=K-1;v>=0;--v){
  int color=digit[v],target=(color+1)%3;bool contact=false;
  if(kind==0) {
   for(int j=0;j<3;j++)contact|=(digit[adj[v][j]]==target);
   if(contact)color=target;
  } else {
   if(color==1)color=2;
   else if(color==2)color=0;
   else {for(int j=0;j<3;j++)contact|=(digit[adj[v][j]]==1);if(contact)color=1;}
  }
  ans=3*ans+color;
 }
 return ans;
}
struct Data{vector<uint8_t> period,entry;};
Data classify(int kind){
 vector<uint8_t> status(N,0); // 0 unseen,1 on active path,2 classified
 Data d{vector<uint8_t>(N),vector<uint8_t>(N)};
 vector<Int> path;path.reserve(64);
 for(Int initial=0;initial<N;++initial){
  if(status[initial])continue;
  path.clear();Int s=initial;
  while(status[s]==0){status[s]=1;path.push_back(s);s=step(s,kind);}
  if(status[s]==1){
   int pos=int(path.size())-1;while(path[pos]!=s){--pos;if(pos<0){puts("bad cycle");exit(1);}}
   int period=int(path.size())-pos;
   if(period<1 || period>255)exit(4);
   for(int t=pos;t<int(path.size());++t){Int k=path[t];d.period[k]=period;d.entry[k]=0;status[k]=2;}
   path.resize(pos);
  }
  for(int t=int(path.size())-1;t>=0;--t){
   Int k=path[t],j=step(k,kind);d.period[k]=d.period[j];if(d.entry[j]==255)exit(5);d.entry[k]=d.entry[j]+1;status[k]=2;
  }
 }
 for(int i=0;i<N;i++)if(status[i]!=2 || !d.period[i]){puts("incomplete");exit(2);}
 return d;
}
int main(){
 pow3[0]=1;for(int i=0;i<K;++i)pow3[i+1]=pow3[i]*3;
 int degree[K]={};
 for(int point=1;point<=7;point++)for(int normal=1;normal<=7;normal++){
   if((__builtin_popcount(unsigned(point & normal))&1)==0){
    int u=point-1,v=normal+6;adj[u][degree[u]++]=v;adj[v][degree[v]++]=u;
   }
 }
 for(int v=0;v<K;v++)if(degree[v]!=3)exit(3);
 auto c=classify(0),h=classify(1);
 map<pair<int,int>,long long> joint;map<tuple<int,int,int,int>,long long> shifts;
 int witness84=-1, witness105=-1;
 for(int i=0;i<N;i++){
  auto p=make_pair(int(c.period[i]),int(h.period[i]));joint[p]++;
  if(p==make_pair(8,4) && witness84<0)witness84=i;
  if(p==make_pair(10,5) && witness105<0)witness105=i;
  if(p.first!=p.second) shifts[{p.first,p.second,int(c.entry[i]),int(h.entry[i])}]++;
 }
 long long mismatch=0;
 for(auto [k,v]:joint)if(k.first!=k.second)mismatch+=v;
 printf("total %d\nmismatch %lld\n",N,mismatch);
 printf("witness_8_4 %d depth %d %d\n",witness84,c.entry[witness84],h.entry[witness84]);
 printf("witness_10_5 %d depth %d %d\n",witness105,c.entry[witness105],h.entry[witness105]);
 for(auto [p,v]:joint)printf("pair %d:%d = %lld\n",p.first,p.second,v);
 for(auto [p,v]:shifts){auto [a,b,c,d]=p;printf("shift %d:%d:%d:%d = %lld\n",a,b,c,d,v);}
}
