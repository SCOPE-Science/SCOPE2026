# Trace-slice discontinuity in the sharp spectral Lipschitz modulus of two-level matrix absolute value

## Finding

Let \(\mathcal H_2(t)=\{A\in\mathbb C^{2\times2}:A=A^*,\ \operatorname{tr}A=t\}\), with real \(t\), and let \(|A|=(A^2)^{1/2}\). For the matrix spectral norm \(\|\cdot\|_{\mathrm{op}}\), define
\[
L(t)=\sup_{\substack{A,B\in\mathcal H_2(t)\\A\ne B}}
\frac{\||A|-|B|\|_{\mathrm{op}}}{\|A-B\|_{\mathrm{op}}}.
\]
Then the complete sharp trace-slice law is
\[
\boxed{L(0)=1,\qquad L(t)=\sqrt2\quad(t\ne0).}
\]
At trace zero the bound is attained by distinct pairs; at every nonzero trace the sharp supremum is **not attained** by any distinct finite pair. More precisely, at a matrix with opposite-sign, nonzero eigenvalues \(t/2+r\) and \(t/2-r\), where \(r>|t|/2\), the exact local derivative norm of \(A\mapsto |A|\) restricted to the fixed-trace affine space is
\[
\boxed{\sqrt{1+\frac{t^2}{4r^2}}.}
\]
At every strictly definite matrix on the slice the local derivative norm is \(1\). This local profile tends to \(\sqrt2\) when an indefinite matrix approaches the rank-one boundary from the indefinite side. All statements hold for complex Hermitian matrices and therefore for real symmetric matrices.

## Assumptions and scope

The domain consists of all Hermitian two-by-two matrices with the **same specified real trace**, with no positivity assumption and no spectral gap imposed. Both input and output distances use the matrix spectral norm. The absolute value is the positive square root of the square, not entrywise absolute value. The coefficient is a two-input Lipschitz supremum, distinct from a one-input norm bound. A local derivative assertion only applies at matrices with no zero eigenvalues and, for its stated indefinite formula, one positive and one negative eigenvalue.

## Proof

**1. Two-level coordinates and norm.** Let \(\sigma_1,\sigma_2,\sigma_3\) be the standard Hermitian Pauli matrices. Every member of the trace slice has a unique representation
\[
A=aI+v\cdot\sigma,\qquad a=t/2,\quad v\in\mathbb R^3.
\]
Set \(r=|v|_2\). The eigenvalues are \(a+r\) and \(a-r\). For any real \(s\) and \(q\in\mathbb R^3\),
\[
\|sI+q\cdot\sigma\|_{\mathrm{op}}=|s|+|q|_2,
\qquad \|A(v)-A(w)\|_{\mathrm{op}}=|v-w|_2.
\]
These identities follow directly from the two eigenvalues \(s\pm|q|_2\).

**2. Exact absolute-value formula.** Functional calculus at the two eigenvalues gives
\[
|aI+v\cdot\sigma|=
\begin{cases}
|a|I+\operatorname{sgn}(a)v\cdot\sigma,& r\le|a|,\ a\ne0,\\
rI+(a/r)v\cdot\sigma,&r>|a|.
\end{cases}
\]
At \(a=v=0\), the value is zero; at \(a=0,r>0\), the second branch is \(rI\). Both formulas agree at the boundary \(r=|a|>0\), hence the map is continuous across the boundary.

**3. Exact local profile.** In the strictly definite region \(r<|a|\), the map in the \(v\)-coordinate is affine with output perturbation \(\pm h\cdot\sigma\). Its operator norm is exactly one. For \(r>|a|\), put \(u=v/r\) and decompose \(h=h_\parallel u+h_\perp\), with \(u\cdot h_\perp=0\). Differentiating gives
\[
\mathrm d|A|[h]=h_\parallel I+\frac a r h_\perp\cdot\sigma,
\qquad
\|\mathrm d|A|[h]\|_{\mathrm{op}}=|h_\parallel|+\frac{|a|}{r}|h_\perp|_2.
\]
Since the input norm is \(\sqrt{h_\parallel^2+|h_\perp|_2^2}\), Cauchy--Schwarz yields exact operator norm \(\sqrt{1+(a/r)^2}\), attained infinitesimally when the component magnitudes are in the ratio \(1:|a|/r\). In particular this norm is strictly less than \(\sqrt2\) at every differentiability point when \(a\ne0\).

