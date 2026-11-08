#include <cstdint>
#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <numeric>
#include <cassert>
#include <algorithm>
#include <string>
using namespace std;
static const int n=5;
static const uint32_t lim=1u<<(n*n);
array<array<uint8_t,32>,2> tbl;
array<array<uint8_t,n>,2> perm={{{1,0,2,3,4},{1,2,3,4,0}}};
uint32_t tr(uint32_t x,int g){uint32_t y=0;for(int i=0;i<n;i++){uint32_t row=(x>>(n*i))&31u; y|=(uint32_t)tbl[g][row]<<(n*perm[g][i]);}return y;}
bool invertible(uint32_t x){uint32_t rows[5];for(int i=0;i<5;i++)rows[i]=(x>>(5*i))&31u;int r=0;for(int col=0;col<5;col++){int p=r;while(p<5 && ((rows[p]>>col)&1u)==0)p++;if(p==5)continue;uint32_t tmp=rows[r];rows[r]=rows[p];rows[p]=tmp;for(int i=r+1;i<5;i++)if((rows[i]>>col)&1u)rows[i]^=rows[r];r++;}return r==5;}
int main(){
 for(int g=0;g<2;g++)for(int x=0;x<32;x++){int y=0;for(int i=0;i<5;i++)if((x>>i)&1)y|=1<<perm[g][i];tbl[g][x]=y;}
 vector<uint8_t> seen(lim,0); vector<uint32_t> stk;stk.reserve(120);
 vector<array<int,5>> allP; array<int,5> pr{0,1,2,3,4};do{allP.push_back(pr);}while(next_permutation(pr.begin(),pr.end()));
 map<string,uint64_t> by_type; map<int,uint64_t> by_order;uint64_t total=0,orbits=0,invs=0;int best=0;
 for(uint32_t x=0;x<lim;x++){
  if(seen[x])continue; if(!invertible(x)){seen[x]=1;continue;}
  stk.clear();stk.push_back(x);seen[x]=1;
  for(size_t z=0;z<stk.size();z++)for(int g=0;g<2;g++){
     uint32_t y=tr(stk[z],g);if(!seen[y]){seen[y]=1;stk.push_back(y);}
  }
  int o=stk.size();if(120%o){cerr<<"bad orbit size "<<o<<"\n";return 2;}
  by_order[120/o]++;
  int ord2=0,ord3=0,ord4=0,ord5=0,ord6=0,fix=0;
  for(const auto &prm:allP){uint32_t img=0; for(int i=0;i<5;i++){uint32_t row=(x>>(5*i))&31u,shifted=0;for(int j=0;j<5;j++)if((row>>j)&1u)shifted|=(1u<<prm[j]);img|=shifted<<(5*prm[i]);}if(img!=x)continue;fix++;int ord=1;bool marked[5]={};for(int i=0;i<5;i++)if(!marked[i]){int v=i,len=0;do{marked[v]=true;v=prm[v];len++;}while(v!=i);ord=std::lcm(ord,len);}ord2+=(ord==2);ord3+=(ord==3);ord4+=(ord==4);ord5+=(ord==5);ord6+=(ord==6);}
  if(fix!=120/o){cerr<<"inconsistent stabilizer";return 3;}
  string ty;switch(fix){case 1:ty="1";break;case 2:ty="C2";break;case 3:ty="C3";break;case 4:ty=ord4?"C4":"V4";break;case 5:ty="C5";break;case 6:ty=ord6?"C6":"S3";break;case 8:ty="D8";break;case 10:ty="D10";break;case 12:ty=ord6?"S3xC2":"A4";break;case 24:ty="S4";break;case 120:ty="S5";break;default:ty="UNKNOWN";}
  by_type[ty]++;
  total+=o;orbits++;best=max(best,o);
 }
 cout<<"GL5 invertible="<<total<<" orbits="<<orbits<<" maxorbit="<<best<<"\n";
 for(auto [a,b]:by_order)cout<<"autorder="<<a<<" classes="<<b<<" labeled="<<b*(120/a)<<"\n";
 for(auto [name,val]:by_type)cout<<"TYPE "<<name<<" "<<val<<"\n";cout<<"VERIFY_OK\n";
}
