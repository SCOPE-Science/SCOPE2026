---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Recomputed using the induced indicators directly. Put H=binom(n,3), U=3(n-3), J=H-1-U. For each fixed triangle, U candidate open triads share one edge (which must be present, leaving two choices of the absent edge), J share no edge (three absent-edge choices), and the identical triple is incompatible. With A_j=(m)_j(N-m)/(N)_(j+1) and q3=(m)_3/(N)_3 the fixed-edge covariance is H[3J A_5+2U A_4-3H q3 A_2]. The independently implemented symbolic difference from the displayed rational formula is identically zero. In the independent model replace A_j by p^j(1-p) and q3 by p^3 to obtain the displayed threshold polynomial exactly. The fixed-edge denominator is positive even at n=4, where B=24-4m is positive in the only nonzero range m=3,4. For n>=5 both coefficients of B in m are positive, and the falling factorials give precisely the stated boundary zeros. In the dense limit B~mn^2, m~pn^2/2, and N-m~(1-p)n^2/2, giving the asserted n^3 normalization and limit. The binomial-edge leading n^4 term is nonzero for fixed interior p other than 2/3. The sign reversal is in the subthreshold region with nondegenerate fixed edge counts, not at every density.

## originality

FAIL

The distinct October 13 indexed result gives the same induced counts, the same finite covariances and sharp sign laws in both ensembles, and the same dense limit. Its compact falling-factorial expression equals the original rational factorization identically. This is documented earlier public catalog coverage, not a claim about any individual's discovery priority.

## value

FAIL

The motif contrast is worth knowing: conditioning changes the sign range and leading scale. But the earlier indexed result already supplies precisely that contrast, with full finite signs and the same limiting constant. The frozen record's equivalent expression and finite recomputation add no new usable invariant, proof insight or broader case beyond the cited prior overlap argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
