// Exact integer-bit verification of reverse-complement-invariant binary
// cross-bifix-free codes: a pivoted maximal-clique census.
// Compile: g++ -std=c++17 -O3 verify_independent.cpp -o verifier && ./verifier
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <utility>
using namespace std;
using U = unsigned __int128;
static int N, length_n, optimal, num_opt, num_nodes;
static vector<vector<int>> orbit_words;
static vector<int> weights;
static vector<U> neighbor;
static const int ans[13]={0,2,1,0,1,0,2,0,5,2,14,10,42};
static const int counts[13]={0,1,2,1,2,1,2,1,2,4,6,96,1134};
int ones(U x){return __builtin_popcountll((uint64_t)x)+__builtin_popcountll((uint64_t)(x>>64));}
int first(U x){uint64_t lo=(uint64_t)x;return lo?__builtin_ctzll(lo):64+__builtin_ctzll((uint64_t)(x>>64));}
int rc(int x,int n){int r=0;for(int i=0;i<n;i++){r=(r<<1)|(1-(x&1));x>>=1;}return r;}
bool overlap(int x,int y,int n){for(int k=1;k<n;k++){
 int mask=(1<<k)-1;
 if((x>>(n-k))==(y&mask)||(y>>(n-k))==(x&mask))return true;
}return false;}
int weight_sum(U b){int r=0;while(b){int k=first(b);r+=weights[k];b&=b-1;}return r;}
void recurse(U P,U X,int total){
 ++num_nodes;
 if(!(P|X)){
   if(total>optimal){optimal=total;num_opt=0;}
   if(total==optimal)++num_opt;
   return;
 }
 if(total+weight_sum(P)<optimal)return;
 U Ux=P|X;
 int pivot=-1, score=-1;
 while(Ux){int i=first(Ux);int s=ones(P&neighbor[i]);
   if(s>score){score=s;pivot=i;} Ux&=Ux-1;}
 U candidates=P & ~neighbor[pivot];
 while(candidates){int i=first(candidates);U b=U(1)<<i;
   recurse(P&neighbor[i],X&neighbor[i],total+weights[i]);
   P&=~b;X|=b;candidates&=~b;
 }
}
void check(int n){
 length_n=n;orbit_words.clear();weights.clear();neighbor.clear();
 if(n==1){cout<<"n=1 M=2 N=1\n";return;}
 vector<char> seen(1<<n,0);
 for(int x=0;x<(1<<n);x++){
   if(seen[x])continue;
   int y=rc(x,n);seen[x]=seen[y]=1;
   vector<int> o={x};if(x!=y)o.push_back(y);
   bool good=true;
   for(int a:o)for(int b:o)if(overlap(a,b,n))good=false;
   if(good)orbit_words.push_back(o);
 }
 N=orbit_words.size();assert(N<=128);
 neighbor.resize(N,U(0));
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j){
   bool compatible=true;
   for(int a:orbit_words[i])for(int b:orbit_words[j])
      if(overlap(a,b,n))compatible=false;
   if(compatible)neighbor[i]|=U(1)<<j;
 }
 for(auto &o:orbit_words)weights.push_back(o.size());
 optimal=-1;num_opt=0;num_nodes=0;
 recurse((U(1)<<N)-1,0,0);
 cout<<"n="<<n<<" orbits="<<N<<" M="<<optimal<<" N="<<num_opt
     <<" nodes="<<num_nodes<<"\n";
 assert(optimal==ans[n]&&num_opt==counts[n]);
}
int main(){for(int n=1;n<=12;n++)check(n);cout<<"PASS: independent bitwise verification\n";}
