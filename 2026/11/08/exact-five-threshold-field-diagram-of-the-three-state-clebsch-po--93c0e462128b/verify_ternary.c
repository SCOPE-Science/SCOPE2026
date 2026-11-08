/* Independent exhaustive verifier for three named spins on the 16-vertex
   folded-cube graph. Compile: cc -O3 -std=c99 verify_ternary.c -o verify_ternary
   Then execute: ./verify_ternary
   No external packages or data files are needed. */
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(void) {
    const int expected_min[17] = {8,7,6,5,3,3,3,3,4,8,12,15,20,25,30,35,40};
    const int expected_count[17] = {10,160,800,2240,160,320,80,160,160,1280,
                                    6400,512,1920,1280,320,32,1};
    int u[40],v[40],e=0,degree[16]={0};
    for(int i=0;i<16;i++) for(int j=i+1;j<16;j++) {
        unsigned diff = (unsigned)(i^j);
        int bits=0; for (;diff;diff>>=1) bits+=diff&1U;
        if(bits==1||bits==4) {
            if(e>=40) return 1;
            u[e]=i;v[e++]=j;degree[i]++;degree[j]++;
        }
    }
    if(e!=40) return 2;
    for(int i=0;i<16;i++) if(degree[i]!=5) return 3;
    int min[17],count[17];
    for(int k=0;k<=16;k++){min[k]=INT_MAX;count[k]=0;}
    int total=1; for(int i=0;i<16;i++) total*=3;
    if(total!=43046721) return 4;
    /* Unlike subset verification, enumerate independently by base-3
       digits, directly evaluating every edge for every state. */
    for(int code=0;code<total;code++) {
        int spins[16],z=code,favored=0;
        for(int i=0;i<16;i++) {spins[i]=z%3;z/=3;if(spins[i]==0)favored++;}
        int energy=0;
        for(int j=0;j<e;j++) energy+=(spins[u[j]]==spins[v[j]]);
        if(energy<min[favored]){min[favored]=energy;count[favored]=1;}
        else if(energy==min[favored])count[favored]++;
    }
    for(int k=0;k<=16;k++) {
        if(min[k]!=expected_min[k]||count[k]!=expected_count[k]) {
            fprintf(stderr,"Mismatch at sector %d: %d %d\n",k,min[k],count[k]);
            return 5;
        }
    }
    puts("VERIFIED: independent ternary enumeration of all 43,046,721 configurations and all 17 sector minima/counts.");
    return 0;
}
