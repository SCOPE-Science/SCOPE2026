# The exact inverse-moment threshold for independently sampled Fourier frames

## Finding

Fix integers \(m\ge N\ge3\). For independent Haar-uniform points \(Z_1,\ldots,Z_m\) on the complex unit circle, put
\[
A=(Z_j^k)_{1\le j\le m,\ 0\le k<N},\qquad
\Lambda=\lambda_{\min}(A^*A),\qquad R=\operatorname{tr}((A^*A)^{-1}).
\]
The Gram matrix is invertible almost surely. Define \(d=N-1\), \(M=m-1\), and \(\alpha=M/(2d)\). For fixed \(m,N\), there are positive constants \(c,C,s_0\) such that for \(0<s<s_0\),
\[
c s^{\alpha}\le \Pr(\Lambda\le s)\le C s^{\alpha}\bigl(1+\log(1/s)\bigr)^{(N-2)M/d}.
\]
In particular, for every \(p>0\),
\[
\mathbb E[\Lambda^{-p}]<\infty\quad\Longleftrightarrow\quad
\mathbb E[R^p]<\infty\quad\Longleftrightarrow\quad p<\alpha.
\]
The endpoint \(p=\alpha\) diverges. **Mean inverse-Gram risk is finite exactly when \(m\ge2N\)** in the stated range. For three modes the transition is from \(m=5\) (infinite) to \(m=6\) (finite).

## Model and statistical interpretation

The matrix is unnormalized and uses consecutive integer frequencies. Translating the band multiplies each row by a scalar of modulus one and preserves the Gram matrix. Let \(y=Ax+e\), with \(\mathbb E[e\mid A]=0\) and \(\mathbb E[ee^*\mid A]=\nu I_m\) almost surely for a fixed \(\nu>0\). In particular, these assumptions hold for centered independent noise entries with common variance \(\nu\) when the noise vector is independent of the design. For least squares, \(\widehat x-x=A^\dagger e\) almost surely, so
\[
\mathbb E[\|\widehat x-x\|_2^2\mid A]
=\operatorname{tr}\bigl(A^\dagger\mathbb E[ee^*\mid A](A^\dagger)^*\bigr)=\nu R.
\]
Thus its unconditional mean squared error is finite exactly at the threshold above. No prior on \(x\) is needed. Independence among noise coordinates alone does not justify conditioning on the design.

## Proof

**Rank and lower tail.** The first \(N\) rows form a square Vandermonde matrix with distinct nodes almost surely, proving full column rank. Write \(B_N^2=\binom{2N-2}{N-1}\). Take the polynomial \(P(z)=(z-Z_1)^d/B_N\), which has unit coefficient norm by the binomial-square identity. When every other node is within circular angular distance \(0<\delta<1\) of \(Z_1\), all chord distances to \(Z_1\) are at most \(\delta\) and
\[
\Lambda\le\|AP_{\rm coef}\|_2^2\le m\delta^{2d}/B_N^2.
\]
The event has probability \((\delta/\pi)^M\) by conditioning on \(Z_1\). Taking \(\delta=(s B_N^2/(2m))^{1/(2d)}\) gives the lower bound even for \(\Pr(\Lambda<s)\).

**Square-subframe estimate.** For a square Vandermonde matrix \(V\) of order \(N\), the \(i\)-th column of \(V^{-1}\) is the coefficient vector of the Lagrange basis polynomial at node \(Z_i\). Its numerator is \(\prod_{j\ne i}(z-Z_j)\), whose coefficient norm is at most \(B_N\) by the triangle inequality for each elementary symmetric sum. For \(L=\lambda_{\min}(V^*V)\),
\[
L^{-1/2}\le \|V^{-1}\|_{\mathrm F}\le B_N\sqrt N\max_i\prod_{j\ne i}|Z_i-Z_j|^{-1}.
\]
With \(N\) independent Haar nodes, condition on \(Z_i\) for each term of the maximum. The rescaled distances \(U_j=|Z_i-Z_j|/2\) are conditionally independent with distribution function \((2/\pi)\arcsin u\le u\) on \([0,1]\), using convexity of \(\arcsin\). Hence \(-\log U_j\) is dominated in the usual stochastic order by a rate-one exponential. The sum of \(d\) independent such exponentials has survival function \(e^{-t}\sum_{a=0}^{d-1}t^a/a!\) for \(t\ge0\). Apply the union bound to the maximum and use \(\prod_{j\ne i}|Z_i-Z_j|^{-1}=2^{-d}\exp(\sum_{j\ne i}-\log U_j)\). At threshold \(L\le s\) the sum must be at least \(\log(2^d/(B_N\sqrt{Ns}))\) for one of the \(i\). It follows that for all sufficiently small \(s>0\),
\[
q_N(s):=\Pr(L\le s)\le C_N\sqrt{s}(1+\log(1/s))^{N-2}.
\]
The same square law holds when one of the \(N\) nodes is fixed arbitrarily and all others remain independent Haar. Indeed, a common rotation of the nodes multiplies the columns by unit phases; for any fixed first node, rotating it to 1 leaves the remaining iid Haar law unchanged. Thus the conditional distribution given the first node is constant and equals the unconditioned one.

