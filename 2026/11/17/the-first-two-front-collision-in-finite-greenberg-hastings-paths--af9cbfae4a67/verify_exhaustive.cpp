#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
#include <cassert>
using namespace std;
static uint64_t factorial(int n){uint64_t a=1;for(int i=2;i<=n;i++)a*=i;return a;}
static bool allzero(const vector<int>&x){for(int a:x)if(a)return false;return true;}
int main(){
 for(int n=4;n<=8;n++){
  int q=n-1;uint64_t total=1;for(int i=0;i<n;i++)total*=q;
  vector<int> x(n),y(n);uint64_t maximal=0,ones=0,twos=0;
  vector<uint64_t> hist(n+1,0);
  for(uint64_t mask=0;mask<total;mask++){
   uint64_t z=mask;int initial_ones=0,refractory=0;
   for(int j=0;j<n;j++){x[j]=z%q;z/=q;initial_ones+=(x[j]==1);refractory+=(x[j]>=2);}
   int t=0;
   while(!allzero(x)){
    for(int j=0;j<n;j++)y[j]=x[j]?((x[j]+1)%q):(((j>0&&x[j-1]==1)||(j+1<n&&x[j+1]==1))?1:0);
    x.swap(y);t++;
    if(t>n+q-2){cerr<<"extinction bound failed"<<endl;return 1;}
   }
   if(t==n+q-2){maximal++;ones+=(initial_ones==1);twos+=(initial_ones==2);hist[refractory]++;if(initial_ones!=1&&initial_ones!=2){cerr<<"wrong source count";return 1;}}
  }
  uint64_t pred=2*(factorial(n-1)-factorial(n-3));
  uint64_t p1=2*(n-2)*factorial(n-2),p2=2*(n-3)*factorial(n-3);
  cout<<"q=n-1 n="<<n<<" q="<<q<<" states="<<total<<" max="<<maximal<<" one="<<ones<<" two="<<twos<<" hist=";
  for(int i=0;i<=n;i++)if(hist[i])cout<<i<<":"<<hist[i]<<",";
  cout<<" expected="<<pred<<"\n";
  if(maximal!=pred||ones!=p1||twos!=p2){cerr<<"formula mismatch"<<endl;return 1;}
 }
 cout<<"PASS exhaustive; all tested states reached rest within bound\n";
}
