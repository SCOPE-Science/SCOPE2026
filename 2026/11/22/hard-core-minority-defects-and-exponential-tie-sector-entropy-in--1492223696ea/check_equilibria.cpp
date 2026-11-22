// Finite independent exhaustive cross-check for the theorem in RESULT.md.
// Compile: g++ -O3 -std=c++17 check_equilibria.cpp -o check_equilibria
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
using namespace std;
long long choose(int n,int k){if(k<0||n<k)return 0; long long x=1;for(int i=1;i<=k;i++)x=x*(n-k+i)/i;return x;}
long long predicted(int n,int r){if(r<1 || n<3*r+2 || ((n-r)&1))return 0; return (6LL*n*choose(n-2*r-1,r-1))/r;}
int main(){
 for(int n=5;n<=16;n++){
  long long bound=1;for(int i=0;i<n;i++)bound*=3;
  map<int,long long> obs;
  for(long long w=0;w<bound;w++){
   auto v=w; int x[20],ct[3]={0,0,0};
   for(int i=0;i<n;i++){x[i]=int(v%3);v/=3;ct[x[i]]++;}
   int L=max({ct[0],ct[1],ct[2]});
   int r=min({ct[0],ct[1],ct[2]});
   if(r<1 || r>=L) continue;
   int maxcount=(ct[0]==L)+(ct[1]==L)+(ct[2]==L);
   if(maxcount!=2)continue;
   int minor=-1;for(int c=0;c<3;c++)if(ct[c]==r)minor=c;
   bool actual=true;
   for(int i=0;i<n;i++){
    int ex[3]={0,0,0};ex[x[(i+n-1)%n]]++;ex[x[i]]++;ex[x[(i+1)%n]]++;
    int vote[3];for(int c=0;c<3;c++)vote[c]=ct[c]-ex[c];
    int high=max({vote[0],vote[1],vote[2]});
    int ties=(vote[0]==high)+(vote[1]==high)+(vote[2]==high);
    if(ties==1 && vote[x[i]]!=high){actual=false;break;}
   }
   bool structure=true;
   for(int i=0;i<n;i++){
    if(x[i]==minor){
     if(x[(i+n-1)%n]==minor || x[(i+1)%n]==minor || x[(i+n-2)%n]==minor || x[(i+2)%n]==minor)structure=false;
    }
    if(x[i]!=minor){
     int j=(i+1)%n;while(x[j]==minor)j=(j+1)%n;
     if(x[j]==x[i]) structure=false;
    }
   }
   if(actual!=structure){cerr<<"MISMATCH n="<<n<<" word="<<w<<" actual="<<actual<<" structure="<<structure<<"\n";return 1;}
   if(actual)obs[r]++;
  }
  long long sum=0;
  for(int r=1;r<=n;r++){
   auto exp=predicted(n,r);
   if(obs[r]!=exp){cerr<<"COUNT MISMATCH n="<<n<<" r="<<r<<" got="<<obs[r]<<" expected="<<exp<<"\n";return 2;}
   sum+=exp;
  }
  cout<<"n="<<n<<" tie-leader fixed states="<<sum<<" verified=true\n";
 }
 cout<<"EXHAUSTIVE PASS, all three-color configurations on n=5..16 considered within the stated histogram sector\n";
}
