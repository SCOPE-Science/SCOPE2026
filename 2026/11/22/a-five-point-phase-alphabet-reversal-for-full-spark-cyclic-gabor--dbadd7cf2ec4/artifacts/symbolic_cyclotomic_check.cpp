// Independent integer-only check of the two contrasting alphabets q=2 and q=5.
// Expands 5x5 determinants into Z[zeta_5]. No finite fields or modular inverses.
// Compile: g++ -O3 -std=c++17 symbolic_cyclotomic_check.cpp -o symbolic
// Run: ./symbolic
#include <array>
#include <iostream>
#include <algorithm>
using namespace std;
using A5=array<int,5>;
A5 permu[120];int sg[120], nperm=0;
void permutations(){
 A5 a={0,1,2,3,4};do{
  int inv=0;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)if(a[i]>a[j])inv++;
  permu[nperm]=a;sg[nperm++]=(inv%2)?-1:1;
 }while(next_permutation(a.begin(),a.end()));
}
bool exact_zero(int q,const A5& a,const A5& cols){
 int coefficients[5]={0,0,0,0,0};
 for(int pi=0;pi<nperm;pi++){
  int residue=0, sign=sg[pi];
  for(int t=0;t<5;t++){
   int c=cols[permu[pi][t]], x=c/5, xi=c%5;
   residue+=xi*t;
   int phase=a[(t-x+5)%5];
   if(q==2){if(phase)sign=-sign;}
   else residue+=phase;
  }
  coefficients[residue%5]+=sign;
 }
 for(int k=1;k<5;k++)if(coefficients[k]!=coefficients[0])return false;
 return true;
}
int main(){
 permutations();
 for(int q: {2,5}){
  int nwords=1;for(int i=0;i<4;i++)nwords*=q;
  int full=0,deficient=0;long long checked=0;int first_defective=-1;
  for(int index=0;index<nwords;index++){
   A5 a{};int h=index;for(int t=1;t<5;t++){a[t]=h%q;h/=q;}
   bool zero=false;
   for(int c0=0;c0<21&&!zero;c0++)for(int c1=c0+1;c1<22&&!zero;c1++)
   for(int c2=c1+1;c2<23&&!zero;c2++)for(int c3=c2+1;c3<24&&!zero;c3++)
   for(int c4=c3+1;c4<25&&!zero;c4++){
    checked++;A5 cols={c0,c1,c2,c3,c4};
    if(exact_zero(q,a,cols)){zero=true;}
   }
   if(zero){deficient++;if(first_defective<0)first_defective=index;}
   else full++;
  }
  cout<<"symbolic q="<<q<<" normalized="<<nwords<<" full="<<full
      <<" deficient="<<deficient<<" checked_minors="<<checked<<"\n";
 }
}
