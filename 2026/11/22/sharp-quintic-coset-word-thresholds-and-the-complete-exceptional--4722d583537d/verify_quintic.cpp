#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <numeric>
#include <vector>
using namespace std;
static int modpow(int a,int e,int p){long long x=a,r=1;while(e){if(e&1)r=r*x%p;x=x*x%p;e>>=1;}return (int)r;}
static vector<bool> sieve(int lim){vector<bool> prime(lim+1,true);prime[0]=prime[1]=false;for(int k=2;k*k<=lim;k++)if(prime[k])for(int j=k*k;j<=lim;j+=k)prime[j]=false;return prime;}
int main(){const int B=31126;auto isprime=sieve(B);int total=0,bad=0,badmixed=0,lastbad=0,lastmixed=0;vector<int> exceptions,mixedexceptions;
for(int p=11;p<=B;p+=10){if(!isprime[p])continue;total++;
 int phi=p-1;vector<int> factors;int t=phi;for(int f=2;f*f<=t;f++)if(t%f==0){factors.push_back(f);while(t%f==0)t/=f;}if(t>1)factors.push_back(t);
 int g=2;for(;;g++){bool primitive=true;for(auto f:factors)if(modpow(g,phi/f,p)==1){primitive=false;break;}if(primitive)break;}
 vector<int> lab1(p,-1),lab2(p,-1);int val=1;for(int e=0;e<phi;e++){assert(lab1[val]==-1);lab1[val]=e%5;val=(long long)val*g%p;}assert(val==1);
 // Independent fifth-power coset construction, no discrete logarithms.
 vector<int> powers;vector<char> seen(p,0);for(int x=1;x<p;x++){int y=modpow(x,5,p);if(!seen[y]){powers.push_back(y);seen[y]=1;}}assert((int)powers.size()==phi/5);
 int gp=1;for(int c=0;c<5;c++){for(int y:powers){int z=(long long)gp*y%p;assert(lab2[z]==-1);lab2[z]=c;}gp=(long long)gp*g%p;}
 assert(lab1==lab2);
 array<int,125> counts1{},counts2{};for(int n=1;n<=p-3;n++){counts1[25*lab1[n]+5*lab1[n+1]+lab1[n+2]]++;counts2[25*lab2[n]+5*lab2[n+1]+lab2[n+2]]++;}assert(counts1==counts2);assert(accumulate(counts1.begin(),counts1.end(),0)==p-3);
 int missing=0,nonzero=0;for(int c=0;c<125;c++)if(!counts1[c]){missing++;nonzero+=(c!=0);}if(missing){bad++;lastbad=p;exceptions.push_back(p);}if(nonzero){badmixed++;lastmixed=p;mixedexceptions.push_back(p);}
 if(p==2311 || p==2411 || p==2731 || p==3331 || p==2341 || p==3361){printf("boundary p=%d missing=%d mixed_missing=%d missing_indices:",p,missing,nonzero);for(int c=0;c<125;c++)if(!counts1[c])printf(" %d",c);puts("");}
}
printf("tested=%d bad=%d badmixed=%d lastbad=%d lastmixed=%d\n",total,bad,badmixed,lastbad,lastmixed);
puts("exceptions:");for(int p:exceptions)printf("%d ",p);puts("");puts("mixed exceptions:");for(int p:mixedexceptions)printf("%d ",p);puts("");assert(total>800 && bad==48 && lastbad==3331 && lastmixed==2311);assert(31126-176*sqrt(31126)-75>0);puts("PASS: exhaustive finite tables, independent coset enumeration and Weil threshold.");}
