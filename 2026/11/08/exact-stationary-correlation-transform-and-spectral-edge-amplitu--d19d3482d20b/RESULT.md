# Exact stationary correlation transform and spectral-edge amplitudes for the Pelikan random map

## Finding

Let \(X_{n+1}=2X_n\bmod 1\) with probability \(p\), and \(X_{n+1}=X_n/2\) with probability \(q=1-p\), with independent choices and \(1/2<p\le1\). Initialize \(X_0\) in the unique absolutely continuous stationary probability. Put
\[
\mu=\frac{2p-1}{3p-1},\qquad c=\frac{q}{2p},\qquad B=\frac{(p-1)(7p-3)}{4(3p-1)(5p-1)},
\]
\[
r(z)=\frac{1-\sqrt{1-4pqz^2}}{2pz},\qquad
\Phi(z;t)=\frac1{[1-pzt-pzr(z)][1-r(z)/2]},
\]
where \(r(0)=0\), the square root equals \(1\) at zero, and \(q=0\) is interpreted by continuation. Define \(C_n=\operatorname{Cov}(X_0,X_n)\), for every integer \(n\ge0\). Then the **entire stationary covariance sequence** has the exact algebraic generating function
\[
\boxed{\displaystyle
\sum_{n\ge0}C_nz^n=
\frac{\mu}{2}\Phi(z;1)+\frac1{12}\Phi(z;1/2)
+B\Phi(z;c)-\frac{\mu^2}{1-z}.}
\tag{1}
\]
The identity holds as a power series about zero; the pole at \(z=1\) on the right is removable. It also yields a finite binomial-sum expression at each lag, so it is an exact computation, not a commutative-map approximation.

The singularities give a **sharp three-regime stationary law**. For \(4/5<p\le1\),
\[
\boxed{\displaystyle
C_n\sim\frac{5p-4}{12(2p-1)}\left(\frac{4-3p}{2}\right)^n.}
\tag{2}
\]
At the spectral collision \(p=4/5\),
\[
\boxed{\displaystyle
C_n\sim\frac2{9\sqrt{2\pi}}\frac{(4/5)^n}{\sqrt n}.}
\tag{3}
\]
For each \(1/2<p<4/5\), let \(R=(2\sqrt{pq})^{-1}\), \(z_\sigma=\sigma R\), \(a_\sigma=4pz_\sigma-1\), \(b_\sigma(t)=1-2pz_\sigma t\), and assign weights \(w(1)=\mu/2\), \(w(1/2)=1/12\), \(w(c)=B\). Define the explicit finite quantities
\[
A_\sigma=\frac{8pz_\sigma}{\sqrt{2\pi}}
\sum_{t\in\{1,1/2,c\}}
 w(t)\frac{a_\sigma+b_\sigma(t)}{a_\sigma^2b_\sigma(t)^2},\qquad \sigma\in\{-1,+1\}.
\]
Here repeated values of \(t\), if any, are included with their indicated weights. Then
\[
\boxed{\displaystyle
C_n=(2\sqrt{pq})^n n^{-3/2}
\bigl[A_{+1}+(-1)^n A_{-1}+O_p(n^{-1})\bigr].}
\tag{4}
\]
Thus stationary initialization yields not only the two competing exponential scales but their exact polynomial exponents, amplitudes, and parity corrections.

## Assumptions and scope

The state space is \([0,1)\), and the sampling choices are independent of the state and of each other. For \(p>1/2\), use the absolutely continuous invariant density already established for this random map. Write \(I_k=(2^{-k-1},2^{-k})\), \(k\ge0\). Its density is constant on each \(I_k\), with value
\[
 a_k=\frac{2p-1}{p}\sum_{j=0}^{k}\left(\frac{2q}{p}\right)^j.
\tag{5}
\]
Equation (5) includes the limiting parameter \(p=2/3\) without a singular quotient. The dyadic endpoints have measure zero. The theorem concerns the annealed stationary **position** covariance, not the quenched covariance, the critical infinite-invariant-density system at \(p=1/2\), or a nonstationary uniform initial law. Asymptotics hold for each fixed indicated \(p\), not uniformly as \(p\) approaches a transition.

## Proof

