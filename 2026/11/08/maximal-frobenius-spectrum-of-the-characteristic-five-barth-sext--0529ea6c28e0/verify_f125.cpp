#include <cstdio>
#include <cstdint>
static int add[125][125],sub[125][125],mul[125][125],sq[125],neg[125];
int v(int a,int b,int c){return a+5*b+25*c;}
void init(){
 for(int i=0;i<125;i++){
  int a=i%5,b=(i/5)%5,c=i/25; neg[i]=v((5-a)%5,(5-b)%5,(5-c)%5);
  for(int j=0;j<125;j++){
   int d=j%5,e=(j/5)%5,f=j/25;
   add[i][j]=v((a+d)%5,(b+e)%5,(c+f)%5);
   int cc[5]={a*d,a*e+b*d,a*f+b*e+c*d,b*f+c*e,c*f};
   // alpha^3=-alpha-1, alpha^4=-alpha^2-alpha
   cc[0]-=cc[3];cc[1]-=cc[3]+cc[4];cc[2]-=cc[4];
   auto mod=[](int k){return (k%5+5)%5;};
   mul[i][j]=v(mod(cc[0]),mod(cc[1]),mod(cc[2]));
  }
 }
 for(int i=0;i<125;i++) {for(int j=0;j<125;j++)sub[i][j]=add[i][neg[j]];sq[i]=mul[i][i];}
}
inline bool e(int x,int y,int z,int w){
 int a=sq[x],b=sq[y],c=sq[z],d=sq[w];
 int P=mul[mul[add[a][b]][add[b][c]]][add[c][a]];
 int K=sub[add[add[a][b]][c]][d];
 return P==mul[2][mul[mul[K][K]][d]];
}
int main(){init();long long count=0;int q=125;
 for(int x=0;x<q;x++)for(int y=0;y<q;y++)for(int z=0;z<q;z++) count+=e(x,y,z,1);
 for(int x=0;x<q;x++)for(int y=0;y<q;y++)count+=e(x,y,1,0);
 for(int x=0;x<q;x++) count+=e(x,1,0,0);
 count+=e(1,0,0,0);
 printf("F125 count %lld predicted 17251\n",count);
 return count==17251?0:1;
}