**4. Global upper bound and strict nonattainment.** The straight path from any \(v\) to any distinct \(w\) crosses the sphere \(|v|_2=|a|\) in at most two points (its squared radius is a strictly convex quadratic along a nonconstant segment). Split the segment at those points; on every open component, the formula in step 2 is differentiable. Step 3 and integration of the derivative imply
\[
\||A(v)|-|A(w)|\|_{\mathrm{op}}\le\sqrt2\,|v-w|_2.
\]
For \(a\ne0\), every derivative bound is strictly below \(\sqrt2\) except at the finitely many boundary points, so the integral is strictly below \(\sqrt2|v-w|_2\) whenever \(v\ne w\). Thus distinct pairs cannot attain \(\sqrt2\).

**5. Sharpness at nonzero trace.** Fix \(a\ne0\), let \(r>|a|\) decrease to \(|a|\), and take a radial direction \(u\) and a perpendicular unit direction \(e\). At \(v=ru\), choose \(h=u+\operatorname{sgn}(a)e\). The derivative ratio is
\[
\frac{1+|a|/r}{\sqrt2}\longrightarrow\sqrt2
\quad\text{as }r\downarrow|a|.
\]
Each derivative is the limit of ratios for actual distinct matrices \(A(v+\varepsilon h)\) and \(A(v)\) of the same trace as \(\varepsilon\downarrow0\); hence \(L(t)\ge\sqrt2\) for every nonzero \(t\). Step 4 supplies equality.

**6. Zero trace.** If \(a=0\), the formula becomes \(|A(v)|=|v|_2 I\) for all \(v\). The reverse triangle inequality gives
\[
\||A(v)|-|A(w)|\|_{\mathrm{op}}
=\big||v|_2-|w|_2\big|\le|v-w|_2.
\]
Equality holds for distinct points on the same ray, including one point at the origin. Thus \(L(0)=1\). This completes the proof.

## Verification

The included standard-library program `checker.py` evaluates the closed-form two-level spectral calculus in high-precision decimal arithmetic. It tests 16,000 fixed-trace input pairs, exact zero-trace equality, local derivative profiles, and a sequence of genuine nonzero-trace pairs approaching the sharp bound. It reports `ALL_TRACE_SLICE_MODULUS_CHECKS_PASS` when completed. These computations corroborate the formulas; the exact all-pair theorem, strict nonattainment, and limit are established analytically in the proof.

## Relationship to prior work

General matrix absolute-value perturbation bounds and the lack of unrestricted operator Lipschitzness of the scalar absolute-value functional calculus are classical; see Bhatia (2010) and Aleksandrov--Peller (2009). The result isolates the smallest noncommutative Hermitian dimension and **fixes the trace in both inputs**. Its claim is the precise discontinuous trace-slice constant, local spectral-gap sensitivity, and nonattainment statement, rather than a general-dimensional bound. Published two-by-two semidefinite projection estimates in entrywise norms concern a different map and metric; they do not imply this trace-slice spectral-norm classification.

## Limitations

The statement does not cover general nonsymmetric matrices, dimensions above two, Schatten norms other than spectral norm, or perturbations with different input traces. The coefficient is a global supremum even though no distinct pair attains it on a nonzero trace slice. No universal best constant for larger dimensions is claimed.

## References

- A. B. Aleksandrov and V. V. Peller, *Operator Hölder--Zygmund functions*, first posted 17 July 2009, https://arxiv.org/abs/0907.3049 . Relevant material: introductory discussion and the operator-modulus discussion of \(f(s)=|s|\) in Section 8.
- R. Bhatia, *Modulus of continuity of the matrix absolute value*, Indian Journal of Pure and Applied Mathematics 41 (2010), 99--111, https://doi.org/10.1007/s13226-010-0014-0 . Relevant material: Section 1 and Theorem 4.2.
