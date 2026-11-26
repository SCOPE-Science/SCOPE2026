// Exact and sampled checks for multiplication ranks in the group algebra of (C2)^5.
// C++17: g++ -O3 -std=c++17 verify.cpp -o verify && ./verify
#include <bits/stdc++.h>
using namespace std;
static vector<int> subs[6];
static uint32_t positions[32];
int gf2rank(vector<uint32_t> cols, int maxbits=32){
 uint32_t basis[32]={}; int rank=0;
 for(uint32_t x: cols){
  while(x){int i=31-__builtin_clz(x); if(basis[i])x^=basis[i]; else{basis[i]=x;rank++;break;}}
 }
 return rank;
}
int multiplication_rank(uint32_t f){
 vector<uint32_t> cols(32,0);
 for(int t=0;t<32;t++){
  uint32_t c=0;
  for(int s=1;s<32;s++)if((f>>s)&1u)if(!(s&t))c^=(uint32_t(1)<<(s|t));
  cols[t]=c;
 }
 return gf2rank(cols);
}
int alternating_rank(uint32_t f,int degree){
 // Encode a degree-2 bivector directly, or a degree-3 trivector using Hodge dual.
 vector<uint32_t> rows(5,0);
 for(int s:subs[degree]) if((f>>s)&1u){
  int t=(degree==2 ? s:(31^s));
  int i=__builtin_ctz(t), j=31-__builtin_clz(t);
  rows[i]^=uint32_t(1)<<j;
  rows[j]^=uint32_t(1)<<i;
 }
 return gf2rank(rows,5);
}
int predicted(uint32_t x){
 uint32_t f[6]={};
 for(int s=1;s<32;s++)if((x>>s)&1u)f[__builtin_popcount((unsigned)s)]|=(uint32_t(1)<<s);
 if(f[1])return 16;
 if(f[2]){
  int ar=alternating_rank(f[2],2);
  if(ar==4)return 12;
  assert(ar==2);
  int wedge=0;
  for(int s:subs[2])if((f[2]>>s)&1u)
   wedge^=(int)((f[3]>>(31^s))&1u);
  return wedge?10:8;
 }
 if(f[3])return alternating_rank(f[3],3)+2;
 if(f[4])return 2;
 if(f[5])return 1;
 return 0;
}
int main(){
 for(int i=0;i<32;i++)subs[__builtin_popcount((unsigned)i)].push_back(i);
 uint32_t choose2mask=0,choose3mask=0;
 for(int i:subs[2])choose2mask|=1u<<i;
 for(int i:subs[3])choose3mask|=1u<<i;
 uint64_t counts[17]={};
 for(int a=0;a<(1<<10);a++){
  uint32_t q=0;
  for(int j=0;j<10;j++) if((a>>j)&1)q|=1u<<subs[2][j];
  for(int b=0;b<(1<<10);b++){
   uint32_t c=0;
   for(int j=0;j<10;j++)if((b>>j)&1)c|=1u<<subs[3][j];
   uint32_t x=q|c;
   int r=multiplication_rank(x),p=predicted(x);
   if(r!=p){cerr<<"FAIL_QC "<<a<<" "<<b<<" "<<r<<" "<<p<<"\n";return 1;}
   counts[r]++;
  }
 }
 // Check explicit compressed rank table with D=E=0.
 assert(counts[0]==1);
 assert(counts[4]==155);
 assert(counts[6]==868);
 assert(counts[8]==155*512);
 assert(counts[10]==155*512);
 assert(counts[12]==868*1024);
 mt19937 rng(102711);
 for(int z=0;z<40000;z++){
  uint32_t q=0,c=0,d=0,e=0,l=0;
  for(int i:subs[2])if(rng()&1)q|=1u<<i;
  for(int i:subs[3])if(rng()&1)c|=1u<<i;
  for(int i:subs[4])if(rng()&1)d|=1u<<i;
  for(int i:subs[5])if(rng()&1)e|=1u<<i;
  if(z%3==0)for(int i:subs[1])if(rng()&1)l|=1u<<i;
  uint32_t x=l|q|c|d|e;
  int r=multiplication_rank(x),p=predicted(x);
  if(r!=p){cerr<<"FAIL_RANDOM "<<x<<" "<<r<<" "<<p<<"\n";return 2;}
 }
 // Sum of predicted full-field rank multiplicities at q=2 is 2^31.
 uint64_t full[17]={};
 full[0]=1;full[1]=1;full[2]=62;full[4]=9920;full[6]=55552;
 full[8]=5079040;full[10]=5079040;full[12]=56885248;full[16]=2080374784ull;
 uint64_t total=0; for(int i=0;i<17;i++)total+=full[i];assert(total==(1ull<<31));
 cout<<"VERIFY_OK_GROUP_ALGEBRA_5\n";
 cout<<"exhaustive_q2_quadratic_cubic=1048576\n";
 cout<<"random_complete_q2=40000\n";
 cout<<"q2_complete_population=2147483648\n";
 return 0;
}
