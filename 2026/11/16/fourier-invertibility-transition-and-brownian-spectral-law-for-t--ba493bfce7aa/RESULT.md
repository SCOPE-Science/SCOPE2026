# Fourier invertibility transition and Brownian spectral law for two-row order ideals

## Finding
For every integer \(n\ge1\), let \(J_n\subseteq\mathbb F_2^{2n}\) be the set of incidence vectors of all order ideals of the product poset \(C_2\times C_n\). Let \(C_n\) denote unnormalized convolution by the indicator \(1_{J_n}\), and let \(W_n(\xi)\) denote its unnormalized Walsh--Fourier multiplier. Then \(C_n\) is invertible **if and only if** \(n\equiv0,1\pmod4\). Furthermore, setting \(g_n=\min\{|W_n(\xi)|:W_n(\xi)\ne0\}\), one has
\[
g_n=\begin{cases}1,&n\equiv0,1\pmod4,\\2,&n\equiv2,3\pmod4.\end{cases}
\]
The exact Moore--Penrose inverse norm is \(\|C_n^\dagger\|_{2\to2}=g_n^{-1}\); the sharp positive-spectral condition number is \(\binom{n+2}{2}/g_n\).

There is also a non-Gaussian *full-spectrum asymptotic law*. If \(\Xi_n\) is uniformly random in \(\mathbb F_2^{2n}\), then
\[
\frac{W_n(\Xi_n)}{n}\ \Longrightarrow\ X,\qquad \mathbb E e^{itX}=\frac{1}{\sqrt{\cosh t}}\quad(t\in\mathbb R).
\]
The limit is continuous and non-Gaussian, with variance \(1/2\) and fourth moment \(7/4\). In particular, even along singular lengths \(n\equiv2,3\pmod4\), the fraction of Fourier multipliers that vanish converges to zero. The theorem therefore separates exact invertibility at finite lengths from asymptotically full spectral rank.

## Assumptions and scope
The poset \(C_r\) is the totally ordered set of \(r\) points. Label \(C_2\times C_n\) with two rows of \(n\) coordinates so every ideal is the union of an initial segment of length \(a\) in the first row and one of length \(b\) in the second row, where \(0\le b\le a\le n\). Here the convention of the row order may be reversed without changing any Fourier assertion. There are exactly \(\binom{n+2}{2}\) such ideals. Boolean addition and convolution are taken in \(G_n=\mathbb F_2^{2n}\): \((C_nf)(x)=\sum_{y\in G_n}1_{J_n}(y)f(x+y)\). Walsh characters are \(\chi_\xi(x)=(-1)^{\xi\cdot x}\), and \(W_n(\xi)=\sum_{I\in J_n}\chi_\xi(1_I)\). All Fourier coefficients are **unnormalized** integers; the Hilbert norm on the finite group is counting-measure \(\ell^2\). These conventions determine the stated inverse norms.

## Proof
**1. Exact two-prefix formula.** For a fixed frequency, write \(s_i=(-1)^{\xi_{1,i}}\) and \(t_j=(-1)^{\xi_{2,j}}\). Put \(A_0=B_0=1\), \(A_a=\prod_{i=1}^a s_i\) and \(B_b=\prod_{j=1}^b t_j\). The contribution of the ideal \((a,b)\) is exactly \(A_aB_b\); hence
\[
W_n=\sum_{a=0}^n\sum_{b=0}^a A_aB_b
=1+\sum_{a=1}^n A_aP_a,\qquad P_a=\sum_{b=0}^a B_b.
\]
Prefix products give a bijection between all \(2^{2n}\) frequencies and all choices of signs \(A_1,\ldots,A_n,B_1,\ldots,B_n\); there are no hidden constraints.

**2. Zero-free widths.** Every signed sum of \(\binom{n+2}{2}\) terms each equal to \(\pm1\) has the same parity as \(\binom{n+2}{2}\). The latter is odd precisely for \(n\equiv0,1\pmod4\). Thus in those widths all multipliers are nonzero and have absolute value at least one.

**3. Sharp zeros and gaps.** Choose \(B_b=(-1)^b\), for \(0\le b\le n\). Then \(P_a\) equals one if \(a\) is even and zero otherwise, giving
\[
W_n=1+\sum_{j=1}^{m}A_{2j},\qquad m=\lfloor n/2\rfloor.
\]
If \(n\equiv0,1\pmod4\), then \(m\) is even; choose exactly \(m/2\) signs positive and \(m/2\) negative, making \(W_n=1\). If \(n\equiv2,3\pmod4\), then \(m\) is odd; choose \((m-1)/2\) signs positive and \((m+1)/2\) negative to get \(W_n=0\), and reverse one choice to get \(W_n=2\). In these singular widths all multipliers are even by part 2, hence every nonzero multiplier has magnitude at least two. These constructions prove the entire finite-length dichotomy and exact \(g_n\).

**4. Sharp operator norms.** Every Walsh character is an eigenvector of convolution with eigenvalue \(W_n(\xi)\). The largest absolute multiplier is at most \(|J_n|\) by the triangle inequality and equals \(|J_n|\) at frequency zero. The Moore--Penrose inverse multiplies every nonzero Fourier mode by its reciprocal and kills zero modes, so its norm is \(1/g_n\), and the ratio of largest to smallest positive singular value is \(|J_n|/g_n\).

