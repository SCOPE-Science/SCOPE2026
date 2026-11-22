// Exhaustive necessary-condition screen for cyclic trinomial Ehrhart numerator
// with exactly two top-height characters. Only integer arithmetic is used.
#include <bits/stdc++.h>
using namespace std;
using ll=long long;
static const ll P=1000000007LL;
ll power(ll a,ll n){ll s=1;while(n){if(n&1)s=s*a%P; a=a*a%P;n/=2;}return s;}
int inverse_mod(int a,int m){int b=m,u=1,v=0;while(b){int t=a/b;a-=t*b;swap(a,b);u-=t*v;swap(u,v);}if(a!=1)return -1;u%=m;if(u<0)u+=m;return u;}
// Returns true if exact modular inconsistency exists and coefficient matrix
// has full column rank mod P, certifying rational inconsistency.
bool obstruction(int m,int a,int b,const vector<int>& chars,int &rank){
 const int s=(int)chars.size();
 vector<vector<ll>> basis(s);
 vector<int> pivots(s,-1);rank=0;
 bool incons=false;
 for(int j=1;j<m;j++){
  vector<ll> row(s+1);
  for(int i=0;i<s;i++) row[i]=(ll)j*chars[i]%m;
  row[s]=(ll)m*(1+(j==a)+(j==b));
  bool inserted=false;
  for(int k=0;k<s;k++){
   if(row[k]==0)continue;
   if(pivots[k]>=0){ll fac=row[k];for(int l=k;l<=s;l++){row[l]=(row[l]-fac*basis[k][l]%P+P)%P;}}
   else {
    ll inv=power(row[k],P-2);
    for(int l=k;l<=s;l++)row[l]=row[l]*inv%P;
    pivots[k]=1;basis[k]=std::move(row);rank++;inserted=true;break;
   }
  }
  if(!inserted){
   bool allzero=true;
   for(int k=0;k<s;k++)if(row[k]!=0){allzero=false;break;}
   if(allzero && row[s]!=0) incons=true;
  }
  // no break: must establish full mod-P column rank
 }
 return incons && rank==s;
}
int main(int argc,char**argv){
 int maxm=argc>1?atoi(argv[1]):60;
 long long cases=0,covered=0, incon=0,exceptions=0;
 for(int m=4;m<=maxm;m++){
  set<pair<int,int>> candidates;
  for(int a=1;a<m;a++) for(int b=a+1;b<m;b++) candidates.insert({a,b});
  int errm=0;
  for(auto [a,b]:candidates){
   cases++;
   vector<int> chars;
   int faithful=m;
   for(int r=1;r<m;r++){
    int g=gcd(r,m), ar=(ll)a*r%m,br=(ll)b*r%m;
    int ca=m-g-ar,cb=m-g-br;
    if(ca>2 || cb>2)continue;
    int dab=(a-b+m)%m, dba=(b-a+m)%m;
    int exa=(br>ar)+((dab!=b)&&((ll)dab*r%m>ar));
    int exb=(ar>br)+((dba!=a)&&((ll)dba*r%m>br));
    if(ca==exa && cb==exb){chars.push_back(r);faithful=gcd(faithful,r);}
   }
   if(faithful!=1)continue;
   covered++;
   int rank=0;
   if(obstruction(m,a,b,chars,rank)) incon++;
   else {exceptions++;errm++;cout<<"EXCEPTION "<<m<<" "<<a<<" "<<b<<" chars";for(auto r:chars)cout<<" "<<r;cout<<" rank "<<rank<<" / "<<chars.size()<<"\n";}
  }
  if(m%50==0||errm>0)cerr<<"up_to="<<m<<" generated="<<cases<<" faithful="<<covered<<" modular_obstructions="<<incon<<" exceptions="<<exceptions<<"\n";
 }
 cerr<<"SUMMARY "<<maxm<<" "<<cases<<" "<<covered<<" "<<incon<<" "<<exceptions<<"\n";
}
