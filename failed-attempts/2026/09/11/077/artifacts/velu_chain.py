# Vélu-verified diametral chains for lane-883.
# Reads output/artifacts/ledger.json, builds explicit Fp2 curve models along the
# diametral j-path (forward) and the reversed j-path (backward), one 2-isogeny per
# link via translated Vélu, logging domain/kernel/codomain. Self-checks j at every step.
import json

P = 1009
D = 11  # Fp2 = Fp[s]/(s^2-11)

class F:
    __slots__ = ("a", "b")
    def __init__(self, a, b=0):
        self.a = a % P; self.b = b % P
    def __add__(self, o): return F(self.a+o.a, self.b+o.b) if isinstance(o, F) else F(self.a+o, self.b)
    def __radd__(self, o): return self.__add__(o)
    def __sub__(self, o): return F(self.a-o.a, self.b-o.b) if isinstance(o, F) else F(self.a-o, self.b)
    def __rsub__(self, o): return F(o-self.a, -self.b)
    def __neg__(self): return F(-self.a, -self.b)
    def __mul__(self, o):
        if isinstance(o, F):
            return F(self.a*o.a + D*self.b*o.b, self.a*o.b + self.b*o.a)
        return F(self.a*o, self.b*o)
    def __rmul__(self, o): return self.__mul__(o)
    def inv(self):
        n = (self.a*self.a - D*self.b*self.b) % P
        assert n != 0
        ni = pow(n, P-2, P)
        return F(self.a*ni, -self.b*ni)
    def __truediv__(self, o): return self*o.inv() if isinstance(o, F) else F(self.a*pow(o,P-2,P), self.b*pow(o,P-2,P))
    def __pow__(self, e):
        r, x = F(1), self
        while e:
            if e & 1: r = r*x
            x = x*x; e >>= 1
        return r
    def __eq__(self, o): return isinstance(o, F) and self.a==o.a and self.b==o.b
    def __repr__(self): return "[%d,%d]" % (self.a, self.b)
    def tolist(self): return [self.a, self.b]

def fp2_roots_cubic(A, B, C):
    """All roots in Fp2 of X^3+A X^2+B X+C by vectorized scan (uses numpy)."""
    import numpy as np
    U = np.repeat(np.arange(P, dtype=np.int64), P)
    V = np.tile(np.arange(P, dtype=np.int64), P)
    def add(X0,X1,c): return (X0+c.a)%P, (X1+c.b)%P
    def mul(X0,X1,Y0,Y1): return (X0*Y0+D*X1*Y1)%P, (X0*Y1+X1*Y0)%P
    Z0,Z1 = (U+0)%P, (V+0)%P
    Z0,Z1 = mul(Z0,Z1,U,V); Z0,Z1 = add(Z0,Z1,A)   # X^2+A... careful: build X^3+A X^2+B X+C
    # redo cleanly with Horner: ((X + A) X + B) X + C
    Z0 = (U + A.a) % P; Z1 = (V + A.b) % P
    Z0,Z1 = mul(Z0,Z1,U,V)
    Z0 = (Z0 + B.a) % P; Z1 = (Z1 + B.b) % P
    Z0,Z1 = mul(Z0,Z1,U,V)
    Z0 = (Z0 + C.a) % P; Z1 = (Z1 + C.b) % P
    idx = __import__("numpy").nonzero((Z0==0)&(Z1==0))[0]
    return [(int(U[i]), int(V[i])) for i in idx]

def j_of(a, b):
    den = 4*a**3 + 27*b**2
    assert den.a != 0 or den.b != 0, "singular!"
    return (1728*4*a**3) / den

def model_of_j(j):
    """Short-Weierstrass model over Fp2 with given j-invariant."""
    if j == F(0): return F(0), F(1)
    if j == F(1728 % P): return F(1), F(0)
    k = j / (F(1728 % P) - j)
    a, b = 3*k, 2*k
    assert j_of(a, b) == j
    return a, b

def velu_step(a, b, x0, j_target):
    """2-isogeny with kernel {O,(x0,0)} on y^2=x^3+a x+b. Returns (a',b',x0)."""
    A = 3*x0
    B = 3*x0*x0 + a
    assert (B.a, B.b) != (0, 0), "multiple root?!"
    Ap = -2*A
    Bp = A*A - 4*B
    assert (Bp.a, Bp.b) != (0, 0), "singular codomain?!"
    # short form via X-shift by Ap/3
    t = Ap/3
    ap = Bp - 3*t*t
    bp = 2*t*t*t - t*Bp
    assert j_of(ap, bp) == j_target, (j_of(ap,bp), j_target)
    return ap, bp

def build_chain(jpath, direction):
    assert len(jpath) >= 2
    a, b = model_of_j(F(*jpath[0]))
    steps = []
    for i in range(len(jpath)-1):
        jt = F(*jpath[i+1])
        assert j_of(a, b) == F(*jpath[i])
        roots = fp2_roots_cubic(F(0), a, b)
        assert len(roots) == 3, (i, roots)  # separable + all rational (Galois argument)
        found = None
        for (r0, r1) in roots:
            x0 = F(r0, r1)
            A = 3*x0; B = 3*x0*x0 + a
            Ap = -2*A; Bp = A*A - 4*B
            t = Ap/3
            ap = Bp - 3*t*t; bp = 2*t*t*t - t*Bp
            if j_of(ap, bp) == jt:
                found = (x0, ap, bp); break
        assert found, "no kernel gives target j at step %d" % i
        x0, ap, bp = found
        steps.append({"domain": [a.tolist(), b.tolist()],
                      "kernel_x": x0.tolist(),
                      "codomain": [ap.tolist(), bp.tolist()],
                      "j_in": jpath[i], "j_out": jpath[i+1]})
        a, b = ap, bp
    assert j_of(a, b) == F(*jpath[-1])
    return steps

led = json.load(open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-883/output/artifacts/ledger.json"))
jp = led["diametral_path_j"]
print("path length:", len(jp), "expected D+1 =", led["diameter"]+1)
fwd = build_chain(jp, "forward")
print("forward chain OK:", len(fwd), "Velu steps")
bwd = build_chain(jp[::-1], "backward")
print("backward chain OK:", len(bwd), "Velu steps")
out = {"forward": fwd, "backward": bwd,
       "j_path": jp,
       "diametral_jpair": led["diametral_jpair"],
       "diameter": led["diameter"]}
json.dump(out, open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-883/output/artifacts/velu_chains.json", "w"), indent=1)
print("wrote velu_chains.json")
