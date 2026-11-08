// Exact independent F4 coefficient count for extremal Frobenius-nonclassical plane sextics.
// Compile: c++ -O2 -std=c++17 verify_fnc_f4_count.cpp -o verify && ./verify
// No external libraries or data files are required.
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
using P=array<int,3>;
int mul(int a,int b){int ans=0;for(int i=0;i<2;++i)for(int j=0;j<2;++j)if((a>>i&1)&&(b>>j&1))ans^=1<<(i+j);if(ans&8)ans^=14;if(ans&4)ans^=7;return ans;}
int power(int a,int n){int r=1;while(n-- >0)r=mul(r,a);return r;}
int f0(P p){return mul(mul(mul(p[0],p[1]),p[2]),power(p[0],3)^power(p[1],3)^power(p[2],3));}
int det3(const int A[3][3]){
 int d=0;
 for(int a=0;a<3;++a)for(int b=0;b<3;++b)if(a!=b){
  int c=3-a-b;
  if(c!=a&&c!=b)d^=mul(mul(A[0][a],A[1][b]),A[2][c]);
 }
 return d;
}
int rank10(int E[21][10]){
 int A[21][10];
 for(int i=0;i<21;++i)for(int j=0;j<10;++j)A[i][j]=E[i][j];
 int piv=0;
 for(int j=0;j<10;++j){
  int k=piv;
  while(k<21 && !A[k][j])++k;
  if(k==21)continue;
  for(int c=0;c<10;++c)swap(A[k][c],A[piv][c]);
  int inv=A[piv][j]==1?1:(A[piv][j]==2?3:2);
  for(int c=j;c<10;++c)A[piv][c]=mul(inv,A[piv][c]);
  for(int r=0;r<21;++r)if(r!=piv && A[r][j]){
   int f=A[r][j];
   for(int c=j;c<10;++c)A[r][c]^=mul(f,A[piv][c]);
  }
  ++piv;
 }
 return piv;
}
int diagform(P p){
 return f0(p)^power(p[0],6)^mul(2,power(p[1],6))^mul(3,power(p[2],6));
}
int main(){
 vector<P> pts;
 for(int y=0;y<4;++y)for(int z=0;z<4;++z)pts.push_back({1,y,z});
 for(int z=0;z<4;++z)pts.push_back({0,1,z});
 pts.push_back({0,0,1});
 if(pts.size()!=21)throw runtime_error("points");
 int mat[21][10],base[21];
 for(int t=0;t<21;++t){
  P p=pts[t];base[t]=f0(p);int j=0;
  for(int i=0;i<=3;++i)for(int k=0;k<=3-i;++k){
   int l=3-i-k;
   mat[t][j++]=mul(mul(power(p[0],2*i),power(p[1],2*k)),power(p[2],2*l));
  }
 }
 uint64_t valid=0;
 for(uint32_t id=0;id<(1U<<20);++id){
  bool ok=true;
  for(int p=0;p<21 && ok;++p){
   int v=base[p];
   for(int j=0;j<10;++j)v^=mul((id>>(2*j))&3,mat[p][j]);
   if(v==0)ok=false;
  }
  valid+=ok;
 }
 if(valid!=960)throw runtime_error("Incorrect census");
 if(rank10(mat)!=10)throw runtime_error("Evaluation map not injective");
 for(P p:pts)if(!diagform(p))throw runtime_error("Diagonal representative not smooth");
 long long invertible=0, stabilizing=0;
 for(uint32_t id=0;id<(1U<<18);++id){
  int A[3][3];
  for(int i=0;i<3;++i)for(int j=0;j<3;++j)A[i][j]=(id>>(2*(3*i+j)))&3;
  int d=det3(A);
  if(!d)continue;
  ++invertible;
  bool fixes=true;
  for(P p:pts){
   P Ap={0,0,0};
   for(int i=0;i<3;++i)for(int j=0;j<3;++j)Ap[i]^=mul(A[i][j],p[j]);
   if(diagform(Ap)!=mul(d,diagform(p))){fixes=false;break;}
  }
  stabilizing+=fixes;
 }
 if(invertible!=181440 || stabilizing!=189)throw runtime_error("Incorrect linear stabilizer count");
 // 3 scalar matrices represent one projectivity; hence projective stabilizer order 63.
 if(invertible/stabilizing!=960)throw runtime_error("Orbit size does not equal smooth count");
 cout<<"F4_EXTREMAL_SEXTICS_COUNT_PASS "<<valid<<"\n";
 cout<<"F4_EXTREMAL_SEXTICS_PGL_ORBIT_PASS "<<invertible<<" "<<stabilizing<<" "<<invertible/stabilizing<<"\n";
}
