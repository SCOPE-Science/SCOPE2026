# An exact Jordan second-quantization horn and its coupled sectorial–Schatten critical crossover

## Finding

Fix real parameters \(a>0\) and \(0<c\le 2a\). Let \(N=\begin{pmatrix}0&1\\0&0\end{pmatrix}\), \(J=aI-cN\), and let \(\mathscr F_s(\mathbb C^2)=\bigoplus_{n\ge0}\operatorname{Sym}^n(\mathbb C^2)\) denote the bosonic symmetric Fock space, including the one-dimensional vacuum sector. On the finite-particle domain define
\[
S(z)=\bigoplus_{n\ge0}\bigl[e^{-zJ}\bigr]^{\odot n},\qquad z=t+is\in\mathbb C.
\]
The zeroth summand is the scalar identity. The exact set on which this densely defined family admits a bounded extension is
\[
\boxed{\mathcal B=\{t+is:\ t\ge0,\ c\sqrt{t^2+s^2}\le 2\sinh(at)\}.}
\]
The extension has operator norm exactly one at every point of \(\mathcal B\); outside \(\mathcal B\) it is unbounded. It is holomorphic, compact, and in every Schatten class \(\mathcal S_p\) (\(p>0\)) precisely on the interior \(\mathcal B^\circ\). On the boundary it is bounded but noncompact and not in any finite Schatten class. The restriction to nonnegative real time is a strongly continuous contraction semigroup.

Set
\[
q(z)=\exp\!\left[-at+\operatorname{arsinh}\!\left(\frac{c|z|}{2}\right)\right],\quad
r(z)=\exp\!\left[-at-\operatorname{arsinh}\!\left(\frac{c|z|}{2}\right)\right].
\]
On \(\mathcal B^\circ\), the complete singular-value multiset is \(\{q(z)^j r(z)^k:j,k\in\mathbb N_0\}\), with each ordered pair counted once, so for every \(p>0\)
\[
\boxed{\|S(z)\|_{\mathcal S_p}^p=\frac1{(1-q(z)^p)(1-r(z)^p)}.}
\]
The **sharp maximal centered sectorial half-angle** is \(\boxed{\theta_*=\arccos(c/(2a))}\); at \(c=2a\) the real-time semigroup is immediately trace class but admits no bounded holomorphic continuation to any nonzero sector at the origin.

The boundary half-width at each real part \(t>0\) is exactly
\[
\boxed{b(t,c)=\sqrt{\left(\frac{2\sinh(at)}c\right)^2-t^2},}\qquad |s|\le b(t,c).
\]
For fixed \(0<c<2a\), the boundary opens linearly, and for each fixed \(p>0\)
\[
\frac{b(t,c)}t\longrightarrow\sqrt{\frac{4a^2}{c^2}-1},\qquad
\|S(t)\|_{\mathcal S_p}^p\sim\frac1{p^2(a^2-c^2/4)t^2}.
\]
At the dissipativity threshold \(c=2a\), **both orders jump**:
\[
\boxed{b(t,2a)\sim\frac a{\sqrt3}t^2,\qquad
\|S(t)\|_{\mathcal S_p}^p\sim\frac3{p^2a^4t^4}.}
\]
Although its singular-value trace norm changes order, its algebraic operator trace is shear-independent:
\[
\boxed{\operatorname{Tr}S(t)=(1-e^{-at})^{-2}\sim a^{-2}t^{-2},\qquad t\downarrow0.}
\]
Thus the critical trace-norm order \(t^{-4}\) is a purely nonnormal amplification, invisible to the eigenvalue multiplicities.

More sharply, put \(c=2a(1-\delta)\) and let \(t\downarrow0\) while \(\delta=\delta(t)\ge0\) tends to zero. Uniformly along all such joint limits,
\[
\boxed{\frac{b(t,2a(1-\delta))}{t\sqrt{2\delta+a^2t^2/3}}\to1,\qquad
2p^2a^2t^2(\delta+a^2t^2/6)\|S(t)\|_{\mathcal S_p}^p\to1.}
\]
The same scaling \(\delta\asymp t^2\) governs both the complex-time cusp and the Schatten blow-up transition. For \(c>0\) this boundedness set is not invariant under any nonzero pure-imaginary translation.

## Assumptions and scope

