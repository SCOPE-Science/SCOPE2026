#include <bits/stdc++.h>
using namespace std;const int L=256;using Bits=bitset<L>;
vector<unsigned> W;Bits adj[L];long long nodes=0,leaves=0;int best=0;vector<int> proof;
void gen(int n,int p,int k,unsigned mask,int h){if(p==2*n){if(h==0)W.push_back(mask);return;}if(k<n)gen(n,p+1,k+1,mask|(1u<<p),h+1); if(p-k<n && h>0)gen(n,p+1,k,mask,h-1);}
void search(Bits P,int depth,vector<int> &select){nodes++;if(P.none()){leaves++;if(depth>best){best=depth;proof=select;cerr<<"new_best "<<best<<" nodes "<<nodes<<"\n";}return;}
 int ord[L],col[L],ct=0,nc=0;Bits rem=P;
 while(rem.any()) {nc++;Bits free=rem;while(free.any()){int v=free._Find_first();ord[ct]=v;col[ct++]=nc;rem.reset(v);free.reset(v);free &=~adj[v];}}
 for(int i=ct-1;i>=0;--i){if(depth+col[i]<=best)return;int v=ord[i]; select.push_back(v);Bits R=P & adj[v];if(R.any())search(R,depth+1,select); else {leaves++;if(depth+1>best){best=depth+1;proof=select;cerr<<"new_best "<<best<<" nodes "<<nodes<<"\n";}}select.pop_back();P.reset(v);}
}
int main(int argc,char **argv){int n= argc>1?atoi(argv[1]):6;gen(n,0,0,0,0);sort(W.begin(),W.end());int sz=W.size();for(int i=0;i<sz;i++)for(int j=0;j<sz;j++)if(i!=j&&__builtin_popcount(W[i]^W[j])>=4)adj[i].set(j); Bits P; for(int i=0;i<sz;i++)P.set(i);vector<int> s;search(P,0,s);cout<<"MAX "<<best<<" NODES "<<nodes<<" LEAVES "<<leaves<<" WORDS "<<sz<<"\n";for(int v:proof)cout<<W[v]<<" ";cout<<"\n";}
