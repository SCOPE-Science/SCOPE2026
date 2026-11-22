// Finite independent check of locating-total rook configurations.
// Compile: g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
// Run: ./verify_exhaustive
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

void test(int m,int n){
 int N=m*n; assert(N<=21);
 vector<uint32_t> adj(N,0);
 for(int a=0;a<N;a++)for(int b=0;b<N;b++)
  if(a!=b&&(a/n==b/n||a%n==b%n))adj[a]|=1u<<b;
 vector<long long> actual(N+1),structural(N+1);
 for(uint32_t S=0;S<(1u<<N);S++){
  vector<uint32_t> signature(N);
  bool good=true;
  for(int a=0;a<N;a++){
   signature[a]=adj[a]&S;
   if(!signature[a]){good=false;break;}
  }
  if(good)for(int a=0;a<N&&good;a++)if(!(S&(1u<<a)))
   for(int b=a+1;b<N;b++)if(!(S&(1u<<b))&&signature[a]==signature[b])
    {good=false;break;}
  vector<int> row(m),col(n);
  for(int a=0;a<N;a++)if(S&(1u<<a)){row[a/n]++;col[a%n]++;}
  int isolates=0;
  for(auto x:row)if(!x)isolates++;
  for(auto x:col)if(!x)isolates++;
  bool structure=isolates<=1;
  for(int a=0;a<N;a++)if((S&(1u<<a)) && row[a/n]==1&&col[a%n]==1)
   structure=false;
  if(good!=structure){cerr<<"Mismatch "<<m<<" "<<n<<" mask="<<S<<endl;exit(2);}
  if(good && __builtin_popcount(S)==max(n-1,(2*(m+n-1)+2)/3)){
   vector<int> parent(m+n);for(int i=0;i<m+n;i++)parent[i]=i;
   auto root=[&](int x){while(x!=parent[x])x=parent[x];return x;};
   bool cyclic=false;
   for(int a=0;a<N;a++)if(S&(1u<<a)){
    int u=root(a/n),v=root(m+a%n);
    if(u==v){cyclic=true;break;}
    parent[u]=v;
   }
   if(cyclic){cerr<<"Optimum is cyclic: "<<m<<" "<<n<<endl;exit(5);}
  }
  if(good)actual[__builtin_popcount(S)]++;
  if(structure)structural[__builtin_popcount(S)]++;
 }
 if(actual!=structural)exit(3);
 int least=0;while(least<=N&&!actual[least])least++;
 int expect=max(n-1,(2*(m+n-1)+2)/3);
 if(least!=expect){cerr<<"Incorrect min "<<m<<" "<<n<<" "<<least<<" "<<expect<<endl;exit(4);}
 cout<<m<<"x"<<n<<": min="<<least<<" min_count="<<actual[least]<<" total=";
 long long total=0;for(auto x:actual)total+=x;cout<<total<<"\n";
}
int main(){
 for(int m=2;m<=4;m++)for(int n=m;n<=6;n++)if(m*n<=20)test(m,n);
 cout<<"EXHAUSTIVE_OK\n";
}
