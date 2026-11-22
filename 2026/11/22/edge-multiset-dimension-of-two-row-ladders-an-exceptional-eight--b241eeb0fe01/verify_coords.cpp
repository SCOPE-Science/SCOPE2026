// Coordinate-distance edge-multiset verification, C++17, no dependencies.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
using Edge=pair<int,int>;
int distance(int x,int y){return abs(x/2-y/2)+(x%2!=y%2);}
vector<Edge> makeEdges(int n){
 vector<Edge> e;
 for(int t=0;t<n;t++)e.emplace_back(2*t,2*t+1);
 for(int t=0;t+1<n;t++)for(int r=0;r<2;r++)e.emplace_back(2*t+r,2*(t+1)+r);
 return e;
}
bool works(int n,const vector<int>& s,const vector<Edge>& edges){
 set<vector<int>> sig;
 for(auto [a,b]:edges){
  vector<int> v;
  for(int x:s)v.push_back(min(distance(x,a),distance(x,b)));
  sort(v.begin(),v.end());
  if(!sig.insert(v).second)return false;
 }
 return true;
}
long long countK(int n,int k,const vector<Edge>& e){
 int m=2*n; vector<int> choose(m);fill(choose.end()-k,choose.end(),1);
 long long cnt=0;
 do {
  vector<int>s;for(int i=0;i<m;i++)if(choose[i])s.push_back(i);
  cnt+=works(n,s,e);
 }while(next_permutation(choose.begin(),choose.end()));
 return cnt;
}
int main(){
 for(int n=2;n<=8;n++){
  auto e=makeEdges(n); int maxk=(n<=4)?2*n:(n==7?3:4);
  vector<long long> cnt;
  for(int k=0;k<=maxk;k++)cnt.push_back(countK(n,k,e));
  vector<long long> ref(maxk+1,0);
  if(n==5)ref[4]=4; if(n==6)ref[4]=20;
  if(n==7)ref[3]=4; if(n==8)ref[4]=80;
  assert(cnt==ref);
  cout<<"n="<<n<<" ";for(auto x:cnt)cout<<x<<",";cout<<"\n";
 }
 for(int n=7;n<=256;n++){
   if(n==8)continue;
   vector<int> S={0,2*(n%2?2:3),2*(n-1)};
   assert(works(n,S,makeEdges(n)));
 }
 cout<<"COORDINATE_EXACT_AND_FAMILY_WITNESS_OK\n";
}
