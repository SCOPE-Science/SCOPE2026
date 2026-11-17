// Exhaustively enumerate the ternary reversible wave on the 3-sunlet.
// All values modulo 3. This is a direct vertex-level check.
#include <iostream>
#include <array>
#include <cstdint>
using namespace std;
int main(){
  constexpr int n=3,N=2*n,D=2*N;
  constexpr int total=531441; // 3^(4*n)
  uint64_t c1=0,c5=0,c15=0,other=0;
  for(int code=0;code<total;code++){
    array<int,D> init{},cur{},nxt{};
    int x=code;
    for(int j=0;j<D;j++){init[j]=x%3;x/=3;}
    cur=init;
    int p=0;
    do {
      for(int i=0;i<n;i++){
        nxt[i]=(cur[(i+1)%n]+cur[(i+n-1)%n]+cur[n+i]+3-cur[N+i])%3;
        nxt[n+i]=(cur[i]+3-cur[N+n+i])%3;
      }
      for(int i=0;i<N;i++)nxt[N+i]=cur[i];
      cur=nxt;p++;
    }while(cur!=init && p<=15);
    if(cur!=init){cerr<<"failed return";return 2;}
    if(p==1)c1++;else if(p==5)c5++;else if(p==15)c15++;else other++;
  }
  cout<<"n=3 q=3 states="<<total<<" primitive_1="<<c1
    <<" primitive_5="<<c5<<" primitive_15="<<c15<<" other="<<other<<"\n";
  if(c1!=1 || c5!=6560 || c15!=524880 || other)return 1;
  return 0;
}
