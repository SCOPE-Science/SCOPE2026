# A logarithmic fluctuation law for palindromic-prefix counts of periodic-directive Sturmian words

## Finding

Fix integers \(k\ge1\) and \(d_1,\ldots,d_k\ge1\), periodically extended as \(d_{i+k}=d_i\), and put \(S=\sum_{r=1}^k d_r\). Let \(c_{\mathbf d}\) be the corresponding standard Sturmian word, and let \(\pi(N)\) count its **nonempty palindromic prefixes** of length at most the integer \(N\ge1\).

Put \(\ell_{-1}=\ell_0=1\) and \(\ell_n=d_n\ell_{n-1}+\ell_{n-2}\). Let \(B=M(d_k)\cdots M(d_1)\), with \(M(a)=\begin{pmatrix}a&1\\1&0\end{pmatrix}\); denote its Perron eigenvalue by \(\lambda>1\) and its second eigenvalue by \(\mu=(-1)^k/\lambda\). For each ordered pair \((r,j)\), \(1\le r\le k\), \(1\le j\le d_r\), set

\[
 A_{r,j}=j\ell_{r-1}+\ell_{r-2},\quad
 D_{r,j}=j\ell_{k+r-1}+\ell_{k+r-2},\quad
 c_{r,j}=\frac{D_{r,j}-\mu A_{r,j}}{\lambda-\mu},\quad
 e_{r,j}=\frac{\lambda A_{r,j}-D_{r,j}}{\lambda-\mu}.
\]

All the \(c_{r,j}\) are positive. Enumerate them in the displayed lexicographic order as \(c_1,\ldots,c_S\) and define

\[
 z_m=\log_{\lambda}(c_m/c_1),\qquad
 z_{S+1}=1.
\]

Then \(0=z_1<z_2<\cdots<z_S<1\). The palindromic-prefix thresholds, including the initial empty one, admit the **exact two-eigenvalue formula**

\[
 \boxed{\,\theta_{q,r,j}+2=c_{r,j}\lambda^q+e_{r,j}\mu^q\,},\qquad
 \theta_{q,r,j}=j\ell_{qk+r-1}+\ell_{qk+r-2}-2,\quad q\ge0.
\]

In particular, at all sufficiently large periods, each \(\theta_{q,r,j}\) is exactly the nearest integer to \(c_{r,j}\lambda^q\), minus two. An explicit sufficient cutoff is any integer \(q_0\ge0\) such that \(\max_{r,j}|e_{r,j}|\lambda^{-q_0}<1/2\).

For \(0\le t<1\), define the right-continuous staircase

\[
 H(t)=\#\{m:z_m\le t\},\qquad F(t)=H(t)-1-St,
\]

and for \(N\ge1\) define the centered count and logarithmic phase

\[
 Z(N)=\pi(N)-S\log_{\lambda}\!\left(\frac{N+2}{c_1}\right),\qquad
 t_N=\left\{\log_{\lambda}\!\left(\frac{N+2}{c_1}\right)\right\}.
\]

**Fluctuation and limit-law theorem.** Outside a set of at most \(O(\log X)\) exceptional integers \(N\le X\), one has the exact equality \(Z(N)=F(t_N)\). For every bounded continuous real-valued function \(g\),

\[
 \boxed{\lim_{X\to\infty}\frac{1}{\sum_{N\le X}N^{-1}}\sum_{N\le X}\frac{g(Z(N))}{N}
 =\int_0^1 g(F(t))\,dt.}
\]

The limiting law is absolutely continuous, with density

\[
 \boxed{\displaystyle f(y)=\frac1S\sum_{m=1}^{S}
 \mathbf1_{\,(m-1-Sz_{m+1},\ m-1-Sz_m)\,}(y).}
\]

Its mean is \(S/2-1-\sum_{m=1}^S z_m\). Moreover, ordinary (unweighted) sampling has a **complete, phase-dependent family** of subsequential laws. If \(X\to\infty\) through integers with \(t_X\to u\in[0,1)\), then

\[
 \boxed{\frac1X\sum_{N=1}^{X}g(Z(N))\ \longrightarrow\ \int_0^1 g(F(t))\,\rho_u(t)\,dt,\qquad
 \rho_u(t)=(\log\lambda)\lambda^{t-u}\left(\frac1{\lambda-1}+\mathbf1_{\{t\le u\}}\right).}
\]

The corresponding limiting means are nonconstant as \(u\) varies, so ordinary empirical means do not converge; this explains why logarithmic weighting is essential for a unique limit law. The **sharp** global oscillation bounds are

\[
 \limsup_{N\to\infty}Z(N)=\max_{1\le m\le S}(m-1-Sz_m),\qquad
 \liminf_{N\to\infty}Z(N)=\min_{1\le m\le S}(m-1-Sz_{m+1}).
\]

