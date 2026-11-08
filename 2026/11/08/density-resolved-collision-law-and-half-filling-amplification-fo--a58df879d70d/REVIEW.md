# Scientific review

## Correctness

**PASS.** The claim fixes labelled cyclic words, synchronous Rule 184 and ordered input pairs. The paired-symbol de Bruijn construction is a bijection between closed walks and colliding ordered inputs, with its monomial recording exactly the conserved particle number. Exact symbolic elimination verifies the displayed determinant; formal trace logarithms yield the full bivariate generating function. The fourth-degree factor has a unique largest positive root at unit weight. A primitive 12-state component with loops of weights \(1\) and \(z\) supplies a strict nonzero-frequency spectral gap, making the central local limit valid without an unacknowledged lattice factor. An exact implicit derivative gives the positive variance. Standalone direct enumeration at all lengths 3–16 and central coefficients at even lengths to 200 provide additional checks, but are not presented as an infinite proof.

## Originality

**PASS, with historical uncertainty.** The closest fully read works are Fukś (1997), https://arxiv.org/pdf/comp-gas/9703001, and Fukś (1999), https://arxiv.org/pdf/comp-gas/9902001, concerning density classification, traffic current, and fixed-block preimage enumeration. They do not state the global one-update, particle-number-resolved second moment or its Gaussian central-density asymptotic. Rodríguez Zamora and Chapa (2004), https://doi.org/10.1007/978-3-540-30479-1_32, analyze Rule 184 using de Bruijn diagrams, but its full text was unavailable; possible coverage is a residual risk, not declared absent. The accessible finite-size atlas gives finite illustrations, not this infinite-family formula. An existing exact mass-resolved Rule-184 entrance-time census counts settling times to free flow, not colliding preimages after one update. Earlier exact collision work for Rule 4 is a different local rule and does not imply this transfer characteristic polynomial or conserved-density result. Published-record searches located no stronger covering statement; search absence alone does not prove novelty.

## Mathematical value

**PASS.** Rule 184 is a canonical conservative traffic automaton. Its output fibers measure irreversible information loss even though particle number is conserved. The exact two-variable count resolves the natural entire microcanonical collision profile, not an arbitrary small-size slice or known traffic-current statistic. The distinction between Bernoulli and exact-half-filling input ensembles is sharp: the same exponential rate acquires an explicit \(\sqrt n\) factor. This is a structural ensemble effect and a useful benchmark for information-theoretic analysis of conservative cellular automata, rather than a mere new finite census.

## Scope and priority limitations

The theorem addresses only one-step collisions on labelled finite rings and the central-density asymptotic; no claim is made about long-time equilibrium, other rules or independent validation. The 2004 de Bruijn chapter was materially inaccessible, and unindexed equivalent formulas are possible. The determinant is a finite exact identity whose source is fully supplied in executable form; the asymptotic proof identifies its necessary spectral conditions.

Self-review: passed. Independent audit: not yet performed.
