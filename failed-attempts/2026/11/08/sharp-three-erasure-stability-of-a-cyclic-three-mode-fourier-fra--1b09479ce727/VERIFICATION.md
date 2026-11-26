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

The columns are orthonormal, so the retained Gramian is I minus the erased Gramian. The latter has all three eigenvalues of the erased row Gramian, and diagonal dephasing gives N^(−1) times a matrix with diagonal 3 and kernel K. For a consecutive mask the odd reflection eigenvalue is 3−v and the even block has roots 3+(v±√(v²+8u²))/2; since u>v≥0 the plus root is largest. Subtracting the three scaled values from one gives exactly the displayed retained spectrum. If N≥8, every nonadjacent absolute kernel entry is ≤v; a nonconsecutive mask has at most one adjacent pair, so its absolute kernel matrix is bounded by edges (u,v,v), strictly below the consecutive matrix after alignment. The Rayleigh modulus inequality and strict nonnegative spectral monotonicity give the needed strict inequality. At N=6, the bound 4+√3 is less than 3+2√2. At N=7, t=2cos(2πs/7) satisfies t³+t²−2t−1=0 for s=1,2,3 by summing the seventh roots in conjugate pairs. Setting z=t+1 gives exactly the paper's cubic. Its signs locate the three ordered roots in (2,9/4),(0,1),(−5/6,−3/4); the small-root comparison and rational bound (9/4)²+8(5/6)²<(33/10)² put all nonconsecutive top eigenvalues below 29/5, while 3+2√2>29/5. Vandermonde minors show positive definiteness for each retained mask. Translation preserves distance, and for N≥6 the N consecutive translates are distinct.

## originality

FAIL

The sharp lower squared singular-value bound and the exact set of worst masks also appear in two distinct same-date Resultary records. The entire retained spectrum is already implied term by term by frozen record 4's explicit consecutive erased spectrum and its Gram-complement identity. This is demonstrable equivalent coverage, not an assessment of priority among same-day reports.

## value

FAIL

The sharp lower bound has genuine use as a worst-case stability constant, but the core claim is already covered by the matched records. The nominal extra spectral characterization is a direct affine transform of record 4's three existing eigenvalues, with no distinct invariant or further extremum established as a contribution of this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
