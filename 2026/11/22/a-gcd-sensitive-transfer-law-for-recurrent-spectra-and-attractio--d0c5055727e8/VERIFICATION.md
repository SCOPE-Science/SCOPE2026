---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproduction
Run `python3 check_two_bridges.py` and `python3 check_two_bridge_walks.py` in the directory containing those files. Python 3 standard library suffices. No network calls or stochastic choices occur.

The first script independently constructs the Boolean map, exhaustively computes its length-\(L\) iterate on all initial states for \(115\) parameter triples satisfying \(2\le a\le7\), \(1\le b\le7\), \(a+b\le11\), \(1\le s<a\), and checks every resulting phase-fiber cardinality against its polynomial coefficient. It also verifies every fixed-iterate population from the orbit decomposition. The total exhaustively examined states are \(76{,}280\). The three \(a=b=8\) cases with \(s=1,2,4\) were separately exhaustively replayed: the recurrent-state totals were \(2207,2209,2401\), each among \(65{,}536\) initial states.

The second script symbolically backtracks all Boolean monomial predecessor sets, rather than enumerating colorings, and verifies the claimed two-coset ancestor formula for \(8{,}450\) triples with \(2\le a\le26\), \(1\le b\le26\), \(1\le s<a\). It is a finite cross-check of the predecessor lemma; the general argument in `RESULT.md` provides the all-size proof.

The transfer matrix weights an inactive upstream residue class by \(2^{a/g}-1\), an active class by one, and a pair of active classes connected by the bridge offset by \(z\). The fixed-iterate enumeration is obtained by shortening both cycles to their gcds with the iterate. All arithmetic is exact integer arithmetic, without numerical tolerance.

## Limits
Neither program proves historical novelty or serves as independent external audit. The proof and quantifiers are contained in `RESULT.md`. The first program deliberately tests a wider family allowing downstream self-loop length one; that extra computation is outside the stated two-cycle theorem's \(b\ge2\) scope.
