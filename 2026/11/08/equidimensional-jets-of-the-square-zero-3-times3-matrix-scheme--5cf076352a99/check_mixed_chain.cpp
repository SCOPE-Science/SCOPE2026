// Exhaustive mixed-characteristic cross-check over Z/p^m (not truncated-polynomial arithmetic).
#include <array>
#include <vector>
#include <iostream>
#include <cstdint>
using namespace std;
using Mat=array<int,9>;
uint64_t power(int p,int e){uint64_t r=1;while(e--)r*=p;return r;}
Mat decode(uint64_t code,int radix){Mat m{};for(int j=0;j<9;j++){m[j]=int(code%radix);code/=radix;}return m;}
bool zero_square(const Mat& x,int mod){for(int i=0;i<3;i++)for(int j=0;j<3;j++){int s=0;for(int k=0;k<3;k++)s+=x[3*i+k]*x[3*k+j];if(s%mod)return false;}return true;}
int main(){for(auto [p,m]:vector<pair<int,int>>{{2,2},{2,3},{3,2}}){int mod=int(power(p,m));vector<Mat> residues;
 for(int a=0;a<power(p,9);a++){auto x=decode(a,p);if(zero_square(x,p))residues.push_back(x);}
 uint64_t lifts=power(p,9*(m-1)),total=0;
 for(const auto& z:residues){for(uint64_t l=0;l<lifts;l++){auto a=decode(l,power(p,m-1));Mat x{};for(int i=0;i<9;i++)x[i]=z[i]+p*a[i];if(zero_square(x,mod))total++;}}
 uint64_t N=(uint64_t)(p*p+p+1)*(p*p-1);uint64_t exp=(m==2)?power(p,9)+N*power(p,5):power(p,9)*(1+2*N);
 cout<<"ring=Z/"<<mod<<" candidates="<<residues.size()*lifts<<" square_zero="<<total<<" expected="<<exp<<"\n";if(total!=exp)return 1;}
 cout<<"ALL_3X3_SQUAREZERO_MIXED_CHARACTERISTIC_TESTS_PASS\n";
}
