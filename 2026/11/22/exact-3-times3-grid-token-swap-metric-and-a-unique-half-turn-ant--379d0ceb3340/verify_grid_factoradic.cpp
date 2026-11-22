/* Independent exact census for all nine-token configurations of the 3x3 grid.
 * The representation is the factorial number system, unlike the byte-string
 * dictionary used in verify_grid.py.  Compile: c++ -O2 -std=c++17 ... -o check
 */
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
constexpr int N=9;
int F[10];
int encode(const array<int,N>& p){
  int s=0;
  for(int i=0;i<N;i++){
    int smaller=0;
    for(int j=i+1;j<N;j++) smaller+=(p[j]<p[i]);
    s+=smaller*F[N-1-i];
  }
  return s;
}
array<int,N> decode(int r){
  array<int,N> p{};
  int pool[N]; iota(pool,pool+N,0); int remaining=N;
  for(int i=0;i<N;i++){
    int index=r/F[N-1-i]; r%=F[N-1-i];
    p[i]=pool[index];
    for(int j=index;j<remaining-1;j++)pool[j]=pool[j+1];
    --remaining;
  }
  return p;
}
int main(){
  F[0]=1; for(int i=1;i<=N;i++)F[i]=i*F[i-1];
  vector<pair<int,int>> E;
  for(int v=0;v<N;v++){
    if(v%3<2)E.push_back({v,v+1});
    if(v/3<2)E.push_back({v,v+3});
  }
  assert(E.size()==12);
  vector<int> dist(F[N],-1), queue(F[N]);
  int head=0,tail=1;queue[0]=0;dist[0]=0;
  while(head<tail){
    int r=queue[head++]; auto p=decode(r);
    assert(encode(p)==r);
    for(auto [u,v]:E){
      swap(p[u],p[v]);int s=encode(p);
      if(dist[s]==-1){dist[s]=dist[r]+1;queue[tail++]=s;}
      swap(p[u],p[v]);
    }
  }
  assert(tail==F[N]);
  vector<int> histogram(17),gap(6);int anti=0;
  for(int r=0;r<F[N];r++){
    auto p=decode(r);int d=dist[r];assert(d>=0 && d<=16);
    ++histogram[d];
    int distance_sum=0;
    for(int v=0;v<N;v++)distance_sum+=abs(v/3-p[v]/3)+abs(v%3-p[v]%3);
    int excess=d-(distance_sum+1)/2;
    assert(0<=excess && excess<=5);++gap[excess];
    if(d==16){++anti;assert(r==F[N]-1);}
  }
  const vector<int> H={1,12,88,470,1978,6658,18081,38936,65246,
                       83000,76688,48316,18975,4024,382,24,1};
  const vector<int> G={98647,167522,84339,11850,502,20};
  assert(histogram==H && gap==G && anti==1);
  cout<<"PASS: 362880 states, 12 generators, diameter 16, one antipode, "
      <<"max lower-bound excess 5 (20 states)\n";
}
