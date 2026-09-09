"""Finite toy-model check of the collar-regluing descent logic (§D).

Models: boundary dW = Z_n, f = cyclic shift (orientation-preserving toy
boundary diffeo), W = {interior *} U dW, C = dW x {0,1} (toy collar),
M_f = (W |_| C)/~_f with (i,0) ~_f f(i) in W,
M_id = (W |_| C)/~_id with (i,0) ~_id i in W.
Psi = id on W, f x id on C.
Checks: Psi descends (a ~_f b => Psi(a) ~_id Psi(b)), induces bijection
on quotients, maps boundary (dW x {1}) to boundary. n=5.
This validates the combinatorial core of the collar lemma used in §D.
"""
import json

n = 5
f = lambda i: (i + 1) % n

# Elements: ('W', x) with x in {'*'} U range(n); ('C', i, t) with t in (0,1).
def reps():
    els = [('W', '*')] + [('W', i) for i in range(n)]
    els += [('C', i, t) for i in range(n) for t in (0, 1)]
    return els

def parent_f(e):
    # union-find over touched gluings for M_f
    return e

class UF:
    def __init__(self):
        self.p = {}
    def find(self, a):
        if a not in self.p:
            self.p[a] = a
        while self.p[a] != a:
            self.p[a] = self.p[self.p[a]]
            a = self.p[a]
        return a
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb

uf_f, uf_id = UF(), UF()
for i in range(n):
    uf_f.union(('C', i, 0), ('W', f(i)))
    uf_id.union(('C', i, 0), ('W', i))

def Psi(e):
    if e[0] == 'W':
        return e
    _, i, t = e
    return ('C', f(i), t)

# Descent: for each generating relation a ~_f b, check Psi(a) ~_id Psi(b).
descent_ok = True
for i in range(n):
    a, b = ('C', i, 0), ('W', f(i))
    if uf_id.find(Psi(a)) != uf_id.find(Psi(b)):
        descent_ok = False

# Induced map on quotients is bijective: count classes + check fiber sizes.
classes_f = set(uf_f.find(e) for e in reps())
classes_id = set(uf_id.find(e) for e in reps())
# image of each f-class lands in one id-class; collect mapping
image = {}
well_defined = True
for e in reps():
    cf, ci = uf_f.find(e), uf_id.find(Psi(e))
    if cf in image and image[cf] != ci:
        well_defined = False
    image[cf] = ci
bijective = well_defined and len(set(image.values())) == len(classes_id) == len(classes_f)

# Boundary preservation: C x {1} maps into C x {1}.
bdy_ok = all(Psi(('C', i, 1))[2] == 1 for i in range(n))

out = {
    "n": n,
    "descent_Psi_respects_gluing": descent_ok,
    "induced_map_well_defined": well_defined,
    "induced_map_bijective_on_quotients": bijective,
    "num_classes_f": len(classes_f),
    "num_classes_id": len(classes_id),
    "boundary_to_boundary": bdy_ok,
    "COLLAR_DESCENT_LOGIC_OK": descent_ok and bijective and bdy_ok,
}
print(json.dumps(out, indent=2))
