import math

c = 7.0/8.0
s = math.sqrt(15.0)/8.0

def p(t):
    return 7.0*t**3 - 12.0*t**2 + 4.0

def bisect(lo, hi, n=100):
    flo = p(lo)
    for _ in range(n):
        mid = 0.5*(lo+hi)
        fm = p(mid)
        if flo*fm <= 0.0:
            hi = mid
        else:
            lo = mid
            flo = fm
    return 0.5*(lo+hi)

tau = bisect(0.75, 0.80)
qstar = math.sqrt(1.0 + tau*tau - 2.0*c*tau)
F0prime = -tau*tau*(1.0 + (tau-c)/qstar)
K = -(s*s)*tau**5 / ((1.0-tau*tau)*(2.0*tau*tau+1.0))
R = s*tau*tau/(1.0+tau)

def step(t,b):
    q = math.sqrt(1.0+t*t-2.0*c*t+s*s*t*t*b*b)
    return 1.0/(t+q), t*b

def metrics(t,b):
    q = math.sqrt(1.0+t*t-2.0*c*t+s*s*t*t*b*b)
    r = t*b*s/(1.0+t+q+t*b*s)
    h = math.sqrt(1.0+b*b)
    pa = math.acos((t-c)/q)
    pb = math.acos((1.0-t*c)/q)
    return q,r,h,pa,pb

print(f"tau={tau:.15f}")
print(f"1/tau={1.0/tau:.15f}")
print(f"tau^2={tau*tau:.15f}")
print(f"p(tau)={p(tau):.3e}")
print(f"F0'(tau)={F0prime:.15f}")
print(f"K_pred={K:.15f}")
print(f"R_pred=lim r_n/b_n={R:.15f}")
print(f"quality_growth_pred=1/tau={1.0/tau:.15f}")
print()

initials = [
    ("paper-seed", 0.75, 0.25),
    ("corner", 0.80, 0.25),
    ("interior-1", 0.77, 0.10),
    ("interior-2", 0.79, 0.05),
]

for name,t,b in initials:
    prev_quality = None
    for n in range(41):
        q,r,h,pa,pb = metrics(t,b)
        quality = h/r
        if n == 40:
            kval = (t-tau)/(b*b)
            print(name)
            print(f"  t_40={t:.15f}")
            print(f"  b_40={b:.15e}")
            print(f"  (t_40-tau)/b_40^2={kval:.15f}")
            print(f"  r_40/b_40={r/b:.15f}")
            print(f"  theta_PA-2 theta_PB={pa-2.0*pb:.3e}")
            if name == "paper-seed":
                Cb = b/(tau**n)
                print(f"  b_40/tau^40={Cb:.15f}")
                print(f"  h/r={quality:.12e}")
        prev_quality = quality
        t,b = step(t,b)
    print()

# Consecutive ratio check for the paper seed.
t,b = 0.75,0.25
vals=[]
for n in range(42):
    q,r,h,pa,pb = metrics(t,b)
    vals.append((t,b,r,h/r,math.atan(t*b)))
    t,b = step(t,b)
for n in (20,30,40):
    t0,b0,r0,q0,a0=vals[n]
    t1,b1,r1,q1,a1=vals[n+1]
    print(f"n={n}: b-ratio={b1/b0:.15f}, r-ratio={r1/r0:.15f}, quality-ratio={q1/q0:.15f}, angle-ratio={a1/a0:.15f}")
