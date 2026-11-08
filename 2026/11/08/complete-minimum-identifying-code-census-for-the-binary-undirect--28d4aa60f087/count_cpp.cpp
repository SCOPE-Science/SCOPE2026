// Exact independent-set-style hitting-set census for binary undirected de Bruijn identifying codes.
// Build: g++ -std=c++17 -O2 count_cpp.cpp -o count_cpp
// Run:   ./count_cpp > enumerated_masks.txt
#include <bits/stdc++.h>
using namespace std;
static const int n=5, N=1<<n;
static vector<uint32_t> constraints;
static unordered_set<uint32_t> visited, optimum;
static int target;
static uint64_t calls;

static int pop(uint32_t x){return __builtin_popcount(x);}
static uint32_t reverse_word(uint32_t x){
 uint32_t y=0;for(int i=0;i<n;++i){y=(y<<1)|(x&1);x>>=1;}return y;
}
static uint32_t act(uint32_t s,int mode){
 uint32_t t=0;
 for(int x=0;x<N;++x)if(s&(uint32_t(1)<<x)){
  uint32_t y=x;
  if(mode&1)y^=31; // global bit complement
  if(mode&2)y=reverse_word(y); // coordinate reversal
  t|=uint32_t(1)<<y;
 }
 return t;
}
static void dfs(uint32_t selected){
 int k=pop(selected);
 if(k>target || !visited.insert(selected).second)return;
 ++calls;
 uint32_t best=0;int best_size=33;
 for(uint32_t c:constraints){
  if(selected&c)continue;
  if(pop(c)<best_size){best=c;best_size=pop(c);}
 }
 if(!best){if(k<=target)optimum.insert(selected);return;}
 if(k==target)return;
 // Every pairwise-disjoint uncovered clause needs a different new vertex.
 uint32_t union_disjoint=0;int lower=0;
 for(uint32_t c:constraints){
  if((selected&c)==0 && (union_disjoint&c)==0){
   union_disjoint|=c; ++lower;
   if(k+lower>target)return;
  }
 }
 while(best){uint32_t bit=best&(-best);best^=bit;dfs(selected|bit);}
}
static vector<uint32_t> make_constraints(){
 vector<uint32_t> ball(N,0),all;
 for(int x=0;x<N;++x){
  int right=(x<<1)&31, left=x>>1;
  ball[x]=(uint32_t(1)<<x)|(uint32_t(1)<<right)|
          (uint32_t(1)<<(right|1))|(uint32_t(1)<<left)|
          (uint32_t(1)<<(left|16));
  all.push_back(ball[x]);
 }
 for(int x=0;x<N;++x)for(int y=x+1;y<N;++y){
  uint32_t diff=ball[x]^ball[y];
  if(!diff)throw runtime_error("twin neighborhoods");
  all.push_back(diff);
 }
 sort(all.begin(),all.end());all.erase(unique(all.begin(),all.end()),all.end());
 sort(all.begin(),all.end(),[](uint32_t a,uint32_t b){
  if(pop(a)!=pop(b))return pop(a)<pop(b);return a<b;
 });
 vector<uint32_t> minimal;
 for(uint32_t c:all){
  bool redundant=false;
  for(uint32_t d:minimal)if((c&d)==d){redundant=true;break;}
  if(!redundant)minimal.push_back(c);
 }
 return minimal;
}
static void run(int k){
 target=k;visited.clear();optimum.clear();calls=0;
 dfs(0);
 cerr<<"CXX_SIZE_"<<k<<"="<<optimum.size()<<" STATES="<<calls<<"\n";
 if(k==11 && !optimum.empty())throw runtime_error("unexpected 11-code");
 if(k==12){
  if(optimum.size()!=58)throw runtime_error("census mismatch");
  for(uint32_t s:optimum)if(pop(s)!=12)throw runtime_error("smaller code found");
  map<int,int> orbit_counts;unordered_set<uint32_t> done;
  int fixed_comp=0,fixed_rev=0,fixed_rc=0;
  for(auto s:optimum){
   for(int mode=0;mode<4;++mode)if(!optimum.count(act(s,mode)))
    throw runtime_error("symmetry not closed");
   fixed_comp+=(act(s,1)==s);fixed_rev+=(act(s,2)==s);fixed_rc+=(act(s,3)==s);
   if(done.count(s))continue;
   set<uint32_t> orbit;for(int mode=0;mode<4;++mode)orbit.insert(act(s,mode));
   orbit_counts[(int)orbit.size()]++;
   for(auto v:orbit)done.insert(v);
  }
  cerr<<"CXX_ORBITS_SIZE2="<<orbit_counts[2]<<" SIZE4="<<orbit_counts[4]
      <<" FIX_COMP="<<fixed_comp<<" FIX_REV="<<fixed_rev<<" FIX_REVCOMP="<<fixed_rc<<"\n";
  vector<uint32_t> ss(optimum.begin(),optimum.end());sort(ss.begin(),ss.end());
  for(auto s:ss)cout<<s<<'\n';
 }
}
int main(){
 constraints=make_constraints();
 cerr<<"CXX_MINIMAL_CLAUSES="<<constraints.size()<<'\n';
 if(constraints.size()!=161)throw runtime_error("clause count mismatch");
 run(11);run(12);
}
