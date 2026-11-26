# Non-self-averaging edge density at the full-duplication endpoint

## Finding

Motivated by recent analysis of random-cograph edge-density fluctuations (Chapuy, 2025), consider instead a sequential uniform-parent twin-insertion law. In the uniform-parent duplication model with **complete inheritance of the parent's neighborhood** and independent parent-link probability \(r\in[0,1]\), let \(E_n\) denote the number of edges on \(n\) vertices. The edge density \(F_n=2E_n/[n(n-1)]\), defined for \(n\ge2\), converges almost surely and in \(L^2\) to a random variable \(F_\infty\in[0,1]\) satisfying

\[
\mathbb E F_\infty=r,\qquad
\operatorname{Var}(F_\infty)=\frac{2r(1-r)}9.
\]

In fact, for **every** \(n\ge2\),

\[
\mathbb E F_n=r,\qquad
\operatorname{Var}(F_n)=\frac{2r(1-r)(n^2+n+3)}{9n(n-1)}.
\]

Consequently, the edge density has a nondegenerate random limit for each \(0<r<1\), despite having deterministic mean \(r\) at every finite order. The endpoint cases \(r=0\) and \(r=1\) have identically empty and complete graphs, respectively. The limits obey the complementary symmetry \(F_\infty(r)\overset{d}=1-F_\infty(1-r)\).

## Assumptions and scope

Start from a single isolated vertex at \(n=1\). Given a finite simple undirected graph \(G_n\), choose a parent \(U_n\) uniformly among its \(n\) vertices, independently of the past. Add vertex \(n+1\), join it to **every neighbor** of \(U_n\), and also join it to \(U_n\) with an independent \(\operatorname{Bernoulli}(r)\) variable \(\xi_{n+1}\), for fixed \(0\le r\le1\). All parent choices and parent-link coins are independent conditional on the current graph. No loops or multiple edges arise. The theorem is about the scalar edge-density process; it does not identify its full limiting distribution or a limiting graphon.

## Proof

Let \(d_v\) denote the degree of vertex \(v\) before a birth, and define the two-star count \(S_n=\sum_{v=1}^n\binom{d_v}{2}\). Write \(\mathcal F_n\) for the graph history. The increment is exactly

\[
\Delta_n=E_{n+1}-E_n=d_{U_n}+\xi_{n+1},
\qquad \sum_{v=1}^n d_v=2E_n,
\qquad \sum_{v=1}^n d_v^2=2S_n+2E_n.
\]

Uniform-parent averaging yields the three conditional identities

\[
\begin{aligned}
\mathbb E(\Delta_n\mid\mathcal F_n)&=\frac{2E_n}{n}+r,\\
\mathbb E(\Delta_n^2\mid\mathcal F_n)&=\frac{2S_n+(2+4r)E_n}{n}+r,\\
\mathbb E(S_{n+1}-S_n\mid\mathcal F_n)&=\frac{3S_n+(2+4r)E_n}{n}.
\end{aligned}
\]

For completeness, the change in \(S_n\) is the sum of (i) the existing neighbors' degree increments, \(\sum_{w\sim U_n}d_w\); (ii) the parent's extra degree increment, \(\xi_{n+1}d_{U_n}\); and (iii) the new vertex's two-stars, \(\binom{d_{U_n}+\xi_{n+1}}2\). Averaging these terms using the displayed degree identities gives the third formula. The second follows by squaring \(d_{U_n}+\xi_{n+1}\).

Set \(e_n=\mathbb E E_n\), \(s_n=\mathbb E S_n\), and \(q_n=\mathbb E E_n^2\). The conditional identities give the closed recurrences

\[
\begin{aligned}
e_{n+1}&=(1+2/n)e_n+r,\\
s_{n+1}&=(1+3/n)s_n+(2+4r)e_n/n,\\
q_{n+1}&=(1+4/n)q_n+2re_n+[2s_n+(2+4r)e_n]/n+r,
\end{aligned}
\]

all starting at zero at \(n=1\). Direct substitution and induction give, for all integers \(n\ge1\),

\[
\begin{aligned}
e_n&=\frac{rn(n-1)}2,\\
s_n&=\frac{r(1+2r)n(n-1)(n-2)}6,\\
q_n&=\frac{rn(n-1)}{36}
\bigl(7n^2r+2n^2-11nr+2n-6r+6\bigr).
\end{aligned}
\]

Subtracting \(e_n^2\) proves

\[
\operatorname{Var}(E_n)=\frac{r(1-r)n(n-1)(n^2+n+3)}{18},
\]

