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

Starting at a tagged uniform site gives an independent uniform phase and cyclic Dirichlet spacings E_i/T from independent unit exponentials. The sum of the two adjacent gaps is Beta(2,n−2), independent of their uniform left fraction. For B_i=E_i+E_{i+1}, the single and adjacent-double exceedance probabilities are (1+u)e^{-u} and 2e^{-u}−e^{-2u}; at the stated center the total adjacent-double contribution is O_x(1/log n). Removing separator indices including at the circular seam loses o(1) expected points; the summed within-block pair bound is o(1) and also bounds the intensity lost by dropping blocks with multiple points. The independent rare blocks have the product intensity from the height tail, grid and exact ratio independence. Uniform partial-sum control and the independent rotation give the spatial limit, while the common scaling n/T changes the entire height array by O_P(log n/√n). The gamma upper-tail bound prevents escape to +∞, and a low cutoff has vanishing limiting probability of missing the top as the cutoff tends to −∞. Distinct neighboring exponential pairs give no exact top tie for n≥3. For counts the cyclic Chen–Stein error about the finite mean is O_x(1/log n); the shift from that mean to e^{-x} costs O_x((1+log log n)/log n). A Chebyshev good event for T/n and a union bound at the two shifted Gamma thresholds cost only O_x(n^{-1/3} log n).

## originality

PASS

Pass rests on the explicit joint asymptotic process with the circular left/right split mark and the independence of the maximizing split. Unmarked k-spacing and spatial extremes, classical count approximations, and the determination of the full finite law are relevant existing coverage; neither the tagged identities nor the count-rate priority is the basis of the pass.

## value

PASS

An extreme Voronoi cell can arise from an almost one-sided gap or from comparable gaps. The theorem gives the limiting distribution of that imbalance for all extreme cells and for the maximizing cell, which cannot be read from unmarked maxima or counts. Uniformity of the maximizing location alone follows from rotational symmetry; the added content is the asymptotic split factorization across the extreme field.

The dated certificate retains the supplied scientific assessment, sources and limitations.
