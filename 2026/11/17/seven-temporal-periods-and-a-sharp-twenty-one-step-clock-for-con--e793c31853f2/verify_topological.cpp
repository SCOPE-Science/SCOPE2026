#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
static constexpr int H=4,W=5,N=20,LIMIT=1<<N;
int step(int z) {
 int out=0;
 for(int r=0;r<H;r++)for(int c=0;c<W;c++) {
  int count=0;
  for(int dr=-1;dr<=1;dr++)for(int dc=-1;dc<=1;dc++) if(dr||dc) {
   int rr=(r+dr+H)%H, cc=(c+dc+W)%W;
   count+=(z>>(rr*W+cc))&1;
  }
  if(count==3 || (count==2 && ((z>>(r*W+c))&1))) out|=1<<(r*W+c);
 }
 return out;
}
int action(int z,int a,int b,int d,int e) {
 int out=0;
 for(int r=0;r<H;r++)for(int c=0;c<W;c++)if((z>>(r*W+c))&1)
   out|=1<<(((a*r+b+H)%H)*W+((d*c+e+W)%W));
 return out;
}
int main(){
 vector<int> to(LIMIT), degree(LIMIT,0),order;order.reserve(LIMIT);
 for(int s=0;s<LIMIT;s++){to[s]=step(s);++degree[to[s]];}
 queue<int> q;
 for(int s=0;s<LIMIT;s++)if(degree[s]==0)q.push(s);
 while(!q.empty()){int s=q.front();q.pop();order.push_back(s);if(--degree[to[s]]==0)q.push(to[s]);}
 vector<int> owner(LIMIT,-1),dist(LIMIT,-1);vector<int> periods,representatives;
 map<int,int> counts;
 for(int s=0;s<LIMIT;s++)if(degree[s]>0 && owner[s]<0){
  int id=periods.size(),t=s,p=0;
  do {owner[t]=id;dist[t]=0;t=to[t];p++;}while(t!=s);
  periods.push_back(p);representatives.push_back(s);counts[p]++;
 }
 for(auto it=order.rbegin();it!=order.rend();++it){int s=*it;owner[s]=owner[to[s]];dist[s]=1+dist[to[s]];}
 map<int,long long> entries,basins;vector<int> basinSize(periods.size(),0);
 for(int s=0;s<LIMIT;s++){if(owner[s]<0 || dist[s]<0){cerr<<"Unclassified state";return 2;}entries[dist[s]]++;basins[periods[owner[s]]]++;basinSize[owner[s]]++;}
 map<int,int> fixed_group_sum,types, orbit_size_check;map<int,map<int,int>> typesBySize;
 for(int id=0;id<(int)periods.size();id++){
  int fixed=0,r=representatives[id];
  for(int a:{-1,1})for(int b=0;b<H;b++)for(int d:{-1,1})for(int e=0;e<W;e++){
   int t=action(r,a,b,d,e);
   if(dist[t]!=0){cerr<<"Symmetry fails periodicity";return 3;}
   if(owner[t]==id)fixed++;
  }
  if(fixed<1 || 80%fixed){cerr<<"Bad stabilizer";return 4;}
  fixed_group_sum[periods[id]]+=fixed;
  typesBySize[periods[id]][80/fixed]++;
 }
 for(auto &[p,bs]:typesBySize)for(auto &[siz,val]:bs){if(val%siz){cerr<<"Bad class orbit division";return 5;}val/=siz;types[p]+=val;}
 // Burnside sum over (g, temporal orbits); independently each orbit contributes its stabilizer.
 for(auto [p,num]:types)if(fixed_group_sum[p]!=80*num){cerr<<"Burnside mismatch";return 6;}
 cout<<"cycle counts:";for(auto [p,n]:counts)cout<<" "<<p<<":"<<n;cout<<"\nentry:";for(auto [t,n]:entries)cout<<" "<<t<<":"<<n;cout<<"\nbasins:";for(auto [p,n]:basins)cout<<" "<<p<<":"<<n;
 cout<<"\nmax basin "<<*max_element(basinSize.begin(),basinSize.end())<<" cycles "<<periods.size()<<"\n";
 cout<<"geometry:";for(auto [p,bySize]:typesBySize){cout<<" period="<<p<<"{";for(auto [s,val]:bySize)cout<<s<<":"<<val<<",";cout<<"}";}cout<<"\ntypes "<<accumulate(types.begin(),types.end(),0,[](int total,const auto &kv){return total+kv.second;})<<"\n";
 // Proof certificate: all state transitions assigned to precisely one cycle; periodic nodes checked.
 long long periodic=0;for(int x:periods)periodic+=x;
 cout<<"periodic states "<<periodic<<"; nonperiodic "<<order.size()<<"; total "<<LIMIT<<"; max entry "<<entries.rbegin()->first<<"\n";
}
