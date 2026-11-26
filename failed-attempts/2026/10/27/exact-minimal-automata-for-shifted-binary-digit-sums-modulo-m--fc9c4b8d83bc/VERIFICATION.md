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

Writing c+p=2^h d+u after an h-digit prefix, a suffix of value v gives disjoint low and high parts u and d+v, so the residual is s2(u)+s2(d+v) mod m, including v=0 and all padded suffixes. For d<e the suffix value 2^L-e gives raw digit-sum difference L-s2(e-d-1)-1, taking successive residues as L varies; no fixed offset identifies the two. Equal carries with distinct residues already disagree at the empty suffix. Beyond ell, a positive carry must be 1 and its low remainder u<c, already realizable at depth ell by p=2^ell+u-c. Each zero-carry residue is attained using c+p=2^t-1 for arbitrarily large t in that residue class. For c=2^r, depths 0..r have distinct carries and phases given by the consecutive weights 0 through h; a late carry 1 only adds residues of remainders less than 2^r, already seen at depth r. This yields both dyadic branches and the c=0 boundary. Inspected the frozen RESULT.md, VERIFICATION.md, checker.py and checker_output.txt; the reported 1,032 parameter cases and 132,096 fixed-length direct tests were not rerun. The reproducibility note should require Python 3.10+ for int.bit_count(), not 3.9+; this does not affect the symbolic result.

## originality

FAIL

The earlier parity record already solves all shifts for m=2, with the same exact residual and depth formulas and the same two-power nonperiodicity witness. Its residual-count proof transports mechanically to Z/mZ, giving the claimed set and dyadic count by direct range counting. A distinct later catalogue statement also explicitly matches every modulus and shift; that later match confirms equivalence, not prior authorship or order of discovery.

## value

FAIL

Exact state complexity in an all-word LSF model is a meaningful natural invariant. Here the exact finite set for higher moduli is the known carry/phase computation using modular addition in place of parity; the same witness proves minimality. The dyadic branches then count consecutive residues, rather than adding a separate structural result. The frozen statement does not clear the value standard for a mechanically transported invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
