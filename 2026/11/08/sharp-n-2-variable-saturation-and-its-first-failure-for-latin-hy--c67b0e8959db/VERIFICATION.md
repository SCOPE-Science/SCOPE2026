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

# Reproducibility

Run `python3 hypercube_check.py` from the directory containing the embedded files. The program uses only the Python standard library; its stdout is recorded in `hypercube_check_output.txt`.

For arity two, each input is a sorted universe of three disjoint copies of a set of size \(q\). The program enumerates all ordered triples of occupied stationary positions and all possible replacements for a fourth pebble. For arity three, the analogous enumeration uses four stationary pebbles and a fifth moving pebble. Every resulting atomic type includes sort labels, equality among all occupied variables, and all admissible ordered relations.

The complete tested extension catalogues agree for the named binary examples of orders four, five and six, including the cyclic and Klein order-four tables. They also agree between the cyclic and Klein ternary additive cubes of order four. These finite tests verify sample instances of the local-completion lemma and catch missing atomic configurations. The general \(n\)-ary completion case analysis, including arbitrary orders and unbounded game length, is supplied in `RESULT.md` and is not inferred from these tests.

The explicit intercalate counts provide finite witnesses for the sharpness discussion in arity two. The proof for arbitrary arity uses the algebraic involution argument and does not rely on these counts.

The results are a mathematical proof together with limited computational cross-checks. No independent audit or external formal certification has been performed.
