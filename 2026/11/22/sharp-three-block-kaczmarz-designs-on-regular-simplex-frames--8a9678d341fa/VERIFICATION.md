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

On the error space H=1⊥, the kernel of a block projection consists of vectors vanishing on that block. Projection preserves the in-block coordinates and distributes their negative sum uniformly outside, verifying the displayed quadratic form. The phrase 'solution space' at RESULT.md line 28 means the ambient error space in the calculation; the actual consistent solution set is a point. Internal block contrasts give eigenvalues p_j for nonsingleton blocks. On the two-dimensional block-constant subspace the projection axes are normalized centered block indicators, and their squared mutual inner products are s_i s_j/[(m−s_i)(m−s_j)]. This verifies the stated determinant for the trace-one mean operator. With two singletons the opposite-singleton test and the large-block contrasts give min(x,m(1−x)/(2(m−1))) as an upper bound. Its unique maximum is t1; equal singleton masses make the tested unit vector an eigenvector of value t1, and the other mean eigenvalue is 1−t1. Conversely equality makes that test vector an eigenvector, and its mixed entry with the other mean direction is a nonzero multiple of the singleton mass difference. With one singleton the mean determinant is strictly decreasing in both large-block masses once both are at least 1/3: in the displayed notation K>B0,C0. At x=y=t2=(m+1)/(3m+1) the determinant equals t2(1−t2). The trace-one eigenvalue criterion and contrast lower requirements force these masses uniquely, and verify attainability. With no singletons all three contrasts bound the rate by min p; uniform masses attain 1/3 since the normalized projections of the orthonormal block indicators contribute at least the identity before multiplying by 1/3. Strict ordering and choosing the pair of singleton row indices yield the global classification and count, also at m=4 where only the two-singleton profile exists. The frozen symbolic/rational checker was inspected but not executed; all-m correctness is analytic.

## originality

PASS

The sharp worst-error projection criterion and general probability optimization are prior techniques. The supported novelty is the explicit joint partition-and-mass optimum, the strict ordering of every three-block profile by its number of singleton blocks, and the uniqueness in each case for this frame and step metric. No distinct inspected statement covers that conjunction. Passage access is limited, so this is not a priority finding.

## value

PASS

This is a natural exact randomized projection design problem on a symmetric tight frame. At equal per-step cost, the sharp guarantee selects the most unbalanced partition and a unique nonuniform mass assignment, and the fixed-profile classification shows exactly which structural change improves the bottleneck. That qualitative design statement is more informative than the small asymptotic gain over uniform masses. It does not assert computational-cost, least-squares noise, or multistep optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
