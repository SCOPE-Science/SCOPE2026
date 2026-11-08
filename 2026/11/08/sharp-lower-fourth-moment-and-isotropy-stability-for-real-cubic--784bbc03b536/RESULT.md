# Sharp lower fourth moment and isotropy stability for real cubic spherical harmonics

## Finding
Let \(\sigma\) be probability surface measure on \(\mathbb S^2\). Every nonzero real spherical harmonic \(h\) of degree three satisfies the **sharp** reverse fourth-moment inequality
\[
\frac{\int_{\mathbb S^2}h^4\,d\sigma}{\bigl(\int_{\mathbb S^2}h^2\,d\sigma\bigr)^2}\geq \frac{315}{143}.
\]
Write its homogeneous harmonic extension as \(H(x)=\sum_{i,j,k=1}^3T_{ijk}x_ix_jx_k\), with \(T\) real, fully symmetric and trace-free, and put
\[
E=\sum_{i,j,k}T_{ijk}^2,\quad B_{ij}=\sum_{k,l}T_{ikl}T_{jkl}.
\]
Then the following **exact remainder identity** holds:
\[
\frac{\int h^4\,d\sigma}{(\int h^2\,d\sigma)^2}-\frac{315}{143}
=\frac{210}{143E^2}\left\|B-\frac E3I_3\right\|_{\mathrm F}^2.
\]
Equality occurs **if and only if** \(B=(E/3)I_3\); this is an intrinsic algebraic characterization of *all* equality tensors, not a claim that a single coordinate representative exhausts them. Equality is attained, for example, by any nonzero scalar multiple or orthogonal image of \(h(x,y,z)=xyz\). The value \(350/143\) for \(h=x(x^2-3y^2)\) demonstrates that the fourth moment is not constant across the cubic harmonic space.

## Assumptions and scope
The sphere has radius one and \(d\sigma=dS/(4\pi)\). The harmonic \(h\) is real-valued, nonzero, and belongs to the exact seven-dimensional eigenspace of \(-\Delta_{\mathbb S^2}\) with eigenvalue \(12\). The tensor \(T\) has all indices in \(\{1,2,3\}\); trace-free means \(\sum_iT_{iik}=0\) for each \(k\). Norms in the finding are ordinary scalar \(L^p(\sigma)\) norms; the tensor norm \(\|\cdot\|_{\mathrm F}\) is the sum-of-squares matrix norm. There are no asymptotic, numerical, or genericity hypotheses.

## Proof
The harmonic extension identifies the real degree-three eigenspace with fully symmetric trace-free rank-three tensors on \(\mathbb R^3\). The tensor is uniquely determined by \(T_{ijk}=\partial_i\partial_j\partial_kH/6\), and \(E>0\) for nonzero \(h\). The matrix \(B\) is positive semidefinite and \(\operatorname{tr}B=E\).

For any nonnegative integers \(a,b,c\), integration against the normalized sphere satisfies
\[
\int_{\mathbb S^2}x^{2a}y^{2b}z^{2c}\,d\sigma
=\frac{(2a-1)!!(2b-1)!!(2c-1)!!}{(2a+2b+2c+1)!!},
\]
with \((-1)!!=1\); monomials with an odd exponent integrate to zero. By expanding a general trace-free cubic in a basis and applying this formula coefficient by coefficient, one obtains the two **exact polynomial identities**
\[
\int h^2\,d\sigma=\frac{2E}{35},\qquad
\int h^4\,d\sigma=\frac{4E^2}{715}+\frac{24}{5005}\operatorname{tr}(B^2).
\]
To make the quartic identity fully checkable rather than relying on a sample of tensors, take the general linear combination of the seven harmonic cubics
\[
5z^3-3zr^2,\quad x(5z^2-r^2),\quad y(5z^2-r^2),\quad
z(x^2-y^2),\quad 2xyz,\quad x(x^2-3y^2),\quad y(3x^2-y^2),
\]
where \(r^2=x^2+y^2+z^2\). These span the entire space. The included `check_cubic_moments.py` forms both sides as rational polynomials in **seven arbitrary real coefficients**, verifies every possible monomial coefficient (all \(\binom{10}{4}=210\) degree-four coefficient slots), and separately verifies the quadratic identity. Thus this check is a complete finite symbolic verification of a universal polynomial identity, not point sampling or a numerical conjecture. It uses only the displayed monomial-integration rule and partial differentiation.

