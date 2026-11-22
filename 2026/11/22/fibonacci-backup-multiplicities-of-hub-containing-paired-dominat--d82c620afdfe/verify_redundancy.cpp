// Standalone direct graph enumeration of matching backup multiplicity in wheels.
#include <bits/stdc++.h>
using namespace std;
long long fib(int n){long long a=0,b=1;for(int i=0;i<n;i++){auto c=a+b;a=b;b=c;}return a;}
int main(){
 for(int n=3;n<=16;n++){
  int V=n+1,N=1<<V;vector<int> adj(V,0);
  for(int i=0;i<n;i++)for(int j: {(i+1)%n,n}) {adj[i]|=1<<j;adj[j]|=1<<i;}
  vector<int> M(N,0);M[0]=1; // number of perfect matchings of selected subgraph
  for(int s=1;s<N;s++){
    if(__builtin_popcount((unsigned)s)%2)continue;
    int a=__builtin_ctz((unsigned)s), t=s^(1<<a);
    for(int r=t&adj[a];r;r&=r-1){int b=__builtin_ctz((unsigned)r);M[s]+=M[t^(1<<b)];}
  }
  long long total=0,unique=0,witness=0;
  int hub=1<<n;
  for(int s=hub;s<N;s++)if(s&hub){
    if(!M[s])continue;
    total++;witness+=M[s];unique+=(M[s]==1);
  }
  long long expectedTotal=n*fib(n-1)+(n%2),expectedUnique=n*fib(n-2),expectedWitness=n*fib(n);
  if(total!=expectedTotal||unique!=expectedUnique||witness!=expectedWitness){cerr<<"ERROR n="<<n<<" got "<<total<<","<<unique<<","<<witness<<" expected "<<expectedTotal<<","<<expectedUnique<<","<<expectedWitness<<"\n";return 1;}
 }
 cout<<"VERIFY_OK rim_orders=3..16 graph_matching_DP=PASS hub_containing_sets=n*F_(n-1)+odd unique_matching_sets=n*F_(n-2) total_matchings=n*F_n\n";
}
