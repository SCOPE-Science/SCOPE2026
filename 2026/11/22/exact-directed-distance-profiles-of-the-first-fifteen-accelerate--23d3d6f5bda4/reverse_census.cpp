// Independent reverse-edge distance census for accelerated Kolakoski graphs.
// Independently implements the published block recurrence, reverses both permutations, and checks inward distances.
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
using namespace std;
static vector<vector<int>> P{{}, {1,0}}, Q{{}, {1,0}};
int main(int argc,char **argv){int max_n=15;if(argc>1)max_n=atoi(argv[1]);if(max_n<1||max_n>18)return 2;
 for(int n=2;n<=max_n;++n){int m=1<<(n-1);vector<int> p(2*m),q(2*m);
  for(int w=0;w<2*m;w++){
    bool b=(w>=m);int suffix=w%m;
    p[w]=(!b?m+Q[n-1][suffix]:P[n-1][suffix]);
    q[w]=(!b?m+Q[n-1][Q[n-1][suffix]]:P[n-1][P[n-1][suffix]]);
  } P.push_back(p);Q.push_back(q);
 }
 for(int n=1;n<=max_n;++n){int m=1<<n;vector<int> ip(m,-1),iq(m,-1);
   for(int i=0;i<m;i++){
     if(ip[P[n][i]]!=-1||iq[Q[n][i]]!=-1)return 3;
     ip[P[n][i]]=i;iq[Q[n][i]]=i;
   }
   vector<int> dist(m,0),queue(m,0),stamp(m,0);int epoch=0,D=0;
   vector<unsigned long long> profile(m+1,0);
   for(int end=0;end<m;++end){
      ++epoch;int head=0,tail=1;queue[0]=end;stamp[end]=epoch;dist[end]=0;
      while(head<tail){int u=queue[head++],dep=dist[u];++profile[dep];
       for(int pre:{ip[u],iq[u]})if(stamp[pre]!=epoch){stamp[pre]=epoch;dist[pre]=dep+1;queue[tail++]=pre;D=max(D,dep+1);}
      }
      if(tail!=m)return 4;
   }
   unsigned long long s=0;for(auto c:profile)s+=c;
   if(s!=(unsigned long long)m*m)return 5;
   printf("%d %d %llu\n",n,D,profile[D]);fflush(stdout);
 }
}
