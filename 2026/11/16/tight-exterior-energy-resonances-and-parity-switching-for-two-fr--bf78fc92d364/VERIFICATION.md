---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Removing a unit-modulus common carrier writes f=A cos(dt/2)+B sin(dt/2). Both symmetric I and E_h kill all even/odd cross terms for arbitrary complex coefficients; exactly integrating gives diagonal input weights 1±s(d) and output h±q_h(d). Since |sin d|<d for d>0, generalized Rayleigh quotient is the larger of two ratios, with complete equality directions. Their deviations from h are (q_h-hs)/(1+s) and -(q_h-hs)/(1-s), so at least one is >=h, and both equal h exactly when F_h(d)=sin((1+h)d)-(1+h)sin d=0. At successive (n+1/2)pi, F_h has strict alternating sign because 1+h>1; therefore every intervening gap interval has a root and winner parity changes. Expanding sin produces odd-branch limit h(h²+3h+3) and coefficient -h(h+1)^3(h+2)/20 at d². Independently recomputed the two ratios for h=.4,1.2,2.3 and d=.3,1.7,5; each max exceeds h away from a root. This is supplementary; analytic parity/IVT establishes infinite sharp set.

## originality

PASS

Best-of-knowledge PASS after separate formulation/implication comparisons, published-result search, and bounded primary-literature inspection; not a certification of absolute historical priority. The novel implication direction is from symmetry/diagonalization to gap equalization; neither prior global transfer inequalities nor single-point leverage imply these zeros and switches.

## value

PASS

The integrated two-frequency exterior energy transfer is a natural stability object in sparse Fourier extrapolation. In contrast to a point-evaluation bound, its sharp entire generalized spectrum, exact gap-wise infimum, infinite perfectly equalized resonance gaps, and mandatory parity switching form a motivated sharp design theorem, even if its diagonalization is elementary after finding the right parity basis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
