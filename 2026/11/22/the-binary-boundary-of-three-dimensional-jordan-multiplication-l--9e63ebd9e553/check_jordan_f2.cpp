// Exhaustive binary three-dimensional commutative Jordan algebra census.
// Compile: c++ -std=c++17 -O2 check_jordan_f2.cpp -o check_jordan_f2
// Run: ./check_jordan_f2 representatives.tsv
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Table = array<uint8_t,64>;
using Linear = array<uint8_t,8>;
constexpr int pairs[6][2]={{0,0},{0,1},{0,2},{1,1},{1,2},{2,2}};

Table multiplication(uint32_t code) {
  uint8_t b[3][3]{};
  for (int p=0;p<6;++p) {
    int i=pairs[p][0],j=pairs[p][1];
    b[i][j]=b[j][i]=(code>>(3*p))&7;
  }
  Table t{};
  for(int x=0;x<8;++x) for(int y=0;y<8;++y) {
    int z=0;
    for(int i=0;i<3;++i) for(int j=0;j<3;++j)
      if((x>>i&1)&&(y>>j&1))z^=b[i][j];
    t[8*x+y]=z;
  }
  return t;
}
uint8_t prod(const Table& t,int x,int y){return t[8*x+y];}

bool jordan_over_F2(const Table& t) {
  for(int x=0;x<8;++x) for(int y=0;y<8;++y){
    int xx=prod(t,x,x);
    if(prod(t,xx,prod(t,x,y))!=prod(t,x,prod(t,xx,y)))return false;
  }
  return true;
}
bool jordan_formal(const Table& t) {
  // Coefficients of x_i^2 x_j y_k in the Jordan polynomial.
  for(int i=0;i<3;++i) for(int j=0;j<3;++j) for(int k=0;k<3;++k){
    int a=1<<i,b=1<<j,y=1<<k,aa=prod(t,a,a);
    if(prod(t,aa,prod(t,b,y))!=prod(t,b,prod(t,aa,y))) return false;
  }
  return true;
}
bool associative(const Table& t){
  for(int x=0;x<8;++x)for(int y=0;y<8;++y)for(int z=0;z<8;++z)
    if(prod(t,prod(t,x,y),z)!=prod(t,x,prod(t,y,z)))return false;
  return true;
}

// Field F4=F2[w]/(w^2+w+1); each coordinate is encoded in two bits.
int gf4mul(int a,int b){
  int c=0;
  for(int i=0;i<2;++i)for(int j=0;j<2;++j)
    if((a>>i&1)&&(b>>j&1))c^=1<<(i+j);
  if(c&4)c^=7;
  return c;
}
int multiply_F4(uint32_t code,int x,int y){
  int out=0;
  for(int p=0;p<6;++p){
    int i=pairs[p][0],j=pairs[p][1],value=(code>>(3*p))&7;
    int c=gf4mul((x>>(2*i))&3,(y>>(2*j))&3);
    if(i!=j)c^=gf4mul((x>>(2*j))&3,(y>>(2*i))&3);
    for(int k=0;k<3;++k)if(value>>k&1)out^=c<<(2*k);
  }
  return out;
}
bool jordan_over_F4(uint32_t code) {
  for(int x=0;x<64;++x)for(int j=0;j<3;++j){
    int y=1<<(2*j),xx=multiply_F4(code,x,x);
    if(multiply_F4(code,xx,multiply_F4(code,x,y))!=
       multiply_F4(code,x,multiply_F4(code,xx,y)))return false;
  }
  return true;
}

vector<Linear> all_GL3_F2(){
  vector<Linear> group;
  for(int a=1;a<8;++a)for(int b=1;b<8;++b)for(int c=1;c<8;++c){
    Linear g{};
    for(int x=0;x<8;++x)g[x]=((x&1)?a:0)^((x&2)?b:0)^((x&4)?c:0);
    set<int> image(g.begin(),g.end());
    if(image.size()==8)group.push_back(g);
  }
  return group;
}
uint32_t change_basis(const Table& t,const Linear& g) {
  // New basis e_i'=g(e_i): coordinates of original product in this basis.
  Linear inverse{};
  for(int x=0;x<8;++x)inverse[g[x]]=x;
  uint32_t code=0;
  for(int p=0;p<6;++p){
    int a=g[1<<pairs[p][0]],b=g[1<<pairs[p][1]];
    code|=uint32_t(inverse[prod(t,a,b)])<<(3*p);
  }
  return code;
}

