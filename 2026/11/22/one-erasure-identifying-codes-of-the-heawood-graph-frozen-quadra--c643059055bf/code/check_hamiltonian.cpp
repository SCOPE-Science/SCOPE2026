// Independent exact verifier using the Hamiltonian-chord representation of H14.
// For each detector placement, explicitly delete each chosen detector and
// retest all fourteen resulting identifying signatures. Standard C++17 only.
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
static constexpr int N=14, FULL=(1<<N)-1;
int A[N] = {};
void edge(int a,int b) { A[a] |= 1<<b; A[b] |= 1<<a; }
bool identifying(int code) {
  int sig[N];
  for(int v=0;v<N;++v) {
    sig[v] = code & (A[v] | (1<<v));
    if(!sig[v]) return false;
  }
  for(int u=0;u<N;++u)
    for(int v=u+1;v<N;++v)
      if(sig[u] == sig[v]) return false;
  return true;
}
bool redundant(int code) {
  if(!identifying(code)) return false;
  for(int c=0;c<N;++c) if(code & (1<<c))
    if(!identifying(code ^ (1<<c))) return false;
  return true;
}
int pop(int mask) { return __builtin_popcount((unsigned)mask); }
struct Metr {int edges=0; map<int,int> degrees,components,ecc; map<vector<int>,int> shells;};
Metr analyze(const vector<int>& opt,int moves) {
  const int K=(int)opt.size();
  vector<vector<int>> adj(K);
  for(int i=0;i<K;++i) for(int j=i+1;j<K;++j)
    if(pop(opt[i]^opt[j])==2*moves) {
      adj[i].push_back(j); adj[j].push_back(i);
    }
  Metr z;
  for(const auto &e:adj) {z.degrees[(int)e.size()]++;z.edges+=(int)e.size();}
  z.edges/=2;
  vector<bool> seen(K,false);
  for(int i=0;i<K;++i) if(!seen[i]) {
    queue<int> q;q.push(i);seen[i]=true;int size=0;
    while(!q.empty()) {
      int v=q.front();q.pop();++size;
      for(int w:adj[v]) if(!seen[w]) {seen[w]=true;q.push(w);}
    }
    ++z.components[size];
  }
  for(int start=0;start<K;++start) {
    vector<int> dist(K,-1);queue<int> q;dist[start]=0;q.push(start);
    while(!q.empty()) {
      int v=q.front();q.pop();
      for(int w:adj[v]) if(dist[w]<0) {dist[w]=dist[v]+1;q.push(w);}
    }
    int maxd=*max_element(dist.begin(),dist.end());
    if(maxd>0) {
      ++z.ecc[maxd]; vector<int> shell(maxd+1);
      for(int x:dist) if(x>=0) ++shell[x];
      ++z.shells[shell];
    }
  }
  return z;
}
int main() {
  for(int i=0;i<N;++i) edge(i,(i+1)%N);
  for(auto [a,b]:vector<pair<int,int>>{{0,5},{1,10},{2,7},{3,12},
                                       {4,9},{6,11},{8,13}}) edge(a,b);
  for(int i=0;i<N;++i) assert(pop(A[i])==3);
  map<int,int> bysize;
  vector<int> best;
  for(int mask=0;mask<=FULL;++mask) if(redundant(mask)) {
    int k=pop(mask);bysize[k]++;
    if(best.empty() || k<pop(best.front())) best={mask};
    else if(k==pop(best.front())) best.push_back(mask);
  }
  assert(((bysize==map<int,int>{{10,98},{11,224},{12,91},{13,14},{14,1}})));
  assert(best.size()==98);
  int isolated_shore=0, two_match=0;
  // A uniform structural test, not the signature inequalities:
  // Omitted quadruples are either independent one-shore quadrangles
  // or induce two disjoint edges in the full graph.
  for(int code:best) {
    int omit=FULL^code;
    assert(pop(omit)==4);
    int shore0=0;for(int i=0;i<N;i+=2) shore0+= (omit>>i)&1;
    int edges=0; int degree[14]={};
    for(int i=0;i<N;++i) if(omit&(1<<i))
      for(int j=i+1;j<N;++j) if((omit&(1<<j))&&(A[i]&(1<<j))) {
        ++edges;++degree[i];++degree[j];
      }
    if(shore0==0 || shore0==4) {assert(edges==0);++isolated_shore;}
    else {
      assert(shore0==2 && edges==2);
      for(int i=0;i<N;++i) if(omit&(1<<i)) assert(degree[i]==1);
      ++two_match;
    }
  }
  assert(isolated_shore==14 && two_match==84);
  auto one=analyze(best,1),two=analyze(best,2);
  assert((one.edges==168 && one.degrees==map<int,int>({{0,14},{4,84}})));
  assert((one.components==map<int,int>({{1,14},{84,1}})));
  assert((one.ecc==map<int,int>({{5,84}})));
  assert((one.shells==map<vector<int>,int>({{{1,4,10,22,39,8},84}})));
  assert((two.edges==1134 && two.degrees==map<int,int>({{22,84},{30,14}})));
  assert((two.components==map<int,int>({{98,1}})));
  assert((two.ecc==map<int,int>({{2,98}})));
  assert((two.shells==map<vector<int>,int>({{{1,22,75},84},{{1,30,67},14}})));
  cout<<"minimum=10 optima=98; all-size=10:98,11:224,12:91,13:14,14:1\n";
  cout<<"omitted=14 one-shore quadrangles + 84 induced two-edge matchings\n";
  cout<<"one-change edges=168, components=14*1+1*84, giant degree=4, diameter=5\n";
  cout<<"two-changes edges=1134, components=1*98, diameter=2\n";
}
