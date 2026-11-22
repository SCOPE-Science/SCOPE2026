#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

// Direct vertex-level enumeration; labels are 0, 1, or 2, and both colour classes must be independent.
int main(){
    for(int n=3;n<=7;++n){
        const int V=2*n; uint64_t limit=1;
        for(int i=0;i<V;++i) limit*=3;
        vector<array<int,3>> nbr(V);
        for(int c=0;c<n;++c)for(int r=0;r<2;++r){
            int v=2*c+r;
            nbr[v]={2*((c+n-1)%n)+r, 2*((c+1)%n)+r, 2*c+(1-r)};
        }
        vector<int> a(V); uint64_t count=0; int minwt=V+1;
        for(uint64_t t=0;t<limit;++t){
            uint64_t z=t;int w=0;
            for(int v=0;v<V;++v){a[v]=int(z%3);z/=3;w+=(a[v]!=0);}
            if(w>minwt)continue;
            bool valid=true;
            for(int v=0;v<V&&valid;++v){
                if(a[v]){
                    for(int u:nbr[v])if(a[u]==a[v]){valid=false;break;}
                }else{
                    int seen=0;
                    for(int u:nbr[v])seen|=(a[u]==1?1:(a[u]==2?2:0));
                    valid=(seen==3);
                }
            }
            if(!valid)continue;
            if(w<minwt){minwt=w;count=0;}
            if(w==minwt)++count;
        }
        cout<<"n="<<n<<" minimum="<<minwt<<" optimal="<<count<<" enumerated="<<limit<<"\n";
        const uint64_t known[8]={0,0,0,18,24,40,76,112};
        if(minwt!=(n==3?4:n) || count!=known[n])return 2;
    }
    return 0;
}
