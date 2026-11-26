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

The consequent of an implication propagates a forcing coordinate. Conversely, in the proposed guarded recursion, at p_i=0 the formulas implement the ordinary Boolean operations with p_i as false, and at p_i=1 all translated terms are true. If H_i denotes the halfcube a_i=0, the possible zero sets of the i-guarded terms are precisely all subsets of H_i. Disagreement is symmetric difference. For any D contained in H_i union H_j, choose the two disjoint zero sets D intersect H_i and D minus H_i, respectively; their symmetric difference is D. Taking complements gives exactly the claimed equality sets (when i=j and k>=2, any distinct j supplies a contained face). Every size from 2^(k-2) to 2^k occurs; the one-variable case and the implication/converse/dual transfers are correct. Read the frozen verifier and its recorded output without executing it. A separate exhaustive bit-mask truth-table closure reproduced 2, 6, 38 term functions and 2, 8, 112 equality sets at arities 1, 2, 3, with numerator ranges [1,2], [1,4], [2,8]. Those checks do not replace the universal proof.

## originality

FAIL

The exact material-implication spectrum and per-arity counts occur in a distinct published Resultary record. Its catalogue date is not a finding about priority. The stronger equality-set statement is not stated there, but it is a mechanical consequence of the 2012 published complete characterization of implication-term functions: symmetric differences of arbitrary subsets of two halfcubes run over exactly all subsets of their union. Cardó's stated gap is real in his paper, but does not establish scientific distinctness from these sources.

## value

FAIL

A clean explanation of the entry left open by Cardó is useful pedagogically. As an independent scientific finding, however, the numerical invariant is already covered and the only stronger part is the immediate power-set symmetric-difference identity applied to a known clone. The frozen claim does not deliver a nonroutine new invariant beyond that.

The dated certificate retains the supplied scientific assessment, sources and limitations.
