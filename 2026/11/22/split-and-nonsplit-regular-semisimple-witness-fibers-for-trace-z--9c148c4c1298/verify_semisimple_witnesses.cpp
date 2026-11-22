// Direct finite-ring multiplication checks for sl2 bracket fibers.
// Compile: c++ -O3 -std=c++17 verify_chain_sl2.cpp -o verify_chain_sl2
// Run: ./verify_chain_sl2
#include <iostream>
#include <vector>
#include <array>
#include <stdexcept>
#include <cstdint>
#include <string>
using ll=long long;
struct Ring {
  int q,k,N; bool polynomial;
  std::vector<int> sum, product, val, negval;
  Ring(int q_,int k_,bool poly):q(q_),k(k_),N(1),polynomial(poly){
    for(int i=0;i<k;i++)N*=q;
    sum.resize(N*N); product.resize(N*N);val.resize(N);negval.resize(N);
    for(int a=0;a<N;a++){
      { int res=0,t=a,pw=1;for(int i=0;i<k;i++){res+=((q-(t%q))%q)*pw;t/=q;pw*=q;}negval[a]=polynomial?res:(N-a)%N;}
      if(!a){val[a]=k;} else {
        int t=a,v=0;while(v<k && t%q==0){v++;t/=q;}val[a]=v;
      }
      for(int b=0;b<N;b++){
        if(!polynomial){sum[a*N+b]=(a+b)%N; product[a*N+b]=(a*b)%N;}
        else {
          int aa=a,bb=b,s=0,p=0,pow=1;
          std::vector<int>da(k),db(k);
          for(int i=0;i<k;i++){da[i]=aa%q;db[i]=bb%q;aa/=q;bb/=q;}
          for(int i=0;i<k;i++){
            s+= ((da[i]+db[i])%q)*pow;
            int co=0;for(int j=0;j<=i;j++)co+=da[j]*db[i-j];
            p+= (co%q)*pow;pow*=q;
          }
          sum[a*N+b]=s;product[a*N+b]=p;
        }
      }
    }
  }
  inline int add(int a,int b)const{return sum[a*N+b];}
  inline int mul(int a,int b)const{return product[a*N+b];}
  inline int neg(int a)const{return negval[a];}
  inline int sub(int a,int b)const{return add(a,neg(b));}
};
ll powi(ll a,int b){ll r=1;for(int i=0;i<b;i++)r*=a;return r;}
// The constrained first factor has -det(X)=c*c+a*b a unit of fixed quadratic type.
int character(int x,int q) {
  x=(x%q+q)%q;
  if(!x)return 0;
  for(int t=1;t<q;t++)if(t*t%q==x)return 1;
  return -1;
}
ll expected(int q,int k,int valuation,int discriminant_type,int type) {
  if(valuation==k) return powi(q,4*k-3) * ((q-1)/2) * (q*q+type*q);
  ll plane=(discriminant_type==0)? (type==1?ll(q)*(q-1):0):
           ll(q-1)/2*(q-discriminant_type);
  return plane*powi(q,3*k+valuation-2);
}
void verify(int q,int k,bool poly){
  Ring R(q,k,poly);int N=R.N;ll order=ll(N)*N*N;
  if(order*order>500000000LL)throw std::runtime_error("test too large");
  std::vector<std::array<int,3>> elems(order);
  for(int a=0;a<N;a++)for(int b=0;b<N;b++)for(int c=0;c<N;c++)
    elems[(a*N+b)*N+c]={a,b,c};
  std::vector<ll> plus(order,0),minus(order,0);
  for(const auto &v:elems) {
    int a=v[0],b=v[1],c=v[2];
    int split=character(R.add(R.mul(c,c),R.mul(a,b))%q,q);
    if(split==0)continue;
    auto& fibers=split==1?plus:minus;
    for(const auto &w:elems){
      int u=w[0],z=w[1],d=w[2];
      int E=R.mul(2%N,R.sub(R.mul(c,u),R.mul(a,d)));
      int F=R.mul(2%N,R.sub(R.mul(b,d),R.mul(c,z)));
      int H=R.sub(R.mul(a,z),R.mul(b,u));
      fibers[(E*N+F)*N+H]++;
    }
  }
  ll totalplus=0,totalminus=0;
  ll nilpt_nonzero=0,missing=0;
  for(int a=0;a<N;a++)for(int b=0;b<N;b++)for(int c=0;c<N;c++){
    int v=std::min(R.val[a],std::min(R.val[b],R.val[c]));
    int delta_type=0;
    if(v!=k){
      int scale=(int)powi(q,v);
      int aa=(a/scale)%q,bb=(b/scale)%q,cc=(c/scale)%q;
      delta_type=character((cc*cc+aa*bb)%q,q);
    }
    auto ind=(a*N+b)*N+c;
    ll ep=expected(q,k,v,delta_type,1),em=expected(q,k,v,delta_type,-1);
    if(plus[ind]!=ep || minus[ind]!=em){
      std::cerr<<"FAIL q="<<q<<" k="<<k<<" ring="<<poly<<" target="<<a<<","<<b<<","<<c
               <<" v="<<v<<" delta="<<delta_type
               <<" got="<<plus[ind]<<","<<minus[ind]<<" expected="<<ep<<","<<em<<"\n";
      throw std::runtime_error("fiber mismatch");
    }
    totalplus+=plus[ind];totalminus+=minus[ind];
    if(v<k && delta_type==0){nilpt_nonzero++;if(minus[ind]==0)missing++;}
  }
  ll expected_total_plus=powi(q,3*k)*powi(q,3*k-3)*((q-1)/2)*(q*q+q);
  ll expected_total_minus=powi(q,3*k)*powi(q,3*k-3)*((q-1)/2)*(q*q-q);
  if(totalplus!=expected_total_plus || totalminus!=expected_total_minus) throw std::runtime_error("total discrepancy");
  std::cout<<"PASS q="<<q<<" length="<<k<<" ring="<<(poly?"Fq[t]/t^length":"Z/(q^length)")
  <<" targets="<<order<<" ordered_pairs="<<order*order
  <<" Qplus_pairs="<<totalplus<<" Qminus_pairs="<<totalminus
  <<" nonzero_reduced_isotropic_targets="<<nilpt_nonzero
  <<" nonsplit_unattainable_targets="<<missing<<"\n"<<std::flush;
}
int main(){
 try{
   verify(3,1,false);verify(5,1,false);verify(3,2,false);verify(3,2,true);
   verify(3,3,false);verify(3,3,true);
 }catch(const std::exception &e){std::cerr<<e.what()<<"\n";return 1;}
}
