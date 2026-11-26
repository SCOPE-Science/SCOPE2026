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

In column coordinates the equation is M^T x^[2]=x, so inversion and transposition give uniform A with x^[2]=Ax. The solution space is F_2-linear. A minimally field-dependent set of independent F_2-solutions would give a relation whose coefficients are unchanged by squaring, by subtracting the relations obtained from applying A and squaring coordinates. This contradicts F_2-independence and bounds the dimension by n. Every F_q independent k-frame has an equally independent squared frame; the number of matrices sending it to that frame is the group order divided by the number of frames, by transitivity. Thus all ordered fixed-frame moments equal 1, including k=0 and k=n. The resulting triangular system has diagonal |GL_k(F_2)|>0 and uniquely determines the same law as over F_2. Pointwise stabilizers of d-spaces have order 2^(d(n-d))|GL_(n-d)(F_2)|; subspace Möbius inversion gives the asserted formula. The no-idempotent probability tends to the binary Euler product by absolute convergence and expansion of that product. Independently enumerating binary matrices in dimensions 2 and 3 by testing bijectivity on all vectors gave exact histograms (2,3,1) and (48,98,21,1); the seven-letter derangement count from its recurrence is 1854. Dimension one has one nonzero idempotent. Conjecture 2's following limit statement does not restrict q to odd characteristic: its unrestricted-prime-power reading fails, not the characteristic-zero Galois-group assertion. The frozen checker was inspected, not executed.

## originality

FAIL

Exact theorem-level coverage is established by the separate earlier-dated 2026/10/25 Resultary record. It gives the entire distribution and the same Gaussian Möbius probability formula under the identical uniform invertible-matrix model. It counts all idempotents: subtracting the zero idempotent translates every outcome to the present theorem. The frame proof is a different exposition, but the claimed law is not distinct. The surveyed limit discrepancy is real, yet its characteristic-two counterexample at n=3 is an immediate consequence of the prior all-field law and its explicit dimension-three table.

## value

FAIL

The law is mathematically useful, and the short frame proof and wording correction can be useful expositively. As submitted, the principal result nevertheless restates an existing exact law and table. The proposed asymptotic contrast takes a listed dimension-three probability from that law and compares it with a standard derangement count; it does not produce an independent exact invariant or substantive new boundary. No distinct valuable remainder is established for a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
