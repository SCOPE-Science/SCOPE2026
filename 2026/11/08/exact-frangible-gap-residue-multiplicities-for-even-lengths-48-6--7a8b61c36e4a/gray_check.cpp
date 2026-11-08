// Independent Gray-code inclusion-exclusion implementation.
#include <bits/stdc++.h>
using namespace std;using I=__int128_t;
string dec(I x){if(x==0)return "0";bool neg=x<0; if(neg)x=-x;string s;for(;x;x/=10)s.push_back(char('0'+x%10));if(neg)s.push_back('-');reverse(s.begin(),s.end());return s;}
bool prime(int x){if(x<2)return false;for(int d=2;d*d<=x;d++)if(x%d==0)return false;return true;}
I count(int h){
 int m=h/2-1;vector<int> q;for(int p=3;p<h;p+=2)if(prime(p))q.push_back(p);
 int np=q.size();int seen[20][64]={};int forbidden[20]={};int residues[20][32]={};
 for(int i=0;i<np;i++){
  int p=q[i]; seen[i][0]=1;forbidden[i]=1;
  int other=(p-h%p)%p;if(!seen[i][other]){seen[i][other]=1;forbidden[i]++;}
  for(int j=0;j<m;j++)residues[i][j]=(p-(2*j+2)%p)%p;
 }
 I s=0; uint64_t mask=0,N=1ULL<<m;
 for(uint64_t t=0;t<N;t++){
  if(t){int j=__builtin_ctzll(t);mask^=(1ULL<<j);int delta=(mask>>j)&1?1:-1;
   for(int i=0;i<np;i++){
    int &v=seen[i][residues[i][j]];
    if(delta==1){if(v==0)forbidden[i]++;++v;}
    else {--v;if(v==0)forbidden[i]--;}
   }
  }
  I prod=1;
  for(int i=0;i<np;i++){int k=q[i]-forbidden[i];prod*=k;if(k==0)break;}
  if(t&1)s-=prod;else s+=prod;
 }
 return s;
}
int main(int argc,char**argv){int first=argc>1?atoi(argv[1]):48,last=argc>2?atoi(argv[2]):56;for(int h=first;h<=last;h+=2){auto t=chrono::steady_clock::now();auto n=count(h);cout<<h<<" "<<dec(n)<<" gray_seconds="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<endl;}}
