// Reproducible finite certificate for ternary length-three exact-distance-two sphere concepts.
// C++17, standard library only. No external data or services.
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stdexcept>
#include <vector>
using namespace std;
using Face=vector<int>;
static int coord(int i,int c) {while(c--)i/=3;return i%3;}
static int encode(array<int,3>a) {return a[0]+3*a[1]+9*a[2];}
static int dist(int a,int b) {return (coord(a,0)!=coord(b,0))+(coord(a,1)!=coord(b,1))+(coord(a,2)!=coord(b,2));}
static bool shattered(Face s){
  uint32_t seen=0;
  for(int center=0;center<27;++center){
    int pattern=0;
    for(int j=0;j<(int)s.size();++j) if(dist(center,s[j])==2)pattern|=1<<j;
    seen|=uint32_t(1)<<pattern;
  }
  return __builtin_popcount(seen)==(1<<(int)s.size());
}
static vector<Face> getfaces(int k){
  vector<Face> v;Face s;
  auto dfs=[&](auto&&self,int start)->void{
    if((int)s.size()==k){if(shattered(s))v.push_back(s);return;}
    for(int x=start;x<=27-(k-(int)s.size());++x){s.push_back(x);self(self,x+1);s.pop_back();}
  };
  dfs(dfs,0);return v;
}
static vector<array<int,27>> generators(){
  vector<array<int,27>> gens;
  for(int c=0;c<3;++c){
    for(array<int,3>p: {array<int,3>{1,0,2},array<int,3>{1,2,0}}){
      array<int,27> g{};
      for(int x=0;x<27;++x){array<int,3>a{coord(x,0),coord(x,1),coord(x,2)};a[c]=p[a[c]];g[x]=encode(a);}
      gens.push_back(g);
    }
  }
  for(array<int,3>p: {array<int,3>{1,0,2},array<int,3>{1,2,0}}){
    array<int,27>g{};
    for(int x=0;x<27;++x){array<int,3>a{coord(x,0),coord(x,1),coord(x,2)};g[x]=encode({a[p[0]],a[p[1]],a[p[2]]});}
    gens.push_back(g);
  }
  return gens;
}
static vector<int> orbit_sizes(const vector<Face>& faces){
  set<Face> rest(faces.begin(),faces.end());auto G=generators();vector<int> sizes;
  while(!rest.empty()){
    queue<Face> q;q.push(*rest.begin());rest.erase(rest.begin());int sz=0;
    while(!q.empty()){
      Face s=q.front();q.pop();++sz;
      for(auto&g:G){Face t;for(int x:s)t.push_back(g[x]);sort(t.begin(),t.end());
        if(rest.erase(t))q.push(t);
      }
    }
    sizes.push_back(sz);
  }
  sort(sizes.begin(),sizes.end());return sizes;
}
template<size_t M>static int rank_gf2(const vector<bitset<M>>& cols){
  map<int,bitset<M>> basis;
  for(auto v: cols){
    while(v.any()){
      int pivot=-1;
      for(int b=int(M)-1;b>=0;--b)if(v.test(b)){pivot=b;break;}
      auto it=basis.find(pivot);
      if(it==basis.end()){basis[pivot]=v;break;}
      v^=it->second;
    }
  }
  return (int)basis.size();
}
int main(){
  auto E=getfaces(2),T=getfaces(3),Q=getfaces(4);
  assert(getfaces(1).size()==27);
  assert(E.size()==351&&T.size()==2808&&Q.size()==3402);
  set<Face> subtri;
  for(auto q:Q){for(int drop=0;drop<4;++drop){Face t;for(int j=0;j<4;++j)if(j!=drop)t.push_back(q[j]);subtri.insert(t);}}
  vector<Face> f3;for(auto t:T)if(!subtri.count(t))f3.push_back(t);
  assert(f3.size()==540);
  assert((orbit_sizes(Q)==vector<int>{162,648,1296,1296}));
  assert((orbit_sizes(f3)==vector<int>{216,324}));
  map<Face,int> eidx,tidx;
  for(int j=0;j<(int)E.size();++j)eidx[E[j]]=j;
  for(int j=0;j<(int)T.size();++j)tidx[T[j]]=j;
  vector<bitset<351>> b2;for(auto t:T){bitset<351> v;
    for(int drop=0;drop<3;++drop){Face e;for(int j=0;j<3;++j)if(j!=drop)e.push_back(t[j]);v.flip(eidx.at(e));}
    b2.push_back(v);
  }
  vector<bitset<2808>> b3;for(auto q:Q){bitset<2808> v;
    for(int drop=0;drop<4;++drop){Face t;for(int j=0;j<4;++j)if(j!=drop)t.push_back(q[j]);v.flip(tidx.at(t));}
    b3.push_back(v);
  }
  int r2=rank_gf2(b2),r3=rank_gf2(b3);
  assert(r2==325&&r3==1913);
  int beta1=351-26-r2,beta2=2808-r2-r3,beta3=3402-r3;
  assert(beta1==0&&beta2==570&&beta3==1489);
  cout<<"CONCEPTS=27\nFACES=1,27,351,2808,3402\nFACETS_3=540\n";
  cout<<"ORBIT_4=162,648,1296,1296\nORBIT_FACET_3=216,324\n";
  cout<<"BOUNDARY_RANKS_1_2_3=26,325,1913\nBETTI_1_2_3=0,570,1489\n";
  cout<<"PASS\n";
}
