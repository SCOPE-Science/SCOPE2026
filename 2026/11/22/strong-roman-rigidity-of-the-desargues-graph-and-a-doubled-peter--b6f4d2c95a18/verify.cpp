// Exhaustive weight-fourteen strong Roman domination certificate for H(5,2).
// Self-contained C++17; compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;
int main() {
 vector<int> P,L;
 for(int m=0;m<32;m++){if(__builtin_popcount((unsigned)m)==2)P.push_back(m);if(__builtin_popcount((unsigned)m)==3)L.push_back(m);}
 array<vector<int>,20> adj;
 for(int i=0;i<10;i++)for(int j=0;j<10;j++)if((P[i]&L[j])==P[i]){adj[i].push_back(10+j);adj[10+j].push_back(i);}
 for(auto &v:adj)assert(v.size()==3);
 set<string> found;
 long long tested=0;
 array<int,20> f{};
 auto inspect=[&](){
   tested++;
   for(int v=0;v<20;v++)if(f[v]==0){
    bool ok=false;
    for(int u:adj[v])if(f[u]>=2){
      int z=0;for(int w:adj[u])z+=(f[w]==0);
      if(f[u]>=1+(z+1)/2){ok=true;break;}
    }
    if(!ok)return;
   }
   string s;for(int x:f)s.push_back(char('0'+x));found.insert(s);
 };
 // The elementary bound w >= 2n/3 implies that at w=14 for n=20,
 // the only feasible (#ones,#twos,#threes) are (0,7,0),(2,6,0),
 // (1,5,1),(0,4,2). Enumerate their labelled placements exactly.
 auto recurse=[&](auto&& self,int v,int n1,int n2,int n3)->void{
   if(v==20){if(n1+n2+n3==0)inspect();return;}
   if(n1+n2+n3>20-v)return;
   if(n1+n2+n3<0)return;
   f[v]=0;self(self,v+1,n1,n2,n3);
   if(n1){f[v]=1;self(self,v+1,n1-1,n2,n3);}
   if(n2){f[v]=2;self(self,v+1,n1,n2-1,n3);}
   if(n3){f[v]=3;self(self,v+1,n1,n2,n3-1);}
   f[v]=0;
 };
 for(auto [a,b,c]:vector<array<int,3>>{{0,7,0},{2,6,0},{1,5,1},{0,4,2}})recurse(recurse,0,a,b,c);
 assert(tested==7441920LL);
 assert(found.size()==40);
 vector<string> F(found.begin(),found.end());
 map<int,int> typecount,distances;
 vector<int> type(F.size());
 for(int i=0;i<(int)F.size();i++){
  const auto &s=F[i];assert(count(s.begin(),s.end(),'1')==2);assert(count(s.begin(),s.end(),'2')==6);assert(count(s.begin(),s.end(),'3')==0);
  int p=-1,l=-1,a=0,b=0;
  for(int v=0;v<20;v++)if(s[v]=='1'){if(v<10){p=P[v];a++;}else{l=L[v-10];b++;}}
  assert(a==1&&b==1);type[i]=(p^l)==31?0:1;
  if(type[i]==1)assert((p&l)==p);
  typecount[type[i]]++;
  for(int v=0;v<20;v++)if(s[v]=='2'){
   int z=0;for(int u:adj[v])z+=(s[u]=='0');assert(z==2);
  }
  for(int v=0;v<20;v++)if(s[v]=='0'){
   int twos=0;for(int u:adj[v])twos+=(s[u]=='2');assert(twos==1);
  }
 }
 assert(typecount[0]==10&&typecount[1]==30);
 vector<vector<int>> H(40);
 for(int i=0;i<40;i++)for(int j=i+1;j<40;j++){
  int diff=0;for(int v=0;v<20;v++)diff+=(F[i][v]!=F[j][v]);distances[diff]++;
  if(diff==6){H[i].push_back(j);H[j].push_back(i);}
 }
 assert((distances==map<int,int>{{6,60},{8,60},{10,180},{12,360},{14,120}}));
 for(int i=0;i<40;i++)assert((int)H[i].size()==(type[i]==0?6:2));
 // The ten degree-six vertices identify with two-subsets of [5].
 // Each pair of disjoint two-subsets is joined by precisely two
 // degree-two vertices, and no intersecting pair is joined.
 map<pair<int,int>,int> double_edges;
 for(int i=0;i<40;i++)if(type[i]==1){assert(H[i].size()==2);int a=H[i][0],b=H[i][1];assert(type[a]==0&&type[b]==0);
   auto getmask=[&](int j){for(int k=0;k<10;k++)if(F[j][k]=='1')return P[k];assert(false);return -1;};
   int u=getmask(a),v=getmask(b);assert((u&v)==0);if(u>v)swap(u,v);double_edges[{u,v}]++;
 }
 assert(double_edges.size()==15);for(auto [p,n]:double_edges)assert(n==2);
 int radius=1000,diam=0;for(int i=0;i<40;i++){
  vector<int>d(40,-1);queue<int>q;d[i]=0;q.push(i);
  while(!q.empty()){int u=q.front();q.pop();for(int v:H[u])if(d[v]<0){d[v]=d[u]+1;q.push(v);}}
  int ecc=*max_element(d.begin(),d.end());assert(*min_element(d.begin(),d.end())==0);radius=min(radius,ecc);diam=max(diam,ecc);
 }
 assert(radius==5&&diam==6);
 cout<<"PASS n=20 edges=30 graph=H(5,2) min_weight=14 explored_weight14="<<tested
     <<" optimum_functions="<<F.size()<<" orbit_sizes=10,30 exchange_threshold=6 exchange_edges=60"
     <<" exchange_graph=doubled_subdivision(Petersen) radius=5 diameter=6\n";
}
