# Real-zero rigidity for symmetric tetrahedral Fourier projections

## Finding
Let \(0<a<1\), let \(W=(W_1,W_2,W_3,W_4)\) have the uniform Dirichlet law \(\operatorname{Dirichlet}(1,1,1,1)\), and set \(Y_a=-W_1-aW_2+aW_3+W_4\). Its characteristic entire function is
\[
\Phi_a(z)=\mathbb E[e^{izY_a}]=\frac{6(\sin(az)-a\sin z)}{a(1-a^2)z^3},\qquad \Phi_a(0)=1.
\]
**Theorem.** Every zero of \(\Phi_a\) is real if and only if there is an integer \(m\ge3\) such that \(a=1-2/m\). For these and only these ratios the Fourier transform belongs to the Laguerre–Pólya real-zero class. For every other \(a\in(0,1)\), the transform has at least one nonreal zero, hence a conjugate pair.

For \(a=(m-2)/m\), all nonzero zeros are located explicitly as follows. Put \(w=z/m\) and
\[
Q_m(x)=mU_{m-3}(x)-(m-2)U_{m-1}(x),
\]
where \(U_j\) is the Chebyshev polynomial of the second kind. The polynomial \(Q_m\) has exactly \(m-1\) distinct simple zeros in \([-1,1]\): both endpoints and \(m-3\) interior points. Every nonzero zero of \(\Phi_a\) occurs at a real \(z\) with either \(\cos(z/m)\) equal to an interior root of \(Q_m\), with multiplicity one, or \(z=mk\pi\) for a nonzero integer \(k\), with multiplicity three. The zero at the origin of the sine numerator is canceled by the denominator and does not yield a zero of \(\Phi_a\).

## Assumptions and scope
The barycentric variables \(W_j\) are nonnegative and sum to one; the normalized uniform law on this three-simplex has constant density \(6\) in independent barycentric coordinates. The four projected vertex heights \(-1,-a,a,1\) are distinct because \(0<a<1\). These heights may also be realized, up to a common positive scaling, as directional projections of the four vertices of a centered regular tetrahedron. No claim is made for unequal vertex masses, asymmetric knot locations, or degenerate endpoint parameters.

## Proof
**1. Transform identity.** For four distinct real knots \(t_j\), Dirichlet multinomial moments give
\[
\mathbb E\left(\sum_{j=1}^{4}t_jW_j\right)^r=\frac{6r!}{(r+3)!}\sum_{e_1+\cdots+e_4=r}\prod_{j=1}^{4}t_j^{e_j}.
\]
The Lagrange divided-difference identity \(\sum_j t_j^n/\prod_{k\ne j}(t_j-t_k)=0\) for \(n<3\), and equals the complete homogeneous polynomial of degree \(n-3\) for \(n\ge3\), proves by comparing the entire power series that
\[
\mathbb E\exp\!\left(iz\sum_jt_jW_j\right)=\frac6{(iz)^3}\sum_{j=1}^4\frac{e^{izt_j}}{\prod_{k\ne j}(t_j-t_k)}.
\]
Inserting \((t_j)=(-1,-a,a,1)\) gives the stated sine quotient. The numerator has the local expansion \(\sin(az)-a\sin z=a(1-a^2)z^3/6+O(z^5)\), hence the singularity is removable with value one.

**2. Necessity by a strict Laguerre obstruction.** Write \(f_a(z)=\sin(az)-a\sin z\). It is real entire of exponential type at most one. If all its zeros are real, its genus-at-most-one Hadamard product places it in the Laguerre–Pólya class, so the classical inequality
\[
L_a(x)=f_a'(x)^2-f_a(x)f_a''(x)\ge0\qquad(x\in\mathbb R)
\]
holds. The zeros of \(f_a\) and \(\Phi_a\) differ only at the triple origin, so the assumption is equivalent to all zeros of \(\Phi_a\) being real. At \(x_0=2\pi/(1-a)\), the two sine arguments differ by \(2\pi\) and therefore
\[
f_a(x_0)=(1-a)\sin x_0,\quad f_a'(x_0)=0,\quad f_a''(x_0)=a(1-a)\sin x_0.
\]
Consequently \(L_a(x_0)=-a(1-a)^2\sin^2 x_0\). As \(0<a<1\), nonnegativity forces \(\sin x_0=0\), equivalently \(2/(1-a)\) is an integer \(m\ge3\). This also proves the existence of nonreal zeros in all other cases; no numerical search is needed.

