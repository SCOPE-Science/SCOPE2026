# A nine-visit homometric pollen-transfer reversal under geometric carryover

## Finding

There exist two ordered **nine-visit, two-species pollinator histories** with identical species abundances and identical numbers of conspecific visit pairs at **every positive temporal lag**, yet opposite rankings of the expected number of distinct pollinated plants at short and long pollen-retention scales. For a donor-to-recipient probability \(q^{j-i}\), with \(0<q<1\), the exact expected-pollination difference switches sign **once and only once** as \(q\) increases.

In symbols, consider the two histories (symbols identify species, not repeated visits to the same individual)

```
A = 110001001
B = 011100100
```

Each history has four visits to species 1 and five to species 0. Their complete conspecific lag-pair profiles, at lags 1 through 8, coincide and equal \((4,2,3,3,2,0,1,1)\). Thus every *additive pairwise* pollen-transfer proxy of the form \(\sum_{k=1}^{8}H(k)w_k\), with arbitrary lag weights \(w_k\), ties between these histories. In particular, their counts of consecutive conspecific visits are both four.

However, let \(F_w(q)\) be the sum of the probabilities that each of the nine visited **distinct plant individuals** receives at least one successful conspecific-pollen transfer from an earlier visit. Define

\[
F_w(q)=\sum_{j=1}^{9}\left[1-\prod_{\substack{1\le i<j\\ w_i=w_j}}(1-q^{j-i})\right].
\]

Assume the donor-to-recipient attempts associated with different earlier donors are independent conditional on the specified history. For \(A\) and \(B\), direct exact expansion yields

\[
F_A(q)-F_B(q)=q^6(q-1)(q^2+q+1)R(q),
\]

where

\[
R(q)=q^9+q^7-q^6-q^4-2q^3+1.
\]

There is exactly one \(q_*\in(0,1)\) satisfying \(R(q_*)=0\); numerically \(q_*=0.719457639510222\ldots\). Consequently

\[
F_A(q)<F_B(q)\quad(0<q<q_*),\qquad
F_A(q)>F_B(q)\quad(q_*<q<1).
\]

The ties at \(q=0,1\) are boundary limits, not additional interior crossings. Nine visits are the **previously known sharp minimum for nontrivially homometric binary sequences** (Katz, Rahman and Ward); the new statement concerns the ecological nonlinear-score reversal within that first possible homometric class, not discovery of the nine-visit homometry threshold.

## Assumptions and scope

A foraging bout makes exactly nine visits, each to a distinct plant individual in one of two species. Every earlier conspecific visit \(i<j\) independently gives the individual at visit \(j\) a successful pollination attempt with probability \(q^{j-i}\). Cross-species visits contribute no conspecific pollen. The expected number of distinct successful recipient plants is the sum of their individual success probabilities. It is not the expected number of pollen grains, fruits, or repeated successful transfer events. The same retention \(q\in(0,1)\) applies to each step and both plant species; no memory or movement probability is assigned to the histories, which are conditioned upon.

