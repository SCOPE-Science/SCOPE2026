// Independent enumeration of primitive circular Burrows-Wheeler last columns.
// Compile: g++ -std=c++17 -O2 -o verify_last_columns verify_last_columns.cpp
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <numeric>
#include <vector>
using namespace std;

// A last column belongs to one primitive necklace iff stable LF mapping
// forms one cycle on all row indices.
static bool one_primitive_necklace(const vector<int>& last, int alphabet_size) {
    int n = (int)last.size();
    vector<int> count(alphabet_size, 0), first(alphabet_size, 0);
    for (int c : last) ++count[c];
    for (int c = 1; c < alphabet_size; ++c)
        first[c] = first[c-1] + count[c-1];
    vector<int> seen_rank(alphabet_size, 0), lf(n);
    for (int i=0; i<n; ++i)
        lf[i] = first[last[i]] + seen_rank[last[i]]++;
    vector<char> seen(n, false);
    int i=0;
    for (int step=0; step<n; ++step) {
        if (seen[i]) return false;
        seen[i]=true;
        i=lf[i];
    }
    return i==0;
}
int main() {
    long long all_cases=0, primitive_cases=0;
    for (int n=3; n<=9; ++n) {
        int r=n-1;
        long long full=0, one_join=0;
        for(int repeated=0; repeated<r; ++repeated) {
            vector<int> last;
            for(int c=0;c<r;++c) last.push_back(c);
            last.push_back(repeated);
            sort(last.begin(),last.end());
            do {
                ++all_cases;
                if (!one_primitive_necklace(last,r)) continue;
                ++primitive_cases;
                int runs=1;
                for(int i=1;i<n;++i) runs+=(last[i]!=last[i-1]);
                assert(runs==n || runs==n-1);
                if(runs==n) ++full;
                else ++one_join;
            }while(next_permutation(last.begin(),last.end()));
        }
        long long fact=1;
        for(int i=2;i<=r;++i) fact*=i;
        assert(full==fact*(n-3)/2);
        assert(one_join==fact);
        printf("n=%d full=%lld one_join=%lld\n",n,full,one_join);
    }
    printf("total_candidate_last_columns=%lld one_cycle_last_columns=%lld\n",all_cases,primitive_cases);
}
