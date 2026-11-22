// Reproducible finite checks for hop-total Roman domination of KG(n,3).
// This enumerates all choices of vertices labelled 2 whose weight can reach the bound;
// vertices not at distance two from a defender must then have label 1.
#include <bits/stdc++.h>
using namespace std;
long long choose3(int a){return a<3?0:1LL*a*(a-1)*(a-2)/6;}
int target(int n){return 2*(n/3)-(n%3==0);}
int main(){
 for(int n=8;n<=12;n++){
  vector<unsigned> v;
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++)
   v.push_back((1u<<i)|(1u<<j)|(1u<<k));
  int q=v.size(), best=target(n);long long count=0, low=LLONG_MAX, total=0;
  vector<int> in(q,0),dist(q,-1),D;
  // Direct graph-distance verification: all distinct intersecting triples at distance 2.
  for(int a=0;a<q;a++){
   fill(dist.begin(),dist.end(),-1);queue<int> Q;dist[a]=0;Q.push(a);
   while(!Q.empty()) {int z=Q.front();Q.pop();for(int b=0;b<q;b++)
      if(dist[b]<0 && !(v[z]&v[b])){dist[b]=dist[z]+1;Q.push(b);}}
   for(int b=0;b<q;b++)if(a!=b && dist[b]!=( (v[a]&v[b])?2:1)){
    cerr<<"distance mismatch at n="<<n<<"\n";return 1;}
  }
  auto check=[&](){
   unsigned uni=0;for(int i:D)uni |= v[i];int uncovered=n-__builtin_popcount(uni);
   int needed=2*(int)D.size()+choose3(uncovered);
   low=min(low, (long long)needed);
   if(needed!=best)return;
   vector<int> pos=D;
   for(int i=0;i<q;i++)if(!(v[i]&uni)) pos.push_back(i); // mandatory 1-vertices
   // All positive vertices have a graph neighbor among positives.
   for(int i:pos){bool ok=false;for(int j:pos)if(i!=j && !(v[i]&v[j])){ok=true;break;}if(!ok)return;}
   // Every zero vertex has a defender at distance exactly two.
   for(int i=0;i<q;i++){
    if(find(pos.begin(),pos.end(),i)!=pos.end())continue;
    bool ok=false;
    for(int j:D)if(i!=j && (v[i]&v[j])){ok=true;break;}
    if(!ok){cerr<<"bad zero";exit(2);}
   }
   count++;
  };
  function<void(int,int)> recur=[&](int start,int rem){
   if(rem==0){total++;check();return;}
   for(int i=start;i<=q-rem;i++){D.push_back(i);recur(i+1,rem-1);D.pop_back();}
  };
  for(int m=1;m<=best/2;m++)recur(0,m);
  cout<<"n="<<n<<" tested="<<total<<" minimum_base="<<low<<" optimum="<<best<<" optimal_labelings="<<count<<"\n";
 }
}
