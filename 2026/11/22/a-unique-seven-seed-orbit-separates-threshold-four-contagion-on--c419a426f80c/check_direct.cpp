// Exhaustive direct synchronous bootstrap infection on two 16-vertex graphs.
// C++17, no external dependencies. Vertex label: 4*a+b, a,b in {0,1,2,3}.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int FULL=(1<<16)-1;
int label(int a,int b){return ((a+4)%4)*4+(b+4)%4;}
int pc(int x){return __builtin_popcount((unsigned)x);}
array<int,16> make_graph(bool shrikhande){
 array<int,16> n{};
 for(int v=0;v<16;++v){
  int a=v/4,b=v%4;
  if(shrikhande){
   for(const auto &d:vector<pair<int,int>>{{1,0},{-1,0},{0,1},{0,-1},{1,1},{-1,-1}})
    n[v] |= 1<<label(a+d.first,b+d.second);
  }else{
   for(int u=0;u<16;++u) if(u!=v && (u/4==a || u%4==b))n[v]|=1<<u;
  }
 }
 for(int v=0;v<16;++v){
  assert(pc(n[v])==6 && !(n[v]&(1<<v)));
  for(int w=0;w<16;++w) if(w!=v){
   assert(((n[v]>>w)&1)==((n[w]>>v)&1));
   assert(pc(n[v]&n[w])==2);
  }
 }
 return n;
}
int infection_time(const array<int,16>&n,int seed){
 int active=seed;
 for(int t=0;t<17;++t){
  if(active==FULL)return t;
  int next=active;
  for(int v=0;v<16;++v) if(!(active&(1<<v)) && pc(active&n[v])>=4)
   next|=1<<v;
  if(next==active)return -1;
  active=next;
 }
 assert(false);return -1;
}
void analyze(const string &name,bool sh){
 auto n=make_graph(sh);
 vector<int> tm(1<<16);
 for(int s=0;s<=FULL;++s)tm[s]=infection_time(n,s);
 map<int,int> successes_by_size;
 map<pair<int,int>,int> minimal_by_size_and_time;
 int minimal7degree=0, all7degree=0;
 for(int s=0;s<=FULL;++s){
  if(tm[s]<0)continue;
  ++successes_by_size[pc(s)];
  bool minimal=true;
  for(int v=0;v<16;++v) if((s&(1<<v)) && tm[s^(1<<v)]>=0){minimal=false;break;}
  if(minimal){
   ++minimal_by_size_and_time[{pc(s),tm[s]}];
   if(pc(s)==7){
    vector<int> degrees;
    for(int v=0;v<16;++v)if(s&(1<<v))degrees.push_back(pc(n[v]&s));
    sort(degrees.begin(),degrees.end());
    if(degrees==vector<int>({2,2,2,3,3,3,3}))++minimal7degree;
   }
  }
 }
 for(int s=0;s<=FULL;++s)if(pc(s)==7){
  vector<int> degrees;
  for(int v=0;v<16;++v)if(s&(1<<v))degrees.push_back(pc(n[v]&s));
  sort(degrees.begin(),degrees.end());
  if(degrees==vector<int>({2,2,2,3,3,3,3}))++all7degree;
 }
 cout<<name<<" successes by size:";
 for(auto [k,v]:successes_by_size)cout<<" "<<k<<":"<<v;
 cout<<"\n"<<name<<" minimal by (size,time):";
 for(auto [p,v]:minimal_by_size_and_time)cout<<" "<<p.first<<","<<p.second<<":"<<v;
 cout<<"\n"<<name<<" seven-set degree signature total:"<<all7degree<<" minimal:"<<minimal7degree<<"\n";
 if(sh){
  assert((minimal_by_size_and_time==map<pair<int,int>,int>{{{6,3},96},{{6,4},336},{{6,5},1152},{{6,6},576},{{7,3},64}}));
  assert(minimal7degree==64 && all7degree==64);
  assert((successes_by_size==map<int,int>{{6,2160},{7,7504},{8,11658},{9,11328},{10,8008},{11,4368},{12,1820},{13,560},{14,120},{15,16},{16,1}}));
 }else{
  assert((minimal_by_size_and_time==map<pair<int,int>,int>{{{6,3},288},{{6,5},576}}));
  assert(minimal7degree==0 && all7degree==0);
  assert((successes_by_size==map<int,int>{{6,864},{7,4272},{8,8010},{9,9312},{10,7432},{11,4272},{12,1812},{13,560},{14,120},{15,16},{16,1}}));
 }
}
int main(){analyze("Shrikhande",true);analyze("Rook",false);cout<<"PASS direct enumeration\n";}
