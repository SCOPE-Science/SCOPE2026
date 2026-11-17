// Independent base-q integer-state simulation and directed-ancestor terminal criterion.
#include <iostream>
#include <vector>
#include <array>
#include <cstdint>
#include <cassert>
using namespace std;
using u64=unsigned long long;
u64 power(int q,int n){u64 v=1;while(n--)v*=q;return v;}
u64 formula(int q,int a,int b){
 auto L=[&](int n){return power(q,n)-power(q-1,n);};
 auto R=[&](int n){return power(q-1,n)-power(q-4,n)+power(q,n)-power(q-3,n);};
 return L(a)*R(b)+L(b)*R(a);
}
int main(){
 const vector<array<int,3>> tests={{4,2,3},{4,3,3},{4,3,4},
    {5,2,2},{5,2,3},{6,2,2},{7,1,2},{8,1,1}};
 for(auto p:tests){
  int q=p[0],a=p[1],b=p[2],n=a+b+2;
  vector<vector<int>> nb(n);
  auto edge=[&](int i,int j){nb[i].push_back(j);nb[j].push_back(i);};
  edge(0,1);
  for(int i=0;i<a;i++)edge(0,2+i);
  for(int i=0;i<b;i++)edge(1,2+a+i);
  u64 cnt=0, predicted=0;
  int maximum=0;
  vector<int> s(n),z(n);
  for(u64 mask=0;mask<power(q,n);mask++){
   u64 k=mask;
   for(int i=0;i<n;i++){s[i]=k%q;k/=q;}
   // Exact wave condition checked independently of trajectory.
   bool A=false,B=false;
   if(s[0]==0 && (s[1]==0 || s[1]==q-1)){
      bool has1=false,noB1=true,hasS=false;
      for(int i=0;i<a;i++)has1|=(s[2+i]==1);
      for(int i=0;i<b;i++){
        int c=s[2+a+i];noB1&=(c!=1);
        hasS|=(c==0||c==q-1||c==q-2);
      }
      A=has1 && hasS && (s[1]==q-1 || noB1);
   }
   if(s[1]==0 && (s[0]==0 || s[0]==q-1)){
      bool has1=false,noA1=true,hasS=false;
      for(int i=0;i<b;i++)has1|=(s[2+a+i]==1);
      for(int i=0;i<a;i++){
        int c=s[2+i];noA1&=(c!=1);
        hasS|=(c==0||c==q-1||c==q-2);
      }
      B=has1 && hasS && (s[0]==q-1 || noA1);
   }
   assert(!(A&&B));
   predicted+=(A||B);
   int t=0;
   for(;;){
      bool nonzero=false;for(int x:s)nonzero|=(x!=0);
      if(!nonzero)break;
      for(int i=0;i<n;i++){
        if(s[i])z[i]=(s[i]+1)%q;
        else{
          z[i]=0;
          for(int j:nb[i])if(s[j]==1){z[i]=1;break;}
        }
      }
      s.swap(z);t++;
      assert(t<=q+2);
   }
   maximum=max(maximum,t);
   cnt+=(t==q+2);
   assert((t==q+2)==(A||B));
  }
  assert(maximum==q+2 && cnt==formula(q,a,b) && predicted==cnt);
  cout<<"q="<<q<<" a="<<a<<" b="<<b<<" states="<<power(q,n)
      <<" max="<<maximum<<" terminal="<<cnt<<" criterion="<<predicted<<"\n";
 }
 cout<<"PASS independent integer simulations and event tests\n";
}
