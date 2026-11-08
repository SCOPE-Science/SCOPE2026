# Two sharp Radau IIA positivity thresholds on rectangular rook graphs

## Finding

Let \(p,q\ge2\) be integers, \(G=K_p\square K_q\) the unweighted rectangular rook graph (equivalently, the line graph of \(K_{p,q}\)), and \(L\) its combinatorial Laplacian. Set
\[
R(z)=\frac{6-2z}{z^2+4z+6},\qquad T_{p,q}(h)=R(hL),\quad h\ge0.
\]
Here \(R\) is the scalar heat-decay stability function of the two-stage, third-order Radau IIA method. The following statements hold simultaneously.

**Theorem.** For every \(p,q\ge2\):

1. The completed numerical transition \(T_{p,q}(h)\) is entrywise nonnegative for **every** \(h\ge0\) if and only if \(pq\le12\). For those and only those seven unordered pairs \((p,q)=(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4)\), every entry is strictly positive whenever \(h>0\).
2. For all \(p,q\ge2\) and every \(h>0\), transition entries between vertices which differ in **both** coordinates are strictly positive. For \(pq\ge13\), every diagonal entry is strictly negative at the explicit timestep \(h=12/(p+q)\).
3. For **square** rook graphs \(p=q=m\ge2\), entries between two distinct vertices which differ in exactly one coordinate remain strictly positive for all \(h>0\) if and only if \(m\le37\). For every \(m\ge38\), all such adjacent entries are negative at \(h=15/m\) and, more precisely, are negative exactly between two distinct positive roots of an explicit cubic in \(z=mh\).

In all cases \(T_{p,q}(h)\mathbf1=\mathbf1\), so negativity in this statement is a positivity-preservation failure rather than a loss of total mass. No claim is made that the diagonal and adjacent negative-time intervals coincide, or that all adjacent entries on a nonsquare rectangular graph stay positive.

## Assumptions and scope

The graph has vertex set \([p]\times[q]\). Two distinct vertices are adjacent exactly when one coordinate agrees. Each edge has unit conductance and \(L=\deg-A\) is the *unscaled*, positive semidefinite Laplacian. The rational matrix function is formed by its real symmetric functional calculus; its denominator is invertible because every Laplacian eigenvalue is nonnegative and \(z^2+4z+6>0\) for \(z\ge0\). The statements are exact over integers \(p,q\) and real timesteps \(h\), with a strict/non-strict distinction at \(h=0\).

## Proof

Put \(P_r=\mathbf1\mathbf1^\top/r\), \(Q_r=I_r-P_r\). Since \(L(K_r)=rQ_r\), the four mutually orthogonal projectors of \(L\) are
\[
P_p\otimes P_q,\quad Q_p\otimes P_q,\quad P_p\otimes Q_q,\quad Q_p\otimes Q_q,
\]
with respective eigenvalues \(0,p,q,p+q\). Write \(u=R(ph)\), \(v=R(qh)\), \(w=R((p+q)h)\). Every entry of \(pq T_{p,q}(h)\) is exactly one of
\[
\begin{aligned}
D&=1+(p-1)u+(q-1)v+(p-1)(q-1)w&&\text{(same vertex)},\\
E_p&=1-u+(q-1)(v-w)&&\text{(first coordinate differs)},\\
E_q&=1-v+(p-1)(u-w)&&\text{(second coordinate differs)},\\
F&=1-u-v+w&&\text{(both coordinates differ)}.
\end{aligned}
\]
Thus these four scalar expressions are also an **exact timestep-by-timestep decision procedure** for entrywise positivity for arbitrary unequal \(p,q\).

For \(d(z)=z^2+4z+6\), the common denominator \(d(ph)d(qh)d((p+q)h)\) is strictly positive. Direct polynomial expansion gives
\[
\begin{aligned}
&d(ph)d(qh)d((p+q)h)F\\
&=p^2q^2(p+q)^2h^6+2pq(p+q)(3p^2+7pq+3q^2)h^5\\
&\quad+12pq(4p^2+9pq+4q^2)h^4+180pq(p+q)h^3+216pqh^2.
\end{aligned}
\]
This is strictly positive at every positive timestep. Hence distance-two entries never cause a positivity failure.

For the seven unordered pairs with \(pq\le12\), substitution into the same four numerators yields polynomials with nonnegative coefficients and at least one positive nonconstant coefficient for each \(E_p,E_q,F\). The diagonal polynomial \(d(ph)d(qh)d((p+q)h)D\) has a *strict* positivity certificate on the entire positive axis: all degree-six Bernstein coefficients are positive on each of \([0,1]\), \([1,3/2]\), and \([3/2,2]\), and all coefficients after the translation \(h=2+t\), \(t\ge0\), are positive. There are precisely seven unordered parameter pairs in this range. The exact, standalone verifier computes all \(147\) Bernstein coefficients and the translated polynomial certificates with rational arithmetic. Since the Bernstein basis is nonnegative on each indicated compact interval and sums to one, these certificates prove strict positivity for all \(h\ge0\) for the diagonal numerator.

Conversely, at \(h=12/(p+q)\), direct substitution gives
\[
D=-\frac{pq\,\mathcal P(p,q)}{11(p^2+10pq+33q^2)(33p^2+10pq+q^2)},
\]
where
\[
\begin{aligned}
\mathcal P(p,q)={}&33(p^4+q^4)+340pq(p^2+q^2)+1190p^2q^2\\
&-384(p^3+q^3)+384pq(p+q)\\
&-4368(p^2+q^2)-14496pq.
\end{aligned}
\]
The polynomial \(\mathcal P(p_0+a,q_0+b)\) has **strictly positive coefficients** in \(a,b\) at each of the three base points \((p_0,q_0)=(2,7),(3,5),(4,4)\), as verified by a complete exact binomial expansion in the attached checker. Symmetry allows \(p\le q\). Every integer pair with \(pq\ge13\) lies in one of the three corresponding positive quadrants: \(p=2,q\ge7\); \(p=3,q\ge5\); or \(4\le p\le q\). Consequently \(\mathcal P(p,q)>0\), and the claimed diagonal failure follows. This proves the first two assertions including their sharpness.

