// Independent direct synchronous-block simulation of original Critters on a
// fully periodic two-row torus. Compile: g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int block(int x) {
    int c=__builtin_popcount((unsigned)x);
    if(c==2) return (x==6||x==9)?(x^15):x;
    int y=x^15;
    if(c==3) y=((y&1)<<3)|((y&2)<<1)|((y&4)>>1)|((y&8)>>3);
    return y;
}
unsigned phase(unsigned s,int length,int offset){
    unsigned result=0;
    for(int c=offset;c<length;c+=2){
        int d=(c+1)%length,r=offset;
        int ids[4]={2*c+r,2*d+r,2*c+(r^1),2*d+(r^1)};
        int input=0;
        for(int q=0;q<4;q++)input|=((s>>ids[q])&1u)<<q;
        int output=block(input);
        for(int q=0;q<4;q++) result|=((unsigned)((output>>q)&1))<<ids[q];
    }
    return result;
}
unsigned double_step(unsigned s,int length){
    return phase(phase(s,length,0),length,1);
}
int main(){
    for(int L:{4,6,8,10}){
        unsigned count=0;
        map<int,unsigned> hist;
        for(unsigned s=0;s<(1u<<(2*L));s++){
            if(double_step(s,L)!=s)continue;
            count++;
            hist[__builtin_popcount(s)]++;
        }
        unsigned expected= (L==4?16:(L==6?44:(L==8?136:448)));
        assert(count==expected);
        cout<<"width="<<L<<" fixed="<<count<<" histogram=";
        for(auto p:hist)cout<<p.first<<":"<<p.second<<" ";
        cout<<"\n";
    }
}
