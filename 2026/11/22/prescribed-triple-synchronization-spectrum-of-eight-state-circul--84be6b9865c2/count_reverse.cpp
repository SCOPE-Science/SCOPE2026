#include <bits/stdc++.h>
using namespace std;
// Rank-7 transformations on Z/8 with unique omitted image 0.
// Independent rank7 parameterization: choose duplicated image among 1..7,
// a pair of inputs, and a bijection of the remaining six inputs onto other six outputs.
int main(){
 const int N=8, ALL=255;
 int perm[6]={0,1,2,3,4,5};
 int ashift[256];
 for(int s=0;s<256;s++)ashift[s]=((s<<1)&255)|(s>>7);
 int masks3[56],k3=0;
 for(int s=0;s<256;s++)if(__builtin_popcount((unsigned)s)==3)masks3[k3++]=s;
 long long count=0,non=0;
 map<int,long long> hist, joint; int best=-1,bestc=0; vector<array<int,8>> extrema; map<int,long long> max_which;
 map<int,long long> resethist; map<pair<int,int>,array<int,8>> examples;
 int b[8],bm[256],ad[256],rhead[256],rlink[512],rfrom[512],d[256],que[256];
 for(int dup=1;dup<8;dup++) for(int i=0;i<8;i++)for(int j=i+1;j<8;j++){
   int inds[6],outs[6],ik=0,ok=0;
   for(int a=0;a<8;a++){if(a!=i&&a!=j)inds[ik++]=a;if(a!=dup&&a!=0)outs[ok++]=a;}
   // rank-seven: i and j go to duplicated output; remaining six inputs map other six outputs
   iota(perm,perm+6,0);
   do {
     b[i]=b[j]=dup;
     for(int t=0;t<6;t++)b[inds[t]]=outs[perm[t]];
     // forward subset transitions
     bm[0]=0;for(int s=1;s<256;s++){int bit=__builtin_ctz((unsigned)s);bm[s]=bm[s&(s-1)]|(1<<b[bit]);}
     // Reverse-BFS from all singleton target masks, computing shortest merge length of EVERY subset
     fill(rhead,rhead+256,-1);int e=0;
     for(int s=1;s<256;s++){
       rfrom[e]=s;rlink[e]=rhead[ashift[s]];rhead[ashift[s]]=e++;
       rfrom[e]=s;rlink[e]=rhead[bm[s]];rhead[bm[s]]=e++;
     }
     fill(d,d+256,-1);int h=0,t=0;
     for(int v=0;v<8;v++){d[1<<v]=0;que[t++]=1<<v;}
     while(h<t){int v=que[h++];for(int e=rhead[v];e!=-1;e=rlink[e]){int u=rfrom[e];if(d[u]<0){d[u]=d[v]+1;que[t++]=u;}}}
     int max3=-1,nd=-1;
     for(int ix=0;ix<56;ix++){int x=d[masks3[ix]];if(x<0){max3=-2;break;} if(x>max3){max3=x;nd=masks3[ix];}}
     if(max3<0){non++;}else {hist[max3]++;joint[max3*100+d[255]]++;resethist[d[255]]++;if(!examples.count({d[255],max3})){array<int,8> z;copy(b,b+8,z.begin());examples[{d[255],max3}]=z;}
       if(max3>best){best=max3;bestc=0;extrema.clear();}
       if(max3==best){bestc++;if(extrema.size()<20){array<int,8> z;copy(b,b+8,z.begin());extrema.push_back(z);}}
       max_which[nd]++;}
     count++;
   }while(next_permutation(perm,perm+6));
 }
 cout<<"TOTAL "<<count<<" NON "<<non<<" MAX "<<best<<" EXTREMA "<<bestc<<"\n";
 cout<<"TRIPLE_HIST ";for(auto &x:hist)cout<<x.first<<":"<<x.second<<" ";cout<<"\n";
 cout<<"RESET_HIST ";for(auto &x:resethist)cout<<x.first<<":"<<x.second<<" ";cout<<"\n";
 cout<<"EXAMPLES\n";for(auto &x:extrema){for(auto v:x)cout<<v;cout<<"\n";}
 cout<<"SAMPLES\n";for(auto [key,z]:examples)if((key.first==28 && (key.second==12||key.second==24))||key.second>=31){cout<<"S "<<key.first<<" "<<key.second<<" ";for(int x:z)cout<<x;cout<<"\n";} cout<<"JOINT_DISTINCT "<<joint.size()<<"\n";
 for(auto [k,v]:joint)cout<<"J "<<k/100<<" "<<k%100<<" "<<v<<"\n";
}
