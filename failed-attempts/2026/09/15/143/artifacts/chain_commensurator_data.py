"""Reproducible computational data for lane-20388 (Yoshida chain-link mutants).

NOT a theorem: volumes below are SnapPy (non-interval-certified) numerical values,
recorded to preserve the attempted routes R1 (chain-PD census identification and
commensurator-volume computation) and R3 (antiprism model). Used as evidence in
output/target_exit_request context and output/target_exit.json (CLEAN_EXIT).

Source lemmas (Yoshida, Proc. Japan Acad. 98A (2022), DOI 10.3792/pjaa.98.014):
  M_n = S^3 \\ C_n non-arithmetic; |Comm(Gamma_n):N(Gamma_n)| = n+1;
  C and C_n commensurable; vol(H^3/Comm) = vol(P)/2(n+1); |Symm(M_n)| = 4.
Hence V_n := vol(C^(n+1))/4(n+1) is the commensurator volume; commensurable
non-arithmetic M_n, M_m force V_n == V_m.
"""


def chain_PD(k):
    """PD code for the closed k-component alternating chain C^(k), k >= 5.

    Reverse-engineered from the nested SnapPy census PDs
    L10a174 (k=5), L12a2020 (k=6), L14a31811 (k=7), which agree prefix-wise;
    validated: reproduced links match census volumes/symmetries exactly.
    """
    PD = [[4, 0, 5, 3], [0, 4, 1, 7]]
    for j in range(1, k - 1):
        if j <= k - 2:
            PD.append([4 * j + 4, 4 * j - 2, 4 * j + 5, 4 * j - 3])
            PD.append([4 * j - 2, 4 * j + 4, 4 * j - 1, 4 * j + 7])
    PD.append([4 * k - 2, 4 * k - 6, 4 * k - 1, 4 * k - 7])
    PD.append([4 * k - 6, 4 * k - 2, 4 * k - 5, 4 * k - 3])
    return PD


# Census dictionary (SnapPy HTLinkExteriors): chain C^(k) and mutant C_n, n = k-1.
# Mutants identified by: same volume as chain + order-4 symmetry group +
# one distinguished large (fused double) cusp c'_2 + non-isometry to chain.
CENSUS_IDS = {
    4: {"chain": "L10a174", "mutant": "L10a168"},
    5: {"chain": "L12a2020", "mutant": "L12a2012"},
    6: {"chain": "L14a31811", "mutant": "L14a31801"},
}

# Commensurator volumes V_n = vol(C^(n+1))/4(n+1), SnapPy 50-digit (ManifoldHP),
# strictly increasing over the computed range; limit appears v_oct/4 = 0.915966.
V_TABLE = {
    4: "0.730153037668772338540056370550441660257469249283991092374092824",
    5: "0.784653473616150312730844290048706298231492225052621175365837618",
    6: "0.818431888929398454995821598358644690795448605745991865665893195",
    7: "0.840747248900307020314429973546277887753700595093485440175534316",
    8: "0.856232271666040901056853724342143507650225990895035973260058878",
    9: "0.867404002126948962596965967909371906995308848837401680026802833",
}

# Chain raw volumes vol(C^(k)): k=5: 14.603061; k=6: 18.831683; k=7: 22.916093;
# k=8: 26.903912; k=9: 30.824362; k=10: 34.69616; k=12: 42.33979;
# k=15: 53.65147; k=20: 72.29431 (SnapPy double precision, last four).
