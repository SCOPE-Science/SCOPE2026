// Exhaustive ordered-separation orbit census for cubic Boolean forms in five variables.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra check_cubic_orbits.cpp -o check_cubic_orbits
// Run: ./check_cubic_orbits
// No external data or libraries are required.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <vector>
using U=uint32_t;
int pop(U x) {return __builtin_popcount(x);}
void require(bool t,const char *reason){if(!t)throw std::runtime_error(reason);}
struct DSU {
  std::vector<int> parent,sz;
  explicit DSU(int n):parent(n),sz(n,1){std::iota(parent.begin(),parent.end(),0);}
  int get(int x){while(x!=parent[x]){parent[x]=parent[parent[x]];x=parent[x];}return x;}
  void unite(int a,int b){a=get(a);b=get(b);if(a==b)return;if(sz[a]<sz[b])std::swap(a,b);parent[b]=a;sz[a]+=sz[b];}
};
int main(){
 std::vector<U> mon;
 for(int d=2;d<=3;d++)for(U b=0;b<32;b++)if(pop(b)==d)mon.push_back(b);
 require(mon.size()==20,"20 monomials");
 std::array<std::array<U,32>,20> rowbasis{};
 for(int i=0;i<20;i++)for(U x=0;x<32;x++)for(U z=0;z<32;z++){
   U m=mon[i];U bit=(((x^z)&m)==m) ^ (((x&m)==m)) ^ (((z&m)==m));
   if(bit)rowbasis[i][x] |= U(1)<<z;
 }
 std::array<U,32> rows{};
 std::vector<U> good;good.reserve(700000);
 int tested=0;
 for(U iteration=0;iteration<(1U<<20);iteration++){
   U mask=iteration^(iteration>>1);
   if(iteration){int i=__builtin_ctz(iteration);for(int x=0;x<32;x++)rows[x]^=rowbasis[i][x];}
   if((mask>>10)==0)continue;
   tested++;
   bool valid=true;
   for(int x=1;valid&&x<32;x++){
     if(rows[x]==0){valid=false;break;}
     for(int y=1;y<x;y++)if((rows[x]&~rows[y])==0||(rows[y]&~rows[x])==0){valid=false;break;}
   }
   if(valid) good.push_back(mask);
 }
 require(tested==1047552,"number of cubic forms");
 require(good.size()==690432,"number of ordered separating forms modulo linear functions");
 // Independently test all representatives by full truth tables and trilinear radicals.
 const U repr[9]={1536,1543,20644,20484,20784,20480,20650,20640,20652};
 for(U mask:repr){
   int radical_cardinality=0;
   for(U v=0;v<32;v++){
     bool in_radical=true;
     for(int i=0;i<5;i++)for(int j=i+1;j<5;j++){
       int contraction=0;
       U ij=(1U<<i)|(1U<<j);
       for(int t=10;t<20;t++)if(mask&(1U<<t)){
         U triple=mon[t];
         if((triple&ij)==ij){ U rem=triple^ij; contraction^=((v&rem)==rem); }
       }
       if(contraction)in_radical=false;
     }
     if(in_radical)radical_cardinality++;
   }
   require(radical_cardinality==((mask==1536||mask==1543)?4:1),"third polar radical dimension");
   U table=0;
   for(U x=0;x<32;x++){
     int a=0;for(int i=0;i<20;i++)if(mask&(1U<<i)) a^=((x&mon[i])==mon[i]);
     table|=U(a)<<x;
   }
   for(int x=1;x<32;x++)for(int y=1;y<32;y++)if(y!=x){
     bool witness=false;
     for(int z=0;z<32;z++){
       int dx=((table>>(x^z))^(table>>x)^(table>>z))&1;
       int dy=((table>>(y^z))^(table>>y)^(table>>z))&1;
       if(dx==1&&dy==0){witness=true;break;}
     }
     require(witness,"direct triple-loop ordered separation of representative");
   }
 }
 std::vector<int> idx(1<<20,-1);
 for(int t=0;t<(int)good.size();t++)idx[good[t]]=t;
 DSU dsu((int)good.size());
 // Adjacent swaps and one elementary transvection generate GL(5,2).
 for(int g=0;g<5;g++){
  std::array<U,20> transformed_basis{};
  for(int i=0;i<20;i++){
   std::array<uint8_t,32> f{};
   for(U x=0;x<32;x++){
    U v=x;
    if(g<4){U two=(v>>g)&3U;if(two==1||two==2)v^=(3U<<g);}
    else if(x&2U)v^=1U;
    f[x]=((v&mon[i])==mon[i]);
   }
   // ANF recovered by complete Boolean-lattice Möbius inversion.
   for(int b=0;b<5;b++)for(int x=0;x<32;x++)if(x&(1<<b))f[x]^=f[x^(1<<b)];
   for(int j=0;j<20;j++)if(f[mon[j]])transformed_basis[i]|=U(1)<<j;
  }
  int missing=0;
  for(int t=0;t<(int)good.size();t++){
   U x=good[t],out=0;
   while(x){int bit=__builtin_ctz(x);out^=transformed_basis[bit];x&=x-1;}
   if(idx[out]==-1){missing++;continue;}
   dsu.unite(t,idx[out]);
  }
  require(missing==0,"GL generators must preserve ordered separation");
 }
 std::map<int,std::pair<int,U>> orbits;
 for(int i=0;i<(int)good.size();i++){
   int r=dsu.get(i);if(!orbits.count(r))orbits[r]={0,good[i]};
   ++orbits[r].first;orbits[r].second=std::min(orbits[r].second,good[i]);
 }
 require(orbits.size()==9,"nine GL-plus-linear orbit classes");
 std::map<U,int> census;
 for(auto [r,pair]:orbits)census[pair.second]=pair.first;
 const std::map<U,int> expectation={{1536,69440},{1543,9920},{20484,208320},{20480,13888},{20640,8680},{20644,52080},{20650,5208},{20652,156240},{20784,166656}};
 require(census==expectation,"orbit representatives and sizes");
 U maskM=0,maskO=0,maskDelta=0,maskExtension=0;
 for(int j=0;j<20;j++){
   if(pop(mon[j])==3)maskM|=1U<<j;
   maskO|=1U<<j;
   if(mon[j]==6||mon[j]==19||mon[j]==13)maskDelta|=1U<<j;
   if(mon[j]==7||mon[j]==24)maskExtension|=1U<<j;
 }
 require(maskM==1047552 && maskO==1048575 && maskDelta==20484 && maskExtension==1536, "published special form coefficient masks");
 std::map<int,U> representative_by_root;
 for(auto [r,v]:orbits)representative_by_root[r]=v.second;
 std::cout << "CUBIC_FIVE_ORBIT_CENSUS_OK tested=" << tested << " ordered_separating=" << good.size()
  << " with_linear=" << good.size()*32U << " orbits=" << census.size() << "\n";
 for(auto [m,size]:census)std::cout << "orbit_min_mask=" << m << " size=" << size << "\n";
 for(auto [label,m]:std::vector<std::pair<const char*,U>>{{"M",maskM},{"O",maskO},{"delta",maskDelta},{"quadratic_extension",maskExtension}}){
   require(idx[m]>=0,"known literature construction satisfies separation");
   std::cout << "known_form=" << label << " orbit_min_mask=" << representative_by_root.at(dsu.get(idx[m])) << "\n";
 }
}