**1. Conditional dyadic moment.** Set \(D(x)=2x\bmod1\) and \(J_m=\mathbb E[X_0D^m(X_0)]\). By (5), the mass of \(I_k\) is \(\pi_k=2^{-k-1}a_k\). Conditionally on \(X_0\in I_k\), write \(X_0=2^{-k-1}(1+U)\), where \(U\) is uniform on \([0,1)\). If \(k\ge m\), then \(D^m(X_0)=2^mX_0\); if \(k<m\), then \(D^m(X_0)=D^{m-k-1}(U)\). The elementary exact identities
\[
\mathbb E(1+U)^2=\frac73,\qquad
\mathbb E[(1+U)D^j(U)]=\frac34+\frac1{12\,2^j}
\quad(j\ge0)
\]
follow by decomposing a uniform binary expansion into its first \(j\) digits and independent tail. Therefore
\[
 J_m=\frac73 2^m\sum_{k=m}^\infty\pi_k4^{-k-1}
 +\sum_{k=0}^{m-1}\pi_k2^{-k-1}
 \left(\frac34+\frac{2^{-(m-k-1)}}{12}\right).
\tag{6}
\]
All series converge absolutely. Substitution of (5), exchanging nonnegative geometric sums, and cancelling terms yields the simple **three-mode identity**
\[
\boxed{\displaystyle J_m=\frac\mu2+\frac1{12}2^{-m}+Bc^m,\qquad m\ge0.}
\tag{7}
\]
For example, \(J_0=4(2p-1)/[3(5p-1)]\), and \(\mu=\mathbb E X_0=(2p-1)/(3p-1)\). Formula (7) is valid at \(p=2/3\) by (5) and at \(p=1\) by its limiting form; it has no hidden non-generic exclusions.

**2. An exact maximum-walk representation.** Let \(S_n\) be the random walk starting at zero that increases by one on a doubling step and decreases by one on a halving step; let \(M_n=\max_{0\le j\le n}S_j\). Since a halving inserts a leading zero binary digit and doubling deletes the leading digit, direct induction on the steps gives, outside the dyadic-null exceptional set,
\[
\boxed{\displaystyle X_n=2^{S_n-M_n}D^{M_n}(X_0).}
\tag{8}
\]
Choices are independent of \(X_0\); hence by (7),
\[
\mathbb E[X_0X_n]=\frac\mu2 K_n(1)+\frac1{12}K_n(1/2)+B K_n(c),
\quad K_n(t)=\mathbb E[2^{S_n-M_n}t^{M_n}].
\tag{9}
\]

**3. Resolvent.** Let \(H_n=M_n-S_n\ge0\) and \(u_n(h)=\mathbb E[t^{M_n}\mathbf1_{\{H_n=h\}}]\). The transition is \(h\mapsto h+1\) with probability \(q\), \(h\mapsto h-1\) with probability \(p\) when \(h>0\); at \(h=0\) a doubling stays at zero and multiplies the weight by \(t\). Thus the generating functions \(U_h(z)=\sum_n u_n(h)z^n\) obey
\[
 U_0=1+zptU_0+zpU_1,\qquad
 U_h=zqU_{h-1}+zpU_{h+1}\quad(h\ge1).
\]
Solving the second-order recurrence as a formal series gives \(U_h=U_0r(z)^h\), with \(r= z(q+pr^2)\) and \(r(0)=0\), and \(U_0=[1-pzt-pzr]^{-1}\). Summing \(K_n(t)=\sum_{h\ge0}2^{-h}u_n(h)\) over time proves \(\sum_nK_n(t)z^n=\Phi(z;t)\). Subtracting the stationary product of means in (9) gives (1). At \(p=1\), (1) reduces to \(C_n=2^{-n}/12\).

