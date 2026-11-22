#include <iostream>
#include <vector>
#include <map>
#include <cstdint>
using namespace std;

map<int,uint64_t> enumerate(int m, int n) {
  vector<uint64_t> nb;
  for(int r=0;r<m;r++) for(int c=0;c<n;c++) {
    uint64_t x=0;
    for(int i=0;i<m;i++)for(int j=0;j<n;j++)
      if(i==r || j==c) x|=1ULL<<(i*n+j);
    nb.push_back(x);
  }
  map<int,uint64_t> cnt;
  const uint64_t stop=1ULL<<(m*n);
  for(uint64_t x=0;x<stop;x++) {
    bool ok=true;
    for(auto b:nb) if(__builtin_popcountll(x & b)>3){ok=false;break;}
    if(ok)cnt[__builtin_popcountll(x)]++;
  }
  return cnt;
}
int main(){
  for(auto [m,n]:vector<pair<int,int>>{{2,2},{2,3},{2,4},{3,3},{3,4},{3,5},{4,4},{4,5},{3,6},{3,7},{4,6}}){
    auto p=enumerate(m,n);
    cout << m << "x" << n << ":";
    for(auto [k,a]:p)cout<<" "<<k<<"="<<a;
    cout<<"\n";
  }
}
