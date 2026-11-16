# Quadratic-logarithmic conditioning of dyadic no-carry convolution

## Finding
For every integer \(n\ge1\), put \(N=2^n\) and \(G_n=(\mathbb Z/N\mathbb Z)^2\). Let \(S_n\subseteq G_n\) be the set of pairs \((a,b)\), with representatives \(0\le a,b<N\), whose binary expansions have no common one-bit. Equivalently, \(\binom{a+b}{a}\) is odd. The cardinality of \(S_n\) is \(3^n\).

Define the **unnormalized** convolution operator on complex-valued functions by
\[
(C_nf)(x)=\sum_{s\in S_n}f(x-s),
\]
and its additive Fourier multipliers by
\[
W_n(u,v)=\sum_{(a,b)\in S_n}\exp\!\left(\frac{2\pi i(ua+vb)}N\right),\qquad 0\le u,v<N.
\]
Write \(T_n=n(n+1)/2\) and \(\sigma_n=\min_{u,v}|W_n(u,v)|\). Then **every multiplier is nonzero**, and
\[
\boxed{2^{-T_n}\le\sigma_n\le (4\pi/3)^n2^{-T_n}.}
\]
In particular \(C_n\) is invertible and its sharp spectral condition number \(\kappa_2(C_n)\) satisfies
\[
\boxed{(9/(4\pi))^n2^{T_n}\le \kappa_2(C_n)\le3^n2^{T_n},\qquad
\lim_{n\to\infty}\frac{\log_2\kappa_2(C_n)}{n^2}=\frac12.}
\]
These bounds determine the **exact quadratic coefficient** of the logarithmic conditioning asymptotics; they do not determine the exact minimum for every \(n\). The qualitative zero-freeness alone follows from classical results on vanishing sums of roots of unity; the quantitative quadratic-logarithmic spectral law is the finding.

## Assumptions and scope
All calculations take place over the complex field. Fourier transforms and convolutions are **not probability-normalized**. The Hilbert-space norm uses counting measure on the finite group \(G_n\). Binary no-carry is ordinary binary digitwise disjointness of the canonical integer representatives, not digitwise disjointness of arbitrary residue representatives. Here \(n\) ranges over all positive integers.

## Proof
**Digit factorization.** Each binary digit allows precisely the choices \((0,0),(1,0),(0,1)\). For \(\zeta=\exp(2\pi i/N)\), the Fourier transform therefore factors as
\[
W_n(u,v)=\prod_{j=0}^{n-1}\left(1+\zeta^{2^ju}+\zeta^{2^jv}\right).
\tag{1}
\]
At scale \(j\), set \(M=2^{n-j}\). Both nontrivial summands in the factor are \(M\)-th roots of unity.

**Uniform lower bound for one factor.** For arbitrary \(M\)-th roots \(z,w\), triangle inequality gives
\[
|1+z+w|\ge\bigl||1+z|-1\bigr|.
\]
If \(z=\exp(2\pi i a/M)\), put \(t=\min(a,M-a)/M\in[0,1/2]\). Then \(|1+z|=2\cos(\pi t)\), hence
\[
|1+z+w|\ge |2\cos(\pi t)-1|\ge3|t-1/3|.
\tag{2}
\]
For completeness, the last estimate follows from concavity of \(h(t)=2\cos(\pi t)-1\) on \([0,1/2]\): on \([0,1/3]\), \(h(t)\) lies above the chord \(1-3t\); on \([1/3,1/2]\), it lies below its tangent \(-\pi\sqrt3(t-1/3)\), which is at most \(-3(t-1/3)\). Since \(M\) is a power of two, \(3\nmid M\), and therefore
\[
|t-1/3|=\frac{|3\min(a,M-a)-M|}{3M}\ge\frac1{3M}.
\]
This proves \(|1+z+w|\ge 1/M\), with no need to assume nonvanishing. Applying it to every factor of (1) gives
\[
\sigma_n\ge\prod_{j=0}^{n-1}2^{-(n-j)}=2^{-T_n}>0.
\tag{3}
\]

