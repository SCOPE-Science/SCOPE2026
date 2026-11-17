// Finite direct-matrix check of commutator fibers in strictly upper triangular 4x4 algebras.
// Compile: c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
struct Field {
    int q;
    int plus(int x,int y) const {return q==3 ? (x+y)%3 : x^y;}
    int neg(int x) const {return q==3 ? (3-x)%3 : x;}
    int mul(int x,int y) const {
        if(q==4){int p=0; for(int j=0;j<2;++j){if((y>>j)&1) p^=x; if(x&2) x=((x<<1)^7)&3; else x=(x<<1)&3;}return p;}
        return x*y%q;
    }
};
using Mat=array<array<int,4>,4>;
Mat decode(int code,int q){
 Mat a{};
 const int r[6]={0,1,2,0,1,0},c[6]={1,2,3,2,3,3};
 for(int i=0;i<6;++i){a[r[i]][c[i]]=code%q;code/=q;}
 return a;
}
Mat multiply(const Mat&a,const Mat&b,const Field&f){
 Mat z{};
 for(int i=0;i<4;++i) for(int j=i+1;j<4;++j)
   for(int k=i+1;k<j;++k) z[i][j]=f.plus(z[i][j],f.mul(a[i][k],b[k][j]));
 return z;
}
int main(){
 for(int q : {2,3,4}) {
   Field f{q};int n=1;for(int i=0;i<6;++i)n*=q;
   vector<Mat> m(n);for(int i=0;i<n;++i)m[i]=decode(i,q);
   vector<uint64_t> cnt(q*q*q,0);
   const int coords[3][2]={{0,2},{1,3},{0,3}};
   for(int ai=0;ai<n;++ai) for(int bi=0;bi<n;++bi){
     const Mat xy=multiply(m[ai],m[bi],f),yx=multiply(m[bi],m[ai],f);
     int ix=0,scale=1;
     for(auto &rc: coords){
       int d=f.plus(xy[rc[0]][rc[1]], f.neg(yx[rc[0]][rc[1]]));
       ix+=scale*d;scale*=q;
     }
     ++cnt[ix];
   }
   const uint64_t q7= [&](){uint64_t v=1;for(int i=0;i<7;++i)v*=q;return v;}();
   const uint64_t q8=q7*q,q9=q8*q;
   const uint64_t generic=q9-q7,pure=2*generic,zero=pure+q8;
   uint64_t sum=0;
   for(int v=0;v<q*q*q;++v){
     int u=v%q,w=(v/q)%q,t=v/(q*q);
     uint64_t expect=(u||w)?generic:(t?pure:zero);
     if(cnt[v]!=expect){cerr<<"FAIL q="<<q<<" output="<<v<<" count="<<cnt[v]<<" expected="<<expect<<'\n';return 1;}
     sum+=cnt[v];
   }
   if(sum!=(uint64_t)n*n) throw runtime_error("pair sum mismatch");
   cout<<"q="<<q<<" pairs="<<sum<<" zero="<<zero<<" pure="<<pure<<" generic="<<generic<<" verified\n";
 }
 cout<<"VERIFY_OK\n";
}
