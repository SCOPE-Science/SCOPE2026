"""Target deepening audit 2 for lane-503 (TARGET phase only).

Proves/certifies (reproducibly):
 L1. Canonical-class label: in -E8 (+) N-block basis with N=[[0,1],[1,-1]]
     (F=fiber, S=section), adjunction on geometric representatives forces
     K_X = -F (up to sign), K^2 = 0. Exact integer linear solve below.
 L2. Cork-twist topological invariance (conditional): for contractible W
     with homology-sphere boundary in simply-connected X, any twist X_f is
     simply connected with H_*(X_f)=H_*(X), Q_{X_f}=Q_X (MV + Van Kampen).
     => Freedman homeomorphism side reduces to sourcing pi1(dW)=homology
        sphere + contractibility (Teng Aux lemma gives contractible for
        P(U)=U winding-1; boundary H_* check recorded as diagram-sourced).
 L3. Twist-side SW=0 still OPEN: knot-surgery mechanism preserves
     nonvanishing; correspondence of K_f needs K_X representable in the
     complement (unsourced for Teng embedding); b2+=1 chamber unmatched.

Quoted (not derived): Freedman; adjunction equality for symplectic/
Kahler representatives; FS98 formula schematic; Teng contractibility.
"""
import json
from sympy import Matrix, Rational

out = {"lemmas": {}, "checks": {}}

# ---- L1: K_X label from adjunction ----
# Basis: e8part (rank 8, -E8) + F, S with gram N=[[0,1],[1,-1]].
# Geometric inputs (quoted representatives in Dolgachev elliptic fibration):
#  F: torus, F^2=0, g=1 -> 0 = F^2 + K.F => K.F = 0.
#  S: sphere, S^2=-1 -> -2 = S^2 + K.S => K.S = -1.
#  C_i: E8 root spheres, C_i^2=-2, g=0 -> K.C_i = 0 for all i.
# Write K = v + aF + bS, v in E8-block (as row). K.F = b (since F.F=0,S.F=1,
# v.F=0) => b=0. K.S = a(F.S) + b(S.S) = a - b = a => a=-1.
# K.C_i = (v^T G_E8)_i = 0 => v=0 (G unimodular/det 1... -E8 det=1).
from sympy import Matrix as M
E8 = M([[2,-1,0,0,0,0,0,0],[-1,2,-1,0,0,0,0,0],[0,-1,2,-1,0,0,0,0],
        [0,0,-1,2,-1,0,0,0],[0,0,0,-1,2,-1,0,-1],[0,0,0,0,-1,2,-1,0],
        [0,0,0,0,0,-1,2,0],[0,0,0,0,-1,0,0,2]])
G = M.zeros(10)
G[:8,:8] = -E8
G[8,8]=0; G[8,9]=1; G[9,8]=1; G[9,9]=-1
assert int(G.det()) == -1
# unknowns k (10-vector); equations: G*k = pairings p where
# p = (0 x8 for E8 roots, K.F=0, K.S=-1)
p = M([0]*8 + [0, -1])
k = G.LUsolve(p)
out["lemmas"]["L1_canonical_label"] = {
    "K_coeffs_E8x8_plus_aF_plus_bS": [str(x) for x in k],
    "claim": "K_X = -F (a=-1,b=0,v=0)",
    "K2": str((k.T*G*k)[0]),
    "status": "PROVED-CONDITIONAL on quoted geometric representatives "
              "(torus fiber, -1 section, E8 root spheres)",
}
out["checks"]["L1"] = (list(k) == [0]*8 + [-1, 0] and (k.T*G*k)[0] == 0)

# ---- L2: cork-twist homology/pi1 invariance (formal argument logged) ----
out["lemmas"]["L2_twist_invariance"] = {
    "statement": "X simply-connected, W contractible, dW a homology sphere "
                 "=> X_f simply-connected, H_*(X_f)=H_*(X), Q_{X_f}=Q_X.",
    "proof_sketch": "MV: H2(dW)=H1(dW)=0, H2(W)=H1(W)=0 give "
        "H2(X-intW)~>H2(X) iso and same for X_f, hence Q preserved; "
        "VK: pi1(X)=pi1(X-intW)/N(i_*pi1(dW))=0, and f_* automorphism of "
        "pi1(dW) preserves the normal closure, so pi1(X_f)=0 identically. "
        "Freedman then gives X_f homeomorphic X (same odd Q, pi1=0).",
    "status": "PROVED-CONDITIONAL (needs: W contractible — Teng Aux lemma "
              "for P(U)=U winding-1; dW homology sphere — diagram-sourced, "
              "not recomputed here)",
    "reduces_homeomorphism_side_to": "sourcing the two parenthetical pins",
}
out["checks"]["L2"] = True

# ---- L3: why SW(X_f,K_f)=0 does not close ----
out["lemmas"]["L3_twist_side_gap"] = {
    "knot_surgery_preserves_nonvanishing": "quoted FS98 schematic SW_{X_K}=SW_X*Alex_K; "
        "twist-knot Alex (k>=1) nontrivial (computed k=1..5 in WORKLOG), so no zero",
    "correspondence_caveat": "K_f<->K_X via H2(X-intW) needs K_X=-F representable "
        "by a surface in the complement of Teng W_1; unsourced (fiber meets nucleus "
        "where W_1 would embed)",
    "chamber_caveat": "b2+=1: quoted SW=+/-1 is symplectic/small-perturbation chamber; "
        "K_f chamber under twist identification unspecified in target",
    "sourced_vanishing_belongs_elsewhere": "Akbulut 0805.1524 positron/Wbar_1 twist "
        "E(1)_{2,3}->E(1); no source for Teng-W_1 twist identification",
    "status": "OPEN",
}
out["checks"]["L3_open"] = True
out["checks"]["target_closed"] = False

with open("output/artifacts/target_audit2.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
print("ARTIFACT_WROTE output/artifacts/target_audit2.json")
