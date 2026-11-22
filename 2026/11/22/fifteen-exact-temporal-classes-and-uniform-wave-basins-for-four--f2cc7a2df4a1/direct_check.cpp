// Independent complete-state enumerator for graph K_n with a private leaf at each vertex.
// For each n=2,3,4,5, enumerate all 4^(2n) labelled configurations.
#include <cstdint>
#include <cstdio>
#include <vector>
#include <map>
#include <utility>
using namespace std;

int main() {
    for (int n=2; n<=5; ++n) {
        const int N=1<<(4*n);
        vector<int> to(N), indeg(N,0), queue; queue.reserve(N);
        for (int x=0; x<N; ++x) {
            bool excited=false;
            for (int i=0; i<n; ++i) if (((x>>(2*i))&3)==1) excited=true;
            int y=0;
            for (int i=0; i<n; ++i) {
                int c=(x>>(2*i))&3;
                int l=(x>>(2*(n+i)))&3;
                int a=c ? (c+1)%4 : int(excited || l==1);
                int b=l ? (l+1)%4 : int(c==1);
                y |= a<<(2*i);
                y |= b<<(2*(n+i));
            }
            to[x]=y; ++indeg[y];
        }
        for (int x=0; x<N; ++x) if (!indeg[x]) queue.push_back(x);
        for (size_t j=0; j<queue.size(); ++j) {
            int y=to[queue[j]];
            if (--indeg[y]==0) queue.push_back(y);
        }
        vector<int> entry(N,-1), period(N,0);
        for (int x=0; x<N; ++x) if (indeg[x] && entry[x]<0) {
            int v=x, p=0;
            do {v=to[v]; ++p;} while(v!=x);
            v=x;
            do {entry[v]=0;period[v]=p;v=to[v];} while(v!=x);
        }
        for (int j=(int)queue.size()-1; j>=0; --j) {
            int x=queue[j], y=to[x];
            entry[x]=entry[y]+1;
            period[x]=period[y];
        }
        map<pair<int,int>,int64_t> freq;
        for (int x=0; x<N; ++x) {
            if (entry[x]<0 || period[x]==0) return 1;
            freq[{entry[x],period[x]}]++;
        }
        for (const auto &it:freq) printf("%d,%d,%d,%lld\n",n,it.first.first,it.first.second,(long long)it.second);
    }
    return 0;
}
