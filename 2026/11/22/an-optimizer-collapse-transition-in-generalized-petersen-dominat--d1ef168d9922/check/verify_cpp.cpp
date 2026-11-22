// Separate exhaustive verification for 1,2-dominating P(8,2), P(9,2).
// Compile: g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp
#include <array>
#include <vector>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <algorithm>
#include <cassert>
using namespace std;
using U=uint64_t;
struct Key { array<U,4> w{}; bool operator==(const Key& t)const{return w==t.w;} };
struct Hasher { size_t operator()(Key const& v)const {U x=0x9e3779b97f4a7c15ULL;for(U w:v.w)x=(x^w)*0xbf58476d1ce4e5b9ULL;return size_t(x^(x>>32));} };
int main(){
 for(int n: {8,9}){
  int N=2*n,k=6; vector<unsigned> neighbors(N);
  for(int x=0;x<N;x++){
   if(x<n)neighbors[x]=(1u<<((x+n-1)%n))|(1u<<((x+1)%n))|(1u<<(n+x));
   else {int j=x-n; neighbors[x]=(1u<<j)|(1u<<(n+(j+n-2)%n))|(1u<<(n+(j+2)%n));}
  }
  vector<unsigned> hypotheses;
  for(unsigned s=0;s<(1u<<N);s++) if(__builtin_popcount(s)==k){
    bool valid=true;
    for(int x=0;x<N;x++) if(!(s&(1u<<x))){int ct=__builtin_popcount(s&neighbors[x]);if(ct<1||ct>2){valid=false;break;}}
    if(valid)hypotheses.push_back(s);
  }
  assert(int(hypotheses.size())==(n==8?248:9));
  vector<int> counts(N+1),shattered;
  for(unsigned support=0;support<(1u<<N);support++){
   int t=__builtin_popcount(support);
   if(t>6)continue;
   unsigned long long traces=0;
   for(unsigned h:hypotheses){
     unsigned mask=0;int z=0;
     for(int x=0;x<N;x++)if(support>>x&1u){if(h>>x&1u) mask|=(1u<<z);z++;}
     traces |= (1ULL<<mask);
   }
   if(__builtin_popcountll(traces)==(1<<t)){counts[t]++;shattered.push_back(support);}
  }
  vector<int> expected=n==8?vector<int>{1,16,116,464,812,32,0}:vector<int>{1,18,81,0,0,0,0};
  for(int i=0;i<=6;i++)assert(counts[i]==expected[i]);
  int num=hypotheses.size(),words=(num+63)/64;
  vector<Key> yes(N);Key root;
  for(int i=0;i<num;i++){
   root.w[i/64]|=1ULL<<(i%64);
   for(int x=0;x<N;x++)if(hypotheses[i]>>x&1u)yes[x].w[i/64]|=1ULL<<(i%64);
  }
  unordered_map<Key,int,Hasher> memo;
  auto rank=[&](auto&& self, Key const& q)->int{
   if(auto it=memo.find(q);it!=memo.end())return it->second;
   int best=0;
   for(int x=0;x<N;x++){
    Key p,z;bool pp=false,zz=false;
    for(int w=0;w<words;w++){
     p.w[w]=q.w[w]&yes[x].w[w];z.w[w]=q.w[w]&~yes[x].w[w];
     pp|=p.w[w]!=0;zz|=z.w[w]!=0;
    }
    if(pp&&zz){int candidate=1+min(self(self,p),self(self,z));best=max(best,candidate);}
   }
   memo.emplace(q,best);return best;
  };
  int d=rank(rank,root);assert(d==(n==8?6:2));
  if(n==8){
   vector<uint8_t> issh(1u<<N);
   for(unsigned s:shattered)issh[s]=1;
   int four=0,five=0;
   for(unsigned s:shattered){
    int t=__builtin_popcount(s);if(t<4||t>5)continue;
    bool maximal=true;
    for(int j=0;j<N;j++)if(!(s>>j&1u)&&issh[s|(1u<<j)]){maximal=false;break;}
    if(maximal){four+=(t==4);five+=(t==5);}
   }
   assert(four==660&&five==32);
  }
  cout<<"n="<<n<<"; optima="<<num<<"; shattering=";
  for(int i=0;i<=6;i++)cout<<(i?",":"")<<counts[i];
  cout<<"; VC="<<(n==8?5:2)<<"; online="<<d<<"; states="<<memo.size()<<"\n";
 }
 cout<<"SECOND C++ VERIFIER PASSED\n";
}
