// Exact 24-vertex cyclic-butterfly identifying-code census.
// Compile: g++ -std=c++17 -O2 verify.cpp -o verify_cpp
// Run from the directory containing OPTIMA.txt: ./verify_cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
using Mask=uint32_t;
constexpr int m=3, q=8, n=24;
static array<Mask,n> nb{};
static int idx(int level,int address){return level*q+address;}
static Mask bit(int i){return Mask(1)<<i;}
static bool good(Mask code){
    array<Mask,n> signatures{};
    for(int i=0;i<n;i++){
        Mask signature=nb[i]&code;
        if(signature==0) return false;
        for(int j=0;j<i;j++) if(signature==signatures[j])return false;
        signatures[i]=signature;
    }
    return true;
}
static Mask next_combination(Mask x){
    Mask u=x&-x,v=x+u;
    return v+(((v^x)/u)>>2);
}
static int rotate(int a,int k){
    int ans=0;
    for(int j=0;j<m;j++)if(a&(1<<j))ans|=1<<((j+k)%m);
    return ans;
}
static int reflect(int a){
    int ans=0;
    for(int j=0;j<m;j++)if(a&(1<<j))ans|=1<<(m-1-j);
    return ans;
}
static int map_vertex(int v,int k,int mask,bool flip){
    int i=v/q,a=v%q;
    return idx(((flip ? (m-i)%m:i)+k)%m,rotate(flip ? reflect(a):a,k)^mask);
}
int main(){
    for(int i=0;i<n;i++)nb[i]|=bit(i);
    for(int level=0;level<m;level++)for(int a=0;a<q;a++){
        int u=idx(level,a);
        for(int b:{a,a^(1<<level)}){
            int v=idx((level+1)%m,b);
            nb[u]|=bit(v);nb[v]|=bit(u);
        }
    }
    for(int i=0;i<n;i++)if(__builtin_popcount(nb[i])!=5)return 1;
    // Verify that all 48 prescribed natural symmetries preserve graph edges.
    for(int k=0;k<m;k++)for(int a=0;a<q;a++)for(int f=0;f<2;f++){
        for(int v=0;v<n;v++)for(int u=0;u<n;u++){
            bool before=(nb[v] & bit(u))!=0;
            int vv=map_vertex(v,k,a,f),uu=map_vertex(u,k,a,f);
            if(before!=bool(nb[vv]&bit(uu)))return 2;
        }
    }
    set<Mask> winners;
    const Mask limit=Mask(1)<<n;
    for(int size=8;size<=9;size++){
        uint64_t count=0;
        for(Mask c=(Mask(1)<<size)-1;c<limit;){
            if(good(c)){
                count++;
                if(size==9)winners.insert(c);
            }
            Mask nxt=next_combination(c);
            if(nxt<=c)break;
            c=nxt;
        }
        if(count!=uint64_t(size==8?0:48))return 3;
    }
    Mask representative=0x901669u;
    if(!good(representative) || winners.count(representative)==0)return 4;
    set<Mask> orbit;
    for(int k=0;k<m;k++)for(int a=0;a<q;a++)for(int f=0;f<2;f++){
        Mask d=0;
        for(int v=0;v<n;v++)if(representative&bit(v))d|=bit(map_vertex(v,k,a,f));
        orbit.insert(d);
    }
    if(orbit.size()!=48 || orbit!=winners)return 5;
    // An independently stored list allows byte-independent reproduction of all optima.
    ifstream in("OPTIMA.txt");
    if(!in)return 6;
    string line;set<Mask> declared;
    while(getline(in,line)){
        if(line.empty() || line[0]=='#')continue;
        Mask msk=0;
        try{msk=stoul(line,nullptr,16);}catch(...){return 7;}
        declared.insert(msk);
    }
    if(declared!=winners || declared.size()!=48)return 8;
    cout<<"VERIFY_OK minimum=9 optima=48 natural_orbits=1 profiles=(2,3,4)"<<endl;
    return 0;
}
