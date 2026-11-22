// Reproducible finite verification of a theorem on insertion-type disagreement polynomials.
// Compile: c++ -std=c++17 -O2 checker.cpp -o checker && ./checker
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
static void require(bool v, const char *msg) { if (!v) throw runtime_error(msg); }

// Method I: Hamming distance of two increasing chains of subset masks.
static vector<int> mask_profile(const vector<int>& p) {
  const int n=(int)p.size(); require(n<=30,"mask dimension");
  vector<uint32_t> a(n+1,0); for(int i=0;i<n;++i) a[i+1]=a[i]|(uint32_t(1)<<p[i]);
  vector<int> h(n+1,0);
  for(int i=0;i<=n;++i) for(int j=0;j<=n;++j)
    ++h[__builtin_popcount(a[i]^((uint32_t(1)<<j)-1))];
  return h;
}
// Method II: independently compute every northwest rectangle's point count.
static vector<int> rectangle_profile(const vector<int>& p) {
  const int n=(int)p.size(); vector<int> inverse(n);
  for(int i=0;i<n;++i) inverse[p[i]]=i;
  vector<int> h(n+1,0);
  for(int i=0;i<=n;++i){
    int r=0;
    for(int j=0;j<=n;++j){
      if(j>0 && inverse[j-1]<i) ++r;
      int k=i+j-2*r; require(0<=k && k<=n,"distance range"); ++h[k];
    }
  }
  return h;
}
static bool unimodal(const vector<int>& h) {
  bool descending=false;
  for(int k=1;k<(int)h.size();++k){
    if(h[k]<h[k-1]) descending=true;
    if(h[k]>h[k-1] && descending) return false;
  }
  return true;
}
static vector<int> reversed_positions(vector<int> p){ reverse(p.begin(),p.end());return p; }
static vector<int> reversed_values(vector<int> p){int n=p.size();for(int &x:p)x=n-1-x;return p;}
static vector<int> inverted(const vector<int>&p){vector<int> q(p.size());for(int i=0;i<(int)p.size();++i)q[p[i]]=i;return q;}
static set<vector<int>> orbit(vector<int> seed){
  set<vector<int>> known={seed};vector<vector<int>> queue={seed};
  for(size_t i=0;i<queue.size();++i){
    vector<vector<int>> nxt={reversed_positions(queue[i]),reversed_values(queue[i]),inverted(queue[i])};
    for(auto q:nxt)if(known.insert(q).second)queue.push_back(q);
  }
  return known;
}
int main(){try{
  const vector<vector<int>> reps={
    {1,3,0,9,2,8,7,6,5,4},
    {1,4,5,6,7,8,0,9,2,3},
    {2,1,4,0,9,8,7,6,5,3},
    {2,3,0,1,9,8,7,6,5,4},
    {2,4,5,6,7,8,0,9,1,3}
  };
  const int orbit_sizes[5]={8,8,8,4,4};
  set<vector<int>> predicted;
  for(int k=0;k<5;++k){
    auto o=orbit(reps[k]);require((int)o.size()==orbit_sizes[k],"wrong orbit size");
    for(const auto &q:o) require(predicted.insert(q).second,"overlapping orbits");
  }
  require(predicted.size()==32,"orbit union not 32");
  uint64_t total=0;set<vector<int>> observed;
  for(int n=1;n<=10;++n){
    vector<int> p(n);for(int i=0;i<n;++i)p[i]=i;
    uint64_t checked=0,bad=0;
    do{
      auto a=mask_profile(p),b=rectangle_profile(p);
      require(a==b,"independent algorithms disagree");
      int sum=0;for(int x:a)sum+=x;
      require(sum==(n+1)*(n+1),"wrong type-count total");
      if(!unimodal(a)){
        ++bad;
        require(n==10,"nonunimodal spectrum below 10");
        observed.insert(p);
      }
      ++checked;
    }while(next_permutation(p.begin(),p.end()));
    uint64_t factorial=1;for(int i=2;i<=n;++i)factorial*=i;
    require(checked==factorial,"permutation enumeration incomplete");
    require(bad==(n==10?32:0),"unexpected nonunimodality census");
    total+=checked;
    cout<<"n="<<n<<" checked="<<checked<<" nonunimodal="<<bad<<"\n";
  }
  require(observed==predicted,"five listed orbits do not exhaust failures");
  cout<<"TEN_ORBITS=8,8,8,4,4\n";
  auto witness=reps[3]; auto h=mask_profile(witness);
  const vector<int> expected={3,8,16,20,19,20,15,8,6,4,2};
  require(h==expected && h[3]>h[4] && h[5]>h[4],"witness histogram incorrect");
  cout<<"WITNESS_HIST=3,8,16,20,19,20,15,8,6,4,2\n";
  // Each common new terminal maximum contributes one zero-grade pair, two at each other grade.
  for(int oldn=10;oldn<25;++oldn){
    auto old=mask_profile(witness);
    witness.push_back(oldn);
    auto now=mask_profile(witness);
    require(now[0]==old[0]+1,"terminal-maximum zero coefficient");
    for(int k=1;k<=oldn;++k)require(now[k]==old[k]+2,"terminal-maximum old grades");
    require(now[oldn+1]==2,"terminal-maximum top coefficient");
    require(now[3]>now[4] && now[5]>now[4],"persistent valley");
  }
  cout<<"TOTAL_CHECKED="<<total<<"\nVERIFY_OK\n";
}catch(const exception &e){cerr<<"VERIFY_FAILURE: "<<e.what()<<"\n";return 1;}}
