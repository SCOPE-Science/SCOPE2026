// Independent exhaustive check at ground order nine (C++17).
#include <array>
#include <iostream>
#include <vector>
using namespace std;
int main() {
    vector<array<int,3>> vertices;
    for (int a=0;a<9;++a) for(int b=a+1;b<9;++b)
        for(int c=b+1;c<9;++c) vertices.push_back({a,b,c});
    const int N=vertices.size(); // 84
    bool open[84][84]={}, closed[84][84]={};
    for (int i=0;i<N;++i) for(int j=0;j<N;++j) {
        int common=0;
        for(int x:vertices[i])for(int y:vertices[j])common+=(x==y);
        open[i][j]=(common==0);
        closed[i][j]=open[i][j]||(i==j);
    }
    long long counts[2][5]={};
    for (int k=0;k<=4;++k) {
        vector<int> q(k);
        for(int j=0;j<k;++j) q[j]=j;
        while(true){
            for(int mode=0;mode<2;++mode){
                bool seen[16]={};int distinct=0;
                for(int center=0;center<N;++center){
                    int trace=0;
                    for(int j=0;j<k;++j)
                        if (mode?closed[center][q[j]]:open[center][q[j]])
                            trace|=(1<<j);
                    if(!seen[trace]){
                        seen[trace]=true;++distinct;
                        if(distinct==(1<<k))break;
                    }
                }
                if(distinct==(1<<k))++counts[mode][k];
            }
            int t=k-1;
            while(t>=0 && q[t]==N-k+t)--t;
            if(t<0)break;
            ++q[t];for(int j=t+1;j<k;++j)q[j]=q[j-1]+1;
        }
    }
    const long long expected[2][5]={{1,84,3486,26460,1260},
                                     {1,84,3486,56700,1260}};
    for(int mode=0;mode<2;++mode){
        cout<<(mode?"closed":"open")<<':';
        for(int k=0;k<=4;++k){
            cout<<' '<<counts[mode][k];
            if(counts[mode][k]!=expected[mode][k])return 1;
        }
        cout<<'\n';
    }
    cout<<"DIRECT n=9 SUPPORT CHECK: PASS\n";
}
