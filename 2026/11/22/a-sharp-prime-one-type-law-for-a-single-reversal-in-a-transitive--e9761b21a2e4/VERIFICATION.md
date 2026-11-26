---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The random tournament extension property realizes each new-vertex bit word, and homogeneity over the named base identifies realizations of the same word; different words differ on an atomic formula. For an adjacent reversal the reordered base is a chain. Its consecutive pairs enforce alternation, and its source/sink force first bit 0 and last 1; a module including the new point and some old vertices must contain both endpoints, so its old interval is the whole chain. In the nonadjacent case, the block B with cyclic classes {p}, M, {q} is strongly connected and the old tournament is the ordered sum L,B,R. If an old module meets B and an outside vertex but omits part of B, that outside member forces B intersected with the module to dominate or lose uniformly to the rest of B. Either cut contradicts strong connectivity. A module using more than one cyclic class within B must include all three classes, hence all their vertices (any omitted middle vertex sees p and q differently). This proves the interval/whole-block old-module list, including the crossing cases. To split every old module missing the new point it suffices to alternate within each run and make B nonconstant, the latter automatic except for singleton M. For a nontrivial module containing the new point the old part K is an old module and must include the old global source/sink wherever the respective outer run exists, because those vertices see the new point opposite to every old vertex. If an outer run exists, the possibilities for K are therefore a subset of an outer run, impossible because B is split, or a quotient interval containing B and the necessary endpoints, which is the whole base. If both outer runs are absent, |M|>=2 and K={p} or {q} would require constant bits on M. K contained in M would require b_p=1 and b_q=0; this combination is excluded and otherwise makes M plus the new point a module. Thus the bit conditions are sufficient as well as necessary. The 2 middle phases and 4 endpoint choices give 8, with exactly 2 removed in each of the disjoint exceptional regimes, and the span multiplicities give the stated sum. Inspected VERIFICATION.md, CHECKS.txt, verify.cpp and verify.py without running the uploads. The reported 458,720 vector checks and 80 endpoint-pair checks are finite diagnostics; contrary to the verification prose, the Python file tests individual pair counts rather than explicitly asserting the total polynomial. The total follows from the proof.

## originality

PASS

The distinct claim is the full marked, named-base cardinality law for every one-arc reversal, principally the 6 versus 8 distinction, not existence of a one-point extension or the parity obstruction for chains. The classical existence result and its constructive proof materially overlap the positivity and nonexistence information, but the inspected construction is not a characterization enumerating every admissible new-point orientation. Other indexed tournament censuses count different invariants. This assessment is bounded by the sources inspected.

## value

PASS

This is a natural minimal perturbation of the transitive tournament and asks quantitatively how changing one old orientation affects the pool of prime extensions. The answer is uniformly bounded, yet differs between cyclic singleton-middle, spanning and other one-reversal bases, and it classifies the admissible labelled words, not just their existence. That structural distinction matters for enumerating modular-decomposition-breaking extension types and is more than a finite-table or transitive parity recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
