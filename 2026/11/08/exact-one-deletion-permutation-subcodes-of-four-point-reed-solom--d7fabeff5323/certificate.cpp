// Exhaustive finite certificate for the seven-symbol one-deletion permutation channel.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra -o certificate certificate.cpp
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
struct T {int x,y,z;};
int mod7(int x) {x%=7; return x<0?x+7:x;}
int pairindex(int x,int y) {if(x>y) swap(x,y); int k=0;
 for(int a=0;a<7;a++)for(int b=a+1;b<7;b++,k++)if(a==x&&b==y)return k;
 return -1;}
uint32_t pairs(T t) {return (1u<<pairindex(t.x,t.y))|(1u<<pairindex(t.x,t.z))|(1u<<pairindex(t.y,t.z));}
bool ap(T t) {return mod7(t.x+t.z-2*t.y)==0 || mod7(t.x+t.y-2*t.z)==0 || mod7(t.y+t.z-2*t.x)==0;}
vector<T> triples(bool arithmetic){vector<T> v;
 for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++) {
  T t{a,b,c};if(ap(t)==arithmetic)v.push_back(t);
 }return v;}
void verify(bool arithmetic,int expectN,int expectMax,int expectCount) {
 auto v=triples(arithmetic);assert((int)v.size()==expectN);
 vector<uint32_t> masks;for(T t:v)masks.push_back(pairs(t));
 int maxK=0,count=0,triangleOmissions=0;
 set<tuple<int,int,int>> missingTriangles;
 // Explicitly examines all 2^N subsets, with no upper-bound heuristic.
 for(uint32_t b=0;b<(1u<<v.size());b++) {
  if(__builtin_popcount(b)<maxK)continue;
  uint32_t used=0;bool valid=true;
  for(size_t j=0;j<v.size();j++)if(b&(1u<<j)) {
   if(used&masks[j]){valid=false;break;}
   used|=masks[j];
  }
  if(!valid)continue;
  int k=__builtin_popcount(b);
  if(k>maxK){maxK=k;count=0;triangleOmissions=0;missingTriangles.clear();}
  if(k==maxK){count++;
   if(arithmetic && k==6){
    uint32_t omitted=((1u<<21)-1)^used;
    assert(__builtin_popcount(omitted)==3);
    for(int a=0;a<7;a++)for(int c=a+1;c<7;c++)for(int d=c+1;d<7;d++) {
      uint32_t candidate=pairs(T{a,c,d});
      if(candidate==omitted){triangleOmissions++;missingTriangles.emplace(a,c,d);assert(!ap(T{a,c,d}));}
    }
   }
  }
 }
 assert(maxK==expectMax && count==expectCount);
 if(arithmetic)assert(triangleOmissions==14 && missingTriangles.size()==14);
 cout<<(arithmetic?"AP":"nonAP")<<" triples="<<v.size()<<" max_pack="<<maxK<<" optimizers="<<count<<"\n";
}
int main(){verify(true,21,6,14);verify(false,14,7,2);cout<<"PASS exhaustive exact certificate\n";}
