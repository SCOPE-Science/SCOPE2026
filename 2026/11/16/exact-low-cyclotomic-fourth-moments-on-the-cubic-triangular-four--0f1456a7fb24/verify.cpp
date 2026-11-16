// Exact finite-phase fourth-moment certificate for the ten-point triangular Fourier aperture.
// Build: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <vector>
using namespace std;
struct Pair {int x=0,y=0;};
static long long norm(Pair a,bool gauss){return (long long)a.x*a.x+(long long)a.y*a.y-(gauss?0:(long long)a.x*a.y);}
static Pair root(int k,int q){
 if(q==4){const Pair r[4]={{1,0},{0,1},{-1,0},{0,-1}};return r[k];}
 if(q==6){const Pair r[6]={{1,0},{1,1},{0,1},{-1,0},{-1,-1},{0,-1}};return r[k];}
 if(q==3){const Pair r[3]={{1,0},{0,1},{-1,-1}};return r[k];}
 if(q==2){const Pair r[2]={{1,0},{-1,0}};return r[k];}
 return {1,0};
}
int main(){
 vector<pair<int,int>> S;for(int i=0;i<=3;++i)for(int j=0;j<=3-i;++j)S.emplace_back(i,j);
 assert(S.size()==10);
 int a00=-1,a10=-1,a01=-1;
 for(int i=0;i<10;++i){if(S[i]==make_pair(0,0))a00=i;if(S[i]==make_pair(1,0))a10=i;if(S[i]==make_pair(0,1))a01=i;}
 vector<int> free;for(int i=0;i<10;++i)if(i!=a00&&i!=a10&&i!=a01)free.push_back(i);
 const map<int,tuple<int,long long,long long,long long,long long,int>> expected={
   {1,{442,1,442,1,0,1}},{2,{138,3,442,1,154,10}},
   {3,{136,8,442,1,148,27}},{4,{138,45,442,1,146,29}},
   {6,{132,6,442,1,134,127}}
 };
 for(int q:{1,2,3,4,6}){
  const bool gauss=(q==4);long long total=1;for(int j=0;j<7;++j)total*=q;
  map<long long,long long> counts;vector<long long> minimizers;
  long long minValue=numeric_limits<long long>::max(),maxValue=0;
  for(long long code=0;code<total;++code){
   int e[10]={};long long z=code;for(int i:free){e[i]=z%q;z/=q;}
   Pair convol[49]={}, corr[49]={};
   // Direct polynomial-square convolution on the sum lattice.
   for(int i=0;i<10;++i)for(int j=0;j<10;++j){
    int k=(e[i]+e[j])%q;Pair r=root(k,q);
    int idx=7*(S[i].first+S[j].first)+S[i].second+S[j].second;
    convol[idx].x+=r.x;convol[idx].y+=r.y;
   }
   // Independent aperiodic autocorrelation on the difference lattice.
   for(int i=0;i<10;++i)for(int j=0;j<10;++j){
    int k=(e[i]-e[j]+q)%q;Pair r=root(k,q);
    int idx=7*(S[i].first-S[j].first+3)+S[i].second-S[j].second+3;
    corr[idx].x+=r.x;corr[idx].y+=r.y;
   }
   long long fromSums=0,fromDiffs=0;
   for(Pair r:convol)fromSums+=norm(r,gauss);
   for(Pair r:corr)fromDiffs+=norm(r,gauss);
   if(fromSums!=fromDiffs){cerr<<"Moment formulas disagree: q="<<q<<" code="<<code<<"\n";return 2;}
   counts[fromSums]++;
   if(fromSums<minValue){minValue=fromSums;minimizers.clear();}
   if(fromSums==minValue)minimizers.push_back(code);
   maxValue=max(maxValue,fromSums);
  }
  auto [expectedMin,expectedCount,expectedMax,expectedMaxCount,expectedSecond,expectedDistinct]=expected.at(q);
  long long second=counts.size()>1?next(counts.begin())->first:0;
  if(minValue!=expectedMin || (long long)minimizers.size()!=expectedCount || maxValue!=expectedMax ||
     counts.at(maxValue)!=expectedMaxCount || second!=expectedSecond || (int)counts.size()!=expectedDistinct){
   cerr<<"Expected result mismatch for alphabet "<<q<<"\n";return 3;
  }
  cout<<"q="<<q<<" gauge_representatives="<<total<<" min="<<minValue<<" normalized_minimizers="<<minimizers.size()
      <<" max="<<maxValue<<" next="<<second<<" distinct_moments="<<counts.size()<<" PASS\n";
  cout<<"min_codes=";for(long long id:minimizers)cout<<id<<",";cout<<"\n";
 }
 cout<<"All exact convolution/autocorrelation comparisons and complete enumerations PASS.\n";
}