**5. Characteristic-function limit.** At uniformly random frequency the signs \(A_1,\ldots,A_n,B_1,\ldots,B_n\) of part 1 are independent symmetric Rademacher variables. Condition on the \(B\) signs. The independence of the \(A\) signs gives, for each fixed real \(t\),
\[
\mathbb E\bigl[e^{itW_n/n}\mid (B_b)\bigr]
=e^{it/n}\prod_{a=1}^n\cos(tP_a/n).
\]
Writing \(P_a=1+\sum_{b=1}^a B_b\), the functional central limit theorem says that the random step paths \(P_{\lfloor ns\rfloor}/\sqrt n\) converge in distribution to standard Brownian motion \((\mathcal B_s)_{0\le s\le1}\). On events where all \(|tP_a/n|\) are small, the estimate \(\log\cos z=-z^2/2+O(z^4)\) applies uniformly. Those events have probability tending to one by the maximal inequality for partial sums; moreover, independence and fourth-moment bounds give
\[
\mathbb E\Bigl[\sum_{a=1}^nP_a^4/n^4\Bigr]=O(1/n).
\]
It follows that the unconditional characteristic function converges to
\[
\mathbb E\exp\Bigl(-\frac{t^2}{2}\int_0^1\mathcal B_s^2\,ds\Bigr).
\]
For completeness, the Brownian quadratic-functional Laplace transform is calculated rather than merely invoked. By the Feynman--Kac formula, \(u(r,x)=\mathbb E_x\exp[-t^2\int_0^r\mathcal B_s^2\,ds/2]\) solves
\[
\partial_r u=\tfrac12\partial_{xx}u-\tfrac12t^2x^2u,\qquad u(0,x)=1.
\]
Direct substitution verifies the bounded solution
\[
u(r,x)=\frac{\exp[-|t|x^2\tanh(|t|r)/2]}{\sqrt{\cosh(|t|r)}}.
\]
Thus \(u(1,0)=(\cosh t)^{-1/2}\). Lévy's continuity theorem gives the claimed weak limit, equivalently represented as \(X=\int_0^1\mathcal B_s\,d\mathcal W_s\) with an independent standard Brownian motion \(\mathcal W\). Expanding the characteristic function at zero yields \(\mathbb EX^2=1/2\) and \(\mathbb EX^4=7/4\), unlike a Gaussian of variance \(1/2\), whose fourth moment would be \(3/4\).

**6. Vanishing density of zero modes.** Conditional on \(\mathcal B\), the variable \(X\) is normal with variance \(\int_0^1\mathcal B_s^2\,ds\), strictly positive almost surely. Hence \(X\) has no point mass at zero. For any \(\varepsilon>0\), the portmanteau theorem gives
\[
\limsup_{n\to\infty}\mathbb P\{W_n(\Xi_n)=0\}
\le\mathbb P\{|X|\le\varepsilon\}.
\]
Letting \(\varepsilon\downarrow0\) proves that \(4^{-n}\#\{\xi:W_n(\xi)=0\}\to0\), including the singular residue classes. This does not assert that there are no zeros at those widths.

## Verification
A standalone exact-integer script `checker.py` builds every order-ideal incidence indicator directly, applies the full Walsh--Hadamard transform for each \(1\le n\le8\), and independently builds the signed two-prefix dynamic-programming spectrum. The full histograms agree at all 87,380 frequency positions. In each length, zero/nonzero and least positive magnitude satisfy the theorem. The checker additionally runs the transfer recurrence through \(n=17\) and checks multiplicity totals against \(4^n\). These are finite consistency checks, not proofs of infinite assertions; the arguments above establish the all-width finite classification and limit law.

## Relationship to prior work
Erné--Heitzig--Reinhold (2002) study enumeration and construction of finite distributive lattices, providing the classical order-ideal setting, not a complete Walsh multiplier classification for their two-row product family. Sjöstrand (2003--2005) studies **sign-imbalances of standard Young tableaux**, namely signed linear extensions, rather than arbitrary coordinate-character signs summed over order-ideal incidence vectors. De Wolf (2008) surveys general Boolean-cube Fourier analysis, including the transform itself, without this spectral classification. Classical random-walk invariance principles and the Brownian harmonic-oscillator Laplace transform are used as **known tools**; the Brownian formula alone is not claimed new. The joint, explicitly normalized two-row order-ideal convolution theorem is the subject of this finding. Historical priority is not independently certified: an equivalent formula for character-weighted Ferrers diagrams or signed order ideals may exist outside the inspected literature.

## Limitations
No exact finite-width formula is established for the number of zero frequencies when \(n\equiv2,3\pmod4\), beyond the proof that it is positive and has vanishing relative density. No quantitative convergence rate, exact nonzero-multiplier distribution at finite width, or corresponding result for three or more rows is claimed. The historical comparison is bounded and no independent mathematical audit has been performed.

## References
- M. Erné, J. Heitzig, J. Reinhold, *On the Number of Distributive Lattices*, Electronic Journal of Combinatorics 9 (2002), #R24, published 2002-04-01, DOI 10.37236/1641.
- J. Sjöstrand, *On the sign-imbalance of partition shapes*, preprint first submitted 2003-09-15, arXiv:math/0309231, Journal of Combinatorial Theory A 111 (2005), 190--203.
- R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Graduate Surveys 1 (2008), DOI 10.4086/toc.gs.2008.001.
- Classical tools: Donsker's invariance principle, the Feynman--Kac formula, and Lévy's continuity theorem (used with their standard hypotheses as checked in the proof).
