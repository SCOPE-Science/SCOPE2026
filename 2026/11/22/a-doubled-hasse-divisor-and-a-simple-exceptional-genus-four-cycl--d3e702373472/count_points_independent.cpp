#include <cstdio>
#include <vector>
#include <cstdint>
#include <array>
#include <cassert>
using namespace std;
int n,q,modc[5];
inline int mul(int x,int y){
 int a[4]={0},b[4]={0},c[8]={0};
 for(int i=0;i<n;i++){a[i]=x%31;x/=31;b[i]=y%31;y/=31;}
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)c[i+j]+=a[i]*b[j];
 for(int k=2*n-2;k>=n;k--){int v=c[k]%31;for(int j=0;j<n;j++)c[k-n+j]-=v*modc[j];}
 int out=0,scale=1;for(int i=0;i<n;i++){int v=(c[i]%31+31)%31;out+=v*scale;scale*=31;}
 return out;
}
inline int add(int x,int y){int out=0,scale=1;for(int i=0;i<n;i++){int s=(x%31)+(y%31);if(s>=31)s-=31;out+=s*scale;x/=31;y/=31;scale*=31;}return out;}
int main(){
 int mod[4][5]={{21,1,0,0,0},{2,12,1,0,0},{8,13,1,1,0},{17,25,23,18,1}};
 for(n=1;n<=4;n++){
  q=1;for(int i=0;i<n;i++)q*=31;
  for(int i=0;i<=n;i++)modc[i]=mod[n-1][i]; // coefficient array, constant first
  vector<char> fifth(q,0);
  for(int y=1;y<q;y++){int y2=mul(y,y),y4=mul(y2,y2);fifth[mul(y4,y)]=1;}
  int count=1; // unique point at infinity, because gcd(5,3)=1
  int zero=0,res=0;
  for(int x=0;x<q;x++){
   int x2=mul(x,x),x3=mul(x2,x);
   int f=add(add(x3,x),10);
   if(f==0){count++;zero++;}
   else if(fifth[f]){count+=5;res++;}
  }
  printf("n=%d q=%d N=%d zeros=%d fifth-residues=%d\n",n,q,count,zero,res);
 }
}
