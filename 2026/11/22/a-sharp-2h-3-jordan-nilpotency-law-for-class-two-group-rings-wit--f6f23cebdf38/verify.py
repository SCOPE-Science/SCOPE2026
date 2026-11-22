"""Exact cyclic convolution tests for nilpotent Jordan products in cyclic-order-four derived group rings."""
import itertools

def mul(x,y,M):
 return tuple(sum(x[i]*y[(k-i)%4] for i in range(4))%M for k in range(4))

def u_power(n,M):
 v=(1,0,0,0); u=(1,1,0,0)
 for _ in range(n):v=mul(v,u,M)
 return v

def heis_mul(x,y):
 a,b,c=x;d,e,f=y
 return ((a+d)%4,(b+e)%4,(c+f+a*e)%4)

def heis_jordan(x,y,M):
 out={}
 for g,ag in x.items():
  for h,bh in y.items():
   for z in (heis_mul(g,h),heis_mul(h,g)):
    out[z]=(out.get(z,0)+ag*bh)%M
 return {g:v for g,v in out.items() if v}

def check():
 for h in range(1,9):
  M=2**h
  a=u_power(2*h+1,M); b=u_power(2*h+2,M)
  assert any(a) and not any(b),(h,a,b)
  # Exhaustively test the ideal-power claim via its monomial generators.
  for i in range(2*h+3):
   j=2*h+2-i
   x=tuple((2**i*t)%M for t in u_power(j,M))
   assert x==(0,0,0,0),(h,i,j,x)
  # The relevant power is nonzero because its coefficients retain 2-adic information.
  print(f'cyclic_h={h} last_nonzero={2*h+1} first_zero={2*h+2} OK')
 # Direct finite 64-element Heisenberg group witness over Z/4.
 M=4; identity=(0,0,0); a=(1,0,0);b=(0,1,0)
 v={(a):1}
 for length in range(2,8):
  v=heis_jordan(v,{b:1},M)
  assert bool(v)==(length<=6),(length,v)
 print('heisenberg_class_two_C4_h2_J6_nonzero_J7_zero_WITNESS_OK')
 # A sample of the universal upper bound, using arbitrary group words.
 sample=[(x,y,z) for x,y,z in itertools.product(range(4),repeat=3)]
 for k in range(25):
  seq=[sample[(k*17+i*37+3)%64] for i in range(7)]
  w={seq[0]:1}
  for g in seq[1:]:w=heis_jordan(w,{g:1},4)
  assert not w,(k,w)
 print('random_heisenberg_7_fold_Jordan_zero_25_checks_OK')
 print('VERIFY_OK')

if __name__=='__main__':check()
