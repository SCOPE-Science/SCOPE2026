# First-order kinetic speedup of dimer jamming on matching-deleted bipartite networks

## Finding

For each integer \(n\ge2\), let \(G_n\) be the bipartite graph with left and right vertices \(L_1,\ldots,L_n\) and \(R_1,\ldots,R_n\), containing every edge \(L_iR_j\) except \(i=j\). Each present edge independently attempts to deposit a dimer at rate one, and a deposition succeeds precisely when both endpoint sites are unoccupied. Let \(T_n\) be the time of the **last successful deposition**, with \(T_n=0\) if no deposition is possible initially.

Write \(H_n^{(2)}=\sum_{j=1}^n j^{-2}\), the expected last-deposition time of the same model on the complete bipartite graph \(K_{n,n}\). Then
\[
\boxed{\mathbb E[T_n]=H_n^{(2)}-\frac1n+O\!\left(\frac{\log n}{n^2}\right).}
\]
In particular, the removal of a perfect matching of adsorption channels **speeds up** expected saturation by \(1/n\) to first order, although it reduces the instantaneous number of available deposition channels. The full finite-size distribution is exactly specified by the following rational Laplace-transform recurrence.

Let \(\mathcal L_{m,k}(s)\) be the transform of the remaining deposition time given \(m\) unoccupied sites in each part, of which \(k\) labels are present in both parts. For \(s\ge0\),
\[
\mathcal L_{1,0}(s)=\frac1{1+s},\quad \mathcal L_{1,1}(s)=1,
\]
and, for \(m\ge2\),
\[
\mathcal L_{m,k}(s)=\frac{k(k-1)\mathcal L_{m-1,k-2}(s)+2k(m-k)\mathcal L_{m-1,k-1}(s)+(m-k)^2\mathcal L_{m-1,k}(s)}{m^2-k+s}.
\]
Terms with a zero coefficient are omitted, including any formally out-of-range subscripts. Thus \(\mathbb E[e^{-sT_n}]=\mathcal L_{n,n}(s)\) and every finite-size moment exists and can be computed exactly. For example,
\[
\mathbb E[T_2]=\frac32,\qquad \mathbb E[T_3]=\frac76,\qquad \mathbb E[T_4]=\frac{115}{84}.
\]

## Assumptions and scope

All graph vertices and edges are labeled; dimers are irreversible and have hard-core site exclusion. The independent attempt clocks are homogeneous rate-one Poisson processes **per edge**. Failed attempts do not modify the configuration. Time is measured in inverse single-edge attempt-rate units. The last-success convention excludes the infinite subsequent sequence of rejected attempts. No assertion is made for nonuniform edge rates or for other graph families.

The result concerns the finite continuous-time process and its dense-graph limit as \(n\to\infty\). Every finite \(n\ge2\) is included. The leading kinetic statement is about a mean and is not an almost-sure or stochastic-order comparison.

## Proof

**1. Closed Markov reduction and transform.** At a stage with \(m\) unoccupied vertices in each part, write the corresponding surviving index sets as \(A,B\subseteq\{1,\ldots,n\}\), with \(|A|=|B|=m\) and \(k=|A\cap B|\). The number of currently allowed edges is \(\lambda_{m,k}=m^2-k\). When \(m\ge2\), this is strictly positive. By independent exponential clocks, the waiting time to the next successful deposition is \(\operatorname{Exp}(\lambda_{m,k})\) and the next edge is uniformly distributed among the currently allowed edges, independently of the waiting time.

Exactly \(k(k-1)\) allowed edges join two distinct common-label vertices and produce overlap \(k-2\); exactly \(2k(m-k)\) join a common-label and a single-side vertex and produce overlap \(k-1\); and exactly \((m-k)^2\) join two single-side vertices and preserve overlap \(k\). The displayed transform recurrence follows by conditioning. With one site per part, the final waiting time is \(\operatorname{Exp}(1)\) for overlap zero and is identically zero for overlap one. This establishes the whole finite-size distribution.

**2. An occupation-count drift.** Let \(K_m\) denote the overlap along the embedded jump chain, which starts with \(K_n=n\) and has one state at each integer \(m\) down to one. Define \(F_m=2K_m/[m(m+1)]\), and \((k)_2=k(k-1)\). The preceding edge counts give
\[
\mathbb E[K_{m-1}\mid K_m=k]
=k-\frac{2k(m-1)}{m^2-k},
\]
so elementary algebra yields the exact nonnegative drift
\[
F_m-\mathbb E[F_{m-1}\mid K_m=k]
=\frac{4(k)_2}{m(m^2-k)(m-1)(m+1)}.
\]
The terminal event \(K_1=1\) means the last unoccupied opposite-side pair has the same excluded label and no final deposition occurs. Put \(p_n=\Pr(K_1=1)\), and for \(1\le m\le n\) define
\[
\varepsilon_m=\frac{2}{n+1}-\mathbb E[F_m].
\]
It follows that \(p_n=2/(n+1)-\varepsilon_1\), that \(\varepsilon_n=0\), and that \(0\le\varepsilon_m\le\varepsilon_1\).

**3. Second-factorial-moment control.** Given \(K_j=k\ge2\), any ordered pair of distinct common labels remains common after one deposition precisely when the selected edge avoids the two corresponding left and right vertices. Hence
\[
\mathbb E[(K_{j-1})_2\mid K_j=k]
=(k)_2\frac{(j-2)^2-(k-2)}{j^2-k}
\le (k)_2\frac{(j-2)^2}{j^2-2}.
\]
The inequality follows because the displayed ratio decreases in \(k\) for \(j\ge2\). It is trivial for \(k=0,1\). Iterating from \(K_n=n\) and factoring the products gives, for \(2\le m\le n\),
\[
\mathbb E[(K_m)_2]\le\frac{C\,m^2(m-1)^2}{n(n-1)},\quad
C=\prod_{j=3}^{\infty}\left(1-\frac{2}{j^2}\right)^{-1}<3.
\]
The infinite product converges. For the explicit bound, \(\log C\le\sum_{j=3}^{\infty}2/(j^2-2)<1\), as follows by treating \(j=3,4,5\) separately and bounding the remaining sum by \(2(1/25+1/5)\); hence \(C<e<3\).

