// Exact cyclotomic verification of third-order Fourier restrictions over two distinct primes.
// Standard C++17, no external libraries. This independently checks the geometric predictions.
#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <array>
using namespace std;
using Triple = array<int,3>;

vector<int> divide_monic(vector<int> a, vector<int> b) {
  int da=(int)a.size()-1, db=(int)b.size()-1;
  assert(b[db]==1 && da>=db);
  vector<int> q(da-db+1);
  for(int k=da-db;k>=0;--k){int c=a[db+k];q[k]=c;for(int j=0;j<=db;j++)a[k+j]-=c*b[j];}
  for(int v:a)assert(v==0);
  return q;
}

void run(int p,int q){
  int N=p*q, degree=(p-1)*(q-1);
  vector<int> num(N+2),den(p+q+1);
  num[N+1]=1;num[N]=-1;num[1]=-1;num[0]=1;
  den[p+q]=1; den[p]--;den[q]--;den[0]++;
  vector<int> phi=divide_monic(num,den);
  assert((int)phi.size()==degree+1);
  vector<vector<int>> v(N,vector<int>(degree));
  for(int i=0;i<degree;i++)v[i][i]=1;
  for(int e=degree;e<N;e++){
    for(int k=0;k<degree;k++) if(phi[k])
      for(int i=0;i<degree;i++)v[e][i]-=phi[k]*v[e-degree+k][i];
  }
  vector<Triple> triples;
  for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++)triples.push_back({a,b,c});
  const long long T=triples.size();
  auto choose3=[](long long n){return n*(n-1)*(n-2)/6;};
  const long long X=p*choose3(q), Y=q*choose3(p);
  const long long A=T-choose3(p)*(long long)q*q*q, B=T-choose3(q)*(long long)p*p*p;
  long long predicted1=2*X*Y, predicted2=2*(X*B+Y*A-2*X*Y);
  long long cnt[3]={};
  for(const auto &r:triples) {
    int a=r[1]-r[0],b=r[2]-r[0];
    int rp=(r[0]%p==r[1]%p || r[0]%p==r[2]%p ||r[1]%p==r[2]%p);
    int rq=(r[0]%q==r[1]%q || r[0]%q==r[2]%q ||r[1]%q==r[2]%q);
    int r_x=(r[0]%p==r[1]%p&&r[1]%p==r[2]%p);
    int r_y=(r[0]%q==r[1]%q&&r[1]%q==r[2]%q);
    for(const auto &c:triples) {
      int s=c[1]-c[0],t=c[2]-c[0];
      int A0=a*s%N,B0=a*t%N,C0=b*s%N,D0=b*t%N;
      int ex[6]={ (A0+D0)%N, B0,C0,(B0+C0)%N,A0,D0};
      vector<int> sum(degree);
      for(int k=0;k<6;k++)for(int j=0;j<degree;j++)sum[j]+=(k<3?1:-1)*v[ex[k]][j];
      int exact_rank=(all_of(sum.begin(),sum.end(),[](int z){return z==0;}))?(A0==0&&B0==0&&C0==0&&D0==0?1:2):3;
      int cp=(c[0]%p==c[1]%p || c[0]%p==c[2]%p ||c[1]%p==c[2]%p);
      int cq=(c[0]%q==c[1]%q || c[0]%q==c[2]%q ||c[1]%q==c[2]%q);
      int c_x=(c[0]%p==c[1]%p&&c[1]%p==c[2]%p);
      int c_y=(c[0]%q==c[1]%q&&c[1]%q==c[2]%q);
      int rank1=(r_x&&c_y)||(r_y&&c_x);
      int singular=(rp&&c_y)||(rq&&c_x)||(cp&&r_y)||(cq&&r_x);
      int geometry=rank1?1:(singular?2:3);
      if(exact_rank!=geometry){cerr<<"ERROR p="<<p<<" q="<<q<<"\n";exit(1);}
      cnt[exact_rank-1]++;
    }
  }
  assert(cnt[0]==predicted1 && cnt[1]==predicted2 && cnt[2]==T*T-predicted1-predicted2);
  cout<<"EXACT_PASS p="<<p<<" q="<<q<<" triples="<<T<<" rank1="<<cnt[0]<<" rank2="<<cnt[1]<<" rank3="<<cnt[2]<<" cyclotomic=true geometry=true"<<endl;
}
int main(){run(2,5);run(3,5);run(3,7);cout<<"ODD_SEMIPRIME_3X3_EXACT_TESTS_PASS"<<endl;}
