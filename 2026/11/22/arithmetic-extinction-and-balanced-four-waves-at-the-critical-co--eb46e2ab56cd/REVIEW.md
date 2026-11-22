# Scientific review: arithmetic extinction and balanced four-waves

## Correctness — PASS

The hypothesis is a connected simple \(2r\)-regular graph with integer adjacency spectrum and \(3\nmid|V|\), with threshold \(r\). The proof verifies its critical nonstandard step directly: every recurrent excitation has exactly \(r\) contacts to the preceding excitation layer and \(r\) to the succeeding layer. Thus \(Ae_t=r(e_{t-1}+e_{t+1})\), every vertex fires the same number of times per period, and each time layer has the same size. Integrality confines Fourier orders to \(1,2,3,4,6\), hence periods divide twelve. Divisibility of layer sizes excludes periods three and six; a primitive twelfth-root coefficient and the three-unit-vector cancellation lemma exclude twelve. Four-period orbits are parametrized bijectively by parity orientation and binary adjacency-nullvectors. The proof covers every finite initial configuration because the transition system is finite, but makes no uniform upper bound on entry time.

Exact independent checks in `verify.py` establish the 35-vertex \(KG(7,3)\) spectrum and odd cycle, the signed-nullvector and actual four-cycle counts on \(Q_4\) and \(K_{4,4}\), extinction on all 243 states of \(K_5\), and the first seven Lucas residues. The infinite claims follow analytically rather than from these tests.

## Originality — PASS, with residual risk

The closest previously recorded integrality argument only bounds recurrent periods by twelve, and does not eliminate twelve-cycles using firing multiplicity, classify four-period states by signed zero eigenvectors, or prove critical-threshold extinction for odd Kneser graphs whose spectra still contain the threshold eigenvalue. The closest earlier half-degree classification concerns initially three-periodic waves and is silent on this arithmetic obstruction. Classical spectral descriptions of odd graphs and standard theory of equitable two-colorings describe necessary ingredients but do not establish this dynamical classification.

The original 1993 threshold-scaling work treats regular lattice media; the primary arbitrary-graph papers by Gravner–Lyu–Sivakoff (2016) and Doba (2018) define the one-neighbor rule, not a half-degree threshold. The perfect-coloring literature concerns local color balance without the stated time-dynamical period restriction. Searches explicitly included synonyms for four-phase perfect colorings, graph adjacency null functions, threshold saturation, Kneser odd graphs and primitive twelve-cycles. The same-model claim-level check found no equivalent theorem or stronger implication. Unindexed results and an incomplete scan of all specialized coding-theory sources remain genuine originality risks; search absence alone is not novelty proof.

## Value — PASS

The result closes a concrete gap left by a spectrum-only twelve-period bound: integral eigenvalues permitting a six- or twelve-frequency can still fail to support a periodic excitation because the order of the graph cannot accommodate the required firing population. The family \(KG(8\cdot3^a-1,4\cdot3^a-1)\) is connected, triangle-free and nonbipartite with growing odd girth; its critical eigenvalue is present, so the earlier spectral-exclusion criterion cannot give the conclusion. At the opposite boundary, the exact binary-nullvector correspondence counts all four-cycles on bipartite graphs and yields a closed formula on balanced bicliques. These are natural graph-theoretic regimes and a structural dynamical selection rule, not an arbitrary parameter computation.

## Limitations and closest related literature

The proof does not cover graphs of nonintegral spectrum, graph orders divisible by three, disconnected graphs or thresholds different from half-degree. It does not compute general transient lengths or extinction-basin sizes. The closest research antecedents are the integral-spectrum twelve-period restriction, the half-degree three-period rigidity theorem, the primary one-neighbor finite-graph excitation analyses, and the theory of equitable or perfect colorings. The new argument is not a claim that the usual Kneser spectral formula, Lucas's theorem or the existence of signed adjacency-nullvectors is new.

Self-review: passed. Independent audit: not yet performed.
