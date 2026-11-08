// Direct finite-field verification of associative commutator fibers in K[S3].
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <array>
#include <vector>
#include <iostream>
#include <stdexcept>
#include <cstdint>
using namespace std;
using Perm = array<int,3>;
const Perm gp[6]={Perm{0,1,2},Perm{1,0,2},Perm{0,2,1},Perm{2,1,0},Perm{1,2,0},Perm{2,0,1}};
int mul[6][6];
void prep(){for(int i=0;i<6;i++)for(int j=0;j<6;j++){
 Perm z;for(int k=0;k<3;k++) z[k]=gp[i][gp[j][k]];
 int r=-1;for(int t=0;t<6;t++)if(z==gp[t])r=t;
 if(r<0)throw runtime_error("perm multiplication");mul[i][j]=r;
 }}
struct Field{int q;int add(int x,int y)const{return q==4 ? x^y : (x+y)%q;}
 int neg(int x)const{return q==4?x:(q-x)%q;}
 int prod(int x,int y)const{if(q!=4)return x*y%q;
  int v=0;for(int i=0;i<2;i++)if((y>>i)&1)v^=(x<<i);
  if(v&8)v^=0b1100; if(v&4)v^=0b111;return v;
 }
 int sub(int x,int y)const{return add(x,neg(y));}
};
using Vec=array<unsigned char,6>;
Vec decode(int n,int q){Vec x{};for(int i=0;i<6;i++){x[i]=n%q;n/=q;}return x;}
int encode(const Vec& x,int q){int a=0,t=1;for(int i=0;i<6;i++){a+=x[i]*t;t*=q;}return a;}
Vec direct(const Vec& x,const Vec& y,const Field& F){Vec z{};
 for(int i=0;i<6;i++)if(x[i])for(int j=0;j<6;j++)if(y[j]){
 int t=F.prod(x[i],y[j]);
 z[mul[i][j]]=F.add(z[mul[i][j]],t);
 z[mul[j][i]]=F.sub(z[mul[j][i]],t);
 } return z;
}
// Input basis order: 1, (12), (23), (13), (123), (132).
// Central class sums: 1, (12)+(23)+(13), (123)+(132).
// The quotient coordinates in basis (12),(23),(123) are
// (x_s - x_u, x_t - x_u, x_r - x_rinv).
// Wedge outputs: [s,t]=r-rinv; [s,r]=t-u; [t,r]=u-s.
Vec predicted(const Vec &x,const Vec &y,const Field &F){
 int A=F.sub(x[1],x[3]),B=F.sub(x[2],x[3]),C=F.sub(x[4],x[5]);
 int D=F.sub(y[1],y[3]),E=F.sub(y[2],y[3]),H=F.sub(y[4],y[5]);
 int h=F.sub(F.prod(A,E),F.prod(B,D));
 int i=F.sub(F.prod(A,H),F.prod(C,D));
 int j=F.sub(F.prod(B,H),F.prod(C,E));
 Vec w{};w[1]=F.neg(j);w[2]=i;w[3]=F.sub(j,i);w[4]=h;w[5]=F.neg(h);return w;
}
void run(int q){Field F{q};int m=1;for(int i=0;i<6;i++)m*=q;
 const long long total=1LL*m*m;
 vector<long long> count(m,0);
 for(int a=0;a<m;a++){
  Vec x=decode(a,q);
  for(int b=0;b<m;b++){
   Vec y=decode(b,q);
   Vec u=direct(x,y,F),v=predicted(x,y,F);
   if(u!=v)throw runtime_error("direct algebra disagrees with wedge reduction");
   count[encode(u,q)]++;
  }
 }
 long long c0=1LL*q*q*q*q*q*q*(1LL*q*q*q*q+1LL*q*q*q-q);
 long long c1=1LL*q*q*q*q*q*q*q*(1LL*q*q-1);
 long long nz=0,un=0;for(int a=0;a<m;a++){
  Vec w=decode(a,q);bool isW=F.add(F.add(w[1],w[2]),w[3])==0 && F.add(w[4],w[5])==0 && w[0]==0;
  long long exp=(a==0?c0:(isW?c1:0));
  if(count[a]!=exp)throw runtime_error("fiber histogram mismatch");
  if(a!=0 && isW)nz++;
  if(count[a])un++;
 }
 if(nz!=1LL*q*q*q-1 || un!=1LL*q*q*q || c0+(1LL*q*q*q-1)*c1!=total)throw runtime_error("global check");
 cout<<"q="<<q<<" elements="<<m<<" pairs="<<total<<" zero_fiber="<<c0<<" nonzero_fiber="<<c1<<" attained="<<un<<" OK\n";
}
int main(){prep();for(int q:{2,3,4})run(q);cout<<"VERIFY_OK\n";}
