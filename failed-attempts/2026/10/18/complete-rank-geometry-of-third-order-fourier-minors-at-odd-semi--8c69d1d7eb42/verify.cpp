// Exact cyclotomic determinant and rank checks for 3-by-3 Fourier minors over cyclic orders 3p.
// Only primes at least five are exercised; general proof is in RESULT.md.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
struct Triple { array<int,3> x; int mod3,modp; };
int variety(array<int,3> v){sort(v.begin(),v.end());return v[0]==v[2]?1:((v[0]==v[1]||v[1]==v[2])?2:3);}
int main(){
 const int permutations[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
 const int signs[6]={1,-1,-1,1,1,-1};
 for(int p:{5,7,11}) {
  const int n=3*p; vector<Triple> t;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)
   t.push_back({{a,b,c},variety({a%3,b%3,c%3}),variety({a%p,b%p,c%p})});
  long long ones=0,twos=0,threes=0,errors=0;
  for(const auto &r:t)for(const auto &c:t) {
   // Det = sum of signed sixth roots of unity split into zeta_3 and zeta_p factors.
   // Minimal polynomial of zeta_p over Q(zeta_3) is 1+X+...+X^{p-1}.
   array<array<int,2>,11> v{};
   for(int j=0;j<6;j++){
    int a=0,b=0;
    for(int i=0;i<3;i++){
     a+=(r.x[i]%p)*(c.x[permutations[j][i]]%p);
     b+=(r.x[i]%3)*(c.x[permutations[j][i]]%3);
    }
    a%=p;b%=3;
    if(b==0)v[a][0]+=signs[j];
    if(b==1)v[a][1]+=signs[j];
    if(b==2){v[a][0]-=signs[j];v[a][1]-=signs[j];}
   }
   bool zero=true;
   for(int j=1;j<p;j++) if(v[j]!=v[0]){zero=false;break;}
   bool rankone=true;
   for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)
    for(int k=0;k<3;k++)for(int l=k+1;l<3;l++)
     if(((r.x[j]-r.x[i])*(c.x[l]-c.x[k]))%n !=0)rankone=false;
   const bool predicted_zero = (r.modp==1&&c.mod3<3)||(c.modp==1&&r.mod3<3)||
                               (r.mod3==1&&c.modp<3)||(c.mod3==1&&r.modp<3);
   const bool predicted_rankone=(r.modp==1&&c.mod3==1)||(c.modp==1&&r.mod3==1);
   if(zero!=predicted_zero || rankone!=predicted_rankone ||(rankone&&!zero))errors++;
   if(rankone)ones++;else if(zero)twos++;else threes++;
  }
  long long P=p,T=3LL*p*(p-1)*(p-2)/6;
  long long singular=1LL*p*p*(p-1)*(9*p*p-20*p+16);
  long long rank1=1LL*p*p*(p-1)*(p-2);
  long long total=1LL*t.size()*t.size();
  if(ones!=rank1||ones+twos!=singular||ones+twos+threes!=total)errors++;
  cout<<"p="<<p<<" n="<<n<<" minors="<<total<<" rank1="<<ones<<" rank2="<<twos<<" rank3="<<threes<<" exact_mismatches="<<errors<<"\n";
  if(errors)return 1;
 }
 cout<<"All tested minors match the stated rank criterion and polynomial counts.\n";
}
