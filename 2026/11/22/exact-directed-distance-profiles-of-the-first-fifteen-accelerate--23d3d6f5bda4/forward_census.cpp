// Exact directed distances in the unweighted accelerated Schreier graphs.
// Source recurrence: Mitchell--Walton--Whittaker (2026), Corollary 4.8.
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 int max_n=15; if(argc>1) max_n=atoi(argv[1]); if(max_n<1 || max_n>20)return 2;
 vector<int> p{1,0},q{1,0};
 for(int n=1;n<=max_n;++n){
  const int N=(int)p.size();
  vector<int> mark(N,0),d(N,0),queue(N); int tag=0,diam=0,rad=N+1;
  vector<unsigned long long> ecc(N+1,0),dist(N+1,0);
  for(int s=0;s<N;++s){
    ++tag; int left=0,right=1;queue[0]=s;mark[s]=tag;d[s]=0;
    int far=0;
    while(left<right){
      int u=queue[left++], depth=d[u];++dist[depth];far=max(far,depth);
      int a=p[u],b=q[u];
      if(mark[a]!=tag){mark[a]=tag;d[a]=depth+1;queue[right++]=a;}
      if(mark[b]!=tag){mark[b]=tag;d[b]=depth+1;queue[right++]=b;}
    }
    if(right!=N){fprintf(stderr,"Graph not connected n=%d s=%d visited=%d\n",n,s,right);return 3;}
    ++ecc[far];diam=max(diam,far);rad=min(rad,far);
  }
  printf("n=%d N=%d radius=%d diameter=%d ecc=",n,N,rad,diam);
  for(int j=rad;j<=diam;++j)if(ecc[j])printf("%s%d:%llu",j==rad?"":",",j,ecc[j]);
  printf(" distance_pairs=");
  for(int j=0;j<=diam;++j)printf("%s%llu",j==0?"":",",dist[j]);
  printf("\n");fflush(stdout);
  if(n==max_n)break;
  vector<int> p2(2*N),q2(2*N);
  for(int i=0;i<N;++i){
    p2[i]=N+q[i];p2[N+i]=p[i];
    q2[i]=N+q[q[i]];q2[N+i]=p[p[i]];
  }
  p.swap(p2);q.swap(q2);
 }
}
