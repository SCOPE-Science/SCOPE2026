// Exhaustive independent support search for perfect Roman domination on T_n.
// Assign every edge of K_n that is adjacent to precisely one defender edge label zero;
// all remaining non-defenders receive label one. This minimizes weight for fixed defenders.
#include <iostream>
#include <vector>
#include <cstdint>
#include <algorithm>
using namespace std;
int main(){
 for(int n=3;n<=7;n++){
  vector<pair<int,int>> edges;
  for(int u=0;u<n;u++) for(int v=u+1;v<n;v++) edges.push_back({u,v});
  int N=edges.size(); long long best=1LL<<60, number=0, matching_number=0;
  for(uint32_t mask=0;mask<(1u<<N);mask++){
   int d[8]={}; int t=__builtin_popcount(mask);
   for(int e=0;e<N;e++) if(mask>>e&1u){auto [u,v]=edges[e]; d[u]++;d[v]++;}
   int a=0,b=0,c=0;
   for(int i=0;i<n;i++){if(d[i]==0)a++;else if(d[i]==1)b++;else c++;}
   int weight=N+t-a*b;
   if(weight<best){best=weight;number=0;matching_number=0;}
   if(weight==best){number++;if(c==0)matching_number++;}
  }
  cout<<"n="<<n<<" min="<<best<<" optimal_supports="<<number<<" matching_supports="<<matching_number<<"\n";
 }
}
