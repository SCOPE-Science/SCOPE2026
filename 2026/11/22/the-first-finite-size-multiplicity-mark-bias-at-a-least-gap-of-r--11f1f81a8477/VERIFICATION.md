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

The shift for stopping at permitted u_j with mark a is sS_{j−1}+a u_j, and forbidding another copy multiplies the partition product by 1−q^{u_j}. Marks telescope to the unmarked count, including n=0. For a<b, the difference kernel has bracket e^(−a x)(1−e^(−(b−a)x))(1−e^(−x)), x=z u_j. Its quadratic term is (b−a)x², with O_s(|x|³) remainder for Re x≥0 (Taylor bounds along the segment to x for |x|≤1, direct boundedness otherwise). For t=Re z and |Im z|≤t^(3/2−δ), |z| is comparable to t. With u_j=j/ρ+O(1) and S_{j−1}=j²/(2ρ)+O(j), summing the Taylor remainder and the replacement errors against a Gaussian gives O(t): the errors are bounded by constants times t³ sum j³ exp(−ct j²) and t² sum j exp(−ct j²). Summing the main x² Gaussian rather than integrating incurs O(t) too, by integrating the absolute derivative of x² exp(−s z x²/(2ρ)) on the positive real axis (this integral is O(t^−1), before multiplying by z²). The complex integral yields (b−a)√(π/2) z^(1/2)/(s^(3/2)√ρ). For coefficient transfer, the eta-product quotient has leading factor ℓ^−1/2 exp(μ/z+(ℓ−1)z/24), μ=π²ρ/6. The modulus deficit off the central arc follows from the product over m≈1/t: for small angles the permit-class cosine deficit is Ω(θ²t^−3); for angles |θ|≥t it is Ω(t^−1) by residue-class geometric sums. In the only resonant subsequences θ→2πh/ℓ, a bounded scaled detuning gives the mean cosine as Re(residue average × integral over [1,2]); this cannot be 1 unless h=0 and detuning is zero, excluded by |θ|≥t. Unbounded scaled detuning gives zero mean cosine. Thus the polynomially bounded kernel leaves the minor arcs exponentially negligible. With t=√(μ/n), phase μ/z+nz has central quadratic term −μθ²/t³, and cubic remainder O(t^(1/2−3δ)) on the stated arc (0<δ<1/6). The same nonzero Gaussian factor cancels in the numerator/denominator, and z^(1/2)/t^(1/2) tends uniformly to 1. This proves the difference on the n^−1/4 scale, not by subtracting two leading marginals. Multiplication by μ^(1/4) gives the claimed C; normalization gives the linear mark profile. Earlier parts have at least s copies, so M_r=M_s iff J_s<r; the sum of the first r coefficients is r(s−r)C/2. An independent exact replay using Euler logarithmic-derivative counts and direct multiplicity-vector enumeration checked 875 mark vectors and 2625 tie counts. Its finite diagnostics are not a proof of the limit. Replay: python3 /workspace/branches/replay2.py; output /workspace/branches/replay2.txt.

## originality

PASS

The positive finding is specifically the explicit signed n^−1/4 multiplicity-mark expansion and its equality-event consequence. The paper arXiv:2611.07871v1 already encodes the exact mark counts by splitting its finite geometric sum at the stopping part, contrary to a possible reading of the frozen prior-work paragraph. The exact identity is not credited as original. Location limits, the previously studied leading unrestricted mark law, and the closely related regular-partition residue-bias theorem do not give this coefficient for the actual stopping multiplicity in their statements.

## value

PASS

The leading uniform mark law or continuous locations miss a systematic signed difference between early multiplicities. The first correction has a sharp nonzero constant for every comparison of distinct marks and quantifies positive coalescence relative to r/s for every fixed 1≤r<s. This is information about a discrete equality event, not merely an improved error bar on an existing limit or a rebranding of the known exact generating function.

The dated certificate retains the supplied scientific assessment, sources and limitations.
