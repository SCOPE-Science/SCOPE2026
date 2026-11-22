// Independent exact enumeration from the cyclic (13,4,1) difference set.
// Build: c++ -O2 -std=c++17 check_singer.cpp -o check_singer
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;
int main(){
  constexpr int n=13, full=(1<<n)-1;
  const array<int,4> difference={0,1,3,9};
  vector<int> lines;
  for(int k=0;k<n;k++){
    int mask=0;
    for(int j:difference)mask |= 1<<((k+j)%n);
    lines.push_back(mask);
  }
  assert(set<int>(lines.begin(),lines.end()).size()==13);
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++){
    int pairs=0;
    for(int line:lines)if((line&(1<<a))&&(line&(1<<b)))pairs++;
    assert(pairs==1);
  }
  // Explicit isomorphism from sorted normalized F_3^3 projective points.
  // The map is the Singer indexing of the orbit of (0,0,1), multiplied by 2.
  const array<int,13> field_to_singer={0,5,7,4,11,10,6,2,12,8,3,9,1};
  set<int> obtained;
  vector<array<int,3>> p;
  for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++){
    if(!(x||y||z))continue;
    int factor= x ? x : (y ? y:z);
    int inv= factor==1 ? 1:2;
    array<int,3> v={x*inv%3,y*inv%3,z*inv%3};
    if(find(p.begin(),p.end(),v)==p.end())p.push_back(v);
  }
  sort(p.begin(),p.end()); assert(p.size()==13);
  for(auto cov:p){
    int mask=0;
    for(int j=0;j<n;j++){
      int dot=0;
      for(int c=0;c<3;c++)dot+=p[j][c]*cov[c];
      if(dot%3==0)mask|=1<<field_to_singer[j];
    }
    obtained.insert(mask);
  }
  assert(obtained==set<int>(lines.begin(),lines.end()));
  vector<char> ok(1<<n,false);
  vector<int> vertices,counts(n+1);
  for(int x=0;x<=full;x++){
    bool allowed=true;
    for(int l:lines)if((x&l)==0||(x&l)==l){allowed=false;break;}
    if(allowed){ok[x]=1;vertices.push_back(x);counts[__builtin_popcount((unsigned)x)]++;}
  }
  assert(vertices.size()==468 && counts[6]==234 && counts[7]==234);
  vector<int> adjdegree(1<<n,0);
  for(int v:vertices)for(int k=0;k<n;k++)if(ok[v^(1<<k)])adjdegree[v]++;
  for(int v:vertices)assert(adjdegree[v]==3);
  map<pair<int,int>,long long> hist;
  long long geodesic=0,detour=0;
  vector<int> dist(1<<n, -1);
  array<int,14> expected_shell={1,3,6,12,24,48,72,96,116,68,12,6,3,1};
  for(size_t ii=0;ii<vertices.size();ii++){
    int start=vertices[ii];
    fill(dist.begin(),dist.end(),-1);
    queue<int> q;q.push(start);dist[start]=0;
    array<int,14> layers{};
    int reached=0;
    while(!q.empty()){
      int v=q.front();q.pop(); reached++;
      assert(dist[v]<=13);layers[dist[v]]++;
      for(int b=0;b<n;b++){
        int w=v^(1<<b);
        if(ok[w]&&dist[w]==-1){dist[w]=dist[v]+1;q.push(w);}
      }
    }
    assert(reached==468 && layers==expected_shell);
    assert(dist[start^full]==13);
    for(size_t jj=ii+1;jj<vertices.size();jj++){
      int target=vertices[jj];
      int h=__builtin_popcount((unsigned)(start^target));
      int d=dist[target];assert(d>=h && (d-h==0||d-h==2));
      hist[{h,d}]++;
      if(h==d)geodesic++;else detour++;
    }
  }
  const map<pair<int,int>,long long> expect={
   {{1,1},702}, {{2,2},1404}, {{3,3},2808},
   {{4,4},5616}, {{4,6},2808}, {{5,5},11232}, {{5,7},5616},
   {{6,6},14040}, {{6,8},10296}, {{7,7},16848}, {{7,9},7488},
   {{8,8},16848}, {{9,9},8424}, {{10,10},2808}, {{11,11},1404},
   {{12,12},702}, {{13,13},234}
  };
  assert(hist==expect);
  assert(geodesic==83070 && detour==26208);
  cout<<"PASS: cyclic Singer difference set, and explicit field-incidence isomorphism\n";
  cout<<"states=468 edges=702 radius=13 diameter=13 degrees=3\n";
  cout<<"geodesic=83070 extra_two=26208 other_excess=0\n";
  for(auto [key,num]:hist)cout<<key.first<<" "<<key.second<<" "<<num<<"\n";
}
