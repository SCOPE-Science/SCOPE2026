#include <bits/stdc++.h>
using namespace std;
int N; int fact[13];
int rankp(const array<unsigned char,12> &p){int mask=(1<<N)-1; int r=0;for(int i=0;i<N;i++){int v=p[i];int num=__builtin_popcount((unsigned)(mask & ((1<<v)-1)));r+=num*fact[N-1-i];mask^=(1<<v);}return r;}
array<unsigned char,12> unrank(int r){array<unsigned char,12> p{};int mask=(1<<N)-1;for(int i=0;i<N;i++){int kth=r/fact[N-1-i];r%=fact[N-1-i];int v=0;for(;v<N;v++){if(mask&(1<<v)){if(kth==0)break; --kth;}}p[i]=v;mask^=(1<<v);}return p;}
int main(int argc,char **argv){int cols=atoi(argv[1]);if(cols<2 || cols>5){cerr<<"supported columns: 2..5\n";return 2;}N=2*cols;fact[0]=1;for(int i=1;i<=N;i++)fact[i]=i*fact[i-1];int size=fact[N];vector<pair<int,int>> edges;for(int r=0;r<2;r++)for(int c=0;c<cols-1;c++)edges.emplace_back(r*cols+c,r*cols+c+1);for(int c=0;c<cols;c++)edges.emplace_back(c,c+cols);
vector<int8_t> dist(size,-1);vector<int> q(size);int head=0,tail=1;q[0]=0;dist[0]=0;int diameter=0;vector<long long> count(100,0);vector<int> furthest;count[0]++;
while(head<tail){int u=q[head++];auto p=unrank(u);int d=dist[u];for(auto [a,b]:edges){swap(p[a],p[b]);int v=rankp(p);swap(p[a],p[b]);if(dist[v]!=-1)continue;dist[v]=d+1;q[tail++]=v;count[d+1]++;if(d+1>diameter){diameter=d+1;furthest.clear();}if(d+1==diameter)furthest.push_back(v);}}
if(tail!=size){cerr<<"incomplete BFS\n";return 2;}for(int rank=0;rank<size;rank++){if(rankp(unrank(rank))!=rank){cerr<<"rank error\n";return 3;}}
cout<<"cols "<<cols<<" states "<<tail<<" edges "<<edges.size()<<" diameter "<<diameter<<" antipodes "<<furthest.size()<<"\ncounts";for(int i=0;i<=diameter;i++)cout<<" "<<count[i];cout<<"\n";
cout<<"furthest";for(int v:furthest){cout<<" [";auto p=unrank(v);for(int i=0;i<N;i++)cout<<(i?",":"")<<int(p[i]);cout<<"]";}cout<<"\n";
vector<vector<int>> gd(N,vector<int>(N,99));for(int i=0;i<N;i++)gd[i][i]=0;for(auto [a,b]:edges)gd[a][b]=gd[b][a]=1;for(int k=0;k<N;k++)for(int i=0;i<N;i++)for(int j=0;j<N;j++)gd[i][j]=min(gd[i][j],gd[i][k]+gd[k][j]);
long long maxgap=-1;vector<long long> gaps(20,0);vector<int> gapwitness;for(int u=0;u<size;u++){auto p=unrank(u);int D=0;for(int i=0;i<N;i++)D+=gd[i][p[i]];if(D%2){cerr<<"odd distance sum\n";return 3;}int delta=dist[u]-D/2;
if(delta<0){cerr<<"error";return 1;}if(delta>=int(gaps.size())){cerr<<"gap too high";return 1;}gaps[delta]++;if(delta>maxgap){maxgap=delta;gapwitness.clear();}if(delta==maxgap && gapwitness.size()<10)gapwitness.push_back(u);}
cout<<"maxgap "<<maxgap<<" hist";for(int i=0;i<=maxgap;i++)cout<<" "<<gaps[i];cout<<"\nwitnesses";for(auto u:gapwitness){auto p=unrank(u);cout<<" [";for(int i=0;i<N;i++)cout<<(i?",":"")<<int(p[i]);cout<<"]";}cout<<"\n";
}
