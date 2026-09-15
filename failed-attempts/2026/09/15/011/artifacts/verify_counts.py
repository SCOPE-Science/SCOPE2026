"""Verify lattice-count obstruction for stabilized ellipsoid lower bound.
For integers a,b and t>=1, S=s*t with s=(a+b-1)/2:
  C_a(a*t) = #{(m,n): m+a*n <= a*t}
  C_b(S)   = #{(m,n): m+b*n <= S}
Checks C_b(S) >= C_a(a*t), which implies N_{k}(1,b)<=S, N_k(1,a)=a*t
for k=C_a(a*t)-1, hence c^N >= a*t/S = a/s.
Also checks analytic lower bound C_b(S) >= S^2/(2b)+S/2 and gap 4(s^2-a*b)>=1.
"""
import math

def C_count(T, b):
    # #{(m,n)>=0 : m + b*n <= T}, T real
    if T < 0: return 0
    Q = int(math.floor(T / b + 1e-12))
    c = 0
    for n in range(Q+1):
        c += int(math.floor(T - b*n + 1e-12)) + 1
    return c

def check_pair(a, b, t):
    s = (a + b - 1) / 2
    S = s * t
    Ca = C_count(a*t, a)
    Cb = C_count(S, b)
    # exact formula for Ca
    Ca_exact = a*t*(t+1)//2 + (t+1)
    assert Ca == Ca_exact, (a, t, Ca, Ca_exact)
    lb = S**2/(2*b) + S/2
    assert Cb + 1e-9 >= lb, (a,b,t,Cb,lb)
    return Ca, Cb, lb

def t0_bound(a, b):
    s = (a+b-1)/2
    L = (a - s + 2)/2
    # smallest t with t^2/(8b) - L*t - 1 >= 0
    import math
    A = 1/(8*b)
    disc = L*L + 4*A*1
    return int(math.ceil((L + math.sqrt(disc))/(2*A)))

pairs = [(6,2),(8,2),(10,2),(20,2),(9,3),(11,3),(13,3),(9,4),(10,4),(12,4),
         (9,5),(11,5),(12,6),(14,6),(16,6),(10,6),(17,9),(18,10),(25,9)]
for (a,b) in pairs:
    if (a-b) % 2 != 0: continue
    if a < b+1+2*math.sqrt(b) - 1e-9: continue
    s=(a+b-1)/2
    gap4 = (a+b-1)**2 - 4*a*b  # =4(s^2-ab)
    assert gap4 >= 1, (a,b,gap4)
    t0 = t0_bound(a,b)
    Ca,Cb,lb = check_pair(a,b,t0)
    ok = Cb >= Ca
    print(f"a={a:3d} b={b:2d} s={s:6.1f} gap4={gap4:5d} t0={t0:4d} Ca={Ca:7d} Cb={Cb:7d} holds={ok} ratio={a/s:.5f}")
    assert ok
print("ALL CHECKS PASSED")
