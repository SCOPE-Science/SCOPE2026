#include <iostream>
#include <array>
using namespace std;
int Q,A;
int norm(int x){x%=Q;return x<0?x+Q:x;}
int rank3(const int M[3][3]) {int T[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++)T[i][j]=M[i][j];int r=0;for(int j=0;j<3;j++){int k=r;while(k<3&&T[k][j]==0)++k;if(k==3)continue;for(int t=0;t<3;t++)swap(T[k][t],T[r][t]);int inv=1;while(norm(inv*T[r][j])!=1)++inv;for(int t=j;t<3;t++)T[r][t]=norm(T[r][t]*inv);for(int i=r+1;i<3;i++){int f=T[i][j];for(int t=j;t<3;t++)T[i][t]=norm(T[i][t]-f*T[r][t]);}r++;if(r==3)break;}return r;}
bool valid(const int M[3][3]) {for(int i=0;i<3;i++)for(int j=0;j<3;j++){
 int left=norm(M[0][i]*M[1][j]+A*M[1][i]*M[0][j]);
 int c1=norm((j==1?M[0][i]:0)+ (j==0?A*M[1][i]:0));
 int c2=norm((i==0?M[1][j]:0)+ (i==1?A*M[0][j]:0));
 for(int t=0;t<3;t++) {int expect=(t==2?left:0);if(expect!=norm(c1*M[t][2]) ||expect!=norm(c2*M[t][2]))return false;}
 }return true;}
int main(){for(int q : {5,7}){Q=q;A=2;long long n=1;for(int i=0;i<9;i++)n*=Q;long long counts[4]={};for(long long z=0;z<n;z++){long long x=z;int M[3][3];for(int i=0;i<3;i++)for(int j=0;j<3;j++){M[i][j]=x%Q;x/=Q;}
 bool id=true;for(int i=0;i<3&&id;i++)for(int j=0;j<3;j++){int sum=0;for(int k=0;k<3;k++)sum+=M[i][k]*M[k][j];if(norm(sum)!=M[i][j]){id=false;break;}}if(!id || !valid(M))continue;counts[rank3(M)]++;}
 cout<<"q="<<Q<<" counts="<<counts[0]<<","<<counts[1]<<","<<counts[2]<<","<<counts[3]<<"\n";
 if(counts[0]!=1||counts[1]!=3LL*Q*Q||counts[2]!=0||counts[3]!=1)return 1;}
 cout<<"DIRECT_IDEMPOTENT_AVERAGING_EXHAUSTIVE_VERIFIED\n";
}
