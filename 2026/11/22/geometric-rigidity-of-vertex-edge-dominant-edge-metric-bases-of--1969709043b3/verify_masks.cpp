// Exhaustive bit-mask certificate for edge-distance identification and
// vertex-edge coverage on binary cubes. No external dependencies.
// Build: g++ -std=c++17 -O2 verify_masks.cpp -o verify_masks
// Run: ./verify_masks
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
using namespace std;
using U = uint64_t;
static int weight(int a) { return __builtin_popcount((unsigned)a); }
static U bit(int i) { return U(1) << i; }
static void insert(set<U>& v, const vector<int>& a) {
  U s=0;
  for (int x : a) { assert(!(s&bit(x))); s|=bit(x); }
  v.insert(s);
}
static set<U> geometry(int d) {
  const int n=1<<d, full=n-1;
  set<U> out;
  if (d==2) {
    for (int c=0;c<n;c++) for (int j=0;j<d;j++)
      insert(out,{c,c^(1<<j)});
  }
  if (d==3) {
    for (int p=0;p<2;p++) {
      vector<int> side;
      for (int x=0;x<n;x++) if (weight(x)%2==p) side.push_back(x);
      for (int i=0;i<4;i++) for (int j=i+1;j<4;j++)
       for (int k=j+1;k<4;k++) insert(out,{side[i],side[j],side[k]});
    }
    for (int c=0;c<n;c++) for (int i=0;i<d;i++) for (int j=i+1;j<d;j++)
      insert(out,{c,c^(1<<i),c^(1<<j)});
  }
  if (d==4) {
    for (int j=0;j<d;j++) for (int f=0;f<2;f++) for (int p=0;p<2;p++) {
      vector<int> a;
      for (int x=0;x<n;x++) if (((x>>j)&1)==f && weight(x)%2==p) a.push_back(x);
      assert(a.size()==4);insert(out,a);
    }
    for (int c=0;c<n;c++) for (int absent=0;absent<d;absent++) {
      vector<int> a{c^full};
      for (int j=0;j<d;j++) if (j!=absent) a.push_back(c^(1<<j));
      insert(out,a);
    }
    for (int a=0;a<n;a++) {
      int b=a^full; if (a>b) continue;
      for (int c=0;c<n;c++) for (int e=c+1;e<n;e++) {
        if (c==a || c==b || e==a || e==b)continue;
        if (weight(c)%2 != weight(a)%2 || weight(e)%2 != weight(a)%2)continue;
        if ((c^e)==full)continue;
        insert(out,{a,b,c,e});
      }
    }
  }
  if (d==5) {
    for (int c=0;c<n;c++) for (int absent=0;absent<d;absent++) {
      vector<int> a{c^full};
      for (int j=0;j<d;j++) if (j!=absent) a.push_back(c^(1<<j));
      insert(out,a);
    }
  }
  return out;
}
struct Summary { long long resolving=0, dominated=0, joint=0; set<U> jointsets; };
static Summary count(int d, int k) {
  int n=1<<d;
  vector<pair<int,int>> edges;
  for (int u=0;u<n;u++) for(int j=0;j<d;j++) if (!(u&(1<<j)))edges.push_back({u,u^(1<<j)});
  int m=edges.size();
  vector<vector<int>> D(n,vector<int>(m));
  vector<U> ve(m,0), separating;
  for (int s=0;s<n;s++) for(int e=0;e<m;e++) {
    auto [u,v]=edges[e]; D[s][e]=min(weight(s^u),weight(s^v));
    if (D[s][e]<=1)ve[e]|=bit(s);
  }
  for (int e=0;e<m;e++) for (int f=0;f<e;f++) {
    U mask=0;
    for (int s=0;s<n;s++) if (D[s][e]!=D[s][f])mask|=bit(s);
    separating.push_back(mask);
  }
  Summary result;
  function<void(int,int,U)> recurse=[&](int first,int left,U mask) {
    if (left==0) {
      bool r=true,v=true;
      for (U c:separating) if (!(mask&c)) {r=false;break;}
      for (U c:ve) if (!(mask&c)) {v=false;break;}
      result.resolving+=r;result.dominated+=v;
      if(r&&v){result.joint++;result.jointsets.insert(mask);}
      return;
    }
    for (int x=first;x<=n-left;x++)recurse(x+1,left-1,mask|bit(x));
  };
  recurse(0,k,0);
  return result;
}
int main() {
  int mins[6]={0,0,2,3,4,5};
  int lower_res[6]={0,0,0,0,64,1280};
  int lower_ve[6]={0,0,4,16,112,80};
  int opt[6]={0,0,4,32,176,160};
  for (int d=2;d<=5;d++) {
    int k=mins[d];
    if (d>=4) assert(count(d,k-2).resolving==0);
    auto prev=count(d,k-1), top=count(d,k);
    assert(prev.resolving==lower_res[d] && prev.dominated==lower_ve[d] && prev.joint==0);
    assert(top.joint==opt[d]);
    auto canonical=geometry(d);
    assert(top.jointsets==canonical);
    cout<<"Q"<<d<<": lower_res="<<prev.resolving
        <<" lower_ve="<<prev.dominated
        <<" lower_joint="<<prev.joint
        <<" minimum="<<k
        <<" bases="<<top.joint
        <<" family_equal=true\n";
  }
  cout<<"CUBE_VE_EDGE_CPP_OK\n";
}
