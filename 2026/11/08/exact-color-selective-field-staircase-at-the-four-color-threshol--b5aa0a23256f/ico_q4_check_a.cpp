// Exact recursive four-color census, with the canonical icosahedron edge table.
#include <array>
#include <cstdint>
#include <iostream>
using namespace std;
static const int E[30][2]={{0,1},{0,5},{0,7},{0,8},{0,11},{1,2},{1,5},{1,6},{1,8},{2,3},{2,6},{2,8},{2,9},{3,4},{3,6},{3,9},{3,10},{4,5},{4,6},{4,10},{4,11},{5,6},{5,11},{7,8},{7,9},{7,10},{7,11},{8,9},{9,10},{10,11}};
static const int B[13]={3,2,1,0,1,3,5,8,11,15,20,25,30};
static const long long C[13]={120,720,1080,240,1080,7560,6840,8640,1620,540,324,36,1};
long long count=0,deg[13]={};int minmono[13],sp[12];
void dfs(int i,int fav,int mono){
 if(i==12){count++;if(mono<minmono[fav]){minmono[fav]=mono;deg[fav]=1;}else if(mono==minmono[fav])deg[fav]++;return;}
 for(int color=0;color<4;color++){
  sp[i]=color;int inc=0;
  for(auto &e:E)if(e[1]==i && sp[e[0]]==color)inc++; // edge list ascending u<v
  dfs(i+1,fav+(color==0),mono+inc);
 }
}
int main(){for(int i=0;i<=12;i++)minmono[i]=999;dfs(0,0,0);
 if(count!=16777216){cerr<<"wrong total\n";return 2;}
 for(int i=0;i<=12;i++){if(minmono[i]!=B[i]||deg[i]!=C[i]){cerr<<"error "<<i<<" "<<minmono[i]<<" "<<deg[i]<<"\n";return 2;}}
 cout<<"PASS: recursive exhaustive independent edge table all 4^12 colorings\n";return 0;
}
