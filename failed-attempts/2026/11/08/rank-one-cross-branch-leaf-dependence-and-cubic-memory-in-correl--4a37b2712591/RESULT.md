# Rank-one cross-branch leaf dependence and cubic memory in correlated recursive trees

## Finding

**Theorem (exact shared-history memory law).** Grow two rooted uniform-attachment trees from the common deterministic edge on vertices \(1,2\). Use the same uniformly sampled parent for every arrival through vertex \(t\), and independent uniform parents thereafter, for integers \(n\ge3\) and \(2\le t\le n\). In tree \(a\in\{1,2\}\), let \(L_s^{(a)}\) be the number of *terminal vertices*, meaning vertices of outdegree zero relative to the distinguished root \(1\), at size \(s\). For all integers \(t\le s,u\le n\),

\[
\operatorname{Cov}(L_s^{(1)},L_u^{(2)})=
\begin{cases}
0,&t=2,\\[3pt]
\displaystyle\frac{t(t-1)^2}{12(s-1)(u-1)},&t\ge3.
\end{cases}
\]

Thus the complete cross-branch, cross-time covariance kernel has rank one for \(t\ge3\). Every coordinatewise nondecreasing bounded measurable functional of the future terminal-count trajectory in one branch has nonnegative covariance with every such functional in the other branch.

In particular, for \(s=u=n\),

\[
\operatorname{Corr}(L_n^{(1)},L_n^{(2)})=
\begin{cases}
0,&t=2,\\[3pt]
\displaystyle\frac{t(t-1)^2}{n(n-1)^2},&t\ge3.
\end{cases}
\]

This is strictly increasing with \(t\) (from zero at the deterministic seed to one for completely shared growth). If \(t=t_n\) satisfies \(t_n/n\to\alpha\in[0,1]\), then the correlation tends to \(\alpha^3\), and

\[
\left(\frac{L_n^{(1)}-n/2}{\sqrt{n/12}},\,
      \frac{L_n^{(2)}-n/2}{\sqrt{n/12}}\right)
\xrightarrow{d}
\mathcal N_2\!\left(0,
\begin{pmatrix}1&\alpha^3\\\alpha^3&1\end{pmatrix}\right).
\]

The endpoint \(\alpha=1\) is allowed: its Gaussian limit is supported on the diagonal. This is an explicit dependence law for *rooted terminal counts*, not for all unrooted degree-one vertices. In particular, a root of undirected degree one is excluded.

## Assumptions and scope

All attachment choices at arrival \(j\ge3\) are uniform among the \(j-1\) existing vertices, independently between different arrival times. For arrivals \(3,\ldots,t\), the choices in the two trees coincide; for arrivals \(t+1,\ldots,n\), they are conditionally independent, given the shared tree at time \(t\). At time \(2\), the root \(1\) has one child and vertex \(2\) has none, so \(L_2=1\). The theorem concerns the exact labelled growth model and all integer parameters specified above; the Gaussian statement is an ordinary weak limit along any sequence with \(t_n/n\to\alpha\).

## Proof

**1. One-tree conditional dynamics and exact moments.** Given \(L_m=\ell\) terminal vertices at size \(m\ge2\), the new parent is terminal with probability \(\ell/m\). If \(B_{m+1}\) indicates that the new parent was terminal, then

\[
L_{m+1}=L_m+1-B_{m+1},\qquad
\mathbb P(B_{m+1}=1\mid\mathcal F_m)=L_m/m.
\]

Consequently, \(\mathbb E[L_{m+1}\mid\mathcal F_m]=(1-1/m)L_m+1\). Inducting from \(L_2=1\) gives \(\mathbb E L_m=m/2\) for every \(m\ge2\). Put \(Z_m=L_m-m/2\) and \(V_m=\operatorname{Var}(L_m)\). Total variance yields

\[
V_{m+1}=\left(1-\frac2m\right)V_m+\frac14,
\qquad V_2=0.
\]

Indeed, the conditional variance is \((L_m/m)(1-L_m/m)\), and its expectation is \(1/4-V_m/m^2\), exactly cancelling the extra \(V_m/m^2\) from the conditional-mean variance. It follows that \(V_3=1/4\) and \(V_m=m/12\) for \(m\ge3\), verified by induction. Iterating the centered conditional mean gives, for \(s\ge t\ge2\),

\[
\mathbb E[L_s-s/2\mid\mathcal F_t]
=\frac{t-1}{s-1}(L_t-t/2).
\tag{1}
\]

**2. Cross-branch covariance.** Given the complete common tree \(\mathcal F_t\), the terminal-count evolutions of the two branches are independent. Their conditional means depend on the common tree only through \(L_t\), by (1). The total-covariance identity therefore gives

\[
\operatorname{Cov}(L_s^{(1)},L_u^{(2)})
=\frac{(t-1)^2}{(s-1)(u-1)}\operatorname{Var}(L_t).
\]

Substituting \(V_2=0\) and \(V_t=t/12\) for \(t\ge3\) proves the exact kernel. The common marginal variance at size \(n\ge3\) is \(n/12\), hence the exact correlation. The numerator \(t(t-1)^2\) is strictly increasing for integer \(t\ge2\) (with a separately verified zero at \(t=2\)), and its value at \(t=n\) equals the denominator \(n(n-1)^2\).

