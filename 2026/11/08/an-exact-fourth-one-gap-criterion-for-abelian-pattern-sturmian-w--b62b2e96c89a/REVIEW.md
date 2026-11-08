# Mathematical review

**Correctness — PASS.** The four-sum bipartite graph decomposes into a two-matching forest whose connected-component labels are residues modulo \(t\). The remaining three edges form a path, and adding that path preserves acyclicity exactly when its four vertices occupy distinct components. The labels \(0,1,M,M-1\) produce the precise congruence criterion, and strict-more-than-double support extension makes the finite test equivalent to infinite existence using Theorem E of [1]. All 7920 direct finite graph checks passed, but finite tests are not used as the proof.

**Originality — PASS (residual priority risk).** Theorem E of [1] is explicitly broader: it decides admissibility of any infinite support by an incidence forest condition, so the present result is not a new general characterization. However, Theorem E and the directly inspected Sections 7.1–7.3 do not state or calculate the complete arithmetic fourth-position spectrum. Deriving four residue-class components and their collision obstructions is the additional claimed result. The directly read earlier [2, Sections 1–4] introduces the subject but lacks this 2026 forest framework. Indexed scientific searches found no direct parameter-level equivalence. Independently discovered or unpublished equivalent specializations remain possible.

**Value — PASS (narrow scope).** The three consecutive divisibility obstructions are a sharp, natural boundary for a binary-word extension problem, determining exactly which fourth 1 positions are possible given first three at \(0,1,M\). The criterion separates ordinary Sidon constraints from longer-cycle obstructions and gives an explicit infinite witness for every permitted gap. Its value is the exact finite-prefix spectrum, not a new general theorem about all supports.

The main limitation is the dependence on [1] and the possibility of an unpublished or implicit earlier special case. The all-parameter statement has not received independent validation.

Self-review: passed. Independent audit: not yet performed.
