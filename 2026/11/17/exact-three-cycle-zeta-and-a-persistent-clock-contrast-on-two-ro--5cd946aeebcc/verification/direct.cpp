#include <cstdint>
#include <iostream>
#include <vector>
#include <array>
// Direct three-step simulation of the original local Greenberg--Hastings rule.
// State indices (2*i+r) on a 2-by-n periodic Moore grid.
static void step(const std::vector<uint8_t>& x,std::vector<uint8_t>& y,int n){
 for(int i=0;i<n;i++) for(int r=0;r<2;r++) {
  int c=x[2*i+r];
  if(c!=0) {y[2*i+r]=(c+1)%3;continue;}
  int prev=(i+n-1)%n,next=(i+1)%n;
  bool one=(x[2*i+(1-r)]==1);
  for(int j:{prev,next}) for(int rr=0;rr<2;rr++)
    if(x[2*j+rr]==1)one=true;
  y[2*i+r]=one?1:0;
 }
}
int main(){
 for(int n=3;n<=6;n++){
  int m=2*n; uint64_t size=1;
  for(int i=0;i<m;i++)size*=3;
  uint64_t fix=0, third=0;
  std::vector<uint8_t> x(m),a(m),b(m),c(m);
  for(uint64_t idx=0;idx<size;idx++){
   uint64_t code=idx;
   for(int i=0;i<m;i++){x[i]=code%3;code/=3;}
   step(x,a,n);
   if(x==a)fix++;
   step(a,b,n);step(b,c,n);
   if(x==c)third++;
  }
  std::cout << "n=" << n << " total="<<size << " fixed=" <<fix
            << " third_return=" <<third << " primitive_orbits="<<(third-fix)/3 << '\n';
 }
}
