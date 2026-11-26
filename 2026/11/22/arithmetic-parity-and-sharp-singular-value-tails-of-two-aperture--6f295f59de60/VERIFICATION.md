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

Fourier integration of the unnormalized boxes gives |K̂(n)|=F_n/|n| with F_n=(2/π)|sin(πna)cos(πnb)|. Both signs of n contribute, so the coefficient is twice the mean of F_n. To justify the threshold limit even with atoms, for B=2/π the finite measures t∑_{1≤n≤B/t}δ_{(tn,F_n)} converge to Lebesgue on [0,B] times the limiting empirical measure: on any fixed block in tn, subtract the two initial-segment averages and then approximate a continuous joint test function by blockwise tests. The diagonal boundary F=tn has product measure zero. The limit is the layer-cake integral, hence the mean. To also check the initial existence claim for any admissible b, not just the three evaluated cases, take the orbit closure H of (a,b) in the torus. Each character averages to zero unless it is trivial on H, by the geometric sum, yielding Haar equidistribution on H. The continuous F is positive at n=1 unless b=1/2, in which case use n=2; its Haar mean on H is therefore positive. Independent coordinates give means 2/π for both factors. Rational residue classes give the same sine mean and a numerator permutation of the absolute cosine values. Summing the positive cosines paired about 0 gives cot(π/(2q)) for q even and csc(π/(2q)) for q odd. The normalized ratios x cot x and x csc x sit strictly below and above 1, respectively, and their monotonicity gives the sharp rational extrema q=2 and q=3. Only even q gives zeros and then exactly n≡q/2 mod q. On b=2a, the change of variable v=cos(πu) gives ∫_{−1}^1|2v²−1|dv=(4√2−2)/3, which gives the stated constant after normalization and doubling. Monotone inversion of the strict count gives ks_k→C, and harmonic comparison gives both Schatten and log-sum results. Inspected check.py and VERIFICATION.md; the frozen finite checks were not executed and are not used to establish a limit.

## originality

PASS

The distinct content is the coherent two-aperture singular-value count with its exact rational denominator-parity laws, rational extrema, and dependent irrational contrast. The Fourier-zero classification is already covered and is not credited; a distinct one-boxcar spectral result gives a close analogue, not these coherent two-boxcar coefficients.

## value

PASS

This is an exact spectral-resolution invariant of a natural coherent convolution. It distinguishes operators with no missing modes and separates the two rational parities on opposite sides of the generic irrational density; the rational extrema and b=2a show why neither a nullity count nor irrationality alone suffices. The result quantifies the ordered spectrum and is not credited as a stability guarantee or a complete evaluation for all dependent irrationals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
