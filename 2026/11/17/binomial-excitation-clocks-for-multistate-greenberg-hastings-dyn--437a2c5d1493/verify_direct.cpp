// Independent complete-state enumerator for directed Greenberg-Hastings dynamics.
// C++17: g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct
#include <iostream>
#include <vector>
#include <map>
#include <cassert>
using namespace std;
int main(){
 for(int k=3;k<=5;k++) for(int n=1;n<=(k==3?10:k==4?8:7);n++){
  long long total=1;for(int i=0;i<n;i++)total*=k;
  vector<long long> hist(n+k,0);
  for(long long code=0;code<total;code++){
   vector<int> a(n);long long c=code;
   for(int i=0;i<n;i++){a[i]=int(c%k);c/=k;}
   int t=0;
   while(true){
    bool done=true;for(int v:a)if(v!=0){done=false;break;}
    if(done) break;
    bool fire=false;
    vector<int>b(n);
    for(int i=n-1;i>=0;i--){
     b[i]=a[i]==0?(fire?1:0):((a[i]+1)%k);
     if(a[i]==1)fire=true;
    }
    a.swap(b);t++;
    if(t>=n+k){cerr<<"bad termination "<<k<<" "<<n<<"\n";return 1;}
   }
   hist[t]++;
  }
  vector<long long> expected(n+k,0);
  long long p=1;
  for(int t=0;t<=k-2;t++){
    long long pp=1,qq=1;
    for(int i=0;i<n;i++){pp*=t+1;qq*=t;}
    expected[t]=pp-qq;
  }
  long long comb=1;
  for(int b=1;b<=n;b++){
   comb=comb*(n-b+1)/b;
   long long w=1;for(int j=0;j<n-b;j++)w*=k-1;
   expected[b+k-2]=comb*w;
  }
  if(hist!=expected){cerr<<"MISMATCH "<<k<<" "<<n<<"\n";return 1;}
  cout<<"k="<<k<<" n="<<n<<" total="<<total<<" max_time="<<n+k-2<<" max_population="<<hist[n+k-2]<<" histogram=";
  for(int i=0;i<(int)hist.size();i++)if(hist[i])cout<<(i?",":"")<<i<<":"<<hist[i];
  cout<<" PASS\n";
 }
}
