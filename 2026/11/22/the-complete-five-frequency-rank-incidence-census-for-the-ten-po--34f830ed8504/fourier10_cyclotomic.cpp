// Independently computes the exact Q(zeta_10) ranks of all central Fourier minors.
// No finite-field rank computations: every determinant is reduced in Z[x]/Phi_10.
#include <array>
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
const int powers[10][4]={{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1},{-1,1,-1,1},{-1,0,0,0},{0,-1,0,0},{0,0,-1,0},{0,0,0,-1},{1,-1,1,-1}};
struct Term {array<int,5> p{};int sign;};
vector<Term> terms[6];
void init(){for(int k=1;k<=5;k++){
 array<int,5> a{};for(int j=0;j<k;j++)a[j]=j;
 do{int inv=0;for(int i=0;i<k;i++)for(int j=i+1;j<k;j++)if(a[i]>a[j])inv++;
 terms[k].push_back({a,inv%2?-1:1});
 }while(next_permutation(a.begin(),a.begin()+k));
}}
inline bool nonzero(const int *r,const int *c,int k){
 int d[4]={0,0,0,0};
 for(const auto &term:terms[k]){
  int exp=0;
  for(int i=0;i<k;i++)exp+=r[i]*c[term.p[i]];
  const int *basis=powers[exp%10];
  for(int t=0;t<4;t++)d[t]+=term.sign*basis[t];
 }
 return d[0]||d[1]||d[2]||d[3];
}
struct Set{int mask;int a[5];};
int exact_rank(const Set &R,const Set &C){
 if(nonzero(R.a,C.a,5))return 5;
 int rows[4],cols[4];
 for(int i=0;i<5;i++)for(int j=0;j<5;j++){
  int nr=0,nc=0;
  for(int ii=0;ii<5;ii++)if(ii!=i)rows[nr++]=R.a[ii];
  for(int jj=0;jj<5;jj++)if(jj!=j)cols[nc++]=C.a[jj];
  if(nonzero(rows,cols,4))return 4;
 }
 // Four minors all zero; determine if an order-three minor survives.
 int rr[3],cc[3];
 for(int x=0;x<5;x++)for(int y=x+1;y<5;y++)for(int a=0;a<5;a++)for(int b=a+1;b<5;b++){
  int nr=0,nc=0;
  for(int i=0;i<5;i++)if(i!=x&&i!=y)rr[nr++]=R.a[i];
  for(int j=0;j<5;j++)if(j!=a&&j!=b)cc[nc++]=C.a[j];
  if(nonzero(rr,cc,3))return 3;
 }
 int a2[2], b2[2];
 for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)for(int x=0;x<5;x++)for(int y=x+1;y<5;y++){
  a2[0]=R.a[i]; a2[1]=R.a[j];b2[0]=C.a[x];b2[1]=C.a[y];
  if(nonzero(a2,b2,2))return 2;
 }
 return 1; // every entry is a nonzero root of unity
}
int main(){init();vector<Set> ss;
 for(int mask=0;mask<1024;mask++)if(__builtin_popcount((unsigned)mask)==5){Set e{};e.mask=mask;int j=0;for(int i=0;i<10;i++)if((mask>>i)&1)e.a[j++]=i;ss.push_back(e);}
 array<long long,6> totals{};
 for(auto &R:ss)for(auto &C:ss){int r=exact_rank(R,C);totals[r]++;}
 cout<<"{\"method\":\"exact cyclotomic integer determinant coefficient reduction\",\"phi\":\"x^4-x^3+x^2-x+1\",\"total_ranks\":[";
 for(int k=0;k<6;k++){if(k)cout<<",";cout<<totals[k];}cout<<"],\"total_pairs\":"<<ss.size()*ss.size()<<"}\n";
}
