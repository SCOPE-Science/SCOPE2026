#include <cstdint>
#include <cstdio>
#include <vector>
#include <cstdlib>
using namespace std;
int main(){
 for(int n: {3,8,15}){
  int M=1<<n;
  vector<int64_t> A(M);
  for(int S=0;S<M;S++){
   int p=1,T=1;
   for(int i=0;i<n;i++){if((S>>i)&1)p=-p; T+=p;}
   int64_t coeff=((int64_t)T*T-(n+1))/2;
   A[S]=coeff?1:0;
  }
  for(int d=1;d<M;d*=2)for(int i=0;i<M;i+=2*d)for(int j=i;j<i+d;j++){
   int64_t x=A[j],y=A[j+d];A[j]=x+y;A[j+d]=x-y;
  }
  int64_t sumabs=0;
  for(int i=0;i<M;i++)sumabs+=llabs(A[i]);
  // Values are numerator over M, reduce by powers of two
  int64_t g=1;
  while(sumabs%(2*g)==0 && M%(2*g)==0)g*=2;
  printf("n=%d endpoint norm=%lld/%lld\n",n,(long long)(sumabs/g),(long long)(M/g));
  if(n==3 && sumabs!=M*1LL)return 1;
  if(n==8 && sumabs!=M*25LL/4)return 1;
  if(n==15 && sumabs!=M*131177LL/2048)return 1;
 }
 puts("PASS direct inverse Walsh projection kernel and sharp norm checks");
}
