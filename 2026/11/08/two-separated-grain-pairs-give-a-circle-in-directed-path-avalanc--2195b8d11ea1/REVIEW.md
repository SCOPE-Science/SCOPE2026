# Review of the two-pair avalanche-circle theorem

## Correctness — PASS

For every integer \(g\ge1\) and \(t\ge0\), the binary configuration on an absorbing right-directed path has firing supports given exactly by translates of \(\{0,1,g+2,g+3\}\), truncated at the sink. The last vertex of every longer path is dominated, since its link is a triangle attached to an edge at a common apex. Five elementary pairs remove each trailing vertex. In the shortest admissible path, seven explicit elementary pairs leave the polygon \(C_{g+2}\). Every step is a valid simplicial collapse and establishes the integral homotopy type \(S^1\), without extrapolation from finite tests. The embedded standard-library verifier replayed 5,772 elementary pairs in 156 parameter cases and independently checked mod-two homology in 42 cases.

## Originality — PASS, subject to literature uncertainty

The closest primary work is Henri Riihimäki and Jason P. Smith, *Avalanche homology of digraphs via sandpile dynamics* (arXiv:2606.26786, posted 2026-06-25). Its Section 3.1 classifies one consecutive block and the separated **three-grain** configuration \(\{0,1,g+2\}\), proving a wedge of \(t+2\) circles for the latter on the same path. Its results do not imply what happens after adding a fourth grain at \(g+3\), and they do not contain the five-pair dominated-vertex reduction or the constant-rank two-pair classification. A published residue-class avalanche finding concerns directed cycles rather than terminating paths. Phrase, equivalence, parameter and broader-result searches found no theorem covering the present claim. Unindexed or implicit earlier work remains a risk; negative searches are not proof of worldwide uniqueness.

## Value — PASS

The four-grain two-run support is a natural first extension of a family whose first-homology rank can grow arbitrarily with the length of the trailing zero run. A single additional grain makes that rank uniformly one. The all-parameter simple-homotopy collapse explains this dramatic sensitivity, establishes a sharp gap transition from the contractible one-block case, and gives a small geometric core for any amount of trailing padding. The finding does not claim results for arbitrary binary strings, alternative firing models, or persistence.

## Evidence, limitations and review status

The first-posted arXiv preprint and its 2026-11-02 revision were inspected at the definitions, comparison theorems and proofs, summary table, and discussion. The standalone verifier and its output are embedded and reproducible, with no third-party package dependencies. The mathematical proof establishes all integer parameters; the finite verification is supplementary. A finding-index search located a result on directed-cycle residue supports, but its full paper was not inspected and no uniqueness claim rests on that absence. Independent mathematical review remains outstanding.

Self-review: passed. Independent audit: not yet performed.
