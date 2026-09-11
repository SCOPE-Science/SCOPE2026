"""Artifact 1: smoothness over Q + good reduction at all p>=5 (proof certificate).

X: F = x^4+y^4-z^4-w^4+x^2y^2-z^2w^2.
grad F = (2x(2x^2+y^2), 2y(x^2+2y^2), -2z(2z^2+w^2), -2w(z^2+2w^2)).
Claim: in characteristic != 2,3, grad=0 (projective) forces x=y=z=w=0.
Proof: 2x(2x^2+y^2)=0 => x=0 or y^2=-2x^2. If x=0, second gives 2y^3=0=>y=0.
If y^2=-2x^2 with x!=0: x^2+2y^2 = x^2-4x^2 = -3x^2 != 0 (char!=3) so y=0,
then 0=y^2=-2x^2 => x=0 (char!=2), contradiction. So x=y=0; same for z,w.
Script: brute-verifies singular loci for p in {2,3,5,7,11,13}.
"""
import json

def Fpoly(x, y, z, w):
    return x**4 + y**4 - z**4 - w**4 + x*x*y*y - z*z*w*w

def grad(x, y, z, w):
    return (4*x**3 + 2*x*y*y, 4*y**3 + 2*x*x*y,
            -4*z**3 - 2*z*w*w, -4*w**3 - 2*z*z*w)

def singular_reps(p):
    out = []
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    if (x, y, z, w) == (0, 0, 0, 0):
                        continue
                    if Fpoly(x, y, z, w) % p != 0:
                        continue
                    if all(v % p == 0 for v in grad(x, y, z, w)):
                        out.append([x, y, z, w])
    return out

res = {}
for p in [2, 3, 5, 7, 11, 13]:
    s = singular_reps(p)
    res[str(p)] = {"n_singular_affine_reps": len(s),
                   "smooth": len(s) == 0,
                   "examples": s[:4]}
print(json.dumps(res, indent=1))
assert res["5"]["smooth"] and res["7"]["smooth"] and res["11"]["smooth"] and res["13"]["smooth"]
assert not res["2"]["smooth"] and not res["3"]["smooth"]
print("SMOOTHNESS_OK: X smooth/Q, good reduction at 5,7,11,13; BAD at 2,3")
