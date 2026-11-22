// Exact brute-force search over all set partitions of the vertices, independent of the normal form.
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdint>
using namespace std;
int n,N; vector<int> c; vector<long long> counts; long long partitions=0,proper=0; long long locatingOnly=0,nlOnly=0;
void test(int k){
 ++partitions;
 vector<uint64_t> masks(k,0);
 for(int v=0;v<N;v++) masks[c[v]] |=1ULL<<v;
 for(int i=0;i<n;i++) for(int j=0;j<n;j++) if(i!=j && c[i]==c[n+j])return;
 ++proper;
 uint64_t sig[24]={};
 for(int v=0;v<N;v++){
   int i=v%n; int side=v/n;
   for(int j=0;j<n;j++)if(i!=j){int w=side?j:n+j;sig[v] |=1ULL<<c[w];}
 }
 bool nl=true, locate=true;
 for(int i=0;i<N;i++)for(int j=0;j<i;j++)if(c[i]==c[j]&&sig[i]==sig[j])nl=false;
 vector<vector<int>> distances(N,vector<int>(k,5));
 for(int v=0;v<N;v++)for(int w=0;w<N;w++){
   int dist;
   if(v==w)dist=0;
   else if(v/n==w/n)dist=2;
   else if(v%n==w%n)dist=3;
   else dist=1;
   distances[v][c[w]]=min(distances[v][c[w]],dist);
 }
 for(int v=0;v<N;v++)for(int w=0;w<v;w++)if(c[v]==c[w]&&distances[v]==distances[w])locate=false;
 if(locate&&!nl)locatingOnly++;
 if(nl&&!locate)nlOnly++;
 if(nl)counts[k]++;
}
void dfs(int pos,int k){
 if(pos==N){test(k);return;}
 for(int color=0;color<=k;color++){
   c[pos]=color;
   if(pos>=n) {
     int i=pos-n;
     // only opposite-shore vertices with different matched indices are adjacent
     bool bad=false;
     for(int j=0;j<n;j++)if(j!=i && c[j]==color){bad=true;break;}
     if(bad)continue;
   }
   dfs(pos+1,max(k,color+1));
 }
}
int main(){
 for(n=2;n<=6;n++) {
  N=2*n;counts.assign(N+1,0);c.assign(N,0);partitions=proper=0;locatingOnly=nlOnly=0;
  c[0]=0;dfs(1,1);
  int optimum=0;while(optimum<=N&&counts[optimum]==0)optimum++;
  long long expect= n;
  long long t=1;for(int i=0;i<n-1;i++)t*=3;
  expect = n*t - (n-2)*(1LL<<n)-2;
  cout<<"n="<<n<<" partitions="<<partitions<<" proper="<<proper<<" optimum="<<optimum<<" optimal_partitions="<<counts[optimum]<<" expected="<<expect<<" locatingOnly="<<locatingOnly<<" nlOnly="<<nlOnly<<"\n";
  if(optimum!=n+1 || counts[optimum]!=expect || locatingOnly || nlOnly)return 2;
 }
 cout<<"EXHAUSTIVE_OK\n";
}
