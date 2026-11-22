// Standalone finite cross-check for independent secure domination on labelled cycles.
// Compile: c++ -std=c++17 -O3 -Wall -Wextra verify_cycle.cpp -o verify_cycle
// Run: ./verify_cycle
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
using U = std::uint64_t;
static U rotation_left(U s,int n) { U full=(U(1)<<n)-1;return ((s<<1)|(s>>(n-1)))&full; }
static U rotation_right(U s,int n) { return (s>>1)|((s&1)<<(n-1)); }
static bool dominates(U s,int n) { U full=(U(1)<<n)-1;return (s|rotation_left(s,n)|rotation_right(s,n))==full; }
static bool direct(U s,int n) {
 if (s&rotation_left(s,n)) return false;
 if (!dominates(s,n)) return false;
 for(int u=0;u<n;u++) if (!(s&(U(1)<<u))) {
  bool defended=false;
  for(int v: {(u+n-1)%n,(u+1)%n}) if (s&(U(1)<<v)) {
    U t=(s&~(U(1)<<v))|(U(1)<<u);
    if(dominates(t,n)){defended=true;break;}
  }
  if(!defended)return false;
 }
 return true;
}
static bool gap_rule(U s,int n) {
 std::vector<int> vertices;
 for(int j=0;j<n;j++) if(s&(U(1)<<j))vertices.push_back(j);
 if(vertices.empty())return false;
 int k=(int)vertices.size();
 std::vector<int> lengths;
 for(int j=0;j<k;j++) {
  int d=(vertices[(j+1)%k]-vertices[j]+n)%n;
  if(d==0)d=n;
  if(d!=2&&d!=3)return false;
  lengths.push_back(d);
 }
 for(int j=0;j<k;j++) if(lengths[j]==3) {
  if(lengths[(j+1)%k]!=2 || lengths[(j+2)%k]!=2)return false;
 }
 return true;
}
static long long choose(int n,int k) {
 if(k<0||k>n)return 0;
 if(k>n-k)k=n-k;
 long long r=1;
 for(int j=1;j<=k;j++)r=r*(n-k+j)/j;
 return r;
}
static std::map<int,long long> formula(int n){
 std::map<int,long long> out;
 for(int b=0;7*b<=n;b++) {
  if((n-7*b)%2)continue;
  int a=(n-7*b)/2,k=a+3*b,tiles=a+b;
  if(tiles==0)continue;
  // n / tiles * choose(tiles,b), avoiding premature division.
  long long t=choose(tiles,b);
  if((long long)n*t%tiles) {std::cerr<<"nonintegral"<<'\n';std::exit(3);}
  out[k]+=(long long)n*t/tiles;
 }
 return out;
}
int main(){
 for(int n=4;n<=22;n++) {
  std::map<int,long long> actual;
  U all=U(1)<<n;
  for(U s=0;s<all;s++) {
    bool a=direct(s,n);
    bool b=gap_rule(s,n);
    if(a!=b){std::cerr<<"GAP_FAIL n="<<n<<" mask="<<s<<'\n';return 1;}
    if(a)actual[__builtin_popcountll(s)]++;
  }
  if(actual!=formula(n)){
    std::cerr<<"COUNT_FAIL n="<<n<<'\n';return 2;
  }
  std::cout<<"n="<<n<<" total=";
  long long total=0;for(auto p:actual) total+=p.second;
  std::cout<<total<<'\n';
 }
 std::cout<<"CYCLE_INDEPENDENT_SECURE_VERIFY_OK\n";
}
