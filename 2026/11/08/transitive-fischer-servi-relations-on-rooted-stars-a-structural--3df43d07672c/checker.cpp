// Exhaustive independent finite check of the rooted-star confluence count.
// Compile: c++ -std=c++17 -O3 star_checker.cpp -o star_checker && ./star_checker
#include <cstdio>
#include <cstdint>
#include <cstdlib>
#include <vector>
#include <array>
using namespace std;
static bool transitive(const int *rows,int n){
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(rows[i]&(1<<j))if(rows[j]&~rows[i])return false;
 return true;
}
static bool satisfies(const int *row,int m){
 int n=m+1;
 if(!transitive(row,n))return false;
 for(int i=1;i<n;i++){
  if((row[0]&1)&&!row[i])return false;
  if((row[i]&row[0]&~1)!=(row[0]&~1))return false;
 }
 for(int i=1;i<n;i++)if(row[i]&1)if((row[i]&~1)!=(((1<<n)-1)&~1))return false;
 if(row[0]&1){
  int all=0;for(int i=0;i<n;i++)all|=row[i];
  if((all&~1)!=(((1<<n)-1)&~1))return false;
 }
 return true;
}
int main(){
 const int target[]={2,8,38,379,7182};
 for(int m=0;m<=4;m++){
  int n=m+1;uint64_t lim=1ULL<<(n*n),count=0;
  int row[5];
  for(uint64_t z=0;z<lim;z++){
   for(int i=0;i<n;i++)row[i]=(int)((z>>(i*n))&((1<<n)-1));
   if(satisfies(row,m))count++;
  }
  if(count!=(uint64_t)target[m]){printf("FAIL m=%d got=%llu expected=%d\n",m,(unsigned long long)count,target[m]);return 1;}
  printf("m=%d count=%llu exhaustive_matrices=%llu\n",m,(unsigned long long)count,(unsigned long long)lim);
 }
 puts("ROOTED_STAR_TRANSITIVE_CONFLUENCE_OK");
}
