// Exhaustive integer verification of seven-vertex convex noncrossing-tree Walsh data.
// Compile: c++ -O2 -std=c++17 check_prufer.cpp -o check_prufer && ./check_prufer
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
int main() {
  constexpr int n=7,m=21,N=1<<m;
  vector<pair<int,int>> edge;
  int eid[n][n];
  for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
    eid[i][j]=eid[j][i]=(int)edge.size();edge.emplace_back(i,j);
  }
  vector<uint32_t> cross(m,0);
  for(int i=0;i<m;i++)for(int j=0;j<m;j++){
    auto [a,b]=edge[i];auto [c,d]=edge[j];
    if((a<c && c<b && b<d) || (c<a && a<d && d<b))cross[i]|=1u<<j;
  }
  vector<int32_t> w(N,0);vector<int> one(m,0);
  int count=0;
  // Prüfer codes bijectively enumerate all 7^(7-2) labelled spanning trees.
  constexpr int codes=16807;
  for(int seed=0;seed<codes;seed++){
    int d[n];fill(d,d+n,1);int code[n-2],v=seed;
    for(int j=0;j<n-2;j++){code[j]=v%n;v/=n;d[code[j]]++;}
    int treeedge[n-1];int ne=0;
    for(int j=0;j<n-2;j++){
      int leaf=0;while(d[leaf]!=1)leaf++;
      treeedge[ne++]=eid[leaf][code[j]];
      d[leaf]--;d[code[j]]--;
    }
    int a=-1,b=-1;
    for(int j=0;j<n;j++)if(d[j]==1){if(a<0)a=j;else b=j;}
    treeedge[ne++]=eid[a][b];assert(ne==n-1);
    uint32_t bits=0;bool good=true;
    for(int j=0;j<ne;j++){
      if(bits&cross[treeedge[j]]){good=false;break;}
      bits|=1u<<treeedge[j];
    }
    if(!good)continue;
    assert(w[bits]==0); w[bits]=1;count++;
    for(int j=0;j<ne;j++)one[treeedge[j]]++;
  }
  assert(count==1428);
  // Boundary, length-2, length-3 chord edge incidence counts.
  for(int j=0;j<m;j++){
    auto [a,b]=edge[j];int length=min(b-a,n-(b-a));
    assert(one[j]==(length==1?728:length==2?286:210));
  }
  auto fwht=[&](vector<int32_t>&x){
    for(int step=1;step<N;step<<=1)
      for(int i=0;i<N;i+=step*2)
        for(int j=0;j<step;j++){
          int u=x[i+j],v=x[i+j+step];
          x[i+j]=u+v;x[i+j+step]=u-v;
        }
  };
  fwht(w);
  int zeros=0,least=1428,gcd=0,twozeros=0;
  vector<int32_t> projection(N,0);
  for(int k=0;k<N;k++){
    int x=w[k];gcd=std::gcd(gcd,abs(x));
    if(x==0){zeros++;if(__builtin_popcount((unsigned)k)==2)twozeros++;}
    else{least=min(least,abs(x));projection[k]=1;}
  }
  assert(w[0]==1428 && zeros==160484 && twozeros==14 && least==4 && gcd==4);
  fwht(projection);
  uint64_t l1numerator=0;
  for(int x:projection)l1numerator+=uint64_t(abs(x));
  assert(l1numerator==312904152ULL);
  assert(projection[0]==N-zeros);
  cout<<"PRUFER_WALSH_PASS count="<<count<<" zeros="<<zeros
      <<" rank="<<(N-zeros)<<" min="<<least<<" gcd="<<gcd
      <<" twozeros="<<twozeros<<" projection_l1_numer="<<l1numerator
      <<" projection_l1_denom="<<N<<"\n";
}
