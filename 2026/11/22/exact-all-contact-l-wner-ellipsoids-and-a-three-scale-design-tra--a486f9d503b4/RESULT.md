# Exact all-contact Löwner ellipsoids and a three-scale design transition for panhandle matroid polytopes

## Finding
For every integer triple \(3\le r\le s\), \(m\ge2\), the canonical rank-\(r\) panhandle matroid base polytope has a uniquely determined minimum-volume enclosing ellipsoid. All of its vertices, and no other points, contact this ellipsoid. Its center and three Euclidean semiaxis classes are explicit in terms of the unique solution \(w\in(0,1)\) of
\[
\frac{(s-1)(2r-s-1)}{r(s-r)+(2r-s-1)w}+\frac m w-\frac1{1-w}=0.
\]
For fixed \(r\) and growing head size \(s\), the optimal fraction \(w\) of tail-incorporating contact mass undergoes a sharp saturation transition at the ratio \(m/s=1/(r-1)\), with distinct interior, square-root, and inverse-linear regimes. These are optimal **contact-design weights**, not spherical normal-cone exposure probabilities.

## Assumptions and scope
Fix integers \(3\le r\le s\) and \(m\ge2\); put \(n=s+m\), \(d=n-1\), \(H=[s]\) and \(T=[n]\setminus H\). Work in the affine hyperplane \(A_r=\{x\in\mathbb R^n:\sum_i x_i=r\}\) with its inherited Euclidean metric. Define
\[
P_{r,s,m}=\operatorname{conv}\{\mathbf1_B:|B|=r,\ |B\cap T|\le1\}.
\]
Its vertices split into a head-only orbit \(\mathcal V_0\) of size \(\binom{s}{r}\), and a one-tail orbit \(\mathcal V_1\) of size \(m\binom{s}{r-1}\). Every such indicator is an extreme vertex: a convex combination of binary indicators can equal another binary indicator only when every summand has the same coordinates.

Write
\[
A=r(s-r),\qquad B=2r-s-1,\qquad
h(w)=\frac{A+Bw}{s(s-1)},\quad t(w)=\frac wm,\quad b(w)=\frac{n\,w(1-w)}{sm}.
\]
The symbol \(A\) in this display is a scalar and should not be confused with the affine hyperplane \(A_r\). For each \(w\in(0,1)\), let \(\mu(w)\) have first \(s\) coordinates \((r-w)/s\) and last \(m\) coordinates \(w/m\). Let \(E=\mathbf1_n^\perp\); decompose it orthogonally as \(E_H\oplus E_T\oplus E_B\), where \(E_H\) consists of zero-sum vectors supported on \(H\), \(E_T\) is its tail analogue, and \(E_B\) is the one-dimensional block-constant contrast. Set \(\Sigma(w)\) to be the positive operator on \(E\) acting by \(h(w)\), \(t(w)\), \(b(w)\) on these three subspaces respectively.

