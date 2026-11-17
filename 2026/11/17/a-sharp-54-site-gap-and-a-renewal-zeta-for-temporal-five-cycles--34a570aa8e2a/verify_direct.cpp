// Independent state-space verification of temporal period five in Rule 22.
#include <cstdint>
#include <iostream>
#include <cassert>
using u32=uint32_t;
static inline u32 step(u32 x,int n) {
    u32 m=(1u<<n)-1;
    u32 a=((x<<1)&m)|(x>>(n-1));
    u32 c=(x>>1)|((x&1u)<<(n-1));
    return (a^x^c)&~(a&x&c)&m;
}
int main(){
    uint64_t s[24]={0};
    for(int n=1;n<=22;n++) {
        if(n==11||n==12||n==13)s[n]+=n;
        if(n>13)s[n]+=s[n-11]+s[n-12]+s[n-13];
    }
    for(int n=3;n<=22;n++){
        u32 total=1u<<n;
        uint64_t f1=0,f5=0;
        for(u32 x=0;x<total;x++){
            u32 y=step(x,n);
            if(y==x)++f1;
            for(int k=1;k<5;k++)y=step(y,n);
            if(y==x)++f5;
        }
        assert(f1==uint64_t(1+2*(n%2==0)));
        assert(f5==f1+5*s[n]);
        std::cout<<n<<" "<<f1<<" "<<f5<<" "<<(f5-f1)/5<<"\n";
    }
    std::cout<<"direct checks=PASS\n";
}
