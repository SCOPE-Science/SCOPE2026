---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The mathematical Finding is correct. Strict triangular multiplication yields a∧b=b∧c=a∧e+d∧c=0 and leaves f free. At b=0, the r columns in coordinates (a,d,c,e) span a totally isotropic space for a nondegenerate alternating form, also in characteristic two. Every such span extends to a Lagrangian plane. The incidence bundle over LG(2,4) is irreducible, with fiber dimension 2r; its rank-two open locus recovers the Lagrangian plane by taking the span, giving a birational map. The chart of planes transverse to a fixed Lagrangian complement is a graph chart with three symmetric matrix coordinates in every characteristic. With the free f, S is therefore rational of dimension 3r+3. For b≠0, write a=λb and c=μb uniquely. If (λ,μ)≠0, the condition λe−μd∈kb cuts out a vector bundle of rank r+1 over the rational base of nonzero b and nonzero (λ,μ), with f still free; its closure R is rational of dimension 3r+3. The other locus lies in the linear variety Z of dimension 4r. These three sets cover the reduced variety; independent b,d,e separate Z from R and S for r≥3 (rank(b,d,e)≤2 on R); independent a,c separate S from R and Z, and R has b≠0 and nonzero (a,c). At r=2 the extra linear locus is covered as stated by dependence modulo kb. Over F_q, all lines in the four-dimensional alternating space are isotropic, each lies in q+1 Lagrangian planes, and each plane has q+1 lines; thus their common number is (q+1)(q²+1). Counting spanning column tuples of ranks 0,1,2 gives the three terms at b=0, and at b≠0 the two scalar cases yield q^{2r} and (q²−1)q^{r+1}. Multiplying by q^r for f proves the formula and its r=1 boundary. The finite arithmetic examples agree with the formula. The uploaded verify.py was inspected, not executed; its small tuple and adjoint-rank counts do not establish the geometry. The limitation paragraph's exclusion of group-commuting tuples is misleading for ordinary commutation in this very UT4: translation by I is an isomorphism of the reduced varieties and a bijection over each finite field. This does not invalidate the Lie-algebra Finding or imply a result about arbitrary groups or genus commutator equations.

## originality

FAIL

There is demonstrable earlier exact coverage. The 2026-10-13 unitriangular Resultary theorem has the same reduced varieties by translation, gives the same three components with the same dimensions in arbitrary characteristic, and supplies the identical all-prime-power tuple-count formula. Rationality is not explicitly named there but is a direct consequence of its dense coordinate charts, so it does not leave an original substantive remainder.

## value

FAIL

A new complete component classification of this natural variety would be valuable, but the frozen contribution repeats a known classification and known tuple counts verbatim in substance. Rationality is mechanical from the earlier open charts. The symplectic incidence description gives a correct alternative proof, but the frozen record does not extract a new geometric invariant, point count, or other independently useful result from it. No genuine surviving claim warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
