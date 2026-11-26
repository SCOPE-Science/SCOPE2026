// Independent labelled-neighborhood Greenberg-Hastings check for K_{a,b,c}.
// Standard C++17; no external packages.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <tuple>
#include <vector>
using namespace std;
using ll=long long;
using Key=pair<int,int>;
ll pw(int base,int n){ll x=1;while(n--)x*=base;return x;}
map<Key,ll> expected(int a,int b,int c){
 array<int,3> n={a,b,c};ll X=0,Y=0,P=0,R=0,Q=0;
 ll U=pw(2,a+b+c),V=pw(3,a+b+c);
 for(int i=0;i<3;i++){
   X+=pw(2,n[i]);Y+=pw(3,n[i]);
   Q+=pw(3,n[i])*pw(2,a+b+c-n[i]);
   for(int j=0;j<3;j++)if(j!=i) R+=pw(3,n[i])*pw(2,n[j]);
   for(int j=i+1;j<3;j++)P+=pw(2,n[i]+n[j]);
 }
 return {
  {{0,1},1},{{0,3},V-3*Q+15*U-3*P+3*Y-6*X+12},
  {{1,1},U-1},{{1,3},Q-R-6*U+5*P+2*Y-6*X+6},
  {{2,1},U+Y-2*X+2},{{2,3},Q-6*U+P-2*Y+4*X-6},
  {{3,1},U+Y-3*X+7},{{3,3},Q-6*U+P-2*Y+4*X-6},
  {{4,1},Y-X-3},{{4,3},R-4*P-4*Y+10*X-12}
 };
}
vector<unsigned char> transition(const vector<unsigned char>& s,const vector<int>& side){
 int N=s.size();vector<unsigned char> t(N);
 for(int i=0;i<N;i++){
  if(s[i]) t[i]=(s[i]+1)%3;
  else {
    bool excited=false;
    for(int j=0;j<N;j++)if(side[i]!=side[j] && s[j]==1){excited=true;break;}
    t[i]=excited?1:0;
  }
 }
 return t;
}
Key classify(vector<unsigned char> s,const vector<int>&side){
 map<vector<unsigned char>,int>seen;
 int round=0;
 while(!seen.count(s)){
  if(round>100)throw runtime_error("Unexpected long orbit");
  seen[s]=round++;
  s=transition(s,side);
 }
 return {seen[s],round-seen[s]};
}
int main(){
 ll tested=0;int tested_graphs=0;
 for(auto sizes: vector<array<int,3>>{{1,1,1},{1,1,2},{1,2,2},{1,3,3},{2,2,2},{2,2,3},{2,3,3},{3,3,3},{3,3,4},{4,4,3}}){
  int a=sizes[0],b=sizes[1],c=sizes[2],N=a+b+c;
  vector<int>side(N);
  for(int i=0;i<N;i++)side[i]=(i<a?0:(i<a+b?1:2));
  map<Key,ll>actual;
  for(ll code=0,lim=pw(3,N);code<lim;code++){
   ll t=code;vector<unsigned char>s(N);
   for(int i=0;i<N;i++){s[i]=t%3;t/=3;}
   actual[classify(s,side)]++;
   tested++;
  }
  auto want=expected(a,b,c);
  for(auto [key,v]:want)if(actual[key]!=v){
   cerr<<"Mismatch "<<a<<","<<b<<","<<c<<" class("<<key.first<<","<<key.second<<") actual "<<actual[key]<<" expected "<<v<<"\n";return 1;
  }
  for(auto [key,v]:actual)if(want[key]!=v){cerr<<"Unexpected class\n";return 1;}
  cout<<"PASS K_("<<a<<","<<b<<","<<c<<") "<<pw(3,N)<<" labelled initial states\n";
  tested_graphs++;
 }
 cout<<"PASS total "<<tested<<" labelled states over "<<tested_graphs<<" graphs\n";
 return 0;
}
