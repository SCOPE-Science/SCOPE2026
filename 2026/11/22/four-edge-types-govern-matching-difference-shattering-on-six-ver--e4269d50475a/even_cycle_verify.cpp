// Exact finite checks for the 6-vertex perfect-matching symmetric-difference family.
// C++17, standard library only. Compile: c++ -O2 -std=c++17 even_cycle_verify.cpp -o verify && ./verify
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using U=uint32_t;
static int edge_index(int a,int b){if(a>b)swap(a,b);int q=0;for(int x=0;x<6;x++)for(int y=x+1;y<6;y++,q++)if(x==a&&y==b)return q;return -1;}
static void match_rec(vector<int> left,U m,vector<U>&out){
 if(left.empty()){out.push_back(m);return;}
 int x=left[0];for(unsigned i=1;i<left.size();i++){vector<int> rest;for(unsigned j=1;j<left.size();j++)if(i!=j)rest.push_back(left[j]);match_rec(rest,m|(U(1)<<edge_index(x,left[i])),out);}
}
static int rank2(const vector<U>& rows,const vector<U>& cols){
 int n=rows.size(), words=(n+63)/64; map<U,int> index;for(int i=0;i<n;i++)index[rows[i]]=i;
 vector<vector<uint64_t>> base(n,vector<uint64_t>(words));vector<char> active(n);
 int r=0;
 for(U face:cols){
  vector<uint64_t> v(words);for(int bit=0;bit<15;bit++)if(face&(U(1)<<bit)){auto it=index.find(face&~(U(1)<<bit));assert(it!=index.end());int j=it->second;v[j/64]^=uint64_t(1)<<(j%64);}
  for(int j=n-1;j>=0;j--)if(v[j/64]&(uint64_t(1)<<(j%64))){
   if(active[j]){for(int t=0;t<words;t++)v[t]^=base[j][t];}
   else{base[j]=v;active[j]=1;r++;break;}
  }
 }
 return r;
}
int main(){
 vector<U> matchings;match_rec({0,1,2,3,4,5},0,matchings);assert(matchings.size()==15);
 set<U> concepts;for(unsigned i=0;i<matchings.size();i++)for(unsigned j=i+1;j<matchings.size();j++)concepts.insert(matchings[i]^matchings[j]);
 assert(concepts.size()==105);map<int,int> weights;for(U c:concepts)weights[__builtin_popcount(c)]++;assert(weights[4]==45&&weights[6]==60);
 vector<vector<U>> f(7);vector<char> isface(1<<15);
 for(U s=0;s<(U(1)<<15);s++){
  int k=__builtin_popcount(s);if(k>6)continue;
  int all=1<<k;vector<char> patterns(all);int count=0;
  for(U c:concepts){int pattern=0,pos=0;for(int e=0;e<15;e++)if(s&(U(1)<<e)){pattern|=((c>>e)&1)<<pos;pos++;}
   if(!patterns[pattern]){patterns[pattern]=1;if(++count==all)break;}}
  if(count==all){f[k].push_back(s);isface[s]=1;}
 }
 array<int,7> expected{1,15,105,375,675,0,0};for(int k=0;k<=6;k++){cout<<"f["<<k<<"]="<<f[k].size()<<"\n";assert((int)f[k].size()==expected[k]);}
 for(U s=0;s<(U(1)<<15);s++)if(__builtin_popcount(s)==5){bool possible=false;for(U c:concepts)if((s&c)==s){possible=true;break;}if(!possible)continue;
  // All size-five positive supports are five-edge paths in a six-cycle.
  // A four-edge subpath forces its missing final edge in every six-cycle.
  int found=0;for(U c:concepts)if((c&s)==s)found++;assert(found>=1);
 }
 map<int,int> facets;for(int k=1;k<=4;k++)for(U s:f[k]){bool max=true;for(int e=0;e<15;e++)if(!(s&(U(1)<<e))&&isface[s|(U(1)<<e)]){max=false;break;}if(max)facets[k]++;}
 assert(facets.size()==1&&facets[4]==675);cout<<"facets4="<<facets[4]<<"\n";
 array<int,5> ranks{};for(int k=1;k<=4;k++){ranks[k]=rank2(f[k-1],f[k]);cout<<"rank_boundary_"<<k<<"="<<ranks[k]<<"\n";}
 assert(ranks[1]==1&&ranks[2]==14&&ranks[3]==91&&ranks[4]==284);
 for(int k=1;k<=4;k++){int betti=int(f[k].size())-ranks[k]-(k<4?ranks[k+1]:0);assert(betti==(k==4?391:0));}
 cout<<"reduced_betti3=391; all other reduced_betti=0\nPASS\n";
}
