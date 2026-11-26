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

Reduction modulo (t) rules out valuation zero. If 2j>=n then the product vanishes by degree, giving q^(n-1) high-valuation elements including zero and the stated counts by leading nonzero coefficient. At 2j<n the leading coefficient is c_j tau^j(c_j), nonzero in the field-coefficient case. In the split case write x=t^j(A+B s) with s^2=1 and sF(t)=F(-t)s. Moving the second t^j to the left multiplies the first s-part by (-1)^j, giving the two listed congruences modulo t^(n-2j). At even j their constant terms force both A_0 and B_0 to vanish. At odd j, A_0=±B_0≠0, and divisibility by the unit B reduces the second equation to A(t)=A(-t) modulo that power. Each of the two possible constants gives exactly one even root of B(t)B(-t) there, by recursion with invertible 2A_0. There are (q-1)q^(n-j-1) choices of B and q^j independent lifts of each root. The number of odd j at most (n-1)/2 is floor((n+1)/4), giving the claimed exact totals and unbounded ratio. Independently, for s^2=d with d nonzero and sigma(F)=F(-t), the commutator of A+B s and C+D s has scalar part d(B sigma(D)-D sigma(B)) and s-part (A-sigma(A))D-(C-sigma(C))B, all modulo t^n. Thus the coordinate map changing d=1 to a nonsquare preserves the entire commutation predicate and all corresponding centralizer sets and dimensions, not their algebra structures. For p=n the Cayley parameter t=(r-1)/(r+1) of k[C_p] is defined because r+1 has augmentation two; t^p=0, sts=-t and the inverse formula recovers r. The surjection between equal-dimensional algebras verifies the dihedral specialization. The finite Ore checker and recorded raw output were inspected, not rerun; extension fields and arbitrary lengths are established by the algebraic proof.

## originality

PASS

Pass for the complete valuation-resolved squaring-to-zero counts and their uniform separation in this particular commutation-equivalent pair. The same-pair commutation and centralizer dimension equivalence and split dihedral realization are credited background. The exact earlier peer record could not be read in full; its indexed statement and the frozen comparison, not source absence, support the distinction.

## value

PASS

What is useful here is not merely that some rings with identical commuting graphs can have different squaring statistics. This explicit same-field linear equivalence has an unbounded disparity at fixed q, with a complete structural explanation by filtration and parity, and a natural modular dihedral specialization. The exact layer law can be used to compare multiplication invariants that the prior pairwise commutation invariant overlooks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
