# A coupled-threshold Poisson clock for ternary circular median dynamics

## Finding

Let \(n\ge3\) and let \(M_n:\{0,1,2\}^n\to\{0,1,2\}^n\) be the synchronous cyclic median,
\[
(M_nx)_i=\operatorname{median}(x_{i-1},x_i,x_{i+1}),\qquad i\in\mathbb Z/n\mathbb Z.
\]
The first entrance time into a periodic orbit is
\[
\tau_n(x)=\min\{t\ge0:M_n^{t+2}x=M_n^t x\}.
\]
All eventual periods are one or two, and the maximal first-entrance time is **exactly** \(\lfloor(n-1)/2\rfloor\). Primitive two-cycles attract exactly
\[
\boxed{\ B_n=\begin{cases}0,&n\text{ odd},\\4\,2^{n/2}-2,&n\text{ even}.\end{cases}\ }
\]
labelled initial configurations. Thus their basin probability is exponentially small, asymptotic to \(4(\sqrt2/3)^n\) along even lengths.

For independent uniform initial symbols, let integer \(t=t(n)\to\infty\) satisfy
\[
n(2/9)^{t+1}\longrightarrow\alpha\in(0,\infty).
\]
Then the **entire first-periodic-entry clock** has the lattice extreme-value limit
\[
\boxed{\Pr\{\tau_n\le t\}\longrightarrow\exp(-10\alpha/9).}
\]
In particular, if \(n_m/(9/2)^m\to c>0\), for each fixed integer \(k\),
\[
\Pr\{\tau_{n_m}\le m-1+k\}\longrightarrow
\exp[-(10c/9)(2/9)^k],
\]
and
\[
\boxed{\mathbb E\tau_n=\log_{9/2}n+O(1),\qquad \tau_n-\log_{9/2}n=O_{\mathbb P}(1).}
\]
The finite-size distribution at every \(t\ge0\) has the exact trace formula in the proof.

## Assumptions and scope

The three symbols have the natural linear order \(0<1<2\), and the update is their median, not majority-by-category with incumbent retention when all symbols differ. Sites are indexed and not identified under cyclic rotation. Every vertex updates simultaneously; indices are modulo \(n\), and the distribution refers to \(3^n\) equally likely labelled words. A state entering a primitive two-cycle is already considered periodic, rather than being assigned an infinite first-*fixed* time. The asymptotic limit is taken through integer sequences satisfying its displayed condition; the lattice effect means no unqualified continuous Gumbel limit is asserted.

## Proof

**1. Ordered threshold conjugacy.** For each \(b=1,2\), define the threshold word \(y_i^{(b)}=\mathbf1_{\{x_i\ge b\}}\). The elementary median identity
\[
\mathbf1_{\{\operatorname{median}(a,c,d)\ge b\}}
=\operatorname{maj}(\mathbf1_{\{a\ge b\}},\mathbf1_{\{c\ge b\}},\mathbf1_{\{d\ge b\}})
\]
shows that the two thresholds evolve by binary three-neighbour majority (Rule 232), with \(y^{(2)}\le y^{(1)}\) preserved. The original ternary state is uniquely recovered from the pair by \(x_i=y_i^{(1)}+y_i^{(2)}\).

