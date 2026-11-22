#include <cstdint>
#include <cstdio>
#include <vector>
#include <set>
#include <array>
#include <cassert>
#include <algorithm>
#include <string>
using namespace std;

// Independent finite verification of one-leak zero forcing on open ladders.
// Vertex indices: top row 0,...,n-1 and bottom row n,...,2n-1.
struct Grid {
 int n, N;
 vector<uint64_t> adj;
 explicit Grid(int n_) : n(n_), N(2*n_), adj(N,0) {
  assert(N<=62);
  for(int r=0;r<2;r++) for(int c=0;c<n;c++) {
   int v=r*n+c;
   adj[v] |= 1ULL<<((1-r)*n+c);
   if(c) adj[v] |= 1ULL<<(r*n+c-1);
   if(c+1<n) adj[v] |= 1ULL<<(r*n+c+1);
  }
 }
 bool force(uint64_t initial, int leak) const {
  uint64_t all=(1ULL<<N)-1;
  uint64_t blue=initial;
  while(blue!=all) {
   uint64_t next=0;
   for(int v=0;v<N;v++) if(v!=leak && (blue>>v&1)) {
    uint64_t w=adj[v]&~blue;
    if(w && !(w&(w-1))) next|=w;
   }
   if(!next) return false;
   blue|=next;
  }
  return true;
 }
 bool one_leaky(uint64_t x) const {
  for(int v=0;v<N;v++) if(!force(x,v)) return false;
  return true;
 }
 uint64_t expected(int a,int b) const {
  int x=n-1;
  auto L=array<array<int,2>,3>{{{{0,1}},{{n,n+1}},{{0,n}}}};
  auto R=array<array<int,2>,3>{{{{x-1,x}},{{n+x-1,n+x}},{{x,n+x}}}};
  uint64_t s=0;
  for(int v:L[a])s|=1ULL<<v;
  for(int v:R[b])s|=1ULL<<v;
  return s;
 }
};
int main(){
 for(int n=2;n<=16;n++) {
  Grid g(n);
  int N=2*n;
  set<uint64_t> opt;
  int size=-1;
  for(int k=1;k<=4;k++) {
   // Exhaustively enumerate every k-subset by Gosper iteration.
   uint64_t c=(1ULL<<k)-1, end=1ULL<<N;
   do {
    if(g.one_leaky(c)) opt.insert(c);
    uint64_t z=c&-c, r=c+z;
    if(!r)break;
    c=(((r^c)>>2)/z)|r;
   } while(c<end);
   if(!opt.empty()){size=k;break;}
  }
  size_t want=n==2?4:n==3?6:n==4?16:9;
  int k_want=n==2?2:n==3?3:4;
  if(size!=k_want || opt.size()!=want){printf("FAIL n=%d min=%d count=%zu\n",n,size,opt.size());return 1;}
  if(n>=5){
   set<uint64_t> exact;
   for(int a=0;a<3;a++)for(int b=0;b<3;b++)exact.insert(g.expected(a,b));
   if(exact!=opt){printf("CLASSIFICATION_FAIL n=%d\n",n);return 2;}
   int jumps=0,slides=0;
   for(auto it=opt.begin();it!=opt.end();it++)for(auto jt=next(it);jt!=opt.end();jt++) {
    uint64_t ab=(*it)^(*jt);
    if(__builtin_popcountll(ab)==2){
     jumps++;
     uint64_t gone=(*it)&~(*jt),added=(*jt)&~(*it);
     int v=__builtin_ctzll(gone);
     if(g.adj[v]&added)slides++;
    }
   }
   // P_3 square P_3 has 12 edges; no minimum-preserving token slide.
   if(jumps!=12 || slides!=0){printf("RECONFIG_FAIL n=%d jumps=%d slides=%d\n",n,jumps,slides);return 3;}
  }
  printf("n=%d minimum=%d count=%zu exact=%s\n",n,size,opt.size(),n>=5?"YES":"small-case");
 }
 puts("VERIFY_OK");
}
