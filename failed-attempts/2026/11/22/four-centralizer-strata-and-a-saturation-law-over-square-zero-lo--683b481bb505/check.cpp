#include <iostream>
#include <map>
#include <array>
#include <vector>
#include <cstdint>
#include <stdexcept>
using namespace std;
struct Ring {
    int n; bool char2;
    int add(int a,int b)const {return char2?(a^b):((a+b)%n);}
    int sub(int a,int b)const {return char2?(a^b):((a-b+n)%n);}
    int mul(int a,int b)const {
        if(!char2) return (a*b)%n;
        int a0=a&1,b0=b&1;
        return (a0&b0) | ((a0?(b&~1):0) ^ (b0?(a&~1):0));
    }
};
static bool commute(const array<int,4>& A,const array<int,4>& B,const Ring& R){
    int diagonal=R.sub(R.mul(A[1],B[2]),R.mul(A[2],B[1]));
    if(diagonal) return false;
    int a_minus_d=R.sub(A[0],A[3]);
    int e_minus_h=R.sub(B[0],B[3]);
    if(R.sub(R.mul(a_minus_d,B[1]),R.mul(e_minus_h,A[1]))) return false;
    if(R.sub(R.mul(a_minus_d,B[2]),R.mul(e_minus_h,A[2]))) return false;
    return true;
}
void run_case(const Ring R, const int q, const int d){
    const int n=R.n, m=n*n*n*n;
    vector<array<int,4>> a(m);
    for(int i=0;i<m;i++){
        int z=i;
        for(int j=0;j<4;j++){a[i][j]=z%n; z/=n;}
    }
    map<int,long long> freq;
    long long pairs=0;
    for(int i=0;i<m;i++){
        int count=0;
        for(int j=0;j<m;j++)count+=commute(a[i],a[j],R);
        freq[count]++;
        pairs+=count;
    }
    long long qd=1;for(int i=0;i<d;i++)qd*=q;
    long long q2=q*q,q4=q2*q2;
    long long n_non=(q4-q)*qd*qd*qd*qd;
    long long n_scalar=q*qd;
    long long n_c2=q*(q2+q+1)*(qd*qd-qd);
    long long n_c1=q*(qd*qd*qd*qd-qd-(q2+q+1)*(qd*qd-qd));
    map<int,long long> expect;
    auto pw=[](long long x,int a){long long p=1;while(a--)p*=x;return p;};
    expect[(int)pw(q,2*d+2)]+=n_non;
    expect[(int)pw(q,4*d+4)]+=n_scalar;
    expect[(int)pw(q,4*d+2)]+=n_c2;
    expect[(int)pw(q,4*d+1)]+=n_c1;
    for(auto it=expect.begin();it!=expect.end();){if(it->second==0)it=expect.erase(it);else ++it;}
    auto formula=pw(q,2)*pw(q,8*d)+(pw(q,6)+pw(q,5)-pw(q,3)-pw(q,2))*pw(q,6*d);
    cout<<"ring="<<(R.char2?"F2[epsilon_1,...,epsilon_d]/(epsilon)^2":"Z/4Z")<<" q="<<q<<" d="<<d<<" matrices="<<m<<" empirical="<<pairs<<" predicted="<<formula<<"\n";
    for(auto [c,count]:freq)cout<<" centralizer_size="<<c<<" matrices="<<count<<"\n";
    if(freq!=expect||pairs!=formula)throw runtime_error("exhaustive check failed");
    cout<<"PASS\n";
}
int main(){
    try {run_case({4,true},2,1);run_case({8,true},2,2);run_case({4,false},2,1);}
    catch(const exception &e){cerr<<e.what()<<"\n";return 1;}
}
