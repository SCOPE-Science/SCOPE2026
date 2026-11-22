#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;
struct Plane {
 int q,N;vector<array<int,3>> vec;vector<ull> nb;
 int add(int a,int b){return q==4?(a^b):(a+b)%q;}
 int mul(int a,int b){if(q!=4)return (a*b)%q;int z=0;while(b){if(b&1)z^=a;b>>=1;a<<=1;if(a&4)a^=7;}return z;}
 Plane(int Q):q(Q){set<array<int,3>> s;for(int x=0;x<q;x++)for(int y=0;y<q;y++)for(int z=0;z<q;z++){if(!(x|y|z))continue;array<int,3>a={x,y,z};int i=0;while(!a[i])i++;int inv=1;while(mul(a[i],inv)!=1)inv++;for(int& t:a)t=mul(t,inv);s.insert(a);}vec=vector<array<int,3>>(s.begin(),s.end());N=vec.size();nb.assign(2*N,0);for(int i=0;i<N;i++)for(int j=0;j<N;j++){int d=0;for(int k=0;k<3;k++)d=add(d,mul(vec[i][k],vec[j][k]));if(!d){nb[i]|=1ull<<(N+j);nb[N+j]|=1ull<<i;}}}
 int rounds(ull seed){ull full=(1ull<<(2*N))-1;ull b=seed;for(int v=0;v<2*N;v++)if(seed>>v&1)b|=nb[v];int r=1;while(b!=full){ull addmask=0;for(auto adj:nb){ull free=adj&~b;if(free && !(free&(free-1)))addmask|=free;}if(!addmask)return 0;b|=addmask;r++;}return r;}
};
int main(int argc,char**argv){int q=argc>1?atoi(argv[1]):4;int K=argc>2?atoi(argv[2]):6;Plane P(q);cerr<<"q "<<q<<" N "<<P.N<<" vtx "<<P.nb.size()<<"\n";array<array<unsigned long long,32>,50> count={};unsigned long long trials=0;vector<int> witness;int maxr=0;int n=P.nb.size();auto start=chrono::steady_clock::now();auto rec=[&](auto &&self,int begin,int needed,ull mask,int np)->void{if(!needed){trials++;int r=P.rounds(mask);if(r){count[np][r]++;maxr=max(maxr,r);if(witness.empty()){for(int i=0;i<n;i++)if(mask>>i&1)witness.push_back(i);}}return;}for(int v=begin;v<=n-needed;v++)self(self,v+1,needed-1,mask|(1ull<<v),np+(v<P.N));};for(int k=1;k<=K;k++){count={};trials=0;witness.clear();maxr=0;rec(rec,0,k,0,0);unsigned long long success=0;cout<<"q "<<q<<" k "<<k<<" trials "<<trials<<"\n";for(int a=0;a<=k;a++)for(int r=1;r<=maxr;r++){auto c=count[a][r];if(c){cout<<"profile "<<a<<" "<<r<<" "<<c<<"\n";success+=c;}}cout<<"success "<<success<<" witness ";for(auto x:witness)cout<<x<<",";cout<<"\n"<<flush;if(success)break;}cerr<<"seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";}