For the Fibonacci directive \((1)^\infty\), \(Z(N)\) has the uniform logarithmic limiting law on \((-1,0)\). For the constant-two directive, \(\lambda=1+\sqrt2\) and \(z_2=\log_{\lambda}(1+1/\sqrt2)\); two overlapping affine branches produce a nonuniform density equal to \(1/2\) on the two edge intervals and \(1\) on their overlap. This is a distributional refinement of the previously established logarithmic count with bounded error, not a new derivation of that first-order bound.

## Assumptions and scope

The directive is **purely periodic**, with positive integers. The count is for distinct **nonempty palindromic prefixes** of the associated one-sided standard Sturmian word, not all palindromic factors, and \(N\) ranges over positive integers. Logarithmic sampling means weighting integer \(N\) by \(1/N\), normalized by the harmonic sum; ordinary uniform sampling is not claimed to have this same limiting distribution. The displayed finite list \(z_1,\ldots,z_S\) may depend on the chosen period presentation of the directive, but the resulting normalized limiting law is consistent under period repetition. No statement is made for nonperiodic directives.

## Proof

**1. Palindromic-prefix indexing.** The established length theorem for standard Sturmian words [1, Theorem 2.15 and Corollary 3.3] identifies all palindromic-prefix lengths with \(j\ell_{i-1}+\ell_{i-2}-2\), for \(i\ge1\) and \(1\le j\le d_i\). Every length occurs exactly once, and the only zero length corresponds to \((i,j)=(1,1)\). This is the specific earlier theorem used as input; it is also checked independently on finite literal words in the attached verifier.

**2. Exact spectral identity.** Set \(v_n=(\ell_n,\ell_{n-1})^\mathsf T\). Periodicity gives \(v_{qk+r}=M(d_r)\cdots M(d_1)B^q v_0\) for every \(q\ge0\) and fixed \(r\). By Cayley–Hamilton, each fixed linear functional of \(v_{qk}\), including \(T_{q,r,j}=\theta_{q,r,j}+2\), satisfies

\[
 T_{q+2,r,j}=(\lambda+\mu)T_{q+1,r,j}-\lambda\mu T_{q,r,j}.
\]

Its two initial values are exactly \(A_{r,j}\) and \(D_{r,j}\). Solving this order-two recurrence yields \(T_{q,r,j}=c_{r,j}\lambda^q+e_{r,j}\mu^q\), including all boundary cases \(k=1\) and \(j=d_r\). Since the values \(T_{q,r,j}\) tend to infinity with \(q\), while \(|\mu|<1\), each \(c_{r,j}>0\). The nearest-integer statement follows because \(T_{q,r,j}\) is an integer and its difference from \(c_{r,j}\lambda^q\) is at most \(|e_{r,j}|\lambda^{-q}\).

**3. Strict spectral phases.** In the indexing in step 1, the increment from \((r,j)\) to the immediately next pair is exactly the appropriate positive standard-word length \(\ell_i\). For a fixed position inside one periodic block, this length grows like a strictly positive constant times \(\lambda^q\) by Perron–Frobenius positivity (the period transfer matrix is primitive after a power). Thus consecutive dominant constants satisfy \(c_{m+1}-c_m>0\). The last length of a period and the first length of the next period have the same kind of positive increment, giving \(\lambda c_1-c_S>0\). Therefore \(0=z_1<\cdots<z_S<1\), including \(S=1\).

**4. Exceptional-threshold bound and sharp extrema.** The ideal thresholds in period \(q\) are \(c_m\lambda^q-2\), and the true integer thresholds differ by \(e_m\mu^q\). For all sufficiently large \(q\), this perturbation is smaller than \(1/2\). Away from the at most two integers neighboring each ideal threshold, the ordered ideal and true threshold indicator functions agree. There are only \(S\) thresholds per period and \(O(\log X)\) periods below \(X\), hence at most \(O(\log X)\) exceptional integers below \(X\). With \(q=\lfloor\log_\lambda((N+2)/c_1)\rfloor\), all earlier complete periods contain \(qS\) indexed lengths, and the initial zero length must be subtracted. The ideal count is therefore \(qS+H(t_N)-1\), proving \(Z(N)=F(t_N)\) off the exceptions. Each branch \([z_m,z_{m+1})\) has \(F(t)=m-1-St\). Integers approaching exponentially growing thresholds from either side realize every one-sided endpoint limit, so the stated limsup and liminf are sharp, not merely bounds.

