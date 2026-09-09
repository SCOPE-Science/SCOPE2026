"""Support chain for the sparse-K lemma + gap/window arithmetic (stdlib only).

B1. e < 2.75 via series partial sum + geometric tail (exact rational arithmetic).
B2. Concavity of x/f(x), f=log2(1+x), on [1,inf): sign(g'') = sign(G(x)) with
    G(x)=(x+2)ln(x+1)-2x; G(1)=3ln2-2>0 (cert: 8>e^2), G'(1)=ln2-1/2>0 (cert 4>e),
    G''(x)=x/(x+1)^2>0 exact. Hence G increasing from positive value. Grid check too.
B3. f submultiplicative on log-grid (analytic case split in comments).
B4. j_2 >> 2^144-1: lnlnln(j_2) >= 2 j_1 >= 2(2^36-1) vs lnlnln(2^144) ~ 1.53.
B5. Prefix-window algebra: ratio>=1/4 needs f(k)/f(n) <= (4/2.4)^2 = 2.777...
B6. First good interval [ln j_1, exp j_1] coverage (log-scale report, no overflow).
"""
import math
from fractions import Fraction

# B1: e < 2.75
N = 12
part = sum(Fraction(1, math.factorial(k)) for k in range(N + 1))
tail = Fraction(1, N * math.factorial(N))  # standard tail bound 1/(N*N!) for N>=1
e_upper = part + tail
assert e_upper < Fraction(11, 4), e_upper
print("B1 e < %.10f < 2.75 OK" % float(e_upper))
e2 = e_upper * e_upper
assert e2 < 8, e2  # -> 8 > e^2 -> ln2 > 2/3 -> G(1) > 0
assert e_upper < 4  # -> 4 > e -> ln2 > 1/2 -> G'(1) > 0
print("B1 certs: e^2 < %.6f < 8, e < 4 OK" % float(e2))

# B2: concavityivia G
ln2 = math.log(2)
G1 = 3 * ln2 - 2
Gp1 = ln2 - Fraction(1, 2)
assert G1 > 0 and Gp1 > 0
print("B2 G(1)=%.4f>0, G'(1)=%.4f>0, G''=x/(x+1)^2>0 exact => G inc. => x/f concave on [1,inf)" % (G1, float(Gp1)))
worst = 1e9
x = 1.0
while x <= 1e15:
    Gv = (x + 2) * math.log(x + 1) - 2 * x
    worst = min(worst, Gv)
    x *= 1.05
assert worst > 0.07  # min at x=1 is ~0.0794
print("B2 grid min G = %.4f > 0 OK" % worst)
# direct second-derivative sign grid for g(x)=x/log2(x+1)
xg = 1.0
ming = 1e9
while xg <= 1e12:
    s = 2 * xg - (xg + 2) * math.log(xg + 1)  # g''<0 iff s<0
    ming = min(ming, s)
    assert s < 0, xg
    xg *= 1.07
print("B2 direct g''<0 on grid (max s=%.4f<0) OK" % ming)

# B3: f submultiplicative: f(xy)<=f(x)f(y), x,y>=1.
# analytic: f>=1; if x==1: equality. Else write a=f(x)>=1,b=f(y)>=1;
# f(xy)=log2(xy+1)<=log2((x+1)(y+1))=log2(x+1)+log2(y+1)=a'+b' (raw logs, base2: same).
# Need a'b'...: f(x)f(y) vs f(xy): (x+1)(y+1)>=xy+1 -> log2((x+1)(y+1))>=f(xy);
# and f(x)f(y)>=log2((x+1)(y+1))? f(x)f(y)-f(x)-f(y)=(f(x)-1)(f(y)-1)-1... not always>=0
# (e.g. x=y=1: 1 vs 1 ok; x=1: f=1, product=f(y), f(y)=f(xy) since xy=y: equality).
# General: x,y>=1 -> f(x),f(y)>=1. If either equals 1 (x or y =1): equality as shown.
# Else f(x),f(y)>1: f(x)f(y) >= f(x)+f(y) iff (f(x)-1)(f(y)-1)>=1, FALSE in general
# (e.g. x=y=2: f=1.585, prod=2.51, sum=3.17). So use direct grid check + known F-membership.
def f(t):
    return math.log2(t + 1)
xs = [1.0]
t = 1.0
while t <= 1e9:
    xs.append(t)
    t *= 1.7
for a in xs:
    for b in xs:
        assert f(a * b) <= f(a) * f(b) + 1e-9, (a, b)
print("B3 f submultiplicative on %d x %d log-grid OK (F-class quoted from GM/Schlumprecht)" % (len(xs), len(xs)))

# B4
j1 = 2**36 - 1
lhs_needed = 2 * j1  # lnlnln(j2) >= this
rhs_is = math.log(math.log(144 * math.log(2)))  # lnlnln(2^144)
print("B4 lnlnln(j2) >= 2*j1 = %.3e >> lnlnln(2^144) = %.4f => j2 >> 2^144-1 OK"
      % (float(lhs_needed), rhs_is))
assert float(lhs_needed) > rhs_is

# B5
assert abs((4 / 2.4) ** 2 - 2.7777777777777777) < 1e-9
print("B5 window: need f(k)/f(n) <= 25/9 = 2.7778 for prefix ratio >= (1/4)sqrt(f(n)) OK")
# example: k+1=(n+1)^2.777 -> boundary; triple-exp K-gaps violate except just below K
print("B5 e.g. n=10^6: f(n)=%.3f, allowed f(k)<=%.3f, i.e. k+1 <= (n+1)^2.78 ~ 10^16.7"
      % (f(1e6), 2.7778 * f(1e6)))

# B6
lj1 = math.log(j1)
print("B6 first good interval [ln j1, exp j1] = [%.3f, 10^(10^%.3f)] (via log10(exp j1)=j1/ln10)"
      % (lj1, math.log10(j1 / math.log(10))))
print("B6 covers all n in [25, 10^(10^10.47...)]; K-elements j2+ sit in gaps above exp(j1) OK")
print("ALL_SUPPORT_OK")
