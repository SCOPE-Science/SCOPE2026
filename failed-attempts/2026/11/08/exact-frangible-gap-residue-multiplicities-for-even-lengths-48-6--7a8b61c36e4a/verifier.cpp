#include <bits/stdc++.h>
using namespace std;
using i128=__int128_t;
string str(i128 n){if(n==0)return "0";bool neg=n<0;if(neg)n=-n;string s;while(n){s.push_back(char('0'+n%10));n/=10;}if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
bool prime(int x){if(x<2)return false;for(int i=2;i*i<=x;i++)if(x%i==0)return false;return true;}
i128 count_omega(int h){
 int m=h/2-1, l=m/2, r=m-l;
 vector<int> qs; for(int q=3;q<h;q+=2)if(prime(q))qs.push_back(q);
 struct QTable{int q;vector<uint64_t> L,R; uint64_t endpoints;};
 vector<QTable> ts;
 for(int q:qs){
  QTable t; t.q=q;
  t.endpoints=(1ULL<<0)|(1ULL<<((q-h%q)%q));
  t.L.resize(1<<l);t.R.resize(1<<r);
  for(int mask=1;mask<(1<<l);mask++){
   int bit=__builtin_ctz((unsigned)mask), prev=mask&(mask-1);
   t.L[mask]=t.L[prev] | (1ULL<<((q-(2*(bit+1))%q)%q));
  }
  for(int mask=1;mask<(1<<r);mask++){
   int bit=__builtin_ctz((unsigned)mask), prev=mask&(mask-1);
   t.R[mask]=t.R[prev] | (1ULL<<((q-(2*(l+bit+1))%q)%q));
  }
  ts.push_back(std::move(t));
 }
 i128 result=0;
 const uint64_t N=(1ULL<<m);
 for(uint64_t s=0;s<N;s++){
  int a=s&((1ULL<<l)-1),b=s>>l;
  i128 prod=1;
  for(const auto &q:ts){
   uint64_t residues=q.endpoints|q.L[a]|q.R[b];
   int good=q.q-__builtin_popcountll(residues);
   prod*=good;
   if(!good)break;
  }
  if(__builtin_parityll(s))result-=prod;else result+=prod;
 }
 return result;
}
int main(int argc,char**argv){int from=argc>1?atoi(argv[1]):4,to=argc>2?atoi(argv[2]):48;for(int h=from;h<=to;h+=2){auto st=chrono::steady_clock::now();auto c=count_omega(h);cout<<h<<" "<<str(c)<<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<endl;}}
