// Exact independent depth-first census on the canonical generalized Petersen graph GP(10,2).
// Spin variables label its 30 edges; no external libraries or data files are needed.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
using i64 = long long;
static int edge[30][2], nedge=0, degree[20]={}, assigned[20]={}, up[20]={};
static i64 hist[31]={};
static unsigned long long visited=0;
void add(int a,int b) {
  if(a<0||b<0||a>=20||b>=20||a==b||nedge>=30) std::abort();
  edge[nedge][0]=a;edge[nedge][1]=b; ++degree[a];++degree[b];++nedge;
}
void recurse(int e,int k){
  ++visited;
  if(e==30){++hist[k];return;}
  const int a=edge[e][0],b=edge[e][1];
  ++assigned[a];++assigned[b];
  for(int spin=0;spin<2;spin++){
    up[a]+=spin;up[b]+=spin;
    const bool impossible=(assigned[a]==3&&(up[a]==0||up[a]==3))
                       ||(assigned[b]==3&&(up[b]==0||up[b]==3));
    if(!impossible) recurse(e+1,k+spin);
    up[a]-=spin;up[b]-=spin;
  }
  --assigned[a];--assigned[b];
}
int main(){
  // u_i=i, v_i=10+i; subscripts are cyclic modulo ten.
  for(int i=0;i<10;i++){
    add(i,(i+1)%10);add(i,10+i);add(10+i,10+(i+2)%10);
  }
  if(nedge!=30)std::abort();
  for(int d:degree)if(d!=3)std::abort();
  recurse(0,0);
  constexpr i64 wanted[31]={
     0,0,0,0,0,0,0,0,0,0,
     36,3150,50265,287370,762390,1044828,
     762390,287370,50265,3150,36,
     0,0,0,0,0,0,0,0,0,0
  };
  i64 total=0;
  for(int k=0;k<=30;k++){
    if(hist[k]!=wanted[k]){
      std::fprintf(stderr,"wrong k=%d actual=%lld expected=%lld\n",k,hist[k],wanted[k]);return 1;
    }
    total+=hist[k];
  }
  if(total!=3251250) return 2;
  std::printf("VERIFY_DFS_OK zero_field=%lld visited=%llu\n",total,visited);
}
