// Direct two-step integer diffusion, using independent edge-gap enumeration.
// No orientation or sign-flip logic is used to recognize a periodic state.
#include <iostream>
#include <vector>
#include <utility>
#include <cassert>
using namespace std;
using ll=long long;

ll formula(int a, int b) {
  auto power=[](ll x,int n){ll y=1; for(int i=0;i<n;++i)y*=x;return y;};
  ll main=(a+b+1)*power(a+1,a)*power(b+1,b);
  ll c1=max(0,a-b+1)*power(a+1,a)*power(b-1,b);
  ll c2=max(0,b-a+1)*power(a-1,a)*power(b+1,b);
  return 1+2*(main+c1+c2)+(a==b?2*power(a,a+b):0);
}

ll check(int a,int b){
  const int n=a+b+2;
  vector<pair<int,int>> edges={{0,1}};
  for(int i=0;i<a;i++)edges.push_back({0,2+i});
  for(int j=0;j<b;j++)edges.push_back({1,2+a+j});
  vector<int> lim;
  // Extended, symmetric margins beyond the largest possible periodic edge gaps.
  lim.push_back(a+b+2);
  for(int i=0;i<a;i++)lim.push_back(a+2);
  for(int j=0;j<b;j++)lim.push_back(b+2);
  vector<int> gaps(lim.size());
  long long tested=0, periodic=0;
  auto run=[&](){
    vector<int> x(n,0);
    x[1]=gaps[0];
    for(int i=0;i<a;i++)x[2+i]=gaps[1+i];
    for(int j=0;j<b;j++)x[2+a+j]=x[1]+gaps[1+a+j];
    auto step=[&](const vector<int>& w){
      vector<int> z=w;
      for(auto [u,v]:edges){
        if(w[u]>w[v]){--z[u];++z[v];}
        if(w[u]<w[v]){++z[u];--z[v];}
      }
      return z;
    };
    auto y=step(x);
    auto z=step(y);
    periodic += (z==x);
    ++tested;
  };
  auto rec=[&](auto&& self,int i)->void{
    if(i==(int)lim.size()){run();return;}
    for(int d=-lim[i];d<=lim[i];++d){gaps[i]=d;self(self,i+1);}
  };
  rec(rec,0);
  cout<<"a="<<a<<" b="<<b<<" direct_states="<<tested<<" fixed_by_F2="<<periodic<<" expected="<<formula(a,b)<<"\n";
  assert(periodic==formula(a,b));
  return tested;
}
int main(){
  long long total=0;
  for(auto [a,b]:vector<pair<int,int>>{{1,1},{1,2},{1,3},{2,2},{2,3},{3,3}}) total+=check(a,b);
  cout<<"PASS: direct two-step dynamics on "<<total<<" labelled normalized configurations\n";
}
