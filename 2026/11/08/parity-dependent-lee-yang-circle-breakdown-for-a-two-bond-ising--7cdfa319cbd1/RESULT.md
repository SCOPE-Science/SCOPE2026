# Parity-dependent Lee–Yang circle breakdown for a two-bond Ising impurity

## Finding

For every integer \(N\ge3\), consider an Ising ring with \(N-2\) bulk bonds of dimensionless coupling \(K>0\), and two identical impurity bonds of real coupling \(L\), joining spin 1 to spins 2 and \(N\). The uniform-field Lee–Yang polynomial has **at most one reciprocal pair of zeros away from the unit circle**, and that pair, when present, lies on the **negative real axis**. Its appearance has the following sharp parity-dependent criterion.

Set
\[
q=e^{-2K}\in(0,1),\qquad u=e^{2L}>0,\qquad
u_N(q)=\frac{q+\sqrt{q^2+N(N-2)}}{N}.
\]

- For **even** \(N\), all zeros are on the unit circle exactly when \(L\ge0\). At \(L=0\), \(z=-1\) is a double zero. For \(L<0\), exactly two zeros are off-circle, simple and negative-real reciprocal; the other \(N-2\) zeros are simple and on-circle.
- For **odd** \(N\), all zeros are on the unit circle exactly when \(u\ge u_N(q)\). At \(u=u_N(q)\), \(z=-1\) is a triple zero, and every other zero is simple and on-circle. For \(u<u_N(q)\), exactly two zeros are off-circle, simple and negative-real reciprocal; the remaining \(N-2\) zeros are simple and on-circle.

In particular, odd rings tolerate a *strictly negative* impurity coupling before the circle property breaks, whereas even rings lose it immediately upon changing the sign of either equal impurity bond. The odd threshold is negative because \(0<u_N(q)<1\) for \(0<q<1\).

## Assumptions and scope

Let \(s_j\in\{-1,1\}\) and set \(s_{N+1}=s_1\). Use the explicit finite-volume partition function
\[
 Z_N(h)=\sum_{s\in\{-1,1\}^N}
 \exp\!\left[K\sum_{j=2}^{N-1}s_js_{j+1}
 +L s_1(s_2+s_N)+h\sum_{j=1}^{N}s_j\right].
\]
Define \(P_N(z)=z^{N/2}Z_N(h)\) for \(z=e^{2h}\); this is an ordinary degree-\(N\) polynomial with strictly positive real coefficients and nonzero leading and constant terms. The same symbol \(h\) may be complex when locating zeros. Zeros are counted with algebraic multiplicity. The conclusions hold at fixed finite \(K>0\) for all real \(L\), without a thermodynamic-limit assumption. The two defect bonds are equal; no claim is made for independent, unequal impurities.

## Proof

