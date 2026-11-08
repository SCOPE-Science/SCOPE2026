// Reconstruct triangular graph as the intersection graph of edges of a labeled complete graph.
// Exhaustive closed-neighborhood parity and induced-connectivity checks.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
using namespace std;
using U=uint64_t;
int main(){
 for(int n=3;n<=7;n++){
  vector<pair<int,int>> edges;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.push_back({i,j});
  int E=edges.size();vector<U> closed(E,0),open(E,0);
  for(int i=0;i<E;i++)for(int j=0;j<E;j++){
   bool meet=(edges[i].first==edges[j].first||edges[i].first==edges[j].second||edges[i].second==edges[j].first||edges[i].second==edges[j].second);
   if(meet) closed[i]|=U(1)<<j;
   if(i!=j&&meet)open[i]|=U(1)<<j;
  }
  map<int,long long> all,con;long long tot=0,connected=0;
  for(U mask=0;mask<(U(1)<<E);mask++){
   bool good=true;
   for(U cl:closed)if((__builtin_popcountll(mask&cl)&1)==0){good=false;break;}
   if(!good)continue;
   ++tot;int w=__builtin_popcountll(mask);all[w]++;
   U seen=0,front=mask&-mask;
   while(front){seen|=front;U next=0;
     for(int i=0;i<E;i++)if(front>>i&1)next|=open[i];
     front=next&mask&~seen;
   }
   if(seen==mask){++connected;con[w]++;}
  }
  map<int,long long> exp,expcon;
  if(n%2==0){exp[E]=1;expcon[E]=1;}
  else{
   for(int a=0;a<=n;a+=2){
    long long choose=1;for(int j=1;j<=a;j++)choose=choose*(n-j+1)/j;
    int w=a*(a-1)/2+(n-a)*(n-a-1)/2;
    exp[w]+=choose;
    if(a==0||a==n-1)expcon[w]+=choose;
   }
  }
  if(all!=exp||con!=expcon){cerr<<"FAILED n="<<n<<"\n";return 1;}
  cout<<"n="<<n<<" solutions="<<tot<<" connected="<<connected<<" weights=";
  for(auto [k,v]:all)cout<<k<<":"<<v<<",";
  cout<<" connected_weights=";
  for(auto [k,v]:con)cout<<k<<":"<<v<<",";
  cout<<" CHECKED\n";
 }
 cout<<"DIRECT_EXHAUSTIVE_PASS\n";
}
