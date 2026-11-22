// Independent exact-cover construction of all labelled Steiner triple systems of order 7.
// Build with: c++ -O2 -std=c++17 check_fano.cpp -o check_fano && ./check_fano
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using U = uint64_t;
vector<array<int,3>> triples;
vector<array<int,2>> pairs;
vector<U> pairmask(35);
vector<U> planes;
U fullpairs=(1ULL<<21)-1;
void exact_cover(U used, U chosen) {
 if (used==fullpairs) { assert(__builtin_popcountll(chosen)==7); planes.push_back(chosen); return; }
 int p=__builtin_ctzll(fullpairs&~used);
 for(int t=0;t<35;t++) if ((pairmask[t]>>p&1) && !(pairmask[t]&used))
   exact_cover(used|pairmask[t], chosen | (1ULL<<t));
}
vector<array<int,4>> tetra;
vector<array<int,3>> tri_supports;
vector<array<int,2>> edge_supports;
vector<int> counts(5,0);
void test(const vector<int>& s) {
 int wanted=1<<s.size();
 unsigned seen=0;
 for(U plane:planes){int tr=0;for(int k=0;k<(int)s.size();k++)if(plane>>s[k]&1)tr|=1<<k;
   seen|=1u<<tr; }
 if (__builtin_popcount(seen)==wanted) {
  counts[s.size()]++;
  if(s.size()==2)edge_supports.push_back({s[0],s[1]});
  if(s.size()==3)tri_supports.push_back({s[0],s[1],s[2]});
  if(s.size()==4)tetra.push_back({s[0],s[1],s[2],s[3]});
 }
}
void subsets(int pos,int k,int remaining,vector<int>&s) {
 if(remaining==0){test(s);return;}
 if(pos==35)return;
 for(int x=pos;x<=35-remaining;x++){s.push_back(x);subsets(x+1,k,remaining-1,s);s.pop_back();}
}
int main(){
 for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)pairs.push_back({a,b});
 for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++){
  triples.push_back({a,b,c});
  U mask=0;for(int p=0;p<21;p++){
    auto [x,y]=pairs[p];
    if((x==a||x==b||x==c)&&(y==a||y==b||y==c))mask|=1ULL<<p;
  } pairmask[triples.size()-1]=mask;
 }
 exact_cover(0,0);
 sort(planes.begin(),planes.end());
 assert(planes.size()==30 && unique(planes.begin(),planes.end())==planes.end());
 for(int k=0;k<=4;k++){vector<int>s;subsets(0,k,k,s);}
 assert(counts==vector<int>({1,35,315,840,0}));
 assert(tetra.empty());
 for(auto e:edge_supports){auto a=triples[e[0]],b=triples[e[1]];
  int shared=0;for(int x:a)for(int y:b)shared+=(x==y);assert(shared==1);}
 for(auto t:tri_supports){
  int shared=0;for(int x:triples[t[0]])for(int y:triples[t[1]])for(int z:triples[t[2]])shared+=(x==y&&y==z);
  assert(shared==0);
 }
 map<pair<int,int>,int> e_index;
 for(int i=0;i<(int)edge_supports.size();i++)e_index[{edge_supports[i][0],edge_supports[i][1]}]=i;
 assert(e_index.size()==315);
 // Connectivity is tested directly on the 35-vertex graph of compatible triples.
 array<vector<int>,35> nbr;
 for(auto e:edge_supports){nbr[e[0]].push_back(e[1]);nbr[e[1]].push_back(e[0]);}
 set<int> visited={0};vector<int> queue={0};
 for(size_t k=0;k<queue.size();k++)for(int y:nbr[queue[k]])
   if(visited.insert(y).second)queue.push_back(y);
 assert(visited.size()==35);
 map<int,bitset<315>> piv;
 for(auto t:tri_supports){
  bitset<315> col;
  for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)col.set(e_index.at({t[i],t[j]}));
  for(int v=314;v>=0;v--){if(!col[v])continue;
   auto it=piv.find(v);
   if(it==piv.end()){piv[v]=col;break;}else col^=it->second;
  }
 }
 assert(piv.size()==281);
 assert(840-(int)piv.size()==559);
 cout<<"EXACT_COVER_PLANES_30_PASS\nSHATTERING_1_35_315_840_PASS\nGF2_HOMOLOGY_0_559_PASS\n";
}
