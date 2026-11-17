# Scientific assessment: leaf-harmonic Lipschitz extension

## Correctness — PASS

A rooted-edge summation-by-parts identity proves the finite tree cut formula without relying on a formal transport black box: all bounded edge increments can be realized simultaneously because the domain graph is a tree. Strong discrete maximum principle applied to the distance-to-a-leaf function gives strict expansion at a leaf edge whenever any branch exists. On spiders, central harmonicity determines the exact weighted mean, and equality in the positive-weight inequalities classifies all norming boundary data. A reciprocal convexity argument proves the fixed-order optimal arm balancing, and two-sided elementary estimates prove the sharp asymptotic constant. `check_harmonic_extension.py` independently checks these calculations on finite instances with exact rational arithmetic. The tests are corroborative, not infinite proofs.

## Originality — PASS, with historical-priority risk

The closest directly relevant public works study **different extension operators or norms**. Naor--Sheffield (arXiv:1005.2535, Theorems 1–3) give norm-preserving infinity-harmonic/absolutely minimal extensions, not the energy-minimizing linear mean-value operator. Espínola--Nicolae (arXiv:1502.06842, introduction and §5) give continuous or nonexpansive selections, not the fixed operator norm. Fefferman--Klartag (arXiv:2301.13792, Theorems 1.1–1.2 and §2) study weighted \(W^{1,p}\) traces for \(1<p<\infty\) on radially symmetric binary trees, not the graph-distance Lipschitz trace on nonuniform spiders. The potential-theoretic Dirichlet existence and Green formulas of Abodayeh--Anandam (2005) are acknowledged as background; the full paper was not materially inspected and could conceal a closely related calculation. Searches of indexed published findings and other literature did not reveal a stronger assertion implying the complete spider norm, the exact finite-order balance classification and the \(\sqrt n/2\) law. Search absence alone is not proof of novelty.

## Value — PASS

Energy-minimizing harmonic extension is a canonical *linear* extension procedure. The sharp distinction between path nonexpansivity and strict distortion on every branching tree, together with a precise unbounded worst-spider rate as the size increases, measures an intrinsic stability cost not explained by existence of optimal nonlinear extensions. A complete finite-size optimizer classification and explicit exact norm formula make the result directly reproducible. This is a sharp structural invariant, not a single low-order example or a routine statement of the maximum principle.

## Limitations and further verification

The general-tree cut formula is finite but depends on the harmonic measure matrix; no closed degree-only formula for arbitrary trees is asserted. The \(\sqrt n/2\) extremal law concerns spiders only. Weights, partial boundary sets and other exponents are outside scope. Historical priority remains uncertain because older potential theory literature was not exhaustively read, including the complete 2005 tree-Dirichlet article. Independent review and validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
