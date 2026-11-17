---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: For w=0^a1 0^b1 0^c with a,c>=0 and b>=1, classify MAFs by number of 1s. Unary 0^{L+1} contributes one; one-1 MAFs arise at missing corners of the union of two down-closed rectangles; 1 0^k 1 contributes K gaps excluding k=b, with two conditional wing extensions; the sole possible three-1 MAF is 1 0^b1 0^b1 if a,c>=b. This exhausts possible counts and yields the eight-term indicator formula in RESULT.md, with main term max(b,min(a,c)) and O(1) error. A uniform (a,b,c) composition with b>=1 converges to Dirichlet(1,1,1), so Z=max(Y,min(X,T)) and the CDF is 4t² (t<=1/3), 6t−5t²−1 (1/3..1/2), 2t−t² (1/2..1); integration yields mean 7/18, variance25/648. Independent literal factor-set enumeration tested every admissible triple at lengths n=3,…,14 against exact formula with no mismatch. All-length proof comes from classification, not tests.

## originality

PASS

PASS, best of knowledge: RLE minimal-absent-factor classification and algorithms are known, and a published five-run Dirichlet MAF-count limit law has a related bridge structure. That five-dimensional positive-run ensemble does not specialize probabilistically to two singleton one-runs (a measure-zero event) and gives a different limit; it also states no exact formula for every (a,b,c) here. The new exact gap count and conditional three-dimensional piecewise-quadratic law are not implied by inspected publications.

## value

PASS

PASS: The uniformly sampled fixed-two-marker sparse ensemble is a canonical conditional word family, and an exact counting formula plus nondegenerate normalized MAF law are natural exact combinatorial/statistical invariants. The nontrivial boundary cases with vanishing exterior gaps and the Dirichlet transition make this more than recomputation of a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
