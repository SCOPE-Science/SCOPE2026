# Sharp variation-optimal affine-reproducing cubic Hermite slopes on alternating meshes

## Finding

Let two positive lengths \(a,b\) alternate along a bi-infinite real knot sequence. Among all local \(C^1\) piecewise-cubic Hermite interpolation operators that use an arbitrary **fixed convex combination of the left and right secants** as their derivative at each knot, the minimum possible sharp discrete-to-continuous total-variation amplification is

\[
\boxed{K_*(a,b)=1+\frac{16ab}{27(a^2+b^2)}.}
\]

It is attained by the two-periodic knot-derivative weights \(\lambda_{2j}=b^2/(a^2+b^2)\) and \(\lambda_{2j+1}=a^2/(a^2+b^2)\). The best coefficient is \(35/27\) on a uniform grid but tends to 1 at extreme alternating mesh contrast. This is a *fixed, linear, affine-reproducing* interpolation design result. The restricted admissible class is essential.

## Assumptions and scope

Fix \(a,b>0\) and strictly increasing knots \((x_i)_{i\in\mathbb Z}\) such that \(h_i=x_{i+1}-x_i=a\) for even \(i\) and \(b\) for odd \(i\). Thus \(x_i\to\pm\infty\). For every real sequence \(y=(y_i)\) with \(V_d(y)=\sum_{i\in\mathbb Z}|y_{i+1}-y_i|<\infty\), define secants \(d_i=(y_{i+1}-y_i)/h_i\). Fix independently of \(y\) any weight sequence \(\lambda_i\in[0,1]\) and knot slopes

\[
m_i=\lambda_i d_{i-1}+(1-\lambda_i)d_i.
\]

On \([x_i,x_{i+1}]\), with \(t=(x-x_i)/h_i\), define \(\mathcal H_\lambda y\) as the polynomial

\[
 y_i(2t^3-3t^2+1)+y_{i+1}(-2t^3+3t^2)
 +h_i m_i(t^3-2t^2+t)+h_i m_{i+1}(t^3-t^2).
\]

It is a bounded \(C^1(\mathbb R)\) interpolant, reproduces constants and affine functions, and its variation seminorm is \(\operatorname{Var}_{\mathbb R}(f)=\sup_{z_0<\cdots<z_m}\sum_{k=1}^m|f(z_k)-f(z_{k-1})|\). Define its sharp quotient norm as the supremum of \(\operatorname{Var}_{\mathbb R}(\mathcal H_\lambda y)/V_d(y)\) for \(V_d(y)>0\). Coefficients need not be periodic for the lower bound or optimization.

## Proof

**Step response lemma.** Let \(e^{(k)}_i=0\) for \(i\le k\) and \(e^{(k)}_i=1\) for \(i>k\). Its only nonzero secant is \(d_k=1/h_k\). The only possibly nonzero knot derivatives are

\[
m_k=(1-\lambda_k)/h_k,\qquad m_{k+1}=\lambda_{k+1}/h_k.
\]

The interpolant is constant except on the three cells indexed \(k-1,k,k+1\). On the middle cell it runs from zero to one with normalized endpoint slopes \(\alpha=1-\lambda_k\), \(\beta=\lambda_{k+1}\), both in \([0,1]\). Its derivative in normalized coordinates is

\[
6t(1-t)+\alpha(3t^2-4t+1)+\beta(3t^2-2t).
\]

This is nonnegative for all \(t\in[0,1]\): being affine in \((\alpha,\beta)\), its minimum over the unit square is at a corner. The four corner derivatives are \(6t(1-t)\), \((1-t)(1+3t)\), \(t(4-3t)\), and \(1\). Thus the middle cell contributes variation 1.

On the left cell the polynomial is \(h_{k-1}(1-\lambda_k)(t^3-t^2)/h_k\), which vanishes at both ends, reaches its negative minimum at \(t=2/3\), and has total variation \(\frac8{27}\frac{h_{k-1}}{h_k}(1-\lambda_k)\). On the right cell it equals 1 plus \(h_{k+1}\lambda_{k+1}(t^3-2t^2+t)/h_k\), with positive maximum at \(t=1/3\), adding \(\frac8{27}\frac{h_{k+1}}{h_k}\lambda_{k+1}\). Consequently

\[
\operatorname{Var}_{\mathbb R}(\mathcal H_\lambda e^{(k)})
=1+\frac8{27}\frac{h_{k-1}(1-\lambda_k)+h_{k+1}\lambda_{k+1}}{h_k}.
\]

**Reduction to steps.** Any finite-variation sequence is \(y=c\mathbf1+\sum_{k\in\mathbb Z}\Delta_k e^{(k)}\) for \(\Delta_k=y_{k+1}-y_k\) and \(\sum|\Delta_k|<\infty\). The step interpolants are uniformly bounded on this alternating mesh, so their series converges uniformly. Subadditivity of variation and lower semicontinuity under uniform convergence give the bound obtained by summing the step variations. Since one step realizes each local factor, the precise norm for every weight sequence is

