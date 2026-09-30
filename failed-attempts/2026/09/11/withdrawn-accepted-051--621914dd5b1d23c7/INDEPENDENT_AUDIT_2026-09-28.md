# Independent Audit — 2026/09/11/051

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `202e586bcf3e4e00820a84be19a0c8fbb4d7c6e5`
- Disposition: **FAILED**

## Correctness

**PASS** — The arithmetic obstruction is valid for the three explicitly defined interpolation counts. For the bundle and unfolded bivariate models, substituting the largest degree allowed by D<t(m-l) reduces feasibility to quadratic inequalities that are ruled out by s(m+1-s)≤(m+1)^2/4. For the generous 5-variable count, direct enumeration of small m and the stated tail estimate 2.5 u(1.08-u)^4<1 cover all m≥2. Because that count deliberately overestimates the true weighted coefficient count, failure of the generous model does transfer in the impossibility direction. The separate Johnson L≤5 observation is also correct and is explicitly labeled non-original.

## Originality

**FAIL** — The headline is a fixed-parameter feasibility check obtained by inserting N=16, s=4, k=16 and agreement 8 (or 31/32 unfolded) into standard interpolation dimension inequalities. The all-m extension is an elementary AM-GM/calculus closure of those same inequalities, not a new decoding theorem, algorithm, code construction, or structural bound for a broader parameter family. Existing folded-Reed–Solomon work supplies the interpolation/multiplicity framework; the record evaluates one small window of it. No exact prior table was found, but a fresh arithmetic evaluation of a standard feasibility condition is not sufficient originality by itself.

## Scientific value

**FAIL** — As an internal route diagnostic the calculation is useful: it says this particular interpolation certificate cannot prove the desired N=16 claim. As a standalone research result, however, it neither strengthens list decoding, changes the achievable radius/list tradeoff, nor proves an obstruction to other interpolation formulations or decoders. Its scope is one chosen finite parameter window and three hand-selected coefficient counts, so the scientific advance is too limited for validation as an independent finding.

## Limitations

- The negative statement is only about the specific existence-plus-multiplicity-lemma formulations defined in the record.
- The generous multivariate count is used only for an impossibility transfer; it is not asserted to equal the true Guruswami–Rudra weighted count.
- No claim is made that the code itself is not list-decodable at radius 0.52; the record's own Johnson calculation gives a textbook list-size bound.

## Sources

- Explicit Capacity-Achieving List-Decodable Codes — Venkatesan Guruswami; Atri Rudra: https://www.cs.cmu.edu/~venkatg/pubs/papers/folded-RS.pdf — Canonical folded Reed–Solomon interpolation framework from which the finite-window count is specialized.
- Improved List Decoding of Folded Reed-Solomon and Multiplicity Codes — Swastik Kopparty; Noga Ron-Zewi; Shubhangi Saraf; Mary Wootters: https://arxiv.org/abs/1805.01498 — Broader modern FRS list-decoding context and parameter tradeoffs.
- Improved List Size for Folded Reed-Solomon Codes — Shashank Srivastava: https://arxiv.org/abs/2410.09031 — Recent list-size work; does not turn the fixed arithmetic infeasibility check into a new decoding result.

GitHub was read only as evidence. The record's pre-existing `AUDIT.json` was inspected only after an independent assessment and was not treated as authority. No repository mutation was performed by this audit chat.
