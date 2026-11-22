// Exhaustive, independent edge-subset test of wheel shattering coefficients.
// Uses only the C++17 standard library; g++ -std=c++17 -O2.
#include <iostream>
#include <vector>
#include <numeric>
#include <stdexcept>
using namespace std;
struct UF {
  vector<int> p;
  explicit UF(int n):p(n){iota(p.begin(),p.end(),0);}
  int root(int a){return p[a]==a?a:p[a]=root(p[a]);}
  bool join(int a,int b){a=root(a);b=root(b);if(a==b)return false;p[a]=b;return true;}
};
struct Check {bool forest,connected;};
Check check(int n,unsigned long long mask){
  UF u(n+1);bool forest=true;
  for(int i=0;i<n;i++){
    if(mask&(1ULL<<i))if(!u.join(i,(i+1)%n))forest=false;
    if(mask&(1ULL<<(n+i)))if(!u.join(i,n))forest=false;
  }
  bool conn=true;for(int i=0;i<n;i++)if(u.root(i)!=u.root(n))conn=false;
  return {forest,conn};
}
int main(){
  const vector<vector<long long>> expected={
    {1,6,15,12},{1,8,28,48,28},{1,10,45,110,140,60},
    {1,12,66,208,387,384,124},
    {1,14,91,350,847,1260,1008,252},
    {1,16,120,544,1612,3152,3872,2560,508},
    {1,18,153,798,2790,6714,10959,11376,6336,1020}
  };
  for(int n=3;n<=9;n++){
    vector<long long> counts(n+1);
    unsigned long long full=(1ULL<<(2*n))-1;
    for(unsigned long long mask=0;mask<=full;mask++){
      int k=__builtin_popcountll(mask);if(k>n)continue;
      if(check(n,mask).forest && check(n,full^mask).connected)counts[k]++;
    }
    // Check full coefficients independently through n=9.
    if(counts!=expected[n-3])throw runtime_error("Mismatch at n="+to_string(n));
    cout<<"n="<<n<<" :";for(auto a:counts)cout<<" "<<a;cout<<"\n";
  }
  cout<<"WHEEL_CPP_CHECKS_PASS\n";
}
