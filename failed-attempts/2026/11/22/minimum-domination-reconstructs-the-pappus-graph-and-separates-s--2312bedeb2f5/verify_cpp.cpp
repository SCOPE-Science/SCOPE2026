// Independent exhaustive C++17 checker for the Pappus optimum-domination membership design.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
int main(){
    constexpr int n=18;
    array<int,n> closed{};for(int i=0;i<n;++i)closed[i]=1<<i;
    auto incidence=[](int p,int l){int x=p%3,y=p/3,d=(l-9)/3,c=(l-9)%3;return (d==0?x:d==1?y:(y-x+3)%3)==c;};
    int edges=0;
    for(int p=0;p<9;++p)for(int l=9;l<18;++l)if(incidence(p,l)){
        closed[p]|=1<<l;closed[l]|=1<<p;++edges;
    }
    assert(edges==27);
    vector<int> minima;
    int gamma=99; // exhaustive over all 2^18 vertex subsets, independent of the predicted classification
    for(int M=1;M<(1<<n);++M){
        int k=__builtin_popcount((unsigned)M);if(k>gamma)continue;
        int cover=0;for(int v=0;v<n;++v)if(M>>v&1)cover|=closed[v];
        if(cover==(1<<n)-1){
            if(k<gamma){gamma=k;minima.clear();}
            minima.push_back(M);
        }
    }
    assert(gamma==5&&minima.size()==18);
    int f[4]={1,0,0,0};int pc[3]={0,0,0};
    for(int i=0;i<n;++i){int v0=0,v1=0;for(int M:minima){if(M>>i&1)++v1;else ++v0;}assert(v1==5&&v0==13);++f[1];}
    for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){
        int t=0,co=0;for(int M:minima){t|=1<<(((M>>i&1)<<1)|(M>>j&1));co+=((M>>i&1)&&(M>>j&1));}
        bool edge=bool(closed[i]>>j&1);
        if(edge)assert(co==0),++pc[0];
        else if((i<9)==(j<9))assert(co==1),++pc[1];
        else assert(co==2),++pc[2];
        if(t==15)++f[2];
    }
    for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)for(int k=j+1;k<n;++k){
        int t=0;for(int M:minima)t|=1<<(((M>>i&1)<<2)|((M>>j&1)<<1)|(M>>k&1));
        if(t==255)++f[3];
    }
    assert(pc[0]==27&&pc[1]==72&&pc[2]==54);
    assert(f[0]==1&&f[1]==18&&f[2]==126&&f[3]==0);
    cout<<"PASS exhaustive 262143 vertex subsets, gamma=5, 18 optimizers, 27 edges\n";
    cout<<"PASS pair counts (edge same-side cross-nonedge)="<<pc[0]<<" "<<pc[1]<<" "<<pc[2]<<"\n";
    cout<<"PASS trace f-vector="<<f[0]<<" "<<f[1]<<" "<<f[2]<<" "<<f[3]<<"\n";
}
