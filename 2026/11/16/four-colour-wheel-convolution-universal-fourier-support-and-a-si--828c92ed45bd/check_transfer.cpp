// Independent exact Gaussian-integer 3-state transfer check for wheel colourings.
#include <array>
#include <complex>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
using Z = std::complex<std::int64_t>;
Z character(int group, int k, int y) {
 if(group==1) return Z((__builtin_popcount((unsigned)(k&y))%2)?-1:1,0);
 switch((k*y)&3){case 0:return {1,0};case 1:return {0,1};case 2:return {-1,0};default:return {0,-1};}
}
Z coefficient(int m, std::uint32_t frequency, int group) {
 Z old[3][3]{};
 for(int u=0;u<3;u++)old[u][u]={1,0};
 for(int j=0;j<m;j++){
  int k=(frequency>>(2*j))&3;Z next[3][3]{};
  for(int a=0;a<3;a++)for(int b=0;b<3;b++)if(a!=b)
   for(int start=0;start<3;start++)next[start][b]+=old[start][a]*character(group,k,a+1);
  for(int a=0;a<3;a++)for(int b=0;b<3;b++)old[a][b]=next[a][b];
 }
 return old[0][0]+old[1][1]+old[2][2];
}
int main(){
 for(int m=3;m<=9;m++){
  std::map<std::int64_t,std::int64_t> hist[2];
  std::uint32_t total=1u<<(2*m);
  for(std::uint32_t k=0;k<total;k++)for(int group=0;group<2;group++){
   Z z=coefficient(m,k,group);
   if(z.imag()!=0 || (z.real()%4!=2 && z.real()%4!=-2))throw std::runtime_error("bad character residue");
   hist[group][std::norm(z)]++;
  }
  if(m<=5 && hist[0]!=hist[1])throw std::runtime_error("unexpected early divergence");
  if(m==6 && (hist[0].at(4)!=1664 || hist[1].at(4)!=1632))throw std::runtime_error("wrong first divergence");
  std::cout<<"m="<<m<<" support="<<total<<" min_positive_squared="<<hist[0].begin()->first<<" equal="<<(hist[0]==hist[1])<<"\n";
 }
 std::cout<<"independent transfer checks PASS\n";
}
