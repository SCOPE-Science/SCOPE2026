// Exact 3-colour Potts ground-state census by disjoint colour-class subsets.
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;
using u32 = uint32_t;
struct Model {array<u32,16> adj{};};
Model make_graph(int type) {
 Model g;
 for(int a=0;a<16;a++)for(int b=a+1;b<16;b++){
  int x=a/4,y=a%4,u=b/4,v=b%4;
  int dx=(u-x+4)%4,dy=(v-y+4)%4;
  bool edge=type==0 ? (x==u || y==v) :
    ((dx==1 && dy==0)||(dx==3 && dy==0)||(dx==0 && dy==1)||(dx==0 && dy==3)||(dx==1 && dy==1)||(dx==3 && dy==3));
  if(edge){g.adj[a]|=1u<<b;g.adj[b]|=1u<<a;}
 }
 return g;
}
int main(){
 for(int which=0;which<2;which++){
  auto g=make_graph(which);
  for(int i=0;i<16;i++){
   if(popcount(g.adj[i])!=6)return 1;
   for(int j=i+1;j<16;j++)if(popcount(g.adj[i]&g.adj[j])!=2)return 2;
  }
  const u32 full=(1u<<16)-1;
  vector<uint8_t> e(1u<<16,0);
  for(u32 m=1;m<=full;m++){
   int v=countr_zero(m);
   u32 rest=m&(m-1);
   e[m]=e[rest]+popcount(g.adj[v]&rest);
  }
  array<int,17> mins; mins.fill(1000);
  array<uint64_t,17> counts{};
  uint64_t assignments=0;
  for(u32 s=0;s<=full;s++){
   int k=popcount(s);u32 rem=full^s;
   for(u32 t=rem;; t=(t-1)&rem){
    u32 r=rem^t;
    int eng=e[s]+e[t]+e[r];
    if(eng<mins[k]){mins[k]=eng;counts[k]=1;}
    else if(eng==mins[k])counts[k]++;
    assignments++;
    if(t==0)break;
   }
  }
  if(assignments!=43046721u)return 3;
  cout<<(which==0?"rook":"shrikhande")<<"\n";
  for(int k=0;k<=16;k++)cout<<k<<" "<<mins[k]<<" "<<counts[k]<<"\n";
 }
}
