// Exact exhaustive two-neighbour percolation on the four-dimensional cube.
// Compile: c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
// Run: ./verify_direct
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
using namespace std;
int main(){
 constexpr int N=16, M=1<<N, FULL=M-1;
 array<uint16_t,N> adj{};
 for(int v=0;v<N;v++)for(int d=0;d<4;d++) adj[v]|=uint16_t(1u<<(v^(1<<d)));
 array<uint16_t,M> terminal{}; array<int,M> rounds{};
 for(int seed=0;seed<M;seed++){
   uint16_t old=uint16_t(seed); int t=0;
   while(true){
     uint16_t next=old;
     for(int v=0;v<N;v++) if(!(old&(1u<<v)) && __builtin_popcount(unsigned(old & adj[v]))>=2) next|=uint16_t(1u<<v);
     if(next==old) break;
     old=next; t++;
     if(t>16) throw runtime_error("nontermination");
   }
   terminal[seed]=old; rounds[seed]=t;
 }
 map<pair<int,int>,int> minimal_by_size_time;
 map<int,int> max_time_by_size;
 int percolating=0, minimal_total=0, max_time=0;
 for(int seed=0;seed<M;seed++) if(terminal[seed]==FULL){
   percolating++; int size=__builtin_popcount(unsigned(seed));
   if(rounds[seed]>max_time) max_time=rounds[seed];
   if(rounds[seed]==5) max_time_by_size[size]++;
   bool minimal=true;
   for(int v=0;v<N;v++)if(seed&(1u<<v))
     if(terminal[seed^(1<<v)]==FULL) {minimal=false;break;}
   if(minimal){ minimal_total++; minimal_by_size_time[{size,rounds[seed]}]++; }
 }
 cout<<"percolating "<<percolating<<"\nminimal "<<minimal_total<<"\n";
 for(auto [p,c]:minimal_by_size_time) cout<<"minimal size "<<p.first<<" time "<<p.second<<" count "<<c<<"\n";
 cout<<"maximum time "<<max_time<<"\n";
 for(auto [s,c]:max_time_by_size)cout<<"time5 size "<<s<<" count "<<c<<"\n";
 if(percolating!=63687 || minimal_total!=256 || max_time!=5 ||
    minimal_by_size_time!=map<pair<int,int>,int>{{{3,4},48},{{3,5},96},{{4,3},16},{{4,4},96}} ||
    max_time_by_size!=map<int,int>{{3,96},{4,96}})
     throw runtime_error("enumeration mismatch");
 cout<<"PASS\n";
}
