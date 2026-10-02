# Review status

The fresh audit rejects this finding as a validated result. The original package is retained as failed-attempt evidence.

- Correctness: **PASS** — The divisor calculation is valid. Over K=Q(sqrt(-2)), D+=X_K cap V(x-a y) is the smooth plane quartic 8y^4-9z^4-36w^4=0 and meets X transversely; x-a y has order one there. The other numerator factor and the denominator are nonzero at an explicit geometric point, so v_D(theta)=1. The tame residue of (theta,-1) is [-1], and -1 is nonsquare in K and hence in the geometrically integral constant-field extension K(D+). Purity therefore excludes the class from Br(X_K), and restriction excludes it from Br(X). The inspected verify.py matches these steps; no finite experiment is used as an infinite proof.
- Originality: **PASS** — Best-of-knowledge searches found the exact record but no earlier source carrying out this ramification calculation for this exact surface and nominated symbol. Ieronymou develops symbol classes and purity for diagonal quartics, but its full text uses different explicit surfaces/classes and does not state this residue computation.
- Scientific value: **FAIL** — The final fact is a one-symbol rejection produced by a direct tame-residue check on an internally nominated representative. It does not establish a motivated boundary, classification, new invariant, or reusable structural lemma, and the record itself disclaims consequences for rational points, local solubility, or repaired classes. Under the shared value bar, a cheap negative membership check needs substantive mathematical motivation beyond correctness and novelty; that motivation is absent.

See `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json` for the complete assessment.
