// Independent exhaustive verifier: adjacency lists + sequential propagation.
// Build: c++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp
#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <cassert>
using namespace std;
using Mask=unsigned int;
const int N=16;
const Mask ALL=(1u<<N)-1u;
int id(int x,int y) {return ((x%4+4)%4)*4+(y%4+4)%4;}
int main() {
 vector<array<int,6>> nb(N);
 const int ds[6][2]={{1,0},{-1,0},{0,1},{0,-1},{1,1},{-1,-1}};
 for(int i=0;i<N;i++) for(int j=0;j<6;j++)
   nb[i][j]=id(i/4+ds[j][0],i%4+ds[j][1]);
 auto dominated=[&](Mask S)->bool {
   bool watched[N]={};
   for(int i=0;i<N;i++) if(S&(1u<<i)){
      watched[i]=true;
      for(int j:nb[i])watched[j]=true;
   }
   bool progress=true;
   while(progress){
      progress=false;
      for(int i=0;i<N;i++) if(watched[i]){
        int last=-1,count=0;
        for(int j:nb[i])if(!watched[j]){last=j;++count;}
        if(count==1){watched[last]=true;progress=true;break;}
      }
   }
   return all_of(watched,watched+N,[](bool b){return b;});
 };
 vector<Mask> facets;
 // Enumerate all triangles without relying on a precomputed triangle count.
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)for(int k=j+1;k<N;k++){
   auto adjacent=[&](int a,int b){return find(nb[a].begin(),nb[a].end(),b)!=nb[a].end();};
   if(adjacent(i,j)&&adjacent(j,k)&&adjacent(i,k))
     facets.push_back((1u<<i)|(1u<<j)|(1u<<k));
 }
 assert(facets.size()==32);
 // Four-element cosets along the three generator directions.
 for(int i=0;i<N;i++)for(int dir=0;dir<3;dir++){
   Mask line=0;
   for(int t=0;t<4;t++)line|=1u<<id(i/4+t*ds[dir*2][0],i%4+t*ds[dir*2][1]);
   facets.push_back(line);
 }
 sort(facets.begin(),facets.end());
 facets.erase(unique(facets.begin(),facets.end()),facets.end());
 assert(facets.size()==44);
 array<int,17> failed{}, minimum{};
 vector<bool> works(1u<<N);
 for(Mask s=0;s<=ALL;s++){
    works[s]=dominated(s);
    bool expected_bad=false;
    for(Mask f:facets)if((s&f)==s){expected_bad=true;break;}
    if(works[s]==expected_bad){cerr<<"counterexample "<<s<<"\n";return 1;}
    if(!works[s])failed[__builtin_popcount(s)]++;
 }
 for(Mask s=0;s<=ALL;s++)if(works[s]){
   bool minimal=true;
   for(int i=0;i<N;i++)if((s&(1u<<i)) && works[s^(1u<<i)]){minimal=false;break;}
   if(minimal)minimum[__builtin_popcount(s)]++;
 }
 assert((failed[0]==1 && failed[1]==16 && failed[2]==72 && failed[3]==80 && failed[4]==12));
 for(int i=5;i<=16;i++)assert(failed[i]==0);
 assert(minimum[2]==48 && minimum[3]==16);
 for(int i=0;i<=16;i++)if(i!=2 && i!=3)assert(minimum[i]==0);
 cout<<"PASS C++: all 65536 subsets, 44 maximal obstructions, 181 failures, 48+16 minimal placements\n";
}
