// Reproducible finite mathematical verification; C++17, no external dependencies.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <unordered_set>
#include <vector>
using namespace std;
static int pc(int x){return __builtin_popcount((unsigned)x);}
static int rank_mod2(const vector<int>& lower, const vector<int>& upper, int m){
    map<int,int> ix;for(int i=0;i<(int)lower.size();++i)ix[lower[i]]=i;
    int W=(lower.size()+63)/64;vector<vector<unsigned long long>> piv(lower.size());int rank=0;
    for(int x:upper){
        vector<unsigned long long> col(W,0);
        for(int b=0;b<m;++b)if(x&(1<<b)){
            auto it=ix.find(x^(1<<b)); assert(it!=ix.end());
            int row=it->second;col[row/64]^=1ULL<<(row%64);
        }
        while(true){
            int j=W-1;while(j>=0&&!col[j])--j;
            if(j<0)break;
            int row=j*64+63-__builtin_clzll(col[j]);
            if(piv[row].empty()){piv[row]=move(col);++rank;break;}
            for(int t=0;t<=j;++t)col[t]^=piv[row][t];
        }
    }
    return rank;
}
static int canonical(int mask,int n,const vector<pair<int,int>>& edges){
    vector<int> perm(n);iota(perm.begin(),perm.end(),0);int best=(1<<edges.size())-1;
    do{
        int newmask=0;
        for(int b=0;b<(int)edges.size();++b)if(mask&(1<<b)){
            int u=perm[edges[b].first],v=perm[edges[b].second];
            if(u>v)swap(u,v);
            for(int z=0;z<(int)edges.size();++z)if(edges[z].first==u&&edges[z].second==v){newmask|=1<<z;break;}
        }
        best=min(best,newmask);
    }while(next_permutation(perm.begin(),perm.end()));
    return best;
}
int main(){
  for(int n=4;n<=6;++n){
    vector<pair<int,int>> edges;for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)edges.push_back({i,j});
    int m=edges.size(),bound=1<<m;
    set<int> cs;
    for(int x=1;x<(1<<n);++x)for(int y=1;y<(1<<n);++y){
      if(x==y)continue;int p=0;
      for(int a=0;a<m;++a){auto [i,j]=edges[a];
        int v=((x>>i&1)&(y>>j&1))^((x>>j&1)&(y>>i&1));
        p|=v<<a;
      }
      assert(p!=0);cs.insert(p);
    }
    vector<int> polys;vector<char> good(bound,0);
    for(int s=0;s<bound;++s){
      int k=pc(s);if((1<<k)>(int)cs.size())continue;
      unordered_set<int> traces;traces.reserve(cs.size());
      for(int c:cs)traces.insert(c&s);
      if((int)traces.size()==(1<<k)){good[s]=1; if(k>=(int)polys.size())polys.resize(k+1,0); ++polys[k];}
    }
    vector<vector<int>> f(m+1);for(int s=0;s<bound;++s)if(good[s])f[pc(s)].push_back(s);
    map<int,int> facets_by_size;map<pair<int,int>,int> orbit;
    for(int s=0;s<bound;++s)if(good[s]){
      bool maxface=true;for(int b=0;b<m;++b)if(!(s&(1<<b))&&good[s|(1<<b)]){maxface=false;break;}
      if(maxface){++facets_by_size[pc(s)];++orbit[{pc(s),canonical(s,n,edges)}];}
    }
    vector<int> boundary(m+1,0);
    for(int k=2;k<=m;++k)if(!f[k].empty())boundary[k]=rank_mod2(f[k-1],f[k],m);
    vector<pair<int,int>> homology;
    for(int k=1;k<=m;++k)if(!f[k].empty()){
      int rk=(k==1?1:boundary[k]);int beta=(int)f[k].size()-rk-(k<m?boundary[k+1]:0);
      assert(beta>=0);
      if(beta)homology.push_back({k-1,beta});
    }
    cout<<"n "<<n<<" concepts "<<cs.size()<<" face_polynomial";
    for(int v:polys)cout<<" "<<v;
    cout<<"\nfacet_sizes";for(auto [k,v]:facets_by_size)cout<<" "<<k<<":"<<v;
    cout<<"\nfacet_orbits";for(auto [kv,v]:orbit)cout<<" "<<kv.first<<":"<<v<<":"<<kv.second;
    cout<<"\nboundary_ranks";for(int k=2;k<=m;++k)if(!f[k].empty())cout<<" "<<k<<":"<<boundary[k];
    cout<<"\nreduced_F2_homology";for(auto [k,v]:homology)cout<<" "<<k<<":"<<v;cout<<"\n";
  }
}
