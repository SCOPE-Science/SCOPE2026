# Condition number two is the sharp second-step positivity frontier for GMRES on diagonal SPD systems

## Finding
Let
\[
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\qquad
0<\mu\le\lambda_i\le L,
\qquad
\kappa=\frac L\mu,
\]
and let \(b\ge0\), \(b\ne0\). Run exact-arithmetic unrestarted GMRES from
\[
x_0=0.
\]
If the method has already converged before a second step is needed, regard \(x_2\) as that exact solution.

Then
\[
\boxed{
\kappa\le2
\quad\Longrightarrow\quad
x_2\ge0
\text{ for every such }A,b.
}
\]
The constant \(2\) is sharp. For every \(\kappa>2\), a three-dimensional diagonal SPD system with condition number exactly \(\kappa\) and a strictly positive right-hand side has a negative component in its second GMRES iterate.

More precisely, when at least two distinct eigenvalues are active, write
\[
x_2=a b-cAb.
\]
Then
\[
\frac ac
\]
is a positive weighted average of pair sums
\[
\lambda_i+\lambda_j.
\]
Consequently
\[
\frac ac\ge2\mu,
\]
and
\[
(x_2)_i
=
cb_i\left(\frac ac-\lambda_i\right).
\]
This proves positivity whenever \(L\le2\mu\).

For sharpness, normalize \(\mu=1\) and take
\[
A_\kappa
=
\operatorname{diag}\left(1,\frac\kappa2,\kappa\right),
\qquad
b_\delta=(1,1,\delta)^{\mathsf T}.
\]
For every \(\kappa>2\), choosing
\[
0<\delta^2<
\frac{(\kappa-2)^3}
{\kappa^4+16(\kappa-1)^2}
\]
makes the third component of \(x_2\) strictly negative.

An exact small witness is
\[
A=
\operatorname{diag}\left(1,\frac32,3\right),
\qquad
b=
\left(1,1,\frac1{20}\right)^{\mathsf T}.
\]
Here
\[
x_2=
\left(
\frac{527}{545},
\frac{374}{545},
-\frac{17}{2180}
\right)^{\mathsf T},
\]
although
\[
A^{-1}b=
\left(
1,\frac23,\frac1{60}
\right)^{\mathsf T}>0.
\]
Thus residual minimization can cross the boundary of the positive orthant even for a perfectly diagonal SPD problem, but this cannot happen at the second step until the spectral condition number exceeds \(2\).

## Assumptions and scope
The theorem concerns exact-arithmetic, unrestarted GMRES with initial guess \(x_0=0\), diagonal positive-definite \(A\), and componentwise nonnegative \(b\). Components with \(b_i=0\) are inactive and remain zero.

If the active spectrum contains only one point, GMRES is exact after one step. If it contains only two points, GMRES is exact after at most two steps. Thus the nontrivial sign-loss mechanism requires at least three distinct active eigenvalues.

For symmetric problems, the same residual-minimizing iterate is obtained by MINRES in exact arithmetic. The claim is specifically the sharp condition-number classification for the second iterate on diagonal SPD systems, not a general positivity theorem for arbitrary SPD or Stieltjes matrices.

The first GMRES iterate is always nonnegative in this setting because
\[
x_1=\alpha b,
\qquad
\alpha=
\frac{b^{\mathsf T}Ab}{b^{\mathsf T}A^2b}>0.
\]
Hence iteration two and three active spectral points are jointly minimal for the phenomenon studied here.

## Proof
Let
\[
w_i=b_i^2
\]
and define moments
\[
m_j=\sum_i w_i\lambda_i^j.
\]
At step two,
\[
x_2=a b-cAb
\]
for some scalars \(a,c\), and the residual is
\[
r_2
=
b-Ax_2
=
\left(I-aA+cA^2\right)b.
\]
GMRES minimizes \(\|r_2\|_2\), so the residual is orthogonal to
\[
A\mathcal K_2(A,b)
=
\operatorname{span}\{Ab,A^2b\}.
\]
Therefore
\[
m_1-a m_2+c m_3=0,
\qquad
m_2-a m_3+c m_4=0.
\]
If there are at least two distinct active eigenvalues, strict Cauchy--Schwarz gives
\[
m_2m_4-m_3^2>0.
\]
Solving the two equations gives
\[
c=
\frac{m_1m_3-m_2^2}{m_2m_4-m_3^2}>0
\]
and
\[
\frac ac
=
\frac{m_1m_4-m_2m_3}
{m_1m_3-m_2^2}.
\]

The two moment differences have exact pairwise expansions:
\[
m_1m_3-m_2^2
=
\sum_{i<j}
w_iw_j\lambda_i\lambda_j(\lambda_i-\lambda_j)^2
\]
and
\[
m_1m_4-m_2m_3
=
\sum_{i<j}
w_iw_j\lambda_i\lambda_j(\lambda_i-\lambda_j)^2
(\lambda_i+\lambda_j).
\]
Terms with equal eigenvalues or zero right-hand-side components vanish. Hence
\[
s:=\frac ac
\]
is a weighted average of the sums of two distinct active eigenvalues. In particular,
\[
s\ge2\mu.
\]
Each coordinate of the iterate is
\[
(x_2)_i
=
b_i(a-c\lambda_i)
=
cb_i(s-\lambda_i).
\]
If
\[
\kappa=\frac L\mu\le2,
\]
then
\[
s\ge2\mu\ge L\ge\lambda_i,
\]
so every coordinate is nonnegative.

