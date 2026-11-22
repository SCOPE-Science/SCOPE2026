// A standalone, finite exhaustive certificate for the stated binary
// two-step length-three palindromic-duplication capacities.
// Standard C++17 only. No external mathematics library or solver.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

// Position zero of the source is the low bit. Operation: x=U V Z,
// |U|=i, |V|=3; replace x with U V reverse(V) Z.
static uint32_t duplicate_bits(uint32_t x, unsigned i) {
  const uint32_t original_prefix_mask=(1u << (i+3))-1u;
  const uint32_t triple=(x>>i)&7u;
  const uint32_t reversed=((triple&1u)<<2)|(triple&2u)|((triple&4u)>>2);
  return (x&original_prefix_mask) | (reversed<<(i+3)) |
         ((x>>(i+3))<<(i+6));
}
static string bitword(uint32_t x,unsigned n){
 string s; for(unsigned i=0;i<n;++i)s.push_back(char('0'+((x>>i)&1u))); return s;
}
static string duplicate_reference(const string &w,unsigned i){
 const string t=w.substr(i,3);return w.substr(0,i+3)+string(t.rbegin(),t.rend())+w.substr(i+3);
}
static unsigned exact_sphere(uint32_t x,unsigned n,vector<uint32_t>& outputs){
 size_t p=0;
 for(unsigned i=0;i+3<=n;i++){
  const auto y=duplicate_bits(x,i);
  for(unsigned j=0;j+3<=n+3;j++)outputs[p++]=duplicate_bits(y,j);
 }
 if(p!=size_t(n-2)*(n+1))throw runtime_error("history boundary");
 sort(outputs.begin(),outputs.end());
 return unsigned(unique(outputs.begin(),outputs.end())-outputs.begin());
}
static void check_reference(){
 // The string construction is independent of bitwise packing and the sort.
 uint64_t tested=0;
 for(unsigned n=3;n<=10;n++){
  vector<uint32_t> a(size_t(n-2)*(n+1));
  for(uint32_t x=0;x<(1u<<n);x++){
   string w=bitword(x,n);vector<string> direct;
   for(unsigned i=0;i+3<=n;i++){
    const string first=duplicate_reference(w,i);
    if(first!=bitword(duplicate_bits(x,i),n+3))throw runtime_error("first-step mismatch");
    for(unsigned j=0;j+3<=n+3;j++){
     string second=duplicate_reference(first,j);
     if(second!=bitword(duplicate_bits(duplicate_bits(x,i),j),n+6))
      throw runtime_error("second-step mismatch");
     direct.push_back(second);
    }
   }
   sort(direct.begin(),direct.end());
   auto direct_count=unsigned(unique(direct.begin(),direct.end())-direct.begin());
   if(direct_count!=exact_sphere(x,n,a))throw runtime_error("reference cardinality mismatch");
   tested++;
  }
 }
 cout<<"REFERENCE_OK words="<<tested<<" n=3..10\n";
}
int main(int argc,char**argv){
 try{
  check_reference();
  const unsigned N=argc>=2?unsigned(stoul(argv[1])):22;
  if(N<3||N>22)throw runtime_error("domain is 3..22");
  const unsigned expected[]={0,0,0,4,9,16,24,32,41,51,62,74,87,101,
                             116,132,149,167,186,206,227,249,272};
  const unsigned expect_n[]={0,0,0,2,4,4,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2};
  uint64_t checked=0;
  for(unsigned n=3;n<=N;n++){
   vector<uint32_t> outputs(size_t(n-2)*(n+1));
   unsigned best=0;uint64_t number=0;uint32_t first=0;
   // Complement symmetry: T_i(1-x)=1-T_i(x), at each length;
   // each complementary pair has one source with low bit zero.
   for(uint32_t x=0;x<(1u<<n);x+=2){
     const unsigned count=exact_sphere(x,n,outputs);
     if(count>best){best=count;number=2;first=x;}
     else if(count==best){number+=2;}
     ++checked;
   }
   if(best!=expected[n] || number!=expect_n[n])throw runtime_error("theorem mismatch");
   if(n>=6){
     if(best!=n*(n+3)/2-3)throw runtime_error("formula mismatch");
     // Since exactly two sources maximize, verify the conjectured phase
     // word is one, and its bitwise complement is necessarily the other.
     uint32_t periodic=0;
     const string template_word="0110";
     for(unsigned i=0;i<n;++i)periodic|=uint32_t(template_word[i%4]-'0')<<i;
     if(exact_sphere(periodic,n,outputs)!=best)throw runtime_error("optimizer mismatch");
   }
   cout<<"n="<<n<<" maximum="<<best<<" maximizers="<<number
       <<" example="<<bitword(first,n)<<"\n";
  }
  cout<<"EXHAUSTIVE_PASS complement_representatives="<<checked
      <<" lengths=3.."<<N<<"\n";
 }catch(const exception&e){cerr<<"FAIL: "<<e.what()<<"\n";return 1;}
}
