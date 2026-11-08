// Exact classification of nonzero primitive periodic words for
// x[t] = x[t-1] + x[t-k]^2 (mod 3), for periods at most 22.
// C++17, standard library only. No heuristic or external data.
#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
#include <stdexcept>
using namespace std;

static bool primitive(const vector<unsigned char>& x, int n) {
  for (int d=1; d<n; ++d) if (n%d==0) {
    bool same=true;
    for(int j=0;j<n;++j) if(x[j]!=x[(j+d)%n]) { same=false; break; }
    if(same) return false;
  }
  return true;
}
static bool same_rotation(const vector<unsigned char>& x, const string& target) {
  int n=(int)x.size();
  if((int)target.size()!=n) return false;
  for(int shift=0;shift<n;shift++) {
    bool eq=true;
    for(int j=0;j<n;j++) if(x[j]!=target[(j+shift)%n]-'0') {eq=false;break;}
    if(eq) return true;
  }
  return false;
}

int main() {
  const string words[23][23] = {
    {}, {}, {}, {},
    {"","","1120","1220"},
    {}, {}, {}, {},
    {"","","","","122201200","","120111200"},
    {}, {}, {}, {}, {}, {}, {}, {}, {},
    {"","","","","","1222201201120012000","","","","","","","","","","1200122012011112000"},
    {}, {},
    {"","","","","","","","","1222011120122012001200","","","","","","","1201120122201112001200"}
  };
  uint64_t tested_masks=0, positive_candidates=0;
  for(int n=1;n<=22;n++) {
    uint64_t full=(uint64_t(1)<<n);
    for(int lag=0;lag<n;lag++) {
      int observed=0, expected=0;
      const string& target=words[n][lag];
      if(!target.empty()) for(char c:target) expected+=(c=='0');
      for(uint64_t mask=1;mask<full;mask++) {
        ++tested_masks;
        if(__builtin_popcountll(mask)%3!=0) continue;
        vector<unsigned char> x(n);
        unsigned c=0;
        for(int j=0;j<n;j++){
          int source=(j-lag+n)%n;
          c=(c+((mask>>source)&1ULL))%3U;
          x[j]=(unsigned char)c;
        }
        if(c!=0U) throw runtime_error("closure invariant violated");
        bool ok=true;
        for(int j=0;j<n;j++)
          if ((x[j]!=0)!=bool((mask>>j)&1ULL)) {ok=false;break;}
        if(!ok || !primitive(x,n)) continue;
        ++observed; ++positive_candidates;
        if(target.empty()) throw runtime_error("unexpected period or lag");
        if(!same_rotation(x,target)) throw runtime_error("unexpected cyclic orbit");
        // Verify the original nonlinear recurrence directly.
        for(int j=0;j<n;j++) {
          int prev=x[(j+n-1)%n], delayed=x[(j+n-lag)%n];
          if(x[j]!=(prev+delayed*delayed)%3)
            throw runtime_error("direct recurrence failure");
        }
      }
      if(observed!=expected) {
        cerr<<"n="<<n<<" lag="<<lag<<" observed="<<observed
            <<" expected="<<expected<<'\n';
        throw runtime_error("incorrect orbit multiplicity");
      }
      if(observed) cout<<"PERIOD "<<n<<" LAG_RESIDUE "<<lag
                       <<" ZERO_ANCHORED_WORDS "<<observed
                       <<" ONE_ORBIT "<<target<<'\n';
    }
  }
  cout<<"VERIFY_OK periods=1..22,lag_residues=all,mask_candidates="
      <<tested_masks<<",valid_zero_anchored="<<positive_candidates
      <<",exact_integer=yes\n";
}
