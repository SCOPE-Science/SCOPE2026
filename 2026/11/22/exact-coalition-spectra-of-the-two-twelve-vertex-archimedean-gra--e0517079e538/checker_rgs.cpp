#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){int mode=argc>1?atoi(argv[1]):0; vector<pair<int,int>> edges;
 if(mode==0){for(int x=0;x<8;x++)for(int b=0;b<3;b++)if(!(x&(1<<b)))edges.push_back({x,x^(1<<b)});}else { // truncated tetrahedron: vertices directed edges of K4 (a,b), a!=b. triangle on each first a, and each pair (a,b)-(b,a)
 for(int a=0;a<4;a++)for(int b=0;b<4;b++)if(a!=b)edges.push_back({a,b});}
 int n=edges.size(); vector<int> neigh(n,0);
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){bool adj = mode==0?(edges[i].first==edges[j].first ||edges[i].first==edges[j].second||edges[i].second==edges[j].first||edges[i].second==edges[j].second):(edges[i].first==edges[j].first||(edges[i].first==edges[j].second&&edges[i].second==edges[j].first));if(adj)neigh[i]|=1<<j;}
 int U=(1<<n)-1;
 vector<uint8_t> dom(1<<n,0); vector<int> closed(n);for(int i=0;i<n;i++)closed[i]=neigh[i]|1<<i;
 for(int m=0;m<=U;m++){int hit=0;for(int i=0;i<n;i++)if((m>>i)&1)hit|=closed[i];dom[m]=(hit==U);}
 vector<int> masks(n,0),part(n,0);vector<long long> counts(n+1,0), profiles[15];
 vector<long long> cgedges(n+1,0);
 vector<pair<vector<int>,int>> maximal;
 long long tot=0;
 auto go=[&](auto&&self,int pos,int k)->void {
 if(pos==n){tot++;int partners[12]={};int edgesCnt=0;for(int a=0;a<k;a++){if(dom[masks[a]])return;for(int b=a+1;b<k;b++)if(dom[masks[a]|masks[b]]){partners[a]++;partners[b]++;edgesCnt++;}}for(int a=0;a<k;a++)if(!partners[a])return;
 counts[k]++;cgedges[k]+=edgesCnt;vector<int> ps;for(int i=0;i<k;i++)ps.push_back(__builtin_popcount((unsigned)masks[i]));sort(ps.begin(),ps.end());int code=0;for(int x:ps)code=code*16+x; profiles[k].push_back(code);return;}
 for(int i=0;i<k;i++){masks[i]|=1<<pos;self(self,pos+1,k);masks[i]^=1<<pos;}masks[k]=1<<pos;self(self,pos+1,k+1);masks[k]=0;
 };
 masks[0]=1;go(go,1,1);
 cout<<"graph="<<(mode==0?"cuboctahedron":"truncated_tetrahedron")<<" n="<<n<<" partitions="<<tot<<"\n";
 for(int k=0;k<=n;k++)if(counts[k]){cout<<"k="<<k<<" count="<<counts[k]<<" sum_coalition_edges="<<cgedges[k]<<" profiles=";map<int,int> f;for(auto x:profiles[k])f[x]++;for(auto [a,b]:f){vector<int> ps;auto m=a;while(m){ps.push_back(m%16);m/=16;}reverse(ps.begin(),ps.end());cout<<"[";for(auto z:ps)cout<<z<<",";cout<<"]:"<<b<<" ";}cout<<"\n";}
}
