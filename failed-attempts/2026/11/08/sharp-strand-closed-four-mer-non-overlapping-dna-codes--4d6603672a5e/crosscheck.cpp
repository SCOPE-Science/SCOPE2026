// Independent exhaustive subset dynamic program for Watson-Crick symmetric non-overlapping codes.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
int comp(int a){return a^1;} // 0<->1 and 2<->3
string rc(string w){reverse(w.begin(),w.end());for(char &c:w)c=char('0'+comp(c-'0'));return w;}
bool ok(string a,string b){for(int k=1;k<=3;k++) if(a.substr(0,k)==b.substr(4-k,k)||b.substr(0,k)==a.substr(4-k,k))return false;return true;}
struct Ans {int n,best,nmax;};
Ans solve(const set<int>& A) {
  set<int> B;for(int a:A)B.insert(comp(a));
  set<string> W;
  for(int a:A)for(int b=0;b<4;b++)for(int c=0;c<4;c++)for(int d:B)W.insert(string({char('0'+a),char('0'+b),char('0'+c),char('0'+d)}));
  vector<vector<string>> orbs;set<string> seen;
  for(const auto& w:W) if(!seen.count(w)) {
    auto v=rc(w);if(!W.count(v)){cerr<<"Not RC invariant";exit(1);}
    seen.insert(w);seen.insert(v);
    vector<string> o={w};if(w!=v)o.push_back(v);
    bool valid=true;for(const auto& x:o)for(const auto& y:o)if(!ok(x,y))valid=false;
    if(valid)orbs.push_back(o);
  }
  int n=(int)orbs.size(); if(n>20){cerr<<"Excess orbits";exit(1);}
  vector<uint32_t> conflicts(n);vector<int> weight(n);
  for(int i=0;i<n;i++){
    weight[i]=(int)orbs[i].size();
    for(int j=0;j<i;j++){
      bool bad=false;
      for(const auto& x:orbs[i])for(const auto& y:orbs[j])if(!ok(x,y))bad=true;
      if(bad){conflicts[i]|=uint32_t(1)<<j; conflicts[j]|=uint32_t(1)<<i;}
    }
  }
  const uint32_t size=uint32_t(1)<<n;
  vector<uint8_t> independent(size);vector<uint8_t> score(size);
  independent[0]=1;int best=0,num=0;
  for(uint32_t mask=0;mask<size;mask++) {
    if(mask){
      int bit=__builtin_ctz(mask);
      uint32_t prev=mask&(mask-1);
      independent[mask] = independent[prev] && ((conflicts[bit]&prev)==0);
      if(independent[mask])score[mask]=score[prev]+weight[bit];
    }
    if(independent[mask]) {
      if((int)score[mask]>best){best=score[mask];num=1;}
      else if((int)score[mask]==best)num++;
    }
  }
  return {n,best,num};
}
int main(){
 auto small=solve({0});auto large=solve({0,2});
 cout<<"A1 "<<small.n<<" "<<small.best<<" "<<small.nmax<<"\n";
 cout<<"A2 "<<large.n<<" "<<large.best<<" "<<large.nmax<<"\n";
 if(small.n!=6||small.best!=7||small.nmax!=2||large.n!=20||large.best!=17||large.nmax!=8)return 1;
 cout<<"CROSSCHECK_OK\n";
}
