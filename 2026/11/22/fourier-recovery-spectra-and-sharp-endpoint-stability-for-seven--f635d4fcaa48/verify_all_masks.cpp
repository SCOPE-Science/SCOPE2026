#include <cstdint>
#include <iostream>
#include <array>
using namespace std;
int main(){
 uint8_t pairdir[49][49] = {};
 for(int a=0;a<49;a++)for(int b=a+1;b<49;b++){
  int x=(b/7-a/7+7)%7, y=(b%7-a%7+7)%7; int d;
  if(x==0)d=7;else {int inv=1;while((inv*x)%7!=1)inv++;d=(y*inv)%7;}
  pairdir[a][b]=(uint8_t)(1u<<d);
 }
 uint64_t count[9] = {};
 for(int a=0;a<43;a++)for(int b=a+1;b<44;b++){
  uint8_t p2=pairdir[a][b];
  for(int c=b+1;c<45;c++){
   uint8_t p3=p2|pairdir[a][c]|pairdir[b][c];
   for(int d=c+1;d<46;d++){
    uint8_t p4=p3|pairdir[a][d]|pairdir[b][d]|pairdir[c][d];
    for(int e=d+1;e<47;e++){
     uint8_t p5=p4|pairdir[a][e]|pairdir[b][e]|pairdir[c][e]|pairdir[d][e];
     for(int f=e+1;f<48;f++){
      uint8_t p6=p5|pairdir[a][f]|pairdir[b][f]|pairdir[c][f]|pairdir[d][f]|pairdir[e][f];
      for(int g=f+1;g<49;g++){
       uint8_t p7=p6|pairdir[a][g]|pairdir[b][g]|pairdir[c][g]|pairdir[d][g]|pairdir[e][g]|pairdir[f][g];
       count[8-__builtin_popcount((unsigned)p7)]++;
      }
     }
    }
   }
  }
 }
 uint64_t tot=0;for(int k=0;k<=8;k++){if(count[k])cout<<k<<":"<<count[k]<<"\n";tot+=count[k];}cout<<"total:" <<tot<<"\n";
}
