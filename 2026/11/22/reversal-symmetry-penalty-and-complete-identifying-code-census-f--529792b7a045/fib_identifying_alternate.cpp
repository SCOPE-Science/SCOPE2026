// Alternate exact checks: exhaustive set enumeration for dimensions 2--6,
// independent fixed-point enumeration at dimension 7, and a direct audit
// of all thirteen explicitly listed dimension-seven solutions.
// Compile: g++ -std=c++17 -O3 fib_identifying_alternate.cpp -o alternate
// Run: ./alternate OPTIMA_N7.tsv
#include <algorithm>
#include <bitset>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <set>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
struct G{int n;vector<string> w;vector<U> balls;vector<int> reversals;
 G(int n):n(n){for(int mask=0;mask<(1<<n);++mask){if(mask&(mask<<1))continue;
 string s;for(int j=n-1;j>=0;--j)s+=char('0'+((mask>>j)&1));w.push_back(s);}
 for(auto s:w){U b=0;for(size_t j=0;j<w.size();++j){int d=0;for(int k=0;k<n;++k)d+=(s[k]!=w[j][k]);if(d<=1)b|=U(1)<<j;}balls.push_back(b);
  reverse(s.begin(),s.end());auto q=find(w.begin(),w.end(),s);if(q==w.end())throw 1;reversals.push_back(int(q-w.begin()));}
 }
 bool check(U mask)const{set<U> sig;
 for(U b:balls){U v=b&mask;if(!v||!sig.insert(v).second)return false;}return true;}
 bool inv(U mask)const{for(size_t i=0;i<w.size();++i)if(bool((mask>>i)&1)!=bool((mask>>reversals[i])&1))return false;return true;}
};
int main(int argc,char**argv){if(argc!=2)return 2;
 const int minvals[]={0,0,2,3,4,5,8},numvals[]={0,0,1,6,14,2,18};
 const int revmin[]={0,0,2,3,4,6,8}, revcount[]={0,0,1,2,2,8,2};
 for(int n=2;n<=6;++n){G g(n);int mini=100,counts=0,rm=100,rc=0;
  for(U s=0;s<(U(1)<<g.w.size());++s){int c=__builtin_popcountll(s);bool sym=g.inv(s);
   if(c>mini&&(!sym||c>rm))continue;
   if(!g.check(s))continue;
   if(c<mini){mini=c;counts=0;}if(c==mini)++counts;
   if(sym){if(c<rm){rm=c;rc=0;}if(c==rm)++rc;}
  }
  if(mini!=minvals[n]||counts!=numvals[n]||rm!=revmin[n]||rc!=revcount[n])return 3;
 }
 G g(7);vector<U> orbital;vector<int>visited(g.w.size());
 for(size_t i=0;i<g.w.size();++i)if(!visited[i]){int j=g.reversals[i];visited[i]=visited[j]=1;orbital.push_back((U(1)<<i)|(U(1)<<j));}
 int rm=100,rc=0;
 for(U q=0;q<(U(1)<<orbital.size());++q){U s=0;for(size_t j=0;j<orbital.size();++j)if(q>>j&1)s|=orbital[j];int k=__builtin_popcountll(s);if(k>rm||!g.check(s))continue;
 if(k<rm){rm=k;rc=0;}if(k==rm)++rc;
 }
 if(rm!=12||rc!=5)return 4;
 ifstream file(argv[1]);if(!file)return 5;set<U>seen;string line;int fixed=0;
 while(getline(file,line)){if(line.empty())return 6;istringstream in(line);string x;U s=0;int items=0;
  while(in>>x){auto it=find(g.w.begin(),g.w.end(),x);if(it==g.w.end())return 7;U bit=U(1)<<int(it-g.w.begin());if(s&bit)return 8;s|=bit;++items;}
  if(items!=12||!g.check(s)||!seen.insert(s).second)return 9;
  if(g.inv(s))++fixed;
 }
 if(seen.size()!=13||fixed!=5)return 10;
 cout<<"ALTERNATE_OK\n";
}
