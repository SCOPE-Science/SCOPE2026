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

# Reproducibility and scope of verification

Run `python3 VERIFY.py` under Python 3; it uses only `fractions.Fraction` and `itertools.combinations`. It constructs the actual two-walker transient generator on unordered distinct vertex pairs, sets unit total rates at each walker, and solves the full rational Poisson equation independently of the proof's six symmetry classes. Results are averaged over the uniformly chosen distinct peripheral pair.

The packaged checker reports 32 exact generator-to-closed-form matches for all \(3\le n\le10\) and \(0\le k\le\lfloor n/2\rfloor\), 5,549 exact positive adjacent-increment matches over \(3\le n<150\), and the star and full-matching endpoint identities. The reported checks were executed on the exact packaged program.

The core proof of strict positivity for all graph sizes is the displayed coefficient-positive polynomial identity in `RESULT.md`. The finite checks support its implementation and do not replace the symbolic identity for arbitrary \(n\). The work is self-reviewed; independent audit is not performed.
