---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Chen–Hu–Ma span incidence resolution Y=P_Gr(k+1,N)(Sym² S^∨) has positive-dimensional fibers solely over doubled k-plane cycles Z=Gr(k,N), with fiber P^{n-k}. Dimensions dimY=(k+1)(n-k)+binom(k+2,2)-1, dimZ=k(n+1-k) give codimZ=n+binom(k,2). Semismall iff 2(n-k)≤codim, equality iff n=2k+binom(k,2). Small resolution theorem then identifies IH(Q)=H(Y); at equality semismall decomposition gives one constant rank-one local system on Z shifted 2r, requiring subtraction q^r P_Gr(k,N). Projective-bundle and Schubert formulas yield claimed Gaussian products and even pure Tate groups. Independent Gaussian q calculation at p=1,n=5 produced (1,2,4,6,9,11,13,13,13,11,9,6,4,2,1), sum105. The cited source fiber classification is a necessary substantive premise and is explicitly credited.

## originality

PASS

Best-of-knowledge: inspected actual primary statements for possible coverage by equivalence and implication, not just matching titles. The input Prop.3.1 of Chen–Hu–Ma plus standard small/semismall theorems logically imply the formulas after elementary codimension and fiber-top-homology work. Their stated results do not themselves give the wall or IH(Q). This is a short but motivated new application of general theorems, with novelty confined to this singular locus.

## value

PASS

Pinpoints the geometric smallness/semismallness wall and computes middle-perversity Betti polynomials of the natural singular irreducible quadric-cycle locus, including a nontrivial boundary correction. Distinguishes intersection cohomology of Q from ordinary cohomology of the reducible Chow variety.

The dated certificate retains the supplied scientific assessment, sources and limitations.
