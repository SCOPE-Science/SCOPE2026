# Characteristic-five canonical nonclassicality and the complete Weierstrass divisor of genus-five Humbert curves

## Finding
Let \(C\) be any smooth generalized Fermat curve of type \((2,4)\) over an algebraically closed field of characteristic \(5\), and \(\pi:C\to\mathbb P^1\) its elementary abelian cover of degree \(16\). There are five distinct branch values. Put one at infinity, denote the four finite branch values by \(a_1,\ldots,a_4\), and set \(f(X)=\prod_{i=1}^4(X-a_i)\). Its **generic canonical Hasse order sequence** is
\[ (0,1,2,3,5). \]
The intrinsic canonical Hasse-Wronskian, with this nonclassical order sequence, has divisor
\[
\boxed{\operatorname{div}(\mathcal W_K)
=2\sum_{P\in\pi^{-1}(\{a_1,a_2,a_3,a_4,\infty\})}P
+\pi^*\operatorname{div}_0(f').}
\]
The first term is the **reduced** branch-point sum, multiplied by two; it must not be confused with twice the full ramified pullback of the branch divisor. Here \(f'\) is the ordinary formal derivative in characteristic five. Every ramification point has Wronskian weight \(2\); all remaining Wronskian points are precisely the unramified points over the critical divisor of the degree-four polynomial \(f\), each weighted by the corresponding multiplicity of \(f'\).

Thus the canonical Wronskian has degree \(128\), and the numbers of distinct Weierstrass points are precisely \(88\) for \((1,1,1)\), \(72\) for \((2,1)\), and \(56\) for \((3)\). All three possibilities occur on smooth curves. In particular, the classical statement that the genus-five Humbert curve has forty Weierstrass points, each of weight three, does not extend unchanged to characteristic five.

## Assumptions and scope
The field \(k\) is algebraically closed of characteristic exactly \(5\). The five branch values are pairwise distinct. Equivalently \(C\) is the smooth connected normalization of the projective curve with affine function field
\[
k(C)=k(X,Y_1,Y_2,Y_3,Y_4),\qquad Y_i^2=X-a_i\quad(1\le i\le4).
\]
This degree-\(16\) Kummer extension is separable, with group \((\mathbb Z/2)^4\). Riemann–Hurwitz gives \(2g-2=-32+5\cdot8=8\), so \(g=5\). The four finite branch values and infinity each have exactly eight geometric points in the fiber; the other fibers have sixteen. Canonical Weierstrass weights throughout mean orders of the Hasse-Wronskian defined using the *generic order sequence*, not a characteristic-zero ordinary-jet determinant.

## Proof
**Canonical basis.** Write \(H=dX/(Y_1Y_2Y_3Y_4)\). At a finite ramification point, a uniformizer is \(t=Y_j\), and \(dX=2t\,dt\), so \(H\) and \(Y_iH\) are regular. At any point over infinity, choose \(t=1/Y_1\): then \(X=a_1+t^{-2}\), \(Y_i=t^{-1}(1+O(t^2))\), and \(H=t\cdot\mathrm{unit}\,dt\). Consequently \(H,Y_1H,\ldots,Y_4H\) are five regular independent one-forms, hence a full basis of \(H^0(C,K_C)\).

**Generic Hasse order.** On the generic unramified \(X\)-chart, trivialize the basis by \(H\). For \(r\ge0\), Hasse differentiation gives
\[
D_X^{(r)}Y_j=\binom{1/2}{r}Y_j(X-a_j)^{-r}.
\]
In characteristic five, the coefficients at indices \(r=0,1,2,3,4,5\) are respectively \(1,3,3,1,0,2\). Thus the first four nontrivial Hasse-jet rows are indexed by \(1,2,3,5\), and the order \(4\) row vanishes. Put \(u_j=(X-a_j)^{-1}\). Removing the constant section and factoring the nonzero binomial constants and the \(Y_j\) leaves the alternant
\[
\det(u_j^{r})_{r\in\{1,2,3,5\},1\le j\le4}
=\biggl(\prod_j u_j\biggr)
 \prod_{i<j}(u_j-u_i)\biggl(\sum_j u_j\biggr).
\]
This integer-polynomial identity is a Vandermonde times the first elementary symmetric polynomial. Since \(\sum_j u_j=f'/f\) and the four \(a_j\) are distinct, the canonical Hasse-jet determinant is a nonzero constant multiple of
\[
(\prod_jY_j)\frac{f'(X)}{f(X)^5}.
\]
The derivative \(f'\) has degree three with nonzero leading coefficient \(4\) in characteristic five. The determinant is therefore generically nonzero and the claimed generic Hasse order sequence is established; no finite-point sampling is used for this assertion.

**Divisor at unramified points.** The canonical Wronskian is a global section of \(K_C^{\otimes(5+0+1+2+3+5)}=K_C^{\otimes16}\), with local coefficient proportional to \((H/dX)^5(\prod Y_j)f'/f^5\) in the local parameter \(X\). Away from the branch values, all factors except \(f'\) are units; hence the Wronskian vanishes with multiplicity equal to \(\operatorname{ord}_X(f')\) at every point over a zero of \(f'\).

**Finite branch values.** At a point over \(X=a_j\), take \(t=Y_j\). Then \(H/dt\) is a unit, \(dX/dt\) has valuation \(1\), and \((\prod Y_i)f'/f^5\) has valuation \(1-10=-9\). By the Hasse-Jet coordinate transformation law, the Wronskian coefficient relative to \(dt^{\otimes16}\) has valuation \(5\cdot0+11\cdot1-9=2\). This is also confirmed directly: the four even local canonical sections have vanishing orders \(0,2,4,6\) by their distinct branch constants, and the odd section has order \(1\); their local sequence \((0,1,2,4,6)\) has excess \(2\) over the generic sequence.

**Infinity.** At each point over infinity use \(t=1/Y_1\). The valuations are \(\operatorname{ord}_t(H/dt)=1\), \(\operatorname{ord}_t(dX/dt)=-3\), and \(\operatorname{ord}_t((\prod Y_j)f'/f^5)=30\); thus its Wronskian valuation is \(5-33+30=2\). This agrees with the direct local sequence \((0,1,2,4,6)\).

**Exhaustion and classification.** The five ramified fibers contribute \(5\cdot8\cdot2=80\). As \(f'\) has degree three, its full unramified inverse image contributes \(16\cdot3=48\), for total \(128\). This also equals \(\deg(K_C^{\otimes16})=16(2g-2)\), ruling out any additional zeros. The zeros of \(f'\) are disjoint from those of \(f\), since \(f\) is squarefree; a cubic has exactly the three indicated root-multiplicity patterns. Therefore the number of distinct points is \(40+16\cdot3=88\), \(40+16\cdot2=72\), or \(40+16\cdot1=56\), respectively.

All types exist already with coefficients in \(\mathbb F_5\): the respective smooth quartics may be taken as \(f(X)=X^4+X+1\), \(f(X)=X^4+2X^3+1\), and \(f(X)=X^4+1\). Their formal derivatives have distinct, double-plus-simple, and triple roots over \(\overline{\mathbb F}_5\), respectively, and each quartic is squarefree. Each defines the stated Humbert cover after passage to the algebraic closure.

## Verification
The accompanying independent-arithmetic, exact-algebra script `verify_humbert.py` uses only the Python standard library. It checks the 24-term four-variable alternant identity as a formal polynomial identity over the integers, verifies the six initial Hasse binomial coefficients modulo five, and checks squarefreeness and the derivative-gcd multiplicity patterns of all three explicit quartics over \(\mathbb F_{25}\). The script reports `ALTERNANT_POLYNOMIAL_IDENTITY_OK`, `BINOMIAL_COEFFICIENTS_MOD5_OK`, and `ALL_THREE_WRONSKIAN_SUPPORT_PATTERNS_OK`. The global divisor assertion is established by the local valuation argument above; finite computation alone is not asserted to prove it.

## Relationship to prior work
Hidalgo and Leyton-Álvarez, arXiv:1409.6258 (first posted 2014-09-22), study generalized Fermat hyperosculating points and Weierstrass weights for compact complex curves. Their type-\((2,4)\) example has classical canonical weights. Kato (2015) and Edge (1969) likewise describe the forty canonical Weierstrass points of the genus-five Humbert curve in characteristic zero. Hidalgo–Kontogeorgis–Leyton-Álvarez–Paramantzoglou, arXiv:1409.3063 (2014), develops generalized Fermat curve geometry over positive characteristics but its abstract hyperosculation assertion is subject to a characteristic bound and does not supply this characteristic-five Wronskian formula. The present finding instead concerns the exceptional Hasse-order phenomenon in characteristic five, its full intrinsic Wronskian divisor, and the resulting three exhaustive distinct-point counts. Related later work on Jacobian p-ranks of genus-five Humbert curves investigates a different invariant; p-rank data do not imply this divisor computation. No claim of an exhaustive historical-priority search is made.

## Limitations
The field is algebraically closed of characteristic exactly five; this theorem does not determine arithmetic Frobenius orbit counts over individual finite fields, nor all Weierstrass semigroups. The trichotomy is for distinct geometric Wronskian support points, not for the scheme degree, which is always \(128\). Earlier papers with inaccessible complete text might contain a version of the characteristic-five Hasse-Wronskian formula. There is no independent mathematical audit.

## References
- R. A. Hidalgo and M. Leyton-Álvarez, *Weierstrass weight of the hyperosculating points of generalized Fermat curves*, arXiv:1409.6258 (first preprint 2014-09-22), https://arxiv.org/abs/1409.6258.
- R. A. Hidalgo, A. Kontogeorgis, M. Leyton-Álvarez, P. Paramantzoglou, *Automorphisms of the Generalized Fermat curves*, arXiv:1409.3063 (2014), https://arxiv.org/abs/1409.3063.
- T. Kato, *A curve of genus 5 having 24 Weierstrass points of weight 5*, Hokkaido Math. J. 44 (2015), 165–173, https://www.math.sci.hokudai.ac.jp/hmj/page/44-2/pdf/HMJ44_165-173.pdf.
- W. L. Edge, *Three Plane Sextics and their Automorphisms*, Canadian Journal of Mathematics (1969), https://doi.org/10.4153/CJM-1969-139-6.
