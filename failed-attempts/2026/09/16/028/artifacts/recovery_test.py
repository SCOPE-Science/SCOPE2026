"""Bounded recovery test: exhibit non-vacuous hypothesis tuple + isolate primitivity gap.
No external libs; brute point-counts for a_p(E)=0, Kronecker inert, N^- parity.
"""
def kronecker(D, n):
    # Kronecker symbol (D/n) for odd prime n not dividing D, plus n=2 handling; D fundamental discriminant
    if n == 2:
        d = D % 16
        # (2/|D|)-type: for odd D: 0 if even, else 1 if D=+-1 mod8, -1 if +-3 mod8
        if D % 2 == 0:
            return 0
        r = D % 8
        if r in (1, 7):
            return 1
        else:
            return -1
    # odd prime: Legendre
    a = D % n
    if a == 0:
        return 0
    return 1 if pow(a, (n-1)//2, n) == 1 else -1

def ap_of_curve(a1,a2,a3,a4,a6,p):
    # count affine points mod p then add infinity
    n = 1  # infinity
    for x in range(p):
        rhs = (x**3 + a2*x**2 + a4*x + a6) % p  # short form handling below generalized below
        # general Weierstrass: y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6
        # count y in F_p
        c = 0
        for y in range(p):
            if (y*y + (a1*x+a3)*y - rhs) % p == 0:
                c += 1
        n += c
    return p + 1 - n

# Candidate semistable curves (squarefree conductor), given as [a1,a2,a3,a4,a6] minimal models
# 11a1: [0,-1,1,0,0]? Actually 11a1 = [0,-1,1,-10,-20]? Let's use standard minimal models:
curves = {
    # label: (N0, [a1,a2,a3,a4,a6])
    "11a1": (11, [0,-1,1,-10,-20]),
    "14a1": (14, [1,0,0,4,0]),       # check: 14.a1 = [1,0,0,-72,-224]? use alternative below
    "15a1": (15, [1,1,1,-10,-10]),
    "17a1": (17, [1,-1,1,-1,-14]),
    "19a1": (19, [0,1,1,-9,-15]),
    "26a1": (26, [1,1,0,-2,0]),
    "30a1": (30, [1,0,1,-36,0]),
    "33a1": (33, [0,-1,1,-114,-1131]),
    "34a1": (34, [1,0,0,-16,0]),
    "35a1": (35, [0,1,1,9,0]),
}
# More reliable: use short models y^2 = x^3 + Ax + B with squarefree conductor candidates
short = {
    "11a-short?": (11, -1, 0),
    "14a": (14, -15, 18),
    "15a": (15, -7, 6),
    "30a": (30, -3, 2),
    "34a": (34, -75, -250),
    "35a": (35, -27, -42),
}

def ap_short(A,B,p):
    n=1
    for x in range(p):
        rhs=(x**3+A*x+B)%p
        for y in range(p):
            if (y*y-rhs)%p==0:
                # count: loop counts each y; fine
                pass
        # faster: number of y = 1+Legendre(rhs)
        if rhs==0:
            n+=1
        else:
            n+=1+ (1 if pow(rhs,(p-1)//2,p)==1 else -1)
    return p+1-n

print("short-model a_p table for p=5,7,13:")
for label,(N,A,B) in short.items():
    disc = -16*(4*A**3+27*B**2)
    aps={}
    for p in [5,7,13,17,19]:
        if disc%p==0:
            aps[p]='bad'
        else:
            aps[p]=ap_short(A,B,p)
    print(label, "N=",N, "disc=",disc, aps)

print()
print("general-model a_p for Cremona minimal models:")
for label,(N,ainv) in curves.items():
    a1,a2,a3,a4,a6=ainv
    aps={}
    for p in [5,7,13]:
        aps[p]=ap_of_curve(a1,a2,a3,a4,a6,p)
    print(label, aps)

# Now search K discriminants for a chosen (E,p): we will pick from results.
print()
print("Kronecker search for E=30a-like N0=30, p=5 (need p inert, all ell|N0 split, (D,N0p)=1):")
N0=30
p=5
fund_discs=[-3,-4,-7,-8,-11,-19,-43,-67,-163,-7*4,-11*4,-19*4,-23,-31,-47,-59,-71,-79,-83,-103,-107,-115,-123,-131,-139,-151,-167,-179,-191,-227,-251]
# fundamental discriminants (negative, ≡0,1 mod4, squarefree part): filter
def is_fund(D):
    if D>=0: return False
    if D%4==1:
        # squarefree
        import math
        n=-D
        for q in range(2,int(n**0.5)+1):
            if n%(q*q)==0: return False
        return True
    elif D%4==0:
        m=D//4
        if m%4 in (2,3):
            import math
            n=-m
            for q in range(2,int(n**0.5)+1):
                if n%(q*q)==0: return False
            return True
    return False

cands=[D for D in range(-300,-1) if is_fund(D)]
for D in cands:
    import math
    if math.gcd(D,N0*p)!=1: continue
    if kronecker(D,p)!=-1: continue
    Nminus=[ell for ell in [2,3,5] if kronecker(D,ell)==-1]
    if len(Nminus)%2==1: continue
    print(f"D={D} inert@5, N^- primes={Nminus} (count {len(Nminus)}, even OK)")
    if len(Nminus)==0:
        print("  ^ N^- =1 (empty product) example")
        break
