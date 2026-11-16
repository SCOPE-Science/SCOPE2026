// Exact integer checks for the small-rank finite consequences of the theorem.
// C++17: g++ -std=c++17 -O2 complete_tree_threshold_check.cpp -o check && ./check
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
ll det(vector<vector<ll>> a){
  int n=(int)a.size(); ll prev=1,sgn=1;
  for(int k=0;k<n-1;k++){
    int pivot=k;while(pivot<n && a[pivot][k]==0)pivot++;
    if(pivot==n)return 0;
    if(pivot!=k){swap(a[pivot],a[k]);sgn=-sgn;}
    ll t=a[k][k];
    for(int i=k+1;i<n;i++)for(int j=k+1;j<n;j++){
      ll v=a[i][j]*t-a[i][k]*a[k][j];
      if(v%prev){cerr<<"nonintegral Bareiss"<<endl;exit(1);}
      a[i][j]=v/prev;
    }
    for(int i=k+1;i<n;i++)a[i][k]=0;
    prev=t;
  }
  return sgn*a[n-1][n-1];
}
vector<pair<int,int>> edges(int n){vector<pair<int,int>> e;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)e.push_back({i,j});return e;}
ll walsh(int n,const vector<int>& chosen){
 auto e=edges(n);vector<vector<ll>> L(n,vector<ll>(n,0));
 for(auto [i,j]:e){L[i][i]++;L[j][j]++;L[i][j]--;L[j][i]--;}
 for(int k:chosen){auto [i,j]=e[k]; L[i][i]-=2;L[j][j]-=2;L[i][j]+=2;L[j][i]+=2;}
 vector<vector<ll>> minor(n-1,vector<ll>(n-1));
 for(int i=0;i<n-1;i++)for(int j=0;j<n-1;j++)minor[i][j]=L[i][j];
 return det(minor);
}
int main(){
 for(int n:{4,6,8,10}){
  auto e=edges(n);int m=e.size();int min_k=n/2-1;
  ll zeros=0,early=0,at=0, negative=0;
  for(int k=0;k<=min_k;k++){
   vector<int> a(k);iota(a.begin(),a.end(),0);
   bool loop=true;
   while(loop){
    ll w=walsh(n,a);
    if(w<0)negative++;
    if(!w){zeros++;if(k<min_k)early++;else at++;}
    if(k==0)break;
    int j=k-1;
    while(j>=0 && a[j]==m-k+j)j--;
    if(j<0)break;
    a[j]++;for(int t=j+1;t<k;t++)a[t]=a[t-1]+1;
   }
  }
  ll expected=n;
  // For n=4, a single negative edge has two star centers.
  if(n==4)expected=n*(n-1)/2;
  else {
   ll binom=1;
   for(int t=1;t<=min_k;t++)binom=binom*(n-t)/t;
   expected=n*binom;
  }
  cout<<"n="<<n<<" min_zero_degree="<<min_k<<" early_zeros="<<early<<" threshold_zeros="<<at<<" expected="<<expected<<" negatives="<<negative<<"\n";
  if(early!=0||at!=expected||negative!=0)return 2;
 }
 cout<<"COMPLETE_TREE_THRESHOLD_PASS\n";
}
