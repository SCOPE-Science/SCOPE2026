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

PASS. For any sign word s_i=(-1)^b_i the hard-core partition value is exactly trace of product M(s_i)=[[1,1],[s_i,0]] by a bijection with cyclic independent occupation states. Modulo 2 every sign is 1 and M(1)^3=I in GL(2,F2); therefore every multiplier has Lucas parity odd exactly when 3 does not divide n, ruling out zeros in those lengths. At divisible-by-three lengths, --+ gives trace 0; M(-1)^3=-I and four explicitly verified six-sign identity words preserve its zero, giving 3*4^floor((n-3)/6) distinct frequencies. The all-negative word has trace 2cos(n*pi/3) of magnitude 1/2 respectively; parity shows this is the least positive absolute multiplier. Walsh diagonalization of full-group convolution yields the stated exact inverse and pseudo-inverse Hilbert norms, Lucas maximum and condition numbers. Independent exhaustive enumeration of all 2^n signs for n=3..10 confirmed zero-counts 3,18,111 for 3,6,9 and none for others, plus exact matrix-word multiplications. Infinite statement follows from the matrix identities and parity, not finite testing.

## originality

PASS

PASS at best of knowledge: Scott-Sokal classical hard-core transfer formulas are an equivalent representation of the coefficient, but their cited uniform-fugacity trace is not a theorem on simultaneous vanishing/nonvanishing at every inhomogeneous +/-1 assignment. The arbitrary-fugacity partition formula can define every coefficient but does not decide global invertibility without the parity/zero construction. At n>=7 published low-degree no-zero results coexist with high-degree zeros when 3 divides n; hence the low-degree theorem cannot cover the all-frequency dichotomy. No universal historical-priority certification is claimed.

## value

PASS

PASS. Global invertibility of a natural graph-independent-set convolution algebra on F2^n, exact spectral gap, and exponentially many constructed singular frequencies supply a structural all-length classification; both positive and negative alternatives are mathematically motivated, not a routine Lucas parity observation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
