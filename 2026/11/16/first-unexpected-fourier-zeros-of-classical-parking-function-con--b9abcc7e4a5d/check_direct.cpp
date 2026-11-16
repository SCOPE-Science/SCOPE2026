// Independent exact character census on the coordinate residue group.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;

static bool parking(const vector<int>& x) {
  vector<int> y=x;
  sort(y.begin(),y.end());
  for(int i=0;i<(int)y.size();i++) if(y[i]>i) return false;
  return true;
}
int main() {
  const int n=5,m=6;
  vector<array<unsigned char,5>> pf;
  for(int z=0;z<3125;z++) {
    int u=z; vector<int> x(n);
    for(int i=0;i<n;i++){x[i]=u%5;u/=5;}
    if(parking(x)) {
      array<unsigned char,5> row{};
      for(int i=0;i<n;i++)row[i]=(unsigned char)x[i];
      pf.push_back(row);
    }
  }
  assert(pf.size()==1296);
  int count_zero=0,count_forced=0,count_extra=0;
  map<array<int,5>,int> extra_types;
  for(int z=0;z<7776;z++){
    int u=z, sm=0; array<int,5> k{};
    for(int i=0;i<n;i++){k[i]=u%6;sm+=k[i];u/=6;}
    array<int,6> c{};
    for(const auto& x:pf){
      int exponent=0;
      for(int i=0;i<n;i++)exponent+=k[i]*x[i];
      c[exponent%6]++;
    }
    int real=c[0]-c[2]-c[3]+c[5];
    int omega=c[1]+c[2]-c[4]-c[5];
    bool zero=real==0&&omega==0;
    bool forced=(sm%6==0&&z!=0);
    assert(!forced||zero);
    if(zero){
      count_zero++;
      if(forced)count_forced++;
      else {count_extra++;sort(k.begin(),k.end());extra_types[k]++;}
    }
  }
  assert(count_zero==1655&&count_forced==1295&&count_extra==360);
  assert(extra_types.size()==5);
  assert(extra_types.at({1,2,3,3,4})==60);
  assert(extra_types.at({1,2,3,3,5})==60);
  assert(extra_types.at({1,2,3,4,5})==120);
  assert(extra_types.at({1,3,3,4,5})==60);
  assert(extra_types.at({2,3,3,4,5})==60);
  cout<<"PARKING5_DIRECT_CHARACTER_PASS parking=1296 frequencies=7776 zeros=1655 extra=360 rank=6121\n";
}
