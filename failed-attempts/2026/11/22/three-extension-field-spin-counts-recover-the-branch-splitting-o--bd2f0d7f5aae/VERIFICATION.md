---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

In odd characteristic the hyperelliptic pencil H is fixed and even, K∼2H, and 2P_i∼H at each ramification point. The even-subset description of J[2] modulo complement, translated by H, gives the equivariant labels: 28 distinct pairs P_i+P_j (odd, since effective with one section and not the pencil), and H plus 35 complementary four-subset pairs (even). On the nth power of a branch permutation, a fixed pair is two fixed points or a 2-cycle. An invariant 4-subset is a union of whole cycles; a 4-subset sent to its complement is alternating on each cycle and exists exactly when all cycle lengths are even. These events are disjoint, and each fixed unordered complementary pair contributes two sets. This gives the stated exact fixed counts. Independent `python3 /workspace/reviews/reproduce_2_3_5.py` uses the powered cycle lengths d/gcd(d,n), subset-sum counts, and divisor inversion rather than following the frozen orbit traversal. It matches all 22 rows, both complete spectra and six counts in the frozen CSV. The joint prefix counts are 15,19,22, with exactly the three stated degree-two collisions; the separate parities have 19 and 21 distinct spectra, respectively (the text's 19 and 21 are numbers of spectrum values, not numbers of partitions individually identified). For (1,7) and (3,5), the first two pairs coincide at (0,1), while cubing the latter permutation fixes its three 3-cycle points and gives (3,1), unlike (1,7). Products of distinct irreducibles of degrees 1 and 7 or 3 and 5 give squarefree degree-eight covers over every odd field. No realization of all abstract partitions in each field is needed or claimed.

## originality

FAIL

This is not just a reduction to the symmetric group and a risk that an equivalent table might exist. The identified S8 really is the index-36 stabilizer of an even theta form in Sp6(2), and the published GAP Character Table Library explicitly stores the class fusion from this stabilizer to Sp6(2). ATLAS supplies class-aligned data for both complete parity actions. Together these give the 22 branch rows by a restriction along a stored class map, followed by counting fixed points of powers and comparing rows. The individual parity collisions are obtained from the same restricted cycle data, not from an additional arithmetic structure. Dolgachev supplies the classical parity identification, and the sharpness examples use ordinary existence of irreducibles with distinct prescribed degrees. No primary text was found printing the exact verbal theorem; the negative assessment is concrete implicit coverage. The accompanying same-day general record also overlaps exactly on the two sharpness examples, but its date is not evidence of priority and the general statement alone does not identify branch partitions without the fusion.

## value

FAIL

The branch and spin schemes are canonical and the cutoff is a correct interpretation. However, after identifying the known index-36 stabilizer the joint and separate exact data are mechanically implied by existing class fusion and the two prior permutation actions. The finite-field sharpness construction needs no additional nonroutine arithmetic. A new tabulation or a narrowing to the parity-alone counts does not yield a distinct valuable remainder here. No repair was made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
