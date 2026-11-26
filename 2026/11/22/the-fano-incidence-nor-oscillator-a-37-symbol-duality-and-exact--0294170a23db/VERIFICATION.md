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

For the specified labelled Heawood graph the non-incidence maps α and β are antitone Galois adjoints: Y⊆α(X) iff X⊆β(Y). The triple-composition identities give F³=F, not merely an eventual period-two bound. F² applies the idempotent closure separately to each shore; its image is the complete recurrent state set. Point sets of sizes 0, 1, and 2 close to themselves: for any outside point some line through it avoids the set. For three points, inclusion–exclusion on their three incident-line stars gives six hit lines when noncollinear, seven when collinear. Thus a noncollinear triple closes to the complement of its unique avoiding line; every such complement has its four three-subsets and itself in its fiber. All other sets of size at least three close to the full set. This gives 37 closed symbols with the stated five fiber types and an all-points fiber of size 128−(1+7+21+35)=64. Anti-incidence interchanges empty/full, singleton/line-complement and pair/pair types. On the closed product, the update swaps the two dual labels; the 37 diagonal states are fixed and the 666 unordered unequal pairs are primitive two-cycle orbits. Basin sizes are one product of the two closure-fiber sizes for a diagonal, or the sum of the two ordered products for an unordered pair. This gives the stated 11 rows, fixed mass 219, period-two mass 16165, and the four entry counts; the empty/full symbol pair alone gives 4097. Independently reproduced the full census from Fano lines given by binary projective triples and by traversing each trajectory until its first repeated state, without assuming any bound on entry or period. It reproduced every row, the four entry counts and the empty/full orbit size. Replay: python3 -B /workspace/reproductions/check.py 3; output /workspace/reproductions/3.log. The frozen C++ and Python files and census were inspected as evidence, not run.

## originality

PASS

The surviving claim is the Fano-specific closure-fiber classification and exact full Heawood NOR individual-attractor census. The general period/entry reduction and the maximal-independent-set correspondence are not distinct contributions. The closest same-day indexed record uses the same duality and kind of census but on three different nine-point incidence structures, and does not determine the Fano fibers or census. Inspected evidence supports a bounded PASS for the precise finite invariant, not a priority claim for the general method.

## value

PASS

The Heawood graph is the canonical smallest nontrivial projective-plane incidence graph, so the host is motivated independently of the census. A complete, reproducible 703-orbit benchmark distinguishes attraction from mere orbit counts; in particular it separates 21 isolated equilibria from the empty/full orbit with 4097 initial states. The fiber geometry explains those values and gives a useful comparison point for other incidence networks or rules, without claiming any downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
