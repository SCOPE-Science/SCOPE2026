"""Target-directed audit for lane-503: Teng W_1 twist in E(1)_{2,3}.

Certifies (reproducibly, stdlib+sympy):
 1. Dolgachev E(1)_{2,3} numerics: e, sigma, b2, b2+/-, chi_h, c1^2.
 2. Intersection-form invariants: odd form diag(+1,-1^9) vs even -E8+H;
    nucleus block N=[[0,1],[1,-1]]; block diag(-E8,N) invariant match;
    rank-overflow check of literal "-E8+H+nucleus" reading.
 3. Teng Stein data pins: framing == tb-1 for C(1,1;-1) and C_m.
 4. Quoted (not derived) SW background table with chamber flags.
 5. Binary gap checklist per target clause.

Quoted theorems (cited, not re-proved): Freedman classification; Serre
classification of odd indefinite unimodular forms (rank+signature determine);
Taubes SW-nonvanishing for symplectic; FS98 knot-surgery formula (schematic);
Gompf tb-1 Stein criterion; Teng Thm/Aux-lemma statements.
"""
import json
from fractions import Fraction
from sympy import Matrix, Rational

out = {"checks": {}, "tables": {}, "gaps": {}}

# ---------- 1. Dolgachev numerics ----------
# Log transform preserves e and sigma (standard, quoted).
e, sig = 12, -8
b2 = e - 2  # simply connected closed: b0=1,b1=b3=0,b4=1
bp = (b2 + sig) // 2
bm = (b2 - sig) // 2
chi_h = (sig + e) // 4
c1sq = 3 * sig + 2 * e
assert (b2 + sig) % 2 == 0
out["tables"]["dolgachev_E12_3"] = {
    "e": e, "sigma": sig, "b2": b2, "b2+": bp, "b2-": bm,
    "chi_h": chi_h, "c1^2": c1sq, "pi1": "0 (2,3 coprime, quoted)",
    "note": "same e,sigma as E(1)=CP2#9CPbar; log transform preserves",
}
out["checks"]["numerics"] = (b2 == 10 and bp == 1 and bm == 9
                             and chi_h == 1 and c1sq == 0)

# ---------- 2. Intersection forms ----------
def gram_invariants(M):
    M = Matrix(M)
    n = M.rows
    det = int(M.det())
    # signature via exact rational LDL (congruence -> signs of pivots)
    A = [[Rational(M[i, j]) for j in range(n)] for i in range(n)]
    signs = []
    k = 0
    while k < n:
        # partial pivot: find nonzero diagonal after symmetric swaps
        if A[k][k] == 0:
            swap = next((j for j in range(k + 1, n) if A[j][j] != 0), None)
            if swap is not None:
                A[k], A[swap] = A[swap], A[k]
                for row in A:
                    row[k], row[swap] = row[swap], row[k]
        if A[k][k] == 0:
            # indefinite 2x2 block [[0,a],[a,b]] -> contributes (+,-), sig 0
            piv = next((j for j in range(k + 1, n) if A[k][j] != 0), None)
            assert piv is not None, "degenerate form"
            A[k + 1], A[piv] = A[piv], A[k + 1]
            for row in A:
                row[k + 1], row[piv] = row[piv], row[k + 1]
            signs += [+1, -1]
            Bm = Matrix([[A[k][k], A[k][k + 1]], [A[k + 1][k], A[k + 1][k + 1]]])
            Bi = Bm.inv()
            for i in range(k + 2, n):
                for j in range(k + 2, n):
                    A[i][j] = (A[i][j] - (Matrix([A[i][k], A[i][k + 1]]) * Bi
                                          * Matrix([A[k][j], A[k + 1][j]]))[0])
            for i in range(k, k + 2):
                for j in range(n):
                    A[i][j] = A[j][i] = Rational(0)
            k += 2
            continue
        piv = A[k][k]
        signs.append(+1 if piv > 0 else -1)
        for i in range(k + 1, n):
            f = A[i][k] / piv
            for j in range(k + 1, n):
                A[i][j] -= f * A[k][j]
        k += 1
    # oddness: exists integral v with v'Mv odd  <=> some diagonal odd after?
    # brute check over basis + pairwise sums (sufficient for unimodular audit)
    odd = any(int(M[i, i]) % 2 != 0 for i in range(n))
    if not odd:
        odd = any(int((Matrix([1 if k in (i, j) else 0 for k in range(n)]).T
                       * M * Matrix([1 if k in (i, j) else 0 for k in range(n)]))[0]) % 2 != 0
                  for i in range(n) for j in range(i + 1, n))
    return {"rank": n, "det": det, "signature": sum(signs), "odd": odd}

G_odd = Matrix.diag(*([1] + [-1] * 9))
inv_odd = gram_invariants(G_odd)
out["tables"]["Q_odd_rank10"] = {"gram": "diag(+1,-1 x9)", **inv_odd}

