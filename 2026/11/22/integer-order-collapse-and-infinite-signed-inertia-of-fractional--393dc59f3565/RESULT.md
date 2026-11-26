# Infinite signed inertia of noninteger fractional Volterra self-commutators

## Finding
For every positive real **noninteger** order \(\alpha\), define the Riemann–Liouville operator
\[
(J_\alpha f)(x)=\frac{1}{\Gamma(\alpha)}\int_0^x (x-t)^{\alpha-1}f(t)\,dt
\]
on complex \(L^2(0,1)\) with Lebesgue measure. Its self-commutator \(D_\alpha=J_\alpha J_\alpha^*-J_\alpha^*J_\alpha\) is compact and has infinitely many positive and infinitely many negative eigenvalues, counting multiplicity. In particular, it has infinite operator rank at every such order, including arbitrarily close to any positive integer.

## Assumptions and scope
The interval is exactly \((0,1)\); the adjoint is with respect to the usual \(L^2\) inner product. No claim is made about the rate of eigenvalue decay or the nullspace. Positive integer orders are included below as a separately established comparison, not as a new finite-rank or spectral-product formula.

## Proof
Extend a function by zero outside \((0,1)\). Convolution with the kernel \(t^{\alpha-1}/\Gamma(\alpha)\) on \((0,1)\) and restriction back to the interval gives \(J_\alpha\). Removing the part with \(t<\varepsilon\) leaves a Hilbert–Schmidt operator; Young's inequality bounds the removed operator in norm by \(\varepsilon^\alpha/\Gamma(\alpha+1)\). Thus \(J_\alpha\) is compact for all \(\alpha>0\), even at orders where the untruncated integration kernel is not square integrable. It follows that \(D_\alpha\) is compact and self-adjoint. Reflection \((Rf)(x)=f(1-x)\) satisfies \(RJ_\alpha R=J_\alpha^*\), hence \(RD_\alpha R=-D_\alpha\). It pairs the eigenspaces for every nonzero eigenvalue and its negative.

Fix \(0<\delta<\varepsilon<1/2\). On the separated rectangle \(0<x<\delta\), \(\varepsilon<y<1-\varepsilon\), composing the two operators gives the kernel
\[
\Gamma(\alpha)^2 K_\alpha(x,y)=
\int_0^x(x-t)^{\alpha-1}(y-t)^{\alpha-1}\,dt
-\int_y^1(t-x)^{\alpha-1}(t-y)^{\alpha-1}\,dt.
\]
The compositions can be computed by Fubini on this rectangle (the possible endpoint singularities are integrable for \(\alpha>0\)); the resulting columns are continuous in \(y\) as vectors in \(L^2(0,\delta)\). For fixed \(y\) the second integral is analytic at \(x=0\): \(t\ge y>\varepsilon\), so the power series in \(x/t\) converges uniformly on smaller disks and is integrated against an integrable weight. Substituting \(t=xu\) in the first integral and expanding \((y-xu)^{\alpha-1}\) gives
\[
x^\alpha\sum_{k=0}^\infty (-1)^k\binom{\alpha-1}{k} B(k+1,\alpha)\,x^k y^{\alpha-1-k},\qquad |x|<y,
\]
where \(B\) is the beta function and the prefactor is taken for positive real \(x\). The power series converges on the indicated disk. All its scalar factors \((-1)^k\binom{\alpha-1}{k}B(k+1,\alpha)\) are nonzero for the stated noninteger orders.

Choose any \(n\) distinct points \(y_j\) in \((\varepsilon,1-\varepsilon)\). If \(\sum_{j=1}^n c_j K_\alpha(\cdot,y_j)=0\) in \(L^2(0,\delta)\), continuity in \(x\) gives pointwise equality. At zero the relation is the sum of an analytic germ and \(x^\alpha\) times an analytic germ. If both germs were nonzero their leading exponents would be respectively an integer and a noninteger, so cancellation is impossible. If one vanishes the other must also vanish. The fractional-series coefficients therefore yield
\[
\sum_{j=1}^n c_j y_j^{\alpha-1}(1/y_j)^k=0\qquad (k=0,\ldots,n-1).
\]
The Vandermonde determinant in the distinct \(1/y_j\) is nonzero, as are the \(y_j^{\alpha-1}\). Thus all \(c_j=0\).