It remains to prove sharpness. Let \(\kappa>2\) and set
\[
A_\kappa=
\operatorname{diag}\left(1,\frac\kappa2,\kappa\right),
\qquad
b_\delta=(1,1,\delta)^{\mathsf T}.
\]
Put
\[
\varepsilon=\delta^2.
\]
For these three weights, direct substitution into the moment formula yields
\[
\kappa(m_1m_3-m_2^2)
-
(m_1m_4-m_2m_3)
=
\frac{\kappa}{16}
\left[
(\kappa-2)^3
-
\varepsilon\bigl(\kappa^4+16(\kappa-1)^2\bigr)
\right].
\]
Therefore the displayed upper bound on \(\delta^2\) makes
\[
s=\frac ac<\kappa.
\]
Since \(c>0\) and \(\delta>0\),
\[
(x_2)_3
=
c\delta(s-\kappa)<0.
\]
This gives a counterexample for every \(\kappa>2\).

Finally, if there are at most two distinct active eigenvalues, the degree-two Krylov space contains the exact inverse action on the active spectrum, so GMRES is exact by step two. Thus three active eigenvalues are minimal for sign loss.

## Verification
The embedded `verify.py` uses exact rational arithmetic.

It checks the pairwise moment identities on several finite rational spectra, reconstructs the GMRES coefficients \(a,c\) from the exact normal equations, and verifies the exact \(\kappa=3\) witness
\[
a=\frac{833}{545},
\qquad
c=\frac{306}{545},
\]
\[
x_2=
\left(
\frac{527}{545},
\frac{374}{545},
-\frac{17}{2180}
\right)^{\mathsf T}.
\]
It also verifies
\[
\|r_0\|_2^2=\frac{801}{400},
\qquad
\|r_1\|_2^2=\frac{25}{308},
\qquad
\|r_2\|_2^2=\frac4{545},
\]
so the negative solution component occurs while the GMRES residual norm decreases normally.

The universal \(\kappa\le2\) implication and the all-\(\kappa>2\) sharpness family are proved analytically above; finite checks are not used as substitutes for those quantifiers.

## Relationship to prior work
Classical GMRES theory characterizes the \(k\)-th residual through a degree-\(k\) polynomial that equals one at the origin. Goossens and Roose identify the zeros of GMRES residual polynomials with harmonic Ritz values. Their analysis concerns Ritz values, harmonic Ritz values, breakdown, stagnation, and residual convergence rather than componentwise signs of solution iterates.

Meurant and Duintjer Tebbens give explicit residual-norm formulas for diagonalizable and normal matrices. For normal matrices they show that the GMRES residual norm is determined by the eigenvalues together with the right-hand-side components in the eigenvector basis. Their full text does not state a componentwise positivity classification.

Meurant later derives closed-form coefficients of FOM and GMRES residual polynomials for diagonalizable matrices and explicit harmonic Ritz formulas for early iterations. That coefficient theory supplies nearby background, but the exact pair-sum representation above and the sharp positivity frontier
\[
\kappa=2
\]
are not stated in the inspected source.

Targeted searches using GMRES, MINRES, diagonal SPD systems, nonnegative right-hand sides, componentwise positivity, sign preservation, harmonic Ritz values, and condition-number thresholds did not locate an implication-equivalent statement. A closely related observation is that symmetric GMRES and MINRES generate the same residual-minimizing iterates in exact arithmetic; this does not by itself provide the condition-number classification proved here.

## Limitations
The theorem is restricted to the second iterate and diagonal SPD matrices. It does not give a positivity criterion for later GMRES iterates, arbitrary SPD matrices in a fixed coordinate basis, general Stieltjes matrices, preconditioned GMRES, restarted GMRES, or finite-precision arithmetic.

Condition number \(2\) is a universal second-step threshold, not a claim that every problem with larger condition number loses positivity. Two-active-eigenvalue problems remain exact and positive at step two for arbitrarily large condition number.

The sharpness construction is three-dimensional and uses a right-hand-side weight that can become small as \(\kappa\downarrow2\). No lower bound on all right-hand-side components is asserted.

Residual-polynomial root theory is classical, so residual originality risk remains that the pair-sum consequence or the same \(2\)-threshold was previously recorded under a positivity-preserving Krylov, pseudo-Ritz, or orthogonal-polynomial formulation not recovered by the searches.

## References
1. S. Goossens and D. Roose, “Ritz and harmonic Ritz values and the convergence of FOM and GMRES,” Numerical Linear Algebra with Applications 6 (1999), 281–293, DOI 10.1002/(SICI)1099-1506(199906)6:4<281::AID-NLA158>3.0.CO;2-B. First published 1999-09-24.
2. G. Meurant and J. Duintjer Tebbens, “The role eigenvalues play in forming GMRES residual norms with non-normal matrices,” Numerical Algorithms 68 (2015), 143–165, DOI 10.1007/s11075-014-9891-3. Published online 2014-07-16.
3. G. Meurant, “The Coefficients of the FOM and GMRES Residual Polynomials,” SIAM Journal on Matrix Analysis and Applications 38 (2017), 96–117, DOI 10.1137/15M1053827.
