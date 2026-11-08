// Independent labelled-state enumeration for three-color successor contact
// dynamics on K_{m,n} with the distinguished edge (0,m) deleted.
// Compile: g++ -O2 -std=c++17 direct_check.cpp -o direct_check
// Run: ./direct_check
#include <array>
#include <vector>
#include <map>
#include <iostream>
#include <cassert>
#include <cstdint>
#include <algorithm>
using namespace std;
using ll=long long;
ll power(ll a,int b){ll p=1;while(b--)p*=a;return p;}
ll ff(int r,int k){if(k==1)return 1;if(k==2)return power(2,r)-2;return power(3,r)-3*power(2,r)+3;}
int main(){
  ll total_checked=0;int graphs=0;
  for(int m=2;m<=6;m++)for(int n=2;n<=6;n++){
    int N=m+n;ll configs=power(3,N);ll u=ff(m-1,2),v=ff(n-1,2),R=ff(m-1,3),S=ff(n-1,3);
    map<pair<int,int>,ll> expected={
      {{0,1},3}, {{0,3},9*R*S+6*R*v+6*S*u+3*u*v}, {{0,4},24*u*v+12*u+12*v},
      {{1,1},12*u*v+15*u+15*v+24}, {{1,3},3*R*v+3*S*u},
      {{1,4},18*R*v+12*R+18*S*u+12*S+30*u*v+12*u+12*v},
      {{2,1},9*R+9*S+24*u+24*v+24},
      {{2,4},6*R+6*S+12*u*v+12*u+12*v},
      {{3,1},6*u+6*v+30}
    };
    map<pair<int,int>,ll> actual;
    for(ll encoded=0;encoded<configs;encoded++){
      vector<unsigned char> state(N);
      ll tmp=encoded;
      for(int i=0;i<N;i++){state[i]=tmp%3;tmp/=3;}
      vector<ll> history;
      while(true){
        ll key=0,weight=1;
        for(int i=0;i<N;i++){key+=weight*state[i];weight*=3;}
        auto found=find(history.begin(),history.end(),key);
        if(found!=history.end()){
          int t=found-history.begin(),p=(int)history.size()-t;
          if(!(t<=3 && (p==1||p==3||p==4))){cerr<<"BAD PERIOD "<<m<<" "<<n<<" "<<t<<" "<<p<<"\n";return 1;}
          actual[{t,p}]++;
          break;
        }
        if(history.size()>16){cerr<<"NO REPEAT\n";return 1;}
        history.push_back(key);
        vector<unsigned char> next(N);
        for(int i=0;i<N;i++){
          bool has=false;unsigned char suc=(state[i]+1)%3;
          for(int j=0;j<N;j++){
            // Edges only cross the bipartition, except (0,m).
            bool cross=(i<m)!=(j<m);
            bool deleted=(i==0&&j==m)||(i==m&&j==0);
            if(cross&&!deleted&&state[j]==suc){has=true;break;}
          }
          next[i]=has?suc:state[i];
        }
        state.swap(next);
      }
    }
    for(auto [tp,exp]:expected)if(actual[tp]!=exp){
      cerr<<"FAILED m="<<m<<" n="<<n<<" T="<<tp.first<<" p="<<tp.second<<" actual="<<actual[tp]<<" expected="<<exp<<"\n";return 1;
    }
    ll sum=0;for(auto [tp,v]:actual){if(!expected.count(tp)){cerr<<"EXTRA CLASS\n";return 1;}sum+=v;}
    assert(sum==configs);
    graphs++;total_checked+=configs;
    cout<<"VERIFIED m="<<m<<" n="<<n<<" configurations="<<configs<<" classes="<<actual.size()<<"\n";
  }
  cout<<"DIRECT_CHECK_OK graphs="<<graphs<<" configurations="<<total_checked<<"\n";
}
