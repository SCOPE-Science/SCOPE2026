#include <bits/stdc++.h>
using namespace std;
constexpr int p=19;
static int mod(int x){x%=p;return x<0?x+p:x;}
static int powmod(int x,int n){int a=1;for(;n;n>>=1,x=mod(x*x))if(n&1)a=mod(a*x);return a;}
using Poly=array<int,5>;
static Poly mul(Poly A,Poly B){Poly C{};for(int i=0;i<5;i++)for(int j=0;i+j<5;j++)C[i+j]=mod(C[i+j]+A[i]*B[j]);return C;}
static Poly sum(Poly A,Poly B,int scale=1){for(int i=0;i<5;i++)A[i]=mod(A[i]+scale*B[i]);return A;}
static bool square_up_to_scalar(Poly a){int d=4;while(d>=0&&!a[d])d--;
 if(d<0){cerr<<"Unexpected contained line\n";exit(3);}if(d&1)return false;
 if(d==0)return true;
 int k=a[d],uinv=powmod(mod(2*k),p-2),u=mod(a[d-1]*uinv);
 if(d==2)return a[0]==mod(k*u*u);
 int v=mod((a[2]-k*u*u)*uinv);
 return a[1]==mod(2*k*u*v)&&a[0]==mod(k*v*v);
}
int main(){int hist[30]={}, detail[30]={};
 for(int c=1;c<p;c++){
  int count=0;
  for(int a=0;a<=1;a++)for(int b=0;b<p;b++)for(int d=0;d<p;d++){
    if((a==0&&b!=1)||(a==0&&d>0&&b==0))continue;
    Poly X{},Y{},Z{};
    if(a==1){X[1]=mod(-b);X[0]=mod(-d);Y[1]=1;Z[0]=1;}
    else {X[1]=1;Y[0]=mod(-d);Z[0]=1;}
    auto P=sum(sum(mul(mul(Y,Y),mul(Y,Z)),mul(mul(X,X),mul(X,X)),-1),mul(X,mul(Z,mul(Z,Z))),c);
    if(square_up_to_scalar(P))count++;
  }
  {Poly X{},Y{},Z{};X[1]=1;Y[0]=1; auto P=sum(mul(mul(Y,Y),mul(Y,Z)),mul(mul(X,X),mul(X,X)),-1);if(square_up_to_scalar(P))count++;}
  if(count!=1&&count!=28){cerr<<"Unexpected bitangent count c="<<c<<": "<<count<<"\n";return 2;}
  int ch=powmod(c,2),order=1,x=ch;
  while(x!=1){x=mod(x*ch);order++;if(order>9)abort();}
  hist[order]+=1;
  if(order==1)detail[1]+=count==28;else detail[order]+=count==1;
  cout<<"c="<<c<<" ninth-character-order="<<order<<" rational-bitangents="<<count<<"\n";
 }
 cout<<"totals: order1="<<hist[1]<<" order3="<<hist[3]<<" order9="<<hist[9]<<"\n";
 // The affine model can have a fixed Frobenius shift; hence compare the number of 28 counts, not order=1 directly.
}
