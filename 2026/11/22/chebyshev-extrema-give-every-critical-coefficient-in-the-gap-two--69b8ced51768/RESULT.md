# Chebyshev extrema give every critical coefficient in the gap-two harmonic-trinomial family

## Finding

Let \(k\ge1\) be odd and \(n=k+2\). For real \(c>0\), consider the planar harmonic polynomial
\[
F_c(z)=z^{k+2}+c\overline z^{\,k}-1.
\]
A *critical coefficient* means a positive \(c\) for which \(F_c\) has a zero on its Jacobian-zero circle. Let \(U_k\) be the degree-\(k\) Chebyshev polynomial of the second kind, uniquely specified by
\[
U_k(\cos\theta)=\frac{\sin((k+1)\theta)}{\sin\theta},\qquad 0<\theta<\pi.
\]
Form the finite set of positive heights
\[
\mathscr H_k=\{k+1\}\ \cup\ \{U_k(x): -1<x<1,\ U_k'(x)=0,\ U_k(x)>0\}.
\]
It contains exactly \((k+1)/2\) distinct numbers. Writing them in strictly decreasing order \(h_1>\cdots>h_{(k+1)/2}>0\), **every** critical coefficient, without omission or duplication, is
\[
\boxed{c_j=\frac{k+2}{k}\left(\frac{k}{2h_j}\right)^{2/(k+2)},\quad 1\le j\le\frac{k+1}{2}.}
\]
Thus the entire coefficient-transition list is algebraic and computable from the real critical points of one explicitly specified integer polynomial. Away from these coefficients the number of distinct zeros is given by the previously established harmonic-trinomial counting theorem [1]. In particular, the counts begin at \(k+2\), jump by two at \(c_1\), then by four at each later coefficient, and end at \(3k+2\).

There is also a sharp large-degree statement. As \(k\to\infty\) through odd integers,
\[
\boxed{c_{(k+1)/2}-c_1=\frac{2\log k}{k}+O\!\left(\frac{(\log k)^2}{k^2}\right).}
\]
More precisely,
\[
c_1=1+\frac{2-2\log2}{k}+O(k^{-2}),\qquad
c_{(k+1)/2}=1+\frac{2+2\log(k/2)}{k}+O\!\left(\frac{(\log k)^2}{k^2}\right).
\]
For the illustrative case \(k=3\) and \(n=5\), the two coefficients are exactly
\[
c_1=\frac53\left(\frac38\right)^{2/5},\qquad
c_2=\frac53\left(\frac{9\sqrt6}{16}\right)^{2/5}=1.8946457081379975\ldots.
\]
The second value was bounded, but not explicitly evaluated, in [1, Example 1.2].

## Assumptions and scope

All exponents \(k\) are positive odd integers, so \(\gcd(k,k+2)=1\), as required by [1]. There are no other free coefficients: the coefficient of \(z^{k+2}\) is one, the antiholomorphic coefficient \(c\) is real positive, and the constant term is minus one. Criticality refers exactly to the coincidence of a zero with the Jacobian-zero circle, not to a zero lying on the unit circle. The zero counts asserted above apply on open parameter intervals, not at critical coefficients where singular roots occur.

## Proof

**1. Jacobian circle and real-axis crossings.** The Jacobian is
\[
J_{F_c}(z)=(k+2)^2|z|^{2k+2}-k^2c^2|z|^{2k-2}.
\]
For \(z\ne0\), it vanishes precisely when \(|z|=R\), where
\[
R^2=\frac{kc}{k+2}.
\]
On this circle, \(cR^k=(k+2)R^{k+2}/k\), hence
\[
F_c(Re^{i\theta})=R^{k+2}\left(e^{i(k+2)\theta}+\frac{k+2}{k}e^{-ik\theta}\right)-1.
\]
A circle crossing occurs exactly when the parenthesized expression is real and positive, with \(R^{k+2}\) its reciprocal.

**2. The Chebyshev derivative identity.** Put \(x=\cos\theta\). The imaginary part is proportional to
\[
k\sin((k+2)\theta)-(k+2)\sin(k\theta)
=-2\sin^3\theta\,U_k'(x).
\]
For \(0<\theta<\pi\), real-axis crossings therefore occur precisely at critical points of \(U_k\). At such a point,
\[
(k+1)\sin\theta\cos((k+1)\theta)=\cos\theta\sin((k+1)\theta).
\]
Using the angle-sum formulas, the real part of the parenthesized expression is exactly \(2U_k(x)/k\). For \(\theta=0,\pi\), direct substitution gives the same formula with \(U_k(1)=k+1\) and \(U_k(-1)=-(k+1)\), respectively. Consequently, every positive real-axis crossing is associated precisely with a member \(h\in\mathscr H_k\), and the reciprocal condition gives
\[
R^{k+2}=\frac{k}{2h},\qquad
c=\frac{k+2}{k}R^2
=\frac{k+2}{k}\left(\frac{k}{2h}\right)^{2/(k+2)}.
\]
This also proves the converse: each positive height produces a zero of \(F_c\) on the Jacobian circle at the displayed coefficient.

**3. Completeness and strict ordering.** For odd \(k\), \(U_k\) is odd, with \(k\) simple real zeros in \((-1,1)\). Strict interlacing gives exactly \(k-1\) simple critical points, all interior, in symmetric nonzero pairs \(\{x,-x\}\). Since \(U_k(-x)=-U_k(x)\), exactly one point in each pair has positive height. At every critical point the squared sine-cosine identity gives
\[
|U_k(x)|=\left(1-\frac{k(k+2)}{(k+1)^2}x^2\right)^{-1/2}.
\]
The modulus increases strictly with \(|x|\). Therefore the positive critical heights are pairwise different; each is strictly less than the endpoint height \(k+1\). This yields exactly \((k+1)/2\) distinct positive heights and exactly that many distinct coefficients. The pre-existing counting theorem [1, Theorem 1.1] establishes that the full real-positive family has precisely \((k+1)/2\) critical coefficients, with the stated zero-count jumps. Hence the exhibited list is exhaustive and ordered by decreasing height. No assertion is made about the number of distinct zeros *at* the singular coefficients.

**4. Large-degree width.** Let \(h_{\min}\) be the smallest positive height. For odd \(k\), the two zeros of \(U_k\) immediately adjacent to its central zero at \(x=0\) are at \(x=\pm\sin(\pi/(k+1))\). By Rolle's theorem there is one critical point in each intervening interval; these are the critical points nearest the origin. The preceding magnitude identity therefore yields
\[
1\le h_{\min}\le\sec\!\left(\frac{\pi}{k+1}\right)=1+O(k^{-2}).
\]
The highest height is \(h_1=k+1\). Substitution into the exact formula gives
\[
\log c_1=\log(1+2/k)+\frac{2}{k+2}\log\frac{k}{2(k+1)},
\]
and
\[
\log c_{(k+1)/2}=\log(1+2/k)+\frac{2}{k+2}\log\frac{k}{2h_{\min}}.
\]
Expanding these two identities uniformly, using \(\log h_{\min}=O(k^{-2})\), proves the two endpoint laws and their difference above. This is a proof of the asymptotic coefficient, not numerical extrapolation.

**5. The first nontrivial explicit example.** For \(k=3\), \(U_3(x)=8x^3-4x\). Its derivative vanishes at \(x=\pm1/\sqrt6\), and the positive interior critical height is \(8/(3\sqrt6)\). The height set is \(\{4,8/(3\sqrt6)\}\). Substituting these heights gives the displayed radical formulas.

## Verification

The standalone file `check.py` checks the trigonometric identity after conversion to Chebyshev polynomials, the real-part identity modulo \(U_k'\), the number and ordering of critical heights for odd \(k\le19\), their exact-angle correspondence, the \(k=3\) radical, and the predicted large-degree trend. It completed 164 finite diagnostics. Run with `python check.py` using Python 3 and SymPy. These tests support implementation consistency; the proof of the all-degree theorem is the analytic argument above.

## Relationship to prior work

Brilleslyper, Brooks, Dorff, Howell and Schaubroeck [1] prove the complete *number* and order of real-parameter transitions and ask explicitly for the exact interior coefficients \(c_j\) with \(1<j<N\), while providing only a bound for the last critical coefficient. This note takes their transition count and produces the Chebyshev-critical-value formula in the natural gap-two family; its large-degree logarithmic width and exact \(k=3\) second coefficient are additional results. Brooks, Dorff, Hudson, Pitts, Whiffen and Woodall [2] extend the parameter-count picture to complex coefficients, without the gap-two algebraic critical-height description. Barrera, Barrera and Navarrete [3] give a general Bohl-type zero-counting method; their later parameter-space work [4] analyzes trochoid loci and equal-radius zeros. These broader results concern counts and geometry, rather than the exact full list and its large-degree clustering law. Priority beyond the inspected sources is not certified.

## Limitations

This result applies only to the gap-two, real-positive-coefficient subfamily with odd antiholomorphic exponent. It does not yield radical expressions for arbitrary degrees: the exact critical values are specified algebraically through all positive extrema of a Chebyshev polynomial. It invokes the established zero-count jump theorem [1] instead of proving all global winding-number facts anew. It does not classify zeros at singular transition coefficients, complex-parameter transitions, or the geometry of all individual roots. A broader equivalent derivation elsewhere in the literature remains a residual priority risk. No independent mathematical validation has been performed.

## References

[1] M. Brilleslyper, J. Brooks, M. Dorff, R. Howell, and L. Schaubroeck, *Zeros of a one-parameter family of harmonic trinomials*, Proc. Amer. Math. Soc. Ser. B 7 (2020), 82–90, published 17 June 2020, https://doi.org/10.1090/bproc/51 ; open text https://pdfs.semanticscholar.org/e1be/17dcd3e27784b5ba170c14e1ed7de09c5681.pdf .

[2] J. Brooks, M. Dorff, A. Hudson, E. Pitts, C. Whiffen, and A. Woodall, *Zeros of a family of complex-valued harmonic trinomials*, Bull. Malays. Math. Sci. Soc. 45 (2022), 1079–1091, https://weusemath.org/wp-content/uploads/2023/05/JB-BDHPWW-ZerosofaFamily.pdf .

[3] G. Barrera, W. Barrera, and J. P. Navarrete, *On the number of roots for harmonic trinomials*, J. Math. Anal. Appl. 514 (2022), 126313, first posted December 2021, https://arxiv.org/pdf/2112.06703 .

[4] W. Barrera, L. Campa, and J. P. Navarrete, *On the parameter spaces of harmonic trinomial equations*, arXiv:2602.11296, first posted 11 February 2026, https://arxiv.org/pdf/2602.11296 .
