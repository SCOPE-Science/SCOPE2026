// Independent bit-mask reproduction of two-rainbow antipodal classifications.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
using U=unsigned long long;

void add(vector<U>& adj,int a,int b){adj[a]|=1ULL<<b; adj[b]|=1ULL<<a;}
vector<U> ico(){vector<U>a(12);for(int i=0;i<5;i++){
 int u=2+i,v=7+i;
 add(a,0,u);add(a,1,v);
 add(a,u,2+(i+1)%5);add(a,v,7+(i+1)%5);
 add(a,u,v);add(a,u,7+(i+4)%5);
 }return a;}
vector<U> j63(){vector<unsigned> t;for(int i=0;i<64;i++)if(__builtin_popcount((unsigned)i)==3)t.push_back(i);
 vector<U>a(t.size());for(size_t i=0;i<t.size();i++)for(size_t j=i+1;j<t.size();j++)
 if(__builtin_popcount(t[i]&t[j])==2)add(a,i,j);return a;}
void solve(const vector<U>&a,int target){
 int n=a.size(),degree=__builtin_popcountll(a[0]); U full=(1ULL<<n)-1;
 assert(n==2*(degree+1));
 vector<pair<U,int>> pairs;
 for(int i=0;i<n;i++){
  assert(__builtin_popcountll(a[i])==degree);assert(!(a[i]&(1ULL<<i)));
  for(int j=i+1;j<n;j++)pairs.push_back({(1ULL<<i)|(1ULL<<j), i*n+j});
 }
 auto good=[&](U p,U q){U empties=full&~(p|q);
  while(empties){int v=__builtin_ctzll(empties);empties&=empties-1;
   if(!(a[v]&p)||!(a[v]&q))return false;
  }return true;};
 vector<U> anti;
 for(auto [p,id]:pairs)if((a[id/n]&a[id%n])==0 && !(a[id/n]&(1ULL<<(id%n)))){
  // Only distance-three pairs have no common neighbor in these diameter-three examples.
  anti.push_back(p);
 }
 assert((int)anti.size()==n/2);
 for(U p:anti){int x=__builtin_ctzll(p),y=__builtin_ctzll(p&~(1ULL<<x));
  assert((a[x]|a[y])==(full&~p));}
 int count=0;
 for(auto [p,_]:pairs)for(auto [q,__]:pairs){
  bool valid=good(p,q);
  bool predicted=find(anti.begin(),anti.end(),p)!=anti.end()&&find(anti.begin(),anti.end(),q)!=anti.end();
  assert(valid==predicted);if(valid)count++;
 }
 assert(count==target);
 for(int weight=0;weight<=3;weight++)for(int x=0;x<=weight;x++){
  int y=weight-x;
  for(U p=0;p<=full;p++)if(__builtin_popcountll(p)==x){
   for(U q=0;q<=full;q++)if(__builtin_popcountll(q)==y)assert(!good(p,q));
  }
 }
 cout<<"n="<<n<<" degree="<<degree<<" antipodal_pairs="<<anti.size()<<" functions="<<count<<"\n";
}
int main(){solve(ico(),36);solve(j63(),100);cout<<"PASS\n";}
