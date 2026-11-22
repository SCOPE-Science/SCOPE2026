// An independent, standalone finite enumeration for a ternary length-3
// undirected de Bruijn identifying-code problem. Requires C++17.
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using std::uint64_t;

int main() {
    constexpr int q=3, n=q*q*q;
    auto index=[](int a,int b,int c){return (a*3+b)*3+c;};
    std::array<uint64_t,n> closed{};
    for(int a=0;a<q;++a) for(int b=0;b<q;++b) for(int c=0;c<q;++c){
        int i=index(a,b,c);
        closed[i] |= uint64_t(1)<<i;
        for(int x=0;x<q;++x){
            closed[i] |= uint64_t(1)<<index(x,a,b);
            closed[i] |= uint64_t(1)<<index(b,c,x);
        }
    }
    auto works=[&](uint64_t candidate){
        std::array<uint64_t,n> sig{};
        for(int i=0;i<n;++i){
            uint64_t s=candidate & closed[i];
            if(s==0)return false;
            for(int j=0;j<i;++j)if(sig[j]==s)return false;
            sig[i]=s;
        }
        return true;
    };
    auto by_size=[&](int size){
        uint64_t total=0,mask=(uint64_t(1)<<size)-1,limit=uint64_t(1)<<n;
        while(mask<limit){
            if(works(mask))++total;
            uint64_t low=mask & (~mask+1),next=mask+low;
            if(next<=mask)break;
            mask=(((next^mask)>>2)/low)|next;
        }
        return total;
    };
    if(by_size(8)!=0 || by_size(9)!=4366) return 1;
    std::vector<uint64_t> reverse_orbits;
    std::array<bool,n> used{};
    for(int i=0;i<n;++i){
        if(used[i])continue;
        int a=i/9,b=(i/3)%3,c=i%3;
        int j=index(c,b,a);
        reverse_orbits.push_back((uint64_t(1)<<i)|(uint64_t(1)<<j));
        used[i]=used[j]=true;
    }
    if(reverse_orbits.size()!=18)return 2;
    uint64_t size11=0,below=0;
    for(int selector=0;selector<(1<<18);++selector){
        uint64_t mask=0;
        for(int j=0;j<18;++j)if(selector&(1<<j))mask|=reverse_orbits[j];
        int size=__builtin_popcountll(mask);
        if(size<=11 && works(mask)){
            if(size<11)++below;
            else ++size11;
        }
    }
    if(below!=0||size11!=117)return 3;
    if(!works(0x222c017ull)||!works(0x128ada1ull))return 4;
    std::cout << "ordinary(8)=0 ordinary(9)=4366 symmetric(<11)=0 symmetric(11)=117 ALTERNATE_OK\n";
}
