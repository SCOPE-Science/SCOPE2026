// Exhaustive check of the domination-query shattering polynomial on a 5-by-5 rook board.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  const int n=5;
  vector<uint32_t> concepts;
  int total=1;
  for(int i=0;i<n;i++) total*=n;
  for(int code=0;code<total;code++) {
    int v=code;uint32_t row=0,col=0;
    for(int i=0;i<n;i++) {int x=v%n;v/=n; row|=(1u<<(n*i+x));col|=(1u<<(n*x+i));}
    concepts.push_back(row);concepts.push_back(col);
  }
  sort(concepts.begin(),concepts.end());concepts.erase(unique(concepts.begin(),concepts.end()),concepts.end());
  assert(concepts.size()==6130);
  uint64_t counts[n+1]={};
  for(int k=0;k<=n;k++) {
    vector<int> s(k);
    for(int i=0;i<k;i++)s[i]=i;
    bool go=true;
    while(go) {
      uint64_t seen=0,all=(1ULL<<(1u<<k))-1ULL;
      for(uint32_t d:concepts) {
        unsigned tr=0;
        for(int j=0;j<k;j++) tr|=((d>>s[j])&1u)<<j;
        seen|=1ULL<<tr;
        if(seen==all)break;
      }
      bool actual=(seen==all),row=false,col=false;
      unsigned r=0,c=0;
      for(int x:s) {r|=1u<<(x/n);c|=1u<<(x%n);}
      row=__builtin_popcount(r)==k;col=__builtin_popcount(c)==k;
      if(actual!=(row||col)){cerr<<"MISMATCH k="<<k<<"\n";return 2;}
      counts[k]+=actual;
      if(k==0)break;
      int pos=k-1;
      while(pos>=0&&s[pos]==25-k+pos)pos--;
      if(pos<0)go=false;
      else {s[pos]++; for(int j=pos+1;j<k;j++)s[j]=s[j-1]+1;}
    }
  }
  uint64_t expected[]={1,25,300,1900,5650,6130};
  for(int k=0;k<=5;k++){assert(counts[k]==expected[k]);cout<<"k="<<k<<" shattered="<<counts[k]<<"\n";}
  cout<<"SUCCESS: all supports of size at most five checked; all larger supports excluded by domination cardinality five.\n";
}
