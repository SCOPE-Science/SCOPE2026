// Exact enumeration of the Schur constraint-deletion profile on [1,14].
// Requires only a C++17 compiler and the supplied critical_triples.csv.
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
struct Triple {int a,b,c;};
int main() {
    const int n=14;
    vector<Triple> triples;
    array<vector<int>,15> ending;
    for (int a=1; a<=n; ++a)
      for (int b=a; a+b<=n; ++b) {
        int j=int(triples.size());
        triples.push_back({a,b,a+b});
        ending[a+b].push_back(j);
      }
    assert(triples.size()==49);
    vector<long long> one(triples.size(),0);
    array<int,15> color;
    color.fill(-1); color[1]=0;
    long long zero=0, oneTotal=0;
    auto dfs = [&](auto&& recur, int next, int bad, int sole)->void {
        if (next>n) {
            if (bad==0) ++zero;
            else {assert(bad==1 && sole>=0);++oneTotal;++one[sole];}
            return;
        }
        for (int hue=0; hue<3; ++hue) {
            color[next]=hue;
            int nb=bad, id=sole;
            for (int t:ending[next]) {
                auto e=triples[t];
                if (color[e.a]==hue && color[e.b]==hue) {
                    ++nb;id=t;
                    if(nb>1) break;
                }
            }
            if (nb<=1) recur(recur,next+1,nb,id);
        }
        color[next]=-1;
    };
    dfs(dfs,2,0,-1);
    if (zero!=0 || oneTotal!=1350) {cerr<<"Unexpected totals "<<zero<<" "<<oneTotal<<'\n';return 1;}
    ifstream in("critical_triples.csv");
    if (!in) {cerr<<"Missing critical_triples.csv\n";return 1;}
    string line;getline(in,line);
    if (line!="x,y,z,normalized_colorings,named_colorings,critical") return 2;
    int rows=0,critical=0;
    while(getline(in,line)) {
        stringstream ss(line);string w;array<int,6> vals;
        for(int k=0;k<6;k++) {
            if(!getline(ss,w,',')) return 3;
            vals[k]=stoi(w);
        }
        if(rows>=int(triples.size())) return 4;
        auto e=triples[rows];
        if(vals[0]!=e.a||vals[1]!=e.b||vals[2]!=e.c ||
           vals[3]!=one[rows] || vals[4]!=3*one[rows] ||
           vals[5]!=(one[rows]>0)) return 5;
        critical+=(one[rows]>0);++rows;
    }
    if(rows!=49 || critical!=29) return 6;
    cout<<"PASS C++ incremental: all 3^13 normalized colorings with at most one "
        <<"violation; zero="<<zero<<" one="<<oneTotal
        <<" critical="<<critical<<" out of "<<rows<<"\n";
}
