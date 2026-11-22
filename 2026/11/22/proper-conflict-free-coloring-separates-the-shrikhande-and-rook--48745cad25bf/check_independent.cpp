// Independent exact certificate replay on the fixed sixteen-vertex graphs.
// Build: c++ -O2 -std=c++17 check_independent.cpp -o check_independent
// Run: ./check_independent
#include <array>
#include <cassert>
#include <iostream>
using namespace std;
int main(){
 const array<array<int,4>,4> s={{{0,4,0,2},{1,3,2,4},{2,0,1,0},{3,1,3,4}}};
 const array<array<int,4>,4> r={{{0,1,2,4},{1,4,3,2},{2,3,0,5},{5,0,1,3}}};
 const array<pair<int,int>,6> step={{{1,0},{3,0},{0,1},{0,3},{1,1},{3,3}}};
 for(int g=0;g<2;g++){
  const auto &f=g==0?s:r;
  bool adj[16][16]={};
  for(int v=0;v<16;v++)for(int w=0;w<16;w++) if(v!=w){
   int a=v/4,b=v%4,c=w/4,d=w%4;
   if(g==1)adj[v][w]=a==c || b==d;
   else for(auto [dx,dy]:step)if((c-a+4)%4==dx && (d-b+4)%4==dy)adj[v][w]=true;
  }
  int palette= g==0?5:6;
  bool seen[6]={};
  for(int v=0;v<16;v++){
   int x=v/4,y=v%4, cnt[6]={};
   seen[f[x][y]]=true;
   int degree=0;
   for(int w=0;w<16;w++)if(adj[v][w]){
    degree++;
    assert(f[x][y]!=f[w/4][w%4]);
    cnt[f[w/4][w%4]]++;
   }
   assert(degree==6);
   bool unique=false;
   for(int c=0;c<palette;c++) unique|=(cnt[c]==1);
   assert(unique);
  }
  for(int c=0;c<palette;c++)assert(seen[c]);
  for(int v=0;v<16;v++)for(int w=v+1;w<16;w++){
   int common=0;for(int x=0;x<16;x++)if(adj[v][x]&&adj[w][x])common++;
   assert(common==2);
  }
  cout << (g==0?"Shrikhande":"Rook") << " certificate PASS\n";
 }
}
