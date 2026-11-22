// Exact quaternary projective-plane power-domination and exchange census.
// An affine construction and a frontier-based boolean simulation.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_set>
#include <vector>
using namespace std;
using U=uint64_t;
int mul(int a,int b){static const int T[4][4]={{0,0,0,0},{0,1,2,3},{0,2,3,1},{0,3,1,2}};return T[a][b];}
struct Graph {
 array<array<unsigned char,42>,42> edge{};
 Graph(){
  // affine points (x,y) indexed 4x+y; infinity slopes m =16+m, vertical =20.
  // affine lines y=mx+b indexed 21+4m+b, vertical x=c indexed 37+c, infinity=41.
  for(int m=0;m<4;m++)for(int b=0;b<4;b++){
   int ell=21+4*m+b;
   for(int x=0;x<4;x++){int y=mul(m,x)^b;add(4*x+y,ell);}
   add(16+m,ell);
  }
  for(int x=0;x<4;x++){int ell=37+x;for(int y=0;y<4;y++)add(4*x+y,ell);add(20,ell);}
  for(int p=16;p<=20;p++)add(p,41);
  for(int i=0;i<42;i++){int d=0;for(int j=0;j<42;j++)d+=edge[i][j];assert(d==5);}
 }
 void add(int i,int j){edge[i][j]=edge[j][i]=1;}
 int process(U chosen) const {
  array<unsigned char,42> alive{};
  for(int i=0;i<42;i++)if(chosen>>i&1){alive[i]=1;for(int j=0;j<42;j++)if(edge[i][j])alive[j]=1;}
  int step=1;
  while(true){int left=0;for(int j=0;j<42;j++)left+=!alive[j];if(!left)return step;
   array<unsigned char,42> next=alive;
   for(int i=0;i<42;i++)if(alive[i]){
    int last=-1,ct=0;
    for(int j=0;j<42;j++)if(edge[i][j]&&!alive[j]){last=j;if(++ct>=2)break;}
    if(ct==1)next[last]=1;
   }
   if(next==alive)return 0;
   alive=next;step++;
  }
 }
};
int main(){Graph G;vector<U> good;array<array<unsigned long long,6>,7> count{};unsigned long long bad5=0;
 auto gen=[&](auto&&self,int from,int left,U mask,int goal)->void{
  if(!left){int t=G.process(mask);if(goal==5){if(t)bad5++;}else if(t){int a=__builtin_popcountll(mask&((U(1)<<21)-1));assert(a>=0&&a<=6&&t<6);count[a][t]++;good.push_back(mask);}return;}
  for(int j=from;j<=42-left;j++)self(self,j+1,left-1,mask|(U(1)<<j),goal);
 };
 gen(gen,0,5,0,5);gen(gen,0,6,0,6);
 cout<<"bad5_success="<<bad5<<" opt="<<good.size()<<"\n";
 for(int a=0;a<=6;a++)for(int t=1;t<6;t++)if(count[a][t])cout<<"profile="<<a<<","<<t<<","<<count[a][t]<<"\n";
 unordered_set<U> found(good.begin(),good.end());
 // Each edge counted twice; an independent flood-fill establishes connectivity.
 vector<U> frontier{good.front()};unordered_set<U> seen;seen.insert(good.front());unsigned long long degree_sum=0;
 for(size_t idx=0;idx<frontier.size();idx++){
  U S=frontier[idx];
  for(int v=0;v<42;v++)if((S>>v)&1)for(int w=0;w<42;w++)if(!((S>>w)&1)){
    U T=S^(U(1)<<v)^(U(1)<<w);
    if(found.count(T)){
      degree_sum++;
      if(seen.insert(T).second)frontier.push_back(T);
    }
  }
 }
 cout<<"reachable="<<seen.size()<<" exchange_edges="<<degree_sum/2<<"\n";
 // Independent token-slide component traversal (not the token-jump traversal above).
 unordered_set<U> processed; vector<size_t> components; unsigned long long slide_degree_sum=0, frozen_fast=0, frozen_slow=0;
 for(U start: good){if(processed.count(start))continue;
  vector<U> queue{start};processed.insert(start);
  for(size_t z=0;z<queue.size();z++){
   U S=queue[z];int degree=0;
   for(int v=0;v<42;v++)if((S>>v)&1)for(int w=0;w<42;w++)if(G.edge[v][w]&&!((S>>w)&1)){
    U T=S^(U(1)<<v)^(U(1)<<w);
    if(!found.count(T))continue;
    degree++;slide_degree_sum++;
    if(processed.insert(T).second)queue.push_back(T);
   }
   if(degree==0){int t=G.process(S);if(t==2)frozen_fast++;else if(t==3)frozen_slow++;else assert(false);}
  }
  components.push_back(queue.size());
 }
 sort(components.begin(),components.end());
 cout<<"slide_components="<<components.size()<<" slide_edges="<<slide_degree_sum/2<<" slide_largest="<<components.back()<<" frozen_fast="<<frozen_fast<<" frozen_slow="<<frozen_slow<<"\n";

 assert(bad5==0 && good.size()==566160 && count[2][3]==65520 && count[3][2]==52080 && count[3][3]==383040 && count[4][3]==65520 && seen.size()==good.size() && degree_sum/2==19706400 && slide_degree_sum/2==2257920 && components.size()==30241 && components.back()==535920 && frozen_fast==10080 && frozen_slow==20160);
 cout<<"PASS\n";
}
