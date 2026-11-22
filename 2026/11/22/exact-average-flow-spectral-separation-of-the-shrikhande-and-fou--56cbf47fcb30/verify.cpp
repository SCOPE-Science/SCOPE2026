// Independent direct depth-first enumeration of every simple rooted path.
// C++17, e.g. c++ -O2 -std=c++17 verify.cpp -o verify && ./verify
#include <array>
#include <cstdint>
#include <iostream>
#include <cassert>
using namespace std;
using Hist=array<uint64_t,16>;
static uint16_t adj[16];
static Hist counts;
void dfs(int v,uint16_t visited,int depth){
    if(depth>0)++counts[depth];
    uint16_t a=adj[v]&static_cast<uint16_t>(~visited);
    while(a){uint16_t bit=a&static_cast<uint16_t>(-a); a^=bit;
       int u=__builtin_ctz(static_cast<unsigned>(bit));
       dfs(u,static_cast<uint16_t>(visited|bit),depth+1);
    }
}
void graph(bool rook){
    for(int i=0;i<16;++i){
        adj[i]=0;
        for(int j=0;j<16;++j)if(i!=j){
            int x=i/4,y=i%4, xx=j/4, yy=j%4;
            bool edge=rook ? (x==xx||y==yy) :
              (((xx+4-x)%4==1&&(yy+4-y)%4==0)||
               ((xx+4-x)%4==3&&(yy+4-y)%4==0)||
               ((xx+4-x)%4==0&&(yy+4-y)%4==1)||
               ((xx+4-x)%4==0&&(yy+4-y)%4==3)||
               ((xx+4-x)%4==1&&(yy+4-y)%4==1)||
               ((xx+4-x)%4==3&&(yy+4-y)%4==3));
            if(edge)adj[i] |= uint16_t(1u<<j);
        }
    }
}
int main(){
    uint64_t expected_P[2]={13991682,14029326};
    uint64_t expected_W[2]={177310488,177724236};
    uint64_t expected_7[2]={34452,34320};
    for(int g=0;g<2;++g){
        graph(g==0); counts.fill(0);
        dfs(0,1,0);
        uint64_t P=0,W=0;
        for(int k=1;k<16;++k){P+=counts[k]; W+=uint64_t(k)*counts[k];}
        assert(counts[7]==expected_7[g]);
        assert(P==expected_P[g]&&W==expected_W[g]);
        cout<<(g==0?"rook":"shrikhande")<<" path_total="<<P<<" weighted="<<W<<"\n";
    }
    cout<<"DIRECT_SELF_AVOIDING_DFS_EXACT_COUNTS_PASS\n";
}
