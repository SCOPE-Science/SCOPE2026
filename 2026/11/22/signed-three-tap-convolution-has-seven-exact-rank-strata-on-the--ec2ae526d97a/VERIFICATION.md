---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Left-normalization multiplies the regular convolution matrix by an invertible left translation and gives I+L_a-L_b. A matrix column y is delta_y+delta_(ay)-delta_(by), with three distinct supports; every row also has exactly three +/-1 entries. Swapping the two positive sites re-normalizes to (a^-1,a^-1 b); S_5-conjugation is a simultaneous A_5 automorphism and preserves rank. Each original kernel has exactly two ordered descriptions, so a normalized-pair count is multiplied by 60/2=30. Independently generated all 3422 normalized ordered pairs and 23 disjoint exhaustive orbits, and checked every pair's intrinsic rule and modular rank at both primes, not just representatives. Normalized counts for ranks 40,45,49,54,55,56,60 were 60,120,120,120,240,360,2402, exactly giving the stated 102660-kernel census. For (3,(5,5),60), 120 same-class pairs had rank 49 and 120 different-class pairs rank 60; the two five-cycle classes were computed and found inversion-stable. The CSV representatives, orbit sizes and order invariants agree. Both primes were checked by trial division. Each integer minor of size k<=60 has |det|<=3^(k/2)<=3^30 by Hadamard, less than the product of the primes. Thus agreement at d<60 forces all (d+1)-minors to vanish integrally while a nonzero d-minor mod a prime yields the lower bound; d=60 is maximal. All signed 64-bit elimination products and subtractions stay within range. The conclusion concerns complex rank and geometric nullity, not algebraic zero-eigenvalue multiplicity. Replay: python3 /workspace/branches/14658e4f-ea82-449c-8709-0e66eaa4030d/independent_check.py. The uploaded CSV and both checker sources were inspected but no uploaded program was executed. This is exhaustive for the stipulated finite signed domain only.

## originality

PASS

Best-of-knowledge pass for the exact signed A5 classification, not for group Fourier decomposition, three-point support geometry, the existence of split 5-cycle classes, or modular elimination. The closest A5 classification is explicitly unweighted in the available statements; the signs cannot in general be removed, and the distinct signed ranks are independently verified. No retrieved stronger theorem or exact catalogue entry covers the signed enumeration; plausible unread primary statements remain a disclosed risk.

## value

PASS

The signed coefficients are a natural minimal change from an unweighted 3-site filter on the smallest nonabelian simple group; the theorem gives a complete fixed-coefficient invertibility/nullity classification rather than selected examples. A full-generating support geometry with identical group and quotient orders can yield rank 49 or invertibility depending only on the relative five-cycle classes. The exact signed counts and order test are useful group-algebra benchmarks, without making claims about condition numbers, general complex coefficients or other groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
