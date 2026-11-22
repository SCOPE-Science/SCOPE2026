// Exact binary suffixient-set substitution sensitivity for n <= 14.
// Standalone C++17: g++ -O2 -std=c++17 verify_suffixient.cpp -o verify_suffixient && ./verify_suffixient
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

// Algorithm A: group substrings u by all immediate followers;
// a right extension u+c survives iff no one-letter left extension z+u+c
// is itself a right extension. Any longer extension has such a first step.
static int chi_context(const string& w) {
    string s = w + '$';
    map<string, unsigned> follows;
    for (int i=0; i<(int)s.size(); ++i)
      for (int j=i; j<(int)s.size(); ++j) {
        unsigned bit = s[j]=='0' ? 1u : (s[j]=='1' ? 2u : 4u);
        follows[s.substr(i,j-i)] |= bit;
      }
    set<string> E;
    for (const auto& kv: follows)
      if (__builtin_popcount(kv.second) > 1)
        for (char c: string("01$"))
          if (kv.second & (c=='0' ? 1u : (c=='1' ? 2u : 4u)))
            E.insert(kv.first+c);
    int ans=0;
    for (const auto& x: E) {
       bool extended=false;
       for (char c: string("01"))
         if (E.count(c+x)) { extended=true; break; }
       ans += !extended;
    }
    return ans;
}

// Algorithm B: independently enumerate unique occurring nonempty factors;
// decide right maximality via explicitly searching for a second follower;
// eliminate factors dominated under the PROPER suffix order, no context maps.
static int chi_suffix(const string& w) {
    string s = w+'$';
    set<string> factors;
    for(int i=0; i<(int)s.size(); ++i)
      for(int len=1; i+len<=(int)s.size(); ++len)
        factors.insert(s.substr(i,len));
    vector<string> extensions;
    for(const auto& e: factors) {
      string prefix=e.substr(0,e.size()-1);
      int mask=0;
      for(int i=0; i+(int)prefix.size()<(int)s.size(); ++i)
        if(s.compare(i,prefix.size(),prefix)==0) {
          char c=s[i+prefix.size()];
          mask |= (c=='0'?1:(c=='1'?2:4));
        }
      if(__builtin_popcount((unsigned)mask)>=2)
        extensions.push_back(e);
    }
    int count=0;
    for (const auto& e:extensions){
      bool dominated=false;
      for (const auto& f:extensions)
        if(f.size()>e.size() && f.compare(f.size()-e.size(),e.size(),e)==0){
          dominated=true; break;
        }
      count+=!dominated;
    }
    return count;
}

static string bits(int x,int n) {
    string s(n,'0');
    for(int i=0;i<n;++i) s[i]=((x>>(n-i-1))&1)?'1':'0';
    return s;
}
int main(){
    cout<<"n max_delta #oriented_max_edges"<<'\n';
    for(int n=1;n<=14;++n){
      int N=1<<n;
      vector<int> chi(N);
      for(int x=0;x<N;++x){
        string w=bits(x,n);
        int a=chi_context(w);
        int b=chi_suffix(w);
        if(a!=b){ cerr<<"INDEPENDENT DISAGREEMENT "<<n<<' '<<w<<' '<<a<<' '<<b<<'\n';return 2; }
        chi[x]=a;
      }
      int best=0, count=0;
      for(int x=0;x<N;++x)
        for(int k=0;k<n;++k){
          int y=x^(1<<k),diff=chi[y]-chi[x];
          if(diff>best){best=diff;count=0;}
          if(diff==best) ++count;
        }
      cout<<n<<' '<<best<<' '<<count<<'\n';
      if(n==14){
        cout<<"all directed increases of six (low high flip_position_1based chi_low chi_high):"<<'\n';
        for(int x=0;x<N;++x)
          for(int k=0;k<n;++k){
            int y=x^(1<<k);
            if(chi[y]-chi[x]==6)
              cout<<bits(x,n)<<' '<<bits(y,n)<<' '<<n-k<<' '<<chi[x]<<' '<<chi[y]<<'\n';
          }
      }
    }
    return 0;
}
