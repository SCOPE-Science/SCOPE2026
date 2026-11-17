// Direct labelled-state verification of deterministic open-neighborhood majority.
// Graph: an m-vertex clique plus a vertex adjacent to the first r clique vertices.
#include <iostream>
#include <vector>
#include <cstdint>
#include <cassert>
using namespace std;
using ull=unsigned long long;

ull choose(int n,int k){if(k<0||k>n)return 0; ull z=1;for(int i=1;i<=k;i++)z=z*(n-i+1)/i;return z;}

ull predicted(int m,int r){
 if(m%2==0){int q=m/2;return r<=q?choose(m-r,q):0;}
 int q=(m-1)/2;return choose(r,q+1)+(r==m-1?choose(m-1,q):0);
}

int main(){
 ull checked=0;
 for(int m=3;m<=15;m++) for(int r=1;r<=m;r++){
  const int n=m+1, Z=1<<n;
  vector<unsigned int> adj(n,0);
  for(int a=0;a<m;a++)for(int b=0;b<m;b++)if(a!=b) adj[a]|=1u<<b;
  for(int a=0;a<r;a++){adj[a]|=1u<<m;adj[m]|=1u<<a;}
  auto step=[&](unsigned int x){
   unsigned int y=0;
   for(int a=0;a<n;a++){
    int degree=__builtin_popcount(adj[a]);
    int ones=__builtin_popcount(x&adj[a]);
    int bit=(2*ones==degree)?((x>>a)&1):(2*ones>degree);
    y|=(unsigned int)bit<<a;
   }
   return y;
  };
  ull fixed=0,prim_states=0,incoming=0;
  vector<unsigned char> cycle(Z);
  for(int x=0;x<Z;x++){
   auto y=step(x),z=step(y);
   if(y==x)fixed++;
   else if(z==x){prim_states++;cycle[x]=1;}
  }
  for(int x=0;x<Z;x++)if(!cycle[x]&&cycle[step(x)])incoming++;
  if(fixed!=2 || prim_states!=2*predicted(m,r) || incoming!=0){
    cerr<<"FAILED m="<<m<<" r="<<r<<" fixed="<<fixed<<" prim="<<prim_states<<" inbound="<<incoming<<"\n";
    return 1;
  }
  checked+=Z;
 }
 cout<<"PASS: 117 graphs (m=3..15; 1<=r<=m), "<<checked<<" labelled configurations; fixed=2, exact primitive two-cycle formula, no extraneous one-step predecessors.\n";
}
