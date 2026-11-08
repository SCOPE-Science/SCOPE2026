# Exact restricted Gaussian hypercontractivity across the first two Wiener chaoses

## Finding
For every positive integer \(d\), the centered real Gaussian polynomials of degree at most two form the \(T_\rho\)-invariant subspace \(\mathcal Q_d\). The exact fourth power of the \(L^2\)-to-\(L^4\) operator norm of the Ornstein--Uhlenbeck noise operator on this subspace is independent of dimension. With \(r=\rho^2\in[0,1]\), it equals
\[
M(r)=\begin{cases}
3r^2,&0\le r\le 1/5,\\
\dfrac{60r^4}{10r-1-5r^2},&1/5<r\le1.
\end{cases}
\]
The maximizing structure changes at \(r=1/5\) from purely first chaos to rank-one aligned mixtures of the first and second chaoses. The restricted semigroup is \(L^2\)-to-\(L^4\) contractive exactly when \(\rho^2\le r_*\), where \(r_*\) is the unique root in \((1/5,1)\) of
\[
60r^4+5r^2-10r+1=0.
\]
The numerical values are \(r_*=0.45164410203579086\ldots\), \(\rho_*=0.6720447172888058\ldots\), and \(s_*=-\frac12\log r_*=0.397430397088381\ldots\), where \(\rho=e^{-s}\). The classical unrestricted Nelson sufficient time \(\frac12\log3=0.549306\ldots\) is strictly larger.

## Assumptions and scope
The standard Gaussian law \(\gamma_d\) on \(\mathbb R^d\) is the product of independent standard normals. Every real-valued, centered polynomial of total degree at most two has the unique representation
\[
f(G)=L(G)+Q(G),\qquad L(G)=v\cdot G,\qquad Q(G)=G^{\mathsf T}AG-\operatorname{tr}A,
\]
for \(v\in\mathbb R^d\) and a real symmetric \(d\times d\) matrix \(A\). It has \(\mathbb Ef=0\) and \(\|f\|_2^2=\|v\|_2^2+2\operatorname{tr}(A^2)\). For \(0\le\rho\le1\), define \(T_\rho f=\rho L+\rho^2Q\), the restriction of the Gaussian Ornstein--Uhlenbeck/Mehler operator. The operator norm is \(\sup_{f\in\mathcal Q_d,\ f\ne0}\|T_\rho f\|_4/\|f\|_2\), and \(M(\rho^2)\) is its fourth power.

At \(\rho=0\), the operator vanishes and every nonzero input has zero output. When \(0<r\le1/5\), all norm extremizers are exactly nonzero linear forms \(v\cdot G\). When \(1/5<r<1\), write \(u\) for a unit vector. Every extremizer is, up to a nonzero scalar, exactly of the form
\[
f(G)=\alpha(u\cdot G)+\beta((u\cdot G)^2-1),\qquad \alpha\beta\ne0,
\qquad \frac{\alpha^2}{\alpha^2+2\beta^2}=\frac{5r(1-r)}{10r-1-5r^2}.
\]
There is no constraint on the relative sign of \(\alpha\) and \(\beta\). At \(r=1\), all extremizers are precisely nonzero multiples of \((u\cdot G)^2-1\) with \(\|u\|_2=1\). For every fixed positive dimension, the sharp operator norm and its contractivity threshold are identical.

## Proof
Set \(a^2=\|v\|_2^2\), \(h=\operatorname{tr}(A^2)\), \(q_4=\operatorname{tr}(A^4)\), and \(j=v^{\mathsf T}A^2v\). Wick's formula or direct diagonalization and one-dimensional Gaussian moments give the **exact identities**
\[
\mathbb E L^4=3a^4,\quad
\mathbb E(L^2Q^2)=2a^2h+8j,\quad
\mathbb E Q^4=12h^2+48q_4.
\]
All odd mixed terms in the expansion of \(\mathbb E(\rho L+\rho^2Q)^4\) vanish by parity. Thus
\[
\mathbb E (T_\rho f)^4
=3r^2a^4+r^3(12a^2h+48j)+r^4(12h^2+48q_4).
\]
By diagonalizing \(A\),
\[
0\le a^2h-j,\qquad 0\le h^2-q_4.
\]
If \(A\ne0\), equality in the second inequality forces \(A\) to have rank one; if also \(v\ne0\), equality in the first then forces \(v\) to lie along its unique nonzero eigendirection. These conditions can be met simultaneously, in any dimension, by \(A=\beta uu^{\mathsf T}\) and \(v=\alpha u\).

For nonzero \(f\), define \(N=\|f\|_2^2=a^2+2h\) and the first-chaos energy fraction \(w=a^2/N\in[0,1]\). Using the two inequalities yields
\[
\frac{\|T_\rho f\|_4^4}{\|f\|_2^4}\le U_r(w):=3r^2w^2+30r^3w(1-w)+15r^4(1-w)^2.
\]
Every \(w\in[0,1]\) is realized with equality using aligned rank-one coefficients, so the scalar maximum equals the operator norm to the fourth power, not merely an upper bound.

