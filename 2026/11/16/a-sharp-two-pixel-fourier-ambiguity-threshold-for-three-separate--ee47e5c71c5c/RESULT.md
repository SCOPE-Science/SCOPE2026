# A sharp two-pixel Fourier ambiguity threshold for three separated intervals

## Finding
Let \(N\ge10\) be an integer, and let \(\Omega\subset[0,N)\) be the union of exactly three separated intervals with integer endpoints, with both extreme unit cells occupied. Suppose that all three occupied runs and both intervening gaps contain **at least two consecutive unit cells**. Given the complete continuous Fourier magnitude \(|\widehat{\mathbf1_\Omega}(\xi)|\), \(\xi\in\mathbb R\), recovery among such three-interval masks is unique up to translation and reflection for every \(N\le23\). At span \(N=24\), precisely one unordered pair of inequivalent reflection classes has the same magnitude. Its representatives are
\[
\Omega_A=[0,10)\cup[12,18)\cup[22,24),\qquad
\Omega_B=[0,4)\cup[8,20)\cup[22,24).
\]
Thus the sharp first ambiguous span is **24 unit cells**, with exactly one nontrivial two-class fiber there. The statement is confined to the stipulated integer-endpoint, three-component, two-cell feature-floor model; it does not assert phase retrieval against unconstrained real-endpoint sets.

A related all-resolution construction is exact: for **every** pair of integers \(w,g\ge1\), two inequivalent homometric three-run masks with occupied lengths at least \(w\) and separating gaps at least \(g\) exist at span \(7w+5g\). Their successive occupied/gap/occupied/gap/occupied length tuples are
\[
(3w+2g,\,g,\,2w+g,\,w+g,\,w),\qquad
(w+g,\,w+g,\,4w+2g,\,g,\,w).
\]
This is an **upper bound**, not a claimed sharp first ambiguity span for arbitrary \(w,g\). The two-cell case \(w=g=2\) is sharp by the complete census above.

## Assumptions and scope
For a tuple \((a,u,b,v,c)\) of positive integers, write the length-\(N\) binary word \(1^a0^u1^b0^v1^c\), where \(N=a+u+b+v+c\). The corresponding set is the union of its occupied half-open unit cells \([j,j+1)\). In the first theorem, \(a,u,b,v,c\ge2\). Reflection reverses the five-tuple, and normalized words begin and end in an occupied cell; any translation equivalence therefore reduces to equality of normalized words. Fourier transform is normalized by \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i\xi t}\,dt\). Complete magnitude means all real frequencies, not a finite DFT grid. All calculations are exact integer identities.

## Proof
**Fourier reduction.** Let \(P(z)=\sum_{j=0}^{N-1}w_jz^j\). With \(U(\xi)=\int_0^1e^{-2\pi i\xi t}\,dt\), direct integration gives \(\widehat{\mathbf1_\Omega}(\xi)=U(\xi)P(e^{-2\pi i\xi})\). Since \(U\) does not vanish on a dense set, equal magnitudes for two masks are equivalent to equal Laurent polynomials \(P(z)P(z^{-1})\). Their coefficients are the exact aperiodic autocorrelations
\[
C(h)=\sum_{j=0}^{N-1-h}w_jw_{j+h},\quad 0\le h<N.
\]
As \(C(N-1)=1\) and all larger lags vanish, the magnitude determines \(N\) before comparison. The reflection symmetry preserves all correlations.

**Complete sharp finite lower bound and first fiber.** Every admissible normalized mask is in bijection with a five-part integer composition of \(N\) with each part at least \(2\); there are exactly \(\binom{N-6}{4}\) such words. `CHECK.py` independently generates all these compositions both by stars-and-bars and by four integer cut positions. For each word, it computes all \(N\) integer correlations in three mathematically equivalent ways: bit intersections, direct cell-pair counting, and set-membership pair counting. It groups masks by the complete vector and collapses tuple reversal. It asserts the exhaustiveness counts, palindromic fixed points and first nontrivial fiber. The complete results are:

| Span \(N\) | Words | Reflection classes | Distinct correlation vectors | Nontrivial fibers |
|---:|---:|---:|---:|---:|
| 10 | 1 | 1 | 1 | 0 |
| 11 | 5 | 3 | 3 | 0 |
| 12 | 15 | 9 | 9 | 0 |
| 13 | 35 | 19 | 19 | 0 |
| 14 | 70 | 38 | 38 | 0 |
| 15 | 126 | 66 | 66 | 0 |
| 16 | 210 | 110 | 110 | 0 |
| 17 | 330 | 170 | 170 | 0 |
| 18 | 495 | 255 | 255 | 0 |
| 19 | 715 | 365 | 365 | 0 |
| 20 | 1001 | 511 | 511 | 0 |
| 21 | 1365 | 693 | 693 | 0 |
| 22 | 1820 | 924 | 924 | 0 |
| 23 | 2380 | 1204 | 1204 | 0 |
| 24 | 3060 | 1548 | 1547 | 1 |