**Overlapping cyclic windows after conditioning.** Condition on \(Z_1\). Index the remaining \(M\) sample variables cyclically. For each of the \(M\) possible start indices, choose the cyclic window of \(d\) successive residual variables and adjoin the first node. This gives \(M\) square subframes \(V_i\); each residual coordinate occurs in exactly \(d\) windows. This holds even at \(M=d\), when windows use the same set of nodes. Because \(A^*A\succeq V_i^*V_i\), a small eigenvalue \(\Lambda\le s\) implies every event \(E_i=\{\lambda_{\min}(V_i^*V_i)\le s\}\).

For nonnegative bounded functions \(f_i\) each of only the variables in window \(i\), the product law on the residual variables gives
\[
\mathbb E\!\left[\prod_i f_i\mid Z_1\right]
\le\prod_i \left(\mathbb E[f_i^d\mid Z_1]\right)^{1/d}.
\]
To prove this, hold all but one residual variable fixed and apply Hölder of exponent \(d\) to its \(d\) incident functions, pulling out the other factors. Replace each incident factor by the \(d\)-th root of its integral to power \(d\) in that variable. Iterate over the residual variables. When the same factor is integrated in a second variable its root and the new power cancel, so its final value is precisely its full \(L^d\) norm. This argument does not assume independence of window events.

Take \(f_i=1_{E_i}\). All conditional one-window probabilities are \(q_N(s)\) by the preceding rotation argument. Therefore
\[
\Pr(\Lambda\le s\mid Z_1)\le q_N(s)^{M/d}.
\]
Removing the conditioning proves the asserted upper estimate with the same exponent \(\alpha\) as the lower bound. By the layer-cake formula, the small-\(s\) contribution to \(\mathbb E[\Lambda^{-p}]\) is determined by the integral of \(p s^{-p-1}\Pr(\Lambda<s)\); it is finite if \(p<\alpha\) and infinite if \(p\ge\alpha\). The endpoint divergence follows already from the power lower bound. The inequalities \(\Lambda^{-1}\le R\le N\Lambda^{-1}\) then give the trace conclusions. For \(p=1\) the strict inequality \(m-1>2N-2\) is equivalent to \(m\ge2N\).

**Uniform disjoint-block corollary.** For integers \(k\ge1\) with \(m\ge kN\), partition the first \(kN\) rows into \(k\) disjoint square blocks. The full Gram matrix dominates their summed Grams and its smallest eigenvalue is at least the sum of their least eigenvalues, by the Rayleigh principle. A small full eigenvalue forces all \(k\) block eigenvalues to be small; those block events are independent. This gives the separate bound \(C_{N,k}s^{k/2}(1+\log(1/s))^{k(N-2)}\) for small \(s>0\), uniform over \(m\ge kN\). This corollary does not replace the fixed-\(m,N\) sharp moment result.

## Verification and scope

The proof is analytic. `CHECK.py` checks the finite window incidence pattern and threshold arithmetic for bounded sizes and verifies the column-index identity in the design-dependent example \(e_j=Z_j\) on an exact fixture. Such checks do not establish the continuous probability laws. The constants in the two-sided tail bound are for fixed \(N,m\); the exact logarithmic correction or leading coefficient of the tall tail is not determined. No claim is made for nonconsecutive bands, nonuniform or dependent nodes, or dimension-asymptotic constants.

## Relationship to prior work

- Xu and Shen, [arXiv:2609.29286v1](https://arxiv.org/html/2609.29286v1), §1.1 and Theorem 6, use the same model in odd dimension after a frequency translation. Their Theorem 6 asserts unconditional inverse-**squared** least positive singular-value divergence for iid uniform sampling without restricting \(m\). Proposition 5, Eq. (19), and its use in §5.2 rely on a bound from a closest pair of rows. In §6.3 the row difference belongs to the domain of \(A^*\) rather than \(A\); even with the adjoint, the test vector need not be orthogonal to \(\ker A^*\) for a tall matrix. For example, two nodes may merge while at least \(N\) distinct nodes remain, in which case the least singular value stays strictly positive. The present mean-risk threshold contradicts that unrestricted divergence for odd \(N\) in the finite regime. It does not assess their other sampling schemes.
- Tucci and Whiting, [arXiv:1202.3184v2](https://arxiv.org/html/1202.3184v2#S3), Theorems 3.1 and 3.3, give inverse Vandermonde formulas and inverse-moment divergence for square matrices. The earlier [*Critical inverse moments and logarithmic tails of random Fourier interpolation*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-critical-inverse-moments-and-logarithmic-tails-of-random-fourier--323dcae74731) gives sharp square-tail information, including the \(1/2\) cutoff. The square estimate above is a supporting lemma, and stacking independent square blocks is a direct corollary of such a lemma. The contribution here is the sharp rectangular threshold using anchored overlapping windows, together with the matching power lower bound. The earlier [two-frequency circular Fourier sketch](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-sharp-small-singular-tails-and-inverse-moment-thresholds-for-a-c--5fb2ea549d24) treats the distinct case \(N=2\).
- Gröchenig, Pötscher, and Rauhut, [arXiv:math/0701781v2](https://arxiv.org/html/math/0701781v2), §2 Theorems 2.1–2.2 and §3 Corollary 3.3, give probability estimates near the well-conditioned regime, not the displayed vanishing upper power law as \(s\downarrow0\) with sample count fixed. They summarize relevant estimates of [Bass and Gröchenig](https://doi.org/10.1137/S0036141003432316). The latter full original text was not available for independent comparison. Historical priority for an equivalent threshold remains provisional.
