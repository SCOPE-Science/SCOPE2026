---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Integrating the four disk fibers gives weight π⁴(1−|z|^(2p))⁴ and beta moments 24π⁵p⁴/product_{j=0}^4(n+1+jp). On the axis all monomials with transverse indices vanish. I reconstructed the quartic separately via S_k=(t∂_t+1+kp)S_{k−1}, S_0=(1−t)^−2: under t=(u−1)/(u+1), put S_k=(u+1)²H_k/2^(k+2), giving H_k=(u²−1)H'_{k−1}+2(u+kp)H_{k−1}. This gives the stated H_4 and hence Q_p by undoing Cayley; Q_p(1)=120 so t=1 is a pole, not an omitted boundary zero. For a nonzero imaginary u=iω one needs ω²=(5p²−2)/3>0; substitution gives −(32/3)(4p²−1)(16p²−1)≠0. At u=0 the two parameter zeros have nonzero linear coefficient in u. The computed Routh pivots 40(16p²−1), 128p(4p²−1) give the stated counts away from exceptional parameters; at p=1/2 there is no axis root and at the two crossings the one simple boundary root is excluded and all remaining roots retain their counts. Every interior t is realized by two axial points; no converse for the full polydisk-fiber domain follows. Read the frozen VERIFY.py and VERIFICATION.md, distinguishing their recorded symbolic agreement from this analytic check. No uploaded program was executed.

## originality

FAIL

The 2007 Demmad–Abdessameud primary paper covers the exact axial count under a ball-fiber reduction, not merely a similar threshold. Compare the egg E_p={(z,W): |z|^(2p)+||W||²<1, W∈C⁴}. At each axial location its transverse ball has 1/24 of the polydisk's volume, independently of the radius. Thus its axial monomial norms are 1/24 as large and its axial kernel is 24 times that of the frozen domain. With the ball as base, E_p is the Cartan–Hartogs domain in that paper with base B⁴, scalar fiber m=1 and μ=1/p. Its representative polynomial P^1_μ at η=1/(1−t) therefore locates the same zeros. The paper's English summary item 5 gives exactly the one- and two-root regimes in Re η>1/2, and Appendix B.5 gives the two parameters μ=sqrt(3/2),4. The remaining boundary simplicity/exclusion is a short substitution into the previously published same polynomial, not an uncovered new census. The domain-level non-Lu-Qi-Keng consequence for the frozen polydisk-fiber domain is immediate from the identical axial zero locus.

## value

FAIL

This is a natural domain and the calculation is correct, but the proposed invariant is exactly a previously classified polynomial under constant axial renormalization and reciprocal parameter change. Excluding nonzero boundary roots or verifying simplicity in the same quartic is routine ancillary work, not a substantive surviving result. No independent off-axis classification is supplied to repair the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
