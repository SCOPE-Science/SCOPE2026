// Exact cyclic double-deletion spectrum verifier.
// Compile: g++ -O2 -std=c++17 verify_two_deletion.cpp -o verify && ./verify
#include <bits/stdc++.h>
using namespace std;
uint64_t canonical(uint64_t w, int len) {
    uint64_t mask=(uint64_t(1)<<len)-1, best=w;
    for (int i=1;i<len;i++) {
        w=((w<<1)&mask)|(w>>(len-1));
        best=min(best,w);
    }
    return best;
}
array<int,3> spectrum(const string &w) {
    const int N=w.size();
    unordered_set<uint64_t> outputs[3];
    for (int i=0;i<N;i++) for (int j=i+1;j<N;j++) {
        uint64_t value=0;int ones=0;
        for (int k=0;k<N;k++) if (k!=i && k!=j) {
            int b=w[k]-'0'; value=(value<<1)|b;ones+=b;
        }
        int index=ones-(N/2-2);
        if(index<0 || index>2) throw logic_error("composition");
        outputs[index].insert(canonical(value,N-2));
    }
    return {(int)outputs[0].size(),(int)outputs[1].size(),(int)outputs[2].size()};
}
int main(){
 for(int n=3;n<=5;n++) {
  int N=1<<n, M=N/2, mask=M-1;int checked=0;
  array<int,3> expected{N*N/32, N*N/16-N/4, N*N/32};
  for(int choices=0;choices<(1<<M);choices++) {
   vector<bool> visited(N);vector<int> edges;int e=0;
   while(!visited[e]){
    visited[e]=true;edges.push_back(e);
    int v=e&mask, b=((e>>(n-1))&1)^((choices>>v)&1);
    e=((e<<1)&(N-1))|b;
   }
   if((int)edges.size()!=N || e!=0) continue;
   string w;for(int x:edges)w+=char('0'+(x>>(n-1)));
   if(spectrum(w)!=expected) throw logic_error("spectrum mismatch");
   ++checked;
  }
  int total_known=(n==3?2:n==4?16:2048);
  if(checked!=total_known) throw logic_error("exhaustiveness mismatch");
  cout<<"order="<<n<<" cycles="<<checked<<" spectrum=("<<expected[0]<<","<<expected[1]<<","<<expected[2]<<") OK\n";
 }
 // One random 64-bit successor table need not give a single Euler tour;
 // sample 2000 deterministic tables and test each complete tour found.
 const int n=6,N=1<<n,M=N/2,mask=M-1;mt19937_64 rng(21879);int sampled=0;
 for(int i=0;i<2000;i++){
   auto choices=rng();vector<bool> seen(N);vector<int> edges;int e=0;
   while(!seen[e]){seen[e]=true;edges.push_back(e);int v=e&mask;
    int b=((e>>(n-1))&1)^((choices>>v)&1);e=((e<<1)&(N-1))|b;}
   if((int)edges.size()!=N||e!=0) continue;
   string w;for(int x:edges)w+=char('0'+(x>>(n-1)));
   if(spectrum(w)!=array<int,3>{128,240,128}) throw logic_error("sample mismatch");
   sampled++;
 }
 cout<<"order=6 sample="<<sampled<<" spectrum=(128,240,128) OK\n";
 cout<<"VERIFY_OK\n";
}
