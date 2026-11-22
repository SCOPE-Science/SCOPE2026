# The persistent-corner passage law and its signed finite-dimension correction

## Finding

Fix \(a>0\). For every integer \(d>2a\), let \(X^{(d)}\) be the discrete-time Markov chain on the binary cube \(\{0,1\}^{d}\) in which, at every step, **each coordinate independently flips** with probability \(q_d=a/d\). Start the chain in its stationary uniform distribution \(\pi_d\), and define the first entrance time into the all-zero corner by
\[
\tau_d=\inf\{k\geq0:X^{(d)}_k=\mathbf0\}.
\]
The chain is neither the nearest-neighbor cube walk nor the fixed-number-of-flips walk. Its one-coordinate relaxation rate tends to zero with dimension.

**Theorem.** The following statements hold, with \(r=e^{-a}\):

1. For every admissible \(d\), the **exact finite-dimensional mean** is
\[
\mathbb E_{\pi_d}\tau_d=\sum_{j=1}^d\frac{\binom dj}{1-(1-2a/d)^j}.
\]
2. The **stationary first-entrance law** is
\[
\frac{\tau_d}{2^d}\ \Rightarrow\ \operatorname{Exp}(1-r),
\qquad
\Pr\{\tau_d>t2^d\}\longrightarrow e^{-(1-r)t}\quad(t\geq0).
\]
Here \(\operatorname{Exp}(\theta)\) denotes the exponential distribution of rate \(\theta\).
3. For every fixed \(a>0\), the **first finite-dimension correction** to the normalized mean is
\[
\boxed{\frac{\mathbb E_{\pi_d}\tau_d}{2^d}
 =\frac1{1-e^{-a}}
 +\frac{a^2e^{-a}(3e^{-a}-1)}{2d(1-e^{-a})^3}
 +O_a(d^{-2}).}
\]
The displayed coefficient is strictly positive for \(0<a<\log3\), zero for \(a=\log3\), and strictly negative for \(a>\log3\). Therefore for every fixed \(a\neq\log3\), the finite-dimensional mean, divided by \(2^d\), eventually approaches its limit from the indicated side.
4. Conditional on entering the corner, the length of the uninterrupted consecutive run of corner visits has the exact geometric law with success parameter \(1-(1-a/d)^d\), which tends to \(1-e^{-a}\). No claim about a full marked point-process limit is needed for parts 1–3.

The meaningful distinction is that a set of stationary mass \(2^{-d}\) is **not** hit on the naive mean scale \(2^d\) with rate one: temporally adjacent visits cluster. The exact slowdown \((1-e^{-a})^{-1}\) and the change of sign of its first finite-dimensional correction quantify the dimension-dependent persistence that a fixed-coordinate-chain mixing theorem does not resolve.

## Assumptions and scope

All coordinates flip independently across both coordinates and time, and \(a\) is constant as \(d\to\infty\). The chain starts at stationarity, **not** at a specified noncorner configuration. Hitting time includes time zero; the initial mass at the corner is exactly \(2^{-d}\). Every assertion is for the single fixed corner \(\mathbf0\), not a growing family of holes. The asymptotic remainder \(O_a(d^{-2})\) may depend on \(a\) and is not uniform as \(a\downarrow0\) or \(a\to\infty\).

## Proof

