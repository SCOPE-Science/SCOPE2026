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

Verified support <=3 for signed Walsh sums of independent vertex sets of C_n (n>=3). The cyclic two-state transfer matrices A=[[1,1],[1,0]] and B=[[1,-1],[1,0]] yield W_n(S)=tr(product(B A^(gap-1))). Exact A²=A+I gives Fibonacci recurrence separately in each positive gap. For two marked vertices H(1,2)=0 at n=3, H(1,e)<0 for e>=3 and H(d,e)>0 for d,e>=2 by seed signs and positive recurrence; one marked always F_n>0. Recomputed all 64 three-gap sign boxes with 1,2,3,H and all H corners 4,5 using independently written exact integer matrix multiplication; only six zero boxes are permutations of (1,2,3). Inductive positive recurrence propagates strict signs to arbitrary high gaps and proves no other cubic zero. Direct independent-set enumeration for 3<=n<=10 corroborates; proves 12 hexagon supports and exactly 3 triangle two-support zeros.

## originality

PASS

Best-of-knowledge originality of the exactly degree<=3 zero-support classification. A broader full-group cycle-independent-set invertibility law supplies only existence of some zero for n divisible by three and global least magnitude, not degree<=3 locations and their exact 12-support multiplicity. Classical Lucas counts and Hasse-edge enumeration do not determine all third-order signed correlations. Relevant primary paper was read; no stronger implication found.

## value

PASS

Degree-three parity observability of the natural cyclic hard-core/Lucas-cube codebook is a motivated local spectral invariant, with a surprising isolated hexagonal obstruction absent from degree one and two at that length. The exact all-n low-degree classification is structurally useful even without any claim about higher degrees or a full spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
