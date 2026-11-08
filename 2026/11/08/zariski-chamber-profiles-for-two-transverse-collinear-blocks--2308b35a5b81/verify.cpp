// Exact integer check of negative-definite support counts for two-line plane blowups.
// Compile: c++ -O3 -std=c++17 check.cpp -o check && ./check
#include <bits/stdc++.h>
using namespace std;
struct Curve {int type,i,j;}; // types: 0=A exceptional,1=B exceptional,2=A line,3=B line,4=connector
long long cmb(int n,int k){if(k<0||k>n)return 0;long long t=1;for(int j=1;j<=k;j++)t=t*(n-j+1)/j;return t;}
long long choose_poly(int N,int k){return cmb(N,k);}
vector<Curve> make(int n,int m){vector<Curve> a;for(int i=0;i<n;i++)a.push_back({0,i,-1});for(int j=0;j<m;j++)a.push_back({1,j,-1});a.push_back({2,0,0});a.push_back({3,0,0});for(int i=0;i<n;i++)for(int j=0;j<m;j++)a.push_back({4,i,j});return a;}
int intersection(const Curve &a,const Curve &b,int n,int m){
 if(a.type==0 && b.type==0)return a.i==b.i?-1:0;
 if(a.type==1 && b.type==1)return a.i==b.i?-1:0;
 if(a.type==0 && b.type==1 || a.type==1 && b.type==0)return 0;
 if(a.type==0 && b.type==2 || a.type==2 && b.type==0)return 1;
 if(a.type==1 && b.type==3 || a.type==3 && b.type==1)return 1;
 if(a.type==0 && b.type==3 || a.type==3 && b.type==0)return 0;
 if(a.type==1 && b.type==2 || a.type==2 && b.type==1)return 0;
 if(a.type==0 && b.type==4)return a.i==b.i;
 if(a.type==4 && b.type==0)return a.i==b.i;
 if(a.type==1 && b.type==4)return a.i==b.j;
 if(a.type==4 && b.type==1)return a.j==b.i;
 if(a.type==2 && b.type==2)return 1-n;
 if(a.type==3 && b.type==3)return 1-m;
 if(a.type==2 && b.type==3 || a.type==3 && b.type==2)return 1;
 if(a.type==2 && b.type==4 || a.type==4 && b.type==2)return 0;
 if(a.type==3 && b.type==4 || a.type==4 && b.type==3)return 0;
 if(a.type==4 && b.type==4){if(a.i==b.i && a.j==b.j)return -1; return a.i==b.i||a.j==b.j?0:1;}
 cerr<<"bad type pair";exit(2);
}
// Exact Bareiss positive-definiteness of negative intersection matrix. No numeric tolerances.
bool negdef(const vector<Curve>& a, uint64_t mask,int n,int m){
 int idx[40],k=0;for(int i=0;i<(int)a.size();i++)if((mask>>i)&1)idx[k++]=i;
 long long mat[40][40];for(int i=0;i<k;i++)for(int j=0;j<k;j++)mat[i][j]=-intersection(a[idx[i]],a[idx[j]],n,m);
 long long prev=1;
 for(int p=0;p<k;p++){
  long long pivot=mat[p][p];if(pivot<=0)return false;
  if(p==k-1)break;
  for(int i=p+1;i<k;i++)for(int j=p+1;j<k;j++){
   __int128 z=(__int128)pivot*mat[i][j]-(__int128)mat[i][p]*mat[p][j];
   if(z%prev!=0){cerr<<"not divisible\n";exit(2);}
   z/=prev;
   if(z>LLONG_MAX||z<LLONG_MIN){cerr<<"overflow\n";exit(2);}
   mat[i][j]=(long long)z;
  }
  prev=pivot;
 }
 return true;
}
using Profile=array<vector<long long>,4>;
Profile formula_profile(int n,int m){
 Profile out;
 for(auto &v:out)v.assign(n+m+3,0);
 auto add=[&](int edgecount,int usedA,int usedB,long long mult){
  int na=n-usedA,mb=m-usedB;
  for(int ka=0;ka<=na;ka++)for(int kb=0;kb<=mb;kb++){
   long long ways=mult*cmb(na,ka)*cmb(mb,kb);
   int base=edgecount+ka+kb;
   out[0][base]+=ways;
   if(ka<=n-2)out[1][base+1]+=ways;
   if(kb<=m-2)out[2][base+1]+=ways;
   if(ka<=n-2 && kb<=m-2 && (ka<n-2||kb<m-2))out[3][base+2]+=ways;
  }
 };
 add(0,0,0,1);
 add(1,1,1,1LL*n*m);
 for(int r=2;r<=m;r++)add(r,1,r,1LL*n*cmb(m,r));
 for(int r=2;r<=n;r++)add(r,r,1,1LL*m*cmb(n,r));
 return out;
}
int main(){for(auto [n,m]:vector<pair<int,int>>{{3,3},{3,4}}){
 auto curves=make(n,m);int total=curves.size();uint64_t count=1ULL<<total;Profile hist;
 for(auto &v:hist)v.assign(n+m+3,0);
 for(uint64_t b=0;b<count;b++)if(negdef(curves,b,n,m)){
  int aa=(b>>(n+m))&1,bb=(b>>(n+m+1))&1;
  hist[aa+2*bb][__builtin_popcountll(b)]++;
 }
 auto pred=formula_profile(n,m);if(hist!=pred){cerr<<"MISMATCH n="<<n<<" m="<<m<<"\n";return 1;}
 cout<<"n="<<n<<" m="<<m<<" curves="<<total<<" exhaustive_subsets="<<count<<"\n";
 for(int q=0;q<4;q++){
  cout<<"distinguished_lines="<<((q&1)?"A":"-")<<((q&2)?"B":"-")<<" coefficients=";
  for(int j=0;j<(int)hist[q].size();j++)if(hist[q][j])cout<<j<<":"<<hist[q][j]<<",";
  cout<<"\n";
 }
 long long sum=0;for(auto&v:hist)sum+=accumulate(v.begin(),v.end(),0LL);
 cout<<"total="<<sum<<" PASS\n";
 }
 cout<<"ALL_CHECKS_PASSED\n";
}
