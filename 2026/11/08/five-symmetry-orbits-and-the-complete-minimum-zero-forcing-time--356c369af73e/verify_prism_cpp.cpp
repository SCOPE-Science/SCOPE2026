// Exhaustive bit-mask and arrival-time checks for cyclic-prism zero forcing.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
#include <cstdint>
using namespace std;
using U = uint64_t;
struct G{
 int n,N; vector<U> nb;
 explicit G(int n):n(n),N(2*n),nb(2*n,0){
  for(int i=0;i<n;i++) for(int s=0;s<2;s++){
    int a=s*n+i;
    nb[a] |= U(1)<<(s*n+(i+1)%n);
    nb[a] |= U(1)<<(s*n+(i+n-1)%n);
    nb[a] |= U(1)<<((1-s)*n+i);
  }
 }
 int sim(U blue) const {
  U full=(U(1)<<N)-1;int step=0;
  while(blue!=full){
    U next=0;
    U avail=blue;
    while(avail){int v=__builtin_ctzll(avail);avail&=avail-1;
       U white=nb[v]&~blue;
       if(white && (white&(white-1))==0)next|=white;
    }
    if(!next)return -1;
    blue|=next;++step;
  } return step;
 }
 vector<int> moments(U start) const {
    vector<int> a(N,-1);U blue=start;
    for(int i=0;i<N;i++)if(blue>>i&1)a[i]=0;
    int step=0;
    while(true){U next=0;
      for(int v=0;v<N;v++)if(blue>>v&1){U white=nb[v]&~blue;
         if(white && !(white&(white-1)))next|=white;
      }
      if(!next)break;
      ++step;
      for(int i=0;i<N;i++)if(next>>i&1) a[i]=step;
      blue|=next;
    }
    return a;
 }
};
static vector<array<int,4>> forms(int n){return {{{0,1,n,n+1}},{{0,1,2,3}},{{0,1,2,n}},{{0,1,n,2*n-1}},{{0,1,3,n+1}}};}
static vector<int> formula(int n,int c){
 vector<int> T(n,0),B(n,0);
 if(c==0){for(int i=2;i<n;i++)T[i]=B[i]=min(i-1,n-i);}
 if(c==1){for(int i=4;i<n;i++)T[i]=B[i]=min(i-1,n+2-i);B[0]=2;B[1]=1;B[2]=1;B[3]=2;}
 if(c==2){for(int i=3;i<n-1;i++)T[i]=min(i,n+1-i);T[n-1]=1;
            for(int i=1;i<n;i++)B[i]=min(i,n+1-i);}
 if(c==3){for(int i=2;i<n;i++)T[i]=min(i,n-i);
            for(int i=1;i<n-1;i++)B[i]=min(i,n-i);}
 if(c==4){T[2]=1;for(int i=4;i<n;i++)T[i]=B[i]=min(i,n+3-i);
            B[0]=3;B[2]=2;B[3]=3;}
 T.insert(T.end(),B.begin(),B.end()); return T;
}
int main(){
  for(int n=5;n<=25;n++){
    G g(n);map<int,int> hist;
    for(int a=0;a<2*n;a++)for(int b=a+1;b<2*n;b++)for(int c=b+1;c<2*n;c++)for(int d=c+1;d<2*n;d++){
      int t=g.sim((U(1)<<a)|(U(1)<<b)|(U(1)<<c)|(U(1)<<d));
      if(t>=0)hist[t]++;
    }
    int m=n/2;
    map<int,int> target;
    if(n%2==0)target={{m-1,n},{m,8*n},{m+1,4*n}};
    else target={{m,3*n},{m+1,6*n},{m+2,4*n}};
    assert(hist==target);
    cout<<"n="<<n<<" accepted="<<13*n<<"\n";
  }
  for(int n=5;n<=300;n++){
    for(int c=0;c<5;c++){
      U x=0; // for n>31, bit masks cannot encode the full state: use indexed propagation below.
      if(n<=30){G g(n);auto F=forms(n);for(int j:F[c]) x|=U(1)<<j;assert(g.moments(x)==formula(n,c));}
      else {
        vector<vector<int>> N(2*n);
        for(int i=0;i<2*n;i++){int s=i/n,k=i%n;
          N[i]={s*n+(k+1)%n,s*n+(k+n-1)%n,(1-s)*n+k};}
        vector<int> mark(2*n,-1);
        auto F=forms(n);for(int v:F[c])mark[v]=0;
        int step=0;
        while(true){vector<int> changed;
          for(int v=0;v<2*n;v++)if(mark[v]>=0){int cnt=0,u=-1;
            for(int w:N[v])if(mark[w]<0){++cnt;u=w;}
            if(cnt==1)changed.push_back(u);
          }
          if(changed.empty())break;
          ++step;for(int v:changed)mark[v]=step;
        }
        assert(mark==formula(n,c));
      }
    }
  }
  cout<<"CPP_EXHAUSTIVE_AND_ARRIVAL_PASS\n";
}
