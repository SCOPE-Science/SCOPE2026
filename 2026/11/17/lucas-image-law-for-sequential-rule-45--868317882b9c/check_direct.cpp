// Reproducible direct image census for sequential elementary Rule 45.
#include <cstdint>
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
static uint32_t sweep(uint32_t v, int n) {
  for (int i=0; i<n; ++i) {
    int l=(v>>((i+n-1)%n))&1, c=(v>>i)&1, r=(v>>((i+1)%n))&1;
    int f=(45>>((l<<2)|(c<<1)|r))&1;
    v=(v & ~(uint32_t(1)<<i)) | (uint32_t(f)<<i);
  }
  return v;
}
static bool predicted(uint32_t y, int n) {
  int b=y&1;
  int q=((y>>(n-1))^(y>>(n-2)))&1;
  bool first=false,last=false,prev=false;
  for(int i=1;i<=n-2;++i){
    bool m=(((y>>i)^(y>>(i-1)))&1)==0;
    if (m&&prev) return false;
    if(i==1)first=m;
    if(i==n-2)last=m;
    prev=m;
  }
  return b==0 ? q==1 : (q==0 ? !last : !first);
}
int main(){
  for(int n=3;n<=20;++n){
    uint32_t N=uint32_t(1)<<n;
    vector<uint8_t> reachable(N,0);
    for(uint32_t x=0;x<N;++x)reachable[sweep(x,n)]=1;
    uint64_t count=0;
    for(uint32_t y=0;y<N;++y){
      if(reachable[y]!=predicted(y,n)) throw runtime_error("language mismatch");
      count+=reachable[y];
    }
    uint64_t a=2,b=1;for(int j=2;j<=n;++j){auto t=a+b;a=b;b=t;}
    if(count!=b)throw runtime_error("Lucas mismatch");
    cout << n << " " << count << " " << (N-count) << "\n";
  }
  cout << "DIRECT_CENSUS_PASS\n";
}
