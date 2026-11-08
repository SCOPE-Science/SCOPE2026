// Separate depth-first transfer enumeration using an independently entered 36-edge list.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <utility>
using namespace std;
constexpr pair<int,int> edges[36] = {
  {0,1},{0,12},{0,23},{1,2},{1,8},{2,3},{2,19},{3,4},{3,15},
  {4,5},{4,11},{5,6},{5,22},{6,7},{6,18},{7,8},{7,14},
  {8,9},{9,10},{9,21},{10,11},{10,17},{11,12},{12,13},
  {13,14},{13,20},{14,15},{15,16},{16,17},{16,23},
  {17,18},{18,19},{19,20},{20,21},{21,22},{22,23}
};
array<int,25> best;
array<uint64_t,25> ways{};
uint64_t hist31=0,m2_31=0,visited=0;
uint32_t lower_neighbors[24]{};
void visit(int v,uint32_t mask,int q,int cut){
  if(v==24){
    ++visited;
    if(cut>best[q]) best[q]=cut,ways[q]=1;
    else if(cut==best[q]) ++ways[q];
    if(cut==31){++hist31;int m=24-2*q;m2_31+=uint64_t(m*m);}
    return;
  }
  const int e=__builtin_popcount(lower_neighbors[v]);
  const int occupied=__builtin_popcount(lower_neighbors[v]&mask);
  // For new bit 0, cut edges are previously occupied bits.
  visit(v+1,mask,q,cut+occupied);
  // For new bit 1, cut edges are previously unoccupied bits.
  visit(v+1,mask|(1u<<v),q+1,cut+e-occupied);
}
int main(){
 best.fill(-1);
 int degree[24]={};
 for(auto [a,b]:edges) {
   assert(a<b && a>=0 && b<24);
   lower_neighbors[b]|=(1u<<a);
   ++degree[a];++degree[b];
 }
 for(int i=0;i<24;i++) assert(degree[i]==3);
 visit(0,0,0,0);
 assert(visited==(1ull<<24));
 const int expect_best[25]={0,3,6,9,12,15,18,21,24,27,30,31,32,31,30,27,24,21,18,15,12,9,6,3,0};
 const uint64_t expect_ways[25]={1,24,240,1304,4212,8328,10024,7072,2668,424,8,8,2,8,8,424,2668,7072,10024,8328,4212,1304,240,24,1};
 for(int q=0;q<=24;q++) assert(best[q]==expect_best[q] && ways[q]==expect_ways[q]);
 assert(hist31==16 && m2_31==64);
 cout<<"VERIFY_RECURSIVE_OK 16777216 leaves maxcut=32 ground=2 first_excited=16 q10=8 q11=8 q12=2\n";
}
