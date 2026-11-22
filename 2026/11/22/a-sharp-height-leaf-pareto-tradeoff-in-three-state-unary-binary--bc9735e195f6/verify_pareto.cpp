// Independent exact dynamic programming by height and exact variable-leaf count.
// Build: g++ -O2 -std=c++17 verify_pareto.cpp -o v2 && ./v2
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
using namespace std;
int main(){
    map<string,long long> frontiers;
    long long no_reset=0, conflict=0, total=0;
    for(int code=0;code<531441;++code){
        int z=code, u[3], b[3][3];
        for(int i=0;i<3;++i){u[i]=z%3;z/=3;}
        for(int i=0;i<3;++i)for(int j=0;j<3;++j){b[i][j]=z%3;z/=3;}
        int U[8]{}, B[8][8]{};
        for(int s=1;s<8;++s)for(int i=0;i<3;++i)if(s&(1<<i))U[s]|=1<<u[i];
        for(int s=1;s<8;++s)for(int t=1;t<8;++t)
            for(int i=0;i<3;++i)for(int j=0;j<3;++j)
                if((s&(1<<i))&&(t&(1<<j))) B[s][t]|=1<<b[i][j];
        // A[h][l] records all subset images from terms of height <=h
        // and exactly l distinct, independently varied state leaves.
        uint8_t images[5]{};images[1]=1<<(7-1);
        bool possible[5][5]{};
        for(int h=0;h<=4;++h){
            for(int l=1;l<=4;++l)if(images[l]&0b00001011)possible[h][l]=true;
            if(h==4)break;
            uint8_t next[5];for(int l=0;l<=4;++l)next[l]=images[l];
            for(int l=1;l<=4;++l)for(int s=1;s<8;++s)
                if(images[l]&(1<<(s-1)))next[l]|=1<<(U[s]-1);
            for(int l=2;l<=4;++l)for(int i=1;i<l;++i)
                for(int s=1;s<8;++s)if(images[i]&(1<<(s-1)))
                    for(int t=1;t<8;++t)if(images[l-i]&(1<<(t-1)))
                        next[l]|=1<<(B[s][t]-1);
            for(int l=1;l<=4;++l)images[l]=next[l];
        }
        int hmin=5,lmin=5;
        for(int h=1;h<=4;++h)for(int l=1;l<=4;++l)if(possible[h][l]){
            hmin=min(hmin,h); lmin=min(lmin,l);
        }
        if(hmin==5){++no_reset;continue;}
        ++total;
        if(!possible[hmin][lmin])++conflict;
        string shape;
        for(int h=1;h<=4;++h)for(int l=1;l<=4;++l)if(possible[h][l]){
            bool dominated=false;
            for(int h2=1;h2<=h;++h2)for(int l2=1;l2<=l;++l2)
                if((h2!=h || l2!=l) && possible[h2][l2]) dominated=true;
            if(!dominated){if(!shape.empty())shape+=";";
                shape+=to_string(h)+","+to_string(l);}
        }
        ++frontiers[shape];
    }
    const map<string,long long> expected={
        {"1,1",59049},{"1,2",54},{"1,2;2,1",18},
        {"2,1",118080},{"2,2",14088},{"2,3",1572},{"2,4",1056},
        {"3,2",35448},{"3,3",2976},{"3,4",1764},
        {"3,4;4,3",180},{"4,3",5220},{"4,4",3492}
    };
    assert(frontiers==expected);
    assert(no_reset==288444 && total==242997 && conflict==198);
    cout << "PARETO_OK total=531441 nonsync=288444 conflict=198 deep=180\n";
}
