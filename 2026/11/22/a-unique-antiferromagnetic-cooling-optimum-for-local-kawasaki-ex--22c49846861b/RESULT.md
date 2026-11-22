# A unique antiferromagnetic cooling optimum for local Kawasaki exchange on every interacting Ising star sector

## Finding

For the conservative heat-bath exchange dynamics of the Ising model on a star, all nontrivial fixed-magnetization sectors with a nonzero hub-energy contrast exhibit a unique finite-temperature optimum in relaxation when the coupling is antiferromagnetic. The exact spectral gap of the **entire** chain is
\[
g_{n,k}(\beta)=\frac{S-\sqrt{S^2-4nab}}2,
\quad S=ka+(n-k+1)b,
\quad a=\frac{1}{1+e^{-2\beta J(2k-n-1)}},\quad b=1-a.
\]
At infinite temperature the gap is \(1/2\). For \(J<0\) it initially increases strictly, reaches a unique strict maximum above \(1/2\), then tends to zero as inverse temperature diverges. For \(J>0\) it strictly decreases. The only interior-sector exception is the symmetry-balanced filling \(2k=n+1\), for which the gap is constantly \(1/2\). The one-particle and one-vacancy sectors, unlike interacting fillings, have monotone antiferromagnetic gap enhancement and no finite-temperature maximum.

## Assumptions and scope

