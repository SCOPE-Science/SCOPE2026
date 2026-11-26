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

An idempotent fixes its interval image pointwise; outside the interval monotonicity forces the respective endpoints, giving exactly the clamps. For a clamp on [a,b], commutation forces g(a),g(b) into [a,b]; monotonicity then handles all interior points. On the left, g(a)=a allows all a−1 binary steps anchored at a, while g(a)>a forces a constant tail; on the right g(b)=b is the corresponding free case. These tests are also sufficient and the tail lengths guarantee the ambient range bounds. Given g(a)=a+i, g(b)=a+j, the binomial coefficient counts the internal rises. Rank is one plus the total number of rises, giving the polynomial including h=1, where both tails are free. The baseline sum is h s^(h−1)−(h−1)z s^(h−2) for h≥2, with the single- and double-tail corrections as stated. For the OGF put w=xu, s=1+z, X=1/(1−x), Y=1/(1−xs); after summing the baseline and corrections the numerator over (1−sw)²(1−zw) is zw[X(1−zw)+(Y−X)(1−sw)]². The bracket equals (1−x−zw)/[(1−x)(1−xs)], proving the claimed expression. At u=z=1 the cancellation gives x/[(1−x)^3(1−2x)^2] with the stated coefficients. Summing the n−k allowed starting values over all binary strings of n−1 steps with k rises gives (n+1)2^(n−2) maps for n≥2, and there are n(n+1)/2 clamps, yielding the stated 32/n² asymptotic. Independently enumerated maps and actual compositions for n=1,…,9 matched every per-clamp polynomial and the aggregated OGF coefficientwise with both rank variables symbolic; replay /workspace/branches/06d52e3e-455c-4b1d-9232-20fdbfd08766/independent_check.py (outputs check_n5.txt and check_n9.txt). The frozen checker was inspected, not run.

## originality

FAIL

A distinct indexed result provides the same individual rank polynomials and the same complete joint rank OGF after removing the trivial rank and length shifts. The unweighted totals also have matching indexed coverage and a known scalar sequence. Both Resultary matches have later catalogue path dates; this establishes mathematical coverage in the inspected corpus, not historical priority or attribution.

## value

FAIL

The image-rank distribution of a natural restricted centralizer is a worthwhile invariant on its own. In the inspected corpus the frozen record does not add a distinct invariant or consequence: both full polynomials are already given up to a monomial shift, and the unweighted probability comes from known exact counts. A different rational arrangement of the same series does not supply an additional mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
