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

In the orthonormal shifted Legendre basis the endpoint constants in the antiderivative cancel at x=0, and for n>=m>=1 the only coefficients are a_n at n+1 and -a_(n-1) at n-1. The squared column norm is [1/(2n-1)-1/(2n+3)]/8, giving the full Hilbert–Schmidt identity by telescoping. The window Gram matrix is the compression to m<=n<=floor(Rm). For a fixed power j, only paths with steps 0 and +/-2 closing at n contribute to its trace. The scaled entries on each such path are uniformly those of the frozen coefficients at n/m up to o(1) away from O(j) boundary sites; integrating their Fourier symbol picks the closing paths. This gives the stated bulk symbol, including both parity sectors, with normalization 1/m. The shift norm bound makes continuous functional calculus by polynomial approximation valid on a common spectral interval. For p>1 the removed columns have Schatten norm O((Rm)^(1/p-1)); the triangle inequality for the rescaled norms followed by R to infinity justifies the global moment limit. The angular beta integral gives the gamma constant. For finite m, JP_<m has rank at most m and the classical unfiltered Volterra sequence and index interlacing squeeze the tail to 1/(pi j), proving the membership threshold. For the fixed-k edge, the two shift norms give limsup at most 1/2 and a nonnegative continuous function supported above any positive squared threshold below 1/4 detects linearly many window values there. Min–max transfers that lower bound to the full operator. Independent replay: python3 /workspace/review_checks.py 5 checks the first six values at three finite truncations against a separate Bessel-zero characterization, and the finite-window moments for real p=1.25, 2 and 3.7 at R=3. The check is corroboration only; the frozen checker and recorded output were inspected, not executed.

## originality

PASS

The supported distinct contribution is the quantitative spectrum of the high-degree orthogonal input restriction, especially the global all-real-p mass and the fixed-rank edge for that family, not a new abstract spectral-distribution theorem. Classical Volterra, general finite-window symbol methods, and exact/even-power Bessel-zero identities already cover proof ingredients or numerical constants under a reduction; the old sources inspected do not provide the operator identification with those constants. Closest plausible partial coverage and access limits are recorded below.

## value

PASS

Polynomial orthogonality is a canonical spectral preprocessing choice distinct from best rank-m approximation. The sharp worst-case attenuation and all-real Schatten profile quantify both the extremal and distributed residual integration errors, and the exact square mass provides an all-cutoff normalization. The density plus separate outlier and infinite-tail controls address a substantive family of infinite operators, not a finite numerical table or routine reparameterization of the ordinary Volterra spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
