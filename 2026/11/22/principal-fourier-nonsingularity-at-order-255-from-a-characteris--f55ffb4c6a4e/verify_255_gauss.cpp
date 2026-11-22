// Independent Gaussian-elimination certificate for order-15 principal Fourier minors.
// Build: g++ -O3 -std=c++17 verify_255_gauss.cpp -o verify_255_gauss
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <utility>
using namespace std;
int p=17,q=83521,C1=0,C0=3;
inline int mul(int A,int B){int a[4],b[4];for(int i=0;i<4;i++){a[i]=A%p;b[i]=B%p;A/=p;B/=p;}int v[7]={};for(int i=0;i<4;i++)for(int j=0;j<4;j++)v[i+j]+=a[i]*b[j];for(int i=6;i>=4;i--){v[i-4]-=C0*v[i];v[i-3]-=C1*v[i];}int r=0,d=1;for(int i=0;i<4;i++){int x=(v[i]%p+p)%p;r+=d*x;d*=p;}return r;}
int powf(int x,int y){int r=1;while(y){if(y&1)r=mul(r,x);x=mul(x,x);y>>=1;}return r;}
int main(){int root=0;for(int x=2;x<q;x++){int y=powf(x,(q-1)/15);if(y!=1 && powf(y,15)==1 && powf(y,5)!=1 && powf(y,3)!=1){root=y;break;}}if(!root){cerr<<"no root";return 1;}cerr<<"p="<<p<<" poly=x4+"<<C1<<"x+"<<C0<<" root="<<root<<" pow3="<<powf(root,3)<<" pow5="<<powf(root,5)<<"\n";for(int exponent : {1,7}) { int arr[15][15],rt[15];for(int i=0;i<15;i++)rt[i]=powf(root,(i*exponent)%15);for(int i=0;i<15;i++)for(int j=0;j<15;j++)arr[i][j]=rt[(i*j)%15];int bad=0,ex=0;map<int,int>badby;for(int mask=1;mask<(1<<15);mask++){int n=__builtin_popcount((unsigned)mask),inds[15],m[15][15],t=0;for(int i=0;i<15;i++)if(mask>>i&1)inds[t++]=i;for(int i=0;i<n;i++)for(int j=0;j<n;j++)m[i][j]=arr[inds[i]][inds[j]];int det=1;for(int i=0;i<n;i++){int k=i;while(k<n && m[k][i]==0)k++;if(k==n){det=0;break;}if(k!=i){det=mul(det,p-1);for(int j=i;j<n;j++)swap(m[i][j],m[k][j]);}det=mul(det,m[i][i]);int inv=powf(m[i][i],q-2);for(int u=i+1;u<n;u++){int fac=mul(m[u][i],inv);for(int j=i+1;j<n;j++){int z=mul(fac,m[i][j]);int a=m[u][j],r=0,d=1;for(int t=0;t<4;t++){int diff=((a%p)-(z%p)+p)%p;r+=d*diff;d*=p;a/=p;z/=p;}m[u][j]=r;}m[u][i]=0;}}if(!det){bad++;if(!ex)ex=mask;badby[n]++;}}cout<<"root="<<root<<" bad="<<bad<<" example="<<ex<<" badby=";for(auto [n,v]:badby)cout<<n<<":"<<v<<",";cout<<"\n";if(bad)return 1;}puts("GAUSSIAN_OK");return 0;}
