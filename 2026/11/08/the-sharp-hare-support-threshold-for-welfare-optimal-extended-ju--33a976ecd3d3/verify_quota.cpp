#include <bits/stdc++.h>
using namespace std;
static int pc(unsigned x){return __builtin_popcount(x);}
static int checkJR(const vector<unsigned>& sup, int n,int k,unsigned w){
  unsigned cover=0;for(int c=0;c<(int)sup.size();c++)if(w>>c&1)cover|=sup[c];
  unsigned missing=((1u<<n)-1)^cover;
  int q=(n+k-1)/k;
  for(int c=0;c<(int)sup.size();c++)if(!(w>>c&1) && pc(sup[c]&missing)>=q)return c;
  return -1;
}
static bool checkEJR(const vector<unsigned>& sup,int n,int k,unsigned w){
  vector<int> sat(n,0);
  for(int c=0;c<(int)sup.size();c++)if(w>>c&1)for(int v=0;v<n;v++)if(sup[c]>>v&1)sat[v]++;
  for(int ell=1;ell<=k;ell++){
    int threshold=(ell*n+k-1)/k;
    for(unsigned S=1;S<(1u<<n);S++)if(pc(S)>=threshold){
      int common=0;
      for(unsigned c:sup)if((c&S)==S)common++;
      if(common<ell)continue;
      bool witness=false;
      for(int v=0;v<n;v++)if((S>>v&1)&&sat[v]>=ell)witness=true;
      if(!witness)return false;
    }
  }
  return true;
}
static bool trial(const vector<unsigned>& sup,int n,int k,long long& swaps){
 int m=sup.size(),q=(n+k-1)/k;
 for(unsigned S:sup)if(pc(S)>q)return true;
 vector<int> order(m);iota(order.begin(),order.end(),0);
 stable_sort(order.begin(),order.end(),[&](int a,int b){return pc(sup[a])>pc(sup[b]);});
 unsigned w=0;int opt=0;
 for(int i=0;i<k;i++){w|=1u<<order[i];opt+=pc(sup[order[i]]);}
 int prevCover=-1;
 for(int step=0;step<=n;step++){
  int c=checkJR(sup,n,k,w);
  if(c==-1){
   int score=0;for(int i=0;i<m;i++)if(w>>i&1)score+=pc(sup[i]);
   return score==opt && checkEJR(sup,n,k,w);
  }
  unsigned unionW=0;for(int e=0;e<m;e++)if(w>>e&1)unionW|=sup[e];
  if(prevCover>=0 && pc(unionW)<=prevCover)return false;
  prevCover=pc(unionW);
  bool found=false;
  for(int e=0;e<m&&!found;e++)if(w>>e&1){
   unsigned others=0;for(int j=0;j<m;j++)if((w>>j&1)&&j!=e)others|=sup[j];
   if((sup[e]&others)!=0){w^=1u<<e;w|=1u<<c;found=true;swaps++;}
  }
  if(!found)return false;
 }
 return false;
}
int main(){
 long long cases=0,swaps=0;
 for(int n=1;n<=5;n++)for(int m=1;m<=4;m++){
  uint64_t profiles=1ULL<<(n*m);
  for(uint64_t z=0;z<profiles;z++){
   vector<unsigned> sup(m);uint64_t x=z;
   for(int c=0;c<m;c++){sup[c]=(unsigned)(x&((1u<<n)-1));x>>=n;}
   for(int k=1;k<=min(n,m);k++){
    int q=(n+k-1)/k;
    bool eligible=true;for(auto S:sup)if(pc(S)>q)eligible=false;
    if(!eligible)continue;
    if(!trial(sup,n,k,swaps)){cerr<<"FAIL n="<<n<<" m="<<m<<" k="<<k<<" profile="<<z<<"\n";return 2;}
    cases++;
   }
  }
 }
 for(int q=1;q<=100;q++){
  // Three candidates have support q+1 and a fourth has disjoint support q.
  // The remaining q-1 voters are indifferent to all candidates.
  int n=3*q,k=3;
  int counts[]={q+1,q+1,q+1,q};
  if((n+k-1)/k!=q || counts[0] <= counts[3] || 3*(q+1)<=2*(q+1)+q){cerr<<"SHARPNESS FAIL q="<<q<<"\n";return 3;}
 }
 cout<<"PASS eligible_profiles="<<cases<<" replacement_swaps="<<swaps<<" sharp_family_q=1..100"<<endl;
}
