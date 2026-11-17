# Sharp rotation distortion of the planar endpoint second-jet Sobolev norm

## Finding
For the real Sobolev space \(W^{2,1}(\mathbb R^2)\), define
\[
 \mathcal N(f)=\|f\|_1+\|f_x\|_1+\|f_y\|_1+\|f_{xx}\|_1+\|f_{xy}\|_1+\|f_{yy}\|_1.
\]
For every real angle \(\theta\), let \(R_\theta\) be the counterclockwise planar rotation through \(\theta\), and let \(U_\theta f=f\circ R_\theta\). Then the exact operator norm is
\[
 \boxed{\|U_\theta\|_{\mathcal N\to\mathcal N}=2|\sin(2\theta)|+|\cos(2\theta)|.}
\]
In particular, the composition operators are isometries exactly when \(\theta\in(\pi/2)\mathbb Z\), but the maximal distortion among *all* rotations is
\[
 \boxed{\max_{\theta\in\mathbb R}\|U_\theta\|=\sqrt5.}
\]
Equality in the maximum holds exactly when \(|\sin(2\theta)|=2/\sqrt5\) and \(|\cos(2\theta)|=1/\sqrt5\). At diagonal rotations \(\theta\in\pi/4+(\pi/2)\mathbb Z\), the norm is \(2\), a strict local cusp minimum, not the global maximum. The exact infinitesimal distortion is
\[
 \lim_{\theta\to0}\frac{\|U_\theta\|-1}{|\theta|}=4.
\]

## Assumptions and scope
All functions are real-valued; all weak derivatives up to order two are integrable with respect to Lebesgue measure on \(\mathbb R^2\). Each mixed derivative appears **once**, rather than with binomial multiplicity. Rotations act by composition \(f\mapsto f\circ R_\theta\); they preserve Lebesgue measure. All angles are real, including multiples of \(\pi/2\), so no positivity or small-angle restriction is imposed. The operator norm is the supremum of \(\mathcal N(U_\theta f)/\mathcal N(f)\) over nonzero functions.

The crucial analytic input is the classical endpoint \(L^1\) non-inequality of Ornstein in its scalar second-order planar form: for every \(\varepsilon>0\) there exists real \(\varphi\in C_c^\infty(\mathbb R^2)\) with \(\|\varphi_{xy}\|_1>0\) and
\[
 \|\varphi_{xx}\|_1+\|\varphi_{yy}\|_1<\varepsilon\|\varphi_{xy}\|_1.
\]
This is a cited established theorem, not a new lemma of the finding.

## Proof
Write \(c=\cos\theta\), \(s=\sin\theta\). By the chain rule, with every derivative of \(f\) evaluated at \(R_\theta(x,y)\),
\[
 \begin{aligned}
 (U_\theta f)_x&=c f_x+s f_y,&(U_\theta f)_y&=-s f_x+c f_y,\\
 (U_\theta f)_{xx}&=c^2f_{xx}+2csf_{xy}+s^2f_{yy},\\
 (U_\theta f)_{xy}&=-csf_{xx}+(c^2-s^2)f_{xy}+csf_{yy},\\
 (U_\theta f)_{yy}&=s^2f_{xx}-2csf_{xy}+c^2f_{yy}.
 \end{aligned}
\]
Since rotations preserve area, triangle inequalities give the operator-norm upper bound from the maximal absolute column sums of the zeroth-, first-, and second-order derivative matrices:
\[
 \|U_\theta\|\le \max\left\{1,\ |c|+|s|,\ 1+|cs|,\ |c^2-s^2|+4|cs|\right\}.
\]
Let \(t=2|cs|=|\sin(2\theta)|\), \(u=|c^2-s^2|=|\cos(2\theta)|\), so \(0\le t,u\le1\) and \(t^2+u^2=1\). The last column sum is \(2t+u\). Because \(u\ge1-t\), it satisfies
\[
 2t+u\ge1+t\ge1+t/2=1+|cs|\ge\sqrt{1+t}=|c|+|s|.
\]
Hence the upper bound simplifies to \(\|U_\theta\|\le2t+u\).

