// Independent subset DP verifier of fixed finite ground state counts.
#include <cstdint>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
 // Build the 27 line classes without input files: E_i, L_{ij}, C_i.
 struct Vertex {int type;int i;int j;};vector<Vertex> verts;
 for(int i=0;i<6;i++)verts.push_back({0,i,-1});
 for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)verts.push_back({1,i,j});
 for(int i=0;i<6;i++)verts.push_back({2,i,-1});
 auto meet=[](Vertex a,Vertex b){
  if(a.type>b.type)swap(a,b);
  if(a.type==0 && b.type==0)return false;
  if(a.type==0 && b.type==1)return a.i==b.i || a.i==b.j;
  if(a.type==0 && b.type==2)return a.i!=b.i;
  if(a.type==1 && b.type==1)return a.i!=b.i && a.i!=b.j && a.j!=b.i && a.j!=b.j;
  if(a.type==1 && b.type==2)return b.i==a.i || b.i==a.j;
  return false;
 };
 uint32_t adj[27]={0};int numedges=0;
 for(int i=0;i<27;i++)for(int j=i+1;j<27;j++)if(!meet(verts[i],verts[j])){adj[i]|=1u<<j;adj[j]|=1u<<i;numedges++;}
 if(numedges!=216) return 1;
 const uint32_t B=1u<<27;
 vector<uint8_t> ee(B,0);
 int best[28];uint64_t count[28]={};fill(best,best+28,-1);
 for(uint32_t s=0;s<B;s++){
  if(s){int v=__builtin_ctz(s);uint32_t rem=s&(s-1);ee[s]=(uint8_t)(ee[rem]+__builtin_popcount(adj[v]&rem));}
  int k=__builtin_popcount(s),cut=16*k-2*ee[s];
  if(cut>best[k]){best[k]=cut;count[k]=1;}
  else if(cut==best[k])count[k]++;
 }
 for(int k=0;k<=27;k++)printf("%d %d %llu\n",k,best[k],(unsigned long long)count[k]);
}
