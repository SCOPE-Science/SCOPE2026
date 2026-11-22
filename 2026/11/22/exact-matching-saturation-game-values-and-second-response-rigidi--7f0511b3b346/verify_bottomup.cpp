// Exact independent finite certificate: bottom-up minimax on every vertex mask.
// No third-party libraries; each graph specified by an explicit edge list.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <utility>
#include <vector>
using namespace std;
using Edge=pair<int,int>;
struct Graph {string name;int n;vector<Edge> edges;};
struct Result {
 int n,e,smallest,largest,maxfirst,minfirst;
 map<int,int> hm,hn;
};
Result solve(const Graph& G){
 int n=G.n, lim=1<<n;
 vector<uint8_t> vmax(lim),vmin(lim),smallest(lim),largest(lim);
 for(int mask=1;mask<lim;mask++){
  int hi=0,lo=99,mn=99,mx=0, legal=0;
  for(auto [u,v]:G.edges){
   int pairmask=(1<<u)|(1<<v);
   if((mask&pairmask)!=pairmask) continue;
   legal++;
   int rem=mask^pairmask;
   hi=max(hi,1+(int)vmin[rem]);
   lo=min(lo,1+(int)vmax[rem]);
   mn=min(mn,1+(int)smallest[rem]);
   mx=max(mx,1+(int)largest[rem]);
  }
  if(legal){vmax[mask]=hi;vmin[mask]=lo;smallest[mask]=mn;largest[mask]=mx;}
 }
 Result r{n,(int)G.edges.size(),smallest[lim-1],largest[lim-1],vmax[lim-1],vmin[lim-1],{}, {}};
 for(size_t i=0;i<G.edges.size();i++){
  auto [a,b]=G.edges[i];
  int rem=(lim-1)^((1<<a)|(1<<b));
  map<int,int> hm,hn;
  for(auto [u,v]:G.edges){
   int pairmask=(1<<u)|(1<<v);
   if((rem&pairmask)!=pairmask)continue;
   int tail=rem^pairmask;
   hm[2+(int)vmax[tail]]++;
   hn[2+(int)vmin[tail]]++;
  }
  if(i==0){r.hm=hm;r.hn=hn;}
  else {assert(r.hm==hm && r.hn==hn);}
 }
 return r;
}
void printHist(map<int,int> const& h){
 cout<<"[";bool first=true;
 for(auto [value,count]:h){if(!first)cout<<",";first=false;cout<<"["<<value<<","<<count<<"]";}
 cout<<"]";
}
int main(){
 vector<Graph> graphs={
 {"tetrahedron",4,{{0,1},{0,2},{0,3},{1,2},{1,3},{2,3}}},
 {"cube",8,{{0,1},{0,3},{0,4},{1,2},{1,7},{2,3},{2,6},{3,5},{4,5},{4,7},{5,6},{6,7}}},
 {"octahedron",6,{{0,1},{0,2},{0,3},{0,4},{1,2},{1,3},{1,5},{2,4},{2,5},{3,4},{3,5},{4,5}}},
 {"dodecahedron",20,{{0,1},{0,10},{0,19},{1,2},{1,8},{2,3},{2,6},{3,4},{3,19},{4,5},{4,17},{5,6},{5,15},{6,7},{7,8},{7,14},{8,9},{9,10},{9,13},{10,11},{11,12},{11,18},{12,13},{12,16},{13,14},{14,15},{15,16},{16,17},{17,18},{18,19}}},
 {"icosahedron",12,{{0,1},{0,5},{0,7},{0,8},{0,11},{1,2},{1,5},{1,6},{1,8},{2,3},{2,6},{2,8},{2,9},{3,4},{3,6},{3,9},{3,10},{4,5},{4,6},{4,10},{4,11},{5,6},{5,11},{7,8},{7,9},{7,10},{7,11},{8,9},{9,10},{10,11}}}
 };
 sort(graphs.begin(),graphs.end(),[](const Graph& a,const Graph& b){return a.name<b.name;});
 cout<<"{";bool first=true;
 for(auto const& g:graphs){
  Result r=solve(g);
  if(!first)cout<<",";first=false;
  cout<<"\""<<g.name<<"\":{\"edges\":"<<r.e<<",\"max_first\":"<<r.maxfirst<<",\"max_matching\":"<<r.largest<<",\"maxfirst_second_response_hist\":";
  printHist(r.hm);
  cout<<",\"min_first\":"<<r.minfirst<<",\"min_maximal\":"<<r.smallest<<",\"minfirst_second_response_hist\":";
  printHist(r.hn);
  cout<<",\"vertices\":"<<r.n<<"}";
 }
 cout<<"}\n";
}
