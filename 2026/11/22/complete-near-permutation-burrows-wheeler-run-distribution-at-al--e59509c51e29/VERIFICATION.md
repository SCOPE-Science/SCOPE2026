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

A singleton letter forces primitivity, and the two rows with predecessor a are exactly the rows starting at its two successors. These positions are distinct, and their symbols cannot coincide: if both were a, the two a-positions would form the entire two-cycle, contrary to n≥3. The only possible adjacent equal pair in the linear last column is aa. When neither successor is a, their row blocks are singletons, consecutive exactly at neighboring occupied ranks. If the successors are a and c, the two a-rows have prefixes aa and ac; precisely the ac row has predecessor a, and it faces the c block because comparing the second symbols puts it on that side of the a block. These rows are consecutive exactly when a and c are neighboring ranks. For any unordered successor pair, delete both a's; on the remaining circle of r−1 distinct letters, uniquely insert either single copies before the designated distinct non-a letters, or the block aa before c. Hence each pair gives (r−2)! circles for each repeated a, also when r=2. Counting r−1 adjacent pairs among all binomial(r,2) pairs gives r! clustered and (r−2)r!/2 unclustered, with (0,2) at n=3. The ambient-alphabet multiplier uses adjacency in the occupied induced order, not across unused letters or around the ends of the rank order. The two supplied checkers test distinct constructions (source rotations and stable LF cycles) for lengths 3–9; their recorded outputs agree. They were inspected, not run, and are not the basis of the all-n proof.

## originality

PASS

The distinct supported contribution is the exact all-length successor-pair criterion and run census for the single-repeat profile. Prior work covers existence of an unclustered necklace in this very profile for n≥4 and gives the unrestricted fixed-Parikh total and standard LF characterization. Those results are credited and are not claimed as new. They do not count the adjacency-constrained fibers, and the closest distinct exact census uses a different content profile except for a small overlap.

## value

PASS

The minimal fixed-content departure from an ordinary alphabet permutation is a natural test for whether BWT sorting clusters a repeated letter. The successor-rank criterion identifies exactly what does so, and the uniform successor fibers turn an existence phenomenon into a complete finite count and probability over arbitrary growing support. This is a useful baseline for stronger fixed-Parikh refinements, not a claim about typical clustering over fixed alphabets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