Using \(j^2-K_j\ge j(j-1)\) in the drift formula now shows
\[
0\le\varepsilon_m\le\frac{4C}{n(n-1)}\sum_{j=m+1}^n\frac1{j+1},\quad
0\le\varepsilon_1\le\frac{4C}{n(n-1)}\left(H_{n+1}-\frac32\right),
\]
where \(H_r=\sum_{j=1}^r1/j\).

**4. The first-order time correction.** Conditional on the jump-chain states, the mean waiting time at stage \(m\ge2\) is \(1/(m^2-K_m)\). The final step at \(m=1\) contributes one unit of conditional mean exactly when \(K_1=0\). Therefore
\[
\mathbb E[T_n]-H_n^{(2)}
=\sum_{m=2}^n\mathbb E\!\left[\frac1{m^2-K_m}-\frac1{m^2}\right]-p_n.
\]
For each \(m\ge2\), the exact decomposition
\[
\frac1{m^2-k}-\frac1{m^2}
=\frac{k}{m^2(m^2-1)}+
\frac{(k)_2}{m^2(m^2-1)(m^2-k)}
\]
separates a first-moment term from a nonnegative second-order term. Define
\[
R_n=\sum_{m=2}^n\mathbb E\!\left[
\frac{(K_m)_2}{m^2(m^2-1)(m^2-K_m)}\right].
\]
The preceding moment estimate implies
\[
0\le R_n\le\frac{C}{n(n-1)}\sum_{m=2}^{\infty}\frac1{m^2}
\le\frac{C\pi^2}{6n(n-1)}.
\]
Since \(\mathbb E[K_m]=\tfrac12m(m+1)(2/(n+1)-\varepsilon_m)\), and \(\sum_{m=2}^{n}1/[m(m-1)]=1-1/n\), substitution gives the **exact identity**
\[
\mathbb E[T_n]-H_n^{(2)}+\frac1n
=\varepsilon_1-\frac12\sum_{m=2}^n\frac{\varepsilon_m}{m(m-1)}+R_n.
\]
Consequently, for every \(n\ge2\),
\[
\boxed{\left|\mathbb E[T_n]-H_n^{(2)}+\frac1n\right|
\le\frac{C}{n(n-1)}\left[6\left(H_{n+1}-\frac32\right)+\frac{\pi^2}{6}\right].}
\]
This proves the asserted asymptotic with its coefficient and a completely explicit error bound. No finite-size extrapolation is used to obtain the infinite-family conclusion.

## Verification

The included standard-library program `verify_kinetics.py` computes the mean and rational Laplace transforms using the displayed compressed recurrence, and independently computes the same quantities using a recursion on the two labeled surviving-vertex masks. Agreement was exact for all \(2\le n\le7\) and at transform arguments \(s=1/2\) and \(s=2\). It also checked the exact mean values displayed above and independently evaluated the large-size coefficient numerically through \(n=2000\); the last estimate was \(-0.990828319615\) for \(n(\mathbb E[T_n]-H_n^{(2)})\). The first-order limit is proved above, not inferred from these computations.

Reproduction: with Python 3 and no third-party packages, execute `python3 verify_kinetics.py`. The arithmetic tests use `fractions.Fraction`; only the separately identified large-size illustration uses floating-point arithmetic.

## Relationship to prior work

The irreversible dimer adsorption and jamming framework is classical; see Cadilhe, Araújo and Privman (first publicly posted 2006), and the earlier graph adsorption paper of Pippenger (1989). Dyer and Frieze (1991) formalized uniform-edge randomized greedy matching. Bennett and Bohman (2012) analyze random greedy matching for regular hypergraphs using concentration methods. Arnosti (2021) compares matching sizes among random-edge and other greedy methods. These sources provide the process and relevant context, but their inspected accessible portions do not give the crown-network **Poisson last-success-time transform** or its explicit first-order comparison with the complete bipartite clock. The graph's finite matching-size defect law can be studied separately; the present statement concerns the clock, not a new matching-size law.

## Limitations

The effect is an asymptotic mean-time correction for homogeneous unit-rate per-edge Poisson trials; no result about stochastic domination, nonuniform rates, or longer spatially structured missing-edge sets is asserted. For \(n=2\), the expected time exceeds the full-bipartite baseline; the negative correction is asymptotic, not claimed to hold uniformly at small sizes. Historical priority remains provisional, particularly because not every older relevant full manuscript was accessible for complete comparison. This is a self-review, not an independent scientific audit.

## References

1. A. Cadilhe, N. A. M. Araújo and V. Privman, *Random Sequential Adsorption: From Continuum to Lattice and Pre-Patterned Substrates*, arXiv:cond-mat/0611413, first posted 2006-11-15. https://arxiv.org/abs/cond-mat/0611413.
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM J. Discrete Math. 2 (1989), 393–401. https://doi.org/10.1137/0402034.
3. M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms 2 (1991), 29–45. https://doi.org/10.1002/rsa.3240020104.
4. P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, arXiv:1210.3581, first posted 2012-10-12. https://arxiv.org/abs/1210.3581.
5. N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, Stochastic Systems 12 (2022), 133–150, first published online 2021-11-02. https://doi.org/10.1287/stsy.2021.0082.
