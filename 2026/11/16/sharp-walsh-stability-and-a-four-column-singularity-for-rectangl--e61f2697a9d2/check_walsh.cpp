#include <algorithm>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
// Exact integer Walsh verification for incidence vectors of C4-free K_{3,n}.
static const int PAIR_MASK[8]={0,0,0,1,0,2,4,7};
void enumerate(int n,int j,int mask,int used,vector<long long>& f) {
  if(j==n){f[mask]=1;return;}
  for(int col=0;col<8;++col) {
    if(PAIR_MASK[col]&used) continue;
    enumerate(n,j+1,mask | (col <<(3*j)),used|PAIR_MASK[col],f);
  }
}
long long w_signs(const vector<int>& frequency_types) {
  long long state[8]={1,0,0,0,0,0,0,0};
  for(int sign:frequency_types){
    long long next[8]={0,0,0,0,0,0,0,0};
    for(int used=0;used<8;++used)
      for(int col=0;col<8;++col)
        if((PAIR_MASK[col]&used)==0)
          next[used|PAIR_MASK[col]]+=((__builtin_popcount((unsigned)(sign&col))%2)?-1:1)*state[used];
    for(int k=0;k<8;++k)state[k]=next[k];
  }
  long long result=0;for(int x:state)result+=x;return result;
}
int main(){
  const long long want_card[6]={54,334,1952,10944,59392,313856};
  const long long want_zeros[6]={0,0,621,3138,58788,551862};
  const long long want_min[6]={2,2,4,8,16,32};
  for(int n=2;n<=7;++n){
    const size_t size=size_t(1)<<(3*n);
    vector<long long> a(size,0);
    enumerate(n,0,0,0,a);
    long long card=0; for(long long x:a)card+=x;
    assert(card==want_card[n-2]);
    for(size_t step=1;step<size;step*=2)
      for(size_t i=0;i<size;i+=2*step)
        for(size_t j=0;j<step;++j){
           const long long u=a[i+j],v=a[i+j+step];
           a[i+j]=u+v;a[i+j+step]=u-v;
        }
    assert(a[0]==card);
    long long zeros=0,minimum=card,parseval=0;
    for(long long x:a){
       if(x==0) ++zeros;
       else minimum=min(minimum, llabs(x));
       parseval+=x*x;
       if(n<=3)assert(x%4==2 || x%4==-2);
       if(n>=3)assert(x% (1LL<<(n-2)) ==0);
    }
    assert(parseval==(long long)size*card);
    assert(zeros==want_zeros[n-2] && minimum==want_min[n-2]);
    vector<int> witness;
    if(n==2) witness={3,3};
    else{witness.assign(n-3,1);witness.insert(witness.end(),{3,3,5});}
    assert(w_signs(witness)==-minimum);
    if(n>=4)assert(w_signs(vector<int>(n,3))==0);
    cout<<"n="<<n<<" count="<<card<<" zero="<<zeros<<" gap="<<minimum<<" PASS\n";
  }
  cout<<"C4FREE_WALSH_ALL_CHECKS_PASS\n";
}