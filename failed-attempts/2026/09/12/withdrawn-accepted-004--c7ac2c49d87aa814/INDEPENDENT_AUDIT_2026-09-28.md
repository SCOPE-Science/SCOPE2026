# Independent Audit — 2026/09/12/004

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `5d5e1947c34cbf614140fbd472b4b1ff865e5b24`
- Disposition: **FAILED**

## Correctness

**PASS** — The full-measure proof is correct. For q=(2^k,b) with b odd and |b|<=2^k there are exactly 2^k vectors per shell. Distinct chosen vectors are never parallel: on one shell the determinant is 2^k(c-b), and across k<j it is 2^k(c-2^(j-k)b), an odd-minus-even factor. For nonzero determinant, the integer torus map x↦(q·x,r·x) is a finite Haar-measure-preserving covering, so the strip events are exactly pairwise independent for every shift. The per-shell mass is 2/log(2^k+2), whose sum diverges. Applying the second-moment/Chung–Erdos bound on each tail gives tail-union measure tending to one and hence limsup measure one. Numerically S(10,30)=3.36428, so the record's weaker certified lower bound and <1/2 loss are safe.

## Originality

**FAIL** — The advertised dependence on delta=sqrt(2)-1 is illusory: the proof itself shows the shift cancels completely. More importantly, the result is a direct application of a handpicked pairwise-independent subfamily, Haar invariance of integer torus endomorphisms, and the elementary second Borel–Cantelli/second-moment argument. Existing restricted-denominator inhomogeneous Diophantine literature treats substantially broader and harder lacunary settings. No new ubiquity or mass-transference mechanism is developed here.

## Scientific value

**FAIL** — The theorem is mathematically clean but the current presentation overstates its significance. Because the argument works for every shift and derives full measure from an explicitly engineered independent subfamily, it does not resolve a delicate shift-specific lacunary obstruction. The fixed silver-ratio shift, k>=10 cutoff, and K=30 overlap ledger are inessential decorations. A more general abstract lemma could be useful pedagogically, but the record as written does not deliver a research-level advance over standard probability plus existing restricted-denominator theory.

## Limitations

- No claim is made that an identical two-dimensional dual statement appears verbatim in the cited papers; the originality failure rests on the elementary, shift-independent reduction to pairwise independence.
- The audit addresses Lebesgue full measure only, not possible Hausdorff refinements.

## Sources

- Inhomogeneous Khintchine–Groshev theorem without monotonicity — Seongmin Kim: https://doi.org/10.1112/blms.70114 — Modern full-height inhomogeneous linear-forms theorem in dimension (2,1); shows the surrounding area already has strong general measure theory.
- Inhomogeneous Diophantine Approximation on M0-sets with restricted denominators — Andrew D. Pollington; Sanju Velani; Agamemnon Zafeiropoulos; Evgeniy Zorin: https://arxiv.org/abs/1906.01151 — Existing quantitative inhomogeneous approximation with lacunary restricted denominators in a broader fractal setting.
- A mass transference principle for systems of linear forms — David Allen; Victor Beresnevich: https://arxiv.org/abs/1703.10015 — General linear-forms transference context; the audited record does not add a new transference principle.

The record was audited independently. GitHub was read only as evidence; no repository write was performed in this chat.
