# Rational inflection spectra of the cyclic-quartic generalized Legendre pencil

## Finding
For every prime power \(q\equiv3\pmod4\) of characteristic at least five, put \(k=\mathbb F_q\) and
\[
C_\lambda:\quad Y^4=XZ(X-Z)(X-\lambda Z),\qquad \lambda\in U(k),
\]
where \(U=\mathbb A^1\setminus\{0,1,-1,2,1/2\}\). Every \(C_\lambda\) is a smooth genus-three plane quartic with four \(k\)-rational hyperflexes of weight two and sixteen geometric ordinary flexes of weight one. The number of \(k\)-rational **distinct flex supports** is either four or twelve, never an intermediate value. Precisely
\[
M_q=\begin{cases}(q-11)/8,&q\equiv3\pmod8,\\(q+1)/8,&q\equiv7\pmod8\end{cases}
\]
of the \(q-5\) coefficient-marked parameters \(\lambda\in U(k)\) have twelve rational flex supports; the other \(q-5-M_q\) have four.

This counts marked coefficients, not curve isomorphism classes. In particular, for \(q=7\), \(\lambda=5\) has twelve rational flex supports and \(\lambda=3\) has four.

## Assumptions and scope
The characteristic is at least five and \(q\equiv3\pmod4\) (thus in practice the prime characteristic is at least seven and the extension degree is odd). The five omitted parameters are distinct under these assumptions. A flex support means a geometric point where the canonical tangent line has contact order at least three, counted once without its Weierstrass weight. The values four and twelve refer to \(k\)-rational supports on the **fixed plane model**. The geometric and arithmetic statements do not claim anything about the excluded harmonic members, nontrivial twists, the Jacobian's zeta function, or fields congruent to one modulo four.

## Proof
Write \(g_\lambda(x)=x(x-1)(x-\lambda)\) and
\[
Q_\lambda(x)=3x^4-4(\lambda+1)x^3+(4\lambda^2+2\lambda+4)x^2-4\lambda(\lambda+1)x+3\lambda^2.
\]
**1. Full inflection divisor.** The Hessian determinant of \(Y^4-XZ(X-Z)(X-\lambda Z)\) equals \(-36Y^2Q_\lambda(X,Z)\), with \(Q_\lambda(X,Z)\) the homogenization of the displayed quartic. Direct polynomial identities give
\[
\operatorname{disc}_x Q_\lambda=4096\lambda^2(\lambda-1)^2(\lambda+1)^2(\lambda-2)^2(2\lambda-1)^2,
\quad \operatorname{Res}_x(Q_\lambda,g_\lambda)=27\lambda^4(\lambda-1)^4.
\]
Thus for every allowed \(\lambda\), the four \(Q_\lambda\)-roots are distinct, finite and unramified over the \(x\)-line; each lifts to four distinct geometric ordinary flex points. The four branch points \((0,0,1),(1,0,1),(\lambda,0,1),(1,0,0)\) are rational hyperflexes, each with local tangent contact exactly four. Hessian--curve intersection has total length \(24=4\cdot2+16\), so these are all geometric flexes with the stated weights.

**2. The root-splitting criterion.** Over the rational-function field \(k(\lambda)\), three involutions of the \(x\)-line are
\[
A(x)=\frac\lambda x,\quad B(x)=\frac{x-\lambda}{x-1},\quad C(x)=\frac{\lambda(x-1)}{x-\lambda}.
\]
They form a Klein four-group and preserve the roots of \(Q_\lambda\). For example, \(x^4Q_\lambda(A(x))=\lambda^2Q_\lambda(x)\); the other two identities have multipliers \((\lambda-1)^2/(x-1)^4\) and \(\lambda^2(\lambda-1)^2/(x-\lambda)^4\). Their fixed-point equations have resultants with \(Q_\lambda\), respectively,
\[
16\lambda^2(\lambda-1)^2(\lambda+1)^2,\quad
16\lambda^2(\lambda-1)^2(\lambda-2)^2,\quad
16\lambda^2(\lambda-1)^2(2\lambda-1)^2.
\]
No nonidentity involution fixes a \(Q_\lambda\)-root on \(U\). Consequently this four-group acts regularly, and Frobenius permutes the roots via an element of this group.

For completeness, the cubic resolvent with pair-product roots \(z\) factors as
\[
(z-2\lambda)\left(z-\frac{2\lambda(2\lambda-1)}3\right)
\left(z-\frac{4-2\lambda}3\right).
\]
For each of its three roots, the square of the difference of the two pair sums is \(16D_i/9\), respectively, where
\[
D_1=-(\lambda-2)(2\lambda-1),\quad
D_2=(\lambda-2)(\lambda+1),\quad
D_3=-(\lambda+1)(2\lambda-1).
\]
The resolvent reconstruction, valid because no \(D_i\) vanishes on \(U\), shows that all four roots of \(Q_\lambda\) are rational exactly when \(D_1\) and \(D_2\) are nonzero squares. Equivalently, the independent two pair-sum differences are rational; their sums then recover each individual root.

