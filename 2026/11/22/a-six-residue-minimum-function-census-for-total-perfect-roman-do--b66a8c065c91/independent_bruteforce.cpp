// Independent exhaustive check on small cyclic prisms.
#include <array>
#include <iostream>
#include <vector>
using namespace std;
int main(){
 for(int n=3;n<=7;n++){
  int N=2*n;vector<int> f(N),best(N+1,0);int minimum=100000;unsigned long long ways=0;
  unsigned long long bound=1;for(int j=0;j<N;j++)bound*=3;
  for(unsigned long long code=0;code<bound;code++){
   auto q=code;int weight=0;for(int i=0;i<N;i++){f[i]=q%3;q/=3;weight+=f[i];}
   if(weight>minimum)continue;
   bool ok=true;
   for(int r=0;r<2&&ok;r++)for(int i=0;i<n&&ok;i++){
    int v=r*n+i, a=r*n+(i+n-1)%n, b=r*n+(i+1)%n,c=(1-r)*n+i;
    int two=(f[a]==2)+(f[b]==2)+(f[c]==2);
    if(f[v]==0){if(two!=1)ok=false;}
    else if(!((f[a]>0)||(f[b]>0)||(f[c]>0)))ok=false;
   }
   if(ok){if(weight<minimum){minimum=weight;ways=1;}else ways++;}
  }
  cout<<n<<" "<<minimum<<" "<<ways<<"\n";
 }
}
