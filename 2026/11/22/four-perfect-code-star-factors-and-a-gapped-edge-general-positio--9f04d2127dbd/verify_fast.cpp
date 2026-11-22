// Exact edge-geodesic-position census of the 16-vertex GP(8,3).
// C++17; uses no external data or libraries.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using U = uint32_t;
int main() {
  set<pair<int,int>> es;
  auto insert_edge = [&](int x, int y) {
    if (x > y) swap(x,y);
    es.insert({x,y});
  };
  for(int i=0;i<8;i++) {
    insert_edge(i,(i+1)%8);
    insert_edge(i,8+i);
    insert_edge(8+i,8+(i+3)%8);
  }
  vector<pair<int,int>> E(es.begin(),es.end());
  assert(E.size()==24);
  vector<vector<pair<int,int>>> adj(16);
  for(int i=0;i<24;i++) {
    auto [a,b]=E[i];
    adj[a].push_back({b,i});adj[b].push_back({a,i});
  }
  for(auto &v:adj) assert(v.size()==3);
  int d[16][16];
  int diam=0;
  for(int s=0;s<16;s++) {
    fill(d[s],d[s]+16,99);d[s][s]=0;
    queue<int> q;q.push(s);
    while(!q.empty()) {
      int v=q.front();q.pop();
      for(auto [w,e]:adj[v]) if(d[s][w]==99) {
        d[s][w]=d[s][v]+1;q.push(w);
      }
    }
    for(int v=0;v<16;v++)diam=max(diam,d[s][v]);
  }
  assert(diam==4);
  set<U> bad;
  for(int s=0;s<16;s++) {
    vector<int> path;
    auto trace = [&](auto&& self,int v)->void {
      if (v>s && path.size()>=3) {
        int z=path.size();
        for(int i=0;i<z;i++)for(int j=i+1;j<z;j++)for(int k=j+1;k<z;k++)
          bad.insert((U(1)<<path[i])|(U(1)<<path[j])|(U(1)<<path[k]));
      }
      for(auto [w,e]:adj[v]) if(d[s][w]==d[s][v]+1) {
        path.push_back(e);self(self,w);path.pop_back();
      }
    };
    trace(trace,s);
  }
  assert(bad.size()==192);
  vector<vector<U>> triples_at_max(24);
  for(U t:bad) {
    int b=31-__builtin_clz(t);
    triples_at_max[b].push_back(t^(U(1)<<b));
  }
  const U ALL=(U(1)<<24)-1;
  vector<uint8_t> ok(ALL+1,0);
  ok[0]=1;
  array<uint64_t,25> h{}, f{};
  h[0]=1;
  vector<U> max_masks;
  for(U x=1;x<=ALL;x++) {
    int b=31-__builtin_clz(x);
    U base=x^(U(1)<<b);
    if(!ok[base])continue;
    bool valid=true;
    for(U pair:triples_at_max[b]) if((base&pair)==pair) {valid=false;break;}
    if(!valid)continue;
    ok[x]=1;
    int k=__builtin_popcount(x);h[k]++;
    if(k==12)max_masks.push_back(x);
    if(k>12){cerr<<"unexpected candidate >12\n";return 1;}
  }
  for(U x=0;x<=ALL;x++) if(ok[x]) {
    bool maximal=true;
    U r=ALL^x;
    while(r) {
      U bit=r&(-r);r^=bit;
      if(ok[x|bit]){maximal=false;break;}
    }
    if(maximal)f[__builtin_popcount(x)]++;
  }
  const array<uint64_t,25> h_want={1,24,276,1832,7362,17712,24468,18240,7017,1576,300,48,4};
  const array<uint64_t,25> f_want={0,0,0,0,0,0,0,792,1329,336,36,0,4};
  if(h!=h_want || f!=f_want){cerr<<"census mismatch\n";return 2;}
  if(max_masks.size()!=4){cerr<<"maximum census mismatch\n";return 3;}
  vector<U> code_masks;
  for(int a=0;a<16;a++)for(int b=a+1;b<16;b++)
  for(int c=b+1;c<16;c++)for(int e=c+1;e<16;e++) {
    array<int,4> C={a,b,c,e};
    int hits[16]={};
    for(int v:C) {
      hits[v]++;
      for(auto [w,edge]:adj[v])hits[w]++;
    }
    if(!all_of(hits,hits+16,[](int k){return k==1;}))continue;
    U x=0;
    for(int i=0;i<24;i++) {
      auto [p,q]=E[i];
      if(find(C.begin(),C.end(),p)!=C.end() || find(C.begin(),C.end(),q)!=C.end())
        x|=U(1)<<i;
    }
    code_masks.push_back(x);
  }
  sort(max_masks.begin(),max_masks.end());
  sort(code_masks.begin(),code_masks.end());
  if(code_masks!=max_masks){cerr<<"efficient-domination correspondence mismatch\n";return 4;}
  for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)
    if(__builtin_popcount(max_masks[i]&max_masks[j])!=4){cerr<<"intersection mismatch\n";return 5;}
  cout<<"VERIFY_FAST_OK vertices=16 edges=24 diameter=4 triple_obstructions=192\n";
  cout<<"face_counts:";
  for(int i=0;i<=12;i++)cout<<" "<<h[i];
  cout<<"\nfacet_counts:";
  for(int i=0;i<=12;i++)cout<<" "<<f[i];
  cout<<"\nmax_masks:";
  for(U x:max_masks)cout<<" "<<x;
  cout<<"\n";
}
