#include <bits/stdc++.h>
using namespace std;
int main(){for(int m=2;m<=8;m++){int n=2*m,N=n+m; uint64_t tot=1ull<<N, fixed=0, p2=0, steps[15]={0};auto F=[&](uint32_t v){uint32_t r=0; for(int i=0;i<n;i++){int l=(v>>((i+n-1)%n))&1, a=(v>>i)&1, b=(v>>((i+1)%n))&1;int x;if(i%2==0){int leaf=(v>>(n+i/2))&1; x=(l+b+leaf)>=2;}else x=l+b==1?a:l; r|=x<<i;}for(int j=0;j<m;j++){r|=((v>>(2*j))&1)<<(n+j);}return r;};for(uint32_t x=0;x<tot;x++){uint32_t y=F(x);if(y==x)fixed++;if(F(y)==x)p2++;}cout<<m<<" "<<tot<<" "<<fixed<<" "<<p2<<" "<<(p2-fixed)/2<<"\n";} }
