#include <bits/stdc++.h>
using namespace std;
using U=unsigned long long;
int main(){
 const vector<array<int,3>> lines={{0,1,2},{0,3,4},{0,5,6},{1,3,5},{1,4,6},{2,3,6},{2,4,5}};
 set<vector<int>> planes;
 array<int,7>perm={0,1,2,3,4,5,6};
 do {int inv=0;for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)inv+=(perm[a]>perm[b]);if(inv%2)continue;
   vector<int> fl; for(auto v:lines){fl.push_back((1<<perm[v[0]])|(1<<perm[v[1]])|(1<<perm[v[2]]));}sort(fl.begin(),fl.end());planes.insert(fl);
 }while(next_permutation(perm.begin(),perm.end()));
 assert(planes.size()==15);
 vector<int> triples;for(int t=0;t<(1<<7);t++)if(__builtin_popcount((unsigned)t)==3)triples.push_back(t);
 assert(triples.size()==35);
 U adj[50]={}; int f=0;
 for(const auto &fl:planes){for(int t=0;t<35;t++)if(binary_search(fl.begin(),fl.end(),triples[t])){
   int a=f,b=15+t;adj[a]|=1ULL<<b;adj[b]|=1ULL<<a;
  }f++;}
 for(int i=0;i<35;i++)for(int j=i+1;j<35;j++)if(!(triples[i]&triples[j])){
    int a=15+i,b=15+j;adj[a]|=1ULL<<b;adj[b]|=1ULL<<a;
  }
 for(int i=0;i<50;i++){
  assert(__builtin_popcountll(adj[i])==7);
  for(int j=i+1;j<50;j++){int common=__builtin_popcountll(adj[i]&adj[j]); assert(common==((adj[i]>>j)&1?0:1));}
 }
 const U FULL=(1ULL<<50)-1;
 auto propagate=[&](U chosen)->int{
    U covered=chosen;
    for(int u=0;u<50;u++)if((chosen>>u)&1)covered|=adj[u];
    int rounds=1;
    while(covered!=FULL){
      U force=0;
      for(int u=0;u<50;u++)if((covered>>u)&1){
       U white=adj[u]&(~covered);
       if(white && __builtin_popcountll(white)==1)force|=white;
      }
      if(!force)return 0;
      covered|=force;
      rounds++;
    }
    return rounds;
 };
 map<tuple<int,int,int>,long long>counts;
 for(int k=5;k<=6;k++){
   long long tested=0,good=0;
   int a[6];iota(a,a+k,0);
   while(true){
    U set=0; for(int q=0;q<k;q++)set|=1ULL<<a[q];
    tested++;
    int rounds=propagate(set);
    if(rounds){good++;
      int e=0;for(int q=0;q<k;q++)for(int h=q+1;h<k;h++)e+=(adj[a[q]]>>a[h])&1;
      counts[{k,rounds,e}]++;
    }
    int i=k-1;while(i>=0&&a[i]==50-k+i)--i;
    if(i<0)break;
    ++a[i];for(int j=i+1;j<k;j++)a[j]=a[j-1]+1;
   }
   cerr<<"FANO size="<<k<<" tested="<<tested<<" success="<<good<<"\n";
 }
 for(auto [key,c]:counts){ auto [k,r,e]=key;cout<<k<<" "<<r<<" "<<e<<" "<<c<<"\n";}
}
