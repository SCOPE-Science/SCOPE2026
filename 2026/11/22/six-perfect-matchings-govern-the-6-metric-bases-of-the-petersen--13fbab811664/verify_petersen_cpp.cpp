// Independent integer exhaustive checker, using the original Petersen edge list.
// Compile: g++ -std=c++17 -O2 verify_petersen_cpp.cpp -o verify_cpp && ./verify_cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <set>
#include <vector>
using namespace std;
const vector<pair<int,int>> EDGES = {{0,1},{0,4},{0,5},{1,2},{1,6},{2,3},{2,7},{3,4},{3,8},{4,9},{5,7},{5,8},{6,8},{6,9},{7,9}};
int main(){
 const int n=15;
 vector<vector<int>> a(n),d(n,vector<int>(n,-1));
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
  auto x=EDGES[i],y=EDGES[j];
  if(x.first==y.first||x.first==y.second||x.second==y.first||x.second==y.second){a[i].push_back(j);a[j].push_back(i);}
 }
 for(int i=0;i<n;i++){
  assert(a[i].size()==4);
  queue<int> Q;Q.push(i);d[i][i]=0;
  while(!Q.empty()){
   int x=Q.front();Q.pop();for(int y:a[x])if(d[i][y]==-1){d[i][y]=d[i][x]+1;Q.push(y);}
  }
 }
 vector<unsigned> E;
 for(int u=0;u<n;u++)for(int v=u+1;v<n;v++){
  unsigned b=0;for(int w=0;w<n;w++)if(d[u][w]==d[v][w])b|=1u<<w;
  E.push_back(b);
 }
 assert(E.size()==105);
 set<unsigned> unique(E.begin(),E.end());assert(unique.size()==105);
 for(unsigned e:E)assert(__builtin_popcount(e)==5);
 array<int,11> opt,ct;opt.fill(n+1);ct.fill(0);
 vector<unsigned> six;
 for(unsigned s=0;s<(1u<<n);s++){
  int level=n;
  for(unsigned e:E){level=min(level,__builtin_popcount(s)-__builtin_popcount(s&e));if(level==0)break;}
  int r=__builtin_popcount(s);
  for(int k=1;k<=level;k++){
   if(r<opt[k]){opt[k]=r;ct[k]=1;if(k==6){six.clear();six.push_back(s);}}
   else if(r==opt[k]){ct[k]++;if(k==6)six.push_back(s);}
  }
 }
 array<int,11> want_size={16,4,5,7,8,9,10,12,13,14,15};
 array<int,11> want_count={0,960,408,3480,1815,375,6,455,105,15,1};
 assert(opt==want_size);assert(ct==want_count);
 set<unsigned> fullmatch;
 for(unsigned m=0;m<(1u<<n);m++)if(__builtin_popcount(m)==5){
  int used=0;bool valid=true;
  for(int i=0;i<n;i++)if((m>>i)&1){auto [u,v]=EDGES[i];if(used&(1<<u|1<<v)){valid=false;break;}used|=1<<u|1<<v;}
  if(valid && used==1023)fullmatch.insert(m);
 }
 assert(fullmatch.size()==6);
 set<unsigned> optimal_complement;for(unsigned s:six)optimal_complement.insert(((1u<<n)-1)^s);
 assert(fullmatch==optimal_complement);
 for(int k=1;k<=10;k++)cout<<k<<" "<<opt[k]<<" "<<ct[k]<<"\n";
 cout<<"PASS all 32768 masks and six perfect matchings\n";
}
