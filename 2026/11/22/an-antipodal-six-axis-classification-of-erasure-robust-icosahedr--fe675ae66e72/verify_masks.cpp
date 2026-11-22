// Independent bitmask verification using a literal 30-edge incidence list.
// Standard C++17 only. No graph libraries or scientific datasets are required.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
static int pc(unsigned x){return __builtin_popcount(x);}
int main(){
 const array<pair<int,int>,30> edges = {{{0,1},{0,2},{0,3},{0,4},{0,5},
 {1,2},{1,5},{1,6},{1,10},{2,3},{2,6},{2,7},
 {3,4},{3,7},{3,8},{4,5},{4,8},{4,9},{5,9},{5,10},
 {6,7},{6,10},{6,11},{7,8},{7,11},{8,9},{8,11},{9,10},{9,11},{10,11}}};
 array<unsigned,12> closed{};
 for(int i=0;i<12;i++)closed[i]=1u<<i;
 for(auto [a,b]:edges){closed[a]|=1u<<b;closed[b]|=1u<<a;}
 for(auto n:closed)assert(pc(n)==6);
 vector<unsigned> requirements;
 for(int i=0;i<12;i++)requirements.push_back(closed[i]);
 for(int a=0;a<12;a++)for(int b=a+1;b<12;b++) requirements.push_back(closed[a]^closed[b]);
 assert(requirements.size()==78);
 array<vector<unsigned>,5> optimum;
 for(unsigned mask=0;mask<(1u<<12);mask++){
   int cap=5;
   for(unsigned r:requirements)cap=min(cap,pc(mask&r));
   for(int t=1;t<=4;t++)if(cap>=t)optimum[t].push_back(mask);
 }
 const array<int,5> minsz={{0,5,6,11,12}};
 const array<int,5> num={{0,120,20,12,1}};
 for(int t=1;t<=4;t++){
   int k=13;for(unsigned x:optimum[t])k=min(k,pc(x));
   int cnt=0;for(unsigned x:optimum[t])if(pc(x)==k)cnt++;
   assert(k==minsz[t]&&cnt==num[t]);
   optimum[t].erase(remove_if(optimum[t].begin(),optimum[t].end(),
     [k](unsigned x){return pc(x)!=k;}),optimum[t].end());
 }
 assert(optimum[4].size()==1&&optimum[4][0]==4095u);
 // Antipodal pairs, obtained independently by the graph-distance metric.
 int d[12][12];
 for(int i=0;i<12;i++){
   for(int j=0;j<12;j++)d[i][j]=100;
   d[i][i]=0;
   vector<int> q={i};
   for(size_t z=0;z<q.size();z++){
     int v=q[z];for(int u=0;u<12;u++)if(u!=v&&(closed[v]>>u&1)&&d[i][u]==100)
      {d[i][u]=d[i][v]+1;q.push_back(u);}
   }
 }
 vector<pair<int,int>> pairs;
 for(int i=0;i<12;i++)for(int j=i+1;j<12;j++)if(d[i][j]==3)pairs.push_back({i,j});
 assert(pairs.size()==6);
 map<unsigned,int> delta;
 for(auto [u,v]:edges)delta[closed[u]^closed[v]]++;
 assert(delta.size()==15);
 for(auto [mask,count]:delta){
   assert(count==2&&pc(mask)==4);
   int np=0;for(auto [a,b]:pairs)if((mask>>a&1)&&(mask>>b&1))np++;
   assert(np==2);
 }
 for(auto [a,b]:pairs)for(int v=0;v<12;v++)assert(((closed[v]>>a)&1)!=((closed[v]>>b)&1));
 // All 20 optimal 6-sets are 3-suns, with one pendant leaf per triangle hub.
 set<unsigned> suns;
 for(int a=0;a<12;a++)for(int b=a+1;b<12;b++)for(int c=b+1;c<12;c++)
  if((closed[a]>>b&1)&&(closed[a]>>c&1)&&(closed[b]>>c&1)){
    unsigned face=(1u<<a)|(1u<<b)|(1u<<c), leaves=0;
    for(int v=0;v<12;v++)if(!(face>>v&1)&&pc((closed[v]&~(1u<<v))&face)==1)
      leaves|=1u<<v;
    assert(pc(leaves)==3);
    for(auto [u,v]:edges)assert(!((leaves>>u&1)&&(leaves>>v&1)));
    suns.insert(face|leaves);
  }
 assert(suns.size()==20&&set<unsigned>(optimum[2].begin(),optimum[2].end())==suns);
 for(unsigned m:optimum[1]){
   int nex=0;for(unsigned n:optimum[2])if((m&n)==m)nex++;
   assert(nex==1);
 }
 for(int t=1;t<=4;t++)cout<<t<<":"<<minsz[t]<<"/"<<num[t]<<" ";
 cout<<"; antipodal blocks=15x2; faces/suns=20; unique extensions=120; PASS\n";
}
