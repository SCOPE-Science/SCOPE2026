// Reproducible exhaustive finite checks for a theorem on threshold-two excitable wheels.
#include <cstdint>
#include <cstdio>
#include <vector>
#include <cassert>
using namespace std;
static int residue(uint64_t z,int q,int i){while(i--)z/=q;return int(z%q);}
static int countP(const vector<int>& s,int q){int n=(int)s.size(),ans=0;for(int i=0;i<n;i++)if(s[(i+n-2)%n]==1 && s[(i+n-1)%n]==0 && (s[i]==0||s[i]==q-1) && s[(i+1)%n]==0 && s[(i+2)%n]==1)ans++;return ans;}
static int countR(const vector<int>& s){int n=(int)s.size(),ans=0;for(int i=0;i<n;i++)ans+=(s[(i+n-1)%n]==1&&s[i]==0&&s[(i+1)%n]==1);return ans;}
int main(){
 for(int q=4;q<=7;q++)for(int n=3;n<=8;n++){
  int N=n+1;uint64_t total=1;for(int i=0;i<N;i++)total*=q;if(total>2500000)break;
  uint64_t count_terminal=0,countP_channel=0,countR_channel=0;int max_time=0;
  for(uint64_t z=0;z<total;z++){
   vector<int>a(N),b(N),rim(n);
   uint64_t x=z;for(int i=0;i<N;i++){a[i]=int(x%q);x/=q;}
   for(int i=0;i<n;i++)rim[i]=a[i+1];
   int p=countP(rim,q),r=countR(rim),observed_time=-1;bool at_time_two=false;
   for(int t=0;t<=q+2;t++){
    bool active=false;for(int c:a)if(c!=0)active=true;
    if(!active){observed_time=t;break;}
    if(t==2){for(int c:a)if(c==1)at_time_two=true;}
    if(t==3){for(int c:a)if(c==1){fprintf(stderr,"EXCITED AT TIME THREE q=%d n=%d z=%llu\n",q,n,(unsigned long long)z);return 1;}}
    int rim_ex=0;for(int i=1;i<N;i++)rim_ex+=(a[i]==1);
    b[0]=a[0]?((a[0]+1)%q):(rim_ex>=2);
    for(int i=1;i<N;i++){
     int l=(i==1?n:i-1),rr=(i==n?1:i+1);
     int ex=(a[0]==1)+(a[l]==1)+(a[rr]==1);
     b[i]=a[i]?((a[i]+1)%q):(ex>=2);
    }
    a.swap(b);
   }
   if(observed_time<0||observed_time>q+1){fprintf(stderr,"EXTINCTION FAILURE q=%d n=%d z=%llu\n",q,n,(unsigned long long)z);return 2;}
   if(observed_time>max_time)max_time=observed_time;
   bool predicted=(residue(z,q,0)==1 && p>=1)||(residue(z,q,0)==q-1 && r>=2);
   if(predicted!=at_time_two){fprintf(stderr,"MOTIF FAILURE q=%d n=%d z=%llu P=%d R=%d\n",q,n,(unsigned long long)z,p,r);return 3;}
   if((observed_time==q+1)!=predicted){fprintf(stderr,"CLOCK FAILURE q=%d n=%d z=%llu\n",q,n,(unsigned long long)z);return 4;}
   if(predicted){count_terminal++;if(residue(z,q,0)==1)countP_channel++;else countR_channel++;}
  }
  printf("q=%d n=%d states=%llu sharp=%d terminal=%llu P=%llu R=%llu CHECK_OK\n",q,n,(unsigned long long)total,max_time,(unsigned long long)count_terminal,(unsigned long long)countP_channel,(unsigned long long)countR_channel);fflush(stdout);
 }
}
