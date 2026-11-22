/* Exact cyclotomic-zero certificates for all 64 normalized sign words.
   A zero of a 7x7 determinant at all six primitive seventh roots modulo
   P, where P > 2*7!, proves the corresponding complex determinant is zero. */
#include <stdint.h>
#include <stdio.h>
#define P 2000000143LL
static int64_t D[48][6];
static int64_t power(int64_t a,int64_t n){int64_t b=1;for(;n;n>>=1,a=a*a%P)if(n&1)b=b*a%P;return b;}
static int64_t residue(int64_t x){x%=P;return x<0?x+P:x;}
static int isprime(int64_t n){if(n<2)return 0;for(int64_t k=2;k*k<=n;k++)if(n%k==0)return 0;return 1;}
static void build(int mask,int root_power){
 int64_t root=power(power(3,(P-1)/7),root_power);
 int64_t zp[7],g[7];zp[0]=1;g[0]=1;
 for(int i=1;i<7;i++){zp[i]=zp[i-1]*root%P;g[i]=(mask>>(i-1))&1 ? P-1 : 1;}
 for(int col=1;col<49;col++){
  int t=col/7,b=col%7;
  int64_t r0=g[(7-t)%7];
  for(int x=1;x<7;x++){
   int64_t m=zp[(b*x)%7]*g[(x-t+7)%7]%P;
   D[col-1][x-1]=residue(m*g[x]%P-r0);
  }
 }
}
static int full_rank(int inds[6]){
 int64_t a[6][6];
 for(int i=0;i<6;i++)for(int j=0;j<6;j++)a[i][j]=D[inds[j]][i];
 for(int k=0;k<6;k++){
  int pi=k;while(pi<6 && a[pi][k]==0)pi++;
  if(pi==6)return 0;
  for(int j=k;j<6;j++){int64_t s=a[k][j];a[k][j]=a[pi][j];a[pi][j]=s;}
  int64_t v=a[k][k];
  for(int i=k+1;i<6;i++){
   int64_t w=a[i][k];
   for(int j=k+1;j<6;j++)a[i][j]=residue(v*a[i][j]-w*a[k][j]);
   a[i][k]=0;
  }
 }
 return 1;
}
static int checked_zero(int mask,int inds[6]){
 for(int j=1;j<=6;j++){
  build(mask,j);
  if(full_rank(inds))return 0;
 }
 return 1;
}
int main(void){
 if(!isprime(P)||P<=10080){fprintf(stderr,"bad prime\n");return 2;}
 int64_t z=power(3,(P-1)/7);
 if(z==1||power(z,7)!=1){fprintf(stderr,"bad root\n");return 2;}
 puts("mask,c0,c1,c2,c3,c4,c5,c6");
 for(int mask=0;mask<64;mask++){
  build(mask,1);
  int ids[6]={0,1,2,3,4,5};
  for(;;){
   if(!full_rank(ids) && checked_zero(mask,ids))break;
   build(mask,1);
   int j=5;while(j>=0 && ids[j]==48-6+j)j--;
   if(j<0){fprintf(stderr,"no certificate for %d\n",mask);return 1;}
   ids[j]++;for(int v=j+1;v<6;v++)ids[v]=ids[v-1]+1;
  }
  printf("%d,0",mask);
  for(int i=0;i<6;i++)printf(",%d",ids[i]+1);
  putchar('\n');
 }
 return 0;
}