For the square case write \(p=q=m\) and \(z=mh\). Both adjacent-entry expressions coincide and equal
\[
E_m(z)=1+(m-2)R(z)-(m-1)R(2z).
\]
A direct exact expansion yields
\[
E_m(z)d(z)d(2z)=4z^4+(36-4m)z^3+(18m+36)z^2+36mz.
\]
Moreover,
\[
R(z)-R(2z)=-\frac{z(z-6)(2z+3)}{d(z)(2z^2+4z+3)}.
\]
For \(0<z\le6\), this difference is nonnegative and \(R(z)<1\), hence \(E_m(z)>0\) for every \(m\ge2\). For \(z>6\), the difference is negative, so \(E_m(z)\ge E_{37}(z)\) for \(m\le37\). The crucial universal certificate is
\[
E_{37}(z)d(z)d(2z)=2z\bigl(2z(z-15)^2+4z^2-99z+666\bigr)>0,
\]
since \(4z^2-99z+666\) has positive leading coefficient and negative discriminant \(-855\). Thus adjacent entries remain strictly positive for every \(m\le37\).

For \(m\ge38\), at \(z=15\) the numerator equals \(-810(11m-410)<0\). Upon division by the positive factor \(4z\), this numerator becomes the cubic
\[
C_m(z)=z^3+(9-m)z^2+\left(\frac92m+9\right)z+9m.
\]
It is positive at \(z=0\) and for all sufficiently large \(z\), and negative at \(z=15\). Hence it has at least two distinct positive roots. Its coefficient sign sequence for \(m\ge38\) is \(+,-,+,+\), so Descartes' rule permits at most two positive roots counted with multiplicity. The two roots are simple and exhaust all positive roots, proving the exact single negative interval. This completes the proof.

## Verification

Run `python3 verify.py` with Python 3 (no external dependencies). Its exact checks include a formal three-variable polynomial identity for distance-two entries; the complete positive Bernstein and translated-polynomial certificates for the seven low-order graphs; positive-coefficient binomial expansions on all three unbounded parameter quadrants; \(361\) independent rational substitutions of the diagonal failure formula; the square-edge formulas; and \(536\) full-matrix entry identities from exact rational matrix inversion on small rook graphs. The program prints `VERIFY_OK` when all checks pass. The mathematical assertions for the infinite parameter family follow from the symbolic steps above; finite matrix checks are only cross-checks.

## Relationship to prior work

Bonaventura and Della Rocca (arXiv:1510.04303v1, first posted 2015-10-14) analyze strong stability and positivity of implicit time-stepping in the framework of absolute monotonicity, including classical Radau schemes in their discussion of positivity/order barriers. Ketcheson, Macdonald and Gottlieb (2008/2009) establish general implicit Runge–Kutta SSP theory; Horváth (1998) studies positivity conditions for Runge–Kutta methods. None of the material inspected in these works gives the explicit \(K_p\square K_q\) spectral classification or the sharp \(m=37/38\) adjacent-transition transition. General method-dependent monotonicity guarantees are not equivalent to a necessary-and-sufficient positivity classification on a fixed graph family.

Earlier available exact results for Radau IIA on equal-alphabet Hamming graphs \(H(d,q)\) include the square \(K_q\square K_q\) as a special case, but cover *all-entry all-timestep positivity* rather than the independent sharp \(37/38\) **adjacent-entry** sign transition, and do not determine the rectangular unequal-alphabet threshold. Earlier results for complete multipartite graphs apply to a distinct graph family (except a few small coincidences) and do not imply the present result. The four spectral values \(0,p,q,p+q\) and their tensor projections are the essential additional structure. Search and inspection cannot exclude an unindexed or inaccessible prior equivalent statement; no formal priority claim is made.

## Limitations

All graph edges must have unit conductance. The complete timestep positivity set for arbitrary \(p\ne q\) is given by the explicit four scalar inequalities but is **not** reduced here to a universal number of intervals; no such stronger claim is made. Strict positivity at positive timesteps in the small-order cases is different from the identity matrix at \(h=0\). Although spectral functions preserve mass, they need not be entrywise positive. The result does not establish stagewise positivity, nonlinear positivity or any general SSP coefficient. The review described separately has not been independently replicated or externally audited.

## References

- L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, arXiv:1510.04303v1, posted October 14, 2015. https://arxiv.org/abs/1510.04303
- D. I. Ketcheson, C. B. Macdonald and S. Gottlieb, *Optimal implicit strong stability preserving Runge–Kutta methods*, Applied Numerical Mathematics 59 (2009), 373–392; public postprint dated February 21, 2008. https://www.davidketcheson.info/assets/papers/implicit_ssp_postprint.pdf
- Z. Horváth, *Positivity of Runge–Kutta and diagonally split Runge–Kutta methods*, Applied Numerical Mathematics 28 (1998), 309–326. https://doi.org/10.1016/S0168-9274(98)00050-6
- E. W. Weisstein, *Rook Graph*, MathWorld, for standard graph nomenclature \(K_p\square K_q=L(K_{p,q})\). https://mathworld.wolfram.com/RookGraph.html
