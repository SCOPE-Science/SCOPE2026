// Exact full-state bottom-up game dynamic programming for GP(10,2).
// Only the standard C++17 library is used.
#include <array>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <cstdint>
using namespace std;
int main(){
 constexpr int n=20,full=(1<<n)-1;
 array<vector<int>,n> g{};
 auto add=[&](int x,int y){g[x].push_back(y);g[y].push_back(x);};
 for(int i=0;i<10;i++){
  add(i,(i+1)%10);add(i,10+i);add(10+i,10+(i+2)%10);
 }
 array<int,n> closed{};
 for(int i=0;i<n;i++){
  assert(g[i].size()==3);
  closed[i]=1<<i;
  for(int v:g[i])closed[i]|=1<<v;
 }
 // d[mask] is the number of remaining moves with minimizer next;
 // s[mask] is the same with maximizer next. Every transition increases mask.
 vector<uint8_t> d(full+1,0),s(full+1,0);
 for(int mask=full-1;mask>=0;--mask){
  int low=127,high=-1;
  for(int i=0;i<n;i++){
    int next=mask|closed[i];
    if(next==mask)continue;
    low=min(low,1+(int)s[next]);
    high=max(high,1+(int)d[next]);
  }
  assert(low!=127 && high>=0);
  d[mask]=low;s[mask]=high;
 }
 assert(d[0]==9 && s[0]==8);
 for(int u=0;u<n;u++){
  array<int,n> dist;dist.fill(-1);dist[u]=0;
  queue<int>q;q.push(u);
  while(!q.empty()){
    int a=q.front();q.pop();
    for(int b:g[a])if(dist[b]<0){dist[b]=dist[a]+1;q.push(b);}
  }
  int counts[6]={};for(int x:dist){assert(x>=0&&x<=5);counts[x]++;}
  int expect[6]={1,3,6,6,3,1};
  for(int j=0;j<6;j++)assert(counts[j]==expect[j]);
  assert(1+(int)s[closed[u]]==9 && 1+(int)d[closed[u]]==8);
  for(int v=0;v<n;v++){
   if(u==v)continue;
   int mask=closed[u]|closed[v];
   // First convention: D then S, next D. Second: S then D, next S.
   int ds=2+(int)d[mask],ss=2+(int)s[mask];
   assert(ds==(dist[v]==1||dist[v]==5?9:8));
   assert(ss==(dist[v]==3?8:9));
  }
 }
 cout<<"graph: GP(10,2), vertices=20 edges=30, distance profile=1,3,6,6,3,1\n";
 cout<<"game values: Dominator-start=9, Staller-start=8\n";
 cout<<"all 20 first choices equivalent by explicitly checked score\n";
 cout<<"after D first, S response: distance 1/5 -> final 9; distance 2/3/4 -> final 8\n";
 cout<<"after S first, D response: distance 3 -> final 8; distance 1/2/4/5 -> final 9\n";
 cout<<"first-two-move positions verified=760\n";
 cout<<"bottom-up state count=1048576\n";
}
