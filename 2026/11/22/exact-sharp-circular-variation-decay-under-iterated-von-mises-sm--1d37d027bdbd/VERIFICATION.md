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

For even kernels a,b the derivative of their convolution on (0,pi) is the integral of a'(u)[b(theta-u)-b(theta+u)] over (0,pi). The bracket is positive because the first argument has strictly smaller geodesic radius; k_beta'<0 initially and strict negativity follows for every iterate. For such a kernel h the positive set of h-h_delta is (delta/2-pi,delta/2) for 0<delta<=pi, and the derivative of its positive mass is h(delta/2)-h(pi-delta/2)>0 inside that interval of separations. Thus the half-L1 distance is uniquely maximal at pi, with value 2 times the centered semicircle mass minus 1. For Df of total mass zero, use the PRODUCT of the two normalized Jordan measures in the coupling estimate: equality requires this product to be supported on y=x+pi, so the marginals must each be singleton atoms. The resulting derivative measures are precisely those of translated/scaled semicircle steps, and attain the bound. After any positive iterate the derivative of such a step is a nonzero smooth density, so equality in the product norm bound is impossible. The Fourier convolution normalization gives the stated Bessel powers and 4/pi factor; positivity and the Bessel recurrence make I_1>I_3>I_5>0 and bound the absolutely summable remainder by O((I_3/I_0)^r). At r=1 the deficit equals 2/(pi I_0) times the integral of exp(-beta sin u) on [0,pi/2], asymptotic to 1/beta before the prefactor. This gives the stated large-beta constant; the small-beta linear coefficient follows by expansion. Independently checked the formula by cyclic FFT on 32768 samples and sampled shifts at beta=0.1,1,5,10,30 and r=1,2,3,5,20; separately checked large-beta tail quadrature. These numerical tests do not prove universal inequalities.

## originality

PASS

The supported distinction is the sharp all-iterate result for the von Mises kernel, including the exact constants and saturation in that setting. The zero-mass/TV norm reduction is classical, nearby circular heat work uses the same reduction and rigidity mechanism for a different kernel, and the Struve evaluation and endpoint asymptotics use standard identities. No inspected distinct source gives a general theorem already covering the whole von Mises iterate result or the same kernel's sharp rigidity and constants. This is a bounded comparison, not a priority claim.

## value

PASS

Von Mises is a standard circular smoothing kernel. A user choosing a concentration and a number of iterations gets the exact worst-case variation loss, not just a Markov contraction bound or a risk formula, and learns which inputs attain it. The norm of repeated smoothing is strictly better than repeated multiplication of the one-step bound. Kernel-specific normalization, strict preservation of shape and the equality-based obstruction are meaningful parts of that answer, even though the special-function evaluations and the basic contraction mechanism are standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