E8 = Matrix([[2, -1, 0, 0, 0, 0, 0, 0],
             [-1, 2, -1, 0, 0, 0, 0, 0],
             [0, -1, 2, -1, 0, 0, 0, 0],
             [0, 0, -1, 2, -1, 0, 0, 0],
             [0, 0, 0, -1, 2, -1, 0, -1],
             [0, 0, 0, 0, -1, 2, -1, 0],
             [0, 0, 0, 0, 0, -1, 2, 0],
             [0, 0, 0, 0, -1, 0, 0, 2]])
inv_mE8 = gram_invariants(-E8)
H = Matrix([[0, 1], [1, 0]])
inv_H = gram_invariants(H)
N = Matrix([[0, 1], [1, -1]])  # Gompf-nucleus-type block G(1)
inv_N = gram_invariants(N)
out["tables"]["summands"] = {"-E8": inv_mE8, "H": inv_H, "NucleusBlock": inv_N}

big = Matrix.zeros(10)
big[:8, :8] = -E8
big[8:, 8:] = N
inv_big = gram_invariants(big)
out["tables"]["minusE8_plus_NucleusBlock"] = {
    "gram": "-E8 (+) [[0,1],[1,-1]]", **inv_big,
    "isometric_to_odd_diag": (inv_big["rank"] == inv_odd["rank"]
                              and inv_big["det"] == inv_odd["det"]
                              and inv_big["signature"] == inv_odd["signature"]
                              and inv_big["odd"] == inv_odd["odd"]),
    "basis": "odd indefinite unimodular => rank+sig+parity determine (Serre, quoted)",
}
# literal three-summand reading overflows b2=10
out["checks"]["Q"] = {
    "odd_diag_matches_E12_3_invariants": (inv_odd == {"rank": 10, "det": -1,
                                                     "signature": -8, "odd": True}),
    "even_E8H_parity_note": "parity of -E8, H checked separately (even)",
    "literal_E8+H+nucleus_rank_overflow": (8 + 2 + 1 > 10),
    "charitable_E8+NucleusBlock_consistent": out["tables"]["minusE8_plus_NucleusBlock"]["isometric_to_odd_diag"],
}

# ---------- 3. Teng Stein pins (Gompf tb-1 criterion, quoted) ----------
def stein_ok(framing, tb):
    return framing == tb - 1
out["tables"]["teng_stein_pins"] = {
    "C(1,1;-1)": {"framing": -2, "tb": -1, "stein_tb-1": stein_ok(-2, -1),
                  "source": "Teng Fig.37 (right of Fig.20240604-1)"},
    "C_m": {"framing": 0, "tb": +1, "stein_tb-1": stein_ok(0, +1),
            "source": "Teng Fig.47 (Fig.20240605-0)"},
    "criterion": "Gompf 1998 handlebody tb-1 (quoted)",
}
out["checks"]["stein_pins"] = True

# ---------- 4. SW background table (QUOTED, chamber-flagged) ----------
out["tables"]["SW_background_quoted"] = {
    "E(1)_{2,3}_canonical": {
        "K^2": 0, "SW": "+/-1 (canonical-related basic class)",
        "status": "QUOTED: Taubes symplectic-nonvanishing + Dolgachev computations "
                  "(Fintushel-Stern / Friedman-Morgan / Morgan-Mrowka-Szabo); "
                  "b2+=1 => chamber must be specified",
    },
    "E(1)=CP2#9CPbar": {
        "SW": "0 (admits PSC; quoted)",
        "status": "QUOTED",
    },
    "knot_surgery_formula": {
        "form": "SW_{X_K} = SW_X * Alexander_K (schematic, b2+>1 sharp; b2+=1 chamber-sensitive)",
        "status": "QUOTED FS98; applies ONLY if twist identified as knot surgery",
    },
}

# ---------- 5. Binary gap checklist vs target clauses ----------
out["gaps"] = {
    "X-side_homeomorphism_type": "QUOTED-CONDITIONAL (Freedman; needs odd-form + pi1=0 pins above)",
    "Q_X_logged": "CERTIFIED-INVARIANTS (grams archived here; explicit unimodular U not constructed, classification quoted)",
    "SW(X,K_X)=+/-1": "QUOTED (chamber-sensitive for b2+=1; exact basic-class label K_X in fixed nucleus basis NOT fixed)",
    "W_1_hookrightarrow_E(1)_{2,3}_nucleus_embedding": "OPEN: Teng embeds in E(n) n>=2 (vanishing-cycle count); no sourced embedding into E(1)_{2,3}; Akbulut-Yasui is general method, no such cell",
    "X_f_identification": "OPEN: no sourced diffeomorphism type of W_1-twist in Dolgachev background",
    "SW(X_f,K_f)=0": "OPEN: quoted knot-surgery formula preserves nonvanishing via Alexander factor; vanishing needs X_f ~= rational/PSC identification which is absent; b2+=1 chamber for K_f unspecified",
    "W_1_label_ambiguity": "FLAGGED: Teng first member C(1,1;-1) vs C_1; collides with Akbulut-Yasui W_1 notation",
}
out["checks"]["target_closed"] = False

with open("output/artifacts/target_audit.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1)[:4000])
print("ARTIFACT_WROTE output/artifacts/target_audit.json")
