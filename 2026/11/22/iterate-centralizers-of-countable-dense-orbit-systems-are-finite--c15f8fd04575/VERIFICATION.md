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

The hypotheses give the claimed phase model. Explicitly, a dense forward orbit on infinite X has no repeated points and contains every isolated point. The images of distinct isolated points converging to p∈X′ are distinct orbit points converging to f(p), so f(X′)⊂X′. Thus the forward orbit cannot enter finite X′. Its omega-limit set is exactly X′, and compactness gives f(X′)=X′. Small disjoint neighborhoods of the finitely many limit points force all sufficiently late visits to follow the permutation f|X′, and every limit point must be visited arbitrarily late. Thus there is one cycle and the index classes modulo k converge to its phases. For each ray r modulo m, commutation fixes the image sequence from a_r. The phases seen along that ray are exactly j≡r mod gcd(k,m), and taking limits forces g(p_j)=p_{j+s_r−r}. Equality of these prescriptions gives the compatibility condition; conversely it suffices for continuity, since there are finitely many rays, and commutation on the cycle follows since m is divisible by d. A surjection must cover all m initial isolated ray points from the m initial source points, hence is a permutation of them and then a bijection on the cycle as well. For a permutation sent from class a to class β(a), write its internal action as σ_a(t) on 0≤t<q. Compatibility says σ_a(t)−t is constant modulo ℓ; summing gives q times this constant congruent to zero, so gcd(q,ℓ)=1 forces residue preservation. The within-residue symmetric groups and arbitrary class permutation give exactly the stated wreath product and both specializations m=1 and m=k. The frozen verification/check_centralizers.py was inspected, not executed; its finite scope gives no substitute for this proof.

## originality

PASS

The orbit presentation and finite-cycle synchronization are established prior results. The supported distinct claim is the full continuous commutant for each sampled map, including nonsurjective maps and the exact group of units. The inspected Ellis-semigroup results concern closures of iterate sets, which do not classify these commutants.

## value

PASS

A natural complete commutant classification identifies exactly the extra symmetries created by time sampling and includes noninvertible maps missed by an automorphism count. The contrast between Aut(X,f)=1 and Aut(X,f^k)≅S_k gives an exact, arbitrarily large change from a simple class of canonical dense-orbit systems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
