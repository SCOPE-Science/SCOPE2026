// Exact independent finite-field replay for smooth F_2-plane-filling quintic pencils.
// C++17, no external libraries. No randomness or external input.
#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;
struct E{int a,b,c;};
vector<E> mo;
int monIndex(int a,int b,int c){for(int j=0;j<(int)mo.size();j++)if(mo[j].a==a&&mo[j].b==b&&mo[j].c==c)return j;throw runtime_error("bad monomial");}
// Polynomial multiplication in characteristic 2: small monomial list (exponent tuple, bitset coefficients)
using Terms=set<array<int,3>>;
Terms prod(const Terms& a,const Terms& b){Terms r;for(auto i:a)for(auto j:b){array<int,3> t{i[0]+j[0],i[1]+j[1],i[2]+j[2]};auto it=r.find(t);if(it==r.end())r.insert(t);else r.erase(it);}return r;}
int transform(int mask, const array<int,3>& mat){
 Terms pow[3][6];
 for(int i=0;i<3;i++){
  Terms one;one.insert({0,0,0});pow[i][0]=one;
  Terms linear;
  for(int j=0;j<3;j++)if((mat[i]>>j)&1){array<int,3> e{0,0,0};e[j]=1;linear.insert(e);}
  for(int k=1;k<=5;k++)pow[i][k]=prod(pow[i][k-1],linear);
 }
 Terms out;
 for(int j=0;j<21;j++)if(mask>>j&1){E e=mo[j];Terms term=prod(prod(pow[0][e.a],pow[1][e.b]),pow[2][e.c]);for(auto t:term){auto it=out.find(t);if(it==out.end())out.insert(t);else out.erase(it);}}
 int result=0;for(auto t:out)result^=1<<monIndex(t[0],t[1],t[2]);return result;
}
struct Field{
 int r,q,mod;
 vector<uint16_t> mult;
 Field(int r_,int m):r(r_),q(1<<r),mod(m),mult(q*q){
  for(int a=0;a<q;a++)for(int b=0;b<q;b++){
   int v=0,aa=a,bb=b;
   while(bb){if(bb&1)v^=aa;aa<<=1;if(aa&q)aa^=mod;bb>>=1;}
   mult[a*q+b]=v;
  }
  for(int a=1;a<q;a++){
   int v=1;for(int j=0;j<q-1;j++)v=(*this)(v,a);
   if(v!=1)throw runtime_error("not field");
  }
 }
 inline int operator()(int a,int b)const{return mult[a*q+b];}
};
struct Deriv{int a,b,c,var;};
vector<Deriv> derivs(int p){vector<Deriv> ds;for(int j=0;j<21;j++)if(p>>j&1){auto e=mo[j];if(e.a&1)ds.push_back({e.a-1,e.b,e.c,0});if(e.b&1)ds.push_back({e.a,e.b-1,e.c,1});if(e.c&1)ds.push_back({e.a,e.b,e.c-1,2});}return ds;}
bool pointSing(const vector<Deriv>& ds,const Field& f,int X,int Y,int Z){
 int xp[6],yp[6],zp[6];xp[0]=yp[0]=zp[0]=1;
 for(int i=1;i<=5;i++){xp[i]=f(xp[i-1],X);yp[i]=f(yp[i-1],Y);zp[i]=f(zp[i-1],Z);}
 int gg[3]={0,0,0};
 for(auto d:ds)gg[d.var]^=f(f(xp[d.a],yp[d.b]),zp[d.c]);
 return !(gg[0]|gg[1]|gg[2]);
}
bool hasSing(const vector<Deriv>& ds, const Field& f){
 for(int Y=0;Y<f.q;Y++)for(int Z=0;Z<f.q;Z++)if(pointSing(ds,f,1,Y,Z))return true;
 for(int Z=0;Z<f.q;Z++)if(pointSing(ds,f,0,1,Z))return true;
 return pointSing(ds,f,0,0,1);
}
int main(){auto T0=chrono::steady_clock::now();
 for(int a=5;a>=0;a--)for(int b=5-a;b>=0;b--)mo.push_back({a,b,5-a-b});
 assert(mo.size()==21);
 map<int,int> piv;for(int X=0;X<2;X++)for(int Y=0;Y<2;Y++)for(int Z=0;Z<2;Z++)if(X||Y||Z){int row=0;for(int j=0;j<21;j++){auto e=mo[j];if((!e.a||X)&&(!e.b||Y)&&(!e.c||Z))row^=1<<j;}while(row){int i=__builtin_ctz((unsigned)row);auto it=piv.find(i);if(it==piv.end()){piv[i]=row;break;}row^=it->second;}}
 vector<int> freecols,basis;
 for(int i=0;i<21;i++)if(!piv.count(i))freecols.push_back(i);
 assert(freecols.size()==14);
 for(int i:freecols){int b=1<<i;for(auto it=piv.rbegin();it!=piv.rend();it++)if(__builtin_parity((unsigned)(b&it->second)))b^=1<<it->first;basis.push_back(b);}
 auto coord=[&](int p){int n=0;for(int i=0;i<14;i++)if(p>>freecols[i]&1)n|=1<<i;return n;};
 vector<int> full(1<<14);for(int n=1;n<(1<<14);n++){int i=__builtin_ctz((unsigned)n);full[n]=full[n^(1<<i)]^basis[i];}
 vector<vector<int>> act;
 for(array<int,3> mat:vector<array<int,3>>{{3,2,4},{2,1,4},{2,4,1}}){vector<int> c(14),A(1<<14);for(int i=0;i<14;i++)c[i]=coord(transform(basis[i],mat));for(int n=1;n<(1<<14);n++){int i=__builtin_ctz((unsigned)n);A[n]=A[n^(1<<i)]^c[i];}act.push_back(move(A));}
 vector<char> visited(1<<14),good(1<<14);vector<vector<int>> orbits;
 for(int n=1;n<(1<<14);n++)if(!visited[n]){vector<int> Q{n};visited[n]=1;for(int idx=0;idx<(int)Q.size();idx++){int u=Q[idx];for(auto& A:act)if(!visited[A[u]]){visited[A[u]]=1;Q.push_back(A[u]);}}orbits.push_back(move(Q));}
 assert(orbits.size()==139);
 const int irr[11]={0,0x3,0x7,0xb,0x13,0x25,0x43,0x83,0x11b,0x203,0x409};
 vector<Field> fields;for(int r=1;r<=10;r++)fields.emplace_back(r,irr[r]);
 vector<int> sm;vector<int> classid(1<<14,-1);int nclass=0;
 for(auto& orb:orbits){int repr=*min_element(orb.begin(),orb.end());vector<Deriv> ds=derivs(full[repr]);bool smooth=true;
  for(const auto& f:fields)if(hasSing(ds,f)){smooth=false;break;}
  if(smooth){for(int v:orb){good[v]=1;sm.push_back(v);classid[v]=nclass;}++nclass;}
 }
 sort(sm.begin(),sm.end());assert(sm.size()==1512 && nclass==10);
 set<array<int,3>> pencils;
 for(int a:sm)for(int b:sm)if(a<b){int c=a^b;if(c>b && good[c])pencils.insert({a,b,c});}
 assert(pencils.size()==16800);
 long long allsame=0,twosame=0,allvariant=0;
 for(auto p:pencils){int a=classid[p[0]],b=classid[p[1]],c=classid[p[2]];if(a==b && b==c)allsame++;else if(a==b || b==c || a==c)twosame++;else allvariant++;}
 assert(allsame==672 && twosame==3024 && allvariant==13104);
 set<array<int,3>> used;
 map<int,int> sizeDist;int pc=0;int same=0;int classified=0;
 for(auto p:pencils)if(!used.count(p)){
  queue<array<int,3>> Q;Q.push(p);used.insert(p);int cnt=0;
  while(!Q.empty()){auto x=Q.front();Q.pop();cnt++;
   for(auto& A:act){array<int,3> y{A[x[0]],A[x[1]],A[x[2]]};sort(y.begin(),y.end());if(used.insert(y).second)Q.push(y);}}
  sizeDist[cnt]++;pc++;
 }
 assert(pc==108);assert(sizeDist[168]==96 && sizeDist[56]==12);
 // Base-point differential argument: for any fixed rational point P, gradient of
 // U->T*_P P^2 is a linear map into a two-dimensional F2 space, so dim U<=2.
 cout<<"F2_FILLING_QUINTIC_PENCILS_FIELD_PASS "<<full.size()<<" "<<orbits.size()<<" "<<sm.size()<<" "<<pencils.size()<<" "<<pc<<" "<<sizeDist[168]<<" "<<sizeDist[56]<<" "<<allsame<<" "<<twosame<<" "<<allvariant<<"\n";
 cerr<<"elapsed="<<chrono::duration_cast<chrono::milliseconds>(chrono::steady_clock::now()-T0).count()<<"ms\n";
}
