---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The left spine is exactly the prefix priority-record minima, and an internal leaf is a local maximum of priority over its neighboring ranks (one neighbor at each endpoint). Relative orders are independent of the next insertion rank, so an interior leaf has covariance only with the three adjacent record indicators. Conditioning on the first of these records uses E[min(U_1,...,U_{j-1})^2]=2/[j(j+1)]; the middle record excludes the leaf, and at the last record the other two priorities are exchangeable. The three terms give the stated negative profile and the two endpoint formulas telescope with it to the stated aggregate, including n=2. For spine length 2, the split conditional on left size s has weight proportional to 1/s, s=1,...,n-1. Its leaf mean is the single-spine conditional mean in the left subtree plus the marginal leaf mean in the right; keeping the singleton contributions and the size-two left subtree gives the displayed harmonic-number term. Length one and length n follow from the empty left subtree and decreasing insertion order, respectively. The middle conditional mean exceeds both end values, which are equal at n=3. An independent exact-rational reproduction built actual BSTs for all 46,232 permutations of orders 2 through 8 and matched the covariances and conditional means. The frozen verifier was inspected, not executed.

## originality

FAIL

The main covariance finding is covered. The earlier catalogue record 3e3926193ad6 gives the entire aggregate formula under key reversal; the separate record 29e7eead2a91 displays the same full rankwise profile for minimum-key depth, which differs only by subtracting one from the frozen spine length. The latter has a later catalogue date; exact overlap is established, not historical priority. The conditional mean of total leaf count given spine length is a distinct question from the comparators’ conditioning on one key being a leaf. Its exact three-point result was not matched in the checked sources, but that does not clear the submitted covariance theorem as original. No narrower replacement is certified here.

## value

PASS

The observables are natural BST search and occupancy statistics, and the result explains why their positive aggregate covariance does not reflect rankwise positive dependence or monotone conditional mean. The exact regression gives that distinction at every size n>=3, rather than relying on an isolated small counterexample. This scientific motivation does not make the already covered covariance findings distinct contributions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
