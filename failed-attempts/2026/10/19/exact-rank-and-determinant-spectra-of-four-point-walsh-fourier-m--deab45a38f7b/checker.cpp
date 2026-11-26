// Exact enumeration of four-by-four submatrices of binary Walsh matrices.
// Compile: c++ -O2 -std=c++17 checker.cpp -o checker && ./checker
#include <array>
#include <vector>
#include <iostream>
#include <cassert>
#include <cstdint>
using namespace std;
using U=uint64_t;

int det3(const int a[3][3]){
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
       -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
       +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]);
}
array<int,2> minor_profile(const array<int,4>& A,const array<int,4>& B){
 int H[4][4];
 for(int i=0;i<4;i++) for(int j=0;j<4;j++)
  H[i][j]=(__builtin_parity((unsigned)(A[i]&B[j])) ? -1:1);
 int Q[3][3];
 for(int i=1;i<4;i++) for(int j=1;j<4;j++)
  Q[i-1][j-1]=(H[i][j]*H[i][0]-H[0][j]*H[0][0])/2;
 int d=det3(Q);
 if(d) return {4,8*(d<0?-d:d)};
 for(int i=0;i<3;i++) for(int k=i+1;k<3;k++)
  for(int j=0;j<3;j++) for(int l=j+1;l<3;l++)
   if(Q[i][j]*Q[k][l]!=Q[i][l]*Q[k][j]) return {3,0};
 for(int i=0;i<3;i++) for(int j=0;j<3;j++) if(Q[i][j]) return {2,0};
 return {1,0};
}
U choose(U n,U k){if(n<k)return 0;U r=1;for(U i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
U choose4(U n){return n>=4?n*(n-1)*(n-2)*(n-3)/24:0;}
U surj(U k,U r,U m){
 // Exactly r occupied fibres from k fibres, four chosen points.
 U ans=0;
 for(U j=0;j<=r;j++){
  U t=choose(r,j)*choose4((r-j)*m);
  if(j%2)ans-=t;else ans+=t;
 }
 return choose(k,r)*ans;
}
array<U,5> expected_ranks(int N){
 U n=N,T=choose4(n),P=n*(n-1)*(n-2)/24,m=n/8;
 array<U,5> arr{};
 for(U r=1;r<=4;r++){
  U pp=surj(4,r,n/4),ii=surj(8,r,m);
  if(r==3)ii+=12*m*m*m*m;
  if(r==4)ii-=12*m*m*m*m;
  arr[r]=P*pp+(T-P)*ii;
 }
 return arr;
}
vector<array<int,4>> subsets(int n){
 vector<array<int,4>> v;
 for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)for(int d=c+1;d<n;d++) v.push_back({a,b,c,d});
 return v;
}
int main(){
 for(int n:{8,16}){
  auto subs=subsets(n);
  array<U,5> count{};array<U,17> vals{};
  for(auto& a:subs)for(auto& b:subs){
   auto [r,d]=minor_profile(a,b);assert(r>=1&&r<=4);assert(d==0||d==8||d==16);
   count[r]++;vals[d]++;
  }
  auto e=expected_ranks(n);assert(count==e);
  U N=n,P=N*(N-1)*(N-2)/24,T=choose4(N),m=N/8;
  U d16=P*(N/4)*(N/4)*(N/4)*(N/4)+(T-P)*2*m*m*m*m;
  U d8=(T-P)*56*m*m*m*m;
  assert(vals[16]==d16 && vals[8]==d8 && vals[0]==T*T-d16-d8);
  cout<<"N="<<N<<" pair_count="<<T*T<<" ranks=";
  for(int r=1;r<=4;r++)cout<<count[r]<<(r==4?' ':';');
  cout<<"det0="<<vals[0]<<" det8="<<vals[8]<<" det16="<<vals[16]<<" PASS\n";
 }
 cout<<"CHECK_PASS\n";
}