For sharpness, apply Ornstein's non-inequality with \(\varepsilon=1/j\) to choose real \(\varphi_j\in C_c^\infty\) with nonzero \(\|\partial_{xy}\varphi_j\|_1\) and with the sum of its two pure second-derivative norms at most \(\|\partial_{xy}\varphi_j\|_1/j\). Replace \(\varphi_j\) by \(f_j(x)=\varphi_j(x/\delta_j)\), with \(\delta_j>0\) so small that \(\|f_j\|_1+\|\nabla f_j\|_{L^1,\ell^1}\le \|\partial_{xy}f_j\|_1/j\). Such a choice exists because in two dimensions the second-derivative \(L^1\) norms are invariant under this dilation, whereas first- and zeroth-order norms acquire factors \(\delta_j\) and \(\delta_j^2\).

The second-derivative transformation displays the \(f_{xy}\) coefficient vector \((2cs,c^2-s^2,-2cs)\). For each of the three transformed second derivatives, the reverse triangle inequality subtracts only a bounded linear combination of \(\|f_{xx}\|_1\) and \(\|f_{yy}\|_1\). Summing yields
\[
 \liminf_{j\to\infty}\frac{\mathcal N(U_\theta f_j)}{\mathcal N(f_j)}\ge 4|cs|+|c^2-s^2|=2t+u.
\]
Together with the upper bound, this proves the formula for every \(\theta\), including those where one or more coefficients vanish.

Finally, \((t,u)\) lies on the unit quarter circle, so by Cauchy–Schwarz,
\[
 2t+u\le\sqrt{2^2+1^2}\sqrt{t^2+u^2}=\sqrt5,
\]
with equality precisely at \((t,u)=(2/\sqrt5,1/\sqrt5)\). The norm equals one precisely when \(t=0\), i.e. \(\theta\in(\pi/2)\mathbb Z\). At \(t=1\), \(u=0\), it equals two, while moving slightly to either side increases \(u\) linearly and decreases \(2t\) only quadratically; hence each diagonal angle is a strict cusp minimum. Taylor expansion at zero gives \(t=2|\theta|+O(|\theta|^3)\) and \(u=1+O(\theta^2)\), proving the infinitesimal limit.

## Verification
The standalone `rotation_checker.py` performs exact rational arithmetic on 1,158 normalized rational rotations (including sign choices), verifying the Hessian chain-rule column sums, dominance comparisons, and the universal squared upper bound five. It ran successfully with `ROTATION_JET_CHECKS_OK 10423`. These finite checks confirm algebraic identities only: the sharpness for all angles and all Sobolev functions is proved by the published endpoint non-inequality and the scaling argument. The checker uses only the Python standard library; run `python rotation_checker.py`.

## Relationship to prior work
Hamad's 2026 paper establishes the isometric classification for this derivative-sum norm; an isometry classification distinguishes norm one from norm greater than one but does not by itself give the exact distortion profile or the nonmonotone maximum \(\sqrt5\). Ornstein's classical non-inequality, with the modern account by Faraco and Guerra, is the indispensable sharpness tool and is not claimed as new.

A prior result on exact norms of planar *shears* for the same endpoint Sobolev scale treats the nonorthogonal shear subgroup. Its theorem does not state the sharp rotation profile. Factoring a rotation into shears gives submultiplicative bounds, not the equality established here. Related published work on rotation-invariant isotropic Sobolev norms concerns a different normalization: the derivative sum here assigns one copy of each mixed derivative and is not rotation invariant.

## Limitations
This finding concerns the real planar order-two derivative-sum norm, not arbitrary orders, dimensions, volume-preserving nonlinear maps, or optimizers among all linear coordinate transformations. Sharpness is via sequences and does not assert existence or nonexistence of a norm-attaining function. A broader unpublished or inaccessible change-of-variables norm formula could imply the result; literature coverage is not a proof of publication priority. The cited 2026 source could be inspected at abstract level only; its full text remained inaccessible during this comparison.

## References
1. S. Hamad, *Isometric Classification of Sobolev Spaces*, arXiv:2611.09577, first publicly submitted 2026-11-06, https://arxiv.org/abs/2611.09577.
2. D. S. Ornstein, *A non-inequality for differential operators in the \(L^1\) norm*, Arch. Rational Mech. Anal. (1962), DOI:10.1007/BF00253928.
3. D. Faraco and A. Guerra, *Remarks on Ornstein's non-inequality in \(\mathbb R^{2\times2}\)*, Quart. J. Math. 73 (2022), 17–21, arXiv:2006.09060, DOI:10.1093/qmath/haab016.
