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

# Reproducible checks and limits

The analytical proof in `RESULT.md` covers every integer pair \(2\le p\le q\), including the case \((p,q)=(2,2)\) and all possible rank-inequality support-plane equalities. The computational tests below corroborate specific finite instances only.

Run `python3 verify.py` using Python 3. The script depends only on the standard library (`fractions`, `math`). Its expected terminal marker is `BICLIQUE_TREE_INBALL_CHECKS_PASSED` with 704 profiles, 187924 rank-orbit distance checks, and eight finite scaling checks. In each profile the checker derives the slack of every subset-rank orbit from its definition and compares the resulting squared support distance using exact rational arithmetic. It additionally checks every orbit attaining the least rank distance, the exceptional four-cycle, the two inradius candidates and the circumradius algebraic identity.

A separate independent numerical optimization check constructed the full matrix of nonnegativity and subset-rank constraints in affine coordinates and maximized the inscribed-ball radius using a linear program (SciPy's `linprog`, HiGHS). The ten tested bipartitions were \((2,2),(2,3),(2,4),(2,6),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)\). Every optimized radius matched the formula with absolute discrepancy below \(10^{-12}\); returned optimizers showed displaced centers in several predicted nonunique cases. This numerical cross-check is described, not used as an infinite certificate.

The central analytic lemma reduces each subset-rank inequality to the function \((A(1-z)+Bz)^2/[mz(1-z)]\), and partitions on the exact relation \(2r\ge q+1\). This is the nonstandard step on which the global result depends. The checker cannot establish the inequalities for untested values, nor can it establish historical novelty. No independent audit or independent validation of this mathematical result has been performed.
