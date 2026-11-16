# Parity-sharp lattice Fourier sparsity of high-dimensional cross-polytopes

## Finding
Let \(d\ge5\) be an integer, and let
\[
 C_d=\{x\in\mathbb R^d:\sum_{j=1}^{d}|x_j|\le1\},\qquad
 F_d(k)=\int_{C_d}e^{-2\pi i\langle k,x\rangle}\,dx
\]
for \(k\in\mathbb Z^d\). For an integer \(N\ge1\), put
\[
 S_d(N)=\#\{k\in\mathbb Z^d:|k_j|\le N\ (1\le j\le d),\ F_d(k)\ne0\}.
\]
Then, as \(N\to\infty\) with \(d\) fixed,
\[
 S_d(N)=
 \begin{cases}
 2^d\binom d2 N^{d-1}+O_d(N^{d-2}),&d\text{ odd},\\
 2^d\binom d3 N^{d-2}+O_d(N^{d-3}),&d\text{ even}.
 \end{cases}
\]
More structurally, if \(d\) is odd and the absolute coordinates \(|k_j|\) are all distinct, then \(F_d(k)=0\); if \(d\) is even, \(F_d(k)=0\) whenever no absolute-coordinate value occurs at least three times. Every frequency with exactly one repeated positive absolute-coordinate value, repeated twice in odd dimension or three times in even dimension, and with all other absolute-coordinate values mutually distinct, has \(F_d(k)\ne0\). Thus the effective generic support changes from collision codimension one to codimension two according to the parity of the dimension. The cases \(d=3,4\) are not presented as new claims.

## Assumptions and scope
The Fourier transform is the ordinary Lebesgue integral with the explicit \(2\pi\) convention above, not a discrete transform or a Fourier transform of lattice points. The body has unit \(\ell^1\) radius. The integer-frequency box uses all signs and includes zero. The constant in the remainder is allowed to depend on fixed \(d\). The theorem gives a sharp asymptotic count and vanishing criteria; it does not classify every deeper multi-collision frequency.

For a finite list \(y_1,\ldots,y_d\), write \([y_1,\ldots,y_d]f\) for the order-\(d-1\) Newton divided difference. When arguments repeat, this means the continuous confluent/Hermite limit; an argument repeated \(r\) times enters through derivatives of order at most \(r-1\). Put \(y_j=(2\pi k_j)^2\).

## Proof
**1. Laplace reduction and exact transform.** Let \(C_d(R)=R C_d\), and define \(H(R)=\int_{C_d(R)}e^{-2\pi i\langle k,x\rangle}\,dx\). For \(s>0\), Tonelli applied to the absolutely integrable envelope gives
\[
 \int_0^\infty e^{-sR}H(R)\,dR
 =\frac1s\prod_{j=1}^d\int_\mathbb R e^{-s|x_j|-2\pi i k_j x_j}\,dx_j
 =\frac{2^d s^{d-1}}{\prod_{j=1}^d(s^2+y_j)}.
\]
For distinct \(y_j\), partial fractions in \(s^2\) followed by the inverse Laplace transforms of \(\cos(R\sqrt y)\) and \(\sin(R\sqrt y)/\sqrt y\) yield, at \(R=1\),
\[
 F_{2m+1}(k)=2^{2m+1}(-1)^m[y_1,\ldots,y_{2m+1}]
 \left(y^m\frac{\sin\sqrt y}{\sqrt y}\right),
\]
\[
 F_{2m}(k)=2^{2m}(-1)^m[y_1,\ldots,y_{2m}]
 \left(y^{m-1}\cos\sqrt y\right).
\]
Both functions are entire in \(y\); continuity in frequency extends the formulas to repeated nodes, giving the exact Hermite interpretation. Evaluating the Taylor coefficients at \(k=0\) also recovers \(F_d(0)=2^d/d!\).

**2. Collision support.** At each lattice node \(y=(2\pi n)^2\), the odd-dimensional function \(f(y)=y^m\sin\sqrt y/\sqrt y\) vanishes for every integer \(n\), including zero because \(m\ge2\). The interpolation formula at pairwise distinct nodes therefore gives zero. At any positive lattice node,
\[
 f'(y)=\frac{y^{m-1}}2.
\]
If one positive value \(y\) occurs exactly twice and all other nodes differ from one another and from \(y\), the confluent residue formula gives
\[
 F_{2m+1}(k)=\frac{(-1)^m 2^{2m}y^{m-1}}
 {\displaystyle\prod_{y_j\ne y}(y-y_j)}\ne0.
\]

