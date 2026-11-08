// Exact finite-field Jacobian-rank certificate for q=7 Heisenberg channel secants.
// Compile: g++ -O3 -std=c++17 verify_q7.cpp -o verify_q7
// Run: ./verify_q7 parameters_q7.txt
#include <iostream>
#include <fstream>
#include <vector>
#include <array>
#include <cassert>
#include <cstdlib>
#include <string>
using namespace std;
constexpr int Q=7, N=49, R=16, P=29, COL=R*(3*N-2), ROW=N*N;
int inv29[29];
int pw(int a,int n) {int r=1; while(n-- >0) r=r*a%P;return r;}
int diff(int u,int v) {return ((u/7-v/7+Q)%Q)*Q+(u%7-v%7+Q)%Q;}
int phase(int s,int t,int k,int u,int v) {int ex=(s*(k/7)*(u%7)+t*(k/7)*(v%7))%7;return pw(7,(Q-ex)%Q);}
int rank_certificate(int s,int t,const vector<int>& par) {
  vector<unsigned short> mat((size_t)ROW*COL,0);
  // Exact partial derivatives of A(a)^T diag(d) B(b) with respect to
  // each a_h, b_h, d_h. The a_0 and b_0 columns are omitted in each
  // channel: they are redundant by the two scaling symmetries.
  for(int i=0;i<N;i++)for(int j=0;j<N;j++){
   size_t off=(size_t)(i*N+j)*COL;
   for(int ell=0;ell<R;ell++){
    int ba=ell*3*N,bc=ell*(3*N-2);
    for(int h=0;h<N;h++){
     if(h) {
      int k=diff(i,h), g=diff(j,k);
      mat[off+bc+h-1]=(phase(s,t,k,h,g)*par[ba+2*N+k]*par[ba+N+g])%P;
      k=diff(j,h);g=diff(i,k);
      mat[off+bc+(N-1)+h-1]=(phase(s,t,k,g,h)*par[ba+2*N+k]*par[ba+g])%P;
     }
     int k=h,u=diff(i,k),v=diff(j,k);
     mat[off+bc+2*(N-1)+h]=(phase(s,t,k,u,v)*par[ba+u]*par[ba+N+v])%P;
    }
   }
  }
  int rank=0;
  for(int c=0;c<COL;c++){
   int pivot=rank;
   while(pivot<ROW && !mat[(size_t)pivot*COL+c]) pivot++;
   if(pivot==ROW) {cerr<<"rank deficit at col="<<c<<" for type "<<s<<","<<t<<"\n";return rank;}
   if(pivot!=rank)for(int j=c;j<COL;j++) swap(mat[(size_t)pivot*COL+j],mat[(size_t)rank*COL+j]);
   const int iv=inv29[mat[(size_t)rank*COL+c]];
   for(int j=c;j<COL;j++)mat[(size_t)rank*COL+j]=(mat[(size_t)rank*COL+j]*iv)%P;
   for(int i=rank+1;i<ROW;i++){
    int f=mat[(size_t)i*COL+c];
    if(!f)continue;
    size_t io=(size_t)i*COL, ro=(size_t)rank*COL;
    // All entries stay in 0..28.
    for(int j=c;j<COL;j++)mat[io+j]=(mat[io+j]+P*P-f*mat[ro+j])%P;
   }
   rank++;
  }
  return rank;
}
int main(int argc,char** argv) {
 if(argc!=2) {cerr<<"Usage: verify_q7 parameters_q7.txt\n";return 2;}
 if(pw(7,7)!=1) return 3;
 for(int k=1;k<7;k++)if(pw(7,k)==1)return 3;
 for(int x=1;x<P;x++)for(int y=1;y<P;y++)if(x*y%P==1){inv29[x]=y;break;}
 ifstream f(argv[1]);if(!f) {cerr<<"Cannot read parameter file\n";return 2;}
 vector<int> par(R*3*N);
 for(auto &v:par) {if(!(f>>v) || v<1 || v>28) {cerr<<"Bad parameters\n";return 4;}}
 string extra;if(f>>extra) {cerr<<"Extra parameter data\n";return 4;}
 const int cases[4][2]={{0,0},{0,1},{1,1},{1,2}};
 for(auto &ca:cases) {
  int rank=rank_certificate(ca[0],ca[1],par);
  cout<<"type=("<<ca[0]<<","<<ca[1]<<") rank="<<rank<<" expected="<<COL<<endl;
  if(rank!=COL)return 1;
 }
 cout<<"ALL_FOUR_JACOBIAN_RANK_CERTIFICATES_OK"<<endl;
 return 0;
}
