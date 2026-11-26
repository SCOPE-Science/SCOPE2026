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

Independently reconstructed the algebra for the stated F_2 ring, including n=3, and inspected VERIFICATION.md and both supporting scripts without executing them. The presentation s e_j=T e_j on site generators is valid because T is symmetric. Eliminate generators with the unit recurrence coefficient, then close the two consecutive generators around the ring; the resulting relation matrix is M-I up to transpose/convention, which preserves its Smith factors. Hence its two monic determinantal divisors describe the entire module and det(M-I) is the characteristic polynomial. In characteristic two det(M-I)=tr(M) since each step has determinant one. With H=H_0 and E=e_11, the two linear-in-E trace terms agree by cyclicity and cancel, the unmarked trace of H^n is s f_n, and the two-E trace is (H^(d-1))_11(H^(n-d-1))_11=f_d f_(n-d). At zero the unmarked matrix S has order two and the marked matrix B has order three. With both unmarked arc lengths even the product is B^2 (no fixed vector except zero); with both odd it is (SB)^2=I; with mixed parity the product is conjugate to S B^2, a nonidentity involution of rank-one difference from I. These cover even n/odd d, even n/even d, and odd n, respectively. In each cyclic summand the nullity of T^k(T^m-I) is the degree of the modulus gcd, and the coprime s-primary and nonzero-primary pieces give exactly min(k,e_i) and deg gcd(h_i,s^m-1). This counts depth at most k and period dividing m; subtract the k-1 counts (zero for k=0), then invert on divisors, recovering the stated joint census including periodic cycles. Squaring H^a gives f_(2a)=s f_a^2. The d=1 and d=2 simplifications are f_(n+1) and s^2 f_(n-1); the specified lengths thus have characteristic polynomial s^n, and their odd-length nullity one gives one Jordan block, proving the sharp cutoff, not just nilpotence. Verification notes report finite rank and enumeration runs; the universal proof does not depend on their scope.

## originality

PASS

Cattell's general cyclic class includes the exact operator family, and MOW already treats polynomial orbit counting on uniform cyclic Rule 90. Do not credit general transfer/determinantal techniques, Smith or divisor inversion, or the broad idea of dyadic nilpotence. The distinct supported content is the marked-site separation rule with exact geometric nullities, the two-invariant joint census instantiated for that nonuniform family, and the pair of explicit sharp nilpotent resonances. Earlier inspected results overlap in methods, model classes and one length sequence, but do not furnish the separation/two-arc specialization and Jordan classification. The two families are sufficient, not asserted to exhaust nilpotence.

## value

PASS

Two marked sites are the first defect configuration with a separation variable. Exact invertibility and kernel changes with that variable, the all-population joint time/period census via two polynomial factors, and two distinct infinite sharp extinction clocks describe concrete effects inaccessible from visually enumerating configurations. The two families produce an exact maximal nilpotence witness even though the ambient cycle normally has periodic states; the value is in this finite-system control by placement, not in claims about arbitrary defects or new general linear algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
