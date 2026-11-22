---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For arbitrary prime-power q=p^f and n>=1, derivations of the nonunital ideal B_n are exactly D_b(x)=x' b with b in tF_q[t]/(t^(n+1)), because D is determined by D(t) and the defining relation adds no condition. If s is the least index of an x coefficient with p not dividing s, then x' = t^(s-1)u with u(0) nonzero; hence {D_b(x)}=t^s B_full. If x'=0, every D_b(x)=0. This proves necessity of zero columns at p-multiples and columns supported in degrees >=j elsewhere, and sufficiency for every x, not merely the basis. The count of free cells gives D=sum_{p not|j}(n-j+1). Ordering eligible columns j_i descending nests each available column space U_{j_i}; with span dimension s there are q^s choices to maintain rank and q^d_i-q^s to raise it. Thus the recurrence and product are exact. The full-rank probability exponent satisfies d_i-(i-1)=1+floor(n/p)-floor(j_i/p), giving the stated residue product; the positive infinite product follows from a summable deficit. Edge cases n<p, n=p, n=1 and r=0 are encompassed. Independently authored GF(2), GF(3), and GF(4) Gaussian elimination enumerated structural matrix rank profiles (n,p,q)=(1,2,2),(3,2,2),(4,2,2),(5,2,2),(3,3,3),(4,3,3),(3,2,4),(4,2,4), including extension field F4 via a^2+a+1; all matched the recurrence and rational products. Separately, all linear maps were directly tested against all possible Leibniz derivation values for (n,q)=(2,3),(3,2),(4,2): 27,16,64 local maps respectively, matching the structural counts. These finite checks corroborate, but do not replace, the all-parameter proof.

## originality

FAIL

The joint implication of prior primary theorems covers the asserted finite local-derivation space and all rank counts: Zielinski (2002), Theorem 8, classifies every local derivation on k[[t]] as a sum f_j h_j with h_j(x)=j[x]_{t^j}t^{j-1}. For the nonunital quotient, restrict to f_j in t k[[t]] and j<=n; this gives exactly arbitrary image columns in t^j k[t]/(t^{n+1}) when p does not divide j, with zero columns when p divides j. Conversely any finite local derivation has precisely these columns by its pointwise Leibniz-image condition, and the extension by f_j=Delta(t^j)/(j t^{j-1}) is covered by Theorem 8 and descends to the finite nilpotent quotient. The allowed matrix support is a Ferrers shape after row reversal and deletion of zero columns. Haglund's general rank-distribution theorem, reproduced as Theorem 1.9 by Cotardo-Gruica-Ravagnani (2023), already counts matrices of every rank on any such shape; the displayed recurrence, maximal-rank probability, and its residue limits are direct nested-column counting and elementary grouping. No identical displayed product was located, but matching wording/numbers is not required for mathematical coverage. The complex-only Theorem 5.1 of Abdurasulov et al. alone does not cover characteristic p. The Leibniz-algebra Resultary results concern different multiplication and are not used for this prior-implication conclusion.

## value

FAIL

The algebra is natural and its characteristic-dependent rank-density statistic is meaningful as an example. But as a proposed independent discovery the exact operator space is the direct finite quotient/ideal restriction of Zielinski's complete local-derivation theorem, the full rank spectrum is an ordinary Ferrers q-rook specialization, and the displayed product/residue limits arise by one nested-subspace count and grouping factors. No new structural obstruction beyond those already encoded in h_j, distinctive unknown invariant beyond the covered specialization, or independently motivated conceptual advance is supplied. The p-periodicity is a genuine correct observation, yet insufficient here to turn a mechanical combination of known complete classifications into a new mathematical contribution. Reproducible finite verification is not a value substitute.

The dated certificate retains the supplied scientific assessment, sources and limitations.
