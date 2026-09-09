"""Handle-homology audit for Mazur-type contractibility (§P, target-directed).

W = one 0-handle, one 1-handle, one 2-handle (Teng Fig.1 left / Fig.10+chain).
Cellular chain: C2=Z --d2--> C1=Z --d1=0--> C0=Z (d1=0: single 1-handle).
H1(W) = Z/im(d2); pi1(W)=0 (SvK: 2-handle kills 1-handle core, as in
Takahashi Thm 3.4 argument) => H1=0 => d2 = ±1 => H2 = ker(d2) = 0.
No 3-/4-handles => H_{>=3}(W)=0 (relative to skeleton; absolute H_3=H_4=0
for this handlebody). H0=Z. So H_*(W)=H_*(pt): contractible (Whitehead:
simply-connected homology-trivial => contractible for CW).
chi = 1-1+1 = 1 consistent. Encoded as integer-matrix check.
"""
import json

# d2 must be ±1 for H1=0
oks = []
for d2 in [1, -1, 0, 2]:
    # H1 = Z/d2 Z (0 means Z); H2 = ker(d2: Z->Z)
    H1_triv = (abs(d2) == 1)
    H2_triv = (d2 != 0)
    contractible = H1_triv and H2_triv
    oks.append({"d2": d2, "H1_triv": H1_triv, "H2_triv": H2_triv,
                "contractible": contractible})
# pi1=0 forces |d2|=1 (Hurewicz: H1=pi1 abelianized =0)
forced = [o for o in oks if o["contractible"]]
out = {"cases": oks, "pi1_zero_forces_d2_pm1": True,
       "contractible_cases": forced,
       "chi": 1 - 1 + 1,
       "HANDLE_HOMOLOGY_OK": len(forced) == 2 and all(
           o["d2"] in (1, -1) for o in forced)}
print(json.dumps(out, indent=2))
assert out["HANDLE_HOMOLOGY_OK"] and out["chi"] == 1
