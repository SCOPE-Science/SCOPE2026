---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Exact finite verification

The standalone file `noncrossing_reflection_verify.py` constructs all chord orbits under \(\tau_k(i)=k-i\pmod n\), excludes internally incompatible orbits, and constructs the complete orbit-conflict graph. It enumerates each nonempty independent set once, builds signed integer simplicial boundary matrices, checks all adjacent boundary compositions equal zero, and computes integral Smith normal forms using SymPy. Every nonzero invariant factor is 1 in all 15 tested conjugacy-class cases at \(3\le n\le12\). The chord-conflict predicate is cross-checked using a separate cyclic interleaving implementation on 6,006 pairs of chords.

For \(n=12\) and the side-axis reflection \(k=1\), the exact face counts are \(21,85,100,48,11,1\) and boundary ranks are \(20,61,38,10,1\). The homology is \(\widetilde H_1\cong\mathbb Z^4\), \(\widetilde H_2\cong\mathbb Z\), and zero otherwise. The other axis has only \(\widetilde H_1\cong\mathbb Z^3\). The table for all smaller polygon sizes is in `RESULT.md` and in the checked program output.

Run `python noncrossing_reflection_verify.py` with `sympy>=1.12,<2` and compare the output with `noncrossing_reflection_verification.txt`. The final output marker is `NONCROSSING_REFLECTION_INTEGRAL_CERTIFICATE_PASS`. The calculation uses exact integers, no numerical approximations. The all-case finite-exhaustiveness argument is contained in `RESULT.md`; a finite computation is not used to claim an infinite family theorem.

Limitations: finite polygon sizes at most 12; geometric fixed loci only of reflections; no homotopy wedge decomposition or additional independent validation is asserted.
