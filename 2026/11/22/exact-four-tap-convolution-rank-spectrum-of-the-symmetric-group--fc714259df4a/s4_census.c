/* Exact rank census of four-shift regular convolution on the permutation group S_4. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#define N 24
#define P 1000000007LL
static int G[N][4], mult[N][N],inv[N];
static int same(const int*a,const int*b){for(int i=0;i<4;i++)if(a[i]!=b[i])return 0;return 1;}
static int number(const int*a){for(int i=0;i<N;i++)if(same(a,G[i]))return i;abort();}
static long long power(long long a,long long b){long long r=1;while(b){if(b&1)r=r*a%P;a=a*a%P;b>>=1;}return r;}
static int rank4(int s0,int s1,int s2,int s3){
 static long long a[N][N]; int s[4]={s0,s1,s2,s3};
 memset(a,0,sizeof(a));for(int i=0;i<N;i++)for(int j=0;j<4;j++)a[i][mult[s[j]][i]]=1;
 int r=0;for(int c=0;c<N;c++){
   int t=r;while(t<N&&a[t][c]==0)t++;if(t==N)continue;
   if(t!=r)for(int j=c;j<N;j++){long long x=a[t][j];a[t][j]=a[r][j];a[r][j]=x;}
   long long iv=power(a[r][c],P-2);
   for(int i=r+1;i<N;i++)if(a[i][c]){
      long long q=a[i][c]*iv%P;a[i][c]=0;
      for(int j=c+1;j<N;j++){long long x=a[i][j]-q*a[r][j]%P;if(x<0)x+=P;a[i][j]=x;}
   }
   r++;
 }return r;
}
static int subgroup(int*a){int vis[N]={0},list[N],n=0;vis[0]=1;list[n++]=0;
 for(int k=0;k<n;k++)for(int j=0;j<3;j++){
  int v=mult[list[k]][a[j]]; if(!vis[v]){vis[v]=1;list[n++]=v;}
 }return n;
}
int main(){
 for(long long d=2;d*d<=P;d++)if(P%d==0)return 6; /* exact trial-division primality test */
 int ct=0;for(int a=0;a<4;a++)for(int b=0;b<4;b++)if(b!=a)for(int c=0;c<4;c++)if(c!=a&&c!=b)for(int d=0;d<4;d++)if(d!=a&&d!=b&&d!=c){G[ct][0]=a;G[ct][1]=b;G[ct][2]=c;G[ct][3]=d;ct++;}
 for(int i=0;i<N;i++)for(int j=0;j<N;j++){int z[4];for(int k=0;k<4;k++)z[k]=G[i][G[j][k]];mult[i][j]=number(z);}
 for(int i=0;i<N;i++){for(int j=0;j<N;j++)if(mult[i][j]==0){inv[i]=j;break;}}
 int freq[N+1]={0}, hfreq[25][25]={{0}}, examples[N+1][4];
 int a,b,c,d,total=0;
 for(a=0;a<N-3;a++)for(b=a+1;b<N-2;b++)for(c=b+1;c<N-1;c++)for(d=c+1;d<N;d++){
   int r=rank4(a,b,c,d);freq[r]++;
   if(freq[r]==1){examples[r][0]=a;examples[r][1]=b;examples[r][2]=c;examples[r][3]=d;}
   int norm[3]={mult[inv[a]][b],mult[inv[a]][c],mult[inv[a]][d]};int h=subgroup(norm);hfreq[h][r]++;total++;

 }
 printf("TOTAL %d\n",total);
 for(int i=0;i<=N;i++)if(freq[i])printf("RANK %d COUNT %d EXAMPLE %d,%d,%d,%d\n",i,freq[i],examples[i][0],examples[i][1],examples[i][2],examples[i][3]);
 for(int h=1;h<=N;h++)for(int r=0;r<=N;r++)if(hfreq[h][r])printf("GENERATED_ORDER %d RANK %d COUNT %d\n",h,r,hfreq[h][r]);
 int expected[N+1]={0}; expected[6]=42;expected[9]=144;expected[12]=576;expected[15]=1008;expected[18]=2856;expected[20]=1728;expected[21]=3024;expected[24]=1248;
 if(total!=10626)return 3;
 for(int r=0;r<=N;r++)if(freq[r]!=expected[r])return 4;
 int hc[25][25]={{0}};
 hc[4][6]=42;hc[6][12]=144;hc[6][24]=96;
 hc[8][9]=144;hc[8][15]=288;hc[8][21]=144;
 hc[12][12]=144;hc[12][18]=552;hc[12][24]=288;
 hc[24][12]=288;hc[24][15]=720;hc[24][18]=2304;hc[24][20]=1728;hc[24][21]=2880;hc[24][24]=864;
 for(int h=0;h<=N;h++)for(int r=0;r<=N;r++)if(hfreq[h][r]!=hc[h][r])return 5;
 return 0;}
