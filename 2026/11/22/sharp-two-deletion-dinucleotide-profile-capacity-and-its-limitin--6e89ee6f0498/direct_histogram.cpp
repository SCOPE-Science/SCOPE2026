// Direct exhaustive strings-and-histograms verifier using literal outputs.
#include <array>
#include <iostream>
#include <set>
#include <string>
using namespace std;
using Hist = array<int,4>;
Hist profile(const string& w) {
  Hist v{0,0,0,0};
  for (int i=0;i+1<(int)w.size();++i)
    ++v[2*(w[i]-'0')+(w[i+1]-'0')];
  return v;
}
int main() {
  int expected[] = {0,0,1,1,4,6,7,9,11,14,15,16,16,17};
  for (int n=2;n<=13;++n) {
    int best=0,number=0;string example;
    for (int mask=0;mask<(1<<n);++mask) {
      string w(n,'0');for (int i=0;i<n;++i) w[i]='0'+((mask>>i)&1);
      set<Hist> H;
      for (int i=0;i<n;++i)for (int j=i+1;j<n;++j) {
        string u;u.reserve(n-2);
        for (int k=0;k<n;++k)if(k!=i&&k!=j)u+=w[k];
        H.insert(profile(u));
      }
      if ((int)H.size()>best) {best=(int)H.size();number=1;example=w;}
      else if ((int)H.size()==best) ++number;
    }
    cout<<n<<' '<<best<<' '<<number<<' '<<example<<'\n';
    if(best!=expected[n])return 1;
  }
  cout<<"exhaustive_enumeration_passed"<<'\n';
}
