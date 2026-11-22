// Independent exhaustive verifier for synchronous open-neighbourhood NOR on L(K_n).
// Compile: g++ -O3 -std=c++17 nor_independent.cpp -o nor_independent
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
using U=uint64_t;
U factorial(int n){U v=1;for(int i=2;i<=n;++i)v*=i;return v;}
U choose(int n,int k){if(k<0||k>n)return 0;return factorial(n)/(factorial(k)*factorial(n-k));}
vector<U> clean(int N){
 vector<U> b(N+1),a(N+1);b[0]=1;
 for(int n=1;n<=N;++n)b[n]=b[n-1]+(n>1?(n-1)*b[n-2]:0);
 for(int n=0;n<=N;++n){
   U total=U(1)<<choose(n,2),loss=0;
   for(int j=1;j<=n;++j)loss+=choose(n,j)*b[j]*a[n-j];
   a[n]=total-loss;
 }
 return a;
}
struct Case{
 int n,m;vector<pair<int,int>> edges;vector<U> nb;int idx[8][8]{};vector<U> a;
 map<U,U> expected,observed;
 Case(int N):n(N),m(N*(N-1)/2),a(clean(N)){
  for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){
    idx[i][j]=idx[j][i]=int(edges.size());edges.push_back({i,j});
  }
  for(int k=0;k<m;++k){U mask=0;auto [u,v]=edges[k];
   for(int h=0;h<m;++h){auto [a,b]=edges[h];if(k!=h&&(u==a||u==b||v==a||v==b))mask|=U(1)<<h;}
   nb.push_back(mask);
  }
 }
 U F(U x)const{U y=0;for(int i=0;i<m;++i)if((x&nb[i])==0)y|=U(1)<<i;return y;}
 U clq(const vector<int>& v)const{U x=0;for(int i=0;i<int(v.size());++i)for(int j=i+1;j<int(v.size());++j)x|=U(1)<<idx[v[i]][v[j]];return x;}
 U key(U x,U y)const{if(x>y)swap(x,y);return(x<<m)|y;}
 void add_expected(U M, int matched_edges, const vector<int>& R){
  int r=int(R.size());
  if(r<=1){expected[key(M,M)]=(r==0?matched_edges+1:1);return;}
  if(r==2)return;
  U Q=M|clq(R);
  expected[key(M,Q)]=1+(matched_edges+1)*a[r]+r*a[r-1];
  for(int mask=0;mask<(1<<(r-1));++mask){
   vector<int>A{R[0]},B;
   for(int i=1;i<r;++i)((mask>>(i-1))&1 ? A:B).push_back(R[i]);
   if(A.size()>=3 && B.size()>=3)expected[key(M|clq(A),M|clq(B))]=a[A.size()]+a[B.size()];
  }
 }
 void enumerate(int pos,int used,U match,int matched_edges){
  while(pos<n&&(used&(1<<pos)))++pos;
  if(pos==n){vector<int>R;for(int i=0;i<n;++i)if(!(used&(1<<i)))R.push_back(i);
   add_expected(match,matched_edges,R);return;}
  enumerate(pos+1,used,match,matched_edges);
  for(int j=pos+1;j<n;++j)if(!(used&(1<<j)))
   enumerate(pos+1,used|(1<<pos)|(1<<j),match|(U(1)<<idx[pos][j]),matched_edges+1);
 }
 void run(){
  enumerate(0,0,0,0);
  U states=U(1)<<m;
  for(U x=0;x<states;++x){
   U y=F(x),z=F(y);
   if(F(z)!=y){cerr<<"one-step identity failure "<<n<<" "<<x<<"\n";exit(2);}
   ++observed[key(y,z)];
  }
  if(expected!=observed){
   cerr<<"mismatch at n="<<n<<" predicted="<<expected.size()<<" actual="<<observed.size()<<"\n";
   for(auto [k,v]:expected)if(observed[k]!=v){cerr<<"first mismatch key="<<k<<" expected="<<v<<" actual="<<observed[k]<<"\n";break;}
   exit(3);
  }
  int fixed=0;for(auto [k,v]:expected)if((k>>m)==(k&((U(1)<<m)-1)))fixed++;
  U distinguished=expected[key(0,states-1)];
  cout<<"PASS n="<<n<<" states="<<states<<" fixed="<<fixed<<" two_cycles="<<expected.size()-fixed
      <<" distinguished_basin="<<distinguished<<" all_individual_basins_verified\n";
 }
};
int main(){for(int n=3;n<=7;++n){Case c(n);c.run();}}
