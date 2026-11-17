# Independent mathematical audit

## correctness

PASS

Pentagonal parity forces >=12 frustrated bonds, energy >=-66J. Icosahedral perfect matching recursion enumerates 125 matchings times 2^6 face choices times two spin orientations =16000 states with 12 frustrated bonds. Fully inspected construction uses 60 truncated-icosahedral darts, 90 edges, and exact bitflip neighbors; independent rebuilt 16000 states and BFS yielded precisely 10 components of 64 and 1 of 15360, degree histogram {6:2720,7:7680,8:5280,9:320}. Each 64-component contains one six-bit face-choice cube. Single flip costs 2J at 24 sites and 6J at 36, giving diagonal -18Γ²/J; each allowed pair has two 2J intermediates, offdiag -Γ²/J. Perron spectral radius of giant >= mean degree 29/4>6, so leading-order selection holds. Finite exhaustive checker is legitimate proof of defined finite graph, plus explicit geometry mapping; no finite-Γ exact decoupling.

## originality

PASS

Lopez-Bezanilla et al 2026 report 16000 ground-state degeneracy and second-order tunneling, which are prior ingredients, but examined full main text plus supplement do not state eleven connected sectors, 10 isomorphic Q6 pieces or giant/small Perron separation. Nakamura 2008 same classical lattice paper accessible abstract only and a residual priority risk, not evidence of tunneling-sector result.

## value

PASS

Complete reconfiguration components and effective spectral tunneling sectors for a canonical frustrated fullerene resolve a motivated finite quantum-order-by-disorder question; exact combinatorial invariants and controlled small-field meaning are useful beyond reproducing groundstate count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