**3. Sufficiency and multiplicities.** Conversely choose an integer \(m\ge3\), put \(a=(m-2)/m\), and substitute \(z=mw\). The Chebyshev identity \(\sin((j+1)w)=\sin w\,U_j(\cos w)\) gives
\[
m f_a(mw)=\sin w\,Q_m(\cos w).
\]
The polynomial \(Q_m\) has degree \(m-1\) and satisfies \(Q_m(1)=Q_m(-1)=0\). At \(w_j=j\pi/(m-1)\), \(j=1,\ldots,m-2\), direct substitution gives
\[
f_a(mw_j)=(-1)^{j+1}\frac{2(m-1)}m\sin w_j.
\]
These \(m-2\) values have alternating nonzero signs, so the intermediate value theorem supplies \(m-3\) distinct roots in \((w_j,w_{j+1})\) for \(j=1,\ldots,m-3\). They yield \(m-3\) distinct roots of \(Q_m\) strictly inside \((-1,1)\), in addition to the two endpoints. Since the degree is exactly \(m-1\), these are *all* its roots and all are simple. Every solution of \(\cos w=x\in[-1,1]\) is real (write \(w=u+iv\) and compare imaginary parts, or use the exponential quadratic with roots on the unit circle). Hence every zero of the sine numerator is real.

An interior root of \(Q_m\) yields a simple numerator zero because \(\sin w\ne0\) and \((\cos w)'\ne0\). At \(w=k\pi\), \(\sin w\) has a simple zero while \(\cos w-(-1)^k\) vanishes to order two and the endpoint root of \(Q_m\) is simple, giving numerator multiplicity three. At \(w=0\) this triple zero is removed by division by \(z^3\); at every nonzero multiple of \(\pi\) it remains. The zero multiplicities of \(\Phi_a\) follow.

## Verification
The accompanying standalone Python script `check_tetrahedral_zeros.py` can be executed with Python 3 and the versions of SymPy, SciPy, and NumPy available locally. It independently checks the divided-difference coefficients, the first thirteen exact even-power series coefficients, exact Sturm counts and squarefreeness for \(3\le m\le14\), the negative Laguerre defect at four nonexceptional rational ratios, and five independent numerical simplex integrals. The recorded output is `checker_output.txt`. These tests corroborate the algebra; the universal theorem rests on the preceding analytical proof.

## Relationship to prior work
Dirichlet averages and their spline interpretation are classical; see Massopust's exposition and its earlier references. The Laguerre–Pólya real-zero criterion and the Laguerre inequality are classical; see Cardon. Adams and Cardon construct broad families of real-rooted exponential sums, but their positive-parameter Hermite–Biehler construction is a sufficient mechanism, not an iff statement for these four uniformly distributed simplex knots. The contribution here is the exact arithmetic classification of all directions in this symmetric one-parameter tetrahedral family together with complete nonzero zero-multiplicity geometry, not the divided-difference representation or the general theory of real-rooted entire functions.

## Limitations
Publication priority has not been independently certified; older spline transform, Hermite–Biehler, and exponential-polynomial literature may contain a logically equivalent classification. The result only treats uniform tetrahedral barycentric coordinates and distinct symmetric knots \(-1,-a,a,1\) for \(0<a<1\). The proof gives existence, but not a quantitative location, of nonreal zeros at nonexceptional ratios. No independent mathematical audit has been performed.

## References
1. S. R. Adams and D. A. Cardon, *Sums of entire functions having only real zeros*, arXiv:math/0608297 (first submitted 2006-08-12), especially Theorem 1.1 and Section 4.
2. D. A. Cardon, *Extended Laguerre inequalities and a criterion for real zeros*, arXiv:0911.1122 (first submitted 2009-11-05), Section 1.
3. P. Massopust, *Fractional Operators, Dirichlet Averages, and Splines*, arXiv:1309.0240 (first submitted 2013-09-01), Sections 4–5.
4. D. A. Cardon, *Fourier transforms having only real zeros*, Proceedings of the American Mathematical Society 133 (2005), 1349–1356, author manuscript https://mathdept.byu.edu/cardon/papers/FourierRealZeros.pdf .
