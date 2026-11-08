#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

static void step(const vector<int>& v, int t, vector<int>& out) {
 const int n=(int)v.size(); const int removed=v[0]+(v[0]>=t);
 for(int i=1;i<n;i++) {
  int b=v[i]+(v[i]>=t);
  out[i-1]=b-(b>removed);
 }
 out[n-1]=t-(t>removed);
}

static unsigned long long return3(const vector<int>& v) {
 const int n=(int)v.size();
 vector<int> a(n),b(n),c(n);
 unsigned long long cnt=0;
 for(int t1=1;t1<=n+1;t1++){
  step(v,t1,a);
  for(int t2=1;t2<=n+1;t2++){
   step(a,t2,b);
   for(int t3=1;t3<=n+1;t3++){
    step(b,t3,c);
    if(c==v)cnt++;
   }
  }
 }
 return cnt;
}

static pair<unsigned long long,unsigned long long> calculate(int n){
 vector<int> a(3),v(n),f(n+1),used(n+1),B(3);
 unsigned long long vertices=0,walks=0;
 for(int a0=1;a0<=n;a0++)for(int a1=1;a1<=n;a1++)if(a1!=a0)
 for(int a2=1;a2<=n;a2++)if(a2!=a0 && a2!=a1){
  a={a0,a1,a2};
  for(int b0=1;b0<=n;b0++)if(b0!=a0&&b0!=a1&&b0!=a2)
  for(int b1=b0+1;b1<=n;b1++)if(b1!=a0&&b1!=a1&&b1!=a2)
  for(int b2=b1+1;b2<=n;b2++)if(b2!=a0&&b2!=a1&&b2!=a2){
    B={b0,b1,b2};
    int j=1; fill(f.begin(),f.end(),0);
    for(int i=1;i<=n;i++){
     if(i==b0||i==b1||i==b2)continue;
     while(j==a0||j==a1||j==a2)j++;
     f[i]=j++;
    }
    fill(used.begin(),used.end(),0);
    bool valid=true;
    for(int r=0;r<3 && valid;r++){
      int x=a[r];
      for(int i=r;i<n;i+=3){
        if(x==0 || used[x]){valid=false;break;}
        v[i]=x;used[x]=1;
        if(i+3<n){x=f[x];}else if(f[x]!=0){valid=false;break;}
      }
    }
    if(valid){
      vertices++;
      walks+=return3(v);
    }
  }
 }
 return {vertices,walks};
}
int main(int argc,char**argv){
 int lo=6,hi=12;
 if (argc>1) lo=atoi(argv[1]);
 if (argc>2) hi=atoi(argv[2]);
 if (lo<6 || hi>24 || hi<lo) {
   cerr<<"Certified census range: 6 <= first <= last <= 24\n";
   return 2;
 }
 for(int n=lo;n<=hi;n++){
  auto [v,w]=calculate(n);
  cout<<"n="<<n<<" candidates="<<v<<" closed3="<<w<<" directed3cycles="<<(w-2)/3<<"\n"<<flush;
 }
}
