#include <cstdio>
#include <cstdint>
#include <algorithm>
unsigned update(int n,unsigned s){unsigned o=0; int N=2*n; for(int i=0;i<N;i++){int a=(s>>((i+N-1)%N))&1,b=(s>>((i+1)%N))&1,c=(s>>((i+n)%N))&1; o|=((a+b+c>=2)?1u:0u)<<i;}return o;}
int main(){for(int n=3;n<=12;n++){unsigned N=2*n,T=1u<<N;uint64_t fix=0,per=0;for(unsigned s=0;s<T;s++){unsigned v=update(n,s);fix+=v==s;per+=update(n,v)==s;}printf("n=%d fix=%llu period<=2=%llu strict2states=%llu\n",n,(unsigned long long)fix,(unsigned long long)per,(unsigned long long)(per-fix));}}
