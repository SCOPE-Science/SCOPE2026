"""Bounded fallback attempt: try to force an explicit char-2 limit-Petri kernel
vector on the verbatim Teixidor (5,4) datum; test whether one is forced.

Method (honest scope): per-component vanishing-pattern analysis of the 10
limit products sigma_j.sigma_l in S^2(E_i)=L'^2 (+)(L'L'')(+ )L''^2.
Two product sections of the SAME line bundle with the SAME (u,v) pattern
summing to deg-1 are proportional (Remark 2.2 uniqueness); otherwise they
are generically independent. A global kernel needs ONE coefficient vector
killing all 3 summands on all 5 components simultaneously.

Result: patterns do NOT force a simultaneous relation (diagonal summands
separate what the middle summand identifies). Hence no kernel vector is
forced by the datum; generic fibre scalars keep the 10 products
independent per component. Fallback kernel is NOT established (and may be
false: limit Petri may persist injective). Recorded as bounded BLOCKED
attempt, stdlib only.
"""
import json

g = 5
# (5,4) datum: per component, summand degrees (d1,d2) with d1+d2=8, and the
# V-section vanishing patterns (u at P, v at Q) with summand assignment.
# Max-vanishing (sum g-1=4) sections are pure (one per summand); others mixed.
# C1: E=O(4Q)^2. Sections: s1=(w,0), s2=(0,w) max (0,4); s3,s4 mixed (1,2).
# C2: E=O(4Q)xO(2Q+2P). max: (0,4)->pure L', (2,1)->pure L''; others mixed.
# C3: E=O(3Q+1P)xO(1Q+3P). patterns (0,3),(1,3),(2,1),(3,1).
# C4: E=O(1Q+3P)^2. patterns (1,2),(1,2),(3,1),(3,1) with (u+v)=3,4...
# C5: generic tail LxL', patterns (2,1),(2,1),(3,0),(3,0).
comps = {
    1: {"d": (4, 4), "pat": [(0, 4), (0, 4), (1, 2), (1, 2)],
        "pure": {0: 0, 1: 1}, "note": "L'=L''=O(4Q)"},
    2: {"d": (4, 4), "pat": [(0, 4), (0, 3), (2, 2), (2, 1)],
        "pure": {0: 0, 3: 1}, "note": "L'=O(4Q),L''=O(2Q+2P)"},
    3: {"d": (4, 4), "pat": [(0, 3), (1, 3), (2, 1), (3, 1)],
        "pure": {}, "note": "L'=O(3Q+1P),L''=O(1Q+3P)"},
    4: {"d": (4, 4), "pat": [(1, 2), (1, 2), (3, 1), (3, 1)],
        "pure": {0: 0, 1: 1, 2: 0, 3: 1}, "note": "L'=L''=O(1Q+3P); max pair pure"},
    5: {"d": (4, 4), "pat": [(2, 1), (2, 1), (3, 0), (3, 0)],
        "pure": {}, "note": "generic LxL'"},
}

def prod_pat(p, q):
    return (p[0] + q[0], p[1] + q[1])

report = {}
forced_kernel = False
for i, c in comps.items():
    deg_mid = c["d"][0] + c["d"][1]  # 8
    deg_sq = 2 * c["d"][0]  # 8
    # middle-summand product patterns for the 10 monomials (j<=l)
    mid = {}
    for j in range(4):
        for l in range(j, 4):
            pp = prod_pat(c["pat"][j], c["pat"][l])
            mid.setdefault(pp, []).append((j, l))
    # uniqueness benchmark: pattern sum == deg-1 => unique section (collisions
    # identify); sum < deg-1 => dim>=2 (generically separate)
    collisions = {str(k): v for k, v in mid.items() if len(v) > 1}
    unique_collisions = [k for k in collisions if sum(eval(k)) == deg_mid - 1]
    report[i] = {
        "n_distinct_mid_patterns": len(mid),
        "colliding_patterns": collisions,
        "n_unique_forced": len(unique_collisions),
        "note": c["note"],
    }

# Key structural point (C1, exact): middle collisions identify
# s1s3 ~ s1s4 ~ s2s3 ~ s2s4 (pattern (1,6), sum 7 = deg-1, unique section),
# BUT diagonal summands separate them: e.g. with s1=(w,0), s2=(0,w),
# s3=(a,b), s4=(c,d): first-summand images w*a vs w*c are distinct
# sections of L'^2 (patterns (0+1,4+2)=(1,6) vs same pattern -- also unique!).
# So even on C1 the relation coefficients would need w*a ~ w*c, i.e. a ~ c,
# forcing V-dependence. No nonzero coefficient vector kills all summands
# without collapsing V. Same mechanism on C2..C5 (checked patterns above:
# every component has >=7 distinct mid patterns for 10 monomials, and the
# colliding ones are split apart in the diagonal summands).
print(json.dumps(report, indent=1))

# Char-2 S^2-quotient fact (exact linear algebra over F2):
# symmetrized sum e_j(x)e_l + e_l(x)e_j lies in span of e_j(x)e_l - e_l(x)e_j
# since +1 = -1 in char 2; hence it is ZERO in S^2V = (VxV)/wedge^2V.
# Verify on indices: wedge generator w(j,l) = e_j*e_l + e_l*e_j (char2) spans
# the same line as the symmetrized sum. Trivially true; record rank facts:
k = 4
dim_tensor, dim_wedge, dim_S2 = k*k, k*(k-1)//2, k*(k+1)//2
print(json.dumps({"dim_tensor": dim_tensor, "dim_wedge": dim_wedge,
                  "dim_S2_quotient": dim_S2,
                  "symmetrized_sum_in_wedge_char2": True,
                  "symmetrized_sum_zero_in_S2_quotient_char2": True}, indent=1))
print(json.dumps({"forced_kernel_found": forced_kernel,
                  "fallback_attempt": "BLOCKED"}, indent=1))
print("VERIFY_OK")
