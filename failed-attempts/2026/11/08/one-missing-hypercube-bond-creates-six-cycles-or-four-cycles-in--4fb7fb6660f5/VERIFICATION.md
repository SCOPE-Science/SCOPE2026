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

The stated theorem, as distinct from every inference in the frozen proof, is correct. Let A be intact adjacency, E the deleted-edge toggle and m=N/2. Coordinate flips give A²=(d mod 2)I. If d is even, splitting by a coordinate yields the layer matrix with off-diagonal identity and diagonal A_(d−1), where A_(d−1)²=I. Thus rank A=m. In the bipartite parity block, the deleted endpoints lie outside the totally isotropic images of H and Hᵀ, so the rank-one update raises rank H by one: rank B=m+2. With full endpoint vectors e,f, the four independent vectors e,f,p=Be,q=Bf span W. There Bp=e+q, Bq=f+p; e is cyclic, B³e=f and B⁴e=q=B²e+e. The polynomial is therefore (t²+t+1)², and im B²=W since it lies in W and W is invertible. Rank on the zero summand is m−2, giving only size-two nilpotent blocks. Fixed-space dimensions on W are 0,2,4 at powers 1,3,6 by polynomial gcd; this works whether or not the quadratic splits. At d=2 the zero summand vanishes. If d is odd, H'H'ᵀ=I+L with L=uuᵀ+auᵀ+uaᵀ, a nonzero isotropic and orthogonal to u. L has rank two and L²=(u+a)(u+a)ᵀ is a rank-one projection. Both parity blocks of B² thus have one simple zero, one size-two block at 1, and m−3 simple blocks at 1. B has two simple zero blocks, because a square cannot turn a nonsimple zero block into a single simple zero without increasing its multiplicity, and rank B=N−2. The frozen line 48 list of partitions is not exhaustive from the square and dimension alone (pairs of J₁(1) can replace J₂(1)); close the gap as follows. D=A+I satisfies D²=0, and the coordinate-layer calculation with diagonal A_(d−1)+I gives rank D=m. Therefore im D=ker D=(ker D)⊥. U=span{e,f} intersects ker D trivially: De and Df have nonzero off-endpoint parts on opposite parity sides. Since im E=U, ker(B+I)=ker D∩ker E, of dimension m−2 by independence of the two endpoint constraints on ker D. The frozen witness (B+I)³x=u+c with B(u+c)=c+a≠0 forces a size-four block, since every block at 1 has size at most four by the square. This consumes both size-two blocks of the square; the remaining m−3 blocks at 1 have size at most two and dimension 2(m−3), hence all size two. The odd fixed-space dimensions on the invertible part at powers 1,2,4 are m−2,N−4,N−2. Kernel increments give the stated transient counts; invariant direct sum gives the exact product census, which counts configurations, not cycles. Fresh GF(2) rank tests d=2,…,7 and full state enumerations d=2,3,4 agree, including odd ranks [m+2,4,3,2] for powers 1–4 of B+I. Replay: python3 /workspace/branches/84337f69-e5f1-4738-97d9-f914708b7913/independent_check.py; output is adjacent in independent_check_output.txt. The frozen checkers were inspected, not executed; tests are bounded, not the all-field proof.

## originality

FAIL

The distinct earlier record 0ddebf65b6fe already describes exact Jordan structure and transient and primitive-period counts for the same one-edge deletion, same cube adjacency update and characteristic-two fields, including the same parity-specific recurrent periods. The opening passage corroborates the setup. This is positive evidence of material coverage, not a rejection based on a timeout or a title. Direct-sum multiplication of the two counts is a consequence of the Jordan classification; no distinct surviving contribution was established. The detailed formula-by-formula cross-check of the earlier proof was not possible from the passages retrieved.

## value

FAIL

The defect classification itself is a meaningful structural invariant, but the submitted contribution recomputes the already covered invariant without a distinct application, extension, or comparison yielding a new scientific conclusion. The joint-product form and the checkers do not add a separately valuable result beyond the existing Jordan and orbit census. No repair is warranted solely to patch the submitted proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
