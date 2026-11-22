// Exact enumeration of closed-neighborhood error-detecting identifying codes.
// Vertex i=4*r+c; the graph is either K_4 square K_4 or the Shrikhande Cayley graph.
#include <array>
#include <iostream>
#include <cstdint>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
using namespace std;
using M=uint32_t;
int countb(M x){return __builtin_popcount(x);}
array<M,16> make_graph(bool shr){
 array<M,16> N{};
 const set<pair<int,int>> steps={{1,0},{3,0},{0,1},{0,3},{1,1},{3,3}};
 for(int i=0;i<16;i++)for(int j=0;j<16;j++){
  int r=i/4,c=i%4,s=j/4,t=j%4;
  bool arc=shr? (steps.count({(s-r+4)%4,(t-c+4)%4})>0) : (i!=j && (r==s||c==t));
  if(i==j||arc)N[i]|=M(1)<<j;
 }
 return N;
}
void run(const char* name,bool shr){
 auto N=make_graph(shr);
 for(int i=0;i<16;i++){
  if(countb(N[i])!=7 || !(N[i]&(M(1)<<i))){cerr<<"invalid degree\n";exit(1);}
  for(int j=0;j<16;j++)if(i!=j){
   bool adj=(N[i]>>j)&1;
   if(adj!=bool((N[j]>>i)&1)) {cerr<<"asymmetry\n";exit(1);}
   M common=(N[i]&N[j])&~((M(1)<<i)|(M(1)<<j));
   if(countb(common)!=(adj?2:2)){cerr<<"wrong SRG parameters\n";exit(1);}
  }
 }
 vector<pair<M,M>> diffs;
 for(int i=0;i<16;i++)for(int j=i+1;j<16;j++)diffs.emplace_back(N[i]&~N[j],N[j]&~N[i]);
 array<uint32_t,17> histogram{};vector<int> optimum;
 for(M S=0;S<65536;S++){
  bool ok=true;
  for(M n:N)if(countb(S&n)<2){ok=false;break;}
  if(!ok)continue;
  for(auto [A,B]:diffs)if(countb(S&A)<2&&countb(S&B)<2){ok=false;break;}
  if(!ok)continue;
  histogram[countb(S)]++;
  if(countb(S)==10)optimum.push_back(S);
 }
 cout<<name<<" graph=16,6,2,2 histogram=";
 for(int k=0;k<=16;k++)if(histogram[k])cout<<k<<":"<<histogram[k]<<",";
 cout<<" minimum10="<<optimum.size()<<"\n";
 if(histogram[10]!= (shr?256u:720u) || histogram[11]!=(shr?1392u:1920u) || histogram[12]!=(shr?1424u:1496u))exit(2);
 for(int k=0;k<10;k++)if(histogram[k])exit(3);
}
int main(){run("rook",false);run("shrikhande",true);}
