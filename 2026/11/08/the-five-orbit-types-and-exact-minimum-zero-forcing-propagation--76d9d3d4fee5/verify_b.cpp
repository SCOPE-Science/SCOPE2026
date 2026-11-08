// Independent bitmask engine and local-time-table validator for the cubic circulant C_(2n)(1,n).
#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
int time_to_force(int n,U mask){
  int N=2*n,round=0;
  U full=(U(1)<<N)-1;
  while(mask!=full){
    U next=0;
    for(int v=0;v<N;v++) if(mask&(U(1)<<v)){
      int ng[3]={(v+N-1)%N,(v+1)%N,(v+n)%N};
      int count=0,only=-1;
      for(int w:ng) if(!(mask&(U(1)<<w))){count++;only=w;}
      if(count==1)next|=U(1)<<only;
    }
    if(!next)return -1;
    mask|=next;round++;
    if(round>N)abort();
  }
  return round;
}
int candidate_time(int n,char kind,int v){
  int i=v%n; bool y=v>=n;
  switch(kind){
    case 'A': if(!y) return i<=3?0:min(i-1,n+2-i);
              return i==1||i==2?1:(i==0||i==3?2:min(i-1,n+2-i));
    case 'B': if(!y) return i<=2?0:min(i,n+1-i);
              return i==0?0:(i==n-1?1:min(i,n+1-i));
    case 'C': if(!y) return (i==0||i==1||i==3)?0:(i==2?1:min(i,n+3-i));
              return i==0?3:(i==1?0:(i==2?2:(i==3?3:min(i,n+3-i))));
    case 'D': if(!y) return (i==0||i==1||i==n-1)?0:min(i,n-i);
              return i==0?0:min(i,n-i);
    case 'E': return i<=1?0:min(i-1,n-i);
  }
  abort();
}
void check_local_formula(int n,char kind){
  // A table satisfying the exact synchronous forcing equation is an algebraic witness.
  int N=2*n;vector<int> tau(N);
  for(int v=0;v<N;v++)tau[v]=candidate_time(n,kind,v);
  int zero=count(tau.begin(),tau.end(),0);
  if(zero!=4)abort();
  for(int v=0;v<N;v++)if(tau[v]>0){
    int best=INT_MAX;
    int ng[3]={(v+N-1)%N,(v+1)%N,(v+n)%N};
    for(int u:ng){
      int maximum=tau[u];
      int un[3]={(u+N-1)%N,(u+1)%N,(u+n)%N};
      for(int w:un) if(w!=v)maximum=max(maximum,tau[w]);
      best=min(best,maximum+1);
    }
    if(best!=tau[v]){cerr<<"local recurrence mismatch: "<<n<<" "<<kind<<" "<<v<<endl;abort();}
  }
  int got=*max_element(tau.begin(),tau.end());
  int want= kind=='C'?((n+3)/2):(kind=='E'?((n-1)/2):(kind=='D'?(n/2):((n+1)/2)));
  if(got!=want)abort();
}
int main(){
  for(int n=4;n<=23;n++){
    int N=2*n; map<int,long long> profile;
    for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)
    for(int c=b+1;c<N;c++)for(int d=c+1;d<N;d++){
      U m=(U(1)<<a)|(U(1)<<b)|(U(1)<<c)|(U(1)<<d);
      int t=time_to_force(n,m);
      if(t>=0)profile[t]++;
    }
    map<int,long long> want;
    if(n%2){int h=(n-1)/2;want[h]=3*n;want[h+1]=6*n;want[h+2]=4*n;}
    else{int h=n/2;want[h-1]=n;want[h]=8*n;want[h+1]=4*n;}
    if(profile!=want){cerr<<"spectrum mismatch n="<<n<<endl;abort();}
  }
  for(int n=4;n<=3000;n++)for(char k: string("ABCDE"))check_local_formula(n,k);
  cout<<"CPP_ENUM_AND_LOCAL_PASS"<<endl;
}
