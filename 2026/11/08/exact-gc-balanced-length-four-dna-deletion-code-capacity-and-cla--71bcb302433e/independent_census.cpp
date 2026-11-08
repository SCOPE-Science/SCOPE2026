// Independent exact finite search for GC-balanced strand-pair deletion codes.
// Standard C++17 only; compile with: c++ -O2 -std=c++17 independent_census.cpp -o census
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
using U=uint64_t;
int comp(int d){return 3-d;}
int rc(int w){
 int a[4];for(int i=3;i>=0;--i){a[i]=w%4;w/=4;}
 int y=0;for(int i=3;i>=0;--i)y=4*y+comp(a[i]);
 return y;
}
int gc(int w){int z=0;for(int i=0;i<4;++i){int d=w%4;w/=4;z+=(d==1||d==2);}return z;}
U shadow(int w){int a[4];for(int i=3;i>=0;--i){a[i]=w%4;w/=4;}
 U ret=0;for(int skip=0;skip<4;++skip){int y=0;for(int i=0;i<4;++i)if(i!=skip)y=4*y+a[i];ret|=U(1)<<y;}
 return ret;
}
struct Search {
 array<U,64> compatible{};
 unsigned long long count=0;
 void recurse(U cand,int need){
  if(need==0){++count;return;}
  if(__builtin_popcountll(cand)<need)return;
  while(cand){
   int v=__builtin_ctzll(cand);
   cand &= cand-1;
   recurse(cand&compatible[v],need-1);
  }
 }
};
int main(){
 set<pair<int,int>> all;
 for(int w=0;w<256;++w)if(gc(w)==2){int r=rc(w);all.emplace(min(w,r),max(w,r));}
 if(all.size()!=52)throw runtime_error("orbit count");
 vector<pair<int,int>> allowed;
 for(auto [a,b]:all)if(a!=b && !(shadow(a)&shadow(b)))allowed.push_back({a,b});
 if(allowed.size()!=44)throw runtime_error("admissible count");
 vector<U> sh;
 for(auto [a,b]:allowed)sh.push_back(shadow(a)|shadow(b));
 Search s;
 unsigned conflicts=0;
 for(int i=0;i<44;++i)for(int j=i+1;j<44;++j){
  if(sh[i]&sh[j])++conflicts;
  else{s.compatible[i]|=U(1)<<j;s.compatible[j]|=U(1)<<i;}
 }
 if(conflicts!=344)throw runtime_error("conflict count");
 s.recurse((U(1)<<44)-1,7);auto seven=s.count;
 s.count=0;s.recurse((U(1)<<44)-1,8);auto eight=s.count;
 if(seven!=20||eight!=0)throw runtime_error("optimum census");
 cout<<"DIRECT_CENSUS_OK: gc_words=96 orbits=52 admissible_pairs=44 conflicts=344 seven_orbit_codes="<<seven<<" eight_orbit_codes="<<eight<<"\n";
}
