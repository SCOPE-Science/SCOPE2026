// Exact finite verification for identifying codes of Lucas cubes.
// Requires a C++17 compiler: g++ -O3 -std=c++17 verify_lucas.cpp -o verify && ./verify
#include <algorithm>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <unordered_set>
#include <vector>
using namespace std;

struct Instance {
 int n,m;
 vector<int> vertices;
 vector<uint32_t> constraints;
 vector<vector<int>> automorphisms;
};
Instance make_instance(int n){
 Instance a;a.n=n;
 for(int x=0;x<(1<<n);++x){
  bool ok=true;
  for(int i=0;i<n;i++)if((x&(1<<i))&&(x&(1<<((i+1)%n))))ok=false;
  if(ok)a.vertices.push_back(x);
 }
 a.m=(int)a.vertices.size();assert(a.m<32);
 vector<uint32_t> balls(a.m,0);
 for(int i=0;i<a.m;i++)for(int j=0;j<a.m;j++)
  if(__builtin_popcount((unsigned)(a.vertices[i]^a.vertices[j]))<=1)
   balls[i]|=uint32_t(1)<<j;
 for(int i=0;i<a.m;i++)a.constraints.push_back(balls[i]);
 for(int i=0;i<a.m;i++)for(int j=0;j<i;j++)a.constraints.push_back(balls[i]^balls[j]);
 for(auto x:a.constraints)assert(x!=0);
 sort(a.constraints.begin(),a.constraints.end());
 a.constraints.erase(unique(a.constraints.begin(),a.constraints.end()),a.constraints.end());
 stable_sort(a.constraints.begin(),a.constraints.end(),[](uint32_t x,uint32_t y){
  return __builtin_popcount(x)<__builtin_popcount(y);
 });
 for(int shift=0;shift<n;shift++)for(int reversed=0;reversed<2;reversed++){
  vector<int> perm(a.m);
  for(int i=0;i<a.m;i++){
   int y=0;
   for(int j=0;j<n;j++)if((a.vertices[i]>>((shift+(reversed?n-j:j))%n))&1)y|=1<<j;
   auto it=find(a.vertices.begin(),a.vertices.end(),y);
   assert(it!=a.vertices.end());perm[i]=it-a.vertices.begin();
  }a.automorphisms.push_back(perm);
 }
 return a;
}
// Exhaustive fixed-size combination traversal, ordered by bitmask integer.
vector<uint32_t> find_codes(const Instance& a,int k){
 vector<uint32_t> answers;
 const uint32_t limit=uint32_t(1)<<a.m;
 for(uint32_t x=(uint32_t(1)<<k)-1;x<limit;){
  bool works=true;
  for(uint32_t needed:a.constraints)if((x&needed)==0){works=false;break;}
  if(works)answers.push_back(x);
  uint32_t low=x&-x,up=x+low;
  if(up==0||up>=limit)break;
  x=(((up^x)>>2)/low)|up;
 }
 return answers;
}
uint32_t transform(uint32_t x,const vector<int>& p){
 uint32_t y=0;
 for(size_t i=0;i<p.size();i++)if((x>>i)&1)y|=uint32_t(1)<<p[i];
 return y;
}
map<int,int> orbit_histogram(const Instance& a,const vector<uint32_t>& codes){
 set<uint32_t> available(codes.begin(),codes.end());map<int,int> histogram;
 while(!available.empty()){
  uint32_t x=*available.begin();set<uint32_t> orbit;
  for(const auto& p:a.automorphisms)orbit.insert(transform(x,p));
  histogram[(int)orbit.size()]++;
  for(uint32_t y:orbit){assert(available.erase(y)==1);}
 }
 return histogram;
}
pair<int,int> invariant_minimum(const Instance& a){
 vector<uint32_t> orbit_masks;set<int> unassigned;
 for(int i=0;i<a.m;i++)unassigned.insert(i);
 while(!unassigned.empty()){
  int seed=*unassigned.begin();uint32_t bits=0;
  for(const auto& p:a.automorphisms)bits|=uint32_t(1)<<p[seed];
  orbit_masks.push_back(bits);
  for(int i=0;i<a.m;i++)if((bits>>i)&1)unassigned.erase(i);
 }
 int best=1000,count=0;
 for(int q=0;q<(1<<(int)orbit_masks.size());q++){
  uint32_t x=0;
  for(size_t j=0;j<orbit_masks.size();j++)if((q>>j)&1)x|=orbit_masks[j];
  bool valid=true;
  for(uint32_t z:a.constraints)if(!(x&z)){valid=false;break;}
  if(!valid)continue;
  int size=__builtin_popcount(x);
  if(size<best){best=size;count=1;}else if(size==best)count++;
 }
 return {best,count};
}
int main(){
 const int mincode[]={0,0,2,3,4,5,7,11};
 const int ncode[]={0,0,1,4,13,21,18,259};
 const int invmin[]={0,0,2,3,4,5,8,14};
 const int invcount[]={0,0,1,1,1,1,1,3};
 const map<int,int> hist[]={ {},{},{ {1,1} },{{1,1},{3,1}},{{1,1},{4,1},{8,1}},{{1,1},{5,2},{10,1}},{{6,1},{12,1}},{{7,9},{14,14}} };
 const int vertexcounts[]={0,0,3,4,7,11,18,29};
 for(int n=2;n<=7;n++){
  auto instance=make_instance(n);
  assert(instance.m==vertexcounts[n]);
  assert(find_codes(instance,mincode[n]-1).empty());
  auto codes=find_codes(instance,mincode[n]);
  assert((int)codes.size()==ncode[n]);
  assert(orbit_histogram(instance,codes)==hist[n]);
  assert(invariant_minimum(instance)==make_pair(invmin[n],invcount[n]));
  cout<<"n="<<n<<" vertices="<<instance.m<<" min="<<mincode[n]<<" optimum_count="<<codes.size()<<" invariant_min="<<invmin[n]<<" invariant_count="<<invcount[n]<<'\n';
 }
 cout<<"VERIFY_OK\n";
}
