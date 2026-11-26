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

RESULT.md lines 22–79 checked algebraically. The inverse length-N DFT gives cyclic correlations with the stated sign; the three zero-lag moments have determinant UV(A−B)^2 and identify the sparsity tier. Away from the self-inverse lag, the ratio gives the ordinary support sum, and the zero-lag recurrence gives the two distinct nodes q^a,q^b as quadratic roots. Support ordering then selects the correct signed lag. At the self-inverse lag, the ramp rotates the product by i, giving C2(h)=−2q^(a+b) Im P. If Re P is zero, two candidate left nodes X<Z<2X force t=R(X+Z)/(R+1), R=2. In the squared-lag difference, substituting gives t−X=(RZ−X)/(R+1) and RX−t=R(RX−Z)/(R+1), with the analogous swapped expressions at Z. The common nonzero factor then multiplies X^2−Z^2, excluding equal data. Zero, singleton and opposite support types are distinguished by the moments and lag locations. The conjugate witness for real masks retains the first entry and all real cross terms and cannot differ by a common phase. The amplitude bounds follow from j<N. I inspected CHECK.py rather than executing it; its finite tolerance checks are supplementary, and the result makes no noisy-recovery or general-signal claim.

## originality

PASS

This pass is for injectivity of the specifically prescribed geometric amplitude profiles and linear phase ramp. Existence of a bounded-contrast even-cycle design and the real-mask obstruction are covered by other catalogued results; neither is credited as a distinct contribution. In particular, three is not the optimal unrestricted mask count. The stronger two-mask existence theorems do not assert injectivity for these prescribed masks or supply the moment disambiguation where the amplitude-pair product code is not injective.

## value

PASS

The result gives a natural alternative design when one wants smooth elementary profiles: all three masks have constant log-amplitude step and constant phase step, and the complex ramp gives exact quadrature at every antipode without a coded coordinate sequence. Pair-sum collisions and overlapping antipodal moment intervals prevent the simpler two-mask support tests from being substituted; the third intensity supplies a mathematically useful way around those constraints. This is value as a structured design and a reconstruction argument, not as a mask-count, contrast, or noise-stability improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
