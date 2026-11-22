// Standalone GF(2) and geometry verifier, with the Pappus graph in LCF form.
#include <array>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <queue>
using namespace std;
int main(){
 constexpr int n=18;
 const int lcf[6]={5,7,-7,7,-7,-5};
 array<unsigned,n> adj{};
 auto edge=[&](int a,int b){assert(a!=b);adj[a]|=1u<<b;adj[b]|=1u<<a;};
 for(int a=0;a<n;a++)edge(a,(a+1)%n);
 for(int a=0;a<n;a++){
   int b=((a+lcf[a%6])%n+n)%n;
   if(a<b)edge(a,b);
 }
 unsigned M[n];
 for(int a=0;a<n;a++){
   assert(__builtin_popcount(adj[a])==3);
   M[a]=adj[a]|(1u<<a);
 }
 unsigned A[n];copy(M,M+n,A);
 vector<int> pivot;int rank=0;
 for(int c=0;c<n;c++){
   int r=rank;while(r<n && !(A[r]&(1u<<c)))r++;
   if(r==n)continue;
   swap(A[rank],A[r]);
   for(int i=0;i<n;i++)if(i!=rank && (A[i]&(1u<<c)))A[i]^=A[rank];
   pivot.push_back(c);rank++;
 }
 assert(rank==11);
 const vector<int> free={10,12,13,14,15,16,17};
 vector<unsigned> K;
 for(int c:free){
   unsigned v=1u<<c;
   for(int i=0;i<rank;i++)if(A[i]&(1u<<c))v|=1u<<pivot[i];
   for(unsigned row:M)assert((__builtin_popcount(row&v)&1)==0);
   K.push_back(v);
 }
 unsigned col[n]={};
 for(int i=0;i<n;i++)for(int j=0;j<7;j++)if((K[j]>>i)&1)col[i]|=1u<<j;
 const unsigned expected[18]={0x62,0x3d,0x0e,0x37,0x38,0x1f,0x45,0x1c,0x51,0x70,0x01,0x46,0x02,0x04,0x08,0x10,0x20,0x40};
 for(int i=0;i<n;i++)assert(col[i]==expected[i] && col[i]);
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
    assert((col[i]^col[j])!=0);
    for(int k=j+1;k<n;k++)assert((col[i]^col[j]^col[k])!=0);
 }
 map<int,int> count;
 vector<unsigned> solutions;
 for(unsigned mask=0;mask<(1u<<n);mask++){
   bool good=true;
   for(unsigned row:M)if((__builtin_popcount(row&mask)&1)!=1){good=false;break;}
   if(good){count[__builtin_popcount(mask)]++;solutions.push_back(mask);}
 }
 const map<int,int> expected_weights={{5,18},{9,92},{13,18}}; assert(count==expected_weights);
 assert(solutions.size()==128);
 // Independent orbit-free computation of distance-four witnesses.
 vector<unsigned> minsets;
 for(int v=0;v<n;v++){
   array<int,n> d;d.fill(-1);d[v]=0;queue<int>q;q.push(v);
   while(!q.empty()){
      int a=q.front();q.pop();
      for(int u=0;u<n;u++)if((adj[a]>>u&1) && d[u]<0){d[u]=d[a]+1;q.push(u);}
   }
   unsigned s=adj[v];for(int u=0;u<n;u++)if(d[u]==4)s|=1u<<u;
   assert(__builtin_popcount(s)==5);
   minsets.push_back(s);
 }
 sort(minsets.begin(),minsets.end());
 assert(unique(minsets.begin(),minsets.end())==minsets.end());
 int f=0;for(unsigned s:solutions)if(__builtin_popcount(s)==5)assert(binary_search(minsets.begin(),minsets.end(),s)),f++;
 assert(f==18);
 cout<<"PASS algebra: rank 11, nullity 7, dual distance 4, 128 coset solutions, 18 geometric minima\n";
}
