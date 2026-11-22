// Reproduce the binary rank-three point-image shattering classification by exhaustive enumeration.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
static int rank2(vector<int> a) {
 int basis[3]={0,0,0}; int r=0;
 for(int x:a){for(int b=2;b>=0;--b)if((x>>b)&1){if(basis[b])x^=basis[b];else{basis[b]=x;++r;break;}}}
 return r;
}
int main(){
 vector<array<int,8>> maps;
 for(int a=1;a<8;a++)for(int b=1;b<8;b++)for(int c=1;c<8;c++) {
  if(rank2({a,b,c})!=3)continue;
  array<int,8> m={};for(int v=0;v<8;v++)m[v]=((v&1)?a:0)^((v&2)?b:0)^((v&4)?c:0);
  maps.push_back(m);
 }
 assert(maps.size()==168);
 vector<pair<int,int>> cells;for(int x=1;x<=7;x++)for(int y=1;y<=7;y++)cells.push_back({x,y});
 long counts[4]={1,0,0,0};
 for(int k=1;k<=3;k++){
  int tested=0, good=0;
  vector<int> ids(k);
  auto recurse=[&](auto&& self,int begin,int depth)->void {
   if(depth<k){for(int i=begin;i<=49-(k-depth);i++){ids[depth]=i;self(self,i+1,depth+1);}return;}
   tested++;
   vector<int> src,dst;for(int id:ids){src.push_back(cells[id].first);dst.push_back(cells[id].second);}
   bool expected=rank2(src)==k && rank2(dst)==k;
   unsigned int traces=0;
   for(const auto&m:maps){int tr=0;for(int j=0;j<k;j++)if(m[src[j]]==dst[j])tr|=1<<j;traces|=1u<<tr;}
   bool actual=traces==((1u<<(1u<<k))-1);
   if(actual!=expected){cerr<<"Failed for k="<<k<<" at ids ";for(int id:ids)cerr<<id<<',';cerr<<"\n";exit(1);}
   good+=actual;
  };
  recurse(recurse,0,0);counts[k]=good;
  cout<<"k="<<k<<" tested="<<tested<<" shattered="<<good<<"\n";
 }
 assert(counts[1]==49 && counts[2]==882 && counts[3]==4704);
 cout<<"GL3_SHATTER_PASS\n";
}
