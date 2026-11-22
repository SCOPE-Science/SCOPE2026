#include <bits/stdc++.h>
using namespace std;
int main(){for(int m=2;m<=4;m++)for(int n=m;n<=6;n++){int N=m*n;if(N>20)continue;vector<uint32_t> adj(N);for(int a=0;a<N;a++)for(int b=0;b<N;b++)if(a!=b&&(a/n==b/n||a%n==b%n))adj[a]|=1u<<b;int count=0;for(uint32_t S=0;S<(1u<<N);S++){vector<uint32_t> sig(N);bool ok=true;for(int i=0;i<N;i++)if(!(S>>i&1)){sig[i]=adj[i]&S;if(!sig[i]){ok=false;break;}}if(ok)for(int i=0;i<N&&ok;i++)if(!(S>>i&1))for(int j=i+1;j<N;j++)if(!(S>>j&1)&&sig[i]==sig[j]){ok=false;break;}
 vector<int> r(m),c(n);for(int i=0;i<N;i++)if(S>>i&1){r[i/n]++;c[i%n]++;}int iso=0,edges=0;for(int x:r)iso+=x==0;for(int x:c)iso+=x==0;for(int i=0;i<N;i++)if(S>>i&1 && r[i/n]==1&&c[i%n]==1)edges++;bool criterion=(iso<=1&&edges<=1);if(ok!=criterion){cerr<<"FAIL "<<m<<" "<<n<<" mask="<<S<<" iso="<<iso<<" ed="<<edges<<endl;return 1;}count+=ok;}
 cout<<m<<"x"<<n<<" "<<count<<endl;}cout<<"LD_OK\n";}
