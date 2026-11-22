#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using ll=long long;
using Mask=uint64_t;
vector<Mask> fronts(int v,int rem){
 if(rem==0) return {Mask(1)<<v};
 auto L=fronts(2*v,rem-1),R=fronts(2*v+1,rem-1);
 vector<Mask> a{Mask(1)<<v};
 for(auto x:L) for(auto y:R) a.push_back(x|y);
 return a;
}
bool anc(int a,int b){while(b>a)b/=2; return b==a;}
bool rule(Mask S,int h,int p){
 vector<int> s;
 for(int v=1;v<(1<<(h+1));v++)if(S>>v&1)s.push_back(v);
 for(int i=0;i<(int)s.size();i++)for(int j=0;j<i;j++)if(anc(s[i],s[j])||anc(s[j],s[i]))return false;
 for(int v=1<<h;v<(1<<(h+1));v+=2)if((S>>v&3)==3)return false;
 for(int w=1<<(h-1);w<(1<<h);w++){
  bool touched=false;
  for(int x:s) if(anc(x,w)||anc(w,x)) {touched=true;break;}
  if(!touched)return true;
 }
 if(s.empty()) return true;
 for(int x:s)if(x>=(1<<(h-1)))return false;
 return ((int)s.size()%2)==p;
}
vector<Mask> ants(int v,int rem){
 if(rem==0)return {0,Mask(1)<<v};
 auto L=ants(2*v,rem-1),R=ants(2*v+1,rem-1);
 vector<Mask> a{Mask(1)<<v};
 for(auto x:L)for(auto y:R)a.push_back(x|y);
 return a;
}
bool shat(Mask s,const vector<Mask>& fam){
 vector<int> q;for(int v=1;v<63;v++)if(s>>v&1)q.push_back(v);
 if(q.size()>=32)return false;
 vector<uint32_t> seen((1u<<q.size()),0);
 unsigned n=0;
 for(auto c:fam){unsigned t=0;for(int j=0;j<(int)q.size();j++)if(c>>q[j]&1)t|=1u<<j;
 if(!seen[t]){seen[t]=1;n++;} }
 return n==(1u<<q.size());
}
vector<ll> sq(vector<ll> a){vector<ll> c(2*a.size()-1);for(size_t i=0;i<a.size();i++)for(size_t j=0;j<a.size();j++)c[i+j]+=a[i]*a[j];return c;}
vector<ll> plusz(vector<ll> a){if(a.size()<2)a.resize(2);a[1]++;return a;}
int main(){
 for(int h=2;h<=3;h++){
  auto F=fronts(1,h);auto S=ants(1,h);
  for(int p=0;p<2;p++){
   vector<Mask> fam;for(auto f:F)if((__builtin_popcountll(f)&1)==p)fam.push_back(f);
   int checked=0;map<int,int> counts;
   for(auto s:S){bool got=shat(s,fam),want=rule(s,h,p);if(got!=want){cerr<<"FAIL h="<<h<<" p="<<p<<" s="<<s<<"\n";return 1;}if(got)counts[__builtin_popcountll(s)]++;checked++;}
   cout<<"height="<<h<<" parity="<<p<<" antichains="<<checked<<" family="<<fam.size()<<" polynomial:";
   for(auto [k,v]:counts)cout<<" "<<k<<":"<<v;cout<<"\n";
  }
 }
 vector<ll> A{1,3},C{0,3},K{0,1};
 for(int h=2;h<=5;h++){
  A=plusz(sq(A));C=plusz(sq(C));
  if(h>=3)K=plusz(sq(K));
  for(int p=0;p<2;p++){
   vector<ll> coef(max(A.size(),C.size()));
   for(size_t i=0;i<coef.size();i++)coef[i]=(i<A.size()?A[i]:0)-(i<C.size()?C[i]:0)+(i<K.size()&&(i%2)==p?K[i]:0);
   int top=0;for(size_t i=0;i<coef.size();i++)if(coef[i])top=(int)i;
   if(top!=(1<<(h-1))-1){cerr<<"degree fail";return 2;}
   if(h>=3&&coef[top] != (1<<(h-1))*[] (int m){ll x=1;for(int i=1;i<m;i++)x*=3;return x;}(1<<(h-1))){cerr<<"top fail";return 3;}
   cout<<"recurrence h="<<h<<" parity="<<p<<" dimension="<<top<<" top_count="<<coef[top]<<"\n";
  }
 }
 cout<<"CPP_PASS\n";
}
