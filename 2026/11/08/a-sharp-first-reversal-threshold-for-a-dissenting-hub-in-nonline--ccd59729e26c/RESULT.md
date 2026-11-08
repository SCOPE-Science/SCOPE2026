# A sharp first-reversal threshold for a dissenting hub in nonlinear voter dynamics

## Finding

**Theorem (first hub-reversal law and its threshold).** Consider the continuous-time two-opinion nonlinear voter rule in which each vertex independently changes to the opposite opinion at rate \((a_i/d_i)^q\), with \(q>0\), \(d_i\) its degree, and \(a_i\) its number of disagreeing neighbors. On the simple star \(K_{1,m}\), \(m\ge2\), initialize the hub with opinion \(+\) and every leaf with opinion \(-\). Let \(K_m\) be the number of still-minus leaves immediately before the *first hub opinion reversal*; set \(K_m=0\) if all leaves adopt \(+\) before any hub reversal. For each integer \(0\le k\le m\),
\[
\Pr(K_m\le k)=\prod_{j=k+1}^{m}\left(1+\frac{j^{q-1}}{m^q}\right)^{-1}.
\]
In particular, the probability of an uninterrupted takeover by the lone positive hub is
\[
P_m(q)=\Pr(K_m=0)=\prod_{j=1}^{m}\left(1+\frac{j^{q-1}}{m^q}\right)^{-1}.
\]
For each \(m\ge2\), \(P_m(q)\) increases strictly and continuously in \(q\) and admits a unique sharp half-probability threshold \(q_m\in(1,2)\), defined by \(P_m(q_m)=1/2\). In the three-vertex path \(q_2=\log_2 3\). As \(m\to\infty\) at fixed \(q>0\), \(K_m/m\) converges in distribution to a random variable \(X_q\) on \([0,1]\) with
\[
\Pr(X_q\le x)=\exp\!\left(-\frac{1-x^q}{q}\right),\quad 0\le x\le1.
\]
Thus \(X_q\) has an atom of mass \(e^{-1/q}\) at zero and density \(x^{q-1}e^{-(1-x^q)/q}\) on \((0,1)\), and
\[
\lim_{m\to\infty}q_m=\frac1{\log2}.
\]
For every \(m\ge2\) and \(q\ge2\), the initially lone hub opinion reaches unanimous consensus **without the hub ever changing opinion** with probability strictly above one half. For every fixed \(q>1/\log2\), the same conclusion holds for all sufficiently large \(m\). Consequently the *unrestricted* probability of eventual positive consensus is also greater than one half in these regimes; no exact unrestricted fixation probability is asserted.

## Assumptions and scope

The graph is a fixed, finite, undirected, unweighted star with a single hub and \(m\) leaves, every node having its own unit-rate exponential update clock. In the binary model, an updating vertex flips only if the independent nonlinear adoption event occurs; equivalently, its actual flip rate is \((a_i/d_i)^q\). The two opinions are symmetric. A hub reversal is its first actual change of opinion, not an update clock ring without a flip. All probabilities refer to the specified initial condition. At \(K_m=0\) the first hub reversal never occurs, since unanimity is absorbing. The exponent \(q\) is fixed when taking \(m\to\infty\). Primary subject: social-network opinion dynamics, MSC2020 91D30.

## Proof

While the hub retains opinion \(+\), suppose exactly \(j\) leaves retain opinion \(-\). Each such leaf has its sole neighbor in state \(+\), and so flips at rate \(1\); hence the total leaf-conversion rate is \(j\). The hub has exactly \(j\) disagreeing neighbors out of \(m\), so its first-reversal hazard is \(r_j=(j/m)^q\). These clocks are independent and memoryless. Starting with \(j=m\), the next actual change is a leaf conversion with probability
\[
\frac{j}{j+r_j}=\left(1+\frac{j^{q-1}}{m^q}\right)^{-1},
\]
and a hub reversal otherwise. To reach \(j=k\) without a reversal, all races at \(j=m,m-1,\ldots,k+1\) must have leaf conversions. After reaching \(k\), either the hub reverses at some level at most \(k\), or all leaves convert; this is precisely \(\{K_m\le k\}\). Multiplication of the independent successive conditional probabilities proves the exact distribution and the expression for \(P_m(q)\).

