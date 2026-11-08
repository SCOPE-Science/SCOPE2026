#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
static uint32_t nei[32];static int deg[32],n=0;
int make_tree(int remaining,int parent){int v=n++; if(parent>=0){nei[v]|=(1u<<parent);nei[parent]|=(1u<<v);deg[v]++;deg[parent]++;}int children=(parent<0)?3:2; if(remaining>0) for(int j=0;j<children;j++)make_tree(remaining-1,v);return v;}
uint32_t step(uint32_t s){uint32_t t=0;for(int v=0;v<n;v++){int hits=__builtin_popcount(s&nei[v]);if(hits*2>deg[v]) t|=1u<<v;}return t;}
int main(){for(int h=1;h<=3;h++){for(int k=0;k<32;k++)nei[k]=0,deg[k]=0;n=0;make_tree(h,-1);uint64_t sum=0;uint64_t max=1ULL<<n;for(uint64_t x=0;x<max;x++){uint32_t a=step(x);uint32_t b=step(a);uint32_t c=step(b);if(a==c)sum++;}printf("h=%d n=%d first_entry_by1=%llu total=%llu\n",h,n,(unsigned long long)sum,(unsigned long long)max);}}