**5. Harmonic and ordinary limiting laws.** The set of exceptions has summable total harmonic weight: at each of the exponentially spaced thresholds there are \(O(1)\) exceptions of size comparable to \(\lambda^q\), so \(\sum_{N\text{ exceptional}}1/N<\infty\). Under harmonic weights, the fractional parts of \(\log_\lambda((N+2)/c_1)\) approach uniform measure on \([0,1)\). This follows by comparison with \(\int dx/x\), substitution \(t=\log_\lambda((x+2)/c_1)\), and counting complete logarithmic periods; the factor \(x+2\) instead of \(x\) changes only a summable error. Since \(F\) is bounded and has only finitely many discontinuities, bounded continuous test functions can be averaged in this way. Pushing uniform measure through the \(S\) affine branches \(y=m-1-St\), each of absolute slope \(S\), yields the claimed density. Integrating \(H-1-St\) gives the displayed mean. This argument also establishes that the limiting law has no atoms, even when some branch images overlap.

For an ordinary integer cutoff of phase \(u\), split the real interval from a fixed large base to \(X\) into full geometric annuli \([c_1\lambda^q,c_1\lambda^{q+1})\) and a final partial annulus. On a full annulus, substituting \(x=c_1\lambda^{q+t}\) gives the weight \(c_1(\log\lambda)\lambda^{q+t}dt\). Relative to \(X\sim c_1\lambda^{Q+u}\), the sum of complete annuli has factor \(\lambda^{-u}/(\lambda-1)\), while the final annulus contributes an additional \(\lambda^{-u}\mathbf1_{t\le u}\). This proves the displayed density \(\rho_u\), which integrates to one. Riemann comparison passes from the continuous integral to integer samples; the exceptional integers contribute \(O(\log X/X)\). Finally, writing \(M(u)=\int_0^1F(t)\rho_u(t)dt\), direct differentiation on each interval between phase discontinuities yields \(M'(u)=(\log\lambda)(F(u)-M(u))\). A constant \(M\) would force \(F\) to be constant almost everywhere, impossible because its slope is \(-S\) away from finitely many jumps. Thus the ordinary empirical means have distinct subsequential limits.

## Verification

The attached `verify_fluctuations.py` is a standalone Python standard-library script; run it with `python verify_fluctuations.py`. It independently forms literal palindromic closures, checks the standard-word length representation, computes the full period matrix, verifies the exact spectral recurrence against integer length values and compares 360,000 explicit integer prefix counts against the phase staircase for twelve different directives. Every observed disagreement is confined to an integer within two of a genuine palindromic threshold, as expected in the finite initial regime; numerical midpoint integration checks the formula for the mean; three directives additionally compare the phase-conditioned ordinary-limit mean against 30,000 cutoff samples. The machine output is provided as `verification_output.txt`.

These finite experiments are evidence of implementation consistency, **not** proof of the infinite claims; the proof rests on the recurrence, strict positivity, threshold bound and harmonic-measure argument above.

## Relationship to prior work

Hamoud [1], first publicly posted 15 November 2026, supplies the palindromic-length formula and proves \(\pi(N)=(S/\log\lambda)\log N+O(1)\), including failure of an \(o(1)\) remainder. The novelty asserted here is **not** those antecedent results: it is the complete finite-parameter fluctuation law, its explicit absolutely continuous limiting density, exact sharp endpoints, and the eventual integer-rounding description of every individual length threshold. Fischler [2] studies the palindromic-prefix length sequence through ratio-growth invariants and continued fractions; its established results do not give the above centered-count distribution. De Luca and Fici [3] characterize open/closed prefix sequences and their run structure, a different statistic. These sources were read and compared at the level of conclusions and implications, not just titles. General lattice-renewal analogies motivate the calculation but do not by themselves supply the word-specific phase constants or the explicit Sturmian density.

## Limitations

The conclusion is conditional on the exact prior palindromic-prefix length theorem; its proof is not claimed as new. All density and endpoint constants refer to the specific additive normalization \(\log_\lambda((N+2)/c_1)\); changing the centering changes the shift of the law. The agreement \(Z(N)=F(t_N)\) is not claimed literally for every integer, and the unique limit law requires logarithmic weighting; ordinary counting produces the stated phase-dependent family instead. The limits do not imply independent confirmation or historical priority beyond the inspected literature. A mathematically equivalent unindexed lattice-renewal formulation or later source may exist.

## References

1. J. Hamoud, *Lengths and Counting of Palindromic Prefixes of Standard Sturmian Words*, arXiv:2611.20221v1, posted 15 November 2026, §§2–4, https://arxiv.org/html/2611.20221v1 .
2. S. Fischler, *Palindromic prefixes and episturmian words*, Journal of Combinatorial Theory, Series A 113 (2006), 1281–1304, https://www.imo.universite-paris-saclay.fr/~stephane.fischler/palindromes.pdf .
3. A. de Luca and G. Fici, *Open and Closed Prefixes of Sturmian Words*, arXiv:1306.2254, https://arxiv.org/abs/1306.2254 .
