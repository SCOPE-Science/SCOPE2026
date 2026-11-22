---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and mathematical limits

The exact spatial numerical-range orbit is obtained by substituting the norming functional of complex \(\ell_p^2\) into the two-sided coordinate flip. Its imaginary part reduces to one scalar modulus ratio and one phase. The top height is a one-variable maximum; its unique root follows from an explicit monotonic derivative. Setting the real part to zero removes the phase and gives a constrained scalar maximum. At \(p=4\) the squared modulus-balance substitution reduces this to the rational function \(u(1-(1+4\delta^2)u)/(1+u)^2\), whose unique global maximizer is \(u=1/(3+8\delta^2)\). The proof covers every real split analytically.

Run `python3 CHECK.py` using Python 3 and only its standard library. The run produces `AXIAL_GAP_DIAGNOSTIC_OK 2246` after direct norming-functional comparisons, quartic witness tests, constrained scalar maximizations, and sampled asymptotic checks over multiple exponents and split sizes. These checks cannot establish the continuum theorem, the bibliographic originality of the result, or independent scientific validation; those matters are addressed separately in the mathematical proof and literature comparison. The quantitative general-exponent laws hold for each fixed \(p\ne2\), and the explicit global quartic formula does not extend here to arbitrary matrices.
