#include <cstdio>
#include <cstdint>
#include <cstring>
#include <vector>
#include <map>
#include <utility>
#include <stdexcept>
using namespace std;
// Independent graph input as explicit neighbor lists instead of topological mask generator.
static constexpr uint8_t neighbors[12][5] = {
 {1,2,3,4,5}, {0,2,5,6,10}, {0,1,3,6,7},
 {0,2,4,7,8}, {0,3,5,8,9}, {0,1,4,9,10},
 {1,2,7,10,11}, {2,3,6,8,11}, {3,4,7,9,11},
 {4,5,8,10,11}, {1,5,6,9,11}, {6,7,8,9,10}
};
uint32_t update(uint32_t k){
 uint8_t a[12],b[12];
 for(int v=0;v<12;v++){a[v]=k&3;k>>=2;}
 for(int v=0;v<12;v++){
  if(a[v]) b[v]=(a[v]+1)&3;
  else {
    b[v]=0;
    for(int j=0;j<5;j++)if(a[neighbors[v][j]]==1){b[v]=1;break;}
  }
 }
 uint32_t y=0;
 for(int v=11;v>=0;v--)y=(y<<2)|b[v];
 return y;
}
int main(){
 const uint32_t TOTAL=1u<<24;
 map<pair<int,int>,uint64_t> count;
 FILE* ext=fopen("extremal_codes.txt","w");
 if(!ext) return 2;
 for(uint32_t x=0;x<TOTAL;x++){
  uint32_t path[15];path[0]=x;
  for(int j=1;j<=14;j++)path[j]=update(path[j-1]);
  if(path[10]!=path[14])throw runtime_error("F14 != F10");
  int tau=0;
  for(;tau<=10;tau++)if(path[tau]==path[tau+4])break;
  if(tau>10)throw runtime_error("no entry");
  int p=(path[tau]==path[tau+1])?1:4;
  count[{tau,p}]++;
  if(tau==10)fprintf(ext,"%u\n",x);
 }
 fclose(ext);
 printf("TOTAL=%u\n",TOTAL);
 for(auto &c:count)printf("%d,%d,%llu\n",c.first.first,c.first.second,(unsigned long long)c.second);
}
