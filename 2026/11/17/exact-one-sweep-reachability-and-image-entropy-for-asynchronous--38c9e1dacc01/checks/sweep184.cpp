#include <cstdint>
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
static unsigned step(unsigned n,unsigned x){
  vector<unsigned> a(n);
  for(unsigned i=0;i<n;i++) a[i]=(x>>i)&1U;
  for(unsigned i=0;i<n;i++){
    unsigned l=a[(i+n-1)%n],c=a[i],r=a[(i+1)%n];
    a[i]=(l&(!c))|(c&r);
  }
  unsigned y=0;
  for(unsigned i=0;i<n;i++)y|=a[i]<<i;
  return y;
}
static bool language(unsigned n,unsigned w){
  auto y=[&](unsigned i){return (w>>i)&1U;};
  for(unsigned i=0;i<n;i++)if(y(i)&&!y((i+1)%n)&&y((i+2)%n))return false;
  if(y(n-1)&&!y(0))return false;
  if(!y(0)&&y(1)&&y(n-2)&&!y(n-1))return false;
  return true;
}
static unsigned explicit_predecessor(unsigned n,unsigned w){
  auto y=[&](unsigned i){return (w>>i)&1U;};
  if(!language(n,w))throw runtime_error("not reachable");
  vector<unsigned>x(n);
  for(unsigned i=1;i+1<n;i++)x[i]=y(i)|y(i-1);
  if(y(0)){x[0]=1;x[n-1]=y(n-1);}
  else if(!y(n-2)){x[0]=0;x[n-1]=0;}
  else{x[0]=1;x[n-1]=1;}
  unsigned a=0;for(unsigned i=0;i<n;i++)a|=x[i]<<i;
  return a;
}
int main(){
  const int expected[]={0,0,0,3,7,13,22,38,67,118,207,363,637,1118,1962,3443,6042,10603,18607};
  for(unsigned n=3;n<=18;n++){
    unsigned N=1U<<n;
    vector<unsigned char> seen(N,0);
    for(unsigned x=0;x<N;x++)seen[step(n,x)]=1;
    int count=0;
    for(unsigned w=0;w<N;w++){
      bool a=language(n,w),b=seen[w];
      if(a!=b){cerr<<"MISMATCH n="<<n<<" w="<<w<<"\n";return 1;}
      if(a){count++;
        if(step(n,explicit_predecessor(n,w))!=w){cerr<<"CONSTRUCTION FAIL n="<<n<<" w="<<w<<"\n";return 1;}
      }
    }
    if(count!=expected[n]){cerr<<"COUNT FAIL n="<<n<<" count="<<count<<" expected="<<expected[n]<<"\n";return 1;}
    cout<<n<<" "<<count<<" verified\n";
  }
  cout<<"PASS: brute image, language, explicit predecessor n=3..18\n";
}