**3. All-or-none rational ordinary flexes.** The transformations satisfy
\[
\frac{g_\lambda(A(x))}{g_\lambda(x)}=\frac{\lambda^2}{x^4},\quad
\frac{g_\lambda(B(x))}{g_\lambda(x)}=\frac{(\lambda-1)^2}{(x-1)^4},\quad
\frac{g_\lambda(C(x))}{g_\lambda(x)}=\frac{\lambda^2(\lambda-1)^2}{(x-\lambda)^4}.
\]
When \(Q_\lambda\) splits, the four nonzero values of \(g_\lambda\) at its roots therefore have the same quadratic character. Since \(q\equiv3\pmod4\), the fourth powers of \(k^\times\) are precisely its squares; any nonzero square has two fourth roots. It follows that there are either zero or eight rational ordinary flexes, and if \(Q_\lambda\) does not split there are none.

**4. Exact parameter census.** Let \(\chi\) be the quadratic character extended by \(\chi(0)=0\), and put \(c=\chi(-2)\). On \(U(k)\), the splitting criterion gives
\[
N_q=\frac14\sum_{\lambda\in U(k)}(1+\chi(D_1))(1+\chi(D_2)).
\]
The elementary quadratic-character identity \(\sum_{t\in k}\chi(at^2+bt+d)=-\chi(a)\) for nondegenerate quadratics and direct removal of the five excluded values give
\[
\sum_{U(k)}\chi(D_1)=\sum_{U(k)}\chi(D_2)
=\sum_{U(k)}\chi(D_1D_2)=-2c.
\]
Here \(D_1D_2=(\lambda-2)^2D_3\) and no factor vanishes on \(U\). Hence \(N_q=(q-5-6c)/4\), equal to \((q-11)/4\) for \(q\equiv3\pmod8\) and \((q+1)/4\) for \(q\equiv7\pmod8\).

Finally, the fixed-point-free parameter involution \(\lambda\mapsto1-\lambda\) preserves \(U\) and the splitting condition. It sends any root \(x\) of \(Q_\lambda\) to \(1-x\), a root of \(Q_{1-\lambda}\), while \(g_{1-\lambda}(1-x)=-g_\lambda(x)\). Because \(\chi(-1)=-1\), precisely half the \(N_q\) split parameters yield square values, hence eight rational ordinary flexes. This is \(M_q=N_q/2\), as claimed.

## Verification
The included `verify_legendre_flex.py` enumerates all generic parameters over every prime \(p\equiv3\pmod4\) through \(211\), compares the predicted and directly computed quartic-root splitting, computes fourth-power lifts, and verifies the exact parameter census. It prints `GENERALIZED_LEGENDRE_RATIONAL_FLEX_SPECTRUM_VERIFIED`. The included `verify_symbolic.py` reproduces the exact symbolic determinant, discriminant, resultant, resolvent, and rational-function identities using SymPy. These finite checks are consistency tests, not proofs of the uniform prime-power statement, which follows from Steps 1--4.

## Relationship to prior work
Babu and Venkataraman, *Group Action on Genus 3 Curves and their Weierstrass Points*, Section 2, explicitly identify the same quartic form and its generic four weight-two and sixteen weight-one Weierstrass points over an algebraically closed field. Their geometric information is presupposed and confirmed, not claimed as new. Goodson, *Hypergeometric Properties of Genus 3 Generalized Legendre Curves*, Section 5, studies the same pencil's periods, Hasse--Witt information and curve point counts, not the coefficient-marked frequency of rational flex supports. Recent calculations of the superspecial Hasse divisor of the same cyclic pencil concern a different invariant. The result here is the uniform arithmetic all-or-none flex phenomenon and its exact marked-parameter frequency, not a reclassification of geometric flex orbits.

## Limitations
The five excluded parameters may have a different geometric flex stratification. No statement is made for fields \(q\equiv1\pmod4\), other plane models or twists, or counts of isomorphism classes. Rational flex-support counts do not determine the curve zeta function. The mathematical proof is internal to the stated identities; finite tests are independent checks only. A mathematically equivalent but unindexed historical flex-splitting calculation could exist; no assertion of globally certified priority is made.

## References
1. H. Goodson, *Hypergeometric Properties of Genus 3 Generalized Legendre Curves*, arXiv:1705.02404 (first public 2017-05-05), Section 5. https://arxiv.org/abs/1705.02404
2. H. Babu and P. K. Venkataraman, *Group Action on Genus 3 Curves and their Weierstrass Points*, 2005, especially the discussion of the order-16 quartic and its Weierstrass points. https://www.academia.edu/4768194/Group_Actions_on_Genus_3_Curves_and_their_Weierstrass_Points
3. *The reduced superspecial divisor of the cyclic-quartic genus-three pencil at inert primes*, publicly indexed mathematical result (distinct invariant), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-reduced-superspecial-divisor-of-the-cyclic-quartic-genus-thr--8c80d021706e (only summary accessible during comparison).
