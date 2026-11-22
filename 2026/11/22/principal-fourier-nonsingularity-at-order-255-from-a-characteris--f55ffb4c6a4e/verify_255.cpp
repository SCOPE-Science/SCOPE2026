// Exact finite-field certificate for all principal minors of the 15-point Fourier matrix.
// Build: c++ -O3 -std=c++17 verify_255.cpp -o verify255
// Run: ./verify255
#include <array>
#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;
constexpr int P=17,Q=83521,N=15;
// F_17[t]/(t^4+3); elements are base-17 digit vectors.
inline int add(int a,int b){int out=0,scale=1;for(int i=0;i<4;++i){int x=(a%P+b%P)%P;out+=x*scale;scale*=P;a/=P;b/=P;}return out;}
inline int neg(int a){int out=0,scale=1;for(int i=0;i<4;++i){int x=(P-a%P)%P;out+=x*scale;scale*=P;a/=P;}return out;}
inline int mul(int a,int b){int x[4],y[4],c[7]={};for(int i=0;i<4;++i){x[i]=a%P;y[i]=b%P;a/=P;b/=P;}for(int i=0;i<4;++i)for(int j=0;j<4;++j)c[i+j]+=x[i]*y[j];for(int i=6;i>=4;--i)c[i-4]-=3*c[i];int out=0,scale=1;for(int i=0;i<4;++i){int v=((c[i]%P)+P)%P;out+=v*scale;scale*=P;}return out;}
int fpow(int a,int k){int out=1;while(k){if(k&1)out=mul(out,a);a=mul(a,a);k>>=1;}return out;}
int main(){
  // Validate the presentation is a field by establishing t^4+3 irreducible:
  // since F17 has 4th roots of unity, t^4+3 is irreducible iff -3
  // has multiplicative order 16 in F17 (binomial criterion).
  // Here -3=14 and 14^8=-1 mod17, hence order 16.
  if(fpow(14,8)!=16 || fpow(14,16)!=1){puts("FAIL: binomial field test");return 1;}
  // Search an exact primitive 15th root, automatically checking its order.
  int root=0;
  for(int a=2;a<Q&&!root;++a){int r=fpow(a,(Q-1)/15);if(r!=1&&fpow(r,15)==1&&fpow(r,3)!=1&&fpow(r,5)!=1)root=r;}
  if(!root){puts("FAIL: no primitive root");return 1;}
  for(int exponent : {1,7}){
  int omega[N];omega[0]=1;int target=fpow(root,exponent);for(int i=1;i<N;++i)omega[i]=mul(omega[i-1],target);
  if(mul(omega[N-1],target)!=1){puts("FAIL: root check");return 1;}
  // Division-free Laplace recursion: dp[T] is determinant of the first
  // |T| selected rows against the selected columns indexed by T.
  int missing=0;array<int,N+1> checked={};
  for(int mask=1;mask<(1<<N);++mask){
    int rows[N],k=0;for(int i=0;i<N;++i)if(mask&(1<<i))rows[k++]=i;
    vector<int> dp(1<<k,0);dp[0]=1;
    for(int T=1;T<(1<<k);++T){
      int t=__builtin_popcount((unsigned)T),j=0,v=0;
      for(int c=0;c<k;++c)if(T&(1<<c)){
        int z=mul(omega[(rows[t-1]*rows[c])%N],dp[T^(1<<c)]);
        if(((t-1+j)&1)==1)z=neg(z);
        v=add(v,z);++j;
      }
      dp[T]=v;
    }
    if(dp[(1<<k)-1]==0){missing++;printf("FAIL: zero determinant mask=%d size=%d\n",mask,k);break;}
    checked[k]++;
  }
  if(missing)return 1;
  printf("PASS: exponent=%d, 32767 nonempty principal minors nonzero in F_17^4; root=%d; counts:",exponent,root);
  for(int i=1;i<=15;++i)printf(" %d",checked[i]);
  puts("");
  }
  return 0;
}
