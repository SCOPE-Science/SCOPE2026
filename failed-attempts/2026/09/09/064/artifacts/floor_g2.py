"""Unconditional genus floor + g=2 characterization (balanced, contractible chi=1,
boundary a homology sphere != S^3). Target-directed refinement of narrow_genus3.py.

Cited inputs (all allowed):
- Takahashi Lemma 4.1 enumeration (balanced): g in {0,1,2} admit exactly one
  type each at chi=1: (0,0,0,1), (1,1,0,2), (2,2,0,3) [verified by exhaustive
  scan in verify_target.py extension below].
- Takahashi Sec.4 via Etnyre-Ozbagci [16]: planar open book b=1 -> S^3;
  b=2 -> lens space. Via Arikan [6]: b=3 -> Seifert fibered or # of two lens
  spaces (as cited in Takahashi p.12 / Cor 4.2 discussion).
- Boundary != S^3: cork non-extension + Diff(S^3) connected (Hatcher) + collar
  extension (same argument as narrow_genus3.py).
- Homology-sphere + lens-space/connected-sum elimination by H1 arithmetic:
  lens homology sphere -> S^3; (# of two lens spaces) homology sphere -> S^3.

Results:
- g=0 type (0,0,1): disk page, 1 binding -> S^3. EXCLUDED.
- g=1 type (1,0,2): annulus page, 2 bindings -> lens space -> homology sphere
  forces S^3. EXCLUDED.
- Hence: unconditional g >= 2 for Y0/Y1 (either side), no hyperbolicity needed.
- g=2 type (2,0,3): pair-of-pants page, 3 bindings -> Seifert or L(p)#L(q);
  L-sum homology sphere forces S^3 (H1 = Z/p + Z/q = 0 -> p=q=1), excluded;
  so g=2 occurs iff boundary is Seifert fibered (the S^3 alternative excluded).
  Therefore: g >= 3  IFF  boundary is NOT Seifert fibered (given boundary is a
  homology sphere != S^3). This reduces the Y0 genus-3 lower bound to ONE
  concrete 3-manifold question: is dC1 Seifert fibered?
"""
import json

scan = {}
for g in [0, 1, 2]:
    sols = []
    for p in range(0, 5):
        for b in range(1, 10):
            for k in range(0, 10):
                if not (2 * p + b - 1 <= k <= g + p + b - 1):
                    continue
                if g - 3 * k + 3 * p + 2 * b - 1 != 1:
                    continue
                A = g + p + b - 1 - k
                sols.append({"k": k, "p": p, "b": b, "A": A})
    scan[g] = sorted(sols)

assert scan[0] == [{"k": 0, "p": 0, "b": 1, "A": 0}]
assert scan[1] == [{"k": 1, "p": 0, "b": 2, "A": 1}]
assert scan[2] == [{"k": 2, "p": 0, "b": 3, "A": 2}]

elimination = {
    "g0_(0,0,1)": "page disk, b=1 -> S^3 by [16]; excluded (boundary != S^3)",
    "g1_(1,0,2)": "page annulus, b=2 -> lens space by [16]; homology sphere lens -> S^3; excluded",
    "g2_(2,0,3)": "page pair-of-pants, b=3 -> Seifert or L#L' by [6]; L#L' homology sphere -> S^3 (H1=Z/p+Z/q=0), excluded; survives iff boundary Seifert fibered",
}
out = {
    "unique_low_genus_types_chi1": {str(g): v for g, v in scan.items()},
    "elimination": elimination,
    "UNCONDITIONAL_FLOOR": "g(Yi) >= 2 for i=0,1 (no boundary hypothesis beyond homology sphere != S^3)",
    "G2_CHARACTERIZATION": "g(Yi)=2 possible iff dC1 Seifert fibered; g>=3 iff dC1 NOT Seifert fibered",
    "missing_step": "Seifert-vs-not determination for dC1 (needs surgery presentation + Seifert/hyperbolic analysis a la Takahashi Prop 3.8; absent from Teng)",
    "note": "Does not separate Y0 from Y1 (both share boundary/topology); feeds the Y0-side lower bound only.",
}
print(json.dumps(out, indent=2))
