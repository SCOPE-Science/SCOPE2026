#include <array>
#include <vector>
#include <iostream>
#include <stdexcept>
#include <cstdint>
using namespace std;
using Mat=array<int,9>;
Mat sym(int k,int q){Mat A{};int d[6];for(int j=0;j<6;j++){d[j]=k%q;k/=q;}A[0]=d[0];A[1]=A[3]=d[1];A[2]=A[6]=d[2];A[4]=d[3];A[5]=A[7]=d[4];A[8]=d[5];return A;}
array<int,3> bracket(const Mat &A,const Mat &B,int q){int ij[3][2]={{0,1},{0,2},{1,2}};array<int,3> v{};for(int a=0;a<3;a++){int i=ij[a][0],j=ij[a][1],z=0;for(int k=0;k<3;k++)z+=A[3*i+k]*B[3*k+j]-B[3*i+k]*A[3*k+j];v[a]=((z%q)+q)%q;}return v;}
int idx(array<int,3> v,int q){return v[0]+q*v[1]+q*q*v[2];}
int64_t pw(int q,int n){int64_t x=1;while(n--)x*=q;return x;}
int main(){for(int q:{3,5,7}){
 int N=(int)pw(q,6),T=q*q*q;
 vector<int64_t> counts(T,0);
 if(q==3){vector<Mat> mats;for(int a=0;a<N;a++)mats.push_back(sym(a,q));for(const auto& A:mats)for(const auto& B:mats)counts[idx(bracket(A,B,q),q)]++;}
 else{Mat bases[6];for(int j=0;j<6;j++)bases[j]=sym((int)pw(q,j),q);
 for(int a=0;a<N;a++){Mat X=sym(a,q);vector<int> sub{0};vector<unsigned char> seen(T,0);seen[0]=1;int rank=0;
 for(const Mat& basis:bases){auto w=bracket(X,basis,q);int wcode=idx(w,q);if(seen[wcode])continue;vector<int> old=sub;
  for(int z:old){int u=z%q,v=(z/q)%q,t=z/(q*q);for(int k=1;k<q;k++){int code=((u+k*w[0])%q)+q*((v+k*w[1])%q)+q*q*((t+k*w[2])%q);if(seen[code])throw runtime_error("span duplicate");seen[code]=1;sub.push_back(code);}}
  rank++;
 }
 if((int)sub.size()!=(int)pw(q,rank))throw runtime_error("span size");
 int64_t num=pw(q,6-rank);for(int code:sub)counts[code]+=num;
 }}
 const int64_t want0=pw(q,9)+pw(q,8)-pw(q,5),want1=pw(q,9)-pw(q,5);
 int64_t total=0;for(int t=0;t<T;t++){total+=counts[t];if(counts[t]!=(t==0?want0:want1)){cerr<<"mismatch q="<<q<<" target="<<t<<" observed="<<counts[t]<<" expected="<<(t==0?want0:want1)<<"\n";return 1;}}
 if(total!=pw(q,12))throw runtime_error("mass");
 cout<<"q="<<q<<" inputs_per_factor="<<N<<" targets="<<T<<" zero_fiber="<<counts[0]<<" nonzero_fiber="<<counts[1]<<" mass="<<total<<" PASS\n";
 }
 cout<<"SYMMETRIC_COMMUTATOR_ALL_CHECKS_PASS\n";}
