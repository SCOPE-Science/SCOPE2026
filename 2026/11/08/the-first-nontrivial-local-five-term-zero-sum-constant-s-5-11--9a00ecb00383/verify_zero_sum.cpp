// Exact rank-exhaustion certificate for a five-term zero-sum problem modulo 25.
#include <array>
#include <vector>
#include <iostream>
#include <cassert>
#include <algorithm>
using namespace std;

int mod5(int x){x%=5;return x<0?x+5:x;}
int inv5(int x){return x==1?1:x==2?3:x==3?2:4;}
struct Result {bool solvable;int rank;int equations;};
Result test(const array<int,4>& c, int n) {
    vector<int> r;
    for(int j=0;j<4;++j) for(int t=0;t<c[j];++t) r.push_back(j+1);
    assert((int)r.size()==n);
    vector<vector<int>> piv(n);
    int rank=0, count=0;
    for(int mask=0;mask<(1<<n);++mask){
        if(__builtin_popcount((unsigned)mask)!=5) continue;
        int sum=0;
        for(int j=0;j<n;++j) if(mask & (1<<j)) sum+=r[j];
        if(sum%5) continue;
        ++count;
        vector<int> row(n+1,0);
        for(int j=0;j<n;++j) if(mask & (1<<j)) row[j]=1;
        row[n]=mod5(-(sum/5));
        for(int col=0;col<n;++col){
            if(!row[col])continue;
            if(piv[col].empty()){
                const int factor=inv5(row[col]);
                for(int &v:row)v=mod5(v*factor);
                piv[col]=row; ++rank;row.clear();break;
            }
            int x=row[col];
            for(int j=col;j<=n;++j)row[j]=mod5(row[j]-x*piv[col][j]);
        }
        if(!row.empty() && row[n]) return {false,rank,count};
    }
    return {true,rank,count};
}
int main(){
    int profiles10=0,consistent10=0,rank2=0,rank8=0;
    for(int a=0;a<=10;++a)for(int b=0;b<=10-a;++b)for(int c=0;c<=10-a-b;++c){
        ++profiles10;
        auto res=test({a,b,c,10-a-b-c},10);
        if(res.solvable){++consistent10;rank2+=res.rank==2;rank8+=res.rank==8;}
    }
    int profiles11=0,consistent11=0,early_eq=0;
    for(int a=0;a<=11;++a)for(int b=0;b<=11-a;++b)for(int c=0;c<=11-a-b;++c){
        ++profiles11;
        auto res=test({a,b,c,11-a-b-c},11);
        consistent11+=res.solvable;
        early_eq+=res.equations;
    }
    assert(profiles10==286 && consistent10==12 && rank2==6 && rank8==6);
    assert(profiles11==364 && consistent11==0 && early_eq==5029);
    cout<<"CPP_TEN_PROFILES "<<profiles10<<" CONSISTENT "<<consistent10<<" RANK2 "<<rank2<<" RANK8 "<<rank8<<"\n";
    cout<<"CPP_ELEVEN_PROFILES "<<profiles11<<" CONSISTENT "<<consistent11<<" EQUATIONS "<<early_eq<<"\n";
    cout<<"CPP_VERIFY_OK exact_rank_exhaustion=True\n";
}
