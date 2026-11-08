#include <array>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;
struct Field {
 int q;
 int add(int a,int b) const {return q==4 ? (a^b) : (a+b)%q;}
 int neg(int a) const {return q==4?a:(q-a)%q;}
 int mul(int a,int b) const {
   if(q!=4)return (a*b)%q;
   int z=0;
   for(int i=0;i<2;i++)for(int j=0;j<2;j++)if((a>>i&1)&&(b>>j&1))z^=1<<(i+j);
   if(z&8) z^=14; // x^3 = x(x^2+x+1), reduce x^3 by x^3+x^2+x
   if(z&4) z^=7; // x^2+x+1
   return z;
 }
 int inv(int a) const {for(int i=1;i<q;i++)if(mul(a,i)==1)return i;return -1;}
};
using Matrix=vector<vector<int>>;
Matrix matrix_for(int code,int n,int q){ Matrix m(n,vector<int>(n,0)); for(int i=0;i<n;i++)for(int j=0;j<n;j++){m[i][j]=code%q;code/=q;}return m;}
Matrix prod(const Matrix &a,const Matrix&b,const Field&f){int n=a.size(); Matrix r(n,vector<int>(n));for(int i=0;i<n;i++)for(int j=0;j<n;j++)for(int k=0;k<n;k++)r[i][j]=f.add(r[i][j],f.mul(a[i][k],b[k][j]));return r;}
int rankof(Matrix a,const Field&f){int n=a.size(),m=a[0].size(),r=0;for(int j=0;j<m&&r<n;j++){int i=r;while(i<n&&a[i][j]==0)i++;if(i==n)continue;swap(a[i],a[r]);int iv=f.inv(a[r][j]);assert(iv>0);for(int k=j;k<m;k++)a[r][k]=f.mul(a[r][k],iv);for(int u=r+1;u<n;u++){int z=a[u][j];for(int k=j;k<m;k++)a[u][k]=f.add(a[u][k],f.neg(f.mul(z,a[r][k])));}r++;}return r;}
void test(int q,int r){Field f{q}; int num=1;for(int i=0;i<r*r;i++)num*=q;map<pair<int,int>,long long> count; long long attempts=0;
 Matrix A(2*r,vector<int>(2*r)); for(int i=0;i<r;i++)A[i][r+i]=1;
 for(int ix=0;ix<num;ix++){
  Matrix X=matrix_for(ix,r,q); Matrix X2=prod(X,X,f);bool square=true;for(int i=0;i<r;i++)for(int j=0;j<r;j++)if(X2[i][j])square=false;if(!square)continue;
  int s=rankof(X,f);
  for(int iy=0;iy<num;iy++){
   Matrix Y=matrix_for(iy,r,q),B(2*r,vector<int>(2*r));for(int i=0;i<r;i++)for(int j=0;j<r;j++){B[i][j]=X[i][j];B[i][j+r]=Y[i][j];B[i+r][j+r]=X[i][j];}
   Matrix B2=prod(B,B,f);bool good=true;for(int i=0;i<2*r;i++)for(int j=0;j<2*r;j++)if(B2[i][j])good=false;
   if(!good)continue;
   Matrix AB=prod(A,B,f),BA=prod(B,A,f);for(int i=0;i<2*r;i++)for(int j=0;j<2*r;j++)assert(AB[i][j]==BA[i][j]);
   count[{s,rankof(B,f)}]++;attempts++;
  }
 }
 printf("q=%d r=%d commuting_square_zero_B=%lld\n",q,r,attempts);
 for(auto [st,v]:count)printf(" reduction_rank=%d B_rank=%d count=%lld\n",st.first,st.second,v);
}
int main(){test(2,1);test(2,2);test(3,2);test(4,2);test(5,2);test(2,3);puts("DIRECT_COMMUTING_SQUARE_ZERO_PASS");}
