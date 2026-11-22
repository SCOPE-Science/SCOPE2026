#include <bits/stdc++.h>
using namespace std;
constexpr uint32_t M=(1u<<20);
array<array<int,4>,20> nei;int edgeidx[5][5];
void build(){int k=10;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++){edgeidx[i][j]=edgeidx[j][i]=k;nei[k++]={2*i,2*i+1,2*j,2*j+1};}
for(int i=0;i<5;i++)for(int e=0;e<2;e++){int t=0;for(int j=0;j<5;j++)if(j!=i)nei[2*i+e][t++]=edgeidx[i][j];}}
uint32_t F(uint32_t x){uint32_t y=0;for(int i=0;i<20;i++){int c=0;for(int v:nei[i]) c+=(x>>v)&1; if(c>2||(c==2&&((x>>i)&1)))y|=1u<<i;}return y;}
uint32_t apply(uint32_t x,array<int,20> &m){uint32_t y=0;for(int v=0;v<20;v++) if(x&(1u<<v))y|=1u<<m[v];return y;}
int main(){build(); vector<array<int,20>> gen;
for(int i=0;i<4;i++){
 array<int,5> perm={0,1,2,3,4};swap(perm[i],perm[i+1]);array<int,20> m;
 for(int j=0;j<5;j++)for(int e=0;e<2;e++)m[2*j+e]=2*perm[j]+e;
 for(int j=0;j<5;j++)for(int k=j+1;k<5;k++)m[edgeidx[j][k]]=edgeidx[perm[j]][perm[k]];
 gen.push_back(m);}
for(int i=0;i<5;i++){array<int,20> m;for(int j=0;j<20;j++)m[j]=j;swap(m[2*i],m[2*i+1]);gen.push_back(m);}
vector<uint8_t> seen(M,0);
for(int period=1;period<=2;period++){
 map<int,int> orbitSizes;
 map<pair<int,int>,int> orbitTypes;
 int countOrbits=0;vector<uint32_t> q;
 for(uint32_t x=0;x<M;x++){
    uint32_t y=F(x); bool recurrent=period==1?y==x:(F(y)==x && y!=x);
    if(!recurrent||seen[x])continue;
    seen[x]=1;q.clear();q.push_back(x);
    for(size_t k=0;k<q.size();k++){
       uint32_t z=q[k];
       for(auto &m:gen){uint32_t w=apply(z,m);if(!seen[w]){seen[w]=1;q.push_back(w);}}
       if(period==2){uint32_t w=F(z);if(!seen[w]){seen[w]=1;q.push_back(w);}}
    }
    int active=__builtin_popcount(x);orbitSizes[(int)q.size()]++;countOrbits++;
 }
 cout<<"PERIOD "<<period<<" spatial"<<(period==2?"+time":"")<<"_orbit_count="<<countOrbits<<"\n";
 for(auto [s,n]:orbitSizes)cout<<"size="<<s<<" number="<<n<<"\n";
}
}
