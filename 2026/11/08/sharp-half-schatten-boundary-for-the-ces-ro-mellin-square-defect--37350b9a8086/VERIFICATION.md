---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Corrected final claim establishes every-rank two-sided s_n(E) asymp n^-2 with new explicit lower c=1/(8e). The exact harmonic-log matrix factorization yields dyadic blocks with s_j(B_r)<=C2^-r/j and off-diagonal rank-one corrections in all Schatten quasi-ideals, implying s_n(E)=O(n^-2). For each J_n={n,...,2n-1}, the exact difference identity Delta D E^(n)=D^-1(I-K) has K_{ab}=a log(a/(a-1))-1 on a>b, bounded by 1/n. Length-j chains yield ||K^j||<=1/j!, so the n-by-n inverse norm <=8e n² and the compression inequality gives s_n(E)>=1/(8en²). The finite code was inspected; it checks small identities and is not used as an infinite proof.

## originality

PASS

The original broad novelty claim for the half-Schatten threshold is false: both Oct25 and Nov1 prior published findings prove membership iff p>1/2 for the identical E=C²-W2, and Nov1 already proves weak endpoint and pointwise upper O(n^-2). Their complete RESULT.md files were read. Neither gives uniform pointwise LOWER s_n>=cn^-2: nonmembership via divergent eigenvalue p-moments does not entail that all-rank inequality. Revised full RESULT/SLOGAN/REVIEW explicitly credit covered components and isolate the novel lower pointwise rate. Residual risk older Hardy matrix approximation-number theorem.

## value

PASS

Uniform pointwise lower bound resolves an exact natural singular-number scale for this canonical lattice multiplicativity error at every rank, stronger than known aggregate membership failure. Meaningful completed invariant independently of any general Mellin product theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
