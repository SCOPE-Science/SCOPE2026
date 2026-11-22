/* Independent direct finite-input enumeration for radius-two binary lazy maps.
   Build: cc -std=c99 -O2 verify_direct.c -o verify_direct
   Run: ./verify_direct word_counts.csv
   Uses no de Bruijn or subset automata; compares every n<=10 row. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char **argv){
 if(argc!=2){fprintf(stderr,"usage: verify_direct word_counts.csv\n");return 2;}
 FILE *fp=fopen(argv[1],"r");if(!fp){perror(argv[1]);return 2;}
 char line[4096]; if(!fgets(line,sizeof(line),fp))return 2;
 for(int p=0;p<16;p++){
  if(!fgets(line,sizeof(line),fp)){fprintf(stderr,"missing row %d\n",p);return 2;}
  int expected[11];char *tok=strtok(line,",\r\n");
  if(!tok||atoi(tok)!=p){fprintf(stderr,"wrong pattern row %d\n",p);return 2;}
  for(int n=0;n<=10;n++){tok=strtok(NULL,",\r\n");if(!tok)return 2;expected[n]=atoi(tok);}
  for(int n=0;n<=10;n++){
   unsigned char seen[1024]={0}; int number=0;
   unsigned num_input=1U<<(n+4);
   for(unsigned seed=0;seed<num_input;seed++){
    unsigned out=0;
    for(int j=0;j<n;j++){
     unsigned w=(seed>>j)&31U;
     unsigned c=(w>>2)&1U;
     unsigned code=(w&3U)|(((w>>3)&3U)<<2);
     unsigned y=c||(!c&&code==(unsigned)p);
     out|=y<<j;
    }
    if(!seen[out]){seen[out]=1;number++;}
   }
   if(number!=expected[n]){fprintf(stderr,"MISMATCH p=%d n=%d counted=%d catalog=%d\n",p,n,number,expected[n]);return 1;}
  }
 }
 if(fgets(line,sizeof(line),fp)){fprintf(stderr,"unexpected extra rows\n");return 2;}
 fclose(fp);
 puts("PASS: 176 independent exhaustive direct image-word counts, 16 pattern rules, lengths 0..10.");return 0;
}
