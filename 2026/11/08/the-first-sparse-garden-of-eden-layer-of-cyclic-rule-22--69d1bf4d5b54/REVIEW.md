# Scientific review

## Correctness — PASS
The Boolean four-state predecessor matrices follow from all eight neighborhoods of Rule 22. A cyclic predecessor is equivalent to a closed labeled path, so a nonzero Boolean trace is necessary and sufficient. The exact stabilization of the zero-labeled matrix at its fourth power reduces unbounded gaps to 125 capped triples. An explicit exhaustive table, oriented gap classification, and orbit-size calculation establish the conclusion for every ring length in scope. The standalone verifier independently enumerated 262136 binary inputs and checked the symbolic table and further lengths; extrapolation is not used as an infinite proof.

## Originality — PASS (historically qualified)
Gravner–Griffeath (2010), particularly the non-surjectivity discussion, and Martínez et al. (2019), particularly the Garden-of-Eden subset diagram, are the closest primary works. The 2019 work lists short forbidden examples (including `10110`), but the inspected works do not state the all-large-ring three oriented families, sharp cutoff, or exact \(3n\) indexed count. General image-testing machinery does not automatically state the stable closed form. Targeted published-record searches found no matching statement, but implicit or unindexed precedents remain a risk.

## Value — PASS
Determining the first impossible image layer is a natural reachability boundary for sparse states of a nonlinear elementary cellular automaton. The classification is infinite, orientation-sensitive, and sharp: every weight-zero-to-two state is reachable at every length at least five, while the three-orbit obstruction begins at weight three and has an exact stable count above the identified cutoff.

## Scope and limitations
Only one update on indexed periodic binary rings is covered. The result does not determine higher-weight unreachable outputs, entire image size or inverse-fiber counts. The most relevant prior papers were inspected in their image/predecessor sections; unindexed results and implicit reformulations cannot be excluded. The review is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
