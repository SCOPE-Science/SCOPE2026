"""Twist-double arithmetic (§E, case d): doubles of a contractible cork are
homotopy 4-spheres -- closed, non-contractible, non-Stein. Hence excluded
by the target's 'compact contractible Stein' clause.

D_k = W U_{f^k} (-W), W contractible, dW closed connected homology 3-sphere.
chi(D) = chi(W) + chi(-W) - chi(dW) = 1 + 1 - 0 = 2 (odd-dim closed => 0).
pi1(D) = 0 by Van Kampen (two simply-connected halves, connected intersection
dW; W contractible => simply-connected).
Closed simply-connected chi=2 => b2 = 0 (chi = 2 - 2b1 + b2 - ... = 2 + b2
with b1=b3=0 by duality/Hurewicz-lite; homology sphere argument below).
So D_k is a homology 4-sphere, simply-connected => homotopy S^4 (Hurewicz +
Whitehead), homeomorphic S^4 by Freedman. Diffeo type may depend on k
(the only construction from (W,f^k) alone that can see k), but it is NEVER
contractible (pi4/homology: contractible => chi=1, here chi=2) and NEVER a
Stein domain (compact Stein without boundary is trivial; Stein domains in
the Gompf/Teng/Takahashi sense are compact WITH boundary).
"""
import json

chi_W = 1
chi_dW = 0  # closed odd-dimensional
chi_D = chi_W + chi_W - chi_dW
# Homology of closed simply-connected 4-manifold with chi=2: b2 = chi - 2 = 0.
b2_D = chi_D - 2
out = {
    "chi_double": chi_D,
    "b2_double": b2_D,
    "pi1_double": 0,
    "homotopy_type": "S^4 (homology sphere + simply-connected)",
    "closed": True,
    "contractible": False,
    "stein_domain_compatible": False,
    "verdict": "doubles excluded by target's 'compact contractible Stein' clause; "
               "the only k-sensitive construction from (W,f^k) alone lands outside the target class",
}
print(json.dumps(out, indent=2))
assert chi_D == 2 and b2_D == 0