**4. Singularities and asymptotic coefficients.** For \(q>0\), set \(w=\sqrt{1-4pqz^2}\) and rewrite
\[
\Phi(z;t)=\frac{8pz}{[4pz-1+w][1+w-2pzt]}.
\tag{10}
\]
The square-root branchpoints are \(\pm R\), \(R=(2\sqrt{pq})^{-1}\). The factor with \(t=1\) has its sole interior physical pole at \(z=1\); its residue contributes \(\mu^2/(1-z)\) and cancels exactly in (1). The \(t=c\) factor has no physical pole inside \(|z|\le R\). For \(t=1/2\), the additional simple pole \(z_*=2/(4-3p)\) is on the physical sheet exactly when \(p>4/5\); it then lies strictly inside \(R\). Its residue in (1) is \((5p-4)/[12(2p-1)]\), proving (2). At \(p=4/5\), \(z_*=R=5/4\), and (10) gives
\[
\Phi(z;1/2)=\frac{8}{3\sqrt2}(1-z/R)^{-1/2}+O(1)
\quad\text{near }z=R.
\]
The coefficient of this leading term, weighted by \(1/12\), gives (3); the branchpoint at \(-R\) contributes only at relative order \(n^{-1}\).

For \(1/2<p<4/5\), none of the three remaining terms has a pole before the two branchpoints. At \(z=z_\sigma\), expanding (10) in \(w\) shows that the coefficient of \(w\) is
\[
-8pz_\sigma\sum_{t\in\{1,1/2,c\}}w(t)
\frac{a_\sigma+b_\sigma(t)}{a_\sigma^2 b_\sigma(t)^2}.
\]
The binomial-coefficient asymptotics of \(\sqrt{1-z^2/R^2}\) at \(z=\pm R\) give (4), including the parity term. The next nonanalytic contribution is cubic in \(w\) and gives the stated \(O_p(n^{-1})\) correction in brackets. Branch choices are fixed by \(w(0)=1\); the algebraic denominators in (10) have no additional singularities of modulus \(\le R\) on this sheet. This proves the claim.

## Verification

The included `verify.py` performs exact rational reconstruction using two independent finite-lag methods: the reflection-principle distribution of \((M_n,S_n)\) and formal-series inversion of the resolvent. It also checks (7) by direct dyadic conditioning, compares the first two lags with the published exact small-lag formulas, and tests the two new critical/pole asymptotic amplitudes at longer lags. Run with `python3 verify.py`; Python's standard library suffices. Finite numerical and symbolic tests support, but do not replace, the proof above.

## Relationship to prior work

Yan, Majumdar, Ruffo, Sato, Beck and Klages give the Pelikan map, its piecewise invariant density, and exact **stationary** correlations only at lags one, two, and three; they resort to a noncommutative-to-commutative approximation for longer lags (their Section III and Appendix D–E). Monthus later derives an exact binary-stack walk for arbitrary starting strings and a time-correlation transform for **Lebesgue-uniform**, rather than stationary, initial data (Section VI E, equations (197)–(211)); that paper also identifies the \(4/5\) exponential-scale crossover. The present theorem applies the exact walk to the stationary two-point observable, evaluates its nonuniform initial-bit covariance into the three explicit modes (7), and obtains a compact **stationary covariance** transform and its sharp polynomial exponents and exact amplitudes. The general binary-string representation and the existence of the crossover are credited, not claimed as new.

A previously known exact stationary **sum of all covariances** does not determine the individual lags or these singular coefficients; the present transform contains strictly more lag-resolved information. A formal specialization of the universal binary-stack machinery could also produce (1), so publication priority should be checked by an independent specialist. No exact stationary expression or these amplitudes was found in the inspected primary sources.

## Limitations

This result is a self-review, not an independent audit or published priority certification. The critical infinite-measure case \(p=1/2\), quenched correlations, random-parameter sampling, and uniformity in the two-parameter near-crossover window are not asserted. The displayed asymptotics are fixed-parameter laws. The possibility of equivalent unindexed stationary correlation formulas and the derivability of the elementary transform from earlier universal-bit methods are acknowledged originality risks. No statement about a central limit theorem is made.

## References

1. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck and R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269 (first public version 2023-08-18); *Chaos* **34**, 023128 (2024), doi:10.1063/5.0176310. Full text: https://webspace.maths.qmul.ac.uk/r.klages/papers/rds_chaos.pdf .
2. C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, arXiv:2409.19999 (first public version 2024-09-30); *J. Stat. Mech.* (2025) 013212. Full preprint: https://arxiv.org/pdf/2409.19999 .
3. S. Pelikan, *Invariant densities for random maps of the interval*, *Transactions of the American Mathematical Society* **281** (1984), 813–825; doi:10.1090/S0002-9947-1984-0722776-1 (invariant-density antecedent, referenced by 1 and 2).
