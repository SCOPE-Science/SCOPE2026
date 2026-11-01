// Independent finite-field exhaustive matrix check, using polynomial-basis arithmetic.
// Characteristic-two alternating matrices have symmetric entries and zero diagonal.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int mul(int a,int b,int q) {
  int poly=(q==2?3:q==4?7:11), out=0;
  while(b){if(b&1)out^=a;b>>=1;a<<=1;if(a&q)a^=poly;}
  return out&(q-1);
}
int rank_mat(vector<vector<int>> a,int q){
  int n=(int)a.size(),r=0;
  for(int j=0;j<n;j++){
    int k=r;while(k<n&&!a[k][j])k++;
    if(k==n)continue;
    swap(a[r],a[k]);
    int inv=0;for(int t=1;t<q;t++)if(mul(a[r][j],t,q)==1)inv=t;
    assert(inv);
    for(int c=j;c<n;c++)a[r][c]=mul(a[r][c],inv,q);
    for(int i=r+1;i<n;i++)if(a[i][j]){
      int t=a[i][j];for(int c=j;c<n;c++)a[i][c]^=mul(t,a[r][c],q);
    }
    r++;
  }
  return r;
}
map<int,uint64_t> brute(int n,int q){
  vector<pair<int,int>> edges;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)edges.push_back({i,j});
  uint64_t total=1;for(size_t t=0;t<edges.size();t++)total*=q;
  map<int,uint64_t> ans;
  for(uint64_t id=0;id<total;id++){
    auto A=vector<vector<int>>(n,vector<int>(n));
    auto x=id;
    for(auto [i,j]:edges){A[i][j]=A[j][i]=x%q;x/=q;}
    bool ok=true;
    for(int i=0;i<n&&ok;i++)for(int j=0;j<n&&ok;j++){
      int sum=0;for(int k=0;k<n;k++)sum^=mul(A[i][k],A[k][j],q);
      if(sum)ok=false;
    }
    if(ok)ans[rank_mat(A,q)]++;
  }
  return ans;
}
int main(){
  for(auto [n,q]:vector<pair<int,int>>{{7,2},{5,4},{4,8}}){
    auto counts=brute(n,q);
    cout<<"n="<<n<<" q="<<q<<" ";
    for(auto [r,c]:counts)cout<<r<<":"<<c<<" ";
    cout<<"\n";
    if(n==7&&q==2)assert((counts==map<int,uint64_t>{{0,1},{2,315}}));
    if(n==5&&q==4)assert((counts==map<int,uint64_t>{{0,1},{2,255}}));
    if(n==4&&q==8)assert((counts==map<int,uint64_t>{{0,1},{2,63}}));
  }
  cout<<"VERIFY_OK_ALTERNATING_SQUAREZERO_CPP\n";
}
