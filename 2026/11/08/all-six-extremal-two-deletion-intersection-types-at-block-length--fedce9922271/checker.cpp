// Exhaustive equality-pattern certificate for length-four deletion intersections.
// C++17: g++ -std=c++17 -O2 checker.cpp -o checker && ./checker
#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Word = vector<int>;
set<Word> deletions(const Word& w, int k) {
  set<Word> ans; const int n = (int)w.size();
  for (int i=0; i<n; ++i) {
    if (k==1) { Word z; for(int j=0;j<n;++j) if(j!=i) z.push_back(w[j]); ans.insert(z); }
    else for(int h=i+1; h<n; ++h) {
      Word z; for(int j=0;j<n;++j) if(j!=i && j!=h) z.push_back(w[j]); ans.insert(z);
    }
  }
  return ans;
}
int intersection(const set<Word>& a, const set<Word>& b) {
  int count=0; for(const Word& w:a) if(b.count(w)) ++count; return count;
}
string signature(const Word& w) { string s; for(int v:w) s.push_back(char('0'+v)); return s; }
long long canonical_count=0, admissible_count=0;
int maximum=0;
set<string> maximizers;
void all_patterns(Word& seq, int maxlabel) {
  if(seq.size()==8) {
    ++canonical_count;
    const Word x(seq.begin(),seq.begin()+4),y(seq.begin()+4,seq.end());
    if(intersection(deletions(x,1),deletions(y,1))!=0) return;
    ++admissible_count;
    int value=intersection(deletions(x,2),deletions(y,2));
    maximum=max(maximum,value);
    if(value==4) maximizers.insert(signature(x)+"/"+signature(y));
    return;
  }
  for(int next=0; next<=maxlabel+1; ++next) {
    seq.push_back(next); all_patterns(seq,max(maxlabel,next)); seq.pop_back();
  }
}
int main() {
  Word seq={0}; all_patterns(seq,0);
  const set<string> expected={
      "0110/1001", "0112/1021", "0120/1002", "0120/1021", "0120/2102", "0123/1032"};
  cout << "canonical_patterns=" << canonical_count << " admissible=" << admissible_count
       << " max_intersection=" << maximum << " maximizing_patterns=" << maximizers.size() << "\n";
  for(const string& s:maximizers) cout << s << "\n";
  if(canonical_count!=4140 || admissible_count!=3690 || maximum!=4 || maximizers!=expected) return 1;
  for(int q=2;q<=7;++q) {
    long long falling=1, predicted=0;
    for(int j=1;j<=4;++j) {
      if(j<=q) falling*=q-j+1;
      else falling=0;
      if(j==2 || j==4) predicted+=falling;
      if(j==3) predicted+=4*falling;
    }
    cout << "alphabet=" << q << " predicted_ordered_extremal_pairs=" << predicted << "\n";
  }
  return 0;
}
