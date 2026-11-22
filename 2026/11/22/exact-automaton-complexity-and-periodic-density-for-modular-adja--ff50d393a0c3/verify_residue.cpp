// Exhaustive modular-incidence construction independent of breadth-first reachability.
// Compile: c++ -O2 -std=c++17 verify_residue.cpp -o verify_residue
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
struct Vertex {int endpoint, code;};
int main(){
 for(auto param: vector<pair<int,int>>{{2,2},{2,3},{2,4},{3,2}}){
  int q=param.first,m=param.second,dim=q*q,all=1;
  for(int i=0;i<dim;i++)all*=m;
  vector<int> pw(dim,1);for(int i=1;i<dim;i++)pw[i]=pw[i-1]*m;
  vector<Vertex> vertices; map<pair<int,int>,int> lookup;
  // Reserve id 0 for start, id 1 for rejecting sink.
  vertices.push_back({-1,-1});vertices.push_back({-2,-2});
  for(int t=0;t<q;t++)for(int code=0;code<all;code++){
   vector<int> bal(q,0);
   for(int a=0;a<q;a++)for(int b=0;b<q;b++){
    int v=(code/pw[a*q+b])%m;
    bal[a]+=v;bal[b]-=v;
   }
   bool yes=true;
   for(int a=0;a<q;a++){
    int want=(a==0)-(a==t);
    if(((bal[a]-want)%m+m)%m)yes=false;
   }
   if(yes){int id=vertices.size();vertices.push_back({t,code});lookup[{t,code}]=id;}
  }
  int N=vertices.size(),d=q*q-q+1;
  int power=1;for(int i=0;i<d;i++)power*=m;
  int expected=2+q*power;
  assert(N==expected);
  vector<vector<int>> delta(N,vector<int>(q,1));
  for(int a=0;a<q;a++)delta[0][a]=(a==0?lookup.at({0,0}):1);
  for(int i=2;i<N;i++)for(int a=0;a<q;a++){
    auto st=vertices[i];int v=(st.code/pw[st.endpoint*q+a])%m;
    int code=st.code+(v+1==m?-(m-1):1)*pw[st.endpoint*q+a];
    delta[i][a]=lookup.at({a,code});
  }
  vector<int> cls(N,0);cls[lookup.at({0,0})]=1;
  int rounds=0;
  while(true){
    map<vector<int>,int> signature;
    vector<int> next(N);
    for(int i=0;i<N;i++){
     vector<int> key={cls[i]};
     for(int a=0;a<q;a++)key.push_back(cls[delta[i][a]]);
     auto it=signature.emplace(key,(int)signature.size());
     next[i]=it.first->second;
    }
    rounds++;
    if(next==cls)break;
    if(rounds>10000) return 2;
    cls.swap(next);
  }
  int classes=*max_element(cls.begin(),cls.end())+1;
  assert(classes==N);
  cout<<"q="<<q<<" m="<<m<<" exponent="<<d<<" incidence_states="<<N<<" minimal="<<classes<<" rounds="<<rounds<<" PASS\n";
 }
}