void demand(bool yes,const string& why){if(!yes)throw runtime_error(why);}
int main(int argc,char** argv){
  try{
    demand(argc==2,"Usage: check_jordan_f2 representatives.tsv");
    auto group=all_GL3_F2();demand(group.size()==168,"wrong group size");
    vector<uint8_t> weak(1<<18,0),strict(1<<18,0),assoc(1<<18,0),visited(1<<18,0);
    vector<uint32_t> good;
    uint64_t weak_count=0,strict_count=0,assoc_count=0;
    uint64_t burnside=0,burnside_strict=0,burnside_assoc=0;
    for(uint32_t code=0;code<(1u<<18);++code){
      Table t=multiplication(code);
      if(!jordan_over_F2(t))continue;
      weak[code]=1;
      good.push_back(code);++weak_count;
      strict[code]=jordan_formal(t);
      demand(strict[code]==jordan_over_F4(code),"formal/F4 disagreement at code "+to_string(code));
      strict_count+=strict[code];
      assoc[code]=associative(t);assoc_count+=assoc[code];
      for(const auto& g:group)if(change_basis(t,g)==code){
        ++burnside;burnside_strict+=strict[code];burnside_assoc+=assoc[code];
      }
    }
    ofstream file(argv[1]);demand(file.good(),"cannot create representative table");
    file<<"code\torbit_size\tautomorphism_order\tassociative\tstrict\tzero_square_vectors\tnonzero_idempotents\n";
    int classes=0,strict_classes=0,assoc_classes=0;
    map<int,int> orbit_distribution;
    uint64_t sum_orbit=0,sum_strict_orbit=0,sum_assoc_orbit=0;
    for(uint32_t code:good){
      if(visited[code])continue;
      Table t=multiplication(code);
      set<uint32_t> orbit;
      for(const auto& g:group)orbit.insert(change_basis(t,g));
      demand(!orbit.empty()&&168%orbit.size()==0,"invalid orbit size");
      demand(*orbit.begin()==code,"noncanonical representative");
      for(uint32_t v:orbit){
        demand(weak[v]&&strict[v]==strict[code]&&assoc[v]==assoc[code],"orbit escapes invariant stratum");
        demand(!visited[v],"orbit overlap");visited[v]=1;
      }
      ++classes;strict_classes+=strict[code];assoc_classes+=assoc[code];
      sum_orbit+=orbit.size();sum_strict_orbit+=strict[code]*orbit.size();
      sum_assoc_orbit+=assoc[code]*orbit.size();
      ++orbit_distribution[orbit.size()];
      int zero_sq=0,nonzero_id=0;
      for(int x=0;x<8;++x){zero_sq+=(prod(t,x,x)==0);nonzero_id+=(x!=0&&prod(t,x,x)==x);}
      file<<code<<'\t'<<orbit.size()<<'\t'<<168/orbit.size()<<'\t'<<int(assoc[code])
          <<'\t'<<int(strict[code])<<'\t'<<zero_sq<<'\t'<<nonzero_id<<'\n';
    }
    file.close();
    demand(weak_count==2858&&strict_count==1898&&assoc_count==988,"structure census mismatch");
    demand(classes==47&&strict_classes==32&&assoc_classes==16,"orbit census mismatch");
    demand(sum_orbit==weak_count&&sum_strict_orbit==strict_count&&sum_assoc_orbit==assoc_count,"incomplete orbits");
    demand(burnside==168*classes&&burnside_strict==168*strict_classes&&burnside_assoc==168*assoc_classes,"Burnside mismatch");
    cout<<"F2_3D_JORDAN_CENSUS_OK\n";
    cout<<"based_tables="<<weak_count<<" formal_tables="<<strict_count<<" associative_tables="<<assoc_count<<"\n";
    cout<<"based_classes="<<classes<<" formal_classes="<<strict_classes<<" associative_classes="<<assoc_classes<<"\n";
    cout<<"burnside_fixed_sums="<<burnside<<","<<burnside_strict<<","<<burnside_assoc<<"\n";
    for(auto [size,count]:orbit_distribution)cout<<"orbit_size="<<size<<" classes="<<count<<"\n";
    return 0;
  }catch(const exception& e){cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
}
