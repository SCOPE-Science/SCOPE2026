// Standalone exhaustive verifier by the edge-degree parity criterion.
// Vertex i of KG(n,2) is the ith edge of K_n; adjacency means disjointness.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
long long count_connected_odd(int n, int k){
 vector<pair<int,int>> es;
 for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)es.emplace_back(a,b);
 int N=(int)es.size();
 vector<int> chosen;
 long long result=0;
 auto dfs=[&](auto&& self,int start)->void{
  if((int)chosen.size()==k){
   if((k&1)==0)return;
   vector<int> deg(n);
   for(int i:chosen){auto [a,b]=es[i];++deg[a];++deg[b];}
   for(int a=1;a<n;++a)if((deg[a]&1)!=(deg[0]&1))return;
   int seen=1,old=0;
   while(old!=seen){
    old=seen;
    for(int i=0;i<k;++i)if(seen&(1<<i))for(int j=0;j<k;++j){
     auto [a,b]=es[chosen[i]]; auto [c,d]=es[chosen[j]];
     if(a!=c&&a!=d&&b!=c&&b!=d)seen|=1<<j;
    }
   }
   if(seen==(1<<k)-1)++result;
   return;
  }
  int remain=k-(int)chosen.size();
  for(int i=start;i<=N-remain;++i){chosen.push_back(i);self(self,i+1);chosen.pop_back();}
 };
 dfs(dfs,0);
 return result;
}
long long choose(int n,int k){long long z=1;for(int i=1;i<=k;++i)z=z*(n-k+i)/i;return z;}
int main(){
 for(int n=5;n<=10;++n){
  long long a=count_connected_odd(n,1), b=count_connected_odd(n,3);
  long long c=count_connected_odd(n,5);
  long long expected=12*choose(n,5)+(n==8?840:0)+(n==10?945:0);
  assert(a==0);
  assert(b==(n==6?15:0));
  assert(c==expected || n==6); // n=6 not a minimum-size test
  cout<<"n="<<n<<" size1="<<a<<" size3="<<b<<" size5="<<c;
  cout<<" minimum="<<(n==6?3:5)<<" minimum_count="<<(n==6?b:c)<<"\n";
 }
 cout<<"PARITY CHECK PASS\n";
}
