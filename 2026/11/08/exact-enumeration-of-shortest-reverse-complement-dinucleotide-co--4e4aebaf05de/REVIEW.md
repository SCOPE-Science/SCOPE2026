# Scientific review of the reverse-complement dinucleotide cycle census

## Correctness — PASS

The ten reverse-complement dinucleotide orbits force length at least ten; the displayed example achieves it. At equality each orbit appears exactly once. There are precisely six independent two-choice orbits, so all candidates reduce to sixty-four distinct directed edge sets, of which twenty-four are balanced and connected. The matrix–tree/BEST evaluation gives eight each of 36, 12 and 20 Euler tours, totaling 544. The direct census independently checks all 1,048,576 rooted ten-letter words and all symmetry orbits. The explicit distinction between cyclic and linear words is essential and is maintained throughout.

## Originality — PASS, qualified

Orenstein and Shamir's 2013 article gives shortest sequence constructions and the length ten at order two, and explicitly lists enumeration of all optimal RC-complete sequences among its open questions. Sections on the optimization, numerical tables and the conclusions were read. Schmidt and Alanko's 2023 article addresses optimal representations of sets of k-mers and proves algorithms for constructing representations, rather than counting the minimum single cycles of this exact instance. Database and targeted published-literature searches found no prior evaluation of 544, 272, or the 37-class symmetry partition. Since absence from search results is not proof of novelty, unindexed historical finite computations remain a stated priority risk. The known minimum length and standard Eulerian counting theorems are not presented as contributions.

## Value — PASS

The original 2013 research expressly motivates counting distinct optimal reverse-complement-complete sequences. For the first even window length, the finding determines the full number of shortest alternative circular probe designs, shows how identifying DNA strands changes the count, and classifies the remaining nucleotide-symmetry types. The 544-cycle catalog is a complete reproducible design space, not an arbitrary numerical slice; it provides a concrete baseline for studying further constraints and longer windows.

## Scope, evidence and residual risks

Reproducibility consists of `RESULT.md`, `verify_graph.cpp`, `verify_direct.py`, and `catalog.txt`; the two verifiers were executed on the embedded artifact versions. The claim is not an all-order theorem or a claim about linear DNA probes. Independent historical-priority verification remains unperformed. The full related articles were inspected using their openly accessible HTML text, not inferred from search snippets.

Self-review: passed. Independent audit: not yet performed.
