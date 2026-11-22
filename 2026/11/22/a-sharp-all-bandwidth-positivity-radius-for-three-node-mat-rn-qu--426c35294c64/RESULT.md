# A sharp all-bandwidth positivity radius for three-node Matérn quadrature

## Finding
Let \(k_t(x,y)=(1+t|x-y|)e^{-t|x-y|}\), \(t>0\), and let the integration measure be Lebesgue measure on \([-1,1]\). For the symmetric design \(X=\{-a,0,a\}\), \(0<a\le1\), define the unregularized optimal kernel-quadrature weights as \(w=K^{-1}b\), with \(K_{ij}=k_t(x_i,x_j)\) and \(b_i=\int_{-1}^1k_t(x_i,x)\,dx\).

**Theorem.** For every \(t>0\), both outer weights are strictly positive. All three weights are strictly positive for every \(t>0\) if and only if
\[
a\ge a_*=6-\sqrt{30}=0.522774424948\ldots.
\]
If \(0<a<a_*\), the central weight is strictly negative for all sufficiently small positive \(t\) and strictly positive for all sufficiently large \(t\). No claim is made about the number of intermediate zero crossings. This is an all-inverse-length-scale statement, not a claim for arbitrary site sets or measures.

## Assumptions and scope
The sites are distinct, the covariance is the exactly stated one-dimensional Matérn-\(3/2\) form with the positive inverse-scale parameter \(t\), and the exact Gram-system weights are used without a nugget or regularization. Multiplying the integration measure by a positive constant rescales every weight without changing signs. Strict positive definiteness on distinct sites guarantees invertibility of \(K\).

## Proof
Set \(c=(1+at)e^{-at}\), \(d=(1+2at)e^{-2at}\), and write \(b_0\) and \(b_a=b_{-a}\) for the kernel means. Direct integration gives
\[
b_0=\frac2t\left[2-(2+t)e^{-t}\right],\qquad
b_a=\frac1t\left[4-(2+t(1-a))e^{-t(1-a)}-(2+t(1+a))e^{-t(1+a)}\right].
\]
By symmetry \(w_{-a}=w_a\). Let \(\Delta=1+d-2c^2>0\), positive by the Schur complement of the strictly positive definite Gram matrix. Solving its two-orbit reduction yields
\[
w_0=\frac{(1+d)b_0-2cb_a}{\Delta},\qquad
w_a=w_{-a}=\frac{b_a-cb_0}{\Delta}.
\]

