// Exact cyclotomic-coefficient verification of the three-by-three minor test.
// No floating-point arithmetic or external libraries are used.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
struct GI { int re=0, im=0; bool operator==(const GI&z)const {return re==z.re&&im==z.im;} };
static const int perm[6][3]={{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};
static const int sgn[6]={1,-1,-1,1,1,-1};
int main(){
  long long total=0; long long bad=0;
  for (int p: {3,5,7,11}) {
    for (int basis=0;basis<2;basis++) { // basis 0: C4; basis 1: C2 x C2
      if (basis==1 && p==11) continue;
      const int N=4*p; long long checked=0;
      vector<array<int,3>> triples;
      for (int a=1;a<N;a++) for(int b=a+1;b<N;b++)
        if (a%p!=b%p && a%p!=0 && b%p!=0) triples.push_back({0,a,b});
      for (auto R: triples) for (auto C: triples) {
        vector<GI> coeff(p);
        for (int k=0;k<6;k++) {
          int e=0; int phase=0;
          for (int i=0;i<3;i++) {
            const int row=R[i],col=C[perm[k][i]];
            e += (row%p)*(col%p);
            if (basis==0) phase += (row%4)*(col%4);
            else {
              const int x=row%4,y=col%4;
              phase+=2*((((x&1)&&(y&1)) ^ ((x&2)&&(y&2)))?1:0);
            }
          }
          const int v=sgn[k];
          auto&z=coeff[e%p];
          switch(phase%4){case 0:z.re+=v;break;case 1:z.im+=v;break;case 2:z.re-=v;break;case 3:z.im-=v;break;}
        }
        bool singular=true;
        for(int k=1;k<p;k++) if (!(coeff[k]==coeff[0])){singular=false;break;}
        if(singular)bad++;
        checked++;
      }
      cout<<"H="<<(basis==0?"C4":"C2xC2")<<" p="<<p<<" normalized_minors="<<checked<<" singular="<<bad<<"\n";
      total+=checked;
    }
  }
  // Directly check the parity obstruction for each ordered normalized pair.
  long long parity_cases=0;
  for(int p: {3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103})
   for(int t=2;t<p;t++)for(int s=2;s<p;s++) {
     int n[103]={0};
     for (int x: {1+t*s,s,t,s+t,t*s,1}) n[x%p]++;
     bool even=true;
     for(int x=0;x<p;x++)if(n[x]%2) even=false;
     if(even){cerr<<"FAIL parity p="<<p<<" s="<<s<<" t="<<t<<"\n";return 1;}
     parity_cases++;
   }
  cout<<"total_exact_normalized_minors="<<total<<" singular="<<bad<<"\n";
  cout<<"parity_pairs_checked="<<parity_cases<<" failing=0\n";
  if (bad) return 1;
  cout<<"PASS\n";
}
