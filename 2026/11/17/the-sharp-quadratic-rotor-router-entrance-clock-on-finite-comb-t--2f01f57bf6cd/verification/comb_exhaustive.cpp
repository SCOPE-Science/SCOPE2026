#include <bits/stdc++.h>
using namespace std;
int main(){
for(int n=2;n<=12;n++){
 int N=2*n; vector<vector<int>> adj(N);
 for(int i=0;i<n;i++){
  if(i>0)adj[i].push_back(i-1);
  adj[i].push_back(n+i);
  if(i<n-1)adj[i].push_back(i+1);
  adj[n+i].push_back(i);
 }
 long long configs=1;for(int i=0;i<n;i++)configs*=adj[i].size();
 if(configs>1000000)break;
 int max_t=0,min_t=INT_MAX;long long ctmax=0;map<int,long long> hist;vector<int> best;
 for(long long mask=0;mask<configs;mask++){
  long long mm=mask;vector<int> rotor(N,0);
  for(int i=0;i<n;i++){rotor[i]=mm%adj[i].size();mm/=adj[i].size();}
  auto initial=rotor;int chip=0,t=0; int lim=2000;
  while(t<=lim){
   // recurrent if exactly one 2-cycle in rotor functional digraph, and chip on its two endpoints
   int nc=0, x=-1,y=-1;
   for(int v=0;v<N;v++){
    int w=adj[v][rotor[v]];
    if(w>v && adj[w][rotor[w]]==v){nc++;x=v;y=w;}
   }
   if(nc==1 && (chip==x || chip==y))break;
   rotor[chip]=(rotor[chip]+1)%adj[chip].size();chip=adj[chip][rotor[chip]];t++;
  }
  if(t>lim){cerr<<"nonconv";return 1;}
  hist[t]++;
  if(t>max_t){max_t=t;ctmax=1;best=initial;}else if(t==max_t)ctmax++;
  min_t=min(min_t,t);
 }
 cout<<"n="<<n<<" count="<<configs<<" max="<<max_t<<" multiplicity="<<ctmax<<" min="<<min_t<<" initials=";for(int i=0;i<n;i++)cout<<best[i]<<",";cout<<"\n";
}
}
