// Reproducible, exhaustive classification of synchronous binary majority on the Folkman graph.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
using namespace std;
int main(){
  constexpr uint32_t M=(1u<<20); vector<array<uint8_t,4>> adjacency(20);array<uint8_t,20> degree{};
  auto edge=[&](int a,int b){adjacency[a][degree[a]++]=b;adjacency[b][degree[b]++]=a;};
  int e=10;
  for(int i=0;i<5;i++)for(int j=i+1;j<5;j++){
    for(int a:{i,5+i,j,5+j})edge(a,e); e++;
  }
  for(auto d:degree)if(d!=4)return 1;
  vector<uint32_t> forward(M);
  for(uint32_t x=0;x<M;x++){
    uint32_t y=0;
    for(int v=0;v<20;v++){
      int n=0;for(uint8_t w:adjacency[v])n+=int((x>>w)&1);
      int z=(n>2)||(n==2&&((x>>v)&1));y|=uint32_t(z)<<v;
    }
    forward[x]=y;
  }
  // Independently enumerate all temporal phases.  Exhaustive two-step equality is necessary and sufficient to detect first periodic entry here.
  vector<uint32_t> a(M),b(M),c(M);for(uint32_t x=0;x<M;x++){a[x]=x;b[x]=forward[x];c[x]=forward[b[x]];}
  vector<int8_t> entry(M,-1),period(M,0);map<int,uint64_t> first_distribution,period_distribution;
  int max_depth=-1;uint32_t example=0;
  for(int d=0;d<24;d++){
    uint64_t newly=0;
    for(uint32_t x=0;x<M;x++)if(entry[x]<0 && a[x]==c[x]){
      entry[x]=d;period[x]=(a[x]==b[x])?1:2;newly++;
      if(d>max_depth){max_depth=d;example=x;}
    }
    first_distribution[d]=newly;
    if(d==24-1 && newly==0)break;
    if(d>0 && newly==0)break;
    for(uint32_t x=0;x<M;x++){a[x]=b[x];b[x]=c[x];c[x]=forward[c[x]];}
  }
  uint64_t nfixed=0,ntwo=0;
  for(uint32_t x=0;x<M;x++){
    if(entry[x]<0){cerr<<"unclassified "<<x<<"\n";return 2;}
    period_distribution[period[x]]++;
    if(entry[x]==0){if(period[x]==1)nfixed++;else ntwo++;}
  }
  // Apply F^max_depth to EVERY state, then identify each temporal orbit by its smallest phase.
  vector<uint32_t> rep(M);for(uint32_t x=0;x<M;x++){
    uint32_t z=x;for(int i=0;i<max_depth;i++)z=forward[z];
    rep[x]=min(z,forward[z]);
  }
  map<uint32_t,uint64_t> basin;for(uint32_t x=0;x<M;x++)basin[rep[x]]++;
  map<uint64_t,uint32_t> spectrum;for(auto [key,size]:basin)spectrum[size]++;
  ifstream cat("basin_catalog.tsv");
 if(cat){
   string head;getline(cat,head);
   if(head!="periodic_representative\tleast_period\tbasin_size")return 4;
   uint32_t k;int p;uint64_t size;size_t found=0;
   while(cat>>k>>p>>size){
     auto it=basin.find(k);
     if(it==basin.end() || it->second!=size || (p!=1 && p!=2) || p!=int(period[k]))return 5;
     found++;
   }
   if(found!=basin.size())return 6;
 }
 cout<<"fixed "<<nfixed<<" two_cycles "<<ntwo/2<<" max_entry "<<max_depth<<" witness "<<example<<"\n";
  cout<<"entry";for(auto [d,n]:first_distribution)cout<<" "<<d<<":"<<n;cout<<"\n";
  cout<<"eventual_period";for(auto [d,n]:period_distribution)cout<<" "<<d<<":"<<n;cout<<"\n";
  cout<<"basin_spectrum";for(auto [d,n]:spectrum)cout<<" "<<d<<":"<<n;cout<<"\n";
  cout<<"total_basins "<<basin.size()<<" unanimous0 "<<basin[0]<<" unanimous1 "<<basin[M-1]<<"\n";
  if(nfixed!=4036 || ntwo!=702 || max_depth!=7 || basin.size()!=4387)return 3;
  return 0;
}
