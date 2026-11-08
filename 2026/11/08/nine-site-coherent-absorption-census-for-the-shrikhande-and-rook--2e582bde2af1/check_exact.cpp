#include <bits/stdc++.h>
using namespace std;using ll=long long;using i128=__int128_t;
int exact_psd_rank(vector<vector<ll>> a){
  int n=a.size(),r=0;ll previous=1;
  for(int k=0;k<n;k++){
    int p=k;while(p<n && a[p][p]==0)p++;
    if(p==n) return r;
    if(a[p][p]<0)throw runtime_error("not PSD");
    if(p!=k){swap(a[p],a[k]);for(auto &row:a)swap(row[p],row[k]);}
    ll pivot=a[k][k];
    for(int i=k+1;i<n;i++)for(int j=k+1;j<n;j++){
      i128 value=i128(a[i][j])*pivot-i128(a[i][k])*a[k][j];
      if(value%previous!=0)throw runtime_error("non-exact division");
      value/=previous;
      if(value>LLONG_MAX||value<LLONG_MIN)throw runtime_error("overflow");
      a[i][j]=(ll)value;
    }
    for(int i=k+1;i<n;i++)a[i][k]=a[k][i]=0;
    previous=pivot;r++;
  }
  return r;
}
// Finite exact-rank certificate. Fraction-free symmetric Gaussian elimination
// uses signed 128-bit intermediates and checks every exact integer quotient.
// Build: g++ -O2 -std=c++17 check_exact.cpp -o check_exact
// Run: ./check_exact
int main(){
 for(int kind=0;kind<2;kind++){
  int A[16][16]={};
  for(int i=0;i<16;i++)for(int j=0;j<16;j++)if(i!=j){
    int a=i>>2,b=i&3,c=j>>2,d=j&3;
    if(kind==0)A[i][j]=(a==c||b==d);
    else {int x=(c-a+4)%4,y=(d-b+4)%4;
      A[i][j]=(x==1&&y==0)||(x==3&&y==0)||(x==0&&y==1)||(x==0&&y==3)||(x==1&&y==1)||(x==3&&y==3);
    }
  }
  for(int i=0;i<16;i++)for(int j=0;j<16;j++){
    if(A[i][j]!=A[j][i])return 2;
    int common=0;for(int t=0;t<16;t++)common+=A[i][t]*A[t][j];
    if(i==j && common!=6)return 3;
    if(i!=j && common!=2)return 4;
  }
  map<pair<int,int>,int> dist;
  for(int mask=0;mask<65536;mask++)if(__builtin_popcount((unsigned)mask)==9){
    vector<int> T;for(int i=0;i<16;i++)if((mask>>i)&1)T.push_back(i);
    vector<vector<ll>> B(9,vector<ll>(9)),C=B;
    for(int i=0;i<9;i++)for(int j=0;j<9;j++){
      B[i][j]=2*A[T[i]][T[j]]+4*(i==j)-1;
      C[i][j]=-4*A[T[i]][T[j]]+8*(i==j)+1;
    }
    dist[{exact_psd_rank(B),exact_psd_rank(C)}]++;
  }
  cout<<(kind==0?"ROOK":"SHRIKHANDE")<<"\n";
  int sum=0;for(auto [key,num]:dist){sum+=num;cout<<"rank2="<<key.first<<" rank-2="<<key.second<<" count="<<num<<"\n";}
  if(sum!=11440)return 5;
  if(kind==0 && dist!=map<pair<int,int>,int>{{{5,9},160},{{6,7},768},{{6,8},6576},{{6,9},3936}})return 6;
  if(kind==1 && dist!=map<pair<int,int>,int>{{{5,8},48},{{5,9},112},{{6,7},48},{{6,8},4032},{{6,9},7200}})return 7;
 }
 cout<<"EXACT_RANKS_OK\n";
}
