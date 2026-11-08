// Exact finite Potts spectrum of the truncated tetrahedral graph.
// Compile: c++ -O2 -std=c++17 verify_enum.cpp -o verify_enum && ./verify_enum
#include <array>
#include <vector>
#include <utility>
#include <iostream>
#include <cassert>
#include <algorithm>
using namespace std;
int main(){
  vector<pair<int,int>> vertex;
  for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(i!=j)vertex.push_back({i,j});
  assert(vertex.size()==12);
  vector<pair<int,int>> edges;
  for(int a=0;a<12;a++)for(int b=a+1;b<12;b++){
    auto [i,j]=vertex[a]; auto [k,l]=vertex[b];
    if(i==k || (i==l && j==k)) edges.push_back({a,b});
  }
  assert(edges.size()==18);
  const array<int,13> expected_e={4,3,2,1,0,1,2,4,6,9,12,15,18};
  const array<int,13> expected_n={24,192,504,480,120,480,384,960,480,576,192,24,1};
  array<array<long long,19>,13> hist{};
  array<int,12> a{};
  long long total=0;
  for(int z=0;z<531441;z++){
    int t=z,k=0,e=0;
    for(int j=0;j<12;j++){a[j]=t%3; t/=3; k+=(a[j]==0);}
    assert(t==0);
    for(auto [u,v]:edges)e+=(a[u]==a[v]);
    hist[k][e]++;total++;
  }
  assert(total==531441);
  for(int k=0;k<=12;k++){
    int min_e=-1; long long sum=0;
    for(int e=0;e<=18;e++){if(min_e==-1 && hist[k][e])min_e=e; sum+=hist[k][e];}
    assert(min_e==expected_e[k]);
    assert(hist[k][min_e]==expected_n[k]);
    cout<<k<<" "<<min_e<<" "<<hist[k][min_e]<<" "<<sum<<"\n";
  }
  const array<int,4> x={-1,1,2,3};
  const array<int,4> g={1320,984,1824,1273};
  for(int j=0;j<4;j++){
    int best=1000000;long long num=0;
    for(int k=0;k<=12;k++) best=min(best,expected_e[k]-x[j]*k);
    for(int k=0;k<=12;k++)if(expected_e[k]-x[j]*k==best)num+=expected_n[k];
    assert(num==g[j]);
  }
  cout<<"ALL_ASSERTIONS_PASSED\n";
}
