// Exact small finite-diagram orbit-signature check for symplectic spaces.
// All vector arithmetic is over the specified prime fields (q=2 or 3).
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <cassert>
using namespace std;
int mod(int x, int q){x%=q;return x<0?x+q:x;}
using Vec=vector<int>;
int B(const Vec &a,const Vec &b,int q){int n=a.size()/2, ans=0;for(int i=0;i<n;i++) ans+=a[2*i]*b[2*i+1]-a[2*i+1]*b[2*i];return mod(ans,q);}
Vec decode(int x,int q,int dim){Vec v(dim);for(int i=0;i<dim;i++){v[i]=x%q;x/=q;}return v;}
int power(int x,int e){int a=1;while(e--)a*=x;return a;}
Vec unit(int dim,int i){Vec v(dim);v[i]=1;return v;}
string kernel(const vector<Vec> &v,int q){int k=v.size(), dim=v[0].size();string ans;for(int c=0;c<power(q,k);c++) {auto z=decode(c,q,k);bool zero=true;for(int j=0;j<dim&&zero;j++){int x=0;for(int i=0;i<k;i++)x+=z[i]*v[i][j];if(mod(x,q)!=0)zero=false;}ans+=zero?'1':'0';}return ans;}
string signature(const vector<Vec>&base,const Vec &x,const Vec&y,int q){vector<Vec> b=base;b.push_back(x);b.push_back(y);string key=kernel(b,q);key+='|';for(auto &u:base){key+=char('A'+B(u,x,q));key+=char('A'+B(u,y,q));}return key;}
string unary(const vector<Vec>&base,const Vec &x,int q){vector<Vec>b=base;b.push_back(x);string key=kernel(b,q);key+='|';for(auto &u:base)key+=char('A'+B(u,x,q));return key;}
long long formula(int q,int d,int rho){long long Q=power(q,d);long long a=2*Q*Q;long long non=(Q-power(q,rho))*(Q-Q/q);long long one=(q+1)*(Q+(Q-1)*(Q/q));return a-non+one;}
void run(int q,int ambient_pairs,vector<int>base_indices,int rho){int dim=ambient_pairs*2, N=power(q,dim);vector<Vec>vs;vs.reserve(N);for(int i=0;i<N;i++)vs.push_back(decode(i,q,dim));vector<Vec> base;for(int j:base_indices)base.push_back(unit(dim,j));int d=base.size();set<string> one,two;for(const auto &x:vs){one.insert(unary(base,x,q));for(const auto &y:vs){if(B(x,y,q)==0)two.insert(signature(base,x,y,q));}}long long expectedOne=2*power(q,d);long long expectedTwo=d?formula(q,d,rho):q+3;cout<<"q="<<q<<" dim="<<dim<<" base_dim="<<d<<" rad="<<rho<<" unary="<<one.size()<<" orthogonal_pair="<<two.size()<<" expected="<<expectedOne<<","<<expectedTwo<<"\n"<<flush;assert(one.size()==expectedOne);assert(two.size()==expectedTwo);}
int main(){run(2,4,{},0);run(2,4,{0},1);run(2,4,{0,2},2);run(2,4,{0,1},0);run(2,4,{0,1,2},1);run(2,5,{0,2,4},3);run(3,3,{0},1);run(3,3,{0,1},0);cout<<"FINITE_SYMPLECTIC_SIGNATURES_PASS\n";}
