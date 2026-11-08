/* Complete finite-light-cone verification of the 3-state excitable rotor bound.
 * Public mathematical code; run gcc -O3 check_forced_wheel.c -o check && ./check
 */
#include <stdio.h>
#include <stdint.h>
int main(void){
  const uint32_t total=14348907U; /* 3^15 */
  unsigned char tab[3][3][3][3]={0};
  for(int h=0;h<3;h++)for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++)
    tab[h][a][b][c]=b==1?2:b==2?0:((h==1||a==1||c==1)?1:0);
  unsigned char A[15], B[15];
  uint64_t tested=0;
  for(int h0=0;h0<3;h0++){
    for(uint32_t code=0;code<total;code++){
      uint32_t v=code;
      for(int j=0;j<15;j++){A[j]=v%3;v/=3;}
      unsigned char *s=A,*d=B,at4=255;
      for(int t=0;t<7;t++){
        int h=(h0+t)%3, length=15-2*t;
        for(int j=0;j<length-2;j++)d[j]=tab[h][s[j]][s[j+1]][s[j+2]];
        unsigned char *tmp=s;s=d;d=tmp;
        if(t==3)at4=s[3];
      }
      if(s[0]!=at4){
        printf("FAIL h0=%d code=%u t4=%u t7=%u\n",h0,code,at4,s[0]);return 1;
      }
      ++tested;
    }
    printf("hub_initial=%d checked=%u\n",h0,total);
  }
  printf("PASS forced rotor F^7=F^4 at all rim sites for %llu local states\n",(unsigned long long)tested);
  return 0;
}
