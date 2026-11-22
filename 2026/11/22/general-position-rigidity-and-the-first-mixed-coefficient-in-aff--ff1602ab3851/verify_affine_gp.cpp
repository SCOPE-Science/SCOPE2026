// Exhaustive general-position verification for affine incidence graphs AG(2,2) and AG(2,3).
#include <bits/stdc++.h>
using namespace std;
void run(int q){
 int P=q*q,L=q*(q+1),N=P+L;
 vector<vector<int>> adj(N);
 auto edge=[&](int a,int b){adj[a].push_back(b);adj[b].push_back(a);};
 for(int x=0;x<q;x++)for(int y=0;y<q;y++){
  int p=x*q+y;
  for(int m=0;m<q;m++){int b=(y-m*x)%q;if(b<0)b+=q;edge(p,P+m*q+b);}
  edge(p,P+q*q+x);
 }
 vector<vector<int>> d(N,vector<int>(N,100));
 for(int x=0;x<N;x++){queue<int> qu;qu.push(x);d[x][x]=0;
  while(!qu.empty()){int t=qu.front();qu.pop();for(int y:adj[t])if(d[x][y]>d[x][t]+1){d[x][y]=d[x][t]+1;qu.push(y);}}
 }
 vector<vector<unsigned long long>> bad(N,vector<unsigned long long>(N));
 for(int x=0;x<N;x++)for(int y=x+1;y<N;y++)for(int z=y+1;z<N;z++){
  if(d[x][y]+d[y][z]==d[x][z]||d[x][z]+d[z][y]==d[x][y]||d[y][x]+d[x][z]==d[y][z]){
   bad[x][y]|=1ULL<<z;bad[y][x]|=1ULL<<z;
   bad[x][z]|=1ULL<<y;bad[z][x]|=1ULL<<y;
   bad[y][z]|=1ULL<<x;bad[z][y]|=1ULL<<x;
  }
 }
 size_t S=1ULL<<N;vector<unsigned char> valid(S);valid[0]=1;
 unsigned long long maxall=0,nall=0,maxmix=0,nmix=0;
 vector<unsigned long long> poly(N+1);
 unsigned long long pointmask=(1ULL<<P)-1;
 map<pair<int,int>,unsigned long long> mmode;
 for(unsigned long long mask=1;mask<S;mask++){
  int x=__builtin_ctzll(mask);auto rem=mask^(1ULL<<x);
  if(!valid[rem])continue;
  bool ok=true;
  for(auto rr=rem;rr;rr&=rr-1){int y=__builtin_ctzll(rr);
    if(bad[x][y]&rem){ok=false;break;}
  }
  if(!ok)continue;
  valid[mask]=1;
  int k=__builtin_popcountll(mask);poly[k]++;
  if(k>maxall){maxall=k;nall=1;}else if(k==maxall)nall++;
  auto pm=mask&pointmask, lm=mask&~pointmask;
  if(pm && lm){
    mmode[{__builtin_popcountll(pm),__builtin_popcountll(lm)}]++;
    if(k>maxmix){maxmix=k;nmix=1;}else if(k==maxmix)nmix++;
  }
 }
 cout<<"q="<<q<<" point_count="<<P<<" line_count="<<L<<" gp="<<maxall<<" max_count="<<nall
  <<" mixed_max="<<maxmix<<" mixed_max_count="<<nmix<<" tail=";
 for(int k=max(0,P-q+1);k<=P;k++)cout<<"("<<k<<","<<poly[k]<<")";
 cout<<" mixed_types_at_max=";
 for(auto [part,n]:mmode)if(part.first+part.second==maxmix)cout<<"("<<part.first<<","<<part.second<<":"<<n<<")";
 cout<<"\n";
}
int main(){run(2);run(3);}
