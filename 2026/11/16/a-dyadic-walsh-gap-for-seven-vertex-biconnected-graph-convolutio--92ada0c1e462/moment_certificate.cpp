// Exact biconnected-graph Walsh certificate, vertex-deletion reachability implementation.
// C++17; g++ -O3 -std=c++17 moment_certificate.cpp -o moment_certificate
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <string>
#include <utility>
#include <vector>
using namespace std;

static bool biconnected(const vector<pair<int,int>>& edge, int n, int s){
 if(__builtin_popcount((unsigned)s)<n)return false;
 int adj[7]={};
 for(int j=0;j<(int)edge.size();j++)if(s&(1<<j)){
  auto [u,v]=edge[j];adj[u]|=(1<<v);adj[v]|=(1<<u);
 }
 for(int removed=0;removed<n;removed++){
  int seen=1<<(removed==0?1:0);
  for(;;){int old=seen;
   for(int u=0;u<n;u++)if(seen&(1<<u))seen|=adj[u]&~(1<<removed);
   if(seen==old)break;
  }
  if(__builtin_popcount((unsigned)seen)!=n-1)return false;
 }
 return true;
}
static void transform(vector<int>&a){int N=a.size();for(int len=1;len<N;len*=2)
 for(int b=0;b<N;b+=2*len)for(int j=0;j<len;j++){
  int x=a[b+j],y=a[b+j+len];a[b+j]=x+y;a[b+j+len]=x-y;
 }}
static string degree_type(const vector<pair<int,int>>&e,int n,int s){
 int d[7]={};for(int j=0;j<(int)e.size();j++)if(s&(1<<j)){auto[u,v]=e[j];d[u]++;d[v]++;}
 vector<int>v;for(int i=0;i<n;i++)if(d[i])v.push_back(d[i]);sort(v.begin(),v.end());
 string t;for(int x:v)t+=to_string(x);return t;
}
int main(int argc,char**argv){int lo=3,hi=7;if(argc>1){lo=hi=stoi(argv[1]);}if(lo<3||hi>7)return 2;
 for(int n=lo;n<=hi;n++){
  vector<pair<int,int>>e;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)e.emplace_back(i,j);
  int m=e.size(),N=1<<m;vector<int>a(N);
  for(int g=0;g<N;g++)a[g]=biconnected(e,n,g);
  int total=accumulate(a.begin(),a.end(),0);
  vector<int>mom=a;
  // Superset zeta transform: mom[T] = number of admissible graphs containing T.
  for(int bit=0;bit<m;bit++)for(int mask=0;mask<N;mask++)if(!(mask&(1<<bit)))mom[mask]+=mom[mask|(1<<bit)];
  map<int,map<string,pair<int,int>>> classes;
  for(int s=0;s<N;s++){
   int w=__builtin_popcount((unsigned)s);if(w>3)continue;
   string typ=degree_type(e,n,s);auto &p=classes[w][typ];
   if(p.second==0)p.first=mom[s];else if(p.first!=mom[s]){cerr<<"ORBIT INCONSISTENCY\n";return 3;}
   p.second++;
  }
  cout<<"n="<<n<<" edge_coords="<<m<<" family="<<total<<"\n";
  for(auto &[k,c]:classes){for(auto &[key,pr]:c)cout<<"forced_edges="<<k<<" degree_type="<<(key.empty()?"none":key)<<" count="<<pr.first<<" frequency="<<pr.second<<"\n";}
  transform(a);
  map<int,int>hist;int minabs=numeric_limits<int>::max(),zero=0,min_support=m+1,minmask=-1,minsign=0;
  bool congruence4=true, congruence16=true;
  long long norm=0;for(int s=0;s<N;s++){
   int x=a[s];hist[abs(x)]++;
   if(x==0){zero++;min_support=min(min_support,__builtin_popcount((unsigned)s));}
   else if(abs(x)<minabs){minabs=abs(x);minmask=s;minsign=x;}
   congruence4 &= ((x-total)%4==0);congruence16 &= ((x-total)%16==0);
   norm+=1LL*x*x;
  }
  cout<<"zero="<<zero<<" min_absolute_nonzero="<<minabs<<" representative_frequency="<<minmask<<" representative_value="<<minsign<<" parseval="<<norm<<" predicted="<<1LL*N*total<<" congruent_mod4="<<congruence4<<" congruent_mod16="<<congruence16<<"\n";
  if(n==7)cout<<"absolute_levels="<<hist.size()<<"\n";
  static const int expected_count[8]={0,0,0,1,10,238,11368,1014888};
  static const int expected_min[8]={0,0,0,1,2,2,8,8};
  if(total!=expected_count[n]||minabs!=expected_min[n]||zero!=0||norm!=1LL*N*total)return 4;
  if((n==6||n==7)&&(!congruence16||classes[0][""].first%16!=8))return 5;
  if((n==4||n==5)&&!congruence4)return 6;
  if(n==7){
   const map<string,int> expected={{"none",1014888},{"11",581464},{"1111",335060},{"112",320432},
   {"111111",194284},{"11112",185444},{"1113",172568},{"1122",177322},{"222",168096}};
   for(auto [w,group]:classes)for(auto [deg,data]:group){string key=deg.empty()?"none":deg;
      if(expected.at(key)!=data.first)return 7;
   }
  }

 }
}
