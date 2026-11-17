// Exact rational certificate for the dyadic four-point subdivision jump response.
// Build: g++ -O3 -std=c++17 verify_fourpoint.cpp -o verify_fourpoint
// Usage: ./verify_fourpoint 20
#include <vector>
#include <iostream>
#include <stdexcept>
#include <string>
#include <algorithm>
using i128=__int128_t;
static i128 ab(i128 a){return a<0?-a:a;}
static std::string dec(i128 n){if(n==0)return "0";bool neg=n<0;if(neg)n=-n;std::string s;while(n){s.push_back('0'+int(n%10));n/=10;}if(neg)s.push_back('-');std::reverse(s.begin(),s.end());return s;}
int main(int argc,char **argv){
 int K=(argc==2)?std::stoi(argv[1]):20;
 if(K<0 || K>22) throw std::invalid_argument("0 <= level <= 22");
 long long low=0;std::vector<i128> d{1};i128 den=1;
 for(int k=0;k<=K;k++){
   i128 V=0,W=0,prev=0;
   for(i128 x:d){V+=ab(x);W+=ab(x-prev);prev=x;}W+=ab(prev);
   if(k==K){
     std::cout<<"level="<<k<<"\n";
     std::cout<<"denominator="<<dec(den)<<"\n";
     std::cout<<"variation_numerator="<<dec(V)<<"\n";
     std::cout<<"second_difference_numerator="<<dec(W)<<"\n";
     // For w=1/16, V_limit lies in [V/den,(V+W)/den].
     std::cout<<"upper_numerator="<<dec(V+W)<<"\n";
     std::cout.precision(18);
     std::cout<<"lower_decimal="<<(long double)V/(long double)den<<"\n";
     std::cout<<"upper_decimal="<<(long double)(V+W)/(long double)den<<"\n";
   }
   if(k==K)break;
   long long nl=2*(low-1),hi=low+(long long)d.size()-1;
   std::vector<i128> nd((size_t)(2*(hi+1)+1-nl+1));
   auto get=[&](long long i)->i128{long long j=i-low;return (j>=0 && j<(long long)d.size())?d[(size_t)j]:0;};
   for(long long i=low-1;i<=hi+1;i++){
      i128 a=get(i),diff=get(i-1)-get(i+1);
      nd[(size_t)(2*i-nl)]=8*a+diff;
      nd[(size_t)(2*i+1-nl)]=8*a-diff;
   }
   low=nl;d.swap(nd);den*=16;
 }
}
