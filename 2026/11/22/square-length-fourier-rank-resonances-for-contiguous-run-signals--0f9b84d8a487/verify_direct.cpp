#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int main(int argc, char** argv){
  int nmax=argc>1?atoi(argv[1]):16;
  if(nmax<1||nmax>20) return 2;
  for(int n=1;n<=nmax;n++){
    int size=1<<n; vector<int64_t> F(size);
    for(int a=0;a<n;a++){
      unsigned mask=0;
      for(int b=a;b<n;b++){
        mask|=(1u<<b); if(F[mask]++) {fprintf(stderr,"duplicate interval\n"); return 1;}
      }
    }
    for(int step=1;step<size;step<<=1)
      for(int i=0;i<size;i+=2*step) for(int j=i;j<i+step;j++){
        int64_t x=F[j],y=F[j+step];F[j]=x+y;F[j+step]=x-y;
      }
    int64_t zeros=0, minabs=1ll<<60, mx=0;
    for(int S=0;S<size;S++){
      int sign=1, signedSum=1, j=0;
      for(int i=0;i<n;i++){
        if((S>>i)&1) sign=-sign;
        signedSum+=sign; j+=(sign<0);
      }
      int N=n+1;
      int64_t formula=((int64_t)signedSum*signedSum-N)/2;
      if(F[S]!=formula){fprintf(stderr,"n=%d S=%d FWHT=%lld formula=%lld\n",n,S,(long long)F[S],(long long)formula);return 1;}
      if(F[S]==0)zeros++;else minabs=min<int64_t>(minabs,llabs(F[S]));
      mx=max<int64_t>(mx,llabs(F[S]));
    }
    int s=sqrt(n+1);int64_t zformula=0;
    if(s*s==n+1){int j1=(s*s-s)/2; // Pascal count exact
      int64_t bin=1;for(int k=1;k<=j1;k++)bin=bin*(n+2-k)/k; // C(n+1,j1)
      zformula=bin;
    }
    if(zeros!=zformula){fprintf(stderr,"bad zeros n=%d: %lld vs %lld\n",n,(long long)zeros,(long long)zformula);return 1;}
    if(minabs<1||mx!=(int64_t)n*(n+1)/2){fprintf(stderr,"bad bound n=%d\n",n);return 1;}
    if(n==3||n==8||n==15||n==nmax)printf("n=%d, zero=%lld, rank=%d, min_nonzero=%lld, max=%lld\n",n,(long long)zeros,size-(int)zeros,(long long)minabs,(long long)mx);
  }
  printf("PASS direct enumeration, exact integer FWHT and analytic formula for n=1..%d\n",nmax);
}
