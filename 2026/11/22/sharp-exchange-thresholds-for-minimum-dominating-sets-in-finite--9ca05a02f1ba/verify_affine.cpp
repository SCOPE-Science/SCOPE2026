// Exhaustive size-bounded domination checks for finite affine planes of orders 2, 3, and 4.
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
int addf(int a,int b,int q){return q==4?(a^b):(a+b)%q;}
int mulf(int a,int b,int q){
 if(q!=4)return a*b%q;
 int v=0;
 for(int k=0;k<2;k++)if((b>>k)&1)v^=a<<k;
 for(int k=3;k>=2;k--)if((v>>k)&1)v^=7<<(k-2);
 return v;
}
int main(){
 for(int q:{2,3,4}){
  int np=q*q,nl=q*(q+1),n=np+nl;
  vector<U> line;
  for(int slope=0;slope<q;slope++)for(int b=0;b<q;b++){
    U m=0;for(int x=0;x<q;x++){int y=addf(mulf(slope,x,q),b,q);m|=U(1)<<(x*q+y);}line.push_back(m);
  }
  for(int c=0;c<q;c++){U m=0;for(int y=0;y<q;y++)m|=U(1)<<(c*q+y);line.push_back(m);}
  vector<U> closed(n);for(int i=0;i<n;i++)closed[i]=U(1)<<i;
  for(int j=0;j<nl;j++)for(int i=0;i<np;i++)if((line[j]>>i)&1){closed[i]|=U(1)<<(np+j);closed[np+j]|=U(1)<<i;}
  U full=(U(1)<<n)-1;vector<U> optimal;
  for(int k=0;k<=2*q-1;k++){
   if(k==0)continue;
   U m=(U(1)<<k)-1,limit=U(1)<<n;long long count=0;
   while(m<limit){
    U covered=0,rest=m;while(rest){int i=__builtin_ctzll(rest);rest&=rest-1;covered|=closed[i];}
    if(covered==full){count++;if(k==2*q-1)optimal.push_back(m);}
    U t=m&-m,r=m+t;
    if(!r || r>=limit)break;
    m=(((r^m)>>2)/t)|r;
   }
   if(k<2*q-1 && count) {cerr<<"SMALL DOMINATION FOUND "<<q<<" "<<k<<"\n";return 1;}
   if(k==2*q-1 && count!=q*(q+1)){cerr<<"COUNT BAD "<<q<<" "<<count<<"\n";return 1;}
  }
  set<U> expected;
  for(int j=0;j<nl;j++){
   U m=line[j];for(int l=0;l<nl;l++)if(j!=l && !(line[j]&line[l]))m|=U(1)<<(np+l);
   expected.insert(m);
  }
  if(set<U>(optimal.begin(),optimal.end())!=expected){cerr<<"FAMILY BAD "<<q<<"\n";return 1;}
  long long par=0,nonpar=0;for(int i=0;i<nl;i++)for(int j=i+1;j<nl;j++){
    U s=U(1)<<0; (void)s;
    auto it=expected.find(line[i]); (void)it;
    int cost=0;
    U mi=line[i],mj=line[j];for(int l=0;l<nl;l++){
      if(i!=l && !(line[i]&line[l]))mi|=U(1)<<(np+l);
      if(j!=l && !(line[j]&line[l]))mj|=U(1)<<(np+l);
    }
    cost=__builtin_popcountll(mi^mj)/2;
    if(!(line[i]&line[j])){if(cost!=q+1)return 2;par++;}
    else {if(cost!=2*q-2)return 3;nonpar++;}
  }
  cout<<"q="<<q<<" verified all sets size <= "<<2*q-1<<", optima="<<optimal.size()<<", parallel pairs="<<par<<", intersecting pairs="<<nonpar<<"\n";
 }
}
