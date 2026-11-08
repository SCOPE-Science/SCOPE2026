#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using U=uint64_t;
U step(U state,int n) {
  U mask=(U(1)<<n)-1, a=state&mask, b=(state>>n)&mask;
  int na=__builtin_popcountll(a),nb=__builtin_popcountll(b),degree=n-1;
  U oa=0,ob=0;
  for(int i=0;i<n;i++){
    int ai=(a>>i)&1,bi=(b>>i)&1;
    int la=2*(nb-bi)-degree, rb=2*(na-ai)-degree;
    if(la>0 || (la==0&&ai)) oa|=U(1)<<i;
    if(rb>0 || (rb==0&&bi)) ob|=U(1)<<i;
  }
  return oa|(ob<<n);
}
U choose(int n,int k){if(k<0||k>n)return 0;U x=1;for(int i=1;i<=k;i++)x=x*(n-k+i)/i;return x;}
std::array<std::array<U,3>,4> prediction(int n){
  std::array<std::array<U,3>,4> v{};
  if(n%2==0){
    U c=choose(n,n/2), low=((U(1)<<n)-c)/2;
    v[0][1]=2+c;
    v[0][2]=(c+2)*(c+1);
    v[1][1]=2*low*low-2;
    v[1][2]=(U(1)<<(2*n))-v[0][1]-v[0][2]-v[1][1];
  }else{
    int k=(n-1)/2; U c=choose(n,k), low=0;
    for(int j=0;j<k;j++)low+=choose(n,j);
    U M=n*choose(n-1,k);
    U h=low-(k+2)*(U(1)<<k)+1+(k+1)*(k+1);
    U theta=c*(c-1-k*(k+1));
    v[0][1]=2+2*M+2*c;
    v[0][2]=2;
    v[1][2]=2*low*low-2;
    v[2][2]=4*c*h+2*theta;
    v[1][1]=2*low*low-2+4*c*((U(1)<<k)-1)+2*c+2*c*k*(k+1);
    v[3][1]=4*c*(k+1)*((U(1)<<k)-k-1);
    v[2][1]=(U(1)<<(2*n))-v[0][1]-v[0][2]-v[1][1]-v[1][2]-v[2][2]-v[3][1];
  }
  return v;
}
int main(){
  for(int n=3;n<=10;n++) {
    auto expected=prediction(n); std::array<std::array<U,3>,4> got{};
    U total=U(1)<<(2*n);
    for(U s=0;s<total;s++) {
      U orbit[6]; orbit[0]=s;
      for(int j=1;j<6;j++)orbit[j]=step(orbit[j-1],n);
      bool found=false;
      for(int t=0;t<=3;t++)if(orbit[t]==orbit[t+2]) {
        int p=(orbit[t]==orbit[t+1])?1:2;
        got[t][p]++;found=true;break;
      }
      if(!found){std::cerr<<"no entry: "<<n<<" "<<s<<"\n";return 1;}
    }
    if(got!=expected){std::cerr<<"Mismatch at n="<<n<<"\n";return 2;}
    std::cout<<"n="<<n<<" ";
    for(int t=0;t<=3;t++)std::cout<<"t"<<t<<"p1="<<got[t][1]<<",p2="<<got[t][2]<<" ";
    std::cout<<"TOTAL="<<total<<" OK\n";
  }
  return 0;
}