The derivative at \(w=1\) is \(6r^2(1-5r)\); the derivative at \(w=0\) is \(30r^3(1-r)\). Hence for \(0<r\le1/5\) the maximum is at \(w=1\), with value \(3r^2\). For \(1/5<r<1\), \(U_r\) is strictly concave, because its quadratic coefficient equals \(-3r^2(10r-1-5r^2)\), and its unique maximizer lies in \((0,1)\):
\[
w_*(r)=\frac{5r(1-r)}{10r-1-5r^2},\qquad
U_r(w_*(r))=\frac{60r^4}{10r-1-5r^2}.
\]
The same endpoint formula holds at \(r=1\), where \(w_*(1)=0\). This gives all equality cases by the spectral equality conditions.

In addition, for \(1/5<r\le1\) there is the **exact nonnegative stability identity**
\[
\begin{aligned}
M(r)-\frac{\|T_\rho f\|_4^4}{\|f\|_2^4}
={}&3r^2(10r-1-5r^2)(w-w_*)^2\\
&+\frac{48r^3}{N^2}(a^2h-j)
+\frac{48r^4}{N^2}(h^2-q_4).
\end{aligned}
\]
The three summands control, respectively, level-energy displacement, directional misalignment, and departure from rank one. Their joint zeros reproduce the complete equality classification.

Finally, \(M(r)\) is strictly increasing on \((0,1]\): each nonzero input has a positive fourth-moment polynomial in \(r\) with nonnegative coefficients after expressing the mixed term as \(6\mathbb E L^2Q^2\), and the sharp maximum is attained. Since \(M(1/5)=3/25<1\) and \(M(1)=15>1\), the contractivity threshold is unique in \((1/5,1)\). On that interval \(M(r)=1\) is equivalent to \(60r^4+5r^2-10r+1=0\); rational substitution shows a sign change between \(45164/100000\) and \(45165/100000\). The exact threshold and numerical approximations follow.

## Verification
The standalone `verify.py` checks the scalar optimization and stability polynomial identities symbolically, verifies the quartic threshold using exact rational brackets, and independently integrates Gaussian monomials for one-variable symbolic coefficients and six nontrivial multivariate matrices (including the three-dimensional case). It checks rank-one equality patterns. Execute `python verify.py` with Python 3 and SymPy installed. Its successful final diagnostic is `ALL_GAUSSIAN_QUADRATIC_HYPERCONTRACTIVITY_CHECKS_PASSED`. The proof for all dimensions and all real coefficient data is the Wick/spectral argument above; finite checks do not replace it.

## Relationship to prior work
The Nelson--Gross Gaussian hypercontractive inequality, as discussed in Bakry--Bolley--Gentil (arXiv:1003.5072, Section 1 and Section 3), gives \(\|T_\rho f\|_4\le\|f\|_2\) for all Gaussian \(L^2\) inputs when \(\rho\le1/\sqrt3\). The present norm on the invariant, centered degree-at-most-two subspace remains at most one over the strictly larger interval \(\rho\le\sqrt{r_*}\). The classical bound does not specify the extremizing mixtures or the second spectral threshold at \(r=1/5\).

Adamczak--Wolff (arXiv:1304.1826, Theorem 1.1 and surrounding discussion) provides moment estimates for Gaussian polynomial chaoses up to constants depending on degree, not the exact restricted OU operator norm and all equality cases. Pang (arXiv:2609.05914, Theorem 1.1) establishes sharp moments for **pure centered quadratic Gaussian forms** with rank-one maximizers; this covers the pure second-chaos endpoint, which is not asserted as new here. That pure-level bound does not determine the strict interior first-plus-second-chaos maximum for \(1/5<r<1\). A separate earlier result for trace-free quadratic forms with linear perturbations imposes \(\operatorname{tr}A=0\), excludes the rank-one extremizers here, and does not address the weighted semigroup norm.

## Limitations
The result concerns real Gaussian coefficients, mean-zero input polynomials of total degree at most two, fourth-moment output norms, and the standard finite-dimensional isotropic Gaussian law. It does not classify arbitrary nonzero constants added to the input, complex coefficients, other exponent pairs, or higher Wiener-chaos levels. No claim is made about independent verification or priority beyond the compared sources. The rank-one fourth-moment endpoint for pure centered quadratics is known; the distinct contribution is the complete mixed-level semigroup curve, threshold, extremizers and stability identity.

## References
- D. Bakry, F. Bolley, I. Gentil, *Dimension dependent hypercontractivity for Gaussian kernels*, arXiv:1003.5072v1 (first public version 26 March 2010), https://arxiv.org/abs/1003.5072.
- R. Adamczak, P. Wolff, *Concentration inequalities for non-Lipschitz functions with bounded derivatives of higher order*, arXiv:1304.1826v1 (5 April 2013), https://arxiv.org/abs/1304.1826.
- Z. Pang, *A Gamma envelope and sharp moment inequalities for Gaussian quadratic forms*, arXiv:2609.05914v1 (5 September 2026), https://arxiv.org/abs/2609.05914.
- E. Nelson, *The free Markoff field*, Journal of Functional Analysis 12 (1973), 211–227 (classical hypercontractive theorem, as quoted in the above primary sources).
