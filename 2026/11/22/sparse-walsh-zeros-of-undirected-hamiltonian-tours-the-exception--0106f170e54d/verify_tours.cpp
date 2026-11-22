// Independent direct enumeration of undirected Hamilton cycles, integer arithmetic only.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
using Edge = pair<int,int>;
static uint64_t mask_of(const vector<Edge>& s, const int e[10][10]) {
    uint64_t m=0;
    for (auto [a,b]:s) m|=1ULL<<e[a][b];
    return m;
}
static long long direct(int n,const vector<vector<Edge>>& tests,const vector<long long>& expected){
    int e[10][10];for(auto &row:e) for(int&z:row) z=-1;
    int m=0;for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)e[u][v]=e[v][u]=m++;
    vector<uint64_t> fs;for(const auto&t:tests)fs.push_back(mask_of(t,e));
    vector<long long> total(fs.size(),0);
    vector<int> p(n-1);iota(p.begin(),p.end(),1);
    long long C=0;
    do {
      if (p.front()>p.back()) continue;
      uint64_t tour=0;int a=0;
      for(int b:p){tour|=1ULL<<e[a][b];a=b;}
      tour|=1ULL<<e[a][0];C++;
      for(size_t j=0;j<fs.size();j++)total[j]+=__builtin_parityll(tour&fs[j])?-1:1;
    }while(next_permutation(p.begin(),p.end()));
    long long fact=1;for(int z=2;z<n;z++)fact*=z;
    assert(C==fact/2);
    for(size_t j=0;j<tests.size();j++){
      if (expected[j]!=total[j]){
       cerr<<"FAIL n="<<n<<" j="<<j<<" expected="<<expected[j]<<" got="<<total[j]<<"\n";
       abort();
      }
    }
    cout<<"n="<<n<<" cycles="<<C<<" checked_masks="<<tests.size()<<" PASS\n";
    return C;
}
int main(){
 vector<Edge> triangle={{0,1},{0,2},{1,2}};
 vector<Edge> star={{0,1},{0,2},{0,3}};
 vector<Edge> plus=triangle;plus.push_back({3,4});
 vector<Edge> starplus=star;starplus.push_back({4,5});
 vector<vector<Edge>> S={triangle,star,plus,starplus,{{0,1}},{{0,1},{2,3}}};
 // Independent fixed numeric values evaluated using direct tours; first 4 are important zeros.
 // Expected for n=9: triangular and star signs -1440, both four-edge signs 0;
 // one-edge and disjoint-two-edge values 10080 and 5760.
 direct(9,S,{-1440,-1440,0,0,10080,5760});
 // n=10: 3-edge cases vanish; 4-edge cases are nonzero.
 direct(10,S,{0,0,5760,5760,100800,60480});
 cout<<"PASS\n";
}
