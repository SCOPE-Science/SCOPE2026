# Sharp square-root star deficit for nonnegative positive-definite Fourier kernels

## Finding

Let \(d\ge2\) be an integer, and let \(\mathcal P_d\) denote all real continuous functions \(f:\mathbb R^d\to[0,\infty)\) that are positive definite and satisfy \(f(0)=1\). Fix \(x_0=0\), \(x_j=\pi e_j\) for \(1\le j\le d\), and \(c=(-1,1,\ldots,1)\). Put
\[
Q_d=\inf_{f\in\mathcal P_d}\sum_{j,k=0}^d c_jc_k f(x_j-x_k).
\]
Then, for every \(d\ge2\),
\[
Q_d\ge d+1-2\sqrt d,
\]
and, for all sufficiently large \(d\), an explicit finite trigonometric polynomial gives
\[
Q_d\le d+1-2\sqrt d+O(1).
\]
The implicit constant is absolute. Consequently
\[
\lim_{d\to\infty}\frac{d+1-Q_d}{\sqrt d}=2,
\qquad
\lim_{d\to\infty}\frac{Q_d-(d-1)^2/(d+1)}{\sqrt d}=-2.
\]
The second statement quantifies the maximal signed-star violation of the former Hinrichs--Vybíral matrix lower bound, not an optimization over arbitrary point configurations or coefficient vectors.

## Assumptions and scope

Positive definite means that for every finite family \(y_1,\ldots,y_n\in\mathbb R^d\) and \(z_1,\ldots,z_n\in\mathbb C\), the form \(\sum_{j,k}\overline z_jz_k f(y_j-y_k)\) is nonnegative. In particular \(f(-t)=f(t)\) because the functions are real. Pointwise nonnegativity is a separate hypothesis. The points and signed coefficients are fixed exactly as above. A sharp leading-order asymptotic is claimed; neither the exact finite-dimensional optimum nor a universal additive constant is determined.

## Proof

**1. Universal bound.** For \(f\in\mathcal P_d\), write \(a_j=f(\pi e_j)\), \(b_{jk}=f(\pi(e_j-e_k))\) for distinct positive \(j,k\), \(S=\sum_{j=1}^d a_j\), and \(T=\sum_{j\ne k}b_{jk}\). The real Gram matrix of \(f\) is positive semidefinite. If \(u_0,\ldots,u_d\) are its Gram vectors, \(\|u_0\|^2=1\), \(\|\sum_{j=1}^d u_j\|^2=d+T\), and \(\langle u_0,\sum_{j=1}^d u_j\rangle=S\). Cauchy--Schwarz yields \(S\le\sqrt{d+T}\). Pointwise nonnegativity gives \(T\ge0\). Hence
\[
\sum_{j,k=0}^d c_jc_k f(x_j-x_k)
=d+1-2S+T\ge d+1-2\sqrt{d+T}+T
\ge d+1-2\sqrt d,
\]
because the final expression is increasing in \(T\ge0\) for \(d\ge2\).

**2. An even central Fourier layer.** For all sufficiently large integers \(d\), let \(X_d\) be the unique integer satisfying
\[
X_d\equiv d\pmod 4,\qquad \sqrt d-6\le X_d<\sqrt d-2.
\]
Set \(r=(d-X_d)/2\), which is even, and write \(X=X_d\). Then \(r=d/2+O(\sqrt d)\), \(X=\sqrt d-c_d\) with \(2<c_d\le6\), and \(0<X<\sqrt d\). Define
\[
\kappa_v=\frac1{\binom dv}\sum_{j=\max(0,v-d+r)}^{\min(v,r)}
(-1)^j\binom rj\binom{d-r}{v-j}\quad(0\le v\le d),
\qquad \varepsilon=\frac{d-X^2}{d^2-X^2}.
\]
In particular \(0<\varepsilon<1\). On \(y\in[-1,1]^d\) define the multiaffine polynomial
\[
P_d(y)=\varepsilon+\frac{1-\varepsilon}{\binom dr}
\sum_{\substack{A\subseteq\{1,\ldots,d\}\\|A|=r}}
\prod_{j\in A}y_j,
\qquad
f_d(t)=P_d(\cos t_1,\ldots,\cos t_d).
\]
Every cosine product is a finite nonnegative mixture of characters, so \(f_d\) is continuous and positive definite, with \(f_d(0)=1\). It remains to establish global pointwise nonnegativity of \(f_d\).

**3. All cube vertices are nonnegative.** A vertex \(y\in\{-1,1\}^d\) with exactly \(v\) negative signs has value \(P_d(y)=\varepsilon+(1-\varepsilon)\kappa_v\). Standard sampling-without-replacement identities yield
\[
\kappa_0=1,\quad \kappa_1=\frac Xd,\quad
\kappa_2=\frac{X^2-d}{d(d-1)},\quad
\kappa_3=\frac{X(X^2-3d+2)}{d(d-1)(d-2)}.
\]
Since \(r\) is even, complementing all signs gives \(\kappa_{d-v}=\kappa_v\). The definition of \(\varepsilon\) gives
\[
\varepsilon=\frac{-\kappa_2}{1-\kappa_2},\qquad
P_d(y)=\frac{\kappa_v-\kappa_2}{1-\kappa_2}.
\]
Thus vertices of weights \(2\) and \(d-2\) have value zero; weights \(0,1,d-1,d\) have positive values.

