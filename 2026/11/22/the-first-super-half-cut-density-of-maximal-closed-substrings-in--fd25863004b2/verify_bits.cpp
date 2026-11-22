// Independent bit-level exhaustive certificate for binary MCS crossing density.
// Compile: c++ -O2 -std=c++17 verify_bits.cpp -o verify_bits && ./verify_bits
#include <algorithm>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

static bool test_closed(int word, int len) {
    if (len == 1) return true;
    for (int b = len-1; b >= 1; --b) {
        int mask = (1<<b)-1;
        if ((word & mask) != (word>>(len-b))) continue;
        int occ = 0;
        for (int at=0; at<=len-b; ++at)
            if (((word>>at)&mask)==(word&mask)) ++occ;
        if (occ == 2) return true;
    }
    return false;
}
static string bits(int word,int len) {
    string s;
    for(int i=0;i<len;++i) s += char('0'+((word>>i)&1));
    return s;
}
int main() {
    // The precomputed intrinsic closedness table depends on substring bits alone.
    constexpr int N=14;
    vector<vector<unsigned char>> is_closed(N+1);
    for(int len=1;len<=N;++len) {
        is_closed[len].resize(1<<len);
        for(int u=0;u<(1<<len);++u) is_closed[len][u]=test_closed(u,len);
    }
    const int expected[15]={0,0,1,1,2,2,3,3,4,4,5,5,6,7,8};
    vector<pair<string,int>> extremizers;
    for(int n=2;n<=N;++n){
        int maximum=0;
        for(int w=0;w<(1<<n);++w){
            unsigned char c[14][14]{};
            for(int i=0;i<n;++i)for(int j=i;j<n;++j){
                int len=j-i+1;
                c[i][j]=is_closed[len][(w>>i)&((1<<len)-1)];
            }
            int difference[15]{};
            for(int i=0;i<n;++i)for(int j=i+1;j<n;++j)
                if(c[i][j] && (i==0||!c[i-1][j]) && (j==n-1||!c[i][j+1])){
                    ++difference[i];--difference[j];
                }
            int cnt=0;
            for(int cut=0;cut<n-1;++cut){
                cnt+=difference[cut];
                maximum=max(maximum,cnt);
                if(n==14 && cnt>=8) extremizers.push_back({bits(w,n),cut+1});
            }
        }
        assert(maximum==expected[n]);
        cout << "n="<<n<<" max_crossings="<<maximum<<"\n";
    }
    sort(extremizers.begin(),extremizers.end());
    const vector<pair<string,int>> expected_pairs={
        {"00101110100011",8}, {"00111010001011",6},
        {"11000101110100",6}, {"11010001011100",8}
    };
    assert(extremizers==expected_pairs);
    cout << "four_pairs:";
    for(const auto &p:extremizers) cout<<" "<<p.first<<"@"<<p.second;
    cout<<"\nBITS_PASS\n";
}
