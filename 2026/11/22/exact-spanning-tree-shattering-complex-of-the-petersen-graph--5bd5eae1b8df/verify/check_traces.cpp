// Independent exhaustive trace test, starting from actual spanning trees.
// Compiles with: c++ -std=c++17 -O2 -o check_traces check_traces.cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<array<int,2>> v;
 for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)v.push_back({i,j});
 vector<array<int,2>> e;
 for(int a=0;a<10;a++)for(int b=a+1;b<10;b++){
  bool disjoint=true;
  for(int x:v[a])for(int y:v[b])if(x==y)disjoint=false;
  if(disjoint)e.push_back({a,b});
 }
 if(e.size()!=15)abort();
 auto tree=[&](int s){
  int p[10];iota(p,p+10,0);
  auto root=[&](int a){while(p[a]!=a)a=p[a];return a;};
  int count=0;
  for(int i=0;i<15;i++)if(s>>i&1){
   int a=root(e[i][0]),b=root(e[i][1]);
   if(a==b)return false;
   p[a]=b;count++;
  }
  if(count!=9)return false;
  int r=root(0);
  for(int i=1;i<10;i++)if(root(i)!=r)return false;
  return true;
 };
 vector<int> trees;
 for(int s=0;s<(1<<15);s++)if(tree(s))trees.push_back(s);
 if(trees.size()!=2000){cerr<<"tree-count";return 1;}
 vector<int> ok(1<<15,0),poly(16,0);
 vector<int> seen(1<<15,-1);
 for(int s=0;s<(1<<15);s++){
  int cnt=0;
  for(int t:trees){
   int q=s&t;
   if(seen[q]!=s){seen[q]=s;cnt++;}
  }
  if(cnt==(1<<__builtin_popcount((unsigned)s))){ok[s]=1;poly[__builtin_popcount((unsigned)s)]++;}
 }
 vector<int> expected={1,15,105,445,1230,2160,1930};
 for(int i=0;i<16;i++)if(poly[i]!=(i<(int)expected.size()?expected[i]:0)){
  cerr<<"poly mismatch "<<i<<" "<<poly[i]<<'\n';return 2;
 }
 vector<int> fs;
 for(int s=0;s<(1<<15);s++)if(ok[s]){
  bool maximal=true;
  for(int i=0;i<15;i++)if(!(s>>i&1)&&ok[s|(1<<i)])maximal=false;
  if(maximal)fs.push_back(s);
 }
 if(fs.size()!=1930) return 3;
 for(int s:fs)if(__builtin_popcount((unsigned)s)!=6)return 4;
 cout<<"PETERSEN_TRACES_PASS trees="<<trees.size()<<" faces=5886 facets="<<fs.size()<<"\n";
}
