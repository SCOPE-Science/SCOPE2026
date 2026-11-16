// Exact signed source-component recurrence for strong tournaments.
// g++ -O3 -std=c++17 verify_tournament_scc.cpp -o scc && ./scc [--dump filename]
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
int main(int argc, char **argv){
 const int n=6, m=15, N=1<<m, T=1<<n;
 vector<pair<int,int>> edges; int eindex[6][6]{};
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){eindex[i][j]=eindex[j][i]=edges.size();edges.emplace_back(i,j);}
 int internal[T]{}, cross[T][T]{}, count[T]{};
 for(int v=0;v<T;v++){
  count[v]=__builtin_popcount((unsigned)v);
  for(int k=0;k<m;k++) if((v>>edges[k].first&1)&&(v>>edges[k].second&1))internal[v]|=1<<k;
  for(int u=v;u;u=(u-1)&v){int r=v^u; for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if((u>>i&1)&&(r>>j&1))cross[u][r]|=1<<eindex[i][j];}
 }
 vector<int> W(N);
 for(int s=0;s<N;s++){
  int H[T]{}, F[T]{}; H[0]=1;
  for(int v=1;v<T;v++)H[v]=(s&internal[v])?0:(1<<(count[v]*(count[v]-1)/2));
  for(int v=1;v<T;v++){
   int val=H[v];
   for(int u=(v-1)&v;u;u=(u-1)&v){int r=v^u;
    int term=F[u]*H[r];
    if(__builtin_parity((unsigned)(s&cross[u][r])))val+=term;else val-=term;
   }
   F[v]=val;
  }
  W[s]=F[T-1];
 }
 int min_pos=INT32_MAX,rank=0;long long moment=0;map<int,int> hist;
 for(auto z:W){hist[abs(z)]++;moment+=1LL*z*z;if(z){rank++;min_pos=min(min_pos,abs(z));}}
 assert(W[0]==22320 && rank==8416 && min_pos==16 && hist[0]==24352);
 assert(moment==32768LL*22320);
 vector<int> P(N);for(int i=0;i<N;i++)P[i]=(W[i]!=0);
 for(int len=1;len<N;len*=2)for(int i=0;i<N;i+=2*len)for(int j=0;j<len;j++){
  int a=P[i+j],b=P[i+j+len];P[i+j]=a+b;P[i+j+len]=a-b;
 }
 long long abs_sum=0;for(auto z:P)abs_sum+=abs(z);assert(abs_sum==1399040);
 cout<<"signed-SCC DP: total="<<W[0]<<" rank="<<rank<<" min="<<min_pos<<" projection_numerator="<<abs_sum<<"\n";
 cout<<"hist:";for(auto [k,v]:hist)cout<<" "<<k<<":"<<v;cout<<"\n";
 if(argc==3 && string(argv[1])=="--dump"){ofstream f(argv[2]);for(int z:W)f<<z<<'\n';}
}
