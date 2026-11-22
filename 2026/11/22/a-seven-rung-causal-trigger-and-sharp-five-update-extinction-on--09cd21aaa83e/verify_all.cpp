// Exact finite local truth-table certificate for a three-state excitation rule.
// Compile: g++ -O3 -std=c++17 verify_all.cpp -o verify_all && ./verify_all
#include <cassert>
#include <cstdint>
#include <cstdio>
#include <vector>
#include <array>
using namespace std;

static int flip(int a) { return (a % 3) * 3 + a / 3; }
static bool motif(const int* x,int n,int col,int row){
    if(col<3 || col+3>=n) return false;
    const int choices[7][9]={{0,1,0,0,1,0,0,1,0},
      {0,0,0,1,0,0,0,0,0},
      {1,0,1,0,0,0,0,0,0},
      {0,0,0,1,1,1,0,0,0},
      {1,0,1,0,0,0,0,0,0},
      {0,0,0,1,0,0,0,0,0},
      {0,1,0,0,1,0,0,1,0}};
    for(int k=0;k<7;k++){
        int a=x[2*(col+k-3)]+3*x[2*(col+k-3)+1];
        if(row==1) a=flip(a);
        if(!choices[k][a])return false;
    }
    return true;
}
int main(){
 for(int n=1;n<=8;n++){
    const int N=2*n;long long S=1;for(int i=0;i<N;i++)S*=3;
    vector<int> nbr[20];
    for(int col=0;col<n;col++)for(int r=0;r<2;r++){
        int v=2*col+r;
        nbr[v].push_back(2*col+1-r);
        if(col>0)nbr[v].push_back(v-2);
        if(col+1<n)nbr[v].push_back(v+2);
    }
    int a[20],b[20],init[20];long long histogram[7]={0};
    for(long long state=0;state<S;state++){
      long long z=state;for(int v=0;v<N;v++){init[v]=z%3;z/=3;a[v]=init[v];}
      int tau=-1;
      for(int t=0;t<=5;t++){
        bool nonzero=false;
        for(int v=0;v<N;v++)nonzero |= a[v]!=0;
        if(!nonzero && tau<0)tau=t;
        if(t==3){
          bool expected=false,actual=false;
          for(int v=0;v<N;v++){
            const bool event=motif(init,n,v/2,v%2);
            expected|=event;actual|=a[v]==1;
            if(event!=(a[v]==1)){
              fprintf(stderr,"motif error n=%d state=%lld v=%d\n",n,state,v);return 1;
            }
          }
          (void)expected;(void)actual;
        }
        if(t==5) break;
        for(int v=0;v<N;v++){
          if(a[v]!=0)b[v]=(a[v]+1)%3;
          else{
            int e=0;for(int w:nbr[v])e+=(a[w]==1);
            b[v]=(e>=2)?1:0;
          }
        }
        for(int v=0;v<N;v++)a[v]=b[v];
      }
      if(tau<0){fprintf(stderr,"Not extinct by five n=%d state=%lld\n",n,state);return 1;}
      histogram[tau]++;
    }
    int expectedMax[]={0,2,3,3,4,4,4,5,5};
    int mx=0;for(int i=0;i<=5;i++)if(histogram[i])mx=i;
    if(mx!=expectedMax[n]){fprintf(stderr,"Unexpected maximum n=%d, mx=%d\n",n,mx);return 1;}
    if(n==7 && histogram[5]!=216)return 1;
    if(n==8 && histogram[5]!=3888)return 1;
    printf("n=%d states=%lld tau=",n,S);
    for(int i=0;i<=5;i++)printf("%s%lld",i?",":"",histogram[i]);
    puts("");
 }
 puts("EXHAUSTIVE_OK");return 0;
}