**Step 1: return kernel and stationary renewal identity.** Set
\[
\varpi_d=2^{-d},\qquad \lambda_d=1-2a/d\in(0,1),\qquad
u_d(k)=\Pr_{\mathbf0}(X^{(d)}_k=\mathbf0)
=\left(\frac{1+\lambda_d^k}{2}\right)^d.
\]
The one-coordinate return probability after \(k\) steps is \((1+\lambda_d^k)/2\). Define \(U_d(z)=\sum_{k\geq0}u_d(k)z^k\) and \(F_d(z)=\mathbb E_{\pi_d}[z^{\tau_d}]\) for \(0\leq z<1\). Stationarity and the strong Markov property at the first entrance give, for each \(k\geq0\),
\[
\varpi_d=\sum_{j=0}^k\Pr_{\pi_d}(\tau_d=j)u_d(k-j).
\]
Therefore
\[
\frac{\varpi_d}{1-z}=F_d(z)U_d(z).
\]
Write
\[
G_d(z)=\sum_{k\geq0}(u_d(k)-\varpi_d)z^k.
\]
Binomial expansion of the return kernel yields the nonnegative spectral representation
\[
G_d(z)=\varpi_d\sum_{j=1}^{d}\frac{\binom dj}{1-z\lambda_d^j},\qquad
F_d(z)=\frac{\varpi_d}{\varpi_d+(1-z)G_d(z)}.
\]
All displayed generating functions converge absolutely for \(z<1\), while \(G_d(1)\) is finite for each \(d\). Differentiating the last formula as \(z\uparrow1\) yields
\[
\mathbb E_{\pi_d}\tau_d=F_d'(1^-)=\frac{G_d(1)}{\varpi_d},
\]
proving assertion 1 exactly.

**Step 2: the rare-hit exponential law.** Let \(J_d\sim\operatorname{Bin}(d,1/2)\). Then
\[
G_d(1)=\mathbb E\left[\frac{\mathbf1_{\{J_d\geq1\}}}{1-\lambda_d^{J_d}}\right].
\]
As \(d\to\infty\), \(J_d/d\to1/2\) in probability and \(\lambda_d^{J_d}\to e^{-a}\). On \(J_d\geq d/4\), the reciprocal denominator is uniformly bounded for large \(d\), while on \(1\leq J_d<d/4\) it is at most \(d/(2a)\) and this event has exponentially small probability. Consequently
\[
G_d(1)\longrightarrow G_\infty=\frac1{1-e^{-a}}.
\]
For each fixed \(k\geq0\), \(u_d(k)-\varpi_d\to e^{-ak}\). These terms are nonnegative, and their total sum tends to \(G_\infty=\sum_{k\geq0}e^{-ak}\), so their mass has uniformly negligible tails beyond a sufficiently large fixed \(k\). It follows for every fixed \(s\geq0\) that
\[
G_d(e^{-s\varpi_d})\longrightarrow G_\infty.
\]
Substituting \(z=e^{-s\varpi_d}\) in the exact expression for \(F_d\), and using \((1-e^{-s\varpi_d})/\varpi_d\to s\), gives
\[
\mathbb E_{\pi_d}e^{-s\tau_d/2^d}
\longrightarrow\frac1{1+sG_\infty}
=\frac{1-e^{-a}}{s+1-e^{-a}}.
\]
This is the Laplace transform of the asserted exponential law. Distribution-function convergence follows by continuity of its limit, including at \(t=0\).

**Step 3: the \(d^{-1}\) correction and its sign.** Put \(b_d=-d\log\lambda_d=2a+2a^2/d+O_a(d^{-2})\), and
\[
h_d(x)=\frac1{1-e^{-b_dx}},\qquad x>0.
\]
On \(x\in[1/4,3/4]\), derivatives of \(h_d\) through order four are uniformly bounded (for fixed \(a\)). By the binomial concentration inequality, the contribution from \(J_d\notin[d/4,3d/4]\) is exponentially small even after the bound \(h_d(j/d)\le d/(2a)\) for \(j\ge1\). The centered binomial law has
\[
\mathbb E(J_d/d-1/2)=\mathbb E(J_d/d-1/2)^3=0,\quad
\mathbb E(J_d/d-1/2)^2=\frac1{4d},\quad
\mathbb E(J_d/d-1/2)^4=O(d^{-2}).
\]
Taylor's theorem to cubic order, with fourth-order remainder, therefore shows
\[
G_d(1)=h_d(1/2)+\frac{h_d''(1/2)}{8d}+O_a(d^{-2}).
\]
Writing \(r=e^{-a}\), straightforward differentiation and the expansion for \(b_d\) give
\[
 h_d(1/2)=\frac1{1-r}-\frac{a^2r}{d(1-r)^2}+O_a(d^{-2}),
\]
\[
 h_d''(1/2)=\frac{4a^2r(1+r)}{(1-r)^3}+O_a(d^{-1}).
\]
Adding the terms yields
\[
G_d(1)=\frac1{1-r}+\frac{a^2r(3r-1)}{2d(1-r)^3}+O_a(d^{-2}),
\]
which is assertion 3 by Step 1. Since \(r=e^{-a}\), the coefficient changes sign precisely at \(a=\log3\). For assertion 4, from the corner the chance of no coordinate flip in the next step is \((1-a/d)^d\). The Markov property makes the length of the consecutive visit run geometric with departure probability \(1-(1-a/d)^d\).

