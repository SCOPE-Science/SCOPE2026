# Scientific self-review

## Correctness — PASS

The precise domain is indexed cyclic binary Rule 30, one synchronous step, \(n\ge3\). The ordered double-preimage de Bruijn graph has twelve off-diagonal vertices and exactly eight cycle-recurrent vertices, verified from the truth table in the embedded script. Exchanging predecessor order gives a seven-edge, four-state signed quotient; the parity of its lift is essential for the period-\(n\) statement. All closed walks either lie on the zero-labeled \(C\)-loop or decompose into \(11\,0^m b\) return segments, with parity given by the number of segments ending in zero. A complete direct independent census through length sixteen (131,064 outputs) matches this proof. The test is not used to infer the result at larger lengths.

## Originality — PASS (qualified)

Historical literature gives Rule 30 predecessor-count growth and algorithms for listing individual ancestors (Wolfram 2002; Jeras–Dobnikar 2007), and homogeneous cases (Powley–Stepney 2010). A previously known aggregate frequency formula, including the Rule-106 reflection/complement equivalent, counts how many words have each predecessor multiplicity, but does not identify **which** indexed output words are ambiguous. The present theorem supplies the explicit signed-block language, including cyclic-cut and parity conditions, not a renamed predecessor-count formula. Closest inspected texts contain de Bruijn methods rather than this exact Rule-30-specific normal form. A potentially unindexed or implicit equivalent structural result remains the residual priority risk. This is not a declaration of uniqueness over all literature.

## Value — PASS

This resolves a natural inverse ambiguity question for each member of an infinite family of binary cyclic configurations: an intrinsic block condition decides whether the previous state is nonunique. The parity correction exposes a genuine obstruction between closed unordered pair walks and true periodic predecessor pairs. It is a structural classification, not a routine isolated small-case census. The result supplies an eight-state linear scanner and a reusable signed-lift technique; it makes no claim to improve general de Bruijn algorithms asymptotically.

## Scientific limits

The theorem does not classify multi-step ancestry, give a new multiplicity histogram, or settle a general inverse-entropy problem. One cited 1983 survey was available as bibliographic abstract rather than complete text. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
