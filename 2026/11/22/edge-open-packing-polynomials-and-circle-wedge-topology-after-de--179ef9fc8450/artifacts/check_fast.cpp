// Independent exhaustive edge-open-packing verifier for complete bipartite graphs minus a matching.
// c++ -O3 -std=c++17 check_fast.cpp -o check_fast && ./check_fast
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static uint64_t c(int n,int k){if(k<0||k>n)return 0;uint64_t x=1;for(int i=1;i<=k;++i)x=x*(n-i+1)/i;return x;}
int main(){int cases=0;
 for(int m=3;m<=5;++m)for(int n=3;n<=5;++n)for(int t=0;t<=min(m,n);++t){
  vector<pair<int,int>> e;for(int i=0;i<m;++i)for(int j=0;j<n;++j)if(!(i==j&&i<t))e.push_back({i,j});
  const int q=e.size();if(q>19)continue;
  vector<uint32_t> conflicts(q,0);
  for(int a=0;a<q;++a)for(int b=a+1;b<q;++b){
   const auto [i,j]=e[a];const auto[k,l]=e[b];
   bool shared=(i==k||j==l);
   bool common=(!shared)&&((i!=l||i>=t)||(k!=j||k>=t));
   if(common){conflicts[a]|=1U<<b;conflicts[b]|=1U<<a;}
  }
  vector<uint64_t> pc(q+1),fc(q+1),ep(q+1),ef(q+1);
  ep[0]=1;ep[1]=q;
  for(int i=0;i<m+n;++i){int d=i<m?(i<t?n-1:n):((i-m)<t?m-1:m);ef[d]++;
   for(int k=2;k<=d;++k)ep[k]+=c(d,k);
  }
  ep[2]+=c(t,2);ef[2]+=c(t,2);
  vector<uint8_t> good(1U<<q);good[0]=1;
  for(uint32_t s=1;s<(1U<<q);++s){uint32_t bit=s&-s;int i=__builtin_ctz(bit);uint32_t rest=s^bit;
   good[s]=good[rest] && !(conflicts[i]&rest);
  }
  for(uint32_t s=0;s<(1U<<q);++s){if(!good[s])continue;int k=__builtin_popcount(s);pc[k]++;
   bool maximal=true;for(int i=0;i<q;++i){if(!(s&(1U<<i)) && !(conflicts[i]&s)){maximal=false;break;}}
   if(maximal)fc[k]++;
  }
  if(pc!=ep||fc!=ef){cerr<<"FAIL m="<<m<<" n="<<n<<" t="<<t<<endl;return 1;}
  ++cases;cout<<m<<","<<n<<","<<t<<" q="<<q<<" good=";uint64_t x=0,y=0;
  for(auto v:pc)x+=v;for(auto v:fc)y+=v;cout<<x<<" max="<<y<<"\n";
 }
 cout<<"PASS "<<cases<<" independent subset-DP cases\n";
}
