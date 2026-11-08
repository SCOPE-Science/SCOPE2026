#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
using namespace std;
static int mod(int x, int q) {x%=q;return x<0?x+q:x;}
int main(){
  for(int q: {3}){
    int N=1;for(int i=0;i<4;++i)N*=q;
    vector<array<int,4>> vec(N);for(int a=0;a<N;++a){int t=a;for(int i=0;i<4;++i){vec[a][i]=t%q;t/=q;}}
    int Q7=1;for(int i=0;i<7;++i)Q7*=q;
    vector<uint64_t> spectrum(Q7,0);
    {
      int Q8=N*N;
      for(int a=0;a<Q8;++a){auto u=vec[a%N],al=vec[a/N];
        for(int b=0;b<Q8;++b){auto v=vec[b%N],be=vec[b/N];
          int co[7];int k=0;
          for(int i=0;i<4;++i)for(int j=i+1;j<4;++j)co[k++]=mod(2*(u[i]*v[j]-u[j]*v[i]),q);
          int t=u[0]*be[3]-u[1]*be[2]+u[2]*be[1]-u[3]*be[0]
                +al[0]*v[3]-al[1]*v[2]+al[2]*v[1]-al[3]*v[0];
          co[6]=mod(2*t,q);
          int idx=0,factor=1;for(int j=0;j<7;++j){idx+=co[j]*factor;factor*=q;}
          ++spectrum[idx];
        }
      }
      uint64_t zero=(uint64_t)q*q*q*q*q*q*q*q;
      zero+=(uint64_t)(N-1)*(q+1)*q*q*q*q*q*q*q;
      uint64_t Zother=(uint64_t)(N-1)*(q+1)*q*q*q*q*q*q*q;
      uint64_t nonzero=(uint64_t)q*q*q*q*q*q*q*q*(q*q-1);
      uint64_t num0=0,numz=0,numd=0,numabs=0;
      for(int i=0;i<Q7;++i){
        int digits[7];int tmp=i;for(int j=0;j<7;++j){digits[j]=tmp%q;tmp/=q;}
        bool gammaZero=true;for(int j=0;j<6;++j)if(digits[j]!=0)gammaZero=false;
        int pf=mod(digits[0]*digits[5]-digits[1]*digits[4]+digits[2]*digits[3],q);
        uint64_t expected=pf!=0?0:(gammaZero?(digits[6]==0?zero:Zother):nonzero);
        uint64_t x=spectrum[i];
        if(x!=expected){cerr<<"value "<<i<<" fiber mismatch got="<<x<<" expected="<<expected<<"\n";return 1;}
        if(gammaZero&&digits[6]==0)++num0;
        else if(gammaZero)++numz;
        else if(pf==0)++numd;
        else ++numabs;
      }
      uint64_t decomp=(uint64_t)(q-1)*(q*q+1)*(q*q+q+1);
      if(numz!=q-1||numd!=decomp*q||numabs!=Q7-1-numz-numd){cerr<<"distribution mismatch\n";return 1;}
      cout<<"q="<<q<<" odd-pair brute checks="<<(uint64_t)Q8*Q8<<" codomain="<<Q7<<" fibers 0="<<num0<<" axial="<<numz<<" Plucker="<<numd<<" absent="<<numabs<<" VERIFY_OK\n";
    }
  }
}
