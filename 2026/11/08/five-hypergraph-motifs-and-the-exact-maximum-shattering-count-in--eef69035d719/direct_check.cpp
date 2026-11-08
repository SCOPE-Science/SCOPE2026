#include <bits/stdc++.h>
using namespace std;
long long count_shattered(int n){
 vector<int> v;
 for(int a=0;a<n;a++) for(int b=a+1;b<n;b++) for(int c=b+1;c<n;c++)v.push_back((1<<a)|(1<<b)|(1<<c));
 int N=v.size();long long cnt=0;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++)for(int d=c+1;d<N;d++){
  int seen=0;
  for(int q:v){
   int mask=((__builtin_popcount((unsigned)(q&v[a]))==2)<<0)|((__builtin_popcount((unsigned)(q&v[b]))==2)<<1)|((__builtin_popcount((unsigned)(q&v[c]))==2)<<2)|((__builtin_popcount((unsigned)(q&v[d]))==2)<<3);
   seen |= (1<<mask);
   if(seen==65535){cnt++;break;}
  }
 }
 return cnt;
}
int main(){const long long expected[]={0,0,720,7035,28980,91980};
for(int n=4;n<=9;n++){
  auto start=chrono::steady_clock::now();auto r=count_shattered(n);
  if(r!=expected[n-4]){cerr<<"FAIL n="<<n<<" count="<<r<<endl; return 1;}
  auto stop=chrono::steady_clock::now();
  cout<<"DIRECT_JOHNSON_CHECK n="<<n<<" shattered_four="<<r<<" seconds="<<chrono::duration<double>(stop-start).count()<<endl;
}
cout<<"ALL_DIRECT_CHECKS_PASS"<<endl;
}