In even dimension set \(g(y)=y^{m-1}(\cos\sqrt y-1)\). Its divided difference is the same as that of \(y^{m-1}\cos\sqrt y\), since the subtracted polynomial has degree \(m-1<2m-1\). At every lattice node, \(g(y)=g'(y)=0\); at zero this uses \(m\ge3\), and at positive nodes it follows from the zero of \(\sin\sqrt y\). Thus every Hermite divided difference with node multiplicities at most two vanishes. At any positive node,
\[
 g''(y)=-\frac{y^{m-2}}4.
\]
If exactly one positive value \(y\) occurs three times and the other nodes are distinct, the residue contribution is
\[
 F_{2m}(k)=\frac{(-1)^{m+1}2^{2m-3}y^{m-2}}
 {\displaystyle\prod_{y_j\ne y}(y-y_j)}\ne0.
\]
These formulas also verify that the relevant generic collision families carry nonzero coefficients. They make no claim about additional cancellations at more complicated collisions.

**3. Sharp lattice count.** For odd \(d\), every nonzero-frequency configuration belongs to at least one of the \(\binom d2\) equal-absolute-coordinate-pair hyperplanes. For a fixed pair, the number of choices with both coordinates nonzero, equal in absolute value, and all remaining absolute coordinates positive and mutually distinct is
\[
 4N\,2^{d-2}(N-1)_{d-2}
 =2^d N^{d-1}+O_d(N^{d-2}),
\]
where \((M)_r=M(M-1)\cdots(M-r+1)\). Each such choice has nonzero Fourier coefficient by step 2. The configurations with a zero in an unrestricted coordinate, an extra equality, or an intersection of two distinct pair hyperplanes have only \(O_d(N^{d-2})\) points. Inclusion and exclusion at leading order gives the odd formula.

For even \(d\), every nonzero coefficient lies on at least one of the \(\binom d3\) triple-equality loci. For a fixed triple, the analogous generic count is
\[
 8N\,2^{d-3}(N-1)_{d-3}
 =2^d N^{d-2}+O_d(N^{d-3}).
\]
Two distinct triple conditions, any extra collision, or a zero in the unrestricted coordinates imposes at least one additional independent equality, so their total is \(O_d(N^{d-3})\). The nonvanishing formula of step 2 supplies the matching lower count. This proves both asymptotics.

## Verification
The standalone `check.py` reproduces the confluent residue expression at 65 decimal digits, checks the explicit isolated-double and isolated-triple formulas in dimensions three through eight, checks zero values when collision multiplicity is too low, and checks the combinatorial leading constants. These finite checks corroborate, but do not replace, the all-dimensional Laplace/Hermite argument. To reproduce: `python -m pip install mpmath` followed by `python check.py`. The program has no external data dependencies.

## Relationship to prior work
Robins' 2021 introductory monograph develops general Fourier transforms of polytopes, including the planar cross-polytope and arbitrary-dimensional polytope transform machinery; these general methods are prior art, not claimed here. Diaz, Le and Robins' earlier work likewise develops polytope Fourier formulas. Published exact lattice Fourier analyses of the three-dimensional octahedron and the four-dimensional cross-polytope cover those individual dimensions, which are excluded from novelty. The present claim is the single parity-sensitive, all-fixed-dimensions \(d\ge5\) support codimension and sharp leading coefficients. No general inverse conclusion about tilings or frames is asserted.

## Limitations
The sharp counts are asymptotic, not exact quasipolynomials. Multi-collision frequency values may vanish or survive; their complete classification remains open here. Polynomial and divided-difference formulas alone are not claimed novel; the assessed contribution is their arithmetic generic-collision implication and the dimension-parity support law. Earlier general polytope-transform literature might implicitly cover this consequence, so historical priority should be independently checked. No independent validation has been performed.

## References
1. Sinai Robins, *A friendly introduction to Fourier analysis on polytopes*, arXiv:2104.06407, originally posted 2021-04-12. Sections 2.8 and 6.
2. Ricardo Diaz, Quang-Nhat Le and Sinai Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, arXiv:1602.08593, 2016.
3. *Octahedral lattice Fourier support and exact three-level covering multiplicities*, public mathematical record, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-octahedral-lattice-fourier-support-and-exact-three-level-coverin--a7565c44edcb .
4. *Arithmetic Fourier support and three-level lattice coverage of the four-dimensional cross-polytope*, public mathematical record, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-arithmetic-fourier-support-and-three-level-lattice-coverage-of-t--313db71ad1f7 .
