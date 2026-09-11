# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Triple-interchanger Yang-Baxter hexagon coherence in Gray-categories
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1003
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Higher Category Theory
- **Method:** polygraph rewriting with critical-pair coherence analysis and string-diagram normalization

## Problem

Decide coherence of the triple-interchanger Yang-Baxter hexagon in Gray-categories. In the free Gray-category on one object with generating 2-cells A,B,C, let P be the clockwise composite of three whiskered interchangers and Q the counterclockwise composite. Determine with a logged rewriting ledger whether P equals Q as 3-cells, or exhibit an explicit Gray-category witness where they differ.

## Attempted claim

In the free Gray-category on one object with distinct generating 2-cells A,B,C, the clockwise triple-interchanger hexagon composite P equals the counterclockwise composite Q as parallel 3-cells with common source and target pastings.

## Research outcome

Proved the triple-interchanger Yang-Baxter hexagon P=Q in the free Gray-category on A,B,C via a logged three-axiom confluence ledger, machine-checked VERIFY_OK.

## Why this attempt failed

Failed axes: originality, value.

originality: FAIL with ADMISSION_DEFECT. Admission preflight claimed no equivalent formulation and no broader coverage; fused live retrieval plus direct nLab primary sources falsify both. The submitted P=Q is the Joyal-Street Yang-Baxter equation transported verbatim: nLab Yang-Baxter page states plain YBE (R⊗id)(id⊗R)(R⊗id)=(id⊗R)(R⊗id)(id⊗R) as Joyal-Street 1985 diagram B7 p7, nLab braided-monoidal page states the two hexagon identities B_{X⊗Y,Z}, B_{X,Y⊗Z} plus naturality, and nLab Gray-category page states a doubly-degenerate Gray-category is essentially a braided monoidal category (Gurski-Cheng). Under that standard equivalence chi<->braiding and whiskering<->tensor, H1/H2 are hexagon axioms and N is naturality, and the 4-step ledger is the textbook YB derivation. Draft Sec.6 admits this transport. A prior source need not state P=Q verbatim for three distinct labels; the universally quantified braided YB theorem substantively implies and exhaustively covers the free 3-generator instance as a strict special case/renamed implementation. Timestamp or failed literal-title search does not establish priority. value: FAIL. The headline P=Q, though correct, is a textbook restatement/renamed implementation of the Joyal-Street Yang-Baxter consequence of hexagon+naturality, not an independently retrievable new coherence lemma. STANDARD rejects results already known or mechanically implied, textbook exercises, mere parameter substitutions, and renamed implementations even if machine-certified. Certification (VERIFY_OK) strengthens evidence but does not create value. Future researchers needing the triple-interchanger YB would cite Joyal-Street/Kassel or the general braided coherence theorem, not this three-generator ledger; no new boundary, obstruction, census, benchmark, or downstream use beyond the already-known general law is established. ADMISSION_DEFECT: Admission value preflight treated the ledger as a new Yang-Baxter law, but objective prior literature unavailable/misstated at Admission shows it is the standard derivation.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; supply independent motivation and a materially stronger contribution; address the recorded limitation: The ledger proves the named three-generator Yang-Baxter hexagon only; it does not decide other Gray-category pastings, higher Zamolodchikov 4-cell coherence, or rewriting confluence beyond this triple overlap, and it relies on the standard stated Gray compatibility and naturality axioms holding in the free construction.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
