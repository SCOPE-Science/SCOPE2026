// Exact inclusion-exclusion verification for unbordered forbidden binary factors.
// Compile: c++ -std=c++17 -O2 check_inclusion.cpp -o check_inclusion && ./check_inclusion
#include <bits/stdc++.h>
using namespace std;
struct Pack {int used; int fixed; int blocks;};
vector<Pack> packs;
void make_packs(int start,int n,const string &w,int used,int fixed,int blocks) {
  packs.push_back({used,fixed,blocks});
  int k=(int)w.size();
  for(int a=start;a+k<=n;++a){
    int u=used,f=fixed;
    for(int t=0;t<k;++t){
      u|=1<<(a+t); if(w[t]=='1')f|=1<<(a+t);
    }
    make_packs(a+k,n,w,u,f,blocks+1);
  }
}
long long ie_coefficient(int s,int n) {
  long long z=0;
  for(const Pack &p:packs) {
    if ((s & ~p.used)!=0)continue;
    int sign=(p.blocks + __builtin_popcount((unsigned)(s & p.fixed)))&1;
    z += (sign ? -1LL:1LL)*(1LL<<(n-__builtin_popcount((unsigned)p.used)));
  }
  return z;
}
long long direct_coefficient(int s,int n,const string &w){
  long long z=0;
  for(int x=0;x<(1<<n);++x){
    bool contains=false;int k=(int)w.size();
    for(int a=0;a+k<=n && !contains;++a){
      bool match=true;
      for(int j=0;j<k;++j)if(((x>>(a+j))&1)!=(w[j]-'0')){match=false;break;}
      if(match)contains=true;
    }
    if(!contains) z += (__builtin_parity((unsigned)(x&s)) ? -1:1);
  }
  return z;
}
int main(){
  vector<string> patterns={"01","001","0011","0001","00101","00011"};
  long long comparisons=0;
  for(const auto &w:patterns) {
    int k=w.size();
    for(int d=1;d<k;++d)if(w.substr(0,d)==w.substr(k-d,d))return 4;
    for(int n=1;n<=10;++n){
      packs.clear();make_packs(0,n,w,0,0,0);
      for(int s=0;s<(1<<n);++s){
        long long a=ie_coefficient(s,n),b=direct_coefficient(s,n,w);
        if(a!=b){cerr<<"MISMATCH "<<w<<" "<<n<<" "<<s<<" "<<a<<" "<<b<<"\n";return 1;}
        int r=n%k;
        if(a%(1LL<<r)){cerr<<"DIVISIBILITY FAIL\n";return 2;}
        if(r==0 && !(a&1)){cerr<<"ODDNESS FAIL\n";return 3;}
        ++comparisons;
      }
      int q=n/k,r=n%k, s=(1<<(q*k))-1;
      long long value=ie_coefficient(s,n);
      long long expected=1LL<<r;
      if((q + q*(int)count(w.begin(),w.end(),'1'))%2)expected=-expected;
      if(value!=expected){cerr<<"WITNESS FAIL "<<w<<" "<<n<<" "<<value<<" "<<expected<<"\n";return 5;}
    }
  }
  cout<<"INCLUSION_OK: "<<comparisons<<" direct character sums equal inclusion-exclusion, sharp witnesses verified\n";
}
