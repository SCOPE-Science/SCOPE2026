#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <time.h>
#define P 2000000143LL
static int64_t D[48][6];
static uint64_t loops=0;
static int64_t power(int64_t a,int64_t n){int64_t b=1;for(;n;n>>=1,a=a*a%P)if(n&1)b=b*a%P;return b;}
static int det(const int inds[6]){
 int64_t a[6][6];
 for(int i=0;i<6;i++)for(int j=0;j<6;j++)a[i][j]=D[inds[j]][i];
 for(int k=0;k<6;k++){
   int piv=k;while(piv<6 && a[piv][k]==0)piv++;
   if(piv==6)return 0;
   if(piv!=k){for(int j=k;j<6;j++){int64_t tmp=a[piv][j];a[piv][j]=a[k][j];a[k][j]=tmp;}}
   if(k==5)break;
   int64_t t=a[k][k];
   for(int i=k+1;i<6;i++){
     int64_t c=a[i][k];
     for(int j=k+1;j<6;j++){
       a[i][j]=(t*a[i][j]-c*a[k][j])%P;
       if(a[i][j]<0)a[i][j]+=P;
     }
     a[i][k]=0;
   }
 }
 return 1;
}
static int isprime(int64_t n){if(n<2)return 0;for(int64_t k=2;k*k<=n;k++)if(n%k==0)return 0;return 1;}
int main(void){
 if(!isprime(P)){puts("NONPRIME MODULUS");return 2;}
 int ex[7]={0,1,1,0,1,0,0};

 int64_t z=power(3,(P-1)/7),eta=power(3,(P-1)/3);
 if(z==1 || eta==1 || power(z,7)!=1 || power(eta,3)!=1){puts("WRONG ROOTS");return 2;}
 int64_t zp[7],ep[3],g[7],invg[7];
 zp[0]=1;for(int i=1;i<7;i++)zp[i]=zp[i-1]*z%P;
 ep[0]=1;for(int i=1;i<3;i++)ep[i]=ep[i-1]*eta%P;
 for(int i=0;i<7;i++)g[i]=ep[ex[i]%3],invg[i]=power(g[i],P-2);
 for(int col=1;col<49;col++){
   int time=col/7, freq=col%7;
   int64_t v0=g[(7-time)%7];
   for(int x=1;x<7;x++){
     int64_t m=zp[(freq*x)%7]*g[(x-time+7)%7]%P;
     int64_t val=m*invg[x]%P;
     D[col-1][x-1]=(val-v0*invg[0]%P+P)%P;
   }
 }
 int idx[6]={0,1,2,3,4,5};
 while(1){
   loops++;
   if(!det(idx)){
      printf("FAIL: at %llu, 0",(unsigned long long)loops);
      for(int j=0;j<6;j++)printf(" %d",idx[j]+1);
      printf("\n");return 1;
   }
   int j=5;while(j>=0 && idx[j]==48-6+j)j--;
   if(j<0)break;
   idx[j]++;for(int k=j+1;k<6;k++)idx[k]=idx[k-1]+1;
 }
 printf("SUCCESS all %llu reduced minors nonzero, p=%lld z=%lld eta=%lld\n",(unsigned long long)loops,P,(long long)z,(long long)eta);
}