which immediately gives the asserted exact variance formula for \(F_n\).

To prove almost-sure convergence, put

\[
M_n=\frac{E_n-e_n}{n(n+1)},\qquad n\ge1.
\]

Since \(e_{n+1}=(1+2/n)e_n+r\) and \(\mathbb E(E_{n+1}\mid\mathcal F_n)=(1+2/n)E_n+r\), the identity \(1+2/n=(n+2)/n\) shows that \((M_n,\mathcal F_n)\) is a martingale. It is uniformly bounded, because \(0\le E_n\le\binom n2\) and \(0\le e_n\le\binom n2\). The bounded martingale convergence theorem therefore gives \(M_n\to M_\infty\) almost surely and in \(L^2\). For \(n\ge2\),

\[
F_n=r+\frac{2(n+1)}{n-1}M_n,
\]

so \(F_n\to F_\infty=r+2M_\infty\) almost surely and in \(L^2\). Passing to the limit in the exact first and second moments gives the stated mean and variance. Their strict positivity when \(0<r<1\) establishes nondegeneracy. Complementing every intermediate graph changes an inherited full neighbor set into the corresponding nonneighbor set and changes a parent-link coin \(\xi\) into \(1-\xi\); hence it couples parameter \(r\) to parameter \(1-r\), proving the stated symmetry.

## Verification

The accompanying standard-library script `verify.py` enumerates all finite graphs through four vertices and evaluates every one-step transition exactly, checks the derived conditional increments at rational parameters \(r\in\{0,1/3,2/5,1\}\), independently propagates the full finite process distribution through six vertices, and checks all three unconditional moment recurrences through order 39. It completes **1,940 exact rational assertions**. The finite assertions are consistency tests; the proof of the infinite limit is the bounded-martingale argument above. Reproduce with `python verify.py`.

## Relationship to prior work

Dey, Maitra, Manthripragada and Terlov (2026) study a closely matching uniform-parent duplication-divergence mechanism when each neighbor is copied with probability strictly between zero and one, focusing on degree and local limits. The complete-inheritance boundary is excluded from that parameter range. Hermann and Pfaffelhuber (2014) study the \(p=1\) endpoint of a **different** model that copies existing neighbors but does **not** independently link the new vertex to its parent; their analysis does not give the present immigrant-edge variance formula. These are substantive model distinctions rather than changes in notation.

The construction also belongs to the class of cographs generated by successive true/false twin insertions. However, Stufler (2021), Bassino et al. (2022), and Chapuy (2025) concern **uniformly sampled cographs**, a different sampling law. In particular, Chapuy reports that the edge density of the Brownian co-graphon at bias \(1/2\) has second moment \(17/60\), and hence variance \(1/30\). The present sequential model at \(r=1/2\) has limiting variance \(1/18\), ruling out equality of those edge-density laws. The new assertion is specifically the exact finite-order variance and almost-sure non-self-averaging for the growing parent-linked full-copy model, not generic martingale convergence or cograph edge-density randomness.

## Limitations

The theorem applies only to full neighborhood inheritance with fixed parent-link probability and a singleton seed. It does not give a density or fluctuation theorem at intermediate inheritance probabilities, a full characterization of the random limit law, or rates in distribution. Historical priority relative to less accessible older twin-insertion and duplication literature is not conclusively established. The limiting random variable is *not* asserted to be a beta law or a Brownian co-graphon edge density. The supporting exact enumeration stops at finite order and is not a proof of convergence.

## References

1. P. S. Dey, N. Maitra, J. M. Manthripragada, and G. Terlov, *Uniform duplication-divergence random graphs I: Degrees and Local Limits*, arXiv:2611.00123v1, November 2026. https://arxiv.org/abs/2611.00123
2. F. Hermann and P. Pfaffelhuber, *Large-scale behavior of the partial duplication random graph*, arXiv:1408.0904, 2014. https://arxiv.org/abs/1408.0904
3. B. Stufler, *Graphon convergence of random cographs*, Random Structures & Algorithms 59 (2021), 464–491. https://doi.org/10.1002/rsa.21002
4. F. Bassino, M. Bouvel, V. Féray, L. Gerin, M. Maazoun, and A. Pierrot, *Random cographs: Brownian graphon limit and asymptotic degree distribution*, Random Structures & Algorithms 60 (2022), 166–200. https://doi.org/10.1002/rsa.21033
5. G. Chapuy, *On the Edge-Density of the Brownian Co-Graphon and Common Ancestors of Pairs in the CRT*, Random Structures & Algorithms 66 (2025), e21281. https://doi.org/10.1002/rsa.21281
