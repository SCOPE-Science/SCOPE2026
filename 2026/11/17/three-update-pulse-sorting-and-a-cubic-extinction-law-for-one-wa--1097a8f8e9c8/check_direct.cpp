// Direct synchronous simulation; no symbolic transfer or matrix algebra.
#include <iostream>
#include <vector>
#include <cstdint>
#include <cassert>
#include <algorithm>
using namespace std;
vector<uint8_t> step(const vector<uint8_t>& a){
 int n=a.size(); vector<uint8_t> b(n);
 for(int i=0;i<n;i++){
  if(a[i]==1)b[i]=2;
  else if(a[i]==2)b[i]=0;
  else b[i]=(a[(i+1)%n]==1)?1:0;
 }
 return b;
}
vector<uint8_t> shiftleft(const vector<uint8_t>& a){
 int n=a.size(); vector<uint8_t> b(n);
 for(int i=0;i<n;i++)b[i]=a[(i+1)%n];
 return b;
}
int pulse_count(const vector<uint8_t>& x){
 int c=0,n=x.size();
 for(int i=0;i<n;i++) c += x[i]==1;
 return c;
}
int main(){
 for(int n=3;n<=12;n++){
  int tot=1;for(int i=0;i<n;i++)tot*=3;
  vector<long long> hist(n/3+1,0);
  long long zero=0,last=0;vector<uint8_t> a(n);
  for(int s=0;s<tot;s++){
   int v=s;for(int i=0;i<n;i++){a[i]=v%3;v/=3;}
   auto b=step(a),c=step(b),d=step(c),e=step(d);
   assert(e==shiftleft(d));
   if(d!=shiftleft(c))last++;
   int k=pulse_count(d); assert(k<=n/3);hist[k]++;
   if(k==0){ zero++;assert(all_of(d.begin(),d.end(),[](uint8_t c){return c==0;})); }
   // Every nonzero periodic phase has 1 immediately followed by 2.
   for(int i=0;i<n;i++)if(d[i]==1){
    assert(d[(i+1)%n]==2);
    assert(d[(i+n-1)%n]==0);
    assert(d[(i+2)%n]==0);
   }
  }
  cout<<"n="<<n<<" total="<<tot<<" extinction="<<zero<<" last="<<last<<" hist=";
  for(auto h:hist)cout<<h<<",";
  cout<<" PASS\n";
 }
}
