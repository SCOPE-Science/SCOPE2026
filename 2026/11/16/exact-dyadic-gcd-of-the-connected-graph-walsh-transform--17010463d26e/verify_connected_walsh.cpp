// Exact independent checks for connected-graph Walsh divisibility.
// Compile: g++ -std=c++17 -O2 verify_connected_walsh.cpp -o verify
// Run: ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;
using i64 = long long;

static void hadamard(vector<i64>& a) {
    const int N = (int)a.size();
    for (int h=1; h<N; h*=2) for(int i=0; i<N; i+=2*h)
      for(int j=i; j<i+h; ++j) {
        i64 x=a[j], y=a[j+h]; a[j]=x+y; a[j+h]=x-y;
      }
}

static void subset_zeta(vector<i64>& a, int m) {
    const int N = (int)a.size();
    for(int e=0; e<m; ++e) for(int mask=0; mask<N; ++mask)
      if(mask & (1<<e)) a[mask] += a[mask ^ (1<<e)];
}

static i64 fact(int n) {i64 a=1; for(int i=2;i<=n;++i)a*=i;return a;}

int main() {
 const i64 connected_expected[] = {0,1,1,4,38,728,26704,1866256};
 const i64 zero_expected[] = {0,0,0,3,0,230,7872,318647};
 for (int n=1;n<=7;++n) {
    vector<pair<int,int>> edges;
    for(int u=0;u<n;u++)for(int v=u+1;v<n;v++) edges.push_back({u,v});
    const int m=(int)edges.size(), N=1<<m, all=N-1;
    // Method I: exhaustive simple-graph connectivity + Walsh-Hadamard transform.
    vector<i64> w(N,0);
    i64 num_connected=0;
    for(int graph=0;graph<N;++graph) {
      int parent[7];iota(parent,parent+n,0);
      auto root=[&](int x) {while(parent[x]!=x) x=parent[x];return x;};
      for(int e=0;e<m;++e) if(graph&(1<<e)) {
        int a=root(edges[e].first),b=root(edges[e].second);parent[a]=b;
      }
      bool conn=true;
      for(int v=1;v<n;++v)if(root(v)!=root(0)){conn=false;break;}
      w[graph]=conn?1:0;
      num_connected += w[graph];
    }
    hadamard(w);

    // Method II: partition-lattice Möbius weights + a subset zeta transform.
    // This uses no graph-connectivity decisions and no Fourier butterfly.
    vector<i64> z(N,0);int blocks[7]={};i64 partitions=0;
    auto visit=[&](auto&& self,int i,int k)->void {
      if(i==n) {
        int internal=0;
        for(int e=0;e<m;++e)
          if(blocks[edges[e].first]==blocks[edges[e].second]) internal|=1<<e;
        i64 weight=((k-1)&1 ? -1LL:1LL)*fact(k-1);
        weight*=1LL<<__builtin_popcount((unsigned)internal);
        assert(z[internal]==0); // within-block edge set uniquely identifies a partition
        z[internal]=weight;
        ++partitions;
        return;
      }
      for(int b=0;b<k;++b){blocks[i]=b;self(self,i+1,k);}
      blocks[i]=k;self(self,i+1,k+1);
    };
    blocks[0]=0;visit(visit,1,1);
    i64 gcd_weights=0;
    for(i64 a:z) gcd_weights=std::gcd(gcd_weights,a);
    subset_zeta(z,m);
    i64 common=0,zero=0,min_nonzero=INT64_MAX;
    for(int mask=0;mask<N;++mask) {
      if(w[mask]!=z[all^mask]) {
        cerr<<"MISMATCH n="<<n<<" mask="<<mask<<"\n";
        return 2;
      }
      common=std::gcd(common,w[mask]);
      if(w[mask]==0) ++zero;
      else min_nonzero=min(min_nonzero,llabs(w[mask]));
    }
    int L=0;while((1<<(L+1))<=n)++L;
    i64 expected=1LL<<(n-1-L);
    assert(common==expected && gcd_weights==expected);
    assert(num_connected==connected_expected[n] && zero==zero_expected[n]);
    cout<<"n="<<n<<" connected="<<num_connected<<" partitions="<<partitions
        <<" Fourier_frequencies="<<N<<" zeros="<<zero
        <<" gcd="<<common<<" min_nonzero="<<min_nonzero<<" PASS\n";
 }
 cout<<"CONNECTED_GRAPH_WALSH_GCD_PASS all_spectra_n=1..7 two_independent_algorithms\n";
}