\[
K(\lambda)=1+\frac8{27}\sup_{k\in\mathbb Z}
\frac{h_{k-1}(1-\lambda_k)+h_{k+1}\lambda_{k+1}}{h_k}.
\]

**Global optimization, without a periodicity assumption on the weights.** Write \(u_j=\lambda_{2j}\), \(v_j=\lambda_{2j+1}\), and denote the supremum in the last display by \(M\). The even and odd cell bounds read

\[
\frac ba(1-u_j+v_j)\le M,\qquad
\frac ab(1-v_j+u_{j+1})\le M.
\]

Adding these two inequalities for \(j=-N,\dots,N\) telescopes the weight terms and yields

\[
2(2N+1)+u_{N+1}-u_{-N}\le (2N+1)M\left(\frac ab+\frac ba\right).
\]

The weights lie in \([0,1]\), so division by \(2N+1\) and passage to the limit prove

\[
M\ge\frac{2}{a/b+b/a}=\frac{2ab}{a^2+b^2}.
\]

Set \(u_j=b^2/(a^2+b^2)\) and \(v_j=a^2/(a^2+b^2)\) for every integer \(j\). Both nonnegative bounds become equalities with \(M=2ab/(a^2+b^2)\), giving the asserted minimum, attained by a two-periodic design. Moreover \(2ab/(a^2+b^2)\le1\), with equality exactly when \(a=b\); it tends to zero as \(a/b\) tends to either extreme. No special finite-support restriction on inputs or periodicity restriction on admissible weights was used.

## Verification

The companion `checker.py` verifies the exact Hermite extrema \(\pm4/27\), all four monotonicity corner derivatives, the two balancing identities of the optimal weights, and the exact final symbolic coefficient. It also checks 300 randomly chosen finite data/mesh/weight instances by a fine-grid lower approximation to the continuous variation, and a separate periodic finite-dimensional linear program checks ratios \((a,b)=(1,1),(1,3),(2,5),(1,100)\). The finite tests illustrate consistency only; the infinite-sequence and exact-optimum statements are proved analytically above. Run `python checker.py` with Python 3 and SymPy installed.

## Relationship to prior work

The classical literature on local cubic interpolation, including Beatson–Chacko's comparison of spline operator and derivative norms, studies pointwise or uniform estimates, not the exact design minimization for the first-order total-variation seminorm here. Its method G (a three-point quadratic-derivative Hermite rule) lies inside the broader convex-secant family, but its tabulated uniform and derivative supremum norms do not imply the present BV infimum. Sablonnière's 2005 work describes local spline quasi-interpolants and their supremum-norm estimates; its operators differ from this knot-interpolatory Hermite class. The known fixed uniform four-tap cubic-convolution variation constant \(35/27\) is the \(a=b\) special case, but does not imply the sharp coefficient-design law for all alternating meshes or the lower bound against nonperiodic choices. Related results for nonlinear Steffen-type slope limiters likewise do not cover this linear coefficient class. The use of alternating meshes in projection theory concerns different projectors and different operator norms.

This definition is not the general nonuniform Catmull–Rom parameterization, whose derivative formulas differ. The optimized rule is selected specifically to control first-order variation; it need not reproduce quadratic or cubic polynomials and it need not preserve monotonicity of every input.

## Limitations

The theorem concerns real bi-infinite *two-periodic positive knots*, linear fixed convex-adjacent-secant slopes, unweighted discrete variation, and full continuous total variation. It does not address arbitrary nonperiodic knot layouts, data-dependent nonlinear limiters, finite-interval endpoint conventions, higher-order polynomial reproduction, or alternative norms. Claims of priority beyond the inspected accessible literature remain provisional, notably for older interpolation sources whose complete histories cannot be established. The chosen source date below refers to a day-verified archival approximation text, not to the invention date of cubic Hermite interpolation.

## References

- P. Sablonnière, *Univariate spline quasi-interpolants and applications to numerical analysis*, arXiv:math/0504022v1, first submitted 1 April 2005, https://arxiv.org/abs/math/0504022. Primary listed MSC 41A15.
- R. K. Beatson and E. Chacko, *Which cubic spline should one use?*, University of Canterbury report, dated 30 November 1990; published in SIAM J. Sci. Stat. Comput. 13 (1992), 1009–1024, DOI:10.1137/0913059. Freely accessible report text at https://files01.core.ac.uk/download/pdf/35472972.pdf.
- R. H. Nochetto and A. J. Salgado, *A total variation diminishing interpolation operator and applications*, arXiv:1211.1069v1, submitted 5 November 2012, https://arxiv.org/abs/1211.1069 (a different, positive finite-element operator).
