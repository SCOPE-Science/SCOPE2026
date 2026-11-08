// Exhaustive 64-profile graph enumeration and integer BEST/matrix-tree count.
// Standard C++17, no external dependencies. Prints GRAPH_VERIFY_OK.
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
using Edge=pair<int,int>;

// Indexed alphabet: A=0,C=1,G=2,T=3. Complement 3-i.
static int det3(const int M[4][4]) {
    const int a=M[0][0], b=M[0][1], c=M[0][2];
    return a*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
         - b*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
         + c*(M[1][0]*M[2][1]-M[1][1]*M[2][0]);
}
static int fact(int x) { int v=1; for(int i=2;i<=x;i++)v*=i;return v; }

int main() {
    const vector<Edge> fixed={{0,3},{3,0},{1,2},{2,1}};
    const vector<array<Edge,2>> pairs = {
      array<Edge,2>{Edge{0,0},Edge{3,3}},
      array<Edge,2>{Edge{0,1},Edge{2,3}},
      array<Edge,2>{Edge{0,2},Edge{1,3}},
      array<Edge,2>{Edge{1,0},Edge{3,2}},
      array<Edge,2>{Edge{1,1},Edge{2,2}},
      array<Edge,2>{Edge{2,0},Edge{3,1}}
    };
    int balanced=0, connected=0, total=0;
    map<pair<int,int>,int> groups; // (arborescences, circuits) -> #graphs
    for(int choice=0;choice<64;choice++) {
        vector<Edge> edges=fixed;
        for(int j=0;j<6;j++)edges.push_back(pairs[j][(choice>>j)&1]);
        int out[4]={0},in[4]={0},L[4][4]={};
        set<Edge> seen;
        for(const auto &e:edges){
          assert(seen.insert(e).second);
          out[e.first]++;in[e.second]++;
          L[e.first][e.first]++;L[e.first][e.second]--;
        }
        bool ok=true;
        for(int j=0;j<4;j++)if(out[j]!=in[j])ok=false;
        if(!ok)continue;
        balanced++;
        int trees=det3(L);
        if(trees>0)connected++;
        int mult=trees;
        for(int j=0;j<4;j++)mult*=fact(out[j]-1);
        groups[{trees,mult}]++;
        total+=mult;
    }
    assert(balanced==24 && connected==24 && total==544);
    assert(groups.size()==3);
    assert(groups.at(make_pair(3,12))==8 && groups.at(make_pair(3,36))==8 && groups.at(make_pair(5,20))==8);
    cout<<"GRAPH_VERIFY_OK balanced=24 connected=24 total=544 groups=8x12+8x20+8x36\n";
}
