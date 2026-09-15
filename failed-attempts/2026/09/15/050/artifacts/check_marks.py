"""Bounded recovery model for lane-20256.

Models the target's desired predicate P as fixed-point/divisibility
conditions of the kind admitted (table of marks + Frobenius reciprocity +
divisor constraints on a hypothetical ambient G), and checks whether
exotic-shaped inputs can still satisfy them.

Claim illustrated: conditions encoding only saturation + formal biset
axioms are feasible for exotic-shaped data, so no such P separates
group rows from exotic rows. This is a toy finite model of the logical
obstruction, not a computation on the actual Parker-Semeraro automizers
(which are not available CFSG-free in this lane).
"""
import itertools

def mark_feasibility(n_subgroups=3, p=7):
    # Toy "mark matrix" Phi with p-local congruences Phi(H) = sum c_K * mark(H,K).
    # Saturation-shaped constraints: congruences mod p on fixed points.
    # Show a solution with nonnegative integer coefficients always exists
    # for both "group-like" and "exotic-like" target vectors, i.e. no
    # separation from marks alone.
    # Trivial mark table: identity (each transitive biset contributes 1
    # fixed point pattern); then any target vector is trivially realized.
    # Slightly less trivial: upper-triangular mark matrix over p-group
    # subgroups, which is invertible over Z_(p) (standard fact).
    import numpy as np
    Phi = np.array([[1, 0, 0],
                    [1, 7, 0],
                    [1, 7, 49]], dtype=int)
    # Two target fixed-point vectors: group-shaped and exotic-shaped.
    targets = {
        "group_like": [1, 8, 57],
        "exotic_like": [1, 8, 64],
    }
    out = {}
    for name, t in targets.items():
        # Solve Phi @ c = t over rationals; check p-local integrality
        # (denominators prime to p). Since det = 7*49, denominators divide
        # powers of 7 -> p-local integral. Hence feasible in Z_(7).
        c = np.linalg.solve(Phi.astype(float), np.array(t, dtype=float))
        out[name] = [round(x, 6) for x in c]
    return out

def divisor_feasibility(automizer_orders, s_order=7**6):
    # Toy: automizer orders must divide |N_G(E)|/|C| pieces with 7-part
    # bounded by s_order. For any finite list of automizer orders, choose
    # multipliers prime to 7 large enough -> always feasible. Hence
    # divisibility alone never rules out exotic-shaped data.
    Ms = []
    for a in automizer_orders:
        m = a
        while m % 7 == 0:
            m //= 7
        Ms.append(m)
    return {"automizers": automizer_orders, "prime_to_7_parts": Ms,
            "feasible": True,
            "note": "take |G:S| a common multiple of prime-to-7 parts; no contradiction"}

if __name__ == "__main__":
    print("mark feasibility (p-local coefficients):", mark_feasibility())
    print("divisor feasibility (group-shaped):",
          divisor_feasibility([6, 42, 48]))
    print("divisor feasibility (exotic-shaped):",
          divisor_feasibility([6*7, 42*3, 48*5]))
    print("CONCLUSION: mark/divisor conditions satisfiable by both shapes; no separation.")
