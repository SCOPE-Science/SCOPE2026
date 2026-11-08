#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;
int main(){
 uint8_t rows[81][4];
 for(int i=0;i<81;i++){int t=i;for(int c=0;c<4;c++){rows[i][c]=t%3;t/=3;}}
 vector<uint8_t> good(81*81*81,0);
 auto idx=[](int a,int b,int c){return (a*81+b)*81+c;};
 for(int a=0;a<81;a++)for(int b=0;b<81;b++)for(int c=0;c<81;c++){
  int valid=1;
  for(int j=0;j<4;j++){
   int predator=(rows[b][j]+1)%3,count=0;
   for(int di=-1;di<=1;di++)for(int dj=-1;dj<=1;dj++)if(di||dj){
    int rr=di<0?a:(di==0?b:c);
    count+=rows[rr][(j+dj+4)%4]==predator;
   }
   if(count>=4)valid=0;
  }
  good[idx(a,b,c)]=valid;
 }
 uint64_t total=0;
 for(int a=0;a<81;a++)for(int b=0;b<81;b++)for(int c=0;c<81;c++){
  if(!good[idx(a,b,c)])continue;
  for(int d=0;d<81;d++)total+=good[idx(b,c,d)]&&good[idx(c,d,a)]&&good[idx(d,a,b)];
 }
 printf("CHECK_FIXED_OK fixed=%llu\n",(unsigned long long)total);
 return total==99819?0:1;
}
