---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Each nonzero differential term replaces an edge generator by its two endpoint generators and preserves all multiplicities w; terms with repeated exterior generators vanish. This is a direct sum of finite subcomplexes, so summing the absolute weight Euler characteristics gives a bound on total cohomology, not a formula for it. For binary vertex and edge masks a,b, the admissibility relation is a_i=w_i−b_{i−1}−b_i, and the sign is (−1)^(sum w−sum b). Thus the four matrices have the displayed column signs, and the trace imposes cyclic consistency including the wrap edge. The independent transition table has 25 reachable distinct matrices, closed under all four right products. It verifies all 25 coordinates of T(T^4−3T^3−4T²+8T+8I)q=0 for q(A)=|tr A|. The identity is applied after at least one transition: S_1 through S_4 are 4,12,36,116, and the polynomial factors as (z²−2z−4)(z−2)(z+1), the four bases of the stated formula. This proves the exact Euler sum even though sampled cohomology need not exhaust all n. The indicated initial bounds and Binet asymptotic then follow. For an induced vertex set, its cochains comprise precisely the summands of the full complex supported on subsets of that set, including constants; the complement is invariant. Thus the rational cohomology inclusion splits using the standard invariant-forms identification, with no independence assumption on the graph edges outside the cycle. The graph assertion begins at n=3. The supplied Python script was not executed; Python 3.10+ is needed to run its bit_count() check. Its internal independent cross-check does not by itself constitute a separate audit.

## originality

PASS

The claim is an exact all-length evaluation of the weight-Euler lower bound, not a new induced-subgraph principle or the first exponential growth bound. Paths already furnish the same exponential base via a weaker induced-path estimate, and the exact fixed-cycle computations already cover particular n. Those results do not supply the uniform Lucas expression or its parity correction.

## value

PASS

The all-length cycle bound gives quantitatively stronger explicit Betti information than inserting just one induced path or using diameter, and may be used for cycles in larger graphs without computing their cohomology. The signed transfer finite-state identity isolates a reusable measure of multigrading cancellations, with exact Lucas and parity terms rather than a fitted growth rate. In particular it quantifies a diameter-blind phenomenon, while the exponential base alone is not new. No general equality, cohomology-ring computation or integral statement is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
