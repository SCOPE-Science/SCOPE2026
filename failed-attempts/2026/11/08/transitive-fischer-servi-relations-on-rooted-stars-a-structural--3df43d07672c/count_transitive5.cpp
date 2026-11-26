#include <cstdio>
#include <cstdint>
int main(){int n=5,row[5];uint64_t t=0,u=0,v=0;for(uint64_t z=0;z<(1ULL<<25);z++){for(int i=0;i<n;i++)row[i]=(z>>(5*i))&31;bool good=true;for(int i=0;i<5&&good;i++)for(int j=0;j<5;j++)if((row[i]>>j)&1)if(row[j]&~row[i]){good=false;break;}if(!good)continue;t++;bool nr=true;int col=0;for(int i=0;i<5;i++){if(!row[i])nr=false;col|=row[i];}if(nr){u++;if(col==31)v++;}}
printf("T5=%llu U5=%llu V5=%llu\n",(unsigned long long)t,(unsigned long long)u,(unsigned long long)v);}
