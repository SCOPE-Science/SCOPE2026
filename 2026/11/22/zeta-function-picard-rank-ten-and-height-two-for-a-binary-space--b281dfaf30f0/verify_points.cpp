#include <bits/stdc++.h>
using namespace std;
struct GF{int n,q,mask,prim;vector<int> ex,lg;
GF(int n):n(n),q(1<<n),mask((1<<n)-1){
// primitive binary polys for n=1..13; need primitive to build log tables
int p[]={0,0x3,0x7,0xb,0x13,0x25,0x43,0x83,0x11d,0x211,0x409,0x805,0x1053,0x201b};prim=p[n];
ex.assign(2*(q-1)+1,0);lg.assign(q,-1);int t=1;
for(int i=0;i<q-1;i++){if(lg[t]>=0){cerr<<"nonprimitive n "<<n<<" cycle "<<i<<"\n"; exit(1);}ex[i]=t;lg[t]=i;t<<=1;if(t&q)t^=prim;}
if(t!=1){cerr<<"not generator n "<<n<<"\n"; exit(1);}for(int i=q-1;i<(int)ex.size();i++)ex[i]=ex[i-q+1];}
inline int mul(int a,int b)const{if(!a||!b)return 0;return ex[lg[a]+lg[b]];}
inline int sq(int a)const{if(!a)return 0;return ex[2*lg[a]];}
inline int cu(int a)const{return mul(sq(a),a);}
};
long long count(int n){GF f(n);int q=f.q;vector<int> square(q),cube(q),cnt(q);for(int a=0;a<q;a++){square[a]=f.sq(a);cube[a]=f.cu(a);}
long long chart=0;for(int y=0;y<q;y++){
 fill(cnt.begin(),cnt.end(),0);int y2=square[y],y3=cube[y];int b=y3^1;
 for(int x=0;x<q;x++){int c=cube[x]^f.mul(y2,square[x])^f.mul(b,x);cnt[c]++;}
 for(int z=0;z<q;z++){int c=f.mul(square[z],y2^1)^f.mul(y,cube[z])^z; chart+=cnt[c];}
 }
long long boundary=0; // x3=0; count projective [x0:x1:x2]
// x2=1
for(int x=0;x<q;x++) for(int y=0;y<q;y++){
 int F=f.mul(square[x],square[y])^f.mul(x,cube[y])^square[y]^f.mul(y,1); // term x1^2*x2^2 + x1*x2^3 = y^2+y
 if(F==0)boundary++;
}
// x2=0,x1=1: F=x0^2+x0 -> two roots over all q
boundary+=2; // x2=x1=0: unique x0=1
boundary++;
return chart+boundary;}
int main(){for(int n=1;n<=13;n++){auto a=count(n);cout<<n<<" "<<(1<<n)<<" "<<a<<"\n";}}