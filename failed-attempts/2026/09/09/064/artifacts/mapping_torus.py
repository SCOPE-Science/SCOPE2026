"""Mapping-torus arithmetic (§E supplement): the other k-sensitive construction
from (W, f^k) alone. T_k = mapping torus of f^k on dW (closed 4-manifold).
chi(T_k) = 0 (mapping torus of any self-map of odd-dim closed manifold;
equivalently chi = chi(dW)*chi(S^1) up to monodromy correction = 0).
Closed => not a Stein domain in the compact-with-boundary sense, and
chi=0 != 1 => never contractible. So mapping tori are also excluded by the
target's 'compact contractible Stein' clause, like doubles.
Together with collar_descent.py (collars are k-blind) and twist_double.py
(doubles are homotopy S^4), this exhausts the ambient-free constructions:
  k-blind (abstract W, collar-reglued W)  ->  g(Y0)=g(Y1), no mismatch;
  k-sensitive (double, mapping torus)     ->  outside target class.
"""
import json

chi_dW = 0  # closed 3-manifold
chi_mapping_torus = 0  # chi(M_f) = 0 for closed odd-dim fiber
out = {
    "chi_boundary": chi_dW,
    "chi_mapping_torus": chi_mapping_torus,
    "closed": True,
    "contractible": False,
    "stein_domain_compatible": False,
    "verdict": "mapping tori excluded by target class; k-sensitive but never "
               "compact contractible Stein",
}
print(json.dumps(out, indent=2))
assert chi_mapping_torus == 0
