// Exhaustive finite checks of a double-centralizer theorem for Catalan monoids.
// Build: c++ -O3 -std=c++17 check_bicommutant.cpp -o check && ./check
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int n;
vector<vector<uint8_t>> maps;
void gen(int i, vector<uint8_t>&v) {
 if(i==n){maps.push_back(v);return;}
 for(int t=(i?v[i-1]:0);t<=i;t++){v[i]=t;gen(i+1,v);}
}
bool commute(const vector<uint8_t>&a,const vector<uint8_t>&b) {
 for(int i=0;i<n;i++) if(a[b[i]]!=b[a[i]]) return false;
 return true;
}
bool idem(const vector<uint8_t>&a){for(int i=0;i<n;i++)if(a[a[i]]!=a[i])return false;return true;}
int main(){
 for(n=1;n<=8;n++){
  maps.clear();vector<uint8_t> t(n);gen(0,t);
  auto ct=maps.size();vector<int> ids;for(int i=0;i<(int)ct;i++)if(idem(maps[i]))ids.push_back(i);
  unsigned long pairs=0;
  for(int e:ids){
   vector<int> c;for(int j=0;j<(int)ct;j++)if(commute(maps[e],maps[j]))c.push_back(j);
   vector<int> z;
   for(int j:c){bool yes=true;for(int k:c){if(!commute(maps[j],maps[k])){yes=false;break;}}if(yes)z.push_back(j);}
   bool nontriv=(e!=0 && e!=(int)ct-1); // enumeration starts at zero map and ends at identity
   if(z.size()!=(nontriv?3:((n==1)?1:2))){cerr<<"FAIL n="<<n<<" e="<<e<<" zsize="<<z.size()<<"\n";return 1;}
   for(int j:z) if(j!=0 && j!=(int)ct-1 && j!=e){cerr<<"EXTRA n="<<n<<" e="<<e<<" j="<<j<<"\n";return 1;}
   pairs++;
  }
  cout<<"n="<<n<<" catalan="<<ct<<" idempotents="<<ids.size()<<" validated="<<pairs<<"\n";
 }
 cout<<"CATALAN_BICOMMUTANT_OK\n";
}
