// Independent functional-graph exploration of the 3-color Greenberg-Hastings rule
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
static constexpr int NV=15;
struct Graph{
 array<array<int,6>,NV> neighbor{};
 array<int,16> powers{};
 Graph(){
  vector<pair<int,int>> lab;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)lab.emplace_back(i,j);
  for(int i=0;i<NV;i++){int z=0;for(int j=0;j<NV;j++){if(i==j)continue;auto a=lab[i],b=lab[j];if(a.first!=b.first&&a.first!=b.second&&a.second!=b.first&&a.second!=b.second)neighbor[i][z++]=j;}if(z!=6)throw 1;}
  powers[0]=1;for(int i=1;i<=NV;i++)powers[i]=3*powers[i-1];
 }
 int advance(int x)const{
  array<unsigned char,NV> c{};
  for(int i=0;i<NV;i++){c[i]=x%3;x/=3;}
  int y=0;
  for(int i=0;i<NV;i++){
   int t=0;
   if(c[i]==1)t=2;
   else if(c[i]==0){bool neighborExcited=false;for(int j:neighbor[i]){if(c[j]==1){neighborExcited=true;break;}}t=neighborExcited?1:0;}
   y+=powers[i]*t;
  }
  return y;
 }
};
int main(){Graph G;int N=G.powers[NV];vector<uint8_t> mark(N),per(N),dist(N);vector<int> path;path.reserve(256);
 map<pair<int,int>,long long> table;
 map<int,long long> cycles;
 int max_path=0;
 for(int x=0;x<N;x++)if(mark[x]==0){
  path.clear();int y=x;
  while(mark[y]==0){mark[y]=1;path.push_back(y);y=G.advance(y);}
  if(mark[y]==1){
   int k=int(path.size())-1;
   while(k>=0&&path[k]!=y)k--;
   if(k<0){cerr<<"ERROR: unsatisfied open-path marking\n";return 1;}
   int len=int(path.size())-k;
   cycles[len]++;
   for(int j=k;j<int(path.size());j++){int z=path[j];per[z]=len;dist[z]=0;mark[z]=2;table[{0,len}]++;}
   path.resize(k);
  }
  while(!path.empty()){
   int z=path.back();path.pop_back();int nxt=G.advance(z);
   if(mark[nxt]!=2){cerr<<"ERROR: successor not closed\n";return 1;}
   per[z]=per[nxt];if(dist[nxt]==255){cerr<<"ERROR: bound\n";return 1;}
   dist[z]=dist[nxt]+1;mark[z]=2;table[{dist[z],per[z]}]++;
   max_path=max(max_path,int(dist[z]));
  }
 }
 long long s=0;for(auto [k,c]:table)s+=c;if(s!=N)return 1;
 ofstream f("forward_census.txt");
 f<<"N "<<N<<" maxT "<<max_path<<"\n";
 for(auto [p,c]:cycles)f<<"P "<<p<<" "<<c<<"\n";
 for(auto [tp,c]:table)f<<"J "<<tp.first<<" "<<tp.second<<" "<<c<<"\n";
 cout<<"VERIFIED_ALL_STATES "<<N<<" maxT "<<max_path<<" cycles "<<cycles.size()<<" joint "<<table.size()<<"\n";
}
