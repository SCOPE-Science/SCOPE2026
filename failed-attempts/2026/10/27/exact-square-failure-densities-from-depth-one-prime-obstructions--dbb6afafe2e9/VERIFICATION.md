---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For reduced u_n/v_n=(x_0+...+x_n)/h, the next pair is (u_n²+v_n²,u_nv_n) and remains coprime. With g=gcd(h,u_n), Q_{n+1}=(u_n+2v_n)/g=(u_{n-1}+v_{n-1})²/g for n≥1. An odd prime dividing g precludes integrality by coprimality; if g has no odd prime and is even, it equals 2 since a sum of two odd squares is 2 mod 8. Division by 2 then precludes an integer square. This independently establishes the imported criterion. Over F_p, 0 maps to infinity and infinity is fixed. For p≡3 mod 4 zero has no preimage; for p≡13,17 mod 20 the two roots of -1 have no preimages since the discriminant -5 is a nonsquare; over F_2 the sole preimage 1 has no preimage. Thus an incident prime can affect Q_2 only. Matching the valuations of x_0 and h at an active p reduces the obstruction to one or two residue classes modulo p^{a+1}, and the CRT yields the stated counts, including 167·287=47929 at h=221. For least period, the nonempty no-failure set is a product of nonempty local good sets; any period must preserve each local set and its complement under translation. A nontrivial translation modulo p^{a+1} has orbit lengths divisible by p, incompatible with 0<r_p<p. Hence each active modulus divides a period; the empty product gives period one. The supplied verifier was inspected, not executed; the finite-field loop tests active primes rather than all eligible inert primes, which are handled analytically.

## originality

FAIL

An earlier Resultary finding explicitly identifies the same support criterion for no failures after index 2 and computes the same local counts. Substitution into its CRT law gives the exact frozen density and examples. Earlier more general density records also cover the fixed-h distribution. The new presentation does not isolate a distinct exact result.

## value

FAIL

The original distribution question is meaningful and the uniform one-failure boundary would be valuable if unknown, but both that boundary and the local inputs to all the claimed densities are already determined. Product substitution, the sample counts, and the elementary least-period consequence leave no independently valuable new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