**2. Binary settling clock.** For any cyclic binary word \(y\), set \(a_i=1\) if \(y_{i-1}=y_{i+1}\ne y_i\), and \(a_i=0\) otherwise. The binary majority update flips precisely those sites with \(a_i=1\). A direct check of the eight binary triples, or the autonomous wall identity \(d'_i=d_i(1\oplus d_{i-1}\oplus d_{i+1})\) for \(d_i=y_i\oplus y_{i+1}\), shows that each finite consecutive run of \(r\) active sites is shortened by one at each end per update. If \(a\) is not identically one, the first fixed-time of \(y\) is therefore \(\lceil r_{\max}/2\rceil\); if \(a\equiv1\), then \(n\) is even and \(y\) is a checkerboard, already on a primitive two-cycle at time zero. Define \(\theta(y)\) to be that fixed-time or zero for the checkerboard. Then
\[
\tau_n(x)=\max\{\theta(y^{(1)}),\theta(y^{(2)})\}.
\]
Each threshold has a non-checkerboard active run of length at most \(n-2\) (with at least two inactive sites in an admissible noncheckerboard cyclic binary word), giving \(\tau_n\le\lfloor(n-1)/2\rfloor\). A binary extremizer on symbols \(0,2\) attains equality, proving sharpness. The threshold decomposition also rules out eventual periods beyond two.

**3. Exact two-cycle basin.** A binary three-point-majority trajectory can reach a checkerboard only when it began as that checkerboard: no zero domain wall can turn into a one. Hence a ternary word eventually oscillates if and only if at least one of the two initial threshold words is a checkerboard. For even \(n\), exactly \(2\cdot2^{n/2}\) ternary words have a checkerboard at threshold one (the low sites must be zero, the high sites can be one or two). The same count holds for threshold two. Their intersection consists exactly of the two alternating words \(0202\cdots\) and \(2020\cdots\). Inclusion-exclusion gives \(4\,2^{n/2}-2\); odd lengths admit no checkerboards.

**4. Rare alternating starts.** Put \(L=2t+3\) and \(s=t+1\). Except for a globally checkerboard threshold, the event \(\theta(y^{(b)})>t\) is exactly the occurrence of a maximal alternating binary block of at least \(L\) symbols. Define \(I_{b,i}=1\) if \(y^{(b)}_{i},\ldots,y^{(b)}_{i+L-1}\) alternate and the preceding symbol \(y^{(b)}_{i-1}\) equals \(y^{(b)}_i\). This is the *non-left-extendible* start of a long alternating block, with no double counting of a longer run. An even ring-wide checkerboard has no such start, consistently with its entrance time zero. Thus
\[
\{\tau_n\le t\}=\Big\{Z_{n,t}:=\sum_{b=1}^2\sum_{i\in\mathbb Z/n\mathbb Z}I_{b,i}=0\Big\}
\]
for \(n>L+1\), and by cyclic interpretation for all sizes. For each threshold the marginal initial binary symbols are independent with probabilities \(1/3\) and \(2/3\). Consequently
\[
\Pr(I_{b,i}=1)=\left[(1/3)^2+(2/3)^2\right]
\left[(1/3)(2/3)\right]^s
=\frac59\left(\frac29\right)^s,
\]
so \(\mathbb EZ_{n,t}=(10/9)n(2/9)^s\to10\alpha/9\).

**5. Poisson dependence estimate.** Each indicator depends on at most \(L+1\) underlying independent symbols; disjoint windows are independent. The total independent-pair error in the standard local-dependence Poisson bound is \(O(nL(2/9)^{2s})=o(1)\). Two distinct non-left-extendible starts at the same threshold cannot begin within the body of one long alternating block, and all remaining overlapping same-threshold pairs have total joint-probability contribution \(O(nL(2/9)^{2s})\). For different thresholds, an overlap of at least two alternating positions forces the common original ternary symbols to alternate strictly between zero and two: a change in *both* binary thresholds at one interface is only the transition \(0\leftrightarrow2\). For overlaps of one or zero positions, a uniform constant factor absorbs the missing forced endpoint. The common-block probability is bounded by \(C\,3^{-(L-d)}\); the two disjoint extensions of length at most \(d+1\) each have combined conditional probability at most \(C(2/9)^d\), using the alternating proportions of the two marginal threshold values. Summing over the two threshold orientations and all offsets yields \(O(n3^{-L})=o(1)\), since \(n3^{-L}=O(2^{-s})\). The finite-dependence Poisson bound therefore gives
\[
Z_{n,t}\Longrightarrow\operatorname{Poisson}(10\alpha/9),
\]
which proves the limiting zero-event law.

**6. Mean clock.** Set \(m=\lfloor\log_{9/2}n\rfloor\). For the upper tail, Markov's bound on the number of rare starts gives \(\Pr(\tau_n>m+k)\le C(2/9)^k\) for all \(k\ge0\). For the lower tail, count starts in only the first threshold. For \(t=m-k\ge0\), their mean is at least \(c(9/2)^k\), and a finite-dependence variance estimate gives \(\operatorname{Var}Z^{(1)}\le\mathbb EZ^{(1)}+CnL\,p^2\), where \(p=(5/9)(2/9)^{t+1}\). Chebyshev's inequality yields \(\Pr(\tau_n\le m-k)\le C(9/2)^{-k}+C(m+1)/n\). Summing over \(1\le k\le m\) bounds the expected negative deviation uniformly; the positive deviation is bounded by the upper tail. Thus \(\mathbb E\tau_n=m+O(1)=\log_{9/2}n+O(1)\). \(\square\)

**7. Exact finite-time matrix.** For fixed \(t\ge0\) set \(L=2t+3\). Take states \(u\in\{0,1,2\}^{L}\). For each symbol \(c\in\{0,1,2\}\), add a directed edge
\[
(u_0,\ldots,u_{L-1})\longrightarrow(u_1,\ldots,u_{L-1},c)
\]
unless for at least one threshold \(b\in\{1,2\}\), the binary projection of the \(L+1\) input symbols satisfies \(v_0\ne v_2\) and \(v_j\ne v_{j+1}\) for all \(1\le j<L\). Let \(A_t\) be this \(3^L\)-square zero-one adjacency matrix. Its closed walks are precisely the indexed ternary words with no long alternating start in either threshold; uniqueness of the cyclic history gives
\[
\boxed{\#\{x\in\{0,1,2\}^n:\tau_n(x)\le t\}=\operatorname{tr}(A_t^n)\qquad(n\ge3).}
\]
This is an exact all-time finite expression, although matrix size grows exponentially with \(t\).

## Verification

The accompanying Python 3 program `verify_median.py` uses only the standard library. It independently iterates the ternary median rule, verifies threshold commutation and the predicted first-periodic-entry clock for every one of the \(3^n\) initial words at every \(3\le n\le11\), and checks the two-cycle basin formula and sharp maximum. A second automaton enumerator compares the trace formula at lengths \(3\le n\le7\) for times zero and one when applicable. Seeded simulations at \((n,t)=(410,3),(1845,4)\) provide a finite statistical check of the Poisson prediction; those experiments are not substituted for the asymptotic proof. The program emits `VERIFY_MEDIAN_OK` upon successful completion; its captured output is provided in `verification_output.txt`.

## Relationship to prior work

Fitch, Coyle and Gallagher (1985) developed general finite-alphabet median-root counting and considered finite pass counts for **binary** signals. The relevant reproduced introduction and final-section text was inspected, but its original full publisher PDF was not completely accessible. Tosic and Agha (2004) and prior results on cyclic binary majority establish fixed/alternating behavior and its binary settling clock. The previously published exact finite-time Rule 232 census and binary Poisson-window analysis concern one threshold, not the ordered, coupled two-threshold ternary median or its two-cycle basin and the mixed-overlap constant \(10/9\). Work on cyclic median Lipschitz/variation constants examines the response to perturbations, rather than this random initial-state clock. On an all-distinct local triple, a ternary median can differ from incumbent-retaining categorical plurality, so general plurality classifications do not imply this result. No equivalence or stronger theorem covering the displayed coupled-threshold law was identified in the inspected sources.

## Limitations

The result is specific to equally likely ordered symbols \(0,1,2\) and synchronous width-three cyclic median. The Poisson limit assumes the stated lattice subsequences; no uniform all-real centered extreme-value convergence is claimed. The trace formula is exact but grows as \(3^{2t+3}\) states. The asymptotic proof uses the fixed uniform distribution and the two nested thresholds. Although the closest accessible literature was compared at the claim level, an unpublished or inaccessible historical equivalent, especially in classical median-filter work, remains possible. No independent external review has been performed.

## References

1. J. P. Fitch, E. J. Coyle and N. C. Gallagher, “Root Properties and Convergence Rates of Median Filters,” *IEEE Transactions on Acoustics, Speech, and Signal Processing* 33(1) (1985), 230–240, https://doi.org/10.1109/TASSP.1985.1164543 .
2. C. Moore, “Majority-Vote Cellular Automata, Ising Dynamics, and P-Completeness,” public preprint January 20, 1997, https://arxiv.org/abs/cond-mat/9701118 .
3. P. T. Tosic and G. A. Agha, “Characterizing Configuration Spaces of Simple Threshold Cellular Automata,” ACRI (2004), https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf .
4. “Exact stabilization-time distribution for the cyclic three-site majority automaton,” published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-stabilization-time-distribution-for-the-cyclic-three-site--ea6170529cae .
5. “Exact first-periodic-entry law and Poisson extremes for majority-three rings,” published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-first-periodic-entry-law-and-poisson-extremes-for-majority--d0c0e063c265 .
