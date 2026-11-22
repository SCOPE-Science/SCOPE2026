// Independent whole-phase-space traversal and basin test.
// Build: c++ -O2 -std=c++17 verify_paths.cpp -o verify_paths
// Run: ./verify_paths
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int N = 15, M = 1<<N;
int main() {
  array<array<int,2>,N> edges{};
  int k=0;
  for(int u=0;u<6;u++) for(int v=u+1;v<6;v++) edges[k++]={u,v};
  for(int mode=0;mode<2;mode++) {
    vector<vector<int>> neighbors(N);
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) if(i!=j) {
      int meets=(edges[i][0]==edges[j][0] || edges[i][0]==edges[j][1]
              || edges[i][1]==edges[j][0] || edges[i][1]==edges[j][1]);
      if(meets==mode) neighbors[i].push_back(j);
    }
    int deg=neighbors[0].size();
    for(int i=0;i<N;i++) assert(int(neighbors[i].size())==deg);
    vector<int> F(M),depth(M,-1),per(M,0),which(M,-1);
    for(int x=0;x<M;x++) {
      int y=0;
      for(int i=0;i<N;i++) {
        int count=0;
        for(int j:neighbors[i]) count+=((x>>j)&1);
        int bit=2*count>deg || (2*count==deg && ((x>>i)&1));
        y |=bit<<i;
      }
      F[x]=y;
    }
    for(int x=0;x<M;x++) {
      if(depth[x]>=0) continue;
      vector<int> path;
      map<int,int> seen;
      int z=x;
      while(depth[z]<0 && seen.count(z)==0) {
        seen[z]=path.size(); path.push_back(z); z=F[z];
      }
      if(seen.count(z)) {
        int j=seen[z],p=int(path.size())-j;
        int rep=path[j];
        for(int a=j;a<int(path.size());a++) if(path[a]<rep) rep=path[a];
        for(int a=j;a<int(path.size());a++) {
          depth[path[a]]=0; per[path[a]]=p; which[path[a]]=rep;
        }
        path.resize(j);
      }
      for(int a=int(path.size())-1;a>=0;a--) {
        int b=path[a], t=F[b];
        depth[b]=depth[t]+1;per[b]=per[t];which[b]=which[t];
      }
    }
    map<pair<int,int>,int> entries, shapes;
    map<int,int> basins,periods;
    int bound=0;
    for(int x=0;x<M;x++) {
      entries[{per[x],depth[x]}]++;
      basins[which[x]]++;
      periods[which[x]]=per[x];
      if(depth[x]>bound) bound=depth[x];
    }
    for(auto a:basins) shapes[{periods[a.first],a.second}]++;
    map<pair<int,int>,int> want_entries,want_shapes;
    if(mode==1){
      want_entries={{{1,0},164},{{1,1},8544},{{1,2},15600},{{1,3},6660},{{2,0},1080},{{2,1},720}};
      want_shapes={{{1,1},120},{{1,22},30},{{1,236},12},{{1,13678},2},{{2,2},180},{{2,4},360}};
      assert(deg==8);
    } else {
      want_entries={{{1,0},502},{{1,1},4426},{{1,2},13680},{{1,3},5040},{{2,0},5340},{{2,1},3780}};
      want_shapes={{{1,1},360},{{1,10},140},{{1,10944},2},{{2,2},2460},{{2,20},210}};
      assert(deg==6);
    }
    assert(bound==3 && entries==want_entries && shapes==want_shapes);
    cout << (mode==1?"triangular":"kneser") << ": validated " << M
         << " state-orbits, max entry " << bound << ", " << basins.size() << " attractors\n";
  }
}
