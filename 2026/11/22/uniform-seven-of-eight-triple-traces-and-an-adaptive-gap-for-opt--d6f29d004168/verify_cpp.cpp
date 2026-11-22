// Standalone independent C++17 check for optimal radius-one Q4 covering codes.
// Run: c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp && ./verify_cpp
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <tuple>
#include <unordered_map>
#include <vector>
using namespace std;
static inline int pop(int v){return __builtin_popcount((unsigned)v);}
static void require(bool p,const char *s){if(!p)throw runtime_error(s);}
int main(){
 array<int,16> N{};
 for(int v=0;v<16;v++){
   N[v]=1<<v;
   for(int k=0;k<4;k++) N[v]|=1<<(v^(1<<k));
 }
 vector<int> C;
 int mincard=17;
 for(int mask=0;mask<(1<<16);mask++){
   int size=pop(mask);
   if(size>mincard)continue;
   int cover=0;
   for(int v=0;v<16;v++)if(mask>>v&1)cover|=N[v];
   if(cover!=65535)continue;
   if(size<mincard){C.clear();mincard=size;}
   C.push_back(mask);
 }
 require(mincard==4 && C.size()==40,"optima");
 int type2=0,type4=0;
 for(int code:C){
   vector<int> ev,od;
   for(int v=0;v<16;v++)if(code>>v&1){
     if(pop(v)%2==0)ev.push_back(v); else od.push_back(v);
   }
   require(ev.size()==2&&od.size()==2,"parity counts");
   int de=pop(ev[0]^ev[1]),doo=pop(od[0]^od[1]);
   require(de==doo,"parity distance agreement");
   if(de==2)type2++; else if(de==4)type4++; else throw runtime_error("type");
 }
 require(type2==24&&type4==16,"type census");
 map<pair<int,array<int,4>>,int> pairs;
 for(int x=0;x<16;x++)for(int y=x+1;y<16;y++){
   array<int,4> ct{};
   for(int code:C)ct[(((code>>x)&1)<<1)|((code>>y)&1)]++;
   pairs[{pop(x^y),ct}]++;
 }
 for(int d=1;d<=4;d++){
   int cnt=(d==1?32:d==2?48:d==3?32:8);
   array<int,4> tr=d<=2?array<int,4>{21,9,9,1}:array<int,4>{24,6,6,4};
   require(pairs[{d,tr}]==cnt,"pair count");
 }
 require(pairs.size()==4,"extra pair signatures");
 map<pair<array<int,3>,int>,int> triple_types;
 int all7=0;
 for(int x=0;x<16;x++)for(int y=x+1;y<16;y++)for(int z=y+1;z<16;z++){
   array<int,3> dis={pop(x^y),pop(x^z),pop(y^z)};
   sort(dis.begin(),dis.end());
   array<int,8> ct{};
   for(int c:C){int s=(((c>>x)&1)<<2)|(((c>>y)&1)<<1)|((c>>z)&1);ct[s]++;}
   int zeros=0,missing=-1;
   for(int j=0;j<8;j++)if(ct[j]==0){zeros++;missing=j;}
   require(zeros==1,"triple exactly 7 traces");
   triple_types[{dis,pop(missing)}]++;
   all7++;
 }
 require(all7==560 && triple_types.size()==6,"triple count");
 vector<pair<pair<array<int,3>,int>,int>> expected={
   {{{1,1,2},3},96},{{{1,2,3},3},192},{{{1,3,4},2},64},
   {{{2,2,2},3},64},{{{2,2,4},3},48},{{{2,3,3},2},96}
 };
 for(auto &e:expected)require(triple_types[e.first]==e.second,"triple geometry");
 // Dynamic recursion over all reachable subfamilies; 40 bits fit in uint64_t.
 uint64_t all=(uint64_t(1)<<C.size())-1;
 array<uint64_t,16> Q{};
 for(int v=0;v<16;v++)for(size_t j=0;j<C.size();j++)if(C[j]>>v&1)Q[v]|=uint64_t(1)<<j;
 unordered_map<uint64_t,int> memo;
 auto ld=[&](auto&& self,uint64_t family)->int{
   auto it=memo.find(family);if(it!=memo.end())return it->second;
   int best=0;
   for(uint64_t q:Q){
     uint64_t yes=family&q,no=family&(~q)&all;
     if(yes&&no)best=max(best,1+min(self(self,yes),self(self,no)));
   }
   memo[family]=best;return best;
 };
 require(ld(ld,all)==3,"Littlestone dimension");
 require(ld(ld,Q[0])==2,"positive branch upper");
 // The explicit depth-three complete tree: eight leaves.
 const int branches[8][3][2]={
   {{0,1},{7,1},{8,1}},{{0,1},{7,1},{8,0}},
   {{0,1},{7,0},{1,1}},{{0,1},{7,0},{1,0}},
   {{0,0},{1,1},{2,1}},{{0,0},{1,1},{2,0}},
   {{0,0},{1,0},{2,1}},{{0,0},{1,0},{2,0}}
 };
 for(auto &branch:branches){
   bool exists=false;
   for(int c:C){
     bool ok=true;
     for(auto &query:branch)if(((c>>query[0])&1)!=query[1])ok=false;
     if(ok)exists=true;
   }
   require(exists,"nonempty witness leaf");
 }
 cout<<"gamma=4; minimum_codes=40; two_parity_orbits=(16,24)\n";
 cout<<"pair_distance_classes=32,48,32,8; all_pairs_shattered=120\n";
 cout<<"triple_geometry_class_sizes=96,192,64,64,48,96\n";
 cout<<"every_one_of_560_triples_has_exactly_7_of_8_traces\n";
 cout<<"shattering_polynomial=1+16*z+120*z^2\n";
 cout<<"VCdim=2; Ldim=3; witness_leaves=8\n";
 cout<<"DP_states="<<memo.size()<<"\nPASS\n";
}