We verify positivity for weight \(3\), hence also \(d-3\). Uniformly for \(2<c_d\le6\), elementary expansion gives
\[
\kappa_2=-2c_d d^{-3/2}+O(d^{-2}),\quad
\kappa_3=-2d^{-3/2}+O(d^{-2}),\quad
\kappa_3-\kappa_2=2(c_d-1)d^{-3/2}+O(d^{-2})>0
\]
for all sufficiently large \(d\), with an absolute threshold.

For the remaining weights \(4\le v\le d-4\), let \(\chi_A\) denote the coordinate product character on \(\{-1,1\}^d\). Orthogonality of these characters implies the exact Krawtchouk Parseval identity
\[
\sum_{v=0}^d\binom dv\kappa_v^2
=\frac{2^d}{\binom dr}.
\]
Since \(r=d/2+O(\sqrt d)\), the central-binomial estimate and its adjacent-ratio product give \(\binom dr\ge C^{-1}2^d/\sqrt d\), with an absolute constant \(C\). Hence, using \(\binom dv\ge\binom d4\) throughout these middle weights,
\[
|\kappa_v|\le\sqrt{\frac{C\sqrt d}{\binom d4}}=O(d^{-7/4}).
\]
But \(-\kappa_2=2c_dd^{-3/2}+O(d^{-2})\ge4d^{-3/2}+O(d^{-2})\). Consequently \(\kappa_v>\kappa_2\) for the middle weights and all sufficiently large \(d\). All vertices therefore have nonnegative \(P_d\)-values. Multiaffine interpolation expresses \(P_d(y)\) on the cube as a convex combination of its vertex values, showing \(f_d(t)\ge0\) for every \(t\in\mathbb R^d\).

For completeness, the central-binomial lower estimate used above follows from Stirling's formula \(\binom d{\lfloor d/2\rfloor}\asymp2^d/\sqrt d\). Moving a distance at most \(C_0\sqrt d\) from the center multiplies this coefficient by a product of \(O(\sqrt d)\) adjacent binomial ratios each \(1-O(d^{-1/2})\), whose product stays bounded below by a positive absolute constant. No finite enumeration is used to justify this infinite-dimensional step.

**4. Sharp leading coefficient.** The one-minus and two-minus values of \(f_d\) simplify to
\[
a_d=f_d(\pi e_j)=\frac{X+1}{d+X},\qquad
b_d=f_d(\pi(e_j-e_k))=0\quad(j\ne k).
\]
Thus its signed star form equals
\[
q_d=d+1-2d\frac{X+1}{d+X}=d+1-2\sqrt d+O(1),
\]
since \(X=\sqrt d+O(1)\). The universal bound and \(Q_d\le q_d\) prove the first limit. The proposed comparison threshold equals \((d-1)^2/(d+1)=d+1-4d/(d+1)\), proving the second limit.

## Verification

The standalone file `CHECKER.py` evaluates the exact normalized Krawtchouk coefficients using integer binomial sums and rational arithmetic for a representative sequence of dimensions. It checks parity symmetry, all Boolean vertices, the weight-two zero, the one-minus value, the three low-degree closed forms, and the exact Parseval identity. The checks are supplementary; Step 3 establishes every sufficiently large dimension by uniform estimates, and Step 1 proves the universal bound for every \(d\ge2\).

## Relationship to prior work

Hinrichs and Vybíral (2011) proposed the positive-positive-definite matrix lower bound whose signed-star instance is quantified here. Vybíral (2026, arXiv:2609.21733), in a complete publicly available manuscript, exhibited one seven-dimensional violation and outlined the symmetric multiaffine linear-programming family; the text does not state a growing-dimensional asymptotic or a global optimum over all nonnegative positive-definite kernels. The present result gives the sharp leading-order global star deficit by pairing a universal Gram bound with a central-degree Krawtchouk construction. Vybíral's 2020 Schur-square theorem applies to the narrower family of kernels of the form \(|g|^2\), and so does not imply the claim for arbitrary nonnegative positive-definite functions. This is a comparison of statements, not a claim that absence from search guarantees priority.

## Limitations

This determines the first-order \(\sqrt d\)-scale only, not the exact finite-dimensional infimum, its optimizers, or the second-order constant. It concerns the fixed star and fixed signed coefficient vector, not arbitrary configurations. The construction is explicit for all sufficiently large dimensions but may not be extremal at each finite dimension. The proof is analytical and supplementary computations cannot certify literature novelty. Independent validation has not been performed.

## References

- A. Hinrichs and J. Vybíral, *On positive positive-definite functions and Bochner's theorem*, Journal of Complexity 27 (2011), 264–272. Author-hosted full text: https://people.fjfi.cvut.cz/vybirja2/publ/Vybiral19.pdf
- J. Vybíral, *A variant of Schur's product theorem and its applications*, Advances in Mathematics 368 (2020), 107140. Author-hosted full text: https://people.fjfi.cvut.cz/vybirja2/TUM-IBC/Vybiral_Advances.pdf
- J. Vybíral, *An explicit counterexample to the Hinrichs--Vybiral conjecture*, arXiv:2609.21733 (first public September 18, 2026). https://arxiv.org/abs/2609.21733