Dividing the quartic identity by the square of the quadratic identity yields
\[
\frac{\int h^4\,d\sigma}{(\int h^2\,d\sigma)^2}
=\frac{245}{143}+\frac{210}{143}\frac{\operatorname{tr}(B^2)}{E^2}.
\]
Because \(B\) is real symmetric with trace \(E\), the decomposition \(B=(E/3)I_3+[B-(E/3)I_3]\) gives
\[
\operatorname{tr}(B^2)=\frac{E^2}{3}+\left\|B-\frac E3I_3\right\|_{\mathrm F}^2.
\]
Substitution proves the exact remainder, sharp lower constant and the necessary-and-sufficient equality criterion. Finally \(H=xyz\) has \(T_{123}=1/6\) and its five other permutations equal to \(1/6\), with all other entries zero. Hence \(E=1/6\) and \(B=(1/18)I_3\), giving equality and sharpness.

## Verification
Run `python check_cubic_moments.py` with Python 3 and SymPy. The program exactly tests the harmonic basis rank, every quadratic and quartic coefficient identity, the isotropic equality example, and a non-isotropic comparison, using rational arithmetic. The completed execution returned `ALL_CUBIC_HARMONIC_MOMENT_CHECKS_OK`. The all-tensor conclusion follows from the complete polynomial identity and spectral nonnegativity; any finite trial configuration alone would be insufficient.

## Relationship to prior work
Stanton and Weinstein's 1981 spherical-harmonic fourth-norm study proves a *local maximum* property of real highest-weight harmonics across degrees. The present finding instead gives a **global minimum** at degree three, an exact quadratic-covariant remainder and an intrinsic iff equality criterion; the cited local-maximum theorem does not imply these statements. Sogge and Zelditch's first publicly posted 2010 analysis studies \(L^4\) behavior of typical, high-degree eigenfunctions and bases, not this degree-three sharp lower constant. The general degree-two sharp fourth norm available in separate related records concerns a distinct eigenspace, and its norm is flat among real quadratics on \(\mathbb S^2\); the cubic case does not follow by identifying the two harmonic degrees.

## Limitations
This result is for **real** harmonics of degree exactly three on the unit two-sphere, not complex coefficients, other degrees, other dimensions, or the sharp **upper** fourth-moment constant. The condition \(B=(E/3)I_3\) is an exact algebraic characterization of equality, not an independent classification of orthogonal orbits. Equivalent formulations may exist in older tensor-invariant or harmonic-analysis literature; the literature comparison is a best-knowledge search, not a mathematical proof of novelty. No independent mathematical validation is claimed.

## References
1. R. J. Stanton and A. Weinstein, *On the L4 norm of spherical harmonics*, Math. Proc. Cambridge Philos. Soc. **89** (1981), 343–358. DOI: https://doi.org/10.1017/S0305004100058229. The accessible author-uploaded text is at https://www.researchgate.net/publication/231819295_On_the_L_norm_of_spherical_harmonics.
2. C. D. Sogge and S. Zelditch, *Concerning the L4 norms of typical eigenfunctions on compact surfaces*, arXiv:1011.0215v1, first publicly posted 2010-10-31, https://arxiv.org/abs/1011.0215.
3. J.-H. Lu, *A note on a theorem of Stanton–Weinstein on the L4-norm of spherical harmonics*, Math. Proc. Cambridge Philos. Soc. **102** (1987), 561–563, DOI: https://doi.org/10.1017/S0305004100067591 (accessible abstract only).
