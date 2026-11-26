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

The greedy embedding of the proper prefix sends each predecessor zero block to the least count that forces the indexed next one: shortening a larger count would keep that source one and hence preserve failure. The last block is likewise forced by failure of the terminal letter and the ability to delete one zero. This injects the words into a subset of the k indexed ones plus the terminal bit, giving Pascal's bound including r=0 and k+1. For (010)^k, the initial cost to select source one i is 2(i-1), and a gap d between selected ones costs g(d)=0 for d=1 and 2d-1 otherwise. A zero deletion in a nonfinal positive block permits shifting all following selected ones back one position: the shortened block fits, interior capacities are unchanged, and the tail gains two zeros (or leaves the final source one available). Deleting a selected one between p and q costs at most 2(q-p-1) merged zeros, which fits before q-1. At the beginning the capacity is 2q-3; at the tail after p it is 2(k-p)+1 for a terminal zero and 2(k-p) before the last source one for a terminal one; the witness counts fit these capacities. With no preceding one the corresponding tail capacities are 2k and 2k-1. Final-block zero deletions and deletion of the terminal letter fit by the threshold definition. Thus every code is realized and different codes give distinct words. The frozen verification is finite corroboration, not the basis of this all-k argument; no frozen code was executed.

## originality

FAIL

The earlier Resultary record explicitly gives the same total bound and the same witness under the identical definition and letter-count constraint. Although its Finding does not display the binomial layers, its binary append proof gives them by the direct operation of retaining the weight of each word in that very induction; see the coefficientwise derivation below. The submitted direct greedy encoding is a different proof, but the claimed extremal theorem is already covered and the record does not establish a distinct result about the encoding beyond this proof.

## value

PASS

The sharp all-k distribution by a source-frequency parameter is a useful structural statement about the minimal-absence set, with a single extremizer family for all layers. The greedy proof gives an explicit injection, not a numeric table. This mathematical value does not make the already-covered theorem a new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
