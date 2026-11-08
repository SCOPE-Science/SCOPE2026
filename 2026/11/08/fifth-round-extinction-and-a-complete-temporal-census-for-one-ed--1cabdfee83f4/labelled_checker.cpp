// Independent vertex-by-vertex enumerator for three-state Greenberg--Hastings
// dynamics on K_{m,n} with the edge (left 0, right 0) removed.
// Build: c++ -O2 -std=c++17 labelled_checker.cpp -o labelled_checker
// Run: ./labelled_checker
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <utility>
#include <vector>
using namespace std;
using ll = long long;
using Key = pair<int,int>;
using Mat = array<array<int,3>,3>;
static const map<Key,Mat> expected = {
 {{0,1}, {{{1,0,0},{0,0,0},{0,0,0}}}},
 {{0,3}, {{{0,0,0},{0,3,6},{0,6,9}}}},
 {{0,4}, {{{0,4,0},{4,8,0},{0,0,0}}}},
 {{1,1}, {{{15,8,0},{8,4,0},{0,0,0}}}},
 {{1,3}, {{{0,0,0},{0,0,1},{0,1,0}}}},
 {{1,4}, {{{0,8,3},{8,20,6},{3,6,0}}}},
 {{2,1}, {{{25,15,3},{15,4,0},{3,0,0}}}},
 {{2,3}, {{{0,0,0},{0,0,1},{0,1,0}}}},
 {{2,4}, {{{0,13,6},{13,22,6},{6,6,0}}}},
 {{3,1}, {{{18,12,3},{12,4,0},{3,0,0}}}},
 {{3,3}, {{{0,0,0},{0,0,1},{0,1,0}}}},
 {{3,4}, {{{0,7,7},{7,12,6},{7,6,0}}}},
 {{4,1}, {{{12,8,3},{8,0,0},{3,0,0}}}},
 {{4,4}, {{{0,4,2},{4,4,0},{2,0,0}}}},
 {{5,1}, {{{10,2,0},{2,0,0},{0,0,0}}}}
};
ll pw(ll b,int e){ll x=1;while(e--) x*=b;return x;}
ll surj(int j,int n){
  if(j==1)return 1;
  if(j==2)return pw(2,n)-2;
  if(j==3)return pw(3,n)-3*pw(2,n)+3;
  assert(false);return 0;
}
uint32_t evolve(uint32_t state,int m,int n){
  int v=m+n;
  array<int,12> x{};
  uint32_t y=state;
  for(int i=0;i<v;++i){x[i]=y%3;y/=3;}
  int left_exc=0,right_exc=0;
  for(int i=0;i<m;++i) left_exc+=(x[i]==1);
  for(int j=m;j<v;++j)right_exc+=(x[j]==1);
  uint32_t out=0,scale=1;
  for(int i=0;i<v;++i){
    int neighbours_exc=(i<m) ? (right_exc-(i==0 && x[m]==1))
                                  : (left_exc-(i==m && x[0]==1));
    int z=(x[i] ? (x[i]+1)%3 : (neighbours_exc>0 ? 1:0));
    out+=scale*z;scale*=3;
  }
  return out;
}
Key classify(uint32_t start,int m,int n){
  array<uint32_t,32> seen{};int t=0;uint32_t z=start;
  while(true){
    for(int i=0;i<t;++i)if(seen[i]==z)return {i,t-i};
    assert(t<32);
    seen[t++]=z;
    z=evolve(z,m,n);
  }
}
int main(){
 ll all=0;
 for(int m=2;m<=6;++m)for(int n=2;n<=6;++n){
   map<Key,ll> got;
   ll states=pw(3,m+n);
   for(uint32_t x=0;x<(uint32_t)states;++x){
      Key k=classify(x,m,n);
      ++got[k];
      assert(expected.count(k));
   }
   for(const auto &a:expected){
     ll pred=0;const Mat &C=a.second;
     for(int i=1;i<=3;++i)for(int j=1;j<=3;++j)
       pred+=(ll)C[i-1][j-1]*surj(i,m-1)*surj(j,n-1);
     if(got[a.first]!=pred){
       cerr<<"FAIL m="<<m<<" n="<<n<<" t,p="<<a.first.first<<","<<a.first.second
           <<" observed="<<got[a.first]<<" predicted="<<pred<<"\n";
       return 1;
     }
   }
   assert((got[{5,1}]==pw(2,m)+pw(2,n)+2));
   all+=states;
   if((m==2&&n==2)||(m==3&&n==3)||(m==6&&n==6))
      cout<<"m="<<m<<" n="<<n<<" states="<<states
          <<" first-entry-5-to-fixed="<<got[{5,1}]<<"\n";
 }
 cout<<"PASS: independent labelled evolution of "<<all
     <<" configurations across 25 graphs, exact agreement on all 15 classes\n";
}
