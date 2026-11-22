# Mathematical assessment

## Correctness (C) — PASS

The claim fixes all parameter ranges and derives \(k=h'\) and the exact sign of \(k'=h''\). The derivative has either a strictly monotone path or one unique minimum according as \(b\) lies above or below \(1-2/a\). Its endpoints and minimum give sharp attainable/approachable derivative bounds \([-L,M]\). The mixed copula density is \(1+\alpha k_1k_2\); full-range density positivity is equivalent to the claimed two-sided amplitude inequality. Uniform margins are automatic from \(h(0)=h(1)=0\). Conditional distribution derivatives and the rank-one determinant give stochastic order and TP2/RR2. Exact boundary cases and the omitted singular exponent are distinguished. SymPy differentiation of the second derivative reduced identically to zero; the packaged standard-library checker reproduced the \([-4,4]\) and \([-2,2]\) special intervals, a one-switch case, negative-density witnesses beyond both boundaries, and 180 deterministic grid envelope checks. The analytic proof, not the grids, establishes universal quantifiers.

## Originality (O) — PASS, priority qualified

Chesneau (2024), DOI 10.37190/ord240304, Table 2 and Section 4.2, gives the identical FGM-N1 construction only with sufficient \(\alpha\in[-1,1]\) and displays density plots, not its optimal amplitude or the directional-order thresholds. Fuchs and Tschimpke (2023), arXiv:2306.09676, Example 4, gives the general FGM derivative-positivity condition and familiar order notions; this implies the method of reducing validity to a derivative range, but does not give the new power-mean extrema, the precise \(b=1-2/a\) switching law, or their full family-specific TP2/RR2 classification. Durante (2009) gives the general copula scheme. Amblard and Girard (2009) gives broad FGM extensions in an abstract; full-text noncoverage cannot be asserted. Search comparisons included aliases, generalized FGM rank-one formulae, and accessible recorded claims, with no identical parameter-specific theorem found. The result is not certified independent or historically unique; the inaccessible older full text remains a priority risk.

## Value (V) — PASS

The original FGM-N1 construction is an explicit five-parameter model for asymmetric dependence. Its amplitude bounds were sufficient but not known sharp within that presentation. The new necessary-and-sufficient classification separates valid from invalid likelihood models without relying on arbitrary parameter boxes, and exhibits nontrivial strict expansions such as \([-2,2]\) with a switch in just one regression direction. The one-coordinate turning-point threshold gives a complete qualitative choice between globally ordered conditional distributions and local stochastic-order reversal; its simultaneous TP2/RR2 boundary identifies when strong dependence regularity is available. These are natural structural and modeling questions about the full originally introduced family, not just a numerical improvement.

## Source comparisons and limitations

The 2024 primary article and the 2023 generalized FGM primary preprint were read at the relevant formulae and dependence discussion. The 2009 Durante construction was compared through the source article's detailed attribution; an Amblard–Girard general FGM article was only accessible at abstract level. No claimed generic FGM determinant or derivative criterion is novel. The result excludes \(b=0\) and limiting shape values; the finite checker is supplemental, and historical priority is not independently settled.

Self-review: passed. Independent audit: not yet performed.
