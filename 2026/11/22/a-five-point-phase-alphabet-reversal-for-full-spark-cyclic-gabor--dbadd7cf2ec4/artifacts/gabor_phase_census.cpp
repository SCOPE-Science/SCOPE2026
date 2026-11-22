// Exact cyclotomic Gabor full-spark census in dimension five.
// Compile: g++ -std=c++17 -O2 gabor_phase_census.cpp -o census
// Run: ./census [witness.tsv]
// No floating point arithmetic is used.
#include <bits/stdc++.h>
using namespace std;
using i64=long long;
struct Field {
    int p, generator, root60;
    vector<int> inv;
    Field(int prime,int g):p(prime),generator(g),inv(p) {
        if (!isprime(p)) throw runtime_error("not a prime");
        root60=power(g,(p-1)/60);
        if (power(root60,60)!=1 || power(root60,30)==1 || power(root60,20)==1 || power(root60,12)==1)
            throw runtime_error("wrong order for root60");
        inv[1]=1;
        for(int i=2;i<p;i++) inv[i]=int(p-(p/i)*i64(inv[p%i])%p);
    }
    static bool isprime(int p) {for(int d=2;d*i64(d)<=p;d++) if(p%d==0)return false;return p>=2;}
    int power(int b, int exponent) const {
        i64 a=1,x=b; while(exponent){if(exponent&1)a=a*x%p;x=x*x%p;exponent>>=1;}return int(a);
    }
    int omega(int order) const {return power(root60,60/order);}
    void make(int q,const array<int,5>& a, int A[5][25]) const {
        int zeta[5],chi[5];
        for(int k=0;k<q;k++)zeta[k]=power(omega(q),k);
        for(int k=0;k<5;k++)chi[k]=power(omega(5),k);
        for(int x=0;x<5;x++)for(int y=0;y<5;y++)for(int t=0;t<5;t++)
            A[t][5*x+y] = i64(chi[(y*t)%5])*zeta[a[(t-x+5)%5]]%p;
    }
    bool singular(const int A[5][25],const array<int,5>& S) const {
        int B[5][5];for(int i=0;i<5;i++)for(int j=0;j<5;j++)B[i][j]=A[i][S[j]];
        for(int k=0;k<5;k++) {
            int pivot=k;while(pivot<5 && B[pivot][k]==0)pivot++;
            if(pivot==5)return true;
            if(pivot!=k)for(int j=k;j<5;j++)swap(B[pivot][j],B[k][j]);
            int inverse=inv[B[k][k]];
            for(int i=k+1;i<5;i++) {
                int m=i64(B[i][k])*inverse%p;
                for(int j=k+1;j<5;j++) {
                    B[i][j] = (B[i][j]-i64(m)*B[k][j])%p;
                    if(B[i][j]<0)B[i][j]+=p;
                }
                B[i][k]=0;
            }
        }
        return false;
    }
};
int main(int argc,char**argv){
    Field F1(10000141,11),F2(10000261,2);
    if(i64(F1.p)*F2.p<=95367431640625LL)throw runtime_error("insufficient norm bound");
    ofstream out;if(argc>1){out.open(argv[1]);out<<"q\texponents_a0_to_a4\tfirst_singular_columns_zero_based\n";}
    for(int q=1;q<=5;q++){
        i64 nwords=1,full=0,witnessed=0,primes_touched=0,minor_checks=0; for(int i=0;i<4;i++)nwords*=q;
        string example="none";int freq[25]={};
        for(int index=0;index<nwords;index++){
            int digits=index;array<int,5> a{};
            for(int j=1;j<5;j++){a[j]=digits%q;digits/=q;}
            int A[5][25],B[5][25]; F1.make(q,a,A);F2.make(q,a,B);
            bool zero=false;array<int,5> cert{};
            for(int a0=0;a0<21&&!zero;a0++)for(int a1=a0+1;a1<22&&!zero;a1++)
            for(int a2=a1+1;a2<23&&!zero;a2++)for(int a3=a2+1;a3<24&&!zero;a3++)
            for(int a4=a3+1;a4<25&&!zero;a4++){
                array<int,5> S={a0,a1,a2,a3,a4}; minor_checks++;
                if(F1.singular(A,S)){
                    primes_touched++;
                    if(F2.singular(B,S)){zero=true;cert=S;}
                }
            }
            if(zero){witnessed++;freq[cert[4]]++;if(out.is_open()){
                out<<q<<'\t';for(int j=0;j<5;j++){if(j)out<<',';out<<a[j];}
                out<<'\t';for(int j=0;j<5;j++){if(j)out<<',';out<<cert[j];}out<<'\n';
            }}else{
                full++;if(example=="none"){
                    example="";for(int j=0;j<5;j++){if(j)example+=',';example+=to_string(a[j]);}
                }
            }
        }
        cout<<"q="<<q<<" normalized="<<nwords<<" full="<<full<<" deficient="<<witnessed
            <<" witnessed_pair_checks="<<primes_touched<<" checked_minors="<<minor_checks
            <<" first_full="<<example<<"\n";
    }
}
