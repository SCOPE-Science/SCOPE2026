// Self-contained exhaustive clique search for constrained ternary block codes.
// Build: g++ -std=c++17 -O2 alternate.cpp -o alternate && ./alternate
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool unbordered(const string& s) {
  int n = (int)s.size();
  for (int k = 1; k < n; ++k)
    if (s.substr(0,k) == s.substr(n-k,k)) return false;
  return true;
}
bool pair_compatible(const string& a, const string& b) {
  int n = (int)a.size(), mismatch = 0;
  for (int i=0;i<n;++i) mismatch += (a[i]!=b[i]);
  if (mismatch < 3) return false;
  for (int k=1;k<n;++k) {
    if (a.compare(0,k,b,n-k,k)==0 || b.compare(0,k,a,n-k,k)==0)
      return false;
  }
  return true;
}
void generate(int n,int i,string& s,vector<string>& W) {
  if(i==n) {if(unbordered(s))W.push_back(s); return;}
  for(char c:string("012")) {s.push_back(c);generate(n,i+1,s,W);s.pop_back();}
}
void dfs(const vector<vector<uint8_t>>& A, vector<int> candidates,int depth,
         array<unsigned long long,10>& counts) {
  assert(depth<10);
  counts[depth]++;
  if(depth==9) return;
  for(size_t k=0;k<candidates.size();++k) {
    int v=candidates[k]; vector<int> next;
    for(size_t j=k+1;j<candidates.size();++j)
      if(A[v][candidates[j]]) next.push_back(candidates[j]);
    dfs(A,std::move(next),depth+1,counts);
  }
}
int main() {
  int expected_sizes[]={0,0,6,18,48,144,414};
  int expected_caps[]={0,0,1,1,2,4,8};
  int expected_opt[]={0,0,6,18,108,300,528};
  int expected_edges[]={0,0,0,0,108,2070,24156};
  for(int n=2;n<=6;++n) {
    string s; vector<string> W;generate(n,0,s,W);
    int V=(int)W.size(); assert(V==expected_sizes[n]);
    vector<vector<uint8_t>> A(V,vector<uint8_t>(V,0));
    int E=0;
    for(int i=0;i<V;++i) for(int j=i+1;j<V;++j)
      if(pair_compatible(W[i],W[j])){A[i][j]=A[j][i]=1;++E;}
    assert(E==expected_edges[n]);
    vector<int> candidates(V);
    for(int i=0;i<V;++i) candidates[i]=i;
    array<unsigned long long,10> counts={};
    dfs(A,candidates,0,counts);
    int cap=0;
    for(int i=1;i<=9;++i) if(counts[i])cap=i;
    assert(cap==expected_caps[n]);
    assert((int)counts[cap]==expected_opt[n]);
    cout << "n=" << n << " V=" << V << " E=" << E
         << " optimum=" << cap << " codebooks=" << counts[cap] << "\n";
  }
  cout << "ALTERNATE_OK\n";
}