**Outer signs.** The numerator equals the integral over \(0\le x\le1\) of
\[
k_t(a-x)+k_t(a+x)-2k_t(a)k_t(x),
\]
where the first argument means the kernel evaluated at the displayed absolute distance. Put \(u=at>0\), \(v=xt\ge0\), and multiply the integrand by \(e^{u+v}>0\). On \(0\le v\le u\) this becomes
\[
F(v)=(1+u-v)e^{2v}-(1+u)-(1+2u)v.
\]
Here \(F(0)=F'(0)=0\) and \(F''(v)=4(u-v)e^{2v}\ge0\), with strict positivity in the interior. On \(v\ge u\), the rescaled integrand is the affine function
\[
(1+v-u)e^{2u}-(1+u)-(1+2u)v,
\]
whose slope \(e^{2u}-1-2u>0\) and whose value at \(v=u\) is positive. Thus the integrand is positive for every \(x>0\), and \(w_{\pm a}>0\).

**Central sign.** Let \(N=(1+d)b_0-2cb_a\) and \(H(t,a)=t e^{(1+2a)t}N\). Algebra gives the entire function
\[
H=4e^t(e^{at}-1)^2-8at e^t(e^{at}-1)
+2at(e^{2at}-1)+2a(1-a)t^2(e^{2at}-1).
\]
The Taylor coefficients through degree three vanish. The next three are
\[
[t^4]H=\frac{a^2}{3}(-a^2+12a-6),\quad
[t^5]H=\frac{a^2}{3}(-2a^3+11a^2-2),\quad
[t^6]H=\frac{a^2}{90}(-47a^4+180a^3+45a^2-15).
\]
Thus the fourth coefficient is nonnegative precisely when \(a\ge a_*\), since \(0<a\le1\), and is negative below that radius. The fifth- and sixth-degree bracket polynomials are strictly increasing on \((0,1]\), and both are positive at \(a_*\), hence positive for \(a\ge a_*\).

For integer \(j\ge7\), set \(P_j(a)=\frac{j!}{2}[t^j]H\). From the exponential identity,
\[
P_j=2[(1+2a)^j-2(1+a)^j+1]-4aj[(1+a)^{j-1}-1]
+aj(2a)^{j-1}+a(1-a)j(j-1)(2a)^{j-2}.
\]
The coefficients of \(a^0,a^1,a^3\) vanish, that of \(a^2\) is \(-2j(j-1)\), and for every \(4\le k\le j-2\), that of \(a^k\) is
\[
(2^{k+1}-4-4k)\binom jk>0.
\]
The coefficient of \(a^{j-1}\) is positive, the coefficient of \(a^j\) is negative, and their sum is
\[
2^{j-2}(6j+8)-4(j^2+j+1)>0\quad(j\ge7).
\]
Because \(a\le1\), these two highest-degree terms have positive sum. Discarding all other nonnegative terms therefore gives
\[
P_j(a)\ge -2j(j-1)a^2+12\binom j4 a^4>0
\]
whenever \(a^2>4/[(j-2)(j-3)]\). For \(j\ge7\), this right-side threshold is at most \(1/5\), while \(a_*^2>1/5\). Hence every Taylor coefficient of \(H\) of degree at least four is nonnegative for \(a\ge a_*\), with strictly positive higher coefficients even at equality. Absolute convergence of the entire exponential series shows \(H(t,a)>0\) for all \(t>0\), and hence \(w_0>0\).

For \(0<a<a_*\), its first nonzero coefficient \([t^4]H<0\), so \(w_0<0\) for all sufficiently small \(t>0\). Finally as \(t\to\infty\), \(c,d\to0\), while \(b_0\sim4/t\) and \(b_a\sim4/t\) for fixed \(0<a<1\); at \(a=1\), \(b_a\sim2/t\). Thus all weights eventually become positive. This completes the proof.

## Verification
A standalone exact-symbolic and high-precision checker is supplied as `matern32_three_node_checker.py`. Run `python matern32_three_node_checker.py` with Python, SymPy and mpmath. It checks the closed numerator identity, the low-order coefficients, the general coefficient formula for degrees 7 through 30, and forty independent high-precision three-by-three Gram solves with independently integrated kernel means. These finite checks are corroborative; the degree-uniform positivity proof is the algebraic coefficient argument above.

## Relationship to prior work
The Gaussian-process/sigma-point quadrature connection is described in Särkkä and collaborators' 2015 public preprint (arXiv:1504.05994). Karvonen, Kanagawa and Särkkä (arXiv:1812.08509, especially the discussion of Matérn examples and positive weights) studied kernel-quadrature weight positivity; their Matérn examples and symmetry reduction do not state this exact all-bandwidth three-site cutoff. A separately indexed finding about symmetric **Gaussian**-kernel three-node quadrature has cutoff \(a=1/\sqrt3\); it is neither the same covariance function nor an implication of this theorem. The current contribution is the sharp radius \(6-\sqrt{30}\), its necessity and its positivity certificate specific to Matérn-\(3/2\).

## Limitations
No statement is made for more than three sites, asymmetric sites, Gaussian integration measures, heterogeneous nuggets, other Matérn smoothness parameters, or full generality of integrand stability. Inaccessible or unindexed classical cardinal-function and radial-basis literature could contain an equivalent formula; complete priority is not certified. The property is strictly positivity of **exact unregularized Gram-system weights**, not merely positivity of an approximate feature truncation.

## References
- Särkkä and collaborators, *On the Relation between Gaussian Process Quadratures and Sigma-Point Methods*, arXiv:1504.05994, first public April 22, 2015. https://arxiv.org/abs/1504.05994
- Karvonen, Kanagawa and Särkkä, *On the Positivity and Magnitudes of Bayesian Quadrature Weights*, arXiv:1812.08509, first public December 20, 2018. https://arxiv.org/abs/1812.08509
