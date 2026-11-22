#include <bits/stdc++.h>
using namespace std;
bool prime(int n,int b,int p,int q){int N=n+1;int out[20]={};for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){if(i==p&&j==q)out[j]|=1<<i;else out[i]|=1<<j;}for(int i=0;i<n;i++){if(b>>i&1)out[i]|=1<<n;else out[n]|=1<<i;}int all=(1<<N)-1;for(int m=1;m<all;m++){if((m&(m-1))==0)continue;for(int t=all^m;t;t&=t-1){int i=__builtin_ctz((unsigned)t);int row=out[i]&m;if(row!=0&&row!=m)goto nextmask;}return false;nextmask:;}return true;}
bool predicted(int n,int b,int p,int q){auto bit=[&](int i){return (b>>i)&1;};if(q==p+1){if(n%2)return false;for(int i=0;i<n;i++){int rank=(i==p?q:(i==q?p:i));if(bit(i)!=(rank%2))return false;}return true;}
 if(p>0){if(bit(0)!=0)return false;for(int i=0;i+1<p;i++)if(bit(i)==bit(i+1))return false;}
 if(q<n-1){if(bit(n-1)!=1)return false;for(int i=q+1;i+1<n;i++)if(bit(i)==bit(i+1))return false;}
 for(int i=p+1;i+1<q;i++)if(bit(i)==bit(i+1))return false;
 if(q==p+2){if(bit(p)==bit(p+1)&&bit(p+1)==bit(q))return false;}
 if(p==0&&q==n-1&&bit(p)==1&&bit(q)==0)return false;
 return true;}
int main(){long long cnt=0;for(int n=4;n<=12;n++){
 for(int p=0;p<n;p++)for(int q=p+1;q<n;q++)for(int b=0;b<(1<<n);b++){bool P=predicted(n,b,p,q), Q=prime(n,b,p,q);if(P!=Q){cerr<<"MISMATCH n,p,q,b="<<n<<","<<p<<","<<q<<","<<b<<" predicted="<<P<<" prime="<<Q<<"\n";return 1;}cnt++;}
 cerr<<"verified n="<<n<<"\n";
 }cout<<"VERIFY_OK cases="<<cnt<<" n=4..12\n";}
