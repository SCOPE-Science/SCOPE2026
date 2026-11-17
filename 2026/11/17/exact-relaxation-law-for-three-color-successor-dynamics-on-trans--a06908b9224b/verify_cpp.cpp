// Independent integer-only verification with ternary bitpacked arrays.
#include <iostream>
#include <vector>
#include <array>
#include <cassert>
using namespace std;
static int T(int n,long long code){
    array<int,13> x{},y{};
    for(int i=0;i<n;i++){x[i]=int(code%3);code/=3;}
    for(int t=0;t<=n;t++){
      bool moved=false;
      for(int i=0;i<n;i++){
        bool seen=false;
        for(int j=i+1;j<n;j++) if(x[j]==(x[i]+1)%3){seen=true;break;}
        y[i]=(x[i]+(seen?1:0))%3;
        if(y[i]!=x[i])moved=true;
      }
      if(!moved) return t;
      x=y;
    }
    return -1;
}
int main(){
    for(int n=1;n<=11;n++){
       long long count=1;for(int i=0;i<n;i++) count*=3;
       vector<long long> H(n+1,0);
       for(long long j=0;j<count;j++){
         int t=T(n,j);assert(t>=0 && t<n);H[t]++;
       }
       vector<long long> exp(1,3);
       for(int m=2;m<=n;m++){
         vector<long long> next(m,0);
         for(int k=0;k<m-1;k++){next[k]+=2*exp[k];next[k+1]+=exp[k];}
         if(m>=3){next[0]-=3LL*(m-2);next[2]+=3LL*(m-2);}
         exp=next;
       }
       for(int k=0;k<n;k++) assert(H[k]==exp[k]);
       cout<<"n="<<n<<" states="<<count<<" max_depth="<<n-1
           <<" max_depth_population="<<H[n-1]<<" fixed="<<H[0]<<" :";
       for(int k=0;k<n;k++) cout<<" "<<H[k];
       cout<<"\n";
    }
    cout<<"PASS: independent C++ exhaustive state sweeps through n=11"<<endl;
}
