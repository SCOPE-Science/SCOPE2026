// Exhaustive subset checker using literal open-neighborhood intersections.
// No transfer matrix or cyclic-word constraints are used here.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
struct Counts {int mx; U amount, all;};
Counts check(int n,int m){
  int N=n*m;
  assert(N<=24);
  vector<U> neigh(N);
  for(int i=0;i<n;i++)for(int c=0;c<m;c++){
    int v=i*m+c;
    for(int d=0;d<m;d++)if(d!=c) neigh[v] |= U(1)<<(i*m+d);
    neigh[v] |= U(1)<<(((i+1)%n)*m+c);
    neigh[v] |= U(1)<<(((i+n-1)%n)*m+c);
  }
  vector<U> conflict(N);
  for(int v=0;v<N;v++)for(int w=0;w<N;w++)if(w!=v && (neigh[v]&neigh[w])) conflict[v]|=U(1)<<w;
  int mx=-1;U amount=0,all=0;
  for(U s=0;s<(U(1)<<N);s++){
    bool good=true; U t=s;
    while(t){int v=__builtin_ctzll(t);t&=t-1;
      if(conflict[v]&t){good=false;break;}
    }
    if(!good)continue;
    all++;
    int weight=__builtin_popcountll(s);
    if(weight>mx){mx=weight;amount=1;}
    else if(weight==mx)amount++;
  }
  return {mx,amount,all};
}
U ipow(U a,int e){U y=1;while(e--){y*=a;}return y;}
pair<int,U> formula(int n,int m){
  U a=m-1;int k=n/3,r=n%3;
  long long z=0;
  if(r==0)z=3*((long long)ipow(a,k)+((k&1)?-(long long)a:(long long)a));
  if(r==1)z=(long long)n*(ipow(a,k)+ipow(a,k-1)+((long long)k*ipow(a,k+1)+((k&1)?k*(long long)a:-k*(long long)a))/2);
  if(r==2)z=(long long)n*a*(ipow(a,k)-((k&1)?-1:1));
  return {2*k+(r==2), (U)z};
}
int main(){
  vector<pair<int,int>> cases={{5,3},{6,3},{7,3},{8,3},{5,4},{6,4}};
  for(auto [n,m]:cases){
    Counts c=check(n,m);auto e=formula(n,m);
    cout<<"n="<<n<<" m="<<m<<" max="<<c.mx<<" count="<<c.amount<<" total="<<c.all<<'\n';
    if(c.mx!=e.first || c.amount!=e.second) return 1;
  }
  cout<<"DIRECT_VERIFIED\n";
}
