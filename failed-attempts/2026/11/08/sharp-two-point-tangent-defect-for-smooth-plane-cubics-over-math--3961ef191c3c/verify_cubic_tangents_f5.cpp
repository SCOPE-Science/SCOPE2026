// Exhaustive exact enumeration of rational tangent unions of ternary cubics over GF(5).
// Compile: c++ -O3 -std=c++17 verify_cubic_tangents_f5.cpp -o verify && ./verify
// Every nonzero cubic is represented once modulo its nonzero scalar multiples.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
using Coeff = array<int,10>;
using Point = array<int,3>;
static const int EX[10][3]={{3,0,0},{2,1,0},{2,0,1},{1,2,0},{1,1,1},{1,0,2},{0,3,0},{0,2,1},{0,1,2},{0,0,3}};
int val[31][10], grad[31][10][3], transf[4][10][10], weights[10];
vector<Point> points;
int power(int a,int e){int r=1;while(e--)r=r*a%5;return r;}
int imod(int a){a%=5;return a<0?a+5:a;}
void setup(){
  for(int a=0;a<5;a++)for(int b=0;b<5;b++)points.push_back({a,b,1});
  for(int a=0;a<5;a++)points.push_back({a,1,0}); points.push_back({1,0,0}); assert(points.size()==31);
  for(int p=0;p<31;p++)for(int j=0;j<10;j++){
    int v=1;for(int t=0;t<3;t++)v=v*power(points[p][t],EX[j][t])%5;val[p][j]=v;
    for(int t=0;t<3;t++){
      int d=EX[j][t];if(d) {d=d*power(points[p][t],EX[j][t]-1)%5;
        for(int s=0;s<3;s++)if(s!=t)d=d*power(points[p][s],EX[j][s])%5;}
      grad[p][j][t]=d;
    }
  }
  weights[9]=1;for(int j=8;j>=0;j--)weights[j]=5*weights[j+1];
  // Four generators of PGL_3(F_5): two adjacent transpositions,
  // scaling the first coordinate by 2, and an elementary transvection.
  const int S[4][3][3]={
    {{0,1,0},{1,0,0},{0,0,1}},
    {{1,0,0},{0,0,1},{0,1,0}},
    {{2,0,0},{0,1,0},{0,0,1}},
    {{1,1,0},{0,1,0},{0,0,1}}
  };
  for(int k=0;k<4;k++)for(int j=0;j<10;j++){
    int terms[4][4][4]={};terms[0][0][0]=1;
    for(int t=0;t<3;t++)for(int rep=0;rep<EX[j][t];rep++){
      int next[4][4][4]={};
      for(int x=0;x<=3;x++)for(int y=0;y<=3-x;y++)for(int z=0;z<=3-x-y;z++)
        if(terms[x][y][z])for(int u=0;u<3;u++){
          int nx=x+(u==0),ny=y+(u==1),nz=z+(u==2);
          if(nx+ny+nz<=3)next[nx][ny][nz]=imod(next[nx][ny][nz]+terms[x][y][z]*S[k][t][u]);
        }
      for(int x=0;x<4;x++)for(int y=0;y<4;y++)for(int z=0;z<4;z++)terms[x][y][z]=next[x][y][z];
    }
    for(int h=0;h<10;h++)transf[k][j][h]=terms[EX[h][0]][EX[h][1]][EX[h][2]];
  }
}
int code(Coeff a){int f=0;while(f<10 && !imod(a[f]))f++;if(f==10)return -1;
  static const int inv[5]={0,1,3,2,4};int ret=0;
  for(int j=0;j<10;j++)ret+=weights[j]*imod(a[j]*inv[imod(a[f])]);return ret;
}
Coeff decode(int v){Coeff a{};for(int j=0;j<10;j++)a[j]=v/weights[j]%5;return a;}
int orbit_size(Coeff seed){unordered_set<int>seen;seen.reserve(100000);vector<int>front;front.reserve(100000);
  int c=code(seed);seen.insert(c);front.push_back(c);
  for(size_t p=0;p<front.size();p++){
    Coeff a=decode(front[p]);
    for(int k=0;k<4;k++){
      Coeff b{};for(int j=0;j<10;j++)for(int h=0;h<10;h++)b[h]+=a[j]*transf[k][j][h];
      int next=code(b);if(seen.insert(next).second)front.push_back(next);
    }
  }
  return (int)seen.size();
}
struct Data{int rational_count;int covered_count;bool rationally_nonsingular;};
Data evaluate(const Coeff&a){uint64_t union_mask=0;int n=0;
  for(int p=0;p<31;p++){
    int f=0;for(int j=0;j<10;j++)f+=a[j]*val[p][j];if(imod(f))continue;
    n++;int g[3]={};for(int j=0;j<10;j++)for(int t=0;t<3;t++)g[t]+=a[j]*grad[p][j][t];
    if(!imod(g[0])&&!imod(g[1])&&!imod(g[2]))return {n,0,false};
    for(int q=0;q<31;q++){
      const auto&Q=points[q];if(!imod(g[0]*Q[0]+g[1]*Q[1]+g[2]*Q[2]))union_mask|=uint64_t(1)<<q;
    }
  }
  return {n,__builtin_popcountll(union_mask),true};
}
int main(){setup();
  map<int,long long>coverage;map<pair<int,int>,long long>high;
  long long total=0,regular=0;int maxcover=0;map<int,long long>topN;
  for(int first=0;first<10;first++){
    int tail=9-first,number=1;for(int i=0;i<tail;i++)number*=5;
    for(int v=0;v<number;v++){
      Coeff a{};a[first]=1;int tmp=v;for(int j=9;j>first;j--){a[j]=tmp%5;tmp/=5;}
      total++;auto d=evaluate(a);if(!d.rationally_nonsingular)continue;regular++;
      coverage[d.covered_count]++;
      if(d.covered_count>maxcover){maxcover=d.covered_count;topN.clear();}
      if(d.covered_count==maxcover)topN[d.rational_count]++;
      if(d.covered_count>=27)high[{d.covered_count,d.rational_count}]++;
    }
  }
  assert(total==2441406LL && regular==1895000LL);
  assert(maxcover==29 && coverage[29]==186000LL);
  assert(topN.size()==2 && topN[8]==93000 && topN[10]==93000);
  Coeff c8={1,0,0,0,0,1,0,2,0,0};
  Coeff c10={1,0,0,0,0,1,1,0,4,0};
  auto a=evaluate(c8),b=evaluate(c10);
  assert(a.rationally_nonsingular && a.rational_count==8 && a.covered_count==29);
  assert(b.rationally_nonsingular && b.rational_count==10 && b.covered_count==29);
  int o8=orbit_size(c8),o10=orbit_size(c10);
  assert(o8==93000 && o10==93000);
  cout<<"CUBIC_F5_TANGENT_EXTREMAL_PASS "<<total<<' '<<regular<<' '<<maxcover<<' '<<coverage[maxcover]<<' '<<o8<<' '<<o10<<'\n';
  for(auto [c,n]:coverage)cout<<"cover="<<c<<" count="<<n<<'\n';
  for(auto [k,v]:high)cout<<"cover="<<k.first<<" rational_points="<<k.second<<" count="<<v<<'\n';
  return 0;
}
