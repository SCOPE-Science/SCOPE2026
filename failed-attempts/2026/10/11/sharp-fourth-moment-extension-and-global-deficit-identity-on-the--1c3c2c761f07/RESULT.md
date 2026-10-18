# Sharp fourth-moment extension and global deficit identity on the split finite-field hyperbola

## Finding

Let \(q\geq3\) be an odd prime power, \(F=\mathbb F_q\), and \(\psi:F\to\mathbb C\) any nontrivial additive character. Put \(m=q-1\), and for each \(f:F^\times\to\mathbb C\) define the split-hyperbola extension operator
\[
\mathcal E_qf(x,y)=\frac1m\sum_{t\in F^\times}f(t)\psi(xt+yt^{-1}),\qquad (x,y)\in F^2.
\]
Then the following inequality has its *optimal* coefficient:
\[
\boxed{\sum_{(x,y)\in F^2}|\mathcal E_qf(x,y)|^4
\leq\frac{3q^2(q-2)}{(q-1)^3}
\left(\frac1{q-1}\sum_{t\in F^\times}|f(t)|^2\right)^2.}
\]
Every nonzero equality case, and no other, is of the form
\[
\boxed{f(a)=\lambda e^{i\theta_a},\quad
f(-a)=\lambda e^{-i\theta_a}\quad(a\in R),}
\]
where \(R\) contains one representative of each antipodal pair in \(F^\times\), \(\lambda\in\mathbb C\setminus\{0\}\), and the \(\theta_a\) are arbitrary real angles. In particular, the extremizer phases have \((q-1)/2\) independent antipodal-pair degrees of freedom before quotienting by common scaling.

The finding also supplies an **exact global four-term nonnegative deficit identity** (below), rather than only the sharp coefficient or a local stability statement.

## Assumptions and scope

The characteristic is odd, with no restriction on the extension degree of \(F\); the case \(q=3\) is included. Ambient \(\ell^4\) uses *counting measure* on \(F^2\); surface \(\ell^2\) uses *normalized counting measure* on \(F^\times\). The curve is exactly \(\{(t,t^{-1}):t\in F^\times\}\), equivalently the split affine conic \(uv=1\), not the quadratic paraboloid in three variables. The zero function is another trivial equality case.

Fix \(R\subset F^\times\) with one element from each \(\{a,-a\}\), and set \(k=(q-1)/2\). For \(a\in R\), write
\[
A_a=|f(a)|^2,\quad B_a=|f(-a)|^2,\quad s_a=A_a+B_a,\quad u_a=\frac{s_a}{2},\quad
 t_a=|f(a)f(-a)|,\quad z_a=f(a)f(-a).
\]
Put \(H=\sum_{a\in R}s_a=\sum_{t\ne0}|f(t)|^2\), \(Z=\sum_{a\in R}z_a\), and \(Q_q(f)=m^4q^{-2}\sum_{x,y}|\mathcal E_qf(x,y)|^4\). The **exact global deficit** is
\[
\begin{aligned}
&\left(3-\frac3m\right)H^2-Q_q(f)\\
&=\frac32\sum_{a\in R}\left(s_a-\frac{H}{k}\right)^2
+\frac12\sum_{a\in R}(A_a-B_a)^2\\
&\quad+8\sum_{\substack{a,b\in R\\a<b}}(u_au_b-t_at_b)
+4\left[\left(\sum_{a\in R}t_a\right)^2-|Z|^2\right]\ \geq0.
\end{aligned}
\]
Here \(a<b\) simply selects each unordered pair of distinct representatives once; it does not presume an order compatible with finite-field operations. All four summands are nonnegative individually.

## Proof

**1. Classification of two-sum fibers.** For \(a,b\in F^\times\), let
\[
(s,w)=(a+b,a^{-1}+b^{-1}).
\]
When \(s=0\), necessarily \(b=-a\), so \(w=0\), and the fiber at \((0,0)\) contains all \(m\) ordered antipodal pairs. When \(s\ne0\), we have \(w=(a+b)/(ab)=s/(ab)\ne0\). Thus \(a,b\) are the two roots (counted with multiplicity) of the *uniquely determined* polynomial
\[
T^2-sT+\frac{s}{w}.
\]
Every other nonempty fiber therefore consists of exactly one ordered diagonal pair \((a,a)\) or exactly two ordered pairs \((a,b),(b,a)\). This uses only that \(F\) is a field and its characteristic is odd.

**2. Exact fourth moment.** Character orthogonality gives
\[
Q_q(f)=\sum_{(s,w)\in F^2}
\left|\sum_{\substack{a,b\in F^\times\\a+b=s,\ a^{-1}+b^{-1}=w}}f(a)f(b)\right|^2.
\]
Let \(V=\sum_{a\ne0}|f(a)|^4\) and \(P=\sum_{a\in R}|f(a)f(-a)|^2\). The diagonal fibers contribute \(V\), the non-antipodal off-diagonal unordered pairs contribute \(4[(H^2-V)/2-P]\), and the exceptional origin contributes \(4|Z|^2\). Therefore
\[
Q_q(f)=2H^2-V-4P+4|Z|^2
=2H^2-\sum_{a\in R}s_a^2-2\sum_{a\in R}t_a^2+4|Z|^2.
\]
There are no unclassified fibers.