**Simultaneous near-cancellation witness.** Put
\[
u_n=\frac{2^n-(-1)^n}{3}\in\mathbb Z,\qquad v_n=N-u_n.
\]
Because \(2^n\equiv(-1)^n\pmod3\), the displayed expression is integral. With \(v_n\equiv-u_n\pmod N\), the factor in (1) at frequency \((u_n,v_n)\) is real and equal to
\[
1+2\cos\!\left(2\pi\frac{2^ju_n}{N}\right).
\]
For every nonnegative integer \(j\), \(1+2\cos(2\pi 2^j/3)=0\). Since
\[
\frac{2^ju_n}{N}=\frac{2^j}{3}-\frac{(-1)^n2^j}{3N},
\]
the global Lipschitz constant \(4\pi\) for \(1+2\cos(2\pi t)\) gives
\[
\left|1+2\cos\!\left(2\pi\frac{2^ju_n}N\right)\right|
\le\frac{4\pi}{3}\,2^{-(n-j)}.
\]
Multiplication over \(j\) proves
\[
\sigma_n\le |W_n(u_n,v_n)|\le(4\pi/3)^n2^{-T_n}.
\tag{4}
\]

**Condition number.** Fourier diagonalization of convolution on the finite abelian group \(G_n\) gives singular values \(|W_n(u,v)|\). Their maximum equals \(|W_n(0,0)|=|S_n|=3^n\), as the triangle inequality bounds every other coefficient by this value. Hence \(\kappa_2(C_n)=3^n/\sigma_n\). Equations (3) and (4) yield both condition bounds in the finding. Taking base-two logarithms yields \(\log_2\kappa_2(C_n)=T_n+O(n)\), and division by \(n^2\) gives the stated limit.

## Verification
The accompanying standalone `check_no_carry.py` computes the Fourier sum directly from the carry-free pairs and independently from product (1) for **all** \(1364\) frequencies at lengths \(1\le n\le5\), comparing results with explicit numerical tolerances. At those lengths it checks the stated universal lower bound and the specified upper-bound witness. It also tests the witness bounds at lengths \(6\le n\le10\). The checker uses standard Python only. Its expected final line is `NO_CARRY_FOURIER_BOUNDS_PASS direct_coefficients 1364`.

These floating-point checks are finite corroboration, not an infinite proof, and do not establish an exact minimizer. The all-length conclusion rests on the explicit analytic inequalities above.

## Relationship to prior work
Lam and Leung, *On vanishing sums for roots of unity* (1995), prove that a nonempty vanishing sum of roots of unity of power-of-two order has even weight. In combination with the elementary digit product (1), their result already implies the **qualitative zero-freeness** here. Neither their weight theorem nor the cited portions of their full text quantify the smallest modulus of the entire product or establish its quadratic logarithmic conditioning rate; those quantitative assertions are the object of this result.

Shevelev, *On Stephan's conjectures concerning Pascal triangle modulo 2 and their polynomial generalization* (first posted 2010), establishes arithmetic and generating-function identities for binary Pascal rows. Its studied statements concern integer encodings and digit combinatorics, not the worst-case two-dimensional cyclic Fourier multiplier and its singular-value growth.

Classical work on harmonic analysis of self-similar measures supplies broad context for digit products. General digit-product identities themselves are not claimed as novel. A prior quantitative theorem specifically treating the minimum modulus of these cyclic products could supersede the main assertion; exhaustive historical priority has not been established.

## Limitations
The result does **not** assert that \((u_n,v_n)\) is a global minimizer; the sharp finite-length minimum and the linear term in \(\log_2\kappa_2(C_n)\) remain open here. It treats only binary no-carry pairs and convolution on the **two-dimensional product of dyadic cyclic groups**, not a general base, general digital fractal, or convolution on a Boolean cube. Independent mathematical validation has not been performed.

## References
1. T. Y. Lam and K. H. Leung, *On vanishing sums for roots of unity*, arXiv:math/9511209v1, first posted 1995-11-13; published as *On vanishing sums of roots of unity*, Journal of Algebra **224** (2000), 91–109. Relevant material: introduction and Theorem 5.2 / Corollary 5.6.
2. V. Shevelev, *On Stephan's conjectures concerning Pascal triangle modulo 2 and their polynomial generalization*, arXiv:1011.6083, first posted 2010-11-17. Relevant material: introduction, Theorem 1, and digit-product formula.
3. P. E. T. Jorgensen and S. Pedersen, *Orthogonal harmonic analysis of fractal measures*, Electronic Research Announcements of the AMS **4** (1998), 35–42; arXiv:math/9912127. General background on fractal harmonic analysis, not a source of the quantitative dyadic convolution bounds.