**3. Positive association across branches.** For deterministic terminal counts \(k\le\ell\) at size \(t\), couple the two one-dimensional Markov terminal-count chains by using the same independent uniforms \(U_m\in[0,1]\), with transition \(x\mapsto x+1-\mathbf1\{U_m\le x/m\}\). If the current values obey \(k\le\ell\), then the updated values also do: when \(k<\ell\), their difference can decrease by at most one, and if \(k=\ell\), they update identically. Hence the entire future trajectories admit a monotone coupling. For any bounded coordinatewise nondecreasing trajectory functionals \(F\) and \(G\), their conditional expectations \(f(k)=\mathbb E[F\mid L_t=k]\) and \(g(k)=\mathbb E[G\mid L_t=k]\) are nondecreasing in \(k\). Given \(L_t\), the two branches are conditionally independent even as terminal-count trajectories, so

\[
\operatorname{Cov}(F,G)=\operatorname{Cov}(f(L_t),g(L_t))\ge0.
\]

The final inequality follows by taking an independent copy \(L_t'\) and writing twice the covariance as \(\mathbb E[(f(L_t)-f(L_t'))(g(L_t)-g(L_t'))]\ge0\). No unconditional within-branch association is asserted.

**4. Joint Gaussian limit.** Define \(p_m^{(a)}=L_m^{(a)}/m\), \(B_{m+1}^{(a)}\) as above, and the bounded martingale differences \(\eta_{m+1}^{(a)}=p_m^{(a)}-B_{m+1}^{(a)}\). Centering the recurrence gives

\[
Z_n^{(a)}=\frac{1}{n-1}\sum_{m=2}^{n-1}m\eta_{m+1}^{(a)}.
\tag{2}
\]

For \(m<t\), the paired martingale increments coincide; for \(m\ge t\), their conditional covariance is zero because attachment choices are independent given both current trees. Each conditional diagonal variance is \(p_m^{(a)}(1-p_m^{(a)})=1/4-(Z_m^{(a)}/m)^2\). The second-moment identity in step 1 gives \(\mathbb E[(Z_m^{(a)}/m)^2]=O(1/m)\), with zero at \(m=2\).

For the vector in the claim, its predictable quadratic-variation matrix, using (2) and scaling by \(12/n\), therefore converges in \(L^1\) entrywise to

\[
\lim_{n\to\infty}\frac{3}{n(n-1)^2}
\begin{pmatrix}
\sum_{m=2}^{n-1}m^2 & \sum_{m=2}^{t_n-1}m^2\\
\sum_{m=2}^{t_n-1}m^2 & \sum_{m=2}^{n-1}m^2
\end{pmatrix}
=
\begin{pmatrix}1&\alpha^3\\\alpha^3&1\end{pmatrix}.
\]

The \(L^1\) error is bounded by a constant times \(n^{-1}\) after summing \(m^2 O(m^{-1})\), divided by \(n(n-1)^2\). Each normalized increment has magnitude at most \(\sqrt{12/n}\), so the conditional Lindeberg condition holds. The bounded-increment martingale central limit theorem and Cramér–Wold establish the stated bivariate Gaussian convergence. This argument remains valid when the limiting covariance is singular at \(\alpha=1\). The cubic correlation limit follows separately from its exact finite expression. \(\square\)

## Verification

The standalone `verify.py` uses rational arithmetic, independently enumerates paired attachment histories for small instances, evaluates the pair distribution by a separate Markov-kernel method, checks conditional regression and the exact cross-time rank-one covariance, and tests all upper-tail indicator association inequalities in its stated finite ranges. Running `python3 verify.py` gives `VERIFY_OK_EXTENDED 5761 exact assertions`. Its finite tests do not certify the infinite-range or asymptotic arguments; those rely on the proof above.

## Relationship to prior work

Rácz and Sridhar introduced the shared-prefix correlated growing-graph model, including uniform-attachment trees, and studied detection and correlation-time estimation. Their original arXiv submission was publicly posted on 2020-04-28. The cross-branch terminal-count covariance kernel and its positivity/normal-limit classification are the narrower claims addressed here, rather than a new growth model. Janson had previously established marginal degree-count Gaussian laws and a within-tree functional limit theorem, including the outdegree-zero process. Its marginal Gaussian theorem and one-tree covariance structure are antecedents, not claimed as new. The cross-branch exact finite-time kernel and positive-association classification require using the forked two-tree conditional structure. Bäumler–Rácz–Ross–Sridhar (2026), Appendix A, already derives a paired leaf-count Gaussian limit under a different **stepwise, constant-probability attachment coupling**. That result is credited, and its correlation law is not the present fork-time cubic law. Their model is expressly distinguished from the 2020 shared-prefix model.

## Limitations

The exact formulas require uniform single-parent attachment, the specific deterministic two-vertex seed, and **rooted outdegree-zero counts**. The association claim concerns increasing functionals of terminal-count paths across different branches, not arbitrary tree statistics or all functionals within the same branch. The Gaussian convergence is weak convergence only; no total-variation limit or optimal detection threshold is asserted. Historical priority should be rechecked against any unlocated general result on Markovian forked-tree statistics and functional limit laws. Independent mathematical review has not been performed.

## References

1. M. Z. Rácz and A. Sridhar, *Correlated randomly growing graphs*, arXiv:2004.13537 (first posted 2020-04-28); https://arxiv.org/abs/2004.13537 .
2. S. Janson, *Asymptotic degree distribution in random recursive trees*, *Random Structures & Algorithms* 26 (2005), 69–83; DOI:10.1002/rsa.20046; lawful author manuscript: https://www2.math.uu.se/~svantejs/papers/sj155.pdf .
3. J. Bäumler, M. Z. Rácz, N. Ross and A. Sridhar, *Correlated uniform attachment trees*, arXiv:2606.02472 (2026), https://arxiv.org/abs/2606.02472 ; related but distinct continuously coupled model.
