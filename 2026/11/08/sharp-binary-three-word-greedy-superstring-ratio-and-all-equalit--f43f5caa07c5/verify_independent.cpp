// Exact independent finite verifier for binary three-word greedy superstrings.
// C++17; no third-party libraries or network use.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

int ov(const string &a,const string &b) {
  int top=min(a.size(), b.size());
  for (int k=top;k>0;--k)
    if (a.substr(a.size()-k)==b.substr(0,k)) return k;
  return 0;
}
string key(const vector<string> &v) {
  string out;
  for (auto &w:v) {out+=to_string(w.size()); out+=':'; out+=w; out+='|';}
  return out;
}
map<string,int> cache;
int worst(vector<string> v) {
  sort(v.begin(),v.end());
  if (v.size()==1) return (int)v[0].size();
  string kk=key(v);
  auto it=cache.find(kk);
  if (it!=cache.end()) return it->second;
  int mx=0;
  for(int i=0;i<(int)v.size();++i)
    for(int j=0;j<(int)v.size();++j)
      if(i!=j) mx=max(mx,ov(v[i],v[j]));
  int res=0;
  for(int i=0;i<(int)v.size();++i) for(int j=0;j<(int)v.size();++j)
    if(i!=j && ov(v[i],v[j])==mx) {
      vector<string> nxt;
      for(int h=0;h<(int)v.size();++h) if(h!=i && h!=j) nxt.push_back(v[h]);
      nxt.push_back(v[i]+v[j].substr(mx));
      res=max(res,worst(nxt));
    }
  cache[kk]=res;
  return res;
}
int optimal(vector<string> v) {
  int n=v.size(), best=0;
  vector<int> p(n);
  iota(p.begin(),p.end(),0);
  do {
    int saving=0;
    for(int i=1;i<n;++i) saving+=ov(v[p[i-1]],v[p[i]]);
    best=max(best,saving);
  } while(next_permutation(p.begin(),p.end()));
  return 3*n-best;
}
int main() {
  array<string,8> w={"000","001","010","011","100","101","110","111"};
  vector<int> attaining;
  int nrows=0;
  for(int mask=1; mask<256; ++mask) {
    vector<string> v;
    for(int i=0;i<8;++i) if(mask&(1<<i)) v.push_back(w[i]);
    int g=worst(v), o=optimal(v);
    assert(7*g <= 10*o);
    if (7*g==10*o) attaining.push_back(mask);
    cout << mask << ',' << v.size() << ',' << o << ',' << g << '\n';
    ++nrows;
  }
  assert(nrows==255);
  assert((attaining==vector<int>{31,87,234,248}));
  cerr << "BINARY_3MER_INDEPENDENT_CPP_OK masks=255 maximizers=4" << endl;
}
