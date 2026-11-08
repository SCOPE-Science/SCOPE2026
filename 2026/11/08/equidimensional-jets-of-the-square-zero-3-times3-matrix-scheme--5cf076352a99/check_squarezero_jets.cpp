// Exhaustive direct matrix-product check for square-zero 3x3 matrices over F_q[t]/(t^m).
// Enumerates only residue matrices satisfying X_0^2=0, an exact necessary condition.
#include <iostream>
#include <array>
#include <vector>
#include <cstdint>
#include <cassert>
using namespace std;
using Mat=array<int,9>;
Mat decode(uint64_t z,int q){Mat a{};for(int i=0;i<9;i++){a[i]=int(z%q);z/=q;}return a;}
bool sqzero(const vector<Mat>& a,int q){int m=a.size();for(int d=0;d<m;d++){for(int i=0;i<3;i++)for(int j=0;j<3;j++){int sum=0;for(int h=0;h<=d;h++)for(int k=0;k<3;k++)sum+=a[h][3*i+k]*a[d-h][3*k+j];if(sum%q)return false;}}return true;}
uint64_t power(int q,int e){uint64_t ans=1;while(e--)ans*=q;return ans;}
uint64_t count_direct(int q,int m){
 uint64_t q9=power(q,9), answer=0;vector<Mat> good;
 for(uint64_t a=0;a<q9;a++){Mat M=decode(a,q);vector<Mat> x={M};if(sqzero(x,q))good.push_back(M);}
 uint64_t lifts=power(q,9*(m-1));
 vector<Mat> x(m);for(const Mat& base:good){x[0]=base;for(uint64_t word=0;word<lifts;word++){
   uint64_t rem=word;for(int d=1;d<m;d++){uint64_t digit=rem%q9;rem/=q9;x[d]=decode(digit,q);}if(sqzero(x,q))answer++;
 }}
 cout << "q="<<q<<" m="<<m<<" allowed_residues="<<good.size()<<" tested="<<(good.size()*lifts)<<" count="<<answer<<"\n";
 return answer;
}
int main(){for(auto [q,m]:vector<pair<int,int>>{{2,1},{3,1},{5,1},{2,2},{3,2},{2,3}}){uint64_t N=(uint64_t(q*q+q+1))*(q*q-1),expected;
 if(m%2==0){int h=m/2;expected=power(q,9*h)+(uint64_t)h*N*power(q,9*h-4);}
 else {int h=(m-1)/2;expected=power(q,9*h)*(1+(uint64_t)(h+1)*N);}
 uint64_t got=count_direct(q,m);if(got!=expected){cerr<<"FAIL expected="<<expected<<"\n";return 1;}}
 cout<<"ALL_3X3_SQUAREZERO_JET_EXHAUSTIVE_TESTS_PASS\n";
}
