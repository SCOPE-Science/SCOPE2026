#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
int main(){
  constexpr int MOD=729,N=6561;
  vector<int> f(N),row{1};
  for(int n=0;n<N;++n){
    long long sum=0;
    for(int c:row) sum=(sum+1LL*c*c%MOD*c)%MOD;
    f[n]=int(sum);
    if(f[n]%3 != (n%2?2:1)) return 1;
    vector<int> next(row.size()+1);
    for(size_t j=0;j<row.size();++j){next[j]=(next[j]+row[j])%MOD; next[j+1]=(next[j+1]+row[j])%MOD;}
    row.swap(next);
  }
  cout<<"Franel mod 729 versus digit parity: 6561/6561 PASS\n";
  int comparisons=0;
  for(int k=1,pk=3;k<=5;++k,pk*=3){
    vector<bool> seen(pk,false);
    for(int n=0;n<N;++n) seen[f[n]%pk]=true;
    for(int r=0;r<pk;++r) if(seen[r] != (r%3!=0)){cerr<<"image fails k="<<k<<" r="<<r<<'\n';return 2;}
    cout<<"Complete unit residue image mod "<<pk<<": "<<2*pk/3<<"/"<<2*pk/3<<" PASS\n";
    int big=1;
    for(int L=0;L<8;++L,big*=3){
      if(L>=1 && big<N && f[big]%27!=2){cerr<<"generator fails L="<<L<<'\n'; return 3;}
      if(L<k || big>=N) continue;
      int q=1;
      for(int j=0;j<L-k+1;++j)q*=3;
      for(int a=0;a<q&&big+a<N;++a){
        ++comparisons;
        if(f[big+a]%pk != (f[big]*f[a])%pk){
          cerr<<"block fails k="<<k<<" L="<<L<<" a="<<a<<'\n'; return 4;
        }
      }
    }
  }
  cout<<"Separated ternary block identities: "<<comparisons<<"/"<<comparisons<<" PASS\n";
  cout<<"Exact finite checks passed; infinite theorem relies on the accompanying proof.\n";
}