## Verification

The accompanying standalone `checker.py` uses exact rational arithmetic to construct and solve the Hamming-weight lumped absorbing chain and compares its stationary first-passage mean and probability generating function against the spectral/renewal identities for \(1\le d\le7\) and three rational flip probabilities. It also numerically tests the first-order asymptotic and sign prediction at dimensions through \(1600\). An execution of that packaged checker passed 225 assertions. The infinite-dimensional limit and signed correction are proved in Steps 2–3; numerical checks are not used to infer those limits.

## Relationship to prior work

Tanzi and Tenaglia (2026, arXiv:2609.10178, initially posted 2026-09-09) study quasi-stationarity for products of a **fixed** mixing one-coordinate chain and arbitrary small holes. Their Theorems 2.1–2.2 depend on dimension-independent single-coordinate contraction, which fails for the present array because \(\lambda_d\to1\). They do not give the stated exact stationary-corner first-passage transform, rate \(1-e^{-a}\), or signed \(1/d\) correction.

Černý and Gayrard (2006/2008, arXiv:math/0611242, Theorems 1.1–1.3) analyze hitting times for the nearest-neighbor cube walk, with random or deterministic target sets. Its one-coordinate-at-a-time transition kernel is different from independent simultaneous bit flips, so neither its transition law nor its assertions imply the displayed finite-dimensional correction. Its discussion of earlier point-hitting formulas and Kemperman's classical stationary passage theory is acknowledged: the renewal identity is standard, and only its particular critical-dimensional analysis is claimed here.

Nestoridi (2015, arXiv:1507.05690) treats fixed-size subsets of flipped coordinates and mixing cutoff, rather than stationary corner entrance for a binomial number of simultaneous flips. Peixoto and Marcondes (2017, arXiv:1709.02359) treat single-coordinate nearest-neighbor walks and their hitting and return times; their full-text model definition excludes simultaneous coordinate flips. General extremal-index theory can explain an exponential law under suitable conditions, but it does not automatically supply the finite-size coefficient or its \(\log3\) sign change. Historical coverage of this precise specialization remains possible.

## Limitations

The result does not apply without modification to a nonstationary initial state, to heterogeneous coordinates, to other target subsets, or to joint path/point-process limits. In particular, the consecutive-run calculation alone is **not** a proof of full Poisson-cluster convergence. The rate and correction concern fixed \(a>0\), not a regime in which \(a\) varies with \(d\). The finite-dimensional sign of the difference is asserted only eventually for fixed \(a\neq\log3\), not uniformly around the crossover. Historical priority in broader rare-event theory is not certified.

## References

1. M. Tanzi and G. Tenaglia, *Stability of quasi-stationary measures in high-dimensional products of mixing Markov chains*, arXiv:2609.10178 (first posted 2026-09-09), https://arxiv.org/abs/2609.10178 .
2. J. Černý and V. Gayrard, *Hitting time of large subsets of the hypercube*, arXiv:math/0611242 (2006), *Random Structures & Algorithms* **33** (2008), 252–267, https://arxiv.org/abs/math/0611242 .
3. E. Nestoridi, *A non-local random walk on the hypercube*, arXiv:1507.05690 (2015), https://arxiv.org/abs/1507.05690 .
4. C. Peixoto and D. Marcondes, *Stopping Times of Random Walks on a Hypercube*, arXiv:1709.02359 (first posted 2017-09-07), https://arxiv.org/abs/1709.02359 .
5. J. H. B. Kemperman, *The Passage Problem for a Stationary Markov Chain*, University of Chicago Press (1961). Classical background; full text was not available in this check.