An aperiodic lag profile is \(H_w(k)=\#\{i:1\le i\le 9-k,\,w_i=w_{i+k}\}\). Complementing labels and reversing time each preserve the entire lag profile. The pair above is **not** related by either operation or their combination. The finite minimality comparison is only for binary histories modulo these trivial operations; no classification is claimed for three or more plant species, repeated visits to the same individual, or other pollen-transfer kernels.

## Proof

**1. Pairwise indistinguishability.** Directly count equal-symbol pairs at each displacement for both displayed words. At lags 1 through 8 the counts are, exactly, \((4,2,3,3,2,0,1,1)\). Each word has four 1s and five 0s. Their four symmetry transforms (identity, complement, reversal, complemented reversal) give disjoint sets, so this is not a trivial reflection or relabelling ambiguity. Therefore every additive lag-score ties for all weights, including the geometric kernel \(q^k\).

**2. Distinct-plant expectation.** For recipient \(j\), independence implies that the probability of no success is \(\prod_{i<j:w_i=w_j}(1-q^{j-i})\). Summing one minus this product gives the stated \(F_w\). Multiplying the finitely many integer-coefficient binomials and subtracting the expressions for the two words gives \(q^6(q-1)(q^2+q+1)R(q)\) exactly. This is an identity of polynomials, not a numerical interpolation. The accompanying standalone checker reconstructs the polynomial from the original histories using only integer polynomial multiplication.

**3. Unique interior switch.** We have \(R(0)=1\) and \(R(1)=-1\). Put \(t=q/(1-q)>0\). The transformed polynomial \((1+t)^9R(t/(1+t))\), written from constant to degree-nine coefficient, has exactly the coefficients

```
1, 9, 36, 82, 113, 91, 33, -6, -9, -1
```

There is exactly one change of sign in the nonzero coefficient sequence in descending or ascending degree order. Descartes' rule of signs gives at most one positive zero, counting multiplicity. The intermediate value theorem supplies at least one; hence precisely one simple root \(q_*\in(0,1)\). The factor \(q^6(q-1)(q^2+q+1)\) is negative throughout this interval. Since \(R\) changes from positive to negative there, the claimed rankings follow. Exact rational evaluations give \(R(7/10)>0\) and \(R(3/4)<0\), bracketing the transition.

**4. The sharp homometry boundary is prior work.** Aperiodic binary autocorrelation equals \(2H_w(k)-(9-k)\), so the histories are homometric in the usual phase-retrieval sense. Katz, Rahman and Ward report no nontrivially equicorrelational binary words of lengths 1 through 8 and one two-class homometry at length 9. Independently, the checker enumerates all \(2^n\) binary words at each \(1\le n\le 9\), groups by their complete lag profiles, and identifies classes up to complement and reversal, confirming this boundary. This combinatorial cutoff is cited as known; only the nonlinear transfer-score comparison is advanced here.

## Verification

Run `python verify.py` with Python 3. This self-contained script computes the exact expected-success polynomials for both words from the definition, checks the closed factorization, checks their entire lag profiles and symmetry inequivalence, verifies the Descartes coefficient identity and signs using exact integers and rational arithmetic, and performs the complete binary enumeration for lengths one through nine. The emitted PASS line is diagnostic; the proof above provides the mathematical reasoning.

## Relationship to prior work

Kortsch et al. (2023) model visitation histories with geometric conspecific-pollen loss and compute the probability of at least one successful transfer by multiplying failure probabilities; their ecological simulations compare visit-count, consecutive-visit and distinct-pollinated-plant measures. That paper defines the underlying nonlinear functional but does not establish the equal-full-lag-data reversal proved here. Bruninga-Socolar et al. (2023) study individual-level specialization and sequence-dependent transfer in ecological coexistence models, without this binary homometric comparison.

Katz, Rahman and Ward (arXiv:2308.07467, first posted 14 August 2023) already give the minimal nine-symbol nontrivial binary aperiodic autocorrelation ambiguity, including its two-class structure. Thus the full-lag collision and its minimum are not newly claimed. The extra result is that, within the **exact** geometric independent-transfer functional, the two histories have a strictly unequal distinct-recipient expectation and a unique internal reversal in relative order. Standard phase-retrieval ambiguity statements do not by themselves imply that nonlinear functional or its parameter-dependent sign.

## Limitations

The claim is a finite exact benchmark for one specified pair of nine-visit histories, not a universal law for arbitrary sequences. The independence of different donor-to-recipient attempts and the geometric loss assumption are idealizations. The relationship to field pollination is conditional and uncalibrated. Both histories have the same full pairwise lag profile, but actual species identities, floral physiology, self-incompatibility, repeated individuals, interactions among donors, and pollen competition could change outcomes. Historical priority of this precise ecological transfer-score consequence has not been independently certified; broader nonlinear phase-retrieval literature could contain equivalent statements. The known nine-word homometry result is explicitly credited.

## References

1. Kortsch, S. et al., *Landscape composition and pollinator traits interact to influence pollination success in an individual-based model*, Functional Ecology (first online 14 May 2023), DOI: https://doi.org/10.1111/1365-2435.14353. Especially sections 2.5, 3 and 4, including the geometric transfer and independent-failure aggregation.
2. Katz, D. J., Rahman, A., and Ward, M. J., *Sequences with identical autocorrelation functions*, arXiv:2308.07467 (first posted 14 August 2023): https://arxiv.org/abs/2308.07467. Especially the binary equicorrelation table and introductory definitions.
3. Bruninga-Socolar, B. et al., *Pollinator-mediated plant coexistence requires high levels of pollinator specialization*, Ecology and Evolution (first published 1 August 2023), DOI: https://doi.org/10.1002/ece3.10349.