There is exactly one \(w_*\in(0,1)\) solving the displayed critical equation. The ellipsoid is
\[
\mathcal E_* = \{x\in A_r:\ \langle x-\mu(w_*),\Sigma(w_*)^{-1}(x-\mu(w_*)\rangle\le d\}.
\]
Its semiaxis lengths are \(\sqrt{d\,h(w_*)}\), \(\sqrt{d\,t(w_*)}\) and \(\sqrt{d\,b(w_*)}\), of multiplicities \(s-1\), \(m-1\), and \(1\). Its intrinsic volume is
\[
\operatorname{vol}_d(\mathcal E_*)=\operatorname{vol}_d(B_2^d)\,d^{d/2}\,h(w_*)^{(s-1)/2}t(w_*)^{(m-1)/2}b(w_*)^{1/2}.
\]
The unique root can equivalently be found from
\[
mA+[\,(n-1)B-(m+1)A\,]w-nBw^2=0,
\]
choosing the root in \((0,1)\) (the derivative equation fixes the root even when \(A=0\) or \(B=0\)). At \(s=2r-1\), the exact value is \(w_*=m/(m+1)\); at \(s=r\), it is \(w_*=(n-1)/n\).

For a fixed integer \(r\ge3\) and sequences \(s\to\infty\) with \(m/s\to\rho\in(0,\infty)\), the following are sharp:
\[
\begin{array}{ll}
0<\rho<1/(r-1): & w_*\longrightarrow r\rho/(1+\rho),\\[2pt]
\rho>1/(r-1): & s(1-w_*)\longrightarrow\big(\rho-1/(r-1)\big)^{-1}.
\end{array}
\]
At the critical ratio, under the more precise integer hypothesis \(m=s/(r-1)+O(1)\),
\[
\sqrt{s}\,(1-w_*)\longrightarrow\frac{r-1}{\sqrt r}.
\]
No uniformity over growing \(r\) is claimed.

## Proof
**1. Symmetric covariance design.** Assign mass \(1-w\) uniformly to \(\mathcal V_0\) and mass \(w\) uniformly to \(\mathcal V_1\), and let \(X\) be the random vertex. Its mean is exactly \(\mu(w)\). Each orbit is transitive under \(S_s\times S_m\). The covariance operator \(\operatorname{Cov}(X)\) preserves the three indicated orthogonal subspaces. If \(k\) heads are selected uniformly, the eigenvalue on head zero-sum contrasts is \(k(s-k)/(s(s-1))\). Taking \(k=r\) with probability \(1-w\) and \(k=r-1\) with probability \(w\) gives \(h(w)\). For tail zero-sum contrasts, the one-hot tail selection yields \(t(w)=w/m\). Since the total selected tail count is Bernoulli with variance \(w(1-w)\), projection onto the unit block contrast yields \(b(w)=nw(1-w)/(sm)\). These are all strictly positive for \(0<w<1\), including at \(s=r\), so the polytope spans \(A_r\).

**2. Unique determinant maximizer.** The determinant of this covariance restricted to \(E\) is
\[
D(w)=h(w)^{s-1}t(w)^{m-1}b(w).
\]
Apart from a constant its logarithm equals
\[
(s-1)\log(A+Bw)+m\log w+\log(1-w).
\]
Its second derivative is
\[
-\frac{(s-1)B^2}{(A+Bw)^2}-\frac m{w^2}-\frac1{(1-w)^2}<0.
\]
It tends to negative infinity as \(w\downarrow0\) or \(w\uparrow1\) (for \(s=r\), the first endpoint only decreases faster). Thus the unique maximizer \(w_*\) lies in \((0,1)\), obeys the stated derivative equation, and after clearing denominators obeys the quadratic.

**3. Exact all-vertex contact.** Let \(q_j(w)\) be the squared Mahalanobis distance from \(\mu(w)\) of any member of orbit \(\mathcal V_j\) using \(\Sigma(w)^{-1}\), for \(j=0,1\). Transitivity makes it constant within each orbit. The covariance trace identity gives
\[
(1-w)q_0(w)+wq_1(w)=\operatorname{tr}(\Sigma(w)^{-1}\Sigma(w))=d.
\]
Differentiating \(\log D(w)\) by the covariance identity gives \(\frac{d}{dw}\log D(w)=q_1(w)-q_0(w)\): the derivative of the centered second moment exactly cancels the center terms. At \(w_*\), this difference vanishes; hence \(q_0(w_*)=q_1(w_*)=d\). Consequently all vertices lie on \(\partial\mathcal E_*\), and by convexity the whole polytope lies inside. Strict convexity of the ellipsoid's quadratic gauge shows that every nonvertex point of the polytope lies strictly inside.

**4. Optimality and uniqueness without an invariant-ellipsoid assumption.** Take any ellipsoid containing the polytope, expressed intrinsically as \(\{x\in A_r:\langle x-c,Q^{-1}(x-c)\rangle\le1\}\) with \(Q\) positive definite on \(E\). Average this inequality under the just-constructed vertex law. Then
\[
\operatorname{tr}(Q^{-1}\Sigma(w_*))+\langle\mu(w_*)-c,Q^{-1}(\mu(w_*)-c)\rangle\le1.
\]
By AM–GM applied to the \(d\) eigenvalues of \(Q^{-1/2}\Sigma(w_*)Q^{-1/2}\), one has \(\det Q\ge d^d\det\Sigma(w_*)\). Equality requires \(c=\mu(w_*)\) and \(Q=d\Sigma(w_*)\). Thus \(\mathcal E_*\) is uniquely minimum-volume among **all** enclosing ellipsoids, not merely symmetry-invariant ones.

**5. Contact-mass transition.** Let \(r\) be fixed, with \(s\to\infty\), \(m/s\to\rho\). Dividing the derivative equation by \(s\) at any fixed \(w\in(0,1)\) gives the strictly decreasing limiting derivative \(-1/(r-w)+\rho/w\). If \(\rho<1/(r-1)\), its unique zero in \((0,1)\) is \(r\rho/(1+\rho)\). Otherwise the maximizer converges to \(1\). For strict supercritical \(\rho\), substitution \(w=1-\varepsilon\) in the derivative equation yields \(s\varepsilon\to(\rho-1/(r-1))^{-1}\). At criticality, under \(m=s/(r-1)+O(1)\), substituting \(w=1-z/\sqrt s\) and dividing by \(\sqrt s\) gives
\[
z\left(\frac1{(r-1)^2}+\frac1{r-1}\right)-\frac1z=0,
\]
whose unique positive solution is \(z=(r-1)/\sqrt r\). Strict concavity and the signs of the derivative on either side supply the matching convergence of the actual maximizers. No finite enumeration is used to justify these limits.

## Verification
Run `python verify_panhandle_loewner.py` with Python and NumPy. It independently enumerates both vertex orbits for all 39 tested integer triples, reconstructs the full covariance matrix directly from the enumerated binary vertices, matches every spectral eigenvalue against the three closed formulas, and checks that the quadratic gauge of every vertex equals the affine dimension. Nine further numerical tests target the three asymptotic branches, including the critical square-root scale. The deterministic run ends `PANHANDLE_LOEWNER_PASS configurations=39 asymptotic_tests=9`. These finite computations corroborate; the infinite claim follows from the analytic proof above.

## Relationship to prior work
Hanely and collaborators introduced and enumerated panhandle matroid base polytopes in 2022. Deligeorgaki and collaborators investigated their Ehrhart properties in 2023; neither cited mathematical result computes their Euclidean Löwner ellipsoids. A previously indexed rank-two one-parallel-class ellipsoid result treats a lower-rank family and is excluded by the hypothesis \(r\ge3\). Other related indexed results treat panhandle widths, inballs, covariance of **uniform vertex** measures, and distance shells. The present ellipsoid uses an **optimally nonuniform** contact measure with a sharp two-block saturation threshold. The covariance determinant comparison and the complete outer-ellipsoid certificate are not implied by those different geometric invariants. Finite-dimensional optimal design and determinant inequalities are established tools, not claimed as new.

## Limitations
The assertion is for integers \(3\le r\le s\), \(m\ge2\) in the canonical inherited Euclidean metric. The asymptotic three-scale transition assumes fixed rank \(r\) and the specified growth hypotheses; no growing-rank or outside-class extension is claimed. The statement includes an exact algebraic root but no elementary radical expression uniformly preferred for all parameter cases. Historical priority is a best-knowledge comparison, not an exhaustive theorem of uniqueness in literature. The result has not undergone independent mathematical validation.

## References
1. D. Hanely, J. L. Martin, D. McGinnis, D. Miyata, G. D. Nasr, A. R. Vindas-Meléndez, M. Yin, *Ehrhart Theory of Paving and Panhandle Matroids*, arXiv:2201.12442, first public 2022-01-28, https://arxiv.org/abs/2201.12442.
2. D. Deligeorgaki, D. McGinnis, A. R. Vindas-Meléndez, *Ehrhart Bounds for Panhandle and Paving Matroids Through Enumeration of Chain Forests*, arXiv:2311.01640, first public 2023-11-02, https://arxiv.org/abs/2311.01640.
3. Standard D-optimal covariance-design and determinant/trace inequality; applied here with a direct proof of the necessary certificate.
