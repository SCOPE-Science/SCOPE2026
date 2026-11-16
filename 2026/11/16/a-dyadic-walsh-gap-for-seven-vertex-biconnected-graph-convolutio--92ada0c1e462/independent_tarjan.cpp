// Independent integer validation of the biconnected-graph Walsh assertions.
// C++17; g++ -O3 -std=c++17 independent_tarjan.cpp -o independent_tarjan
#include <cstdio>
#include <vector>
#include <functional>
#include <algorithm>
#include <cassert>
using namespace std;
static bool is_biconnected(const vector<pair<int,int>>&E, int n,int mask){
 if(__builtin_popcount((unsigned)mask)<n)return false;
 vector<vector<int>>adj(n);
 for(int k=0;k<(int)E.size();k++) if((mask>>k)&1){auto [u,v]=E[k];adj[u].push_back(v);adj[v].push_back(u);}
 vector<int>tin(n,-1),low(n,-1);int clock=0;bool art=false;
 function<void(int,int)> dfs=[&](int u,int par){
  tin[u]=low[u]=clock++;int children=0;
  for(int v:adj[u]){
   if(v==par)continue;
   if(tin[v]!=-1)low[u]=min(low[u],tin[v]);
   else {dfs(v,u);children++;low[u]=min(low[u],low[v]);
    if(par!=-1&&low[v]>=tin[u])art=true;
   }
  }
  if(par==-1&&children>1)art=true;
 };
 dfs(0,-1);
 if(art)return false;
 for(int i=0;i<n;i++)if(tin[i]<0)return false;
 return true;
}
static void recursive_hadamard(vector<int>&v,int start,int span){
 if(span==1)return;
 int h=span/2;
 recursive_hadamard(v,start,h);recursive_hadamard(v,start+h,h);
 for(int j=0;j<h;j++){int a=v[start+j],b=v[start+j+h];v[start+j]=a+b;v[start+j+h]=a-b;}
}
int main(){
 for(int n=3;n<=7;n++){
  vector<pair<int,int>>E;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)E.emplace_back(i,j);
  int N=1<<E.size();vector<int> b(N,0);long long count=0,direct=0;int witness=(n==7?2396:(n==6?107:0));
  for(int x=0;x<N;x++)if(is_biconnected(E,n,x)){b[x]=1;count++;direct+= (__builtin_parity((unsigned)(x&witness))?-1:1);}
  recursive_hadamard(b,0,N);
  int zeros=0,minabs=2000000000;long long sq=0;bool mod_ok=true;
  for(int x:b){if(x==0)zeros++;else minabs=min(minabs,abs(x));sq+=1LL*x*x;if(n>=6 && ((x-count)&15)!=0)mod_ok=false;}
  printf("n=%d labelled=%lld zeros=%d minabs=%d parseval=%lld mod16=%d witness_mask=%d witness_direct=%lld witness_FWHT=%d\n",n,count,zeros,minabs,sq,mod_ok,witness,direct,b[witness]); if(direct!=b[witness])return 4;
  static const int c[8]={0,0,0,1,10,238,11368,1014888};static const int mn[8]={0,0,0,1,2,2,8,8};if(sq!=count*N || zeros || (n>=6&&!mod_ok) || count!=c[n] || minabs!=mn[n] || (n==6&&direct!=-8) || (n==7&&direct!=8))return 1;
 }
}
