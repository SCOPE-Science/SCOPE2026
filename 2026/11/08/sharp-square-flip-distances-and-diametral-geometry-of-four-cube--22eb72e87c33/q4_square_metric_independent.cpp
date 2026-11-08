// Independent C++17 enumeration via permutations of the odd side of Q4.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;

int main() {
  vector<int> left, right;
  for (int v=0; v<16; ++v) {
    if (__builtin_popcount((unsigned)v)%2==0) left.push_back(v);
    else right.push_back(v);
  }
  assert(left.size()==8 && right.size()==8);
  array<int,8> p{};
  iota(p.begin(),p.end(),0);
  vector<array<int,8>> M;
  do {
    bool ok=true;
    for (int i=0;i<8;++i)
      if (__builtin_popcount((unsigned)(left[i]^right[p[i]])) != 1) ok=false;
    if (ok) M.push_back(p);
  } while (next_permutation(p.begin(),p.end()));
  assert(M.size()==272);
  map<array<int,8>,int> ind;
  for (int i=0;i<(int)M.size();++i) ind[M[i]]=i;
  vector<set<int>> G(M.size());
  for (int x=0;x<(int)M.size();++x)
    for (int i=0;i<8;++i) for (int j=i+1;j<8;++j) {
      auto q=M[x];
      if (__builtin_popcount((unsigned)(left[i]^right[q[j]]))!=1 ||
          __builtin_popcount((unsigned)(left[j]^right[q[i]]))!=1) continue;
      swap(q[i],q[j]);
      auto it=ind.find(q);
      assert(it!=ind.end());
      G[x].insert(it->second);
    }
  long long directed=0;
  map<int,int> deg;
  for (int x=0;x<(int)M.size();++x) {
    deg[(int)G[x].size()]++;
    directed += G[x].size();
    for(int y:G[x]) assert(G[y].count(x));
  }
  assert(directed==1536);
  assert((deg==map<int,int>{{0,8},{3,32},{4,12},{5,96},{6,48},{8,72},{12,4}}));

  vector<int> component(M.size(),-1),sizes;
  for (int x=0;x<(int)M.size();++x) if(component[x]<0) {
    int label=sizes.size(), count=0;
    queue<int> q; q.push(x);component[x]=label;
    while(!q.empty()) {
      int u=q.front();q.pop();++count;
      for(int v:G[u]) if(component[v]<0) {component[v]=label;q.push(v);}
    }
    sizes.push_back(count);
  }
  sort(sizes.begin(),sizes.end());
  assert(sizes==vector<int>({1,1,1,1,1,1,1,1,264}));
  int giant=-1;
  for(int x=0;x<(int)M.size();++x)
    if(G[x].size()>0) {giant=component[x];break;}
  assert(giant>=0);

  map<int,int> eccentricity;
  map<int,long long> pairs;
  vector<int> per;
  vector<vector<int>> dist(M.size());
  for (int x=0;x<(int)M.size();++x) if(component[x]==giant) {
    vector<int> d(M.size(),-1);
    queue<int> q;d[x]=0;q.push(x);
    while(!q.empty()) {
      int u=q.front();q.pop();
      for(int v:G[u]) if(d[v]<0){d[v]=d[u]+1;q.push(v);}
    }
    int visited=0,ecc=0;
    for(int y=0;y<(int)M.size();++y) if(component[y]==giant) {
      assert(d[y]>=0);++visited;ecc=max(ecc,d[y]);
      if(y>x) pairs[d[y]]++;
    }
    assert(visited==264);
    eccentricity[ecc]++;
    if (ecc==8) per.push_back(x);
    dist[x]=move(d);
  }
  assert((eccentricity==map<int,int>{{7,252},{8,12}}));
  assert((pairs==map<int,long long>{{1,768},{2,2640},{3,6032},{4,9360},
                                    {5,9504},{6,5296},{7,1104},{8,12}}));
  assert(per.size()==12);
  // Explicit witness: actual odd neighbors indexed by increasing even vertices.
  array<int,8> witnessA={1,2,7,4,11,8,13,14};
  array<int,8> witnessB={4,7,13,14,1,2,8,11};
  array<int,8> wa{},wb{};
  for(int k=0;k<8;++k){
    wa[k]=int(find(right.begin(),right.end(),witnessA[k])-right.begin());
    wb[k]=int(find(right.begin(),right.end(),witnessB[k])-right.begin());
    assert(wa[k]<8 && wb[k]<8);
  }
  assert(dist[ind.at(wa)][ind.at(wb)]==8);
  for(int x:per) assert(G[x].size()==4);
  vector<int> farComp(M.size(),-1);
  int farCC=0;
  for(int x:per) if(farComp[x]<0) {
    queue<int> q;q.push(x);farComp[x]=farCC;int count=0;
    while(!q.empty()){
      int u=q.front();q.pop();++count;
      int farDegree=0;
      for(int v:per) if(dist[u][v]==8){
        ++farDegree;
        if(farComp[v]<0){farComp[v]=farCC;q.push(v);}
      }
      assert(farDegree==2);
    }
    assert(count==4);++farCC;
  }
  assert(farCC==3);
  cout << "CPP_Q4_SQUARE_METRIC_PASS\n";
  cout << "matchings=272 flip_edges=768 components=264+8*1\n";
  cout << "mobile_radius=7 mobile_diameter=8 mobile_ecc=7:252,8:12\n";
  cout << "diametral_pair_graph=3*C4 peripheral_iff_degree4=true\n";
}
