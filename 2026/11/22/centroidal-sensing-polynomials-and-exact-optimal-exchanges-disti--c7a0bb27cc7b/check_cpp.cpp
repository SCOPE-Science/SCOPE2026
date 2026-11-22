// Exhaustive centroidal-detection census for two labelled sixteen-vertex graphs.
// Build: c++ -O2 -std=c++17 check_cpp.cpp -o check_cpp && ./check_cpp
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Matrix = array<array<int, 16>, 16>;

Matrix build(bool rook) {
  Matrix a{};
  const array<pair<int,int>,6> moves = {{{1,0},{3,0},{0,1},{0,3},{1,1},{3,3}}};
  for (int u=0;u<16;u++) for (int v=0;v<16;v++) if (u!=v) {
    int dx = ((v/4-u/4)+4)%4, dy = ((v%4-u%4)+4)%4;
    if (rook) a[u][v] = (u/4==v/4 || u%4==v%4);
    else for (auto [x,y] : moves) if (dx==x && dy==y) a[u][v]=1;
  }
  for (int x=0;x<16;x++) {
    assert(accumulate(a[x].begin(), a[x].end(),0)==6);
    for (int y=0;y<16;y++) {
      int n=0;for(int t=0;t<16;t++)n+=a[x][t]*a[y][t];
      if(x!=y) assert(n==2);
    }
  }
  return a;
}

Matrix distances(const Matrix& a) {
  Matrix d{};
  for(int s=0;s<16;s++) {
    d[s].fill(100);d[s][s]=0;queue<int> q;q.push(s);
    while(!q.empty()) {
      int x=q.front();q.pop();
      for(int y=0;y<16;y++) if(a[x][y] && d[s][y]>d[s][x]+1) {
        d[s][y]=d[s][x]+1;q.push(y);
      }
    }
    assert(*max_element(d[s].begin(),d[s].end())==2);
  }
  return d;
}

// Ordered partitions, with empty distance layers removed. The entries are
// subsets of the globally-labelled set of detectors; distances themselves
// are deliberately forgotten, preserving only their relative order.
vector<int> signature(const Matrix& dist,int location,int mask) {
  vector<int> parts;
  for(int k=0;k<=2;k++) {
    int group=0;
    for(int sensor=0;sensor<16;sensor++)
      if((mask>>sensor&1) && dist[location][sensor]==k) group |= 1<<sensor;
    if(group)parts.push_back(group);
  }
  return parts;
}

bool resolves(const Matrix& dist,int mask) {
  set<vector<int>> sigs;
  for(int location=0;location<16;location++)
    if(!sigs.insert(signature(dist,location,mask)).second) return false;
  return true;
}

void run(bool rook) {
  auto a=build(rook),d=distances(a);
  array<int,17> hist{};vector<int> bases;array<unsigned char,65536> yes{};
  for(int mask=0;mask<65536;mask++) {
    if(resolves(d,mask)) {
      hist[__builtin_popcount((unsigned)mask)]++;
      yes[mask]=1;
      if(__builtin_popcount((unsigned)mask)==5) bases.push_back(mask);
    }
  }
  const array<int,17> expected = rook ?
    array<int,17>{0,0,0,0,0,2112,7024,11248,12858,11440,8008,4368,1820,560,120,16,1} :
    array<int,17>{0,0,0,0,0,1728,6736,11152,12846,11440,8008,4368,1820,560,120,16,1};
  assert(hist==expected);
  assert(bases.size()==static_cast<size_t>(rook?2112:1728));
  array<int,17> maximal_bad{};
  for(int m=0;m<65536;m++)if(!yes[m]){
    bool maximal=true;
    for(int x=0;x<16;x++)if(!(m>>x&1) && !yes[m|(1<<x)]) {maximal=false;break;}
    if(maximal) maximal_bad[__builtin_popcount((unsigned)m)]++;
  }
  const array<int,17> expected_bad = rook ?
    array<int,17>{0,0,0,0,144,0,72,96,12,0,0,0,0,0,0,0,0} :
    array<int,17>{0,0,0,0,48,0,24,96,24,0,0,0,0,0,0,0,0};
  assert(maximal_bad==expected_bad);

  map<int,int> idx;for(int i=0;i<(int)bases.size();i++)idx[bases[i]]=i;
  vector<vector<int>> neighbors(bases.size());
  for(int i=0;i<(int)bases.size();i++) {
    int mask=bases[i];
    for(int p=0;p<16;p++)if(mask>>p&1)
      for(int q=0;q<16;q++)if(!(mask>>q&1)) {
        int change=mask^(1<<p)^(1<<q);
        auto it=idx.find(change);
        if(it!=idx.end())neighbors[i].push_back(it->second);
      }
  }
  long long degree_sum=0;map<int,int> deg_hist;
  for(auto &v:neighbors){degree_sum+=v.size();deg_hist[v.size()]++;}
  assert(degree_sum/2==(rook?30624:22176));
  queue<int> que;vector<int> seen(bases.size());int components=0;
  for(int i=0;i<(int)bases.size();i++)if(!seen[i]) {
    components++;que.push(i);seen[i]=1;
    while(!que.empty()){int v=que.front();que.pop();for(int w:neighbors[v])if(!seen[w]){seen[w]=1;que.push(w);}}
  }
  assert(components==1);
  int diam=0,rad=9999;map<int,int> ecc_hist;
  for(int i=0;i<(int)bases.size();i++) {
    vector<int> dd(bases.size(),-1);queue<int> qq;qq.push(i);dd[i]=0;
    while(!qq.empty()) {int v=qq.front();qq.pop();for(int w:neighbors[v])if(dd[w]==-1){dd[w]=dd[v]+1;qq.push(w);}}
    int ecc=*max_element(dd.begin(),dd.end());
    diam=max(ecc,diam);rad=min(ecc,rad);ecc_hist[ecc]++;
  }
  cout<<(rook?"rook":"shrikhande")<<" coefficient:";
  for(int k=0;k<=16;k++)cout<<" "<<hist[k];
  cout<<"\nmaximal_failures:";
  for(int k=0;k<=16;k++)if(maximal_bad[k])cout<<" "<<k<<":"<<maximal_bad[k];
  cout<<"\nexchange edges="<<degree_sum/2<<", components="<<components<<", radius="<<rad<<", diameter="<<diam<<"\ndegrees:";
  for(auto [a,b]:deg_hist)cout<<" "<<a<<":"<<b;
  cout<<"\neccentricities:";for(auto [a,b]:ecc_hist)cout<<" "<<a<<":"<<b;cout<<"\n";
}
int main(){run(false);run(true);cout<<"ALL CHECKS PASS\n";}