Let \(n\ge3\) be an integer, let the center be site \(0\) and the leaves be \(1,\ldots,n\), and fix exactly \(k\in\{1,\ldots,n\}\) spins \(+1\). The Ising Hamiltonian and reversible Gibbs weights are
\[
H(\sigma)=-J\sum_{i=1}^n\sigma_0\sigma_i,
\qquad \pi_{\beta,k}(\sigma)\propto e^{-\beta H(\sigma)}.
\]
For every hub-leaf edge whose endpoint spins disagree, exchange the spins at continuous-time rate \(1/(1+e^{\beta[H(\sigma')-H(\sigma)]})\); otherwise no move occurs. All edges have independent, unit-rate proposal clocks, without dividing rates by the number of edges. Set \(d=2k-n-1\), \(c=n-k+1\), \(a=(1+e^{-2\beta Jd})^{-1}\) and \(b=1-a\). At finite \(\beta\), \(0<a,b<1\). The spectral gap is the smallest strictly positive eigenvalue of the negative generator.

## Proof

**1. Two energy levels and the exact generator.** If the hub has spin \(-1\), exactly \(k\) leaves are \(+1\), and its energy is \(H_- =J(2k-n)\). If the hub has spin \(+1\), exactly \(k-1\) leaves are \(+1\), and its energy is \(H_+=-J(2k-n-2)\). Therefore \(H_+-H_-=-2Jd\). Every edge from a hub-minus configuration to a hub-plus configuration has rate \(a\), and every reverse edge rate \(b\). The former has \(k\) available exchanges, and the latter \(c=n-k+1\). The chain is irreducible and reversible because \(a/b=e^{2\beta Jd}=e^{-\beta(H_+-H_-)}\).

Index minus-hub configurations by the \(k\)-subsets of the leaf set, plus-hub configurations by the \((k-1)\)-subsets, and let \(B\) be the unsigned incidence matrix between them. Its entry is one exactly when the smaller subset lies inside the larger one. The generator is
\[
Q=\begin{pmatrix}-ka I&aB\\ bB^{\mathsf T}&-cb I\end{pmatrix}.
\]
The state-space blocks have sizes \(\binom nk\) and \(\binom n{k-1}\), so no cardinality reduction has been assumed.

**2. Entire spectrum and the gap.** For completeness, recall the Boolean-lattice incidence identity. Let \(U_r\) sum over adding an element to an \(r\)-subset and let \(D_{r+1}=U_r^{\mathsf T}\) sum over removing an element. Directly counting the add-then-remove and remove-then-add paths gives \(D_{r+1}U_r-U_{r-1}D_r=(n-2r)I\). On vectors arising by \(k-j\) successive raises from a level-\(j\) harmonic vector in \(\ker D_j\), this identity gives \(BB^{\mathsf T}\)-eigenvalue
\[
s_j^2=(k-j)(n-k+1-j)=(k-j)(c-j),
\quad 0\le j\le\min(k,n-k),
\]
with multiplicity \(\binom nj-\binom n{j-1}\) (with \(\binom n{-1}=0\)). The harmonic subspaces are orthogonal and span each Boolean-lattice level by dimension counting; this establishes all nonzero singular values, not merely a spectral bound. On each singular pair, \(-Q\) has the two eigenvalues
\[
\lambda_j^{\pm}=\frac{S\pm\sqrt{S^2-4ab[kc-(k-j)(c-j)]}}2.
\]
At \(j=0\), the pair is \(0,S\). Since \((k-j)(c-j)\) strictly decreases with \(j\) in the positive range, the lower eigenvalue increases with \(j\). All unpaired null-incidence vectors, if present, have eigenvalue \(ka\) or \(cb\), which are no smaller than \(\lambda_1^-\) by the two-by-two eigenvalue bound. For \(2\le k\le n-1\), the \(j=1\) pair exists and has \(kc-(k-1)(c-1)=k+c-1=n\). Consequently the **full-chain** gap is \(\lambda_1^-=(S-\sqrt{S^2-4nab})/2\). For \(k=1\) only the leaf-standard unpaired sector has eigenvalue \(a\), so the gap is \(a\); for \(k=n\) it is \(b\). These endpoint exceptions are essential.

**3. Strict temperature classification.** In interacting sectors, \(g=g(a)\) is the smaller solution of
\[
g(S-g)=na(1-a),\qquad S=c+(k-c)a=c+da.
\]
The discriminant stays strictly positive in \(0<a<1\), and differentiation gives
\[
g'(a)=\frac{n(1-2a)-dg(a)}{S-2g(a)}.
\]
At \(a=1/2\), \(S=(n+1)/2\) and \(g=1/2\), and \(g'(1/2)=-d/(n-1)\). If \(d>0\), \(g'(a)<0\) throughout \([1/2,1)\); if \(d<0\), \(g'(a)>0\) throughout \((0,1/2]\). To show there is exactly one maximum on the other half-interval, put \(F(a)=n(1-2a)-dg(a)\). For \(d>0\), \(F(0)>0\) and \(F(1/2)<0\). At every root of \(F\), \(g'=0\) and \(F'=-2n<0\); therefore only one zero is possible, and it gives a strict maximum. The \(d<0\) case is its reflection \((k,c,a)\mapsto(c,k,1-a)\). For antiferromagnetic \(J<0\) the logistic parameter moves away from \(1/2\) into exactly that maximizing half-interval as \(\beta\) increases; for ferromagnetic \(J>0\) it moves into the strictly decreasing half-interval. The interior maximum is thus unique, finite and exceeds \(1/2\). The optimum solves \(n(1-2a_*)=d g(a_*)\) and
\[
\beta_* = \frac{\left|\log(a_*/(1-a_*))\right|}{2|Jd|}.
\]
If \(d=0\), \(a=b=1/2\) independently of \(\beta,J\) and the gap is exactly \(1/2\). If \(d\ne0\), the antiferromagnetic gap tends to zero because \(ab\to0\) and \(S\) tends to a positive number. More precisely, \(g\sim(n/c)e^{-2\beta|Jd|}\) if \(d>0\), and \(g\sim(n/k)e^{-2\beta|Jd|}\) if \(d<0\). Its derivative at infinite temperature is \(g_{\beta}'(0)=-Jd^2/[2(n-1)]\). At \(k=1\) and \(k=n\), the exact endpoint gap \(a\) or \(b\) increases strictly from \(1/2\) toward \(1\) when \(J<0\), confirming the sharp dilute-sector distinction.

**4. An exact smallest nondegenerate example.** For \(n=4\), \(k=2\), \(J=-1\), the optimizing logistic parameter and gap are
\[
a_* =\frac{11-\sqrt2}{17},\qquad
\beta_*=\frac12\log\frac{11-\sqrt2}{6+\sqrt2},\qquad
g(\beta_*)=\frac{20-8\sqrt2}{17}\approx0.51095832>\frac12.
\]
The alternative root from squaring the stationary equation belongs to the upper spectral branch and is not an optimizer; the sign-of-derivative proof selects the stated value without ambiguity.

## Verification

The accompanying program `verify_star_kawasaki.py` constructs the generator independently from every fixed-size spin configuration, symmetrizes it with the exact reversible state weights, numerically diagonalizes the entire matrix, and compares its first nonzero eigenvalue against the analytic formula on 165 combinations of size, filling, and logistic parameter. It separately searches the analytic stationary derivative across interior sectors through size 16. Replaying it with Python, NumPy, and SciPy prints `EXACT_RATES_FULL_STATES_OK 165`. Floating-point tests corroborate the all-size proof, but do not replace its exact algebraic reasoning.

## Relationship to prior work

Grynberg's 2010 study analyzes Kawasaki spectral relaxation for one-dimensional spin chains, including different dynamical behavior of ferro- and antiferromagnetic exchange; it does not give the full-generator star spectrum or a unique finite-temperature antiferromagnetic maximizer. Caputo, Liggett, and Richthammer's 2009 proof of Aldous' spectral-gap conjecture addresses symmetric interchange, hence the uniform-rate \(\beta=0\) limit; it does not imply the temperature-dependent two-energy-level spectral formula. Recent bounded-degree Kawasaki mixing theory studies another graph regime and typically globally proposed swaps, whereas the present high-degree star has only local hub-leaf exchanges. The results are thus complementary rather than asserted consequences of those treatments. Novelty is claimed only for the combined sharp star-sector temperature classification, not for Boolean-lattice incidence eigenvalues.

## Limitations

The graph must be a star and the update must be continuous-time heat-bath **local** exchange with rate clocks per eligible hub-leaf edge. It is not a theorem about Glauber (nonconservative) dynamics, global Kawasaki proposals, arbitrary trees, total-variation mixing times, or infinite-volume phase transitions. The flat balanced sector is excluded from strict-maximizer statements; the endpoint sectors have different formulas. The independent computations cover finite sizes only. Historical priority beyond the examined literature is not independently certified.

## References

- M. D. Grynberg, *Revisiting Kawasaki dynamics in one dimension*, arXiv:1009.4511v1 (public 2010-09-23), https://arxiv.org/abs/1009.4511.
- P. Caputo, T. M. Liggett and T. Richthammer, *Proof of Aldous' spectral gap conjecture*, arXiv:0906.1238v1 (public 2009-06-06), https://arxiv.org/abs/0906.1238.
- D. Kuchukova et al., *Fast and Slow Mixing of the Kawasaki Dynamics on Bounded-Degree Graphs*, Random Structures & Algorithms (recent comparison), https://doi.org/10.1002/rsa.70038.
