// Independent exact enumeration of strong-odd colour classes and partitions of GP(10,2).
// Compile: g++ -O2 -std=c++17 verify_independent.cpp -o verifier
// No nonstandard libraries or external graph data.
#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int N=20, FULL=(1<<N)-1;
array<int,N> neighbors{};
vector<int> classes;
array<vector<int>,N> byvertex;
array<vector<int>,N> square_byvertex;
long long square_covers=0;
array<long long,7> sizes{};
array<long long,7> cover_counts{};
long long profiles[3]{};

int pop(int x){return __builtin_popcount((unsigned)x);}
void record_independent(int mask){
 for(int v=0;v<N;v++) if(pop(mask&neighbors[v])==2) return;
 classes.push_back(mask); sizes[pop(mask)]++;
 for(int v=0;v<N;v++) if(mask&(1<<v)) byvertex[v].push_back(mask);
}
void enumerate_independent(int vertex,int chosen){
 if(vertex==N){record_independent(chosen);return;}
 enumerate_independent(vertex+1,chosen);
 if(!(chosen&neighbors[vertex])) enumerate_independent(vertex+1,chosen|(1<<vertex));
}
void enumerate_covers(int uncovered,int remaining,int original,vector<int>& block_sizes){
 if(uncovered==0){
  if(remaining==0){
   ++cover_counts[original];
   if(original==5){
    auto p=block_sizes;sort(p.begin(),p.end());
    if(p==vector<int>{2,3,3,6,6})++profiles[0];
    else if(p==vector<int>{3,3,4,4,6})++profiles[1];
    else if(p==vector<int>{4,4,4,4,4})++profiles[2];
    else {cerr<<"UNEXPECTED_PROFILE\n";exit(3);}
   }
  }
  return;
 }
 if(remaining==0||pop(uncovered)<remaining)return;
 int v=__builtin_ctz((unsigned)uncovered);
 for(int s:byvertex[v]) if((s&uncovered)==s){
  block_sizes.push_back(pop(s));
  enumerate_covers(uncovered^s,remaining-1,original,block_sizes);
  block_sizes.pop_back();
 }
}
void square_exact_cover(int uncovered,int blocks){
 if(uncovered==0){if(blocks==0)++square_covers;return;}
 if(blocks==0)return;
 int v=__builtin_ctz((unsigned)uncovered);
 for(int s:square_byvertex[v])if((s&uncovered)==s)square_exact_cover(uncovered^s,blocks-1);
}
int main(){
 for(int i=0;i<10;i++)for(auto [a,b]:array<pair<int,int>,3>{{{i,(i+1)%10},{i,10+i},{10+i,10+(i+2)%10}}}){
  neighbors[a]|=1<<b;neighbors[b]|=1<<a;
 }
 for(int n:neighbors)if(pop(n)!=3)return 2;
 enumerate_independent(0,0);
 array<int,N> square_neighbor{};
 for(int v=0;v<N;v++){square_neighbor[v]=neighbors[v];
  for(int u=0;u<N;u++)if(neighbors[v]&(1<<u))square_neighbor[v]|=neighbors[u];
  square_neighbor[v]&=~(1<<v);
 }
 for(int s:classes){
  bool sq=true;for(int v=0;v<N;v++)if((s&(1<<v))&&(s&square_neighbor[v])){sq=false;break;}
  if(sq)for(int v=0;v<N;v++)if(s&(1<<v))square_byvertex[v].push_back(s);
 }
 square_exact_cover(FULL,5);
 if(sizes[0]!=1||sizes[1]!=20||sizes[2]!=100||sizes[3]!=120||sizes[4]!=90||sizes[5]!=0||sizes[6]!=10)return 4;
 vector<int> current;
 enumerate_covers(FULL,4,4,current);
 enumerate_covers(FULL,5,5,current);
 cout<<"ODD_INDEPENDENT=";
 for(int i=0;i<=6;i++)cout<<sizes[i]<<(i==6?'\n':' ');
 cout<<"FOUR="<<cover_counts[4]<<" FIVE="<<cover_counts[5]<<" SQUARE_FIVE="<<square_covers<<"\n";
 cout<<"FIVE_PROFILES="<<profiles[0]<<" "<<profiles[1]<<" "<<profiles[2]<<"\n";
 if(cover_counts[4]!=0||cover_counts[5]!=212||square_covers!=2||profiles[0]!=60||profiles[1]!=100||profiles[2]!=52)return 5;
 cout<<"VERIFY_INDEPENDENT_OK\n";
}
