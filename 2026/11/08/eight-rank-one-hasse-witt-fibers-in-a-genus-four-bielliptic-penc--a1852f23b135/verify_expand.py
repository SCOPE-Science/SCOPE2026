"""Exact independent Hasse--Witt extraction by sparse expansion over F_19."""
from collections import defaultdict
P = 19
E = ((1,1,1,2),(1,1,2,1),(1,2,0,1),(2,1,1,1))
# exponent order x,y,z,w,t; coefficients in F_19
cubic = [((0,2,1,0,0),1), ((3,0,0,0,0),-1), ((1,0,2,0,0),1)]
quadric = [((0,0,0,2,0),1), ((1,1,0,0,0),-1), ((0,0,2,0,1),-1)]

def multiply(f, terms):
    out = defaultdict(int)
    for a,ca in f.items():
        for b,cb in terms:
            v = tuple(a[i]+b[i] for i in range(5))
            out[v] = (out[v]+ca*cb)%P
    return {k:v for k,v in out.items() if v}

def power(terms, n):
    f = {(0,0,0,0,0):1}
    for _ in range(n): f = multiply(f, terms)
    return f

f = power(cubic, 18)
g = power(quadric, 18)
full = multiply(f, list(g.items()))
mat = []
for e in E:
    row=[]
    for d in E:
        mon=tuple(19*e[i]-d[i] for i in range(4))
        coeff={k[4]:v for k,v in full.items() if k[:4]==mon}
        row.append(coeff)
    mat.append(row)

expected=[[{}, {}, {}, {}],
          [{}, {3:-49,7:-7}, {}, {5:56,9:7}],
          [{}, {}, {}, {}],
          [{}, {1:7,5:-7}, {}, {3:7}]]
normalize=lambda d:{k:v%P for k,v in d.items() if v%P}
assert [[normalize(a) for a in row] for row in mat]==[[normalize(a) for a in row] for row in expected],mat
print('VERIFY_OK: independently expanded (P Q)^18; 16 Hasse--Witt entries and all coefficients match')
print('P terms',len(f),'Q terms',len(g),'product terms',len(full))
