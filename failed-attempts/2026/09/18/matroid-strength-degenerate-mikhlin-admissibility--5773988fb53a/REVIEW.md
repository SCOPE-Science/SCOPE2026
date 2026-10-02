# Review status

Fresh independent mathematical audit: **failed**.

- Correctness: **PASS** — The mathematics is correct. After deleting loop coordinates, Vandanjon's good \(k\)-directions are exactly the bases of the represented row matroid. Hence the admissible load vectors are exactly the base polytope intersected with the open half-box. Edmonds' base-polytope/box-intersection theorem gives the rank-defect inequalities, and the fractional base-packing/strength theorem gives the threshold \(\Phi(M)>2\). The strict positivity step is valid because every retained element is a nonloop and one may mix with a full-support base distribution.
- Originality: **FAIL** — The final statements are mechanically implied by classical matroid polytope and fractional base-packing theorems once the row matroid is named. The identification 'good directions = bases' is a direct restatement of coordinate-projection invertibility. Edmonds' box-intersection theorem, explicitly restated as Theorem 2.2 in Husić–Koh–Loho–Végh, supplies the capacity inequalities, and standard strength/base-packing theory supplies the maximum-load threshold. Under an implication-based originality bar, this is a routine corollary/application rather than a new theorem.
- Value: **FAIL** — The translation may be useful expositionally, but the scientific payload is a direct dictionary plus standard polyhedral theorems. It does not add a new structural lemma, boundary phenomenon, or nonmechanical classification beyond what those general results already imply, so it does not clear the value bar.

Detailed comparisons and limitations are in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
Earlier same-model evidence remains preserved in `AUDIT.json` as historical evidence.