All Hilbert spaces are complex, with the standard Hilbert tensor-product norm on symmetric powers. The coefficients satisfy \(a>0\) and \(0<c\le2a\); the endpoint \(c=2a\) is included. The word "Schatten" includes quasi-normed classes \(0<p<1\). The boundedness and analytic continuation statements refer to the canonical finite-particle expression above and its unique bounded extension. A boundary point is understood relative to the complex plane, not just the right half-plane. The finite-dimensional drift is not claimed to be self-adjoint or normal.

## Proof

**1. Exact one-particle singular values.** Nilpotence \(N^2=0\) gives \(Q(z):=e^{-zJ}=e^{-az}(I+czN)\). The matrix \(I+wN\) has determinant one, and its positive singular values are \(\sqrt{1+|w|^2/4}\pm |w|/2\), since the sum of their squares is \(2+|w|^2\). These equal \(e^{\pm\operatorname{arsinh}(|w|/2)}\). Thus \(Q(z)\) has singular values \(q(z)\ge r(z)>0\), with \(q(z)r(z)=e^{-2at}\). In particular,
\[
q(z)\le1\iff at\ge\operatorname{arsinh}(c|z|/2)
\iff t\ge0\ \text{and}\ c|z|\le2\sinh(at).
\]

**2. Boundedness and singular spectrum on Fock space.** The operator norm of \(Q(z)^{\odot n}\) is exactly \(q(z)^n\): the upper bound follows from tensor norms and equality is attained by the symmetric tensor power of a top singular vector. Hence the direct sum is bounded iff \(q(z)\le1\), and its norm is then one because of the vacuum. If \(q(z)>1\), unit vectors in the \(n\)-particle sectors are amplified by \(q(z)^n\to\infty\). A singular-value decomposition of \(Q(z)\) induces unitary singular-value decompositions on every symmetric power. The singular values on \(\operatorname{Sym}^n(\mathbb C^2)\) are exactly \(q(z)^j r(z)^{n-j}\), \(0\le j\le n\). Summing their \(p\)th powers for every \(n\) produces the asserted two-geometric-series product when \(q(z)<1\), and divergence when \(q(z)=1\). At \(q=1\), one singular vector from each particle number has singular value one, proving noncompactness. At \(q<1\), finite-particle truncations converge in operator norm since \(q^n\to0\), proving compactness. The finite-particle summands are entire functions of \(z\); on compact subsets of \(\{q<1\}\) their norm series (and derivative series, by Cauchy's formula on slightly larger compact neighborhoods) converge uniformly. Therefore the extension is holomorphic precisely throughout \(\mathcal B^\circ=\{q<1\}\). There is no bounded extension beyond this region from the dense finite-particle formula. This also excludes any larger open domain of bounded holomorphic continuation containing it.

**3. Real-time semigroup and sharp sector.** For every \(t>0\), \(ct\le2at<2\sinh(at)\), so \(q(t)<1\). The direct sum semigroup law follows from \(Q(t+u)=Q(t)Q(u)\). Strong continuity at zero holds first on finite-particle vectors and then on all Fock vectors using uniform operator-norm contractivity. Along any ray \(z=\rho e^{i\theta}\) with \(|\theta|<\arccos(c/(2a))\), we have \(c|z|<2a\operatorname{Re}z<2\sinh(a\operatorname{Re}z)\), hence bounded holomorphy and norm one. If a strictly larger sector is chosen, it includes a ray with \(c>2a\cos\theta\); on that ray the strict reverse inequality holds for all sufficiently small \(\rho>0\), because \(2\sinh(a\rho\cos\theta)=2a\rho\cos\theta+O(\rho^3)\). For \(c=2a\), every nonzero ray angle fails near zero. This proves sharpness.

The eigenvalues of \(Q(t)\) are both \(e^{-at}\), so every \(n\)-particle block has trace \((n+1)e^{-ant}\). Absolute summability follows from \(q(t)<1\); therefore \(\operatorname{Tr}S(t)=\sum_{n\ge0}(n+1)e^{-ant}=(1-e^{-at})^{-2}\), independent of the Jordan shear.

**4. Exact horn geometry and nonperiodicity.** Solving \(c\sqrt{t^2+s^2}\le2\sinh(at)\) for \(|s|\) gives the boundary half-width \(b(t,c)\). For every \(c>0\), no pure-imaginary nonzero \(i\tau\) belongs to \(\mathcal B\), whereas \(0\in\mathcal B\). Therefore \(\mathcal B+i\tau=\mathcal B\) cannot hold for \(\tau\ne0\).

**5. Fixed-parameter asymptotics.** For \(0<c<2a\), Taylor expansion gives \(q(t)=1-(a-c/2)t+O(t^2)\), \(r(t)=1-(a+c/2)t+O(t^2)\), and \(b(t,c)=t\sqrt{4a^2/c^2-1}+O(t^3)\). Consequently the exact Schatten product yields the claimed \(t^{-2}\) law. For \(c=2a\), expansion of \(\operatorname{arsinh}(at)=at-(at)^3/6+O(t^5)\) gives \(1-q(t)\sim a^3t^3/6\), \(1-r(t)\sim2at\); inserting into the product yields \(3/(p^2a^4t^4)\). Expanding \(\sinh(at)/(at)\) in the half-width gives \(b(t,2a)\sim at^2/\sqrt3\).

**6. Uniform joint crossover.** With \(c=2a(1-\delta)\), \(0\le\delta\to0\), the exact width satisfies
\[
\left(\frac{b(t,c)}t\right)^2
=\frac{\left(\sinh(at)/(at)\right)^2}{(1-\delta)^2}-1
=2\delta+\frac{a^2t^2}{3}+O(\delta^2+\delta t^2+t^4).
\]
The error divided by \(\delta+t^2\) tends uniformly to zero, proving the first ratio limit even when \(\delta=0\). Similarly,
\[
-\log q(t)=a\delta t+\frac{a^3(1-\delta)^3t^3}{6}+O(t^5),\qquad
-\log r(t)=a(2-\delta)t-\frac{a^3(1-\delta)^3t^3}{6}+O(t^5).
\]
Thus \(1-q(t)^p=p[a\delta t+a^3t^3/6](1+o(1))\) and \(1-r(t)^p=2pat(1+o(1))\), with relative errors uniform over joint paths because \(\delta t+t^3\) is never smaller than a fixed multiple of \(t^3\). Multiplication proves the second ratio limit for each fixed \(p>0\).

## Verification

A standalone executable `check_jordan_horn.py` separately computes singular values by numerical SVD, checks exact formulae against the predicted horn, tests the small-time laws in both regimes, and samples the coupled crossover including the critical endpoint. On the packaged version it reports `JORDAN_FOCK_HORN_DIAGNOSTIC_OK 1852`. These numerical tests are finite diagnostics, **not** a proof of any uniform or infinite-particle assertion; the mathematical proof above covers those assertions. The checker requires Python with NumPy and runs as `python check_jordan_horn.py` from the extracted package directory.

## Relationship to prior work

Perelmuter's 2026 paper studies imaginary-time covariance and periodic complex-time boundedness, including the known quadratic cusp of a different hypoelliptic operator. Araki, Sinha and Sunder (1995) give general boundedness and Schatten criteria for second quantization; their criterion and product formula are **used and credited**, not asserted as new. Li's 2026 Gaussian quantum-semigroup paper develops real-time compactness and trace formulas. The present exact **Jordan shear horn**, its loss of imaginary periods and sharp sectorial threshold, and its **joint horn-width/Schatten crossover at the dissipativity edge** are the specific assessed results. A quadratic cusp or second-quantization criterion in isolation is not being claimed as original.

## Limitations

The model is a two-mode upper-Jordan one-particle generator and its symmetric bosonic Fock amplification, not an arbitrary Gaussian Ornstein–Uhlenbeck realization on \(L^p\) or a general nonnormal drift. The exact Schatten formula assumes the canonical Fock Hilbert norm. The stated crossover is for fixed \(a,p>0\), with \(\delta\to0\) and \(t\downarrow0\). General second-quantization results imply significant parts of the argument; the claim of novelty is restricted to the combined sharp phase diagram and critical matching laws. An unlocated older application of those general results to precisely this Jordan family remains a bibliographic risk. No independent audit is asserted here.

## References

1. M. A. Perelmuter, *Semigroups with periodic complex-time boundedness and holomorphy regions*, arXiv:2611.15455v1 (first posted 11 November 2026), https://arxiv.org/html/2611.15455v1 .
2. H. Araki, K. B. Sinha and V. S. Sunder, *On boundedness and \(\|\cdot\|_p\) continuity of second quantisation* (1995), https://ems.press/content/serial-article-files/40585 .
3. Z. Li, *Second quantization and compactness of induced Gaussian quantum Markov semigroups*, arXiv:2610.13358 (first posted 9 October 2026), https://arxiv.org/abs/2610.13358 .
