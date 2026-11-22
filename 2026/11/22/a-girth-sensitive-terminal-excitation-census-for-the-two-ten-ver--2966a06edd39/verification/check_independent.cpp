// Standalone exact finite-state verifier. C++17, no external dependencies.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using S = std::array<unsigned char,10>;
std::vector<std::array<int,3>> neighbors(int k) {
 std::array<std::vector<int>,10> adj;
 auto edge=[&](int u,int v){adj[u].push_back(v);adj[v].push_back(u);};
 for(int i=0;i<5;i++){edge(i,(i+1)%5);edge(i,i+5);edge(i+5,5+(i+k)%5);}
 std::vector<std::array<int,3>> out;
 for(auto& x:adj){assert(x.size()==3);out.push_back({x[0],x[1],x[2]});}
 return out;
}
S update(const S& x,const std::vector<std::array<int,3>>& adj){
 S out{};
 for(int i=0;i<10;i++){
  if(x[i]==1) out[i]=2;
  else if(x[i]==2) out[i]=0;
  else {int cnt=0;for(int j:adj[i])cnt+=(x[j]==1);out[i]=(cnt>=2);}
 }
 return out;
}
bool rest(const S& x){for(auto b:x)if(b)return false;return true;}
int main(){
 for(int k:{1,2}){
  std::array<uint64_t,5> hist{};
  std::array<uint64_t,11> last_by_seed{};
  std::array<uint64_t,11> last_by_a2{};
  auto adj=neighbors(k);
  for(int code=0;code<59049;code++){
   int z=code,ones=0;
   S state{};
   for(int i=0;i<10;i++){state[i]=z%3;z/=3;ones+=(state[i]==1);}
   int hit=-1,a2=-1;
   for(int t=0;t<=4;t++){
    if(t==2){a2=0;for(int j=0;j<10;j++)a2+=(state[j]==1);}
    if(hit==-1&&rest(state))hit=t;
    if(t<4)state=update(state,adj);
   }
   assert(rest(state)&&hit>=0&&hit<=4);
   hist[hit]++;
   if(hit==4){last_by_seed[ones]++;last_by_a2[a2]++;assert(a2>0);}
  }
  if(k==1){
   assert((hist==std::array<uint64_t,5>{1,1023,25415,29230,3380}));
   assert((last_by_seed==std::array<uint64_t,11>{0,0,0,640,1240,1040,400,60,0,0,0}));
   assert((last_by_a2==std::array<uint64_t,11>{0,3340,40,0,0,0,0,0,0,0,0}));
  } else {
   assert((hist==std::array<uint64_t,5>{1,1023,25205,31300,1520}));
   assert((last_by_seed==std::array<uint64_t,11>{0,0,0,0,420,720,320,60,0,0,0}));
   assert((last_by_a2==std::array<uint64_t,11>{0,1460,60,0,0,0,0,0,0,0,0}));
  }
  std::cout<<"GP(5,"<<k<<") first-hit:";
  for(auto x:hist)std::cout<<" "<<x;
  std::cout<<"; t=4 by seed:";
  for(auto x:last_by_seed)std::cout<<" "<<x;
  std::cout<<"; A2 distribution:";
  for(auto x:last_by_a2)std::cout<<" "<<x;
  std::cout<<"\n";
 }
 std::cout<<"PASS exact full-state enumeration\n";
}
