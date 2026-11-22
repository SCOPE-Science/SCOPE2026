// Independent exact septaphase self-STFT checker using cyclic increment words.
// Every execution path performs integer residue counts; no floating-point decisions.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int mod7(int x){ x%=7; return x<0?x+7:x; }
int main(){
    const int P=7;
    map<int,long long> ranks;
    map<array<int,7>,long long> profile;
    for(int code=0;code<117649;code++){
        int increment[7]={0};
        int u=code;
        int sum=0;
        for(int t=1;t<P;t++){
            increment[t]=u%P;
            sum+=increment[t];
            u/=P;
        }
        increment[0]=mod7(-sum); // explicit cyclic closure
        int word[7]={0};
        for(int t=1;t<P;t++)word[t]=mod7(word[t-1]+increment[t]);
        assert(mod7(word[0]-word[6])==increment[0]);
        array<int,7> zeros{};
        for(int shift=0;shift<P;shift++)for(int k=0;k<P;k++){
            array<int,7> counts{};
            for(int x=0;x<P;x++){
                // Independent coefficient construction in the cyclotomic quotient.
                int power=mod7(word[x]-word[mod7(x-shift)]-k*x);
                counts[power]++;
            }
            bool vanishes=true;
            for(int j=0;j<6;j++)if(counts[j]!=counts[6])vanishes=false;
            if(vanishes)zeros[shift]++;
        }
        int nonzero=49;
        for(int n:zeros)nonzero-=n;
        ranks[nonzero]++;
        profile[zeros]++;
    }
    const map<int,long long> expected_ranks={{7,49},{37,14406},{39,18522},{41,24696},{43,59976}};
    assert(ranks==expected_ranks);
    assert(profile.size()==12);
    map<array<int,7>,long long> expected={
      {{{6,0,0,0,0,0,0}},59976},
      {{{6,0,0,1,1,0,0}},8232},
      {{{6,0,0,2,2,0,0}},2058},
      {{{6,0,1,0,0,1,0}},8232},
      {{{6,0,1,1,1,1,0}},4116},
      {{{6,0,2,0,0,2,0}},2058},
      {{{6,1,0,0,0,0,1}},8232},
      {{{6,1,0,1,1,0,1}},4116},
      {{{6,1,1,0,0,1,1}},4116},
      {{{6,1,1,1,1,1,1}},14406},
      {{{6,2,0,0,0,0,2}},2058},
      {{{6,6,6,6,6,6,6}},49}
    };
    assert(profile==expected);
    cout<<"SEPTAPHASE_P7_INCREMENT_PASS total=117649\n";
    for(auto [rank,count]:ranks)cout<<"rank "<<rank<<" count "<<count<<"\n";
    for(auto [mask,count]:profile){
      cout<<"profile ";for(int n:mask)cout<<n;cout<<" count "<<count<<"\n";
    }
}
