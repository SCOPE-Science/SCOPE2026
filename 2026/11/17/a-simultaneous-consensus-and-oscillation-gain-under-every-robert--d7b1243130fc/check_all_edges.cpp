#include <bits/stdc++.h>
using namespace std;
const int N=19, STATES=1<<N;
const int adj[N][4] = {
{1,2,3,4},{0,5,6,7},{0,8,9,10},{0,11,12,13},{0,14,15,16},{1,8,11,14},{1,9,12,15},{1,10,13,16},{2,5,12,16},{2,6,13,17},{2,7,15,18},{3,5,15,17},{3,6,8,18},{3,7,9,14},{4,5,13,18},{4,6,10,11},{4,7,8,17},{9,11,16,18},{10,12,14,17}};
int main(){
vector<pair<int,int>> edges;
for(int i=0;i<N;i++)for(int j:adj[i])if(i<j)edges.push_back({i,j});
cout<<"edges "<<edges.size()<<"\n";
vector<unsigned char> degree(N);
for (int v=0;v<N;v++)degree[v]=4;
for(int e=-1;e<(int)edges.size();e++){
vector<unsigned> masks(N);fill(degree.begin(),degree.end(),4);
for(int v=0;v<N;v++)for(int u:adj[v])masks[v]|=(1u<<u);
if(e>=0){auto [u,v]=edges[e];masks[u]&=~(1u<<v);masks[v]&=~(1u<<u);degree[u]--;degree[v]--;}
vector<uint32_t> f(STATES);
for(int x=0;x<STATES;x++){
  uint32_t y=0;
  for(int v=0;v<N;v++){
    int count=__builtin_popcount((unsigned)x&masks[v]);
    bool b=(2*count>degree[v])||(2*count==degree[v] && ((x>>v)&1));
    y|=uint32_t(b)<<v;
  }
  f[x]=y;
}
// For dynamics size <=2 attractors compute F^K and F^(K+1) exact once F^K=f^K global via arrays
vector<uint32_t> p(STATES), q(STATES);
iota(p.begin(),p.end(),0);
int K=0;vector<uint32_t> first_entry(16,0), fix_entry(16,0), cycle_entry(16,0);
vector<uint8_t> reached(STATES,0);int maxent=0;
for(;K<16;K++) {
 unsigned long long cfix=0, c2=0; int anew=0;
 for(int x=0;x<STATES;x++) {
  int y=p[x];if(f[y]==y) cfix++;
  else if(f[f[y]]==y)c2++;
  if(!reached[x]&&(f[y]==y||f[f[y]]==y)) {
    reached[x]=1;anew++;
    if(f[y]==y)fix_entry[K]++;else cycle_entry[K]++;
  }
  q[x]=f[y];
 }
 first_entry[K]=anew;
 if(cfix+c2==STATES){maxent=K;break;}
 p.swap(q);
}
if(K==16){cerr<<"ERROR no settle";return 3;}
uint64_t bas0=0,bas1=0; int fixed=0, per2=0;vector<int> cons_entries(K+1);
for(int x=0;x<STATES;x++){
 int y=x,t=0;
 while(f[y]!=y&&f[f[y]]!=y){y=f[y];t++; if(t>20){cerr<<"not period2";return 5;}}
 if(y==0||f[y]==0){bas0++;cons_entries[t]++;}
 if(y==STATES-1||f[y]==STATES-1){bas1++;cons_entries[t]++;}
 if(f[x]==x)fixed++; else if(f[f[x]]==x)per2++;
}
if(e==-1) cout<<"base "; else cout<<edges[e].first+1<<"-"<<edges[e].second+1<<" ";
cout<<"fixed="<<fixed<<" primitive2="<<per2/2<<" max="<<maxent<<" consensus="<<bas0+bas1<<" fixedbas="<<accumulate(fix_entry.begin(),fix_entry.end(),0LL)<<" 2bas="<<accumulate(cycle_entry.begin(),cycle_entry.end(),0LL)<<" entry=";
for(int j=0;j<=K;j++)cout<<first_entry[j]<<(j==K?' ':',');cout<<"\n";
}
}
