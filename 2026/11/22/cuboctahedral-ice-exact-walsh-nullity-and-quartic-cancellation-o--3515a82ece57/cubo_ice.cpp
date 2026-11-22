#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<pair<int,int>> cube;for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)if(__builtin_popcount((unsigned)(i^j))==1)cube.emplace_back(i,j);
 vector<pair<int,int>> ed;for(int i=0;i<12;i++)for(int j=i+1;j<12;j++) if(cube[i].first==cube[j].first||cube[i].first==cube[j].second||cube[i].second==cube[j].first||cube[i].second==cube[j].second)ed.emplace_back(i,j);
 int m=ed.size();cerr<<"edges "<<m<<endl;
 if(m!=24)return 1;
 const int N=1<<24;
 vector<int> f(N,0); int cnt=0;long long enumerate=0;
 // DFS orient each edge with all outgoing bits; edge k=1 means first vertex outgoing
 vector<int> remaining(12,0),out(12,0);
 for(auto [a,b]:ed)remaining[a]++,remaining[b]++;
 auto rec=[&](auto&&self,int k,int mask)->void{
 if(k==m){cnt++;f[mask]=1;return;}
 auto [a,b]=ed[k];remaining[a]--;remaining[b]--;
 out[a]++;
 if(out[a]<=2&&out[a]+remaining[a]>=2&&out[b]<=2&&out[b]+remaining[b]>=2)self(self,k+1,mask | (1<<k));
 out[a]--;out[b]++;
 if(out[a]<=2&&out[a]+remaining[a]>=2&&out[b]<=2&&out[b]+remaining[b]>=2)self(self,k+1,mask);
 out[b]--;remaining[a]++;remaining[b]++;
 };
 rec(rec,0,0);
 cerr<<"orientations "<<cnt<<endl;
 map<int,int> initial={{cnt,1}};
 for(int i=0;i<m;i++){
  int jump=1<<i;
  for(int j=0;j<N;j+=2*jump) for(int x=j;x<j+jump;x++){
    int u=f[x],v=f[x+jump];f[x]=u+v;f[x+jump]=u-v;
  }
 }
 map<int,long long> hist;long long zeros=0;int minAbs=INT_MAX,minEvenZero=100,minOddNonZero=100;long long zeroEven=0,zeroOdd=0;
 vector<long long> zerosByWeight(25,0);
 long long l1proj=0;
 vector<unsigned char> islive(N);
 for(int i=0;i<N;i++){
  int v=f[i];hist[v]++;if(v)minAbs=min(minAbs,abs(v));else {zerosByWeight[__builtin_popcount((unsigned)i)]++;if(__builtin_popcount((unsigned)i)%2)zeroOdd++;else{zeroEven++;minEvenZero=min(minEvenZero,__builtin_popcount((unsigned)i));}}
  islive[i]=(v!=0);
 }
 cerr<<"zeros "<<zeroEven+zeroOdd<<" even "<<zeroEven<<" odd "<<zeroOdd<<" minabs "<<minAbs<<" minEvenZero "<<minEvenZero<<endl;
 cout<<"orientation_count="<<cnt<<"\nzero_even="<<zeroEven<<"\nzero_odd="<<zeroOdd<<"\nminimum_nonzero="<<minAbs<<"\nmin_even_zero_weight="<<minEvenZero<<"\n";
 for(auto [v,c]:hist)cout<<"spectral "<<v<<" "<<c<<"\n";
 for(int i=0;i<25;i++)if(zerosByWeight[i])cout<<"zeros_weight "<<i<<" "<<zerosByWeight[i]<<"\n";
 for(int i=0;i<N;i++)f[i]=islive[i];
 for(int i=0;i<m;i++){
  int jump=1<<i;
  for(int j=0;j<N;j+=2*jump) for(int x=j;x<j+jump;x++){
    int u=f[x],v=f[x+jump]; f[x]=u+v;f[x+jump]=u-v;
  }
 }
 long long sum=0;for(int x:f)sum+=abs(x);long long denom=N;long long g=std::gcd(sum,denom);cout<<"projection_norm="<<(sum/g)<<"/"<<(denom/g)<<"\n";
 cerr<<"l1sum "<<sum<<endl;
}
