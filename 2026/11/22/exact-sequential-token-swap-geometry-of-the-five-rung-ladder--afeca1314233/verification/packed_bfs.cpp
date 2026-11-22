#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
int main(int argc,char**argv){
 int c=atoi(argv[1]);if(c<2 || c>5)throw runtime_error("supported columns: 2..5");const int n=2*c;
 vector<pair<int,int>> E;
 for(int r=0;r<2;r++)for(int i=0;i<c-1;i++)E.push_back({r*c+i,r*c+i+1});
 for(int i=0;i<c;i++)E.push_back({i,i+c});
 U start=0;for(int i=0;i<n;i++)start|=U(i)<<(4*i);
 unordered_map<U,uint8_t> seen;unsigned long long f=1;for(int i=2;i<=n;i++)f*=i;
 seen.reserve(f*1.3);seen.max_load_factor(.8);
 vector<U> Q;Q.reserve(f);seen.emplace(start,0);Q.push_back(start);
 vector<unsigned long long> layers(50,0),gaps(50,0);unsigned long long count=0;
 int diameter=0,largestGap=-1;vector<U> far, gapset;
 for(size_t h=0;h<Q.size();h++){
  U s=Q[h];uint8_t d=seen.find(s)->second;layers[d]++;
  int D=0;
  for(int i=0;i<n;i++){
   int j=(s>>(4*i))&15;
   D+=abs((i%c)-(j%c)) + (i/c!=j/c);
  }
  if(D&1)throw runtime_error("parity mismatch");
  int gap=d-D/2;
  if(gap<0)throw runtime_error("lower bound contradiction");
  gaps[gap]++;
  if(d>diameter){diameter=d;far.clear();}
  if(d==diameter)far.push_back(s);
  if(gap>largestGap){largestGap=gap;gapset.clear();}
  if(gap==largestGap)gapset.push_back(s);
  for(auto [a,b]:E){int sa=4*a,sb=4*b; U x=((s>>sa)^(s>>sb))&15; U v=s^(x<<sa)^(x<<sb);if(seen.emplace(v,d+1).second)Q.push_back(v);}
 }
 auto repr=[&](U x){string s="[";for(int i=0;i<n;i++){if(i)s+=",";s+=to_string((x>>(4*i))&15);}return s+"]";};
 cout<<"cols "<<c<<" nstate "<<Q.size()<<" diameter "<<diameter<<" antipodes "<<far.size()<<"\ncounts";
 for(int i=0;i<=diameter;i++)cout<<" "<<layers[i];cout<<"\n";
 cout<<"furthest";for(auto a:far)cout<<" "<<repr(a);cout<<"\n";
 cout<<"maxgap "<<largestGap<<" count "<<gapset.size()<<" histogram";for(int i=0;i<=largestGap;i++)cout<<" "<<gaps[i];cout<<"\n";
 cout<<"gapstate";for(auto a:gapset)if(gapset.size()<20)cout<<" "<<repr(a);cout<<"\n";
 if(Q.size()!=f)throw runtime_error("not all permutations reached");
}
