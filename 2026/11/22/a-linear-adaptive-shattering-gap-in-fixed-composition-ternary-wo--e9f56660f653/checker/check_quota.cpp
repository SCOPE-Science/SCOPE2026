// Independently enumerates fixed-composition words and their binary query traces.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
static uint64_t checks=0;
void verify(vector<int> cap) {
 int q=cap.size(), n=accumulate(cap.begin(),cap.end(),0), E=q*n;
 if(E>20)throw runtime_error("finite verifier restricted to at most 20 queries");
 vector<int> word;
 for(int c=0;c<q;c++)word.insert(word.end(),cap[c],c);
 vector<uint32_t> concepts;
 do { uint32_t p=0; for(int i=0;i<n;i++)p|=(1u<<(i*q+word[i])); concepts.push_back(p); } while(next_permutation(word.begin(),word.end()));
 vector<uint64_t> coeff(n+1,0), expected(n+1,0);
 int maximum=*max_element(cap.begin(),cap.end());
 for(uint32_t s=0;s<(1u<<E);s++) {
  int k=__builtin_popcount(s);
  if(k>n)continue;
  int rowSeen=0; vector<int> colorCount(q,0); bool rowOk=true;
  vector<int> bitindices;
  for(int e=0;e<E;e++)if(s&(1u<<e)){int i=e/q,c=e%q;if(rowSeen&(1<<i))rowOk=false;rowSeen|=(1<<i);colorCount[c]++;bitindices.push_back(e);}
  bool pred=rowOk && k<=n-maximum;
  for(int c=0;c<q;c++)if(colorCount[c]>cap[c])pred=false;
  if(pred)expected[k]++;
  // No support with duplicate row or too many tests can be shattered; however
  // directly compute traces for every support in the exhaustive finite cases.
  if(k>10)throw runtime_error("unexpected finite test depth");
  uint64_t traces=0;
  for(uint32_t p:concepts){int pattern=0;for(int j=0;j<k;j++)if(p&(1u<<bitindices[j]))pattern|=(1<<j);traces|=(1ull<<pattern);}
  bool real=traces==((k==6)?~0ull:((1ull<<(1<<k))-1));
  if(real)coeff[k]++;
  if(real!=pred){cerr<<"DISAGREEMENT cap=";for(int a:cap)cerr<<a<<',';cerr<<" support="<<s<<" k="<<k<<"\n";exit(1);}
  checks++;
 }
 if(coeff!=expected)throw runtime_error("coefficient mismatch");
 cout<<"capacities:";for(int a:cap)cout<<' '<<a;
 cout<<" concepts="<<concepts.size()<<" supports="<<(1u<<E)<<" polynomial:";
 for(auto v:coeff)cout<<' '<<v;
 cout<<'\n';
}
int main(){
 for(auto c:vector<vector<int>>{{1,1},{1,2},{2,2},{1,1,1},{1,1,2},{1,2,2},{2,2,2},{1,1,1,1},{1,1,1,2}}) verify(c);
 cout<<"QUOTA_SHATTERING_EXHAUSTIVE_PASS "<<checks<<" supports\n";
}
