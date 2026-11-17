// Independent finite functional-graph and Burnside verification.
// Compile: c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent
// Run: ./verify_independent
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;
constexpr int X = 3, Y = 4, V = X*Y, BOARDS = 1<<V;
constexpr int STATES = BOARDS*4*V;
constexpr array<int,4> DX{{1,0,-1,0}}, DY{{0,1,0,-1}}; // east, south, west, north

int pack(int bits, int direction, int position) {
    return ((bits*4 + direction)*V + position);
}
void unpack(int z, int& bits, int& direction, int& position) {
    position=z%V; z/=V; direction=z%4; bits=z/4;
}
int iterate(int z) {
    int board,d,p; unpack(z,board,d,p);
    int old=(board>>p)&1;
    d=(d+(old?3:1))&3;
    board^=1<<p;
    int x=p%X,y=p/X;
    x=(x+DX[d]+X)%X; y=(y+DY[d]+Y)%Y;
    return pack(board,d,y*X+x);
}
struct Geo {
    array<int,V> p{};
    array<int,4> d{};
    bool swap_color=false;
};
Geo geometric(int ax,int ay,int bx,int by) {
    Geo g; g.swap_color=(ax*ay<0);
    for(int p=0;p<V;p++)g.p[p]=((ax*(p%X)+bx+X)%X)+X*((ay*(p/X)+by+Y)%Y);
    for(int d=0;d<4;d++){
        int xx=ax*DX[d], yy=ay*DY[d];
        for(int j=0;j<4;j++)if(DX[j]==xx && DY[j]==yy)g.d[d]=j;
    }
    return g;
}
int apply(int z,const Geo &g){
    int board,d,p;unpack(z,board,d,p);
    int b2=0;
    for(int q=0;q<V;q++)if(board&(1<<q))b2|=1<<g.p[q];
    if(g.swap_color)b2^=BOARDS-1;
    return pack(b2,g.d[d],g.p[p]);
}
int main() {
    vector<int> next(STATES), indegree(STATES,0);
    for(int z=0;z<STATES;z++){
        next[z]=iterate(z);
        indegree[next[z]]++;
    }
    for(int z=0;z<STATES;z++)if(indegree[z]!=1)throw runtime_error("non-bijection");
    vector<int> cycle(STATES,-1), reps, lengths;
    map<int,int> length_count;
    for(int z=0;z<STATES;z++)if(cycle[z]<0){
        int k=cycle[z]; (void)k;
        int c=(int)reps.size(), current=z, length=0;
        do {
            if(cycle[current]>=0)throw runtime_error("orbit collision");
            cycle[current]=c;
            length++;
            current=next[current];
        } while(current!=z);
        reps.push_back(z);lengths.push_back(length);length_count[length]++;
    }
    vector<Geo> group;
    for(int ax:{1,-1})for(int ay:{1,-1})
    for(int bx=0;bx<X;bx++)for(int by=0;by<Y;by++)
        group.push_back(geometric(ax,ay,bx,by));
    if(group.size()!=48)throw runtime_error("group size");
    // Burnside's lemma counts orbits of the symmetry action on temporal cycles.
    map<int,int> fixed_sum;
    for(const Geo &g:group){
        for(int c=0;c<(int)reps.size();c++){
            int d=cycle[apply(reps[c],g)];
            if(lengths[c]!=lengths[d])throw runtime_error("period noninvariance");
            if(c==d)fixed_sum[lengths[c]]++;
        }
    }
    int cycles=0,types=0,volume=0;
    cout<<"total_states "<<STATES<<"\n";
    cout<<"length,cycles,burnside_fixed_sum,types\n";
    for(auto [length,count]:length_count){
        if(fixed_sum[length]%48)throw runtime_error("noninteger Burnside count");
        int t=fixed_sum[length]/48;
        cout<<length<<","<<count<<","<<fixed_sum[length]<<","<<t<<"\n";
        cycles+=count;types+=t;volume+=length*count;
        if(length%8)throw runtime_error("period not divisible by eight");
    }
    cout<<"total_cycles "<<cycles<<"\n";
    cout<<"total_symmetry_types "<<types<<"\n";
    if(cycles!=2480||types!=74||volume!=STATES||length_count.rbegin()->first!=312)
        throw runtime_error("incorrect final totals");
    cout<<"all_checks_passed\n";
}
