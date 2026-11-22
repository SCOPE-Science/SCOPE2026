// Exact 14-bit state census for open-neighborhood NOR on the Fano incidence graph.
// Compile: c++ -O2 -std=c++17 heawood_nor.cpp -o heawood_nor
#include <array>
#include <algorithm>
#include <map>
#include <utility>
#include <iostream>
#include <cassert>
using namespace std;
int main() {
 constexpr int n=14, size=1<<n;
 array<int,n> adj{};
 for(int j=0;j<7;++j)
   for(int d: {0,1,3}) {int p=(j+d)%7,q=7+j; adj[p]|=1<<q; adj[q]|=1<<p;}
 auto F=[&](int x){int out=0;for(int i=0;i<n;++i)if(!(x&adj[i]))out|=1<<i;return out;};
 map<pair<int,int>,int> basins;
 map<pair<int,int>,int> layer;
 int fixed=0, period2_states=0;
 for(int x=0;x<size;++x){
   int a=F(x), b=F(a);
   assert(F(b)==a);
   bool periodic=(x==a || x==b);
   int period=(a==b?1:2);
   if (x==a) ++fixed;
   if (x==b && a!=b) ++period2_states;
   ++layer[{periodic?0:1,period}];
   ++basins[minmax(a,b)];
 }
 map<int,int> fb,ob;
 for(auto const& kv:basins){
   bool eq=(kv.first.first==kv.first.second);
   ++(eq?fb:ob)[kv.second];
 }
 assert(fixed==37 && period2_states==1332 && basins.size()==703);
 assert(layer.at({0,1})==37 && layer.at({0,2})==1332);
 assert(layer.at({1,1})==182 && layer.at({1,2})==14833);
 assert((fb==map<int,int>({{1,21},{5,14},{64,2}})));
 assert((ob==map<int,int>({{2,210},{6,294},{10,42},{26,49},{65,42},{69,14},{321,14},{4097,1}})));
 cout << "states 16384\nfixed 37\nprimitive_two_orbits 666\nfirst_entry (0,1)=37 (0,2)=1332 (1,1)=182 (1,2)=14833\nfixed_basins";
 for(auto [k,v]:fb) cout << " "<<k<<":"<<v;
 cout << "\ntwo_basins";
 for(auto [k,v]:ob) cout << " "<<k<<":"<<v;
 cout << "\n";
}