For \(m\ge2\), the factor indexed by \(j<m\) strictly increases with \(q\), while the \(j=m\) factor is \(m/(m+1)\). Thus \(P_m\) is continuous and strictly increasing. As \(q\downarrow0\), every \(r_j\to1\), so telescoping gives \(P_m(q)\to\prod_{j=1}^m j/(j+1)=1/(m+1)<1/2\). As \(q\to\infty\), all \(r_j\to0\) for \(j<m\), and \(P_m(q)\to m/(m+1)>1/2\). Consequently the intermediate-value theorem gives a unique \(q_m>0\). At \(q=1\), every denominator factor is \(1+1/m\), yielding \(P_m(1)=(m/(m+1))^m<1/2\), since \((1+1/m)^m>2\) for \(m\ge2\). At \(q=2\) and \(m\ge3\), using \(\log(1+t)<t\) gives
\[
-\log P_m(2)<\sum_{j=1}^{m}\frac{j}{m^2}=\frac{m+1}{2m}\le\frac23<\log2.
\]
The final inequality follows, for example, from \(\log2=2(1/3+1/(3\cdot3^3)+\cdots)>2/3\). For \(m=2\), \(P_2(2)=8/15>1/2\). Thus \(1<q_m<2\). Moreover \(P_2(q)=(2/3)(1+2^{-q})^{-1}\); the equation \(P_2=1/2\) is \(2^{-q}=1/3\), proving \(q_2=\log_2 3\).

Fix \(q>0\) and \(x\in[0,1]\); write \(k_m=\lfloor mx\rfloor\) and \(t_{m,j}=m^{-1}(j/m)^{q-1}\). Then
\[
\log\Pr(K_m/m\le x)=-\sum_{j=k_m+1}^{m}\log(1+t_{m,j}).
\]
For every \(q>0\), the largest \(t_{m,j}\) tends to zero (it is at most \(\max(m^{-q},m^{-1})\)); the sum of the \(t_{m,j}\) is bounded because its improper Riemann sums converge to \(\int_x^1u^{q-1}\,du=(1-x^q)/q\). The inequality \(0\le t-\log(1+t)\le t^2/2\) bounds the total logarithmic approximation error by \((\max_jt_{m,j})\sum_jt_{m,j}/2\to0\). Therefore the limiting distribution function is \(F_q(x)=e^{-(1-x^q)/q}\). It is continuous on \((0,1]\) and has a jump of size \(e^{-1/q}\) at zero when extended by zero to the negative half-line. Differentiating on \((0,1)\) gives the density claimed. In particular \(P_m(q)\to e^{-1/q}\). Since each \(P_m\) is strictly increasing and \(e^{-1/q}\) is continuous strictly increasing with its unique half-crossing at \(q_*=1/\log2\), bracketing at \(q_*\pm\varepsilon\) proves \(q_m\to q_*\). The takeover-without-reversal event implies eventual positive consensus, establishing both majority-probability consequences without any claim about the other paths.

## Verification

Run `python3 verify.py` with Python 3 standard library. The checker independently constructs the first-event absorbing chain (states: number of dissenting leaves while the hub is unchanged), solves exact rational hitting recurrences, and compares with the product law for \(m=2,\ldots,16\) and integer exponents \(q=1,2,3,4\). It also checks normalization and an independent full two-opinion star chain's positive-consensus probability, confirming that it is at least the no-reversal probability for small stars. Numerical root samples and limiting-law comparisons are diagnostic only. The proof above, not these finite computations, establishes the theorem for all \(m\ge2\) and real \(q>0\).

## Relationship to prior work

Ramirez, Vazquez, San Miguel and Galla's 2023 nonlinear voter model defines flip rates as powers of local disagreement fractions and studies nonlinear ordering and pair approximations on complex networks. The first-reversal stopping distribution, its atom-containing star limit, and its half-probability threshold are not stated in the inspected original full text. The earlier q-voter literature studies nonlinear imitation, mainly mean-field and other network classes. The exact initial-hub stopping law is distinct from previously studied *eventual fixation* probabilities or stationary magnetizations. Standard competing exponential races and Riemann-sum methods are used openly; the claim of originality is the combined model-specific law and sharp leader-stability transition, not those tools themselves.

## Limitations

The formula gives the **first** hub reversal, including an atom for no reversal; it does not describe subsequent reversals, the full law of ultimate consensus, conditional mean absorption time, or arbitrary graph topologies. The majority lower bound is sufficient rather than necessary for eventual hub-opinion fixation. These statements do not imply a sharp eventual-fixation threshold at \(1/\log2\). The zero-at-origin atom is not a continuous density. The empirical numerical checks do not establish general identities. Publication-priority search is not exhaustive and no independent external validation has occurred.

## References

- L. S. Ramirez, F. Vazquez, M. San Miguel, T. Galla, *Ordering dynamics of nonlinear voter models*, arXiv:2310.20548v1 (publicly submitted 31 October 2023), https://arxiv.org/html/2310.20548v1 . In particular sections II (definition), V (network approximations), and VII (conclusions).
- C. Castellano, M. A. Muñoz, R. Pastor-Satorras, *Nonlinear q-voter model*, Physical Review E 80, 041129 (2009), https://doi.org/10.1103/PhysRevE.80.041129 .
- B. Min, M. San Miguel, *Fragmentation transitions in a coevolving nonlinear voter model*, Scientific Reports 7, 12864 (2017), https://www.nature.com/articles/s41598-017-13047-2 .
- V. Sood, S. Redner, *Voter Model on Heterogeneous Graphs*, Physical Review Letters 94, 178701 (2005), https://doi.org/10.1103/PhysRevLett.94.178701 .
