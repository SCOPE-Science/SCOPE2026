// Independent direct NOC-condition enumeration: no witness-cache updates.
#include <vector>
#include <iostream>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
using namespace std;
struct Direct {
 int n,full; vector<int> mids,chosen; vector<uint64_t> counts; uint64_t visited=0,accepted=0;
 bool good() {
  for(int c:chosen){
   int used=0;
   for(int d:chosen) if(d!=c) {
     int v=c&d;
     if(v && v!=c && v!=d) used |=d;
   }
   if((c & ~used)==0) return false;
  }
  return true;
 }
 int retic() {
  vector<int> ss=chosen;
  ss.push_back(full);
  for(int i=0;i<n;i++)ss.push_back(1<<i);
  int ct=0;
  for(int u:ss){
   int par=0;
   for(int v:ss) {
    if(v==u || (v&u)!=u)continue;
    bool cover=true;
    for(int w:ss) if(w!=u && w!=v && (w&u)==u && (w&v)==w){cover=false;break;}
    par+=cover;
   }
   ct +=par>=2;
  }
  return ct;
 }
 void visit(int i){
  visited++;
  if(i==(int)mids.size()){accepted++;int k=retic(); if(k>=(int)counts.size())counts.resize(k+1); counts[k]++;return;}
  visit(i+1);
  chosen.push_back(mids[i]);
  if(good())visit(i+1);
  chosen.pop_back();
 }
 void run(int N){n=N;full=(1<<n)-1; for(int m=1;m<full;m++) if(__builtin_popcount((unsigned)m)>=2) mids.push_back(m);
 // Increasing mask, deliberately different from grouped descending-size order.
 visit(0);cout<<"n="<<n<<" accepted="<<accepted<<" visited="<<visited<<"\n";
 for(int k=0;k<(int)counts.size();k++)cout<<"k="<<k<<" count="<<counts[k]<<"\n";
 }
};
int main(int argc,char**argv){Direct d;d.run(argc>1?atoi(argv[1]):6);}
