// Reproducible exhaustive check for the incidence subdivision of a complete graph.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using U = uint64_t;
int pop(U a){return __builtin_popcountll(a);}
struct Graph {
 int n,N,m; vector<pair<int,int>> edges; vector<U> adj;
 Graph(int n): n(n),N(n+n*(n-1)/2),m(n*(n-1)/2),adj(N,0) {
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
   int k=edges.size(), w=n+k;edges.push_back({i,j});
   adj[i] |= U(1)<<w; adj[j]|=U(1)<<w;
   adj[w] = (U(1)<<i)|(U(1)<<j);
  }
 }
 bool power(U S)const{
  U seen=S;
  for(int i=0;i<N;i++) if((S>>i)&1) seen|=adj[i];
  for(;;){
   U newseen=seen;
   for(int i=0;i<N;i++)if((seen>>i)&1){U unseen=adj[i]&~seen;
    if(pop(unseen)==1)newseen|=unseen;
   }
   if(newseen==seen)break;
   seen=newseen;
  }
  return seen==((U(1)<<N)-1);
 }
 bool forest(U S)const{
  int parent[20];for(int i=0;i<n;i++)parent[i]=i;
  auto root=[&](int x){while(parent[x]!=x)x=parent[x];return x;};
  for(int e=0;e<m;e++){
   auto [i,j]=edges[e];
   if((S>>i)&1 || (S>>j)&1 || (S>>(n+e))&1)continue;
   int x=root(i),y=root(j);
   if(x==y)return false;
   parent[x]=y;
  }
  return true;
 }
 bool minimal(U S)const{
  if(!power(S))return false;
  for(int i=0;i<N;i++)if((S>>i)&1){
   if(power(S & ~(U(1)<<i)))return false;
  }
  return true;
 }
 bool tree_form(U S)const{
  int Uc=0, e_missing=0;
  for(int i=0;i<n;i++)if(!((S>>i)&1))Uc++;
  if(Uc<2)return false;
  for(int e=0;e<m;e++){
   auto [i,j]=edges[e];
   if((S>>i)&1 || (S>>j)&1){if((S>>(n+e))&1)return false;}
   else if(!((S>>(n+e))&1))e_missing++;
  }
  return forest(S)&&e_missing==Uc-1;
 }
};
int main(){
 for(int n=3;n<=5;n++){
  Graph g(n);U total=U(1)<<g.N;
  uint64_t pass=0,mins=0;int mind=100; vector<long> bysize(g.N+1),minby(g.N+1);
  for(U S=0;S<total;S++){
   bool p=g.power(S),f=g.forest(S);if(p!=f){cerr<<"COUNTEREXAMPLE n="<<n<<" S="<<S<<" power="<<p<<" forest="<<f<<"\n";return 1;}
   if(p){pass++;bysize[pop(S)]++;}
   bool m=g.minimal(S),t=g.tree_form(S);if(m!=t){cerr<<"MINIMAL COUNTEREXAMPLE n="<<n<<" S="<<S<<"\n";return 2;}
   if(m){mins++;minby[pop(S)]++;mind=min(mind,pop(S));}
  }
  cout<<"n="<<n<<" vertices="<<g.N<<" states="<<total<<" successful="<<pass<<" minimal="<<mins<<" min_size="<<mind<<"\n";
  cout<<"successful_coeffs:";for(int k=0;k<=g.N;k++)if(bysize[k])cout<<" "<<k<<":"<<bysize[k];cout<<"\n";
  cout<<"minimal_coeffs:";for(int k=0;k<=g.N;k++)if(minby[k])cout<<" "<<k<<":"<<minby[k];cout<<"\n";
 }
 cout<<"VERIFY_OK\n";
}
