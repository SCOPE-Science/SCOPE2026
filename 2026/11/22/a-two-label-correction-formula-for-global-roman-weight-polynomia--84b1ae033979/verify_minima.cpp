#include <bits/stdc++.h>
using namespace std;
int main(){for(int n=3;n<=12;n++){long long lim=1;for(int i=0;i<n;i++)lim*=3;long long best=1e9,ways=0;map<int,long long> poly;vector<int>ex;
 for(int hub=1;hub<=2;hub++)for(long long m=0;m<lim;m++){long long x=m;int a[20],w=hub;for(int i=0;i<n;i++){a[i]=x%3; x/=3;w+=a[i];} bool ok=1; for(int i=0;i<n&&ok;i++)if(a[i]==0){bool ng=hub==2 || a[(i+1)%n]==2 || a[(i+n-1)%n]==2;bool nc=0;for(int j=0;j<n;j++)if(j!=i&&j!=(i+1)%n&&j!=(i+n-1)%n&&a[j]==2)nc=1; if(!ng||!nc)ok=0;} if(ok){poly[w]++;if(w<best){best=w;ways=1;ex=vector<int>(a,a+n);}else if(w==best)ways++;} }
 cout<<n<<" best "<<best<<" ways "<<ways<<" example ";for(auto i:ex)cout<<i;cout<<"\n";}
}
