#include <bits/stdc++.h>
using namespace std;
int main(){for(int n=2;n<=7;n++){
 int N=3*n;vector<int> nb(N,0),deg(N,0);
 for(int c=0;c<n;c++)for(int r=0;r<3;r++){int i=3*c+r;
 for(int s=0;s<3;s++)if(s!=r) nb[i]|=1<<(3*c+s);
 if(c>0)nb[i]|=1<<(3*(c-1)+r);
 if(c+1<n)nb[i]|=1<<(3*(c+1)+r);
 deg[i]=__builtin_popcount((unsigned)nb[i]);}
 auto F=[&](int x){int y=0;for(int i=0;i<N;i++){
 int a=__builtin_popcount((unsigned)(x&nb[i]));
 if(2*a>deg[i] || (2*a==deg[i] && (x>>i&1)))y|=1<<i;
 }return y;};
 uint64_t fix=0,periodic=0,flipall=0,partflip=0;vector<int> classflip(N+1,0);
 for(int x=0;x<(1<<N);x++) {int y=F(x);if(F(y)==x){periodic++;if(y==x)fix++;else{int k=__builtin_popcount((unsigned)(y^x)); classflip[k]++;if(k==N)flipall++;else partflip++;}}}
 cout<<"n "<<n<<" fixed "<<fix<<" periodic "<<periodic<<" primitive2 "<<periodic-fix<<" allflip "<<flipall<<" partflip "<<partflip<<" byflips ";for(int i=1;i<=N;i++)if(classflip[i])cout<<i<<":"<<classflip[i]<<" ";cout<<"\n";
 }}
