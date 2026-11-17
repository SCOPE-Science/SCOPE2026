// Exhaustive original two-stage east-then-north BML dynamics on labelled 3 x n tori.
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main() {
 for (int n=3;n<=5;n++) {
  int k=3*n; uint64_t total=1; for(int i=0;i<k;i++) total*=3;
  uint64_t fixed=0;
  vector<uint8_t> a(k),b(k),c(k);
  for(uint64_t s=0;s<total;s++) {
   uint64_t t=s;
   for(int i=0;i<k;i++){a[i]=t%3;t/=3;}
   b=a;
   for(int r=0;r<3;r++) for(int j=0;j<n;j++) {
    int i=r*n+j, e=r*n+(j+1)%n;
    if(a[i]==1 && a[e]==0) { b[i]=0;b[e]=1; }
   }
   c=b;
   for(int r=0;r<3;r++) for(int j=0;j<n;j++) {
    int i=r*n+j, u=((r+1)%3)*n+j;
    if(b[i]==2 && b[u]==0) { c[i]=0;c[u]=2; }
   }
   if(c==a) fixed++;
  }
  cout << "n "<<n<<" direct_fixed "<<fixed<<" total "<<total<<"\n";
  uint64_t target=(n==3?1686:n==4?19988:237828);
  if (fixed!=target) return 1;
 }
}
