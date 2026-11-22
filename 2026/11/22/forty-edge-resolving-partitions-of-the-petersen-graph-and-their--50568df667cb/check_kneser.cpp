// Self-contained exact enumeration of edge-resolving vertex partitions of KG(5,2).
// Build: g++ -std=c++17 -O2 check_kneser.cpp -o check_kneser && ./check_kneser
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using Partition=vector<vector<int>>;
int main(){
 vector<pair<int,int>> labels;
 for(int a=0;a<5;a++)for(int b=a+1;b<5;b++)labels.push_back({a,b});
 const int N=10;
 int distance[N][N];
 vector<pair<int,int>> edges;
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)distance[i][j]=(i==j?0:2);
 for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
  auto [a,b]=labels[i];auto [c,d]=labels[j];
  if(a!=c&&a!=d&&b!=c&&b!=d){distance[i][j]=distance[j][i]=1;edges.push_back({i,j});}
 }
 assert(edges.size()==15);
 vector<array<int,N>> edist;
 for(auto [a,b]:edges){array<int,N> d{};for(int v=0;v<N;v++)d[v]=min(distance[a][v],distance[b][v]);edist.push_back(d);}
 array<long long,11> counts{};
 map<vector<int>,int> size_profiles;
 set<vector<vector<int>>> optima;
 long long three=0,three_at_most_six=0,three_limited_pairs=0,three_limit_adjacent_singletons=0;
 int word[N]={};
 auto verify=[&](int k){
  vector<vector<int>> blocks(k);
  for(int v=0;v<N;v++)blocks[word[v]].push_back(v);
  if(k==3){
   ++three;
   int cross=0,pairc[3][3]{};
   for(auto [u,v]:edges)if(word[u]!=word[v]){cross++;pairc[min(word[u],word[v])][max(word[u],word[v])]++;}
   if(cross<=6){
    ++three_at_most_six;
    bool limited=1;
    for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)if(pairc[i][j]>2)limited=0;
    if(limited){
     ++three_limited_pairs;
     vector<int> singles;
     for(auto b:blocks)if(b.size()==1)singles.push_back(b[0]);
     if(singles.size()==2 && distance[singles[0]][singles[1]]==1)++three_limit_adjacent_singletons;
    }
   }
  }
  vector<array<int,10>> signatures;
  for(auto e:edist){array<int,10> s{};s.fill(99);
   for(int b=0;b<k;b++)for(int v:blocks[b])s[b]=min(s[b],e[v]);
   signatures.push_back(s);
  }
  sort(signatures.begin(),signatures.end());
  if(unique(signatures.begin(),signatures.end())!=signatures.end())return;
  ++counts[k];
  if(k==4){
   vector<int> prof;for(auto b:blocks)prof.push_back(b.size());sort(prof.begin(),prof.end());size_profiles[prof]++;
   for(auto &b:blocks)sort(b.begin(),b.end());sort(blocks.begin(),blocks.end());optima.insert(blocks);
  }
 };
 auto visit=[&](auto&& self,int i,int k)->void{
  if(i==N){verify(k);return;}
  for(int z=0;z<=k;z++){word[i]=z;self(self,i+1,max(k,z+1));}
 };
 visit(visit,1,1);
 cout<<"vertices=10 edges="<<edges.size()<<"\n";
 cout<<"edge_partition_polynomial=";
 for(int k=1;k<=N;k++)if(counts[k])cout<<" "<<k<<":"<<counts[k];
 cout<<"\n";
 cout<<"three_partitions="<<three<<" crossing_le6="<<three_at_most_six
     <<" pair_multiplicities_le2="<<three_limited_pairs
     <<" adjacent_singletons="<<three_limit_adjacent_singletons<<"\n";
 for(auto [p,n]:size_profiles){cout<<"four_block_size_profile=";for(int z:p)cout<<z<<",";cout<<" count="<<n<<"\n";}
 auto rep=*optima.begin();
 set<vector<vector<int>>> orbit;
 vector<int> perm={0,1,2,3,4};
 do{
  vector<vector<int>> image;
  for(auto block:rep){vector<int> b;
   for(int v:block){int a=perm[labels[v].first],c=perm[labels[v].second];if(a>c)swap(a,c);
    int j=int(find(labels.begin(),labels.end(),make_pair(a,c))-labels.begin());assert(j<N);b.push_back(j);
   }sort(b.begin(),b.end());image.push_back(b);
  }sort(image.begin(),image.end());orbit.insert(image);
 }while(next_permutation(perm.begin(),perm.end()));
 cout<<"minimum_orbit="<<orbit.size()<<" optimum_count="<<optima.size()<<" orbit_equals_optima="<<(orbit==optima)<<"\n";
 cout<<"representative_blocks=";for(auto block:rep){cout<<"{";for(int v:block){cout<<labels[v].first<<labels[v].second<<" ";}cout<<"}";}cout<<"\n";
 assert(counts[1]==0&&counts[2]==0&&counts[3]==0&&counts[4]==40&&counts[5]==11965&&counts[6]==14877&&counts[7]==5045&&counts[8]==720&&counts[9]==45&&counts[10]==1);
 assert(three==9330&&three_at_most_six==105&&three_limited_pairs==15&&three_limit_adjacent_singletons==15);
 assert(size_profiles.size()==1&&size_profiles.begin()->first==vector<int>({1,3,3,3}));
 assert(orbit==optima);
 cout<<"KG5_CHECK_OK\n";
}
