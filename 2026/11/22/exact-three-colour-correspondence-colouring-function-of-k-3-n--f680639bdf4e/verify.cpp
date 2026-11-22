#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;
using i64=long long;

int main() {
    array<array<int,3>,6> perms{};
    array<int,3> a{0,1,2};
    for (int i=0;i<6;i++) {
        perms[i]=a;
        if (i<5) assert(next_permutation(a.begin(),a.end()));
    }
    array<array<int,27>,36> f{};
    for (int b=0;b<6;b++) for (int c=0;c<6;c++)
      for (int x=0;x<3;x++) for (int y=0;y<3;y++) for (int z=0;z<3;z++) {
        array<int,3> used{};
        used[x]=used[perms[b][y]]=used[perms[c][z]]=1;
        f[6*b+c][9*x+3*y+z]=3-used[0]-used[1]-used[2];
      }
    const array<int,6> expected{24,18,14,6,5,0};
    const array<i64,6> expected_tests{1,36,666,8436,82251,658008};
    const vector<vector<int>> witness{{0},{0,22},{0,8,29},
       {0,8,29,33},{0,1,8,16,24},{0,3,4,18,21,22}};
    for (int n=1;n<=6;n++) {
        int best=numeric_limits<int>::max();
        i64 tested=0, minimizers=0;
        vector<int> weights(f[0].begin(),f[0].end());
        function<void(int,int)> walk=[&](int last,int taken) {
            if (taken==n) {
                int total=0;
                for (int v:weights) total+=v;
                ++tested;
                if (total<best) { best=total; minimizers=1; }
                else if (total==best) ++minimizers;
                return;
            }
            for (int t=last;t<36;t++) {
                auto old=weights;
                for (int j=0;j<27;j++) weights[j]*=f[t][j];
                walk(t,taken+1);
                weights=old;
            }
        };
        walk(0,1);
        assert(tested==expected_tests[n-1]);
        assert(best==expected[n-1]);
        int witness_formula=0;
        for(int j=0;j<27;j++) {
            int product=1;
            for(int t:witness[n-1]) product*=f[t][j];
            witness_formula+=product;
        }
        assert(witness_formula==best);
        int witness_direct=0;
        int total_assignments=1;
        for(int i=0;i<3+n;i++) total_assignments*=3;
        for(int k=0;k<total_assignments;k++) {
            vector<int> colors(3+n);
            int v=k;
            for(int i=0;i<3+n;i++){colors[i]=v%3;v/=3;}
            bool valid=true;
            for(int i=0;i<n;i++) {
                int type=witness[n-1][i];
                if(colors[3+i]==colors[0] ||
                   colors[3+i]==perms[type/6][colors[1]] ||
                   colors[3+i]==perms[type%6][colors[2]]) {
                   valid=false;break;
                }
            }
            witness_direct+=valid;
        }
        assert(witness_direct==best);
        cout<<"n="<<n<<" minimum="<<best<<" combinations="<<tested
            <<" normalized_minimizers="<<minimizers
            <<" direct_witness="<<witness_direct<<" PASS\n";
    }
    // The six normalized types 0,3,4,18,21,22 kill every left triple.
    for(int j=0;j<27;j++) {
        bool killed=false;
        for(int t:witness[5]) if(f[t][j]==0) killed=true;
        assert(killed);
    }
    cout << "ALL_27_LEFT_TRIPLES_COVERED PASS\nVERIFY_OK\n";
}
