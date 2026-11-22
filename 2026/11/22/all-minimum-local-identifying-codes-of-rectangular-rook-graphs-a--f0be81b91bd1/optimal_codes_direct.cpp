#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
long long fact(int n){long long p=1;for(int i=2;i<=n;i++)p*=i;return p;}
int main(){
  for(auto [s,l]:vector<pair<int,int>>{{3,3},{3,4},{3,5},{4,4},{4,5},{4,6},{5,7}}){
    int N=s*l; assert(N<64);
    vector<U> neigh(N);
    for(int v=0;v<N;v++)for(int w=0;w<N;w++)
      if(v/l==w/l||v%l==w%l)neigh[v]|=U(1)<<w;
    long long local=0,global=0,invalid=0;
    vector<int> leaf(l,-1); vector<int> pairs(l,-1);
    function<void(int)> putpairs=[&](int j){
      if(j==l){
        U code=0;
        for(int c=0;c<l;c++){
          if(leaf[c]>=0)code|=U(1)<<(leaf[c]*l+c);
          else {int k=0;for(int r=0;r<s;r++)for(int rr=r+1;rr<s;rr++){
            if(k==pairs[c]){code|=U(1)<<(r*l+c);code|=U(1)<<(rr*l+c);} k++;
          }}
        }
        vector<U> I(N);bool cover=1;for(int v=0;v<N;v++){I[v]=neigh[v]&code;if(!I[v])cover=0;}
        bool loc=cover,glob=cover;
        for(int v=0;v<N;v++)for(int w=v+1;w<N;w++){
          if(I[v]==I[w]){glob=0;if(v/l==w/l||v%l==w%l)loc=0;}
        }
        if(!loc){invalid++;return;}local++;if(glob)global++;
        return;
      }
      if(leaf[j]>=0){putpairs(j+1);return;}
      for(int p=0;p<s*(s-1)/2;p++){pairs[j]=p;putpairs(j+1);}
    };
    function<void(int)> putleaves=[&](int r){
      if(r==s){putpairs(0);return;}
      for(int c=0;c<l;c++)if(leaf[c]<0){leaf[c]=r;putleaves(r+1);leaf[c]=-1;}
    };
    putleaves(0);
    cout<<s<<" "<<l<<" local="<<local<<" ordinary_identifying="<<global<<" failed_local="<<invalid<<"\n";
  }
}
