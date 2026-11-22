// Exact finite checks for zero-diagonal binary invertible matrices.
// C++17: g++ -std=c++17 -O2 CHECKER.cpp -o checker && ./checker
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
int rankGF2(int n,int rows[5]) {
  int r=0;
  for(int j=0;j<n;j++){
    int k=r;
    while(k<n && ((rows[k]>>j)&1)==0)++k;
    if(k==n)continue;
    swap(rows[r],rows[k]);
    for(int i=r+1;i<n;i++)if((rows[i]>>j)&1)rows[i]^=rows[r];
    ++r;
  }
  return r;
}
int main(){
  const long long expected[6]={0,0,1,14,984,267968};
  for(int n=2;n<=5;n++){
    int m=n*(n-1),N=1<<m;
    vector<pair<int,int>> c;
    for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j)c.emplace_back(i,j);
    vector<int> a(N,0);
    int members=0;
    for(int z=0;z<N;z++){
      int rows[5]={0,0,0,0,0};
      for(int b=0;b<m;b++)if((z>>b)&1)rows[c[b].first]|=1<<c[b].second;
      a[z]=(rankGF2(n,rows)==n);
      members+=a[z];
    }
    if(members!=expected[n])return 1;
    for(int t=1;t<N;t<<=1)
      for(int z=0;z<N;z+=2*t)
        for(int j=0;j<t;j++){
          int x=a[z+j],y=a[z+t+j];
          a[z+j]=x+y;a[z+t+j]=x-y;
        }
    int e=(n-1)*(n-2)/2,mod=1<<(e+1),want=1<<e;
    int zeros=0,mn=100000000;
    for(int a0:a){
      if((a0%mod+mod)%mod != want)return 2;
      if(!a0)zeros++;
      else mn=min(mn,abs(a0));
    }
    if(zeros!=0 || mn!=want)return 3;
    cout<<"n="<<n<<" |D|="<<members<<" characters="<<N<<" zeros="<<zeros
        <<" valuation="<<e<<" minimum_abs="<<mn<<" PASS\n";
  }
}
