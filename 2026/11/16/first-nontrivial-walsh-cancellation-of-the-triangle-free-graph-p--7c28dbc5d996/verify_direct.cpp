// Self-contained exact-integer enumeration and Walsh check for triangle-free graphs.
// Compile with: g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct
#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <cstdlib>
#include <numeric>
#include <cstdint>
#include <cassert>
#include <climits>
using namespace std;
static vector<long long> fft(vector<long long> a){
  for(size_t h=1;h<a.size();h*=2)
    for(size_t b=0;b<a.size();b+=2*h)
      for(size_t i=b;i<b+h;i++){
        auto x=a[i],y=a[i+h];a[i]=x+y;a[i+h]=x-y;
      }
  return a;
}
static vector<long long> graph_walsh(int n){
  vector<pair<int,int>> e;for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)e.push_back({a,b});
  int m=(int)e.size(),N=1<<m;vector<int> tri;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++){
    int t=0;for(int j=0;j<m;j++)if(e[j]==pair<int,int>(a,b)||e[j]==pair<int,int>(a,c)||e[j]==pair<int,int>(b,c))t|=1<<j;
    assert(__builtin_popcount((unsigned)t)==3);tri.push_back(t);
  }
  vector<long long> f(N,1);
  for(int g=0;g<N;g++)for(int t:tri)if((g&t)==t){f[g]=0;break;}
  return fft(f);
}
int main(){
  for(int n=3;n<=6;n++){
    vector<long long> w=graph_walsh(n);
    long long count=(n==3?7:n==4?41:n==5?388:5789);
    assert(w[0]==count);
    long long energy=0;for(auto x:w)energy+=x*x;
    assert(energy==(long long)w.size()*count);
    size_t zero=0;long long gap=LONG_LONG_MAX;
    for(auto x:w){if(x==0)zero++;else gap=min(gap,llabs(x));}
    if(n!=5){assert(zero==0);assert(gap==1);}else{
      assert(zero==150);assert(gap==2);
      map<int,int> hist,zeroweights;
      for(int s=0;s<(int)w.size();s++){
        hist[(int)w[s]]++;
        if(w[s]==0)zeroweights[__builtin_popcount((unsigned)s)]++;
      }
      const vector<pair<int,int>> ref={
        {-26,20},{-22,60},{-20,5},{-12,60},{-10,20},{-8,90},{-6,60},{-4,20},{-2,40},{0,150},
        {2,160},{4,91},{6,72},{8,70},{10,30},{14,30},{16,10},{44,15},{46,10},{106,10},{388,1}};
      bool histogram_ok=(vector<pair<int,int>>(hist.begin(),hist.end())==ref);assert(histogram_ok);
      bool weights_ok=(zeroweights==map<int,int>({{6,120},{8,30}}));assert(weights_ok);
      vector<long long> support(w.size());
      for(size_t i=0;i<w.size();i++)support[i]=w[i]!=0;
      auto kernel=fft(support);
      long long l1=0;for(auto x:kernel)l1+=llabs(x);
      assert(l1==7924);
      assert(kernel[0]==874);
      cout << "n=5: total="<<count<<" zero="<<zero<<" rank="<<kernel[0]<<" gap="<<gap<<" endpoint=7924/1024\n";
    }
  }
  cout<<"PASS direct FWHT: all four graph sizes, full 21-level signed spectrum, first zeros, range-projection norm, Parseval.\n";
}