Every one of the \(11{,}628\) admissible words through span \(24\) is visited. The unique exceptional correlation vector is
\[
(18,15,12,11,10,10,10,10,10,9,8,7,6,6,6,5,4,3,2,2,2,2,2,1).
\]
The two canonical tuples are \((2,2,12,4,4)\) and \((2,4,6,2,10)\); reflecting them produces the displayed representatives. By the composition bijection and exhaustive exact comparison, no earlier ambiguity is possible. This is a finite proof certificate with a clearly specified complete search space, not extrapolation from sampled lengths.

**Exact all-resolution witness.** Put \(X=z^w\) and \(Y=z^g\), and let \(Q=(1-z)P\), the signed endpoint polynomial of an interval mask. For the two parametrized masks, direct endpoint expansion gives
\[
Q_A=R(1+XY+X^4Y^3),\qquad
Q_B=R(1+X^3Y^2+X^4Y^3),
\]
where \(R=1-XY+X^2Y^2-X^3Y^2\). The second parenthesis is the two-variable reciprocal of the first, multiplied by \(X^4Y^3\). On \(|z|=1\), both have equal modulus. Their endpoint polynomials, hence indicator Fourier transforms, have equal moduli for **every** positive integer \(w,g\). Their tuples are neither identical nor reversals for any \(w,g>0\). Their length is \(7w+5g\), and the occupied/gap lower bounds are satisfied. A direct symbolic coefficient comparison of the endpoint autocorrelations is included in `CHECK.py`.

## Verification
Run `python3 CHECK.py` using Python 3.10 or later and only the standard library. Successful complete execution ends with `CHECK_OK raw_words=11628 reflection_classes=5916 first_ambiguity=24 exceptional_unordered_pairs=1`. The checker additionally verifies the all-resolution endpoint identity as a formal Laurent-polynomial identity in two independent variables, and tests sample integer parameters; the formal identity, not the parameter samples, proves that assertion. Every comparison of the finite classification is integer-exact. The complete census is limited to spans through the first ambiguity and does not imply uniqueness at subsequent spans.

## Relationship to prior work
Xia and Xu's *Fourier Phase Retrieval for Finite Unions of Intervals* (2026) establishes general nonuniqueness for three or more intervals and polynomial factor reversal, and discusses separation-based uniqueness criteria; these principles explain the algebraic construction but do not provide the exact two-cell-width **and** two-cell-gap first-span classification. A prior complete integer-grid census establishes first three-run nonuniqueness at span \(12\) with one-cell features; another establishes first nonuniqueness at span \(19\) when only occupied lengths are at least \(2\). Neither has the simultaneous two-cell foreground-and-background restriction. A published four-run result for the simultaneous two-cell floor has first nonuniqueness at span \(22\): its different component count means it does not imply this theorem, but the comparison shows that the onset of ambiguity need not increase with the number of components. General autocorrelation factor-reversal and run theory are acknowledged, not claimed as new here.

## Limitations
The sharp assertion is only for exactly three occupied components with integer endpoints, two-cell minimum occupied intervals **and** gaps, and complete continuous-frequency measurements. It does not assert uniqueness against masks with other component numbers, noninteger endpoints or noisy finite frequency sampling. The all-resolution construction gives upper bounds, not exact thresholds for general \(w,g\). Aperiodic-autocorrelation factorization and dilation of older witnesses are prior mathematics; the specifically new claim is the constrained sharp first threshold and complete first fiber, not a novel factorization mechanism. Similar unindexed constrained binary-homometry tables may exist. The finite census is reproducible but has not undergone independent mathematical audit.

## References
1. Yu Xia and Zhiqiang Xu, *Fourier Phase Retrieval for Finite Unions of Intervals*, arXiv:2606.19855, first publicly posted 2026-06-18, https://arxiv.org/abs/2606.19855 .
2. Daniel J. Katz, Adeebur Rahman, and Michael J. Ward, *Sequences with identical autocorrelation functions*, arXiv:2308.07467, first publicly posted 2023-08-14, https://arxiv.org/abs/2308.07467 .
3. Jürgen Willms, *Autocorrelations of Binary Sequences and Run Structure*, arXiv:1206.4572, https://arxiv.org/abs/1206.4572 .
4. *The first Fourier-indistinguishable three-block binary apertures* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-first-fourier-indistinguishable-three-block-binary-apertures--3e3357db2e1b .
5. *The first no-singleton three-interval Fourier ambiguity on an integer grid* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-first-no-singleton-three-interval-fourier-ambiguity-on-an-in--1547c05410eb .
6. *First Fourier ambiguity for four binary intervals with a two-pixel feature floor* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-first-fourier-ambiguity-for-four-binary-intervals-with-a-two-pix--9b4c47fba605 .
