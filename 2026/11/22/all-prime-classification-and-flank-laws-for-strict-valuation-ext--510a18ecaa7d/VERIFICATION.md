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

Writing F_n=(3n)!/(n!(2n+1)!) gives the claimed quotient and hence the signed valuation jump J_p(n). A peak needs J_p(n-1)>0>J_p(n), and a valley the opposite. For p>=5 a peak requires one of 3n-2,3n-1 to vanish modulo p together with one of n+1,2n+3. Their four eliminants have absolute values 5,13,4,11. Direct substitution at (p,n mod p)=(5,4),(11,4),(13,5) shows every other factor in the respective jumps is a unit, giving exactly the reported drops. For a valley, n or 2n+1 would have to vanish alongside one of 3n+1,3n+2; at n=0 the latter have values 1,2, and the two eliminants involving 2n+1 are +/-1. At p=3 the jump is 1-v_3(n+1)-v_3(2n+3): it is positive in class 1 modulo 3 and negative precisely in classes 3,8 modulo 9. At p=2 the successive classes modulo 4 have sign zero, nonnegative, positive, negative, with exact jumps as given; thus only 3 modulo 4 is a peak, and the following zero jump rules out valleys. The case n=1 uses F_0=1 and requires no exception. For p=5,11,13, after writing n=c+pt and dividing each active factor by p, the root pairs for t modulo p are (1,4),(7,5),(4,6), respectively. Since they are distinct, at most one flank exceeds one, and one unit-slope root class at each higher power gives (p-1)/p^j for a flank of size j. For p=3 the varying factors after removing the fixed powers are t+1 or 1+2t on the respective progressions, and at p=2 the factors are 2+3t and t+1 with opposite parities. These exact residue counts verify every joint mass and its normalization. The frozen checker was inspected, not executed; the all-prime exclusions and density limits follow analytically.

## originality

PASS

The factorial quotient and prior pointwise digit or carry formulas are not new. The supported distinct claim is the evaluated all-prime adjacency classification, including the three odd primes beyond 3, the absence of other peaks and valleys, and exact conditional paired-flank densities. Prior block spectra and pointwise expressions provide real overlap but not that classification; related adjacent laws use different counting sequences.

## value

PASS

The exact exceptional-prime set is a structural result for the natural ternary-tree count, and strict valleys are notably scarcer than strict peaks. The joint laws add information absent even from separate flank marginals: at 5,11,13 one flank must equal one, whereas the other has unbounded support. The classification and dependence are useful local structure, not just a different presentation of a factorial quotient or a list of examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
