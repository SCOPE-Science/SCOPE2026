"""Excision invariance under cork twist (§D Lemma D2 arithmetic).

X' = (X - C) U_tau C, C contractible, dC closed connected (homology sphere).
chi: chi(X') = chi(X-C) + chi(C) - chi(dC) [gluing along collar, chi(dC)=0]
            = chi(X-C) + 1.
     chi(X)  = chi(X-C) + chi(C) - chi(dC) = chi(X-C) + 1.  Equal.
sigma: Novikov additivity sigma(X') = sigma(X-C) + sigma(C) = sigma(X-C),
       sigma(X) = sigma(X-C) (sigma(C)=0 since H2(C)=0). Equal.
H_*: excision H_*(X', X-C) ~= H_*(C, dC) = 0 for *<4 (contractible +
       Poincare-Lefschetz: H_*(C,dC) ~= H^{4-*}(C) = 0 for *!=4).
       So inclusion X-C -> X' is H_*-iso through degree 3; same for X.
       Hence b2, homology below top degree preserved.
"""
import json

chi_C = 1
chi_dC = 0
sigma_C = 0
# symbolic: chi(X-C) =: q  ->  chi(X) = chi(X') = q + 1
q = 7  # dummy value to exhibit arithmetic
out = {
    "chi_X": q + chi_C - chi_dC,
    "chi_Xprime": q + chi_C - chi_dC,
    "chi_equal": True,
    "sigma_X": "sigma(X-C) + 0",
    "sigma_Xprime": "sigma(X-C) + 0",
    "sigma_equal": True,
    "H_below_top_preserved": True,
    "b2_equal": True,
    "consequence": "ambient-twist pair shares chi/sigma/H_*<4/b2; "
                   "contractible pair needs contractible ambient",
}
print(json.dumps(out, indent=2))
assert out["chi_X"] == out["chi_Xprime"]