**3. Nonnegative deficit and optimality.** We have \(t_a\le u_a\) by the arithmetic-geometric mean inequality. Also \(H=\sum s_a\), and \(|Z|\le\sum t_a\). Substitute the exact moment in the claimed deficit and use the identities
\[
\sum_a\left(s_a-\frac Hk\right)^2=\sum_as_a^2-\frac{H^2}{k},
\qquad 4(u_a^2-t_a^2)=(A_a-B_a)^2.
\]
Expanding the right-hand side of the stated four-term identity gives exactly \((3-3/m)H^2-Q_q(f)\), since \(m=2k\). Each term is nonnegative: dispersion and amplitude imbalance are sums of squares, \(u_au_b\ge t_at_b\), and the final term is the squared triangle inequality. This proves the sharp inequality after the definitions of \(H\) and \(Q_q\) are substituted.

For \(f\ne0\), equality in the first two terms forces \(A_a=B_a=H/m>0\) for *every* \(a\in R\), and hence \(t_a=u_a=H/m\). Equality in the final term forces the nonzero complex numbers \(z_a\) to share a common argument; this condition is automatic when \(k=1\). Consequently \(z_a=\lambda^2\) independently of \(a\), with \(|\lambda|^2=H/m\). Choosing one square root \(\lambda\) and arbitrary angles for \(f(a)/\lambda\) yields precisely \(f(a)=\lambda e^{i\theta_a}\), \(f(-a)=\lambda e^{-i\theta_a}\). Conversely such choices make all four deficit summands vanish. Thus the bound is attained and the extremizer family is complete.

## Verification

The accompanying standalone Python program `check_hyperbola.py` enumerates every two-sum fiber and checks the exact fourth-moment identity, the four-way nonnegative deficit identity, and the counting-measure Fourier expression, for \(q\in\{3,5,7,9,11,13\}\), including \(F_9=\mathbb F_3[t]/(t^2+1)\). It tests \(120\) independently selected complex Gaussian-integer coefficient vectors and six nonconstant-phase equality cases, with reproducible random seed. Its floating-point Fourier and phase tests are corroboration; the proof above establishes the assertion for all odd prime powers. Execute `python3 check_hyperbola.py` in the directory containing that file.

## Relationship to prior work

González-Riquelme and Oliveira e Silva [1] introduced sharp finite-field Fourier extension constants for parabolae, paraboloids and cones, and derived a sharp bound for the **two-parameter hyperbolic paraboloid in three-dimensional frequency space**. Their Theorems 1.1–1.5 do not give the present sharp coefficient, full antipodal-pair extremizer family, or exact global deficit for the **one-dimensional split affine hyperbola in two-dimensional frequency space**. These are distinct objects, not interchangeable normalizations.

Iosevich–Koh–Lee–Pham–Shen [2, Theorem 1.5] prove the *sharp range of exponents* for finite-field nonzero-radius spheres in even dimension **at least four**, using dimension-dependent bounds with unspecified constants; their theorem does not give the present dimension-two exact coefficient or equality cases. The conic extension work of González-Riquelme–Ismoilov [3] concerns higher-dimensional cones in \(F^4\), not the curve \(uv=1\). A theorem under a less obvious equivalent conic formulation could exist and remains a novelty risk. The collision calculation and deficit identity here are self-contained.

## Limitations

The assertion is limited to odd characteristic and the exact split hyperbola with normalized surface measure. It does not cover characteristic two, the zero-radius cone, general quadratic surfaces, or other extension exponents. The computational tests do not establish the unrestricted theorem independently. Literature searches and inspection cannot rule out unindexed or differently named prior results; no independent mathematical audit has been performed.

## References

[1] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first posted 26 May 2024, https://arxiv.org/html/2405.16647v1 . Relevant: Theorems 1.1–1.5 and Sections 1.1–1.2.

[2] A. Iosevich, D. Koh, S. Lee, T. Pham, and C.-Y. Shen, *On Restriction Estimates for the Zero Radius Sphere over Finite Fields*, arXiv:1806.11387, first posted 29 June 2018, https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/on-restriction-estimates-for-the-zero-radius-sphere-over-finite-fields/BD04A06192620C6B701E44B560F81F6A . Relevant: Theorem 1.5 and Section 3.

[3] C. González-Riquelme and T. Ismoilov, *Maximizers of the L2 to L4 Fourier extension inequality for cones in finite fields*, arXiv:2509.05600, https://arxiv.org/abs/2509.05600 . Relevant: abstract and stated ambient-dimensional scope.
