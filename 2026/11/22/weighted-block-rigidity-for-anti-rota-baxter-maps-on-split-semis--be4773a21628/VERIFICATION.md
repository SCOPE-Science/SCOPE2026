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

Testing on coordinate idempotents gives r_is r_it+r_it r_ts+r_is r_st=0 at every row i and input pair s,t. Repeated input yields r_is(r_is+2r_ss)=0, in particular 3r_ss²=0. Thus outside characteristic three the diagonals, then the columns, vanish. In characteristic three each nonzero column s has entries 0 or d_s=r_ss≠0. For active s,t, the equations at rows s and t force the two cross entries to be either both nonzero or both zero. In the first case the polynomial forbids a row in exactly one support; in the second it forbids a shared row. This partitions the active coordinates into equal-support classes with disjoint supports, and any inactive coordinate can be in at most one support. Conversely equal supports give three identical summands, disjoint supports give zero terms, and any pair involving a zero column contributes zero. Each support has an active column, so its indicator contributes one to rank. Multiplication inside each support verifies the averaging identities. The strong identity on (e_s,e_s,e_i), i≠s, forces r_is²=0, and diagonals satisfy it. At rank n all coordinates must be active singleton blocks. For the counts, choosing the active set, an unordered partition, weights and assignments of inactive points gives the Stirling formula. One block contributes e^z(e^((q−1)z)−1) and unassigned labels contribute e^z; expanding rank coefficients gives the alternating formula. R acts on each image indicator by its block weight sum. Zero-sum nonzero c-tuples satisfy W_(c+1)=(q−1)^c−W_c and W_1=0, which gives the stated square-zero EGF. These are exponential generating functions over rational coefficients with integral labeled counts.

## originality

PASS

The anti and strong identities, the two-sided averaging terminology, characteristic-three nontriviality in a different algebra, and a substantial idempotent-averaging subfamily are credited. The distinct contribution supported here is the all-operator classification on split products, including blocks of arbitrary weight sum, its characteristic restriction for the anti identity, and the exact unrestricted and square-zero rank enumerations.

## value

PASS

The theorem answers a complete operator-classification question on the basic split reduced algebra, with a stark characteristic dependence. The weighted blocks capture both operators with projection-like behavior and nilpotent operators absent from the projection census. They give all attainable ranks, identify strong and invertible operators, and permit a separate rank census of the square-zero subfamily, a natural exact structural distinction beyond a low-dimensional example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
