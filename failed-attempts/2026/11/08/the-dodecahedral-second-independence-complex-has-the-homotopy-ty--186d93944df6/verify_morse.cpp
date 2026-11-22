// Exhaustive simplicial and integral Morse check for the second independence
// complex of the twenty-vertex dodecahedral graph GP(10,2).
// Compile: g++ -O2 -std=c++17 verify_morse.cpp -o verify_morse
// Run: ./verify_morse
#include <array>
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
constexpr int N = 1 << 20;
int adjacency[20] = {};
vector<uint8_t> face(N), used(N), visit(N);
vector<int> partner(N,-1), critical6, critical7;
vector<array<long long, 2>> projection(N);
void check(bool ok, const char *msg) { if(!ok){cerr << "CHECK_FAILED: " << msg << '\n'; exit(1);} }
int countbits(int s) {return __builtin_popcount((unsigned)s);}
int lowbitpos(int s) {return __builtin_ctz((unsigned)s);}
int incidence(int s, int v) {return countbits(s & ((1<<v)-1))%2 ? -1:1;}
void edge(int a,int b){adjacency[a] |= 1<<b; adjacency[b] |= 1<<a;}
void build_graph(){for(int j=0;j<10;j++){
    edge(j,(j+1)%10); edge(j,j+10);edge(10+j,10+(j+2)%10);
}}
void enumerate_faces(){face[0]=1;
 for(int s=1;s<N;s++){
    const int v=lowbitpos(s),t=s^(1<<v);
    if(!face[t])continue;
    const int deg=countbits(adjacency[v]&t);
    if(deg>1)continue;
    if(deg==1){const int w=lowbitpos(adjacency[v]&t);
       if(countbits(adjacency[w]&t)>0)continue;}
    face[s]=1;
 }
 // Different enumeration: 60 forbidden induced 3-paths.
 vector<int> paths;
 for(int v=0;v<20;v++){
   vector<int> ns;for(int w=0;w<20;w++)if(adjacency[v]&(1<<w))ns.push_back(w);
   check(ns.size()==3,"graph not cubic");
   for(int a=0;a<3;a++)for(int b=a+1;b<3;b++)
     paths.push_back((1<<v)|(1<<ns[a])|(1<<ns[b]));
 }
 check(paths.size()==60,"3-path count");
 vector<int> histogram(21);
 int total=0;
 for(int s=0;s<N;s++){
   bool p3free=true;
   for(int p:paths)if((s&p)==p){p3free=false;break;}
   check(p3free==(bool)face[s],"independent forbidden-triple enumeration");
   if(face[s]){histogram[countbits(s)]++;total++;}
 }
 const vector<int> expected={1,20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5};
 for(int k=0;k<(int)expected.size();k++)check(histogram[k]==expected[k],"face vector");
 check(total==63143,"total simplices including empty");
 cout<<"ENUMERATION_OK faces="<<total<<" nonempty="<<total-1
     <<" max_dimension=11 forbidden_paths="<<paths.size()<<'\n';
}
void match_faces(){
 vector<int> order;for(int i=0;i<10;i++){order.push_back(i);order.push_back(10+i);}
 // Sequential elementary toggles on the currently unmatched face set.
 // The empty face is deliberately left unmatched.
 for(int v:order){const int b=1<<v;
   for(int s=1;s<N;s++)if(face[s] && !(s&b)){
      const int t=s|b;
      if(face[t] && partner[s]<0 && partner[t]<0){partner[s]=t;partner[t]=s;}
   }
 }
 vector<int> dims(21);int pairs=0;
 for(int s=1;s<N;s++)if(face[s]){
    if(partner[s]<0){dims[countbits(s)]++;
       if(countbits(s)==7)critical6.push_back(s);
       if(countbits(s)==8)critical7.push_back(s);
    }else if(s<partner[s])pairs++;
 }
 check(partner[0]==-1,"empty face unmatched");
 check(pairs==31569,"matching pair count");
 check(dims[1]==1 && dims[7]==2 && dims[8]==1,"critical-cell counts");
 for(int k=2;k<=20;k++)if(k!=7&&k!=8)check(dims[k]==0,"extraneous critical cell");
 check(critical6==vector<int>({26312,420992}),"critical 6-cell masks");
 check(critical7==vector<int>({406098}),"critical 7-cell mask");
 cout<<"MATCHING_OK pairs="<<pairs<<" critical=(one_dim0,two_dim6,one_dim7)"
     <<" critical6_masks=26312,420992 critical7_mask=406098\n";
}
void verify_acyclicity(){
 vector<int> indeg(N);
 long long arrows=0;
 for(int s=0;s<N;s++)if(face[s])for(int v=0;v<20;v++)if(!(s&(1<<v)) && face[s|(1<<v)]){
    const int t=s|(1<<v);
    const int to=(partner[s]==t) ? t:s;
    indeg[to]++;arrows++;
 }
 check(arrows==410520,"cover count");
 vector<int> q;q.reserve(63143);
 for(int s=0;s<N;s++)if(face[s]&&indeg[s]==0)q.push_back(s);
 for(size_t i=0;i<q.size();i++){
    const int s=q[i];
    for(int v=0;v<20;v++){
       const int bit=1<<v,t=s^bit;
       if(!face[t])continue;
       if(s&bit){if(partner[s]!=t && --indeg[t]==0)q.push_back(t);}
       else {if(partner[s]==t && --indeg[t]==0)q.push_back(t);}
    }
 }
 check(q.size()==63143,"reversed Hasse orientation has a directed cycle");
 cout<<"ACYCLICITY_OK covering_relations="<<arrows<<" sorted_faces="<<q.size()<<'\n';
}
// Morse projection of 6-faces onto the critical 6-cell basis.
// For lower-matched B < A (dim A=7), use d(A)=epsilon(B)B+sum epsilon(C)C
// and eliminate B, recursively. Upper-matched 6-cells project to zero.
array<long long,2> mproj(int s){
 if(visit[s]==2)return projection[s];
 check(visit[s]!=1,"gradient recursion cycle");visit[s]=1;
 array<long long,2> result{0,0};
 if(partner[s]<0){for(int j=0;j<2;j++)if(critical6[j]==s)result[j]=1;}
 else if(countbits(partner[s])==8){
   const int a=partner[s],v=lowbitpos(a^s),pivot=incidence(a,v);
   for(int bits=a;bits;bits&=bits-1){const int i=lowbitpos(bits),b=a^(1<<i);
      if(b==s)continue;
      auto z=mproj(b);const int coefficient=-pivot*incidence(a,i);
      for(int j=0;j<2;j++){
         check(z[j]!=INT64_MIN,"projection sign overflow");
         long long term=coefficient*z[j], next=0;
         check(!__builtin_add_overflow(result[j],term,&next),"projection integer overflow");
         result[j]=next;
      }
   }
 }
 projection[s]=result;visit[s]=2;return result;
}
void verify_morse_boundary(){
 check(critical7.size()==1 && critical6.size()==2,"boundary basis sizes");
 const int a=critical7[0];array<long long,2> boundary{0,0};
 for(int bits=a;bits;bits&=bits-1){const int v=lowbitpos(bits);
    const auto z=mproj(a^(1<<v));const int sign=incidence(a,v);
    for(int j=0;j<2;j++){
       check(z[j]!=INT64_MIN,"boundary sign overflow");
       long long term=sign*z[j],next=0;
       check(!__builtin_add_overflow(boundary[j],term,&next),"boundary integer overflow");
       boundary[j]=next;
    }
 }
 check(boundary[0]==1 && boundary[1]==1,"integral Morse boundary");
 cout<<"INTEGRAL_MORSE_BOUNDARY_OK d7=(1,1) primitive=1\n";
}
int main(){build_graph();enumerate_faces();match_faces();verify_acyclicity();verify_morse_boundary();
 cout<<"ALL_CHECKS_PASS\n";
}
