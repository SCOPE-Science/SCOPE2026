// Independent whole-space check: inspect all 2^16 binary 4-by-4 matrices.
#include <array>
#include <cassert>
#include <cstdio>
#include <map>
using namespace std;
using Mat = array<unsigned,4>;
Mat multiply(Mat a, Mat b){Mat o{};for(int i=0;i<4;i++)for(int k=0;k<4;k++)if(a[i]>>k&1) o[i]^=b[k];return o;}
int rank_binary(Mat a){int r=0;for(int c=0;c<4;c++){int i=r;while(i<4&&!(a[i]>>c&1))i++;if(i==4)continue;swap(a[r],a[i]);for(int j=r+1;j<4;j++)if(a[j]>>c&1)a[j]^=a[r];r++;if(r==4)break;}return r;}
int main(){const Mat A={4,8,0,0}; map<pair<int,int>,int> C;for(unsigned x=0;x<(1U<<16);x++){
 Mat B{};for(int i=0;i<4;i++)B[i]=(x>>(4*i))&15;
 if(multiply(B,B)!=Mat{})continue;
 Mat AB=multiply(A,B);if(AB!=multiply(B,A))continue;
 C[{rank_binary(AB),rank_binary(B)}]++;
}
map<pair<int,int>,int> expected={{{0,0},1},{{0,1},9},{{0,2},6},{{1,2},12}};
assert(C==expected);for(auto [p,v]:C)printf("rank_AB=%d rank_B=%d count=%d\n",p.first,p.second,v);
puts("FULL_MATRIX_SPACE_GF2_PASS");}
