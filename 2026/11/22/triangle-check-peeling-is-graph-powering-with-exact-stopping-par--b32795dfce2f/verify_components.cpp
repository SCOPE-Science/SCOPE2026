// Independent bit-graph verification of triangle-peeling and partition counts.
// Public reproducibility artifact: all statements refer to a finite explicit model.
#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;
int main(){
 for(int n=3;n<=6;n++){
  vector<pair<int,int>> e; int ix[9][9]; memset(ix,-1,sizeof ix);
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++) {ix[a][b]=ix[b][a]=(int)e.size();e.push_back({a,b});}
  int m=e.size(); assert(m<=15);
  vector<array<int,3>> tris;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)
   tris.push_back({ix[a][b],ix[a][c],ix[b][c]});
  long long num_stops=0,num_success=0;map<int,long long> stop_weights;
  for(int mask=0;mask<(1<<m);mask++){
   // Explicitly simulate parallel recovery on erasure variables from checks.
   int erased=mask, rounds=0;
   for(;;){
    int p=0;
    for(auto &tr:tris){int cnt=0,j=-1;for(auto id:tr)if(erased&(1<<id)){cnt++;j=id;}
     if(cnt==1)p|=1<<j;
    }
    if(!p)break;
    erased&=~p;rounds++;
   }
   // Separately use a fresh adjacency representation for the retained edges.
   int dist[9][9];
   for(int a=0;a<n;a++){
    for(int b=0;b<n;b++)dist[a][b]=1000;
    dist[a][a]=0;
   }
   for(int j=0;j<m;j++)if(!(mask&(1<<j))){auto [a,b]=e[j];dist[a][b]=dist[b][a]=1;}
   for(int k=0;k<n;k++)for(int a=0;a<n;a++)for(int b=0;b<n;b++)
     dist[a][b]=min(dist[a][b],dist[a][k]+dist[k][b]);
   int predicted=0,maxdist=0;
   for(int j=0;j<m;j++){
    auto [a,b]=e[j];if(dist[a][b]==1000)predicted|=1<<j;
   }
   for(int a=0;a<n;a++)for(int b=0;b<n;b++)if(dist[a][b]<1000) maxdist=max(maxdist,dist[a][b]);
   int pred_rounds=0;while((1<<pred_rounds)<maxdist)pred_rounds++;
   if(erased!=predicted || pred_rounds!=rounds){cerr<<"FAIL n="<<n<<" mask="<<mask<<"\n";return 1;}
   if(!erased)num_success++;
   if(erased==mask){num_stops++;stop_weights[__builtin_popcount((unsigned)mask)]++;}
  }
  vector<long long> B(n+1);B[0]=1;
  for(int i=1;i<=n;i++){
   for(int j=0;j<i;j++){
    long long choose=1;for(int k=1;k<=j;k++)choose=choose*(i-k)/k;
    B[i]+=choose*B[j];
   }
  }
  assert(num_stops==B[n]);
  cout<<"n="<<n<<" stopping="<<num_stops<<" success="<<num_success<<" weights:";
  for(auto [k,v]:stop_weights) cout<<" "<<k<<":"<<v;
  cout<<"\n";
 }
}
