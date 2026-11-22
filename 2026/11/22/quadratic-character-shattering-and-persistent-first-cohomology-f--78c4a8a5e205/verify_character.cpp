// Verify finite-prime determinant-character faces and binary boundary ranks.
// Build: c++ -O2 -std=c++17 verify_character.cpp -o verify_character
// Run: ./verify_character
#include <algorithm>
#include <cassert>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <array>
#include <cstdint>
using namespace std;

int mod(int a,int p){a%=p;return a<0?a+p:a;}
int detpoint(int x,int y,int p){
    // Finite x represents (x,1); infinity p represents (1,0).
    int xa=(x==p?1:x), xb=(x==p?0:1);
    int ya=(y==p?1:y), yb=(y==p?0:1);
    return mod(xa*yb-xb*ya,p);
}
int sign(int x,int p){
    if(!x)return 0;
    for(int y=1;y<p;++y)if(y*y%p==x)return 1;
    return -1;
}
int edge_parity(int x,int y,int u,int v,int p){
    return sign(mod(detpoint(x,u,p)*detpoint(y,v,p),p),p)==1?0:1;
}
void run(int p){
    int n=p+1,V=n*n;
    auto vertex=[n](int x,int y){return n*x+y;};
    vector<array<int,2>> edges;
    vector<int> edgeid(V*V,-1);
    for(int x=0;x<n;++x)for(int y=0;y<n;++y)
      for(int u=x+1;u<n;++u)for(int v=0;v<n;++v)if(v!=y){
        int a=vertex(x,y),b=vertex(u,v);
        edgeid[a*V+b]=(int)edges.size();edges.push_back({a,b});
      }
    int E=(int)edges.size();
    vector<vector<uint64_t>> basis(E);
    int rank=0,good=0,bad=0;
    const int words=(E+63)/64;
    for(int x=0;x<n;++x)for(int u=x+1;u<n;++u)
      for(int w=u+1;w<n;++w)
       for(int y=0;y<n;++y)
        for(int v=0;v<n;++v)if(v!=y)
         for(int z=0;z<n;++z)if(z!=y&&z!=v){
          int parity=edge_parity(x,y,u,v,p)^edge_parity(x,y,w,z,p)^edge_parity(u,v,w,z,p);
          if(parity){++bad;continue;}
          ++good;
          int a=vertex(x,y),b=vertex(u,v),c=vertex(w,z);
          vector<uint64_t> col(words,0);
          for(int e:{edgeid[a*V+b],edgeid[a*V+c],edgeid[b*V+c]}){
            assert(e>=0);col[e/64]^=uint64_t(1)<<(e%64);
          }
          for(int pos=words-1;pos>=0;--pos){
            while(col[pos]){
              int k=pos*64+63-__builtin_clzll(col[pos]);
              if(basis[k].empty()){
                basis[k]=std::move(col);++rank;goto reduced;
              }
              for(int j=0;j<=pos;++j)col[j]^=basis[k][j];
            }
          }
          reduced:;
         }
    long long choose3=1LL*n*(n-1)*(n-2)/6;
    assert(good+bad==6*choose3*choose3);
    assert(good==bad);
    int beta1=E-V+1-rank,beta2=good-rank;
    // Explicit nontrivial 1-cocycle witness: x=inf,0,1; y=inf,0,a,
    // with a a nonsquare. Its boundary has edge-parity sum one.
    int nonsquare=-1;
    for(int a=2;a<p;++a)if(sign(a,p)==-1){nonsquare=a;break;}
    assert(nonsquare>=0);
    int w=edge_parity(p,p,0,0,p)^edge_parity(p,p,1,nonsquare,p)^edge_parity(0,0,1,nonsquare,p);
    assert(w==1);
    cout<<"p="<<p<<" vertices="<<V<<" edges="<<E<<" good_triangles="<<good
        <<" excluded_triangles="<<bad<<" boundary2_rank="<<rank
        <<" beta1="<<beta1<<" beta2="<<beta2<<" witness="<<nonsquare<<"\n";
    if(p==5)assert(rank==414&&beta1==1&&beta2==786);
    if(p==7)assert(rank==1504&&beta1==1&&beta2==7904);
}
int main(){run(5);run(7);}
