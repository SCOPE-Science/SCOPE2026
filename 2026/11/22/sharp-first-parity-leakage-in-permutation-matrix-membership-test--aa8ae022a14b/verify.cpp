// Independent exhaustive parity-trace and shattering test on 6-by-6 boards.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
using P=array<unsigned char,6>;
struct Rec { P p; unsigned char parity; };
int main(){
    vector<Rec> perms;
    P p={0,1,2,3,4,5};
    do {
      int parity=0;
      for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)parity^=(p[i]>p[j]);
      perms.push_back({p,(unsigned char)parity});
    } while(next_permutation(p.begin(),p.end()));
    assert(perms.size()==720);
    int matched=0, balanced=0, boundary=0;
    for(int k=0;k<=6;k++){
      vector<int> idx(k);
      auto run=[&](){
        bool matching=true;
        unsigned row=0,col=0;
        for(int e:idx){
           int i=e/6,j=e%6;
           if((row&(1u<<i))||(col&(1u<<j)))matching=false;
           row|=1u<<i;col|=1u<<j;
        }
        if(k<=4){
           array<int,64> even={}, odd={};
           for(auto &rec:perms){
              int trace=0;
              for(int j=0;j<k;j++) if(rec.p[idx[j]/6]==idx[j]%6)trace|=1<<j;
              (rec.parity ? odd:even)[trace]++;
           }
           for(int j=0;j<(1<<k);j++) assert(even[j]==odd[j]);
           if(matching){for(int j=0;j<(1<<k);j++)assert(even[j]>0);matched++;}
           balanced++;
        } else if(matching){
           array<int,64> even={}, odd={};
           for(auto &rec:perms){
              int trace=0;
              for(int j=0;j<k;j++)if(rec.p[idx[j]/6]==idx[j]%6)trace|=1<<j;
              (rec.parity ? odd:even)[trace]++;
           }
           int countEven=0,countOdd=0;
           for(int j=0;j<(1<<k);j++) {countEven+=(even[j]>0);countOdd+=(odd[j]>0);}
           assert(countEven<(1<<k) && countOdd<(1<<k));
           if(k==5){
             P completion={0,0,0,0,0,0};
             unsigned rows=0,cols=0;
             for(int edge:idx){completion[edge/6]=edge%6;rows|=1u<<(edge/6);cols|=1u<<(edge%6);}
             int missingR=0,missingC=0;
             while(rows & (1u<<missingR))missingR++;
             while(cols & (1u<<missingC))missingC++;
             completion[missingR]=missingC;
             int inversionParity=0;
             for(int a=0;a<6;a++)for(int b=a+1;b<6;b++) inversionParity^=(completion[a]>completion[b]);
             int signedCompletion=inversionParity ? -1:1;
             int absolute=0;
             for(int j=0;j<(1<<k);j++){
                 int ones=__builtin_popcount((unsigned)j);
                 int expected=signedCompletion * (((k-ones)%2) ? -1:1);
                 assert(even[j]-odd[j]==expected);
                 absolute+=abs(even[j]-odd[j]);
             }
             assert(absolute==(1<<k));
           }
           boundary++;
        }
      };
      if(k==0){run();continue;}
      for(int j=0;j<k;j++)idx[j]=j;
      for(;;){
        run();
        int t=k-1;
        while(t>=0 && idx[t]==36-k+t)t--;
        if(t<0)break;
        idx[t]++;
        for(int j=t+1;j<k;j++)idx[j]=idx[j-1]+1;
      }
    }
    assert(balanced==1+36+630+7140+58905);
    assert(boundary==4320+720);
    cout<<"CXX_n=6 balanced_supports="<<balanced<<" matched_small="<<matched<<" matched_boundary="<<boundary<<" first_leakage_verified=4320 PASS\n";
}
