from itertools import product

def reduce_word(w):
 s=''.join(w)
 return None if ('ee' in s or 'qeq' in s) else s

def mul(a,b):
 return reduce_word(a+b)

def normals(N):
 return [''.join(w) for n in range(N+1) for w in product('eq',repeat=n) if reduce_word(w) is not None]

def check(N=9):
 W=normals(N)
 for n in range(1,N-1):
  z='e'+'q'*n+'e'
  assert z in W
  for t in 'eq':
   assert mul(t,z)==mul(z,t)==None
 # nonzero and independent in monomial quotient by forbidden subwords
 assert len(set('e'+'q'*n+'e' for n in range(1,N-1)))==N-2
 print('VERIFY_OK')
check()