If \(D_\alpha\) had finite rank, the operator compressed from the \(y\)-interval to the \(x\)-interval above would have a closed finite-dimensional range. For each interior \(y_j\), the column \(K_\alpha(\cdot,y_j)\) is a norm limit of compressed outputs: average the kernel over shrinking intervals about \(y_j\) using normalized indicator inputs. It would therefore lie in that finite-dimensional range. Since there are arbitrarily many independent columns, this is impossible. Compact self-adjointness and reflection pairing now give infinitely many eigenvalues of both signs.

## Relation to the integer case and to prior work
At \(\alpha=m\in\mathbb N\), repeated integration gives \(J_m=V^m\) for \((Vf)(x)=\int_0^x f(t)\,dt\). *Mixed Volterra-power commutators: exact rank and factorial spectral product* gives rank \(2m\) and \(m\) eigenvalues of each sign for \([V^m,(V^*)^m]\), with range equal to the polynomials of degree at most \(2m-1\). In particular, only eigenfunctions **for nonzero eigenvalues** are asserted to lie in that range. Its product of the squares of the positive eigenvalues is \(\bigl(\prod_{j=0}^{2m-1} j!\bigr)^2/\prod_{j=0}^{4m-1} j!\); the product over the paired nonzero spectrum has the additional factor \((-1)^m\). These exact integer formulas serve as a comparison and are not a distinct contribution here. The noninteger proof instead uses the nonterminating fractional expansion and proves infinite inertia even below the Hilbert–Schmidt threshold of \(J_\alpha\).

Khadkhuu and Tsedenbayar study the self-commutator norms of the first two integer powers. The finite-horizon convolution theorem for minimal strictly stable rational kernels concerns a different hypothesis: the power-law kernel on the positive half-line has Laplace transform \(s^{-\alpha}\), not rational at noninteger orders. Neither that stated theorem nor the signed Hankel defect result for a different fractional Cesàro–Hardy family supplies the infinite positive and negative inertia proved here. Historical equivalence to a broader truncated-convolution result is not ruled out.

## Reproducibility
For an exact finite instance of the column argument, choose rational distinct \(y_j\) and calculate the determinant of the matrix \(((1/y_j)^k)_{k=0}^{n-1}\); the nonzero fractional coefficient and column factors are justified symbolically above, not by floating-point tests. The accompanying original `verify.py` (Python 3.10 or later) includes sampled Vandermonde consistency checks and finite integer-order consistency checks for the comparison. The all-order proof does not rely on a numerical rank threshold or a finite test.

## References
- *Mixed Volterra-power commutators: exact rank and factorial spectral product*, [research record](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-mixed-volterra-power-commutators-exact-rank-and-factorial-spectr--876937a001c2/RESULT.md), Finding and exact self-commutator determinant section.
- L. Khadkhuu and D. Tsedenbayar, “A note on self-commutators of Volterra operator and its square,” *Journal of Applied Science and Engineering A* **3** (2022), 11–16, https://doi.org/10.5564/jasea.v3i1.2455.
- *Self-commutator rank and spectral inertia recover the McMillan degree of a stable scalar convolution*, [research record](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-self-commutator-rank-and-spectral-inertia-recover-the-mcmillan-d--40bbd0b1cc26/RESULT.md), Finding and scope.
- *Hankel signature transitions and exact nonnormality energy for fractional Cesàro–Hardy operators*, [research record](https://github.com/Resultary/2026/blob/main/2026/11/1/SCOPE-hankel-signature-transitions-and-exact-nonnormality-energy-for-f--5d2c64797cf9/RESULT.md), Finding and scope.
