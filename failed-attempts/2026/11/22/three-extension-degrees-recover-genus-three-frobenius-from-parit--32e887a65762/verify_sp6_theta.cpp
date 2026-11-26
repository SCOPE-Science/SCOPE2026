#include <bits/stdc++.h>
using namespace std;
using ull=uint64_t;
int B(int x,int y){int a=x&7,b=(x>>3)&7,c=y&7,d=(y>>3)&7;return (__builtin_parity((a&d)^(b&c)));}
int Q(int x){return __builtin_parity((x&7)&((x>>3)&7));}
int apply(ull A,int x){int y=0;for(int i=0;i<6;i++) if(x>>i&1)y^=(A>>(6*i))&63;return y;}
ull identity(){ull a=0;for(int i=0;i<6;i++)a|=ull(1<<i)<<(6*i);return a;}
ull right_trans(ull A,int v){int w=apply(A,v);ull z=0;for(int i=0;i<6;i++){int c=(A>>(6*i))&63;if(B(1<<i,v))c^=w;z |=ull(c)<<(6*i);}return z;}
string part(const array<int,64>&perm,int parity){bool seen[64]={};vector<int> cs;for(int u=0;u<64;u++)if(Q(u)==parity&&!seen[u]){int v=u,n=0;do{seen[v]=1;v=perm[v];n++;if(n>64){cerr<<"bad loop";exit(3);}}while(v!=u);cs.push_back(n);}sort(cs.begin(),cs.end());string s;for(int x:cs){if(s.size())s+=",";s+=to_string(x);}return s;}
int main(){vector<int> vs={1,2,4,8,16,32,3,6};vector<ull> group;group.reserve(1451520);unordered_set<ull> seen;seen.reserve(2000000);auto I=identity();seen.insert(I);group.push_back(I);for(size_t z=0;z<group.size();z++){ull A=group[z];for(int v:vs){ull H=right_trans(A,v);if(seen.insert(H).second)group.push_back(H);}if(group.size()>1600000){cerr<<"bad";return 1;}}cerr<<"ORDER "<<group.size()<<"\n";map<pair<string,string>,long long> counts;for(ull A:group){int d=0;for(int i=0;i<6;i++)if(Q((A>>(6*i))&63))d^=1<<(i<3?i+3:i-3);int c=apply(A,d);array<int,64> pm;for(int u=0;u<64;u++){pm[u]=apply(A,u)^c;if(Q(pm[u])!=Q(u)){cerr<<"BAD ARF";return 2;}}
 counts[{part(pm,1),part(pm,0)}]++;
}
cerr<<"SPECTRA "<<counts.size()<<"\n";int maxlen=20;
for(int n=1;n<=maxlen;n++){
 map<vector<int>,int> m;for(auto [k,v]:counts){vector<int> sig;for(auto s:{k.first,k.second}){vector<int> cs;istringstream in(s);string x;while(getline(in,x,','))cs.push_back(stoi(x));for(int z=1;z<=n;z++){int cnt=0;for(int r:cs)if(z%r==0)cnt+=r;sig.push_back(cnt);}}m[sig]++;}
 int coll=0;for(auto [k,nv]:m)if(nv>1)coll+=nv-1;cout<<"prefix="<<n<<" distinct="<<m.size()<<" collisions="<<coll<<"\n";if(m.size()==counts.size())break;
}
int i=0;for(auto [k,cnt]:counts)cout<<"SPEC,"<<++i<<","<<k.first<<";"<<k.second<<","<<cnt<<"\n";
}
