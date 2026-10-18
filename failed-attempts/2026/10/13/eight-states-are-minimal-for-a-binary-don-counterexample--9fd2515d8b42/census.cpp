#include <bits/stdc++.h>
using namespace std;
static uint64_t encode_map(const vector<int>& a,int n){
    uint64_t c=0,p=1; for(int i=0;i<n;i++){c+=p*(uint64_t)a[i];p*=n;} return c;
}
static vector<int> decode_map(uint64_t code,int n){
    vector<int>a(n); for(int i=0;i<n;i++){a[i]=code%n;code/=n;} return a;
}
static vector<int> rotate_conjugate(const vector<int>&a,int r,int n){
    vector<int>z(n); for(int q=0;q<n;q++){int pre=(q-r+n)%n;z[q]=(a[pre]+r)%n;} return z;
}
int main(){
    const vector<long long> ec={0,0,2,18,128,1200,9936,105840,1093632};
    const vector<long long> eb={0,0,0,0,0,0,0,0,544};
    vector<uint64_t> bad8;
    for(int n=2;n<=8;n++){
        uint64_t total=1; for(int i=0;i<n;i++) total*=n;
        int N=1<<n; vector<int> sz(N), bimg(N), a(n), aimg(N), dist(N), qv(N);
        for(int s=1;s<N;s++) sz[s]=sz[s>>1]+(s&1);
        for(int s=0;s<N;s++){int t=0;for(int q=0;q<n;q++)if((s>>q)&1)t|=1<<((q+1)%n);bimg[s]=t;}
        long long complete=0,bad=0;
        for(uint64_t code=0;code<total;code++){
            uint64_t x=code;for(int i=0;i<n;i++){a[i]=x%n;x/=n;}
            aimg[0]=0;for(int s=1;s<N;s++){int q=__builtin_ctz((unsigned)s);aimg[s]=aimg[s&(s-1)]|(1<<a[q]);}
            fill(dist.begin(),dist.end(),-1);int h=0,t=0,full=N-1;dist[full]=0;qv[t++]=full;
            while(h<t){int s=qv[h++],d=dist[s]+1;int u=aimg[s];if(dist[u]<0){dist[u]=d;qv[t++]=u;}u=bimg[s];if(dist[u]<0){dist[u]=d;qv[t++]=u;}}
            if(t!=N-1) continue;
            complete++;
            int violating=0;
            for(int s=1;s<N;s++){
                int bound=n*(n-sz[s]);
                if(dist[s]>bound){violating++;if(n!=8||sz[s]!=6||dist[s]!=17)return 20;}
            }
            if(violating){if(violating!=1)return 21;bad++;if(n==8)bad8.push_back(code);}
        }
        if(complete!=ec[n]||bad!=eb[n]) return 22;
    }
    if(bad8.size()!=544) return 23;
    unordered_set<uint64_t>B(bad8.begin(),bad8.end()),seen;
    int orbits=0;
    for(uint64_t code:bad8) if(!seen.count(code)){
        vector<int>a=decode_map(code,8); set<uint64_t> orb;
        for(int r=0;r<8;r++){uint64_t c=encode_map(rotate_conjugate(a,r,8),8);if(B.count(c))orb.insert(c);}
        if(orb.size()!=8)return 24;
        for(auto c:orb)seen.insert(c);orbits++;
    }
    if(orbits!=68||seen.size()!=544)return 25;
    vector<int> rep={0,0,3,5,1,2,6,7};
    for(uint64_t code:bad8) if(decode_map(code,8)<rep) return 26;
    cout<<"VERIFY_OK sizes=2..8 complete=2,18,128,1200,9936,105840,1093632 "
          "violations=0,0,0,0,0,0,544 first=8 "
          "n8_profile=size6-distance17-singleton-per-map rotation_orbits=68\n";
}