**1. Exact Chebyshev reduction.** Define
\[
 a=e^K,\quad b=e^{-K},\quad D=a^2-b^2>0,\quad
 c=e^{L-K},\quad d=e^{-L}-e^{L-2K},\quad
 x=\frac{a\cosh h}{\sqrt D}.
\]
The standard bulk transfer matrix and impurity-bond matrix are
\[
 T=\begin{pmatrix}ae^h&b\\b&ae^{-h}\end{pmatrix},\qquad
 T_L=\begin{pmatrix}e^{L+h}&e^{-L}\\e^{-L}&e^{L-h}\end{pmatrix}
 =cT+d\sigma_x,\quad
 \sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
There are exactly \(N-2\) bulk transfer factors, so by cyclicity
\(Z_N=\operatorname{tr}(T_L^2T^{N-2})\). The determinant of \(T\) is \(D\). Cayley–Hamilton gives, with first- and second-kind Chebyshev polynomials \(T_j(x)\) and \(U_j(x)\),
\[
\operatorname{tr}(T^j)=2D^{j/2}T_j(x),\qquad
\operatorname{tr}(\sigma_xT^{N-1})=2bD^{(N-2)/2}U_{N-2}(x).
\]
Consequently,
\[
 Z_N(h)=2D^{(N-2)/2}F_N(x),\qquad
 F_N(x)=c^2D\,T_N(x)+d^2T_{N-2}(x)
 +2cdb\,U_{N-2}(x). \tag{1}
\]
This is a real polynomial of degree exactly \(N\), with leading coefficient \(c^2D\,2^{N-1}>0\). It has parity \(F_N(-x)=(-1)^NF_N(x)\).

**2. At least \(N-2\) real interior roots.** For \(j=0,\ldots,N-1\) set \(x_j=\cos(j\pi/(N-1))\). At every such node, \(U_{N-2}(x_j)=0\) for interior nodes, and the same identity holds at endpoints *only after accounting for the nonzero endpoint value of* \(U_{N-2}\). Therefore, for the sign argument use instead the interior nodes \(j=1,\ldots,N-2\), where
\[
 F_N(x_j)=(-1)^j x_j(c^2D+d^2). \tag{2}
\]
To obtain the outermost intervals, one also needs direct endpoint values, not the invalid extension of (2) to \(j=0,N-1\). They obey
\[
 F_N(1)=c^2D+d^2+2cdb(N-1),\qquad F_N(-1)=(-1)^NF_N(1). \tag{3}
\]
For the parameter range in which the off-circle pair is asserted, \(L<0\), we have \(c,d,b>0\), hence \(F_N(1)>0\), and (2)–(3) give alternating signs on each side of zero, except across the central gap. This yields \(N-2\) distinct roots in \((-1,1)\) for either parity, including the automatic root \(x=0\) when \(N\) is odd.

For the *all-on-circle* regime with \(L\ge0\), if \(d\) becomes negative, the boundary-node signs alone may not secure outermost intervals. In that regime the classical Lee–Yang circle theorem for nonnegative Ising couplings supplies the all-on-circle conclusion directly. For \(L\le0\), \(d\ge0\), so all subsequent sign arguments use (2)–(3) without extra assumptions.

**3. Exact central sign tests.** The identities \(T_{2m}(0)=(-1)^m\), \(U_{2m-2}(0)=(-1)^{m-1}\), and the derivatives of their odd counterparts give
\[
 \frac{F_{2m}(0)}{(-1)^m}
 =c^2D-d^2-2cdb=e^{2L}-e^{-2L}=u-u^{-1}, \tag{4}
\]
\[
 \frac{F_{2m+1}'(0)}{(-1)^m}
 =(2m+1)c^2D-(2m-1)d^2-4m cdb
 =Nu-\frac{N-2}{u}-2q. \tag{5}
\]
For even \(N\), the sign changes at \(L=0\). For odd \(N\), the sign changes at the unique positive root of \(Nu^2-2qu-(N-2)=0\), namely \(u_N(q)\). Strict monotonicity of the left-hand expression in \(u>0\) makes this threshold unique. At each threshold, zero is at least a double (even case) or triple (odd case) root of \(F_N\).

**4. Two additional on-circle zeros before the threshold.** For \(L<0\), use the positive interior node closest to zero, \(x_{m-1}\), and the sign from (2), which is \((-1)^{m-1}\). When \(N=2m\) and \(L<0\), the central value in (4) has sign \((-1)^{m+1}\), the same as \(F_N(x_{m-1})\), so it gives no new real root. When \(N=2m\) and \(L=0\), zero is double and the \(N-2\) already counted sign-change roots account for all multiplicity. For \(N=2m+1\), if the quantity in (5) is positive, the sign immediately to the right of zero is \((-1)^m\), opposite to that at \(x_{m-1}\); there is one further positive real root and one symmetric negative root. Hence all \(N\) roots lie in \((-1,1)\). If the quantity in (5) vanishes, zero has multiplicity at least three; together with the \(N-3\) nonzero interior sign-change roots this exhausts degree \(N\), so its multiplicity is exactly three. For even \(L>0\) and odd \(L\ge0\) the ferromagnetic Lee–Yang theorem supplies the circle conclusion, with no need to assert the strong \((-1,1)\) location of every \(x\)-root.

**5. The missing pair is purely imaginary.** When \(N\) is even and \(L<0\), set \(H(y)=i^{-N}F_N(iy)\), real for \(y\ge0\). Equation (4) makes \(H(0)<0\), whereas the positive leading coefficient makes \(H(y)\to+\infty\). A root \(iy\) exists for some \(y>0\). Polynomial parity supplies \(-iy\). When \(N\) is odd and \(u<u_N(q)\), use instead \(H(y)=i^{-N}F_N(iy)/y\) on \(y>0\), extended continuously to zero. Equation (5) makes \(H(0)<0\), and its leading coefficient makes \(H(y)\to+\infty\). Again \(\pm iy\) are roots for some \(y>0\). Combined with the \(N-2\) real roots established in step 2, these exhaust degree \(N\): the pair is unique and simple.

**6. Mapping to field fugacity.** Let \(\kappa=\sqrt{1-e^{-4K}}\in(0,1)\), so that \(\cosh h=\kappa x\). If \(x\in(-1,1)\) is real, then \(h\) can be chosen purely imaginary and \(|z|=|e^{2h}|=1\). If \(x=\pm iy\) is a missing-root pair, its two fugacity zeros are exactly
\[
 z_{\pm}=-\exp\left(\pm 2\operatorname{arsinh}(\kappa y)\right),
\]
which are negative, real, reciprocal, and strictly off-circle. The involution \(x\mapsto-x\) corresponds to the same two fugacity values under \(h\mapsto i\pi-h\); the root counts therefore transfer faithfully from the degree-\(N\) Chebyshev polynomial to the degree-\(N\) fugacity polynomial. At \(x=0\), \(z=-1\), and multiplicity of the central root is preserved. This completes the classification.

## Verification

A self-contained Python 3 script, `verify.py`, recomputes the transfer traces and directly enumerates all spin configurations for rational exponential couplings. It performed **321 exact-rational consistency and boundary-coefficient checks** across ring sizes \(3\le N\le10\), two bulk couplings, four impurity couplings, and two real-field values. The code uses only the Python standard library; run `python3 verify.py` from the folder containing the extracted package. These finite checks are diagnostic, not a replacement for the all-\(N\) sign-count proof above.

## Relationship to prior work

Dantchev's October 2026 paper gives the exactly solvable two-bond impurity model, its transfer representation and thermodynamic observables, but does not give a Lee–Yang zero-location classification. Tonchev and Dantchev's 2024 work describes Chebyshev zero methods for a uniform ring and antiperiodic one-bond seam; their 2026 single-defect work and 2026 work on periodically modulated finite chains provide related transfer machinery. A one-bond antiperiodic seam is *not* the same as two equal antiferromagnetic bonds incident on a single spin: the parity-dependent thresholds, triple collision, and unique off-circle reciprocal pair here are not implied by the listed results. The ferromagnetic portion of the claim is a special case of the classical Lee–Yang theorem and is not proposed as a new theorem.

## Limitations

The result concerns a finite one-dimensional nearest-neighbor system with two **equal** defect couplings and fixed positive bulk coupling. It makes no claim about unequal defects, higher-dimensional systems, or thermodynamic accumulation measures. Its central novelty concerns the antiferromagnetic impurity and the exact finite-volume parity threshold. Although relevant published sources were inspected, other unindexed generalizations may imply the classification. Numerical checks alone cannot establish completeness.

## References

1. D. M. Dantchev, *Casimir Force, Magnetization, and Susceptibility for Ising Chain with an Impurity Atom in the Presence of an External Field* (2026), arXiv:2610.04035v1, first public 2026-10-02, https://arxiv.org/abs/2610.04035 .
2. N. Tonchev and D. Dantchev, *Chebyshev Polynomials in the Physics of the One-Dimensional Finite-Size Ising Model: An Alternative View and Some New Results*, Condensed Matter 9 (2024) 53, https://doi.org/10.3390/condmat9040053 .
3. N. Tonchev and D. Dantchev, *The Algebra of Chebyshev Polynomials and the Transfer-Matrix Approach for the One-Dimensional Ising Model with a Defect*, Mathematics 14 (2026) 741, https://doi.org/10.3390/math14040741 .
4. N. Tonchev and D. Dantchev, *GL(2,R) in the Finite One-Dimensional Ising Model with Nonuniform Couplings*, Axioms 15 (2026) 599, https://doi.org/10.3390/axioms15080599 .
5. T. D. Lee and C. N. Yang, *Statistical Theory of Equations of State and Phase Transitions. II. Lattice Gas and Ising Model*, Phys. Rev. 87 (1952) 410, https://doi.org/10.1103/PhysRev.87.410 .
