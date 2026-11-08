// Independent finite enumeration of strict graph-burning source schedules on cycles.
// Compile: g++ -std=c++17 -O2 direct_exhaustive.cpp -o direct_exhaustive
#include <bits/stdc++.h>
using namespace std;
static int k,n;
static uint64_t fullmask,balls[8][40];
static vector<int> seq;
static vector<uint64_t> feasible;
static uint64_t encode(const vector<int> &p){uint64_t u=0;for(int v:p)u=u*n+v;return u;}
static void generate(int level,uint64_t cover){
 if(level==k){if(cover==fullmask)feasible.push_back(encode(seq));return;}
 for(int v=0;v<n;v++){
  bool legal=true;
  for(int j=0;j<level;j++){
   int d=abs(v-seq[j]);d=min(d,n-d);
   if(d<level-j){legal=false;break;}
  }
  if(legal){seq[level]=v;generate(level+1,cover|balls[level][v]);}
 }
}
int main(){
 for(k=3;k<=5;k++){
  n=k*k-2;seq.assign(k,0);feasible.clear();fullmask=(1ull<<n)-1;
  for(int i=0;i<k;i++)for(int x=0;x<n;x++){
   uint64_t m=0;for(int y=0;y<n;y++)if(min(abs(x-y),n-abs(x-y))<=k-1-i)m|=1ull<<y;
   balls[i][x]=m;
  }
  generate(0,0);
  unordered_map<uint64_t,int> index;index.reserve(feasible.size()*2);
  for(size_t i=0;i<feasible.size();i++)index.emplace(feasible[i],(int)i);
  if(index.size()!=feasible.size())throw runtime_error("duplicates");
  vector<int> seen(feasible.size());map<int,int> degrees,components;long long degsum=0;
  for(size_t i=0;i<feasible.size();i++){
   uint64_t tmp=feasible[i];vector<int> p(k);
   for(int j=k-1;j>=0;j--){p[j]=tmp%n;tmp/=n;}
   int d=0;
   for(int j=0;j<k;j++)for(int h:{-1,1}){
    vector<int> q=p;q[j]=(q[j]+h+n)%n;
    if(index.count(encode(q)))d++;
   }
   degrees[d]++;degsum+=d;
  }
  for(size_t i=0;i<feasible.size();i++)if(!seen[i]){
   queue<int> bfs;bfs.push((int)i);seen[i]=1;int sz=0;
   while(!bfs.empty()){
    int v=bfs.front();bfs.pop();sz++;
    uint64_t tmp=feasible[v];vector<int> p(k);
    for(int j=k-1;j>=0;j--){p[j]=tmp%n;tmp/=n;}
    for(int j=0;j<k;j++)for(int h:{-1,1}){
     vector<int> q=p;q[j]=(q[j]+h+n)%n;
     auto it=index.find(encode(q));if(it!=index.end()&&!seen[it->second]){
      seen[it->second]=1;bfs.push(it->second);
     }
    }
   }
   components[sz]++;
  }
  long long fact=1;for(int j=1;j<k;j++)fact*=j;
  long long type=(k*k+k-4)/2;
  if((long long)feasible.size()!=n*fact*type || degrees[2]!=n*fact*(k-1)
    || degrees[3]!=n*fact*2 || degrees[4]!=n*fact*(k*k-k-6)/2
    || degsum/2!=n*fact*(k*k-4) || components.size()!=1
    || components[n*type]!=fact)throw runtime_error("theoretical comparison failed");
  cout<<"k="<<k<<" n="<<n<<" schedules="<<feasible.size()<<" degrees={2:"<<degrees[2]<<",3:"<<degrees[3]<<",4:"<<degrees[4]<<"} components="<<fact<<"x"<<n*type<<" edges="<<degsum/2<<" PASS\n";
 }
 cout<<"DIRECT_EXHAUSTIVE_OK\n";
}
