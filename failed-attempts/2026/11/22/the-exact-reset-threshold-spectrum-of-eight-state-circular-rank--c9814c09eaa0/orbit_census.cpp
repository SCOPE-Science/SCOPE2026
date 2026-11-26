#include <bits/stdc++.h>
using namespace std;
// Complete alphabet is a cyclic permutation a(i)=i+1 mod 8 and an arbitrary rank-six map b.
static inline int rank8(const array<uint8_t,8>& b){ unsigned m=0;for(auto x:b)m|=1u<<x;return __builtin_popcount(m); }
static inline array<uint8_t,8> rotated(const array<uint8_t,8>& b,int k){array<uint8_t,8> q;for(int i=0;i<8;i++)q[i]=(b[(i+8-k)&7]+k)&7;return q;}
static inline int threshold(const array<uint8_t,8>& b,int *viscnt=nullptr){
  unsigned char bm[256];bm[0]=0;
  for(int s=1;s<256;s++){int i=__builtin_ctz((unsigned)s);bm[s]=bm[s&(s-1)]|(1<<b[i]);}
  unsigned char dist[256];memset(dist,255,sizeof dist);
  unsigned char queue[256]; int head=0,tail=0;queue[tail++]=255;dist[255]=0;
  while(head<tail){int s=queue[head++];int d=dist[s];
    int a=((s<<1)|(s>>7))&255;
    if(dist[a]==255){if((a&(a-1))==0){if(viscnt)*viscnt=tail+1;return d+1;} dist[a]=d+1;queue[tail++]=a;}
    int t=bm[s];
    if(dist[t]==255){if((t&(t-1))==0){if(viscnt)*viscnt=tail+1;return d+1;} dist[t]=d+1;queue[tail++]=t;}
  }
  if(viscnt)*viscnt=tail; return -1;
}
int main(int argc,char**argv){
 bool canonical=argc==1 || string(argv[1])=="canonical";
 map<int,long long> hist; long long rank6=0,representatives=0,orbitmass=0;int mx=-1, max_count=0; vector<array<uint8_t,8>> max_reps;
 long long inspected=0, visit_total=0;
 array<uint8_t,8>b;
 for(int z=0;z<16777216;z++){
   int t=z;unsigned mask=0;
   for(int i=0;i<8;i++){int v=t&7;t>>=3;b[i]=v;mask|=1u<<v;}
   if(__builtin_popcount(mask)!=6)continue;
   ++rank6;
   if(canonical){bool ismin=true;for(int k=1;k<8;k++){auto q=rotated(b,k);if(q<b){ismin=false;break;}}if(!ismin)continue;}
   int orbit=1;
   if(canonical){for(int k=1;k<8;k++)if(rotated(b,k)==b){orbit=8/__gcd(8,k);break;}
     // actual orbit count = 8/number of distinct stabilizing rotations
     int stabilizer=0;for(int k=0;k<8;k++)if(rotated(b,k)==b)stabilizer++;
     orbit=8/stabilizer;
   }
   representatives++;orbitmass+=orbit;
   int visited=0,rt=threshold(b,&visited);visit_total+=visited;
   hist[rt]++;
   if(rt>mx){mx=rt;max_count=0;max_reps.clear();}
   if(rt==mx){max_count++;if(max_reps.size()<60)max_reps.push_back(b);}
 }
 printf("mode=%s rank6=%lld inspected=%lld classes=%lld mass=%lld visits=%lld max=%d extrema=%d\n",canonical?"canonical":"labeled",rank6,inspected,representatives,orbitmass,visit_total,mx,max_count);
 for(auto [t,n]:hist)printf("%d %lld\n",t,n);
 puts("extrema:");for(auto a:max_reps){for(auto x:a)printf("%d",x);puts("");}
}
