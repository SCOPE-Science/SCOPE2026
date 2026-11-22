// Standalone independent pair-witness certificate. Compile with: g++ -O2 -std=c++17 verify_witness.cpp -o verify_witness
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <utility>
#include <vector>
using namespace std;
using ll=long long;
ll choose(int n,int k){if(k<0 || k>n)return 0;ll r=1;for(int i=1;i<=k;i++)r=r*(n-k+i)/i;return r;}
map<int,ll> predicted(int m,int n,int t){
  map<int,ll> a;
  for(int j=0;j<=t;j++) {a[j]+=2*choose(t,j);a[j+1]+=(m+n-2*t)*choose(t,j);}
  a[0]--;a[2]+=t;
  for(auto it=a.begin();it!=a.end();) if(it->second==0)it=a.erase(it);else ++it;
  return a;
}
void run(int m,int n,int t){
  const int N=m+n;
  vector<pair<int,int>> E;
  vector<vector<int>> adj(N);
  for(int a=0;a<m;a++)for(int b=0;b<n;b++)if(!(a==b && a<t)){
    E.push_back({a,m+b});adj[a].push_back(m+b);adj[m+b].push_back(a);
  }
  vector<vector<int>> d(N,vector<int>(N,999));
  for(int s=0;s<N;s++){
    queue<int> q;q.push(s);d[s][s]=0;
    while(!q.empty()){int x=q.front();q.pop();for(int y:adj[x])if(d[s][y]==999){d[s][y]=d[s][x]+1;q.push(y);}}
    for(int v=0;v<N;v++)assert(d[s][v]<999);
  }
  // A set distinguishes an edge pair if it contains a witness vertex.
  // Build witness bit masks independently from Python's tuple-of-signatures test.
  vector<unsigned> distinguish;
  for(size_t i=0;i<E.size();i++)for(size_t j=i+1;j<E.size();j++){
    unsigned w=0;
    for(int v=0;v<N;v++){
      auto a=E[i],b=E[j];
      int da=min(d[v][a.first],d[v][a.second]);
      int db=min(d[v][b.first],d[v][b.second]);
      if(da!=db)w|=1u<<v;
    }
    assert(w);distinguish.push_back(w);
  }
  map<int,ll> count;
  for(unsigned mask=0;mask<(1u<<N);mask++){
    bool good=true;
    for(auto [a,b]:E)if(!(mask & ((1u<<a)|(1u<<b)))){good=false;break;}
    if(!good)continue;
    for(unsigned w:distinguish)if(!(mask&w)){good=false;break;}
    if(good)count[N-__builtin_popcount(mask)]++;
  }
  if(count!=predicted(m,n,t)){
    cerr<<"FAIL "<<m<<" "<<n<<" "<<t<<"\n";abort();
  }
}
int main(){
  int cases=0;
  for(int m=3;m<=7;m++)for(int n=3;n<=7;n++)if(m+n<=12)
    for(int t=0;t<=min(m,n);t++){run(m,n,t);cases++;}
  cout<<"PASS: all "<<cases<<" cases, m,n>=3 and m+n<=12, all t; "
      <<"pair-witness masks and exhaustive cover checks.\n";
}
