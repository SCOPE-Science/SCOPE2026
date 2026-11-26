# Independent mathematical audit

## correctness

PASS

Reassessed the complete replacement finding in /workspace/repairs/5. Stabilizer averaging proves the kernel is proportional to the monic hypergeometric orthogonal cubic, constant diagonal fixes it to d_3 h(J)/h(k), and transitivity, symmetry and idempotence give the common absolute-row-sum norm and E K²=d_3. The repaired sparse limit follows from the overlap factorial moments, positivity of the limiting Poisson Gram system, h(k)~k³ and uniform integrability via d_3/n³. The factorial generating identity verifies the Charlier cubic. At λ=3 the sole integer root j=1 yields exactly e^(−λ) λ^(3/2)|3−λ|/6 in Φ(√λ); all other terms have continuously differentiable sum, giving 6e^(−3) in the c variable. The four leading terms at λ↓0 and the standardized Poisson cubic at λ→∞ give the stated end behavior. At positive density the hypergeometric CLT and exponential tails give Gram convergence, and (k−μ)/σ=√(n−1) fixes the Gaussian kernel normalization. The original finite formula was also correct (Hahn flux identity and alternating signs including integer roots), but does not survive as a novelty claim. `python3 /workspace/reviews/evidence/reproduce.py 5` independently formed exact inclusion-matrix projections for (6,3),(7,3),(8,4),(9,4), checking norms 2, 16/5, 12/5 and 32/7 and the background finite identity. These checks are not the proof of the limit or cusp; the frozen verifier was inspected, not executed.

## originality

PASS

PASS is for the repaired sparse third-projector Poisson–Charlier profile and its explicit mean-three derivative jump, with endpoint calibrations; it is not a PASS for the original headline finite three-boundary evaluation. The original originality assessment fails for that headline because it follows directly from the classical all-degrees Hahn flux and the three sign changes. The replacement drops that headline and credits the general identity. The closest indexed precedent has integer cusps for the first projector, not the cubic third-projector limit or its jump. The Gaussian comparison is retained as calibration, not as an independent novelty claim.

## value

PASS

The repaired result quantifies the sharp endpoint stability constant of a canonical harmonic projection when intersections have a sparse Poisson law. The first positive overlap j=1 supplies a concrete arithmetic threshold where this constant is nonsmooth, with an exact jump, and the two ends of the profile connect sparse decay to the dense Gaussian scale. This is a useful norm asymptotic and boundary effect, distinct from routine finite Hahn summation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
