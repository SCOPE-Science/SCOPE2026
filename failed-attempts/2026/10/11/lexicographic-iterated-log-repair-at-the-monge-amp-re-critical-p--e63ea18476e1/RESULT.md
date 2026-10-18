# Lexicographic iterated-log repair at the Monge–Ampère critical power

## Finding

Let \(n\ge3\), let \(f\) be a nonzero holomorphic germ at \(0\in\mathbb C^n\) with \(f(0)=0\), and shrink a neighborhood \(U\) so that \(-\log|f|\) is sufficiently large. For \(m\ge1\), define
\[
L_1(t)=\log t,
\qquad
L_{j+1}(t)=\log L_j(t),
\]
and for \(\beta=(\beta_1,\ldots,\beta_m)\in\mathbb R^m\),
\[
g_\beta(t)=t^{1/n}\prod_{j=1}^mL_j(t)^{-\beta_j},
\qquad
\chi_\beta(s)=-g_\beta(-s),
\]
\[
v_\beta(z)=\chi_\beta(\log|f(z)|).
\]
After moving the left endpoint far enough, \(\chi_\beta\) is smooth, nondecreasing and convex, so \(v_\beta\) is plurisubharmonic.

Every member of this family obeys
\[
\Delta v_\beta\in L^1_{\mathrm{loc}}(U),
\qquad
v_\beta\in W^{1,2}_{\mathrm{loc}}(U),
\qquad
v_\beta\notin W^{2,1}_{\mathrm{loc}}(U).
\]
Nevertheless, membership in the local Monge–Ampère domain has an arbitrarily deep iterated-log phase transition:
\[
v_\beta\in\mathcal D(U)
\quad\Longleftrightarrow\quad
\beta\succ_{\mathrm{lex}}(1/n,\ldots,1/n).
\]
Here lexicographic strict inequality means that, at the first coordinate where \(\beta\) differs from \((1/n,\ldots,1/n)\), that coordinate is larger. If every coordinate equals \(1/n\), membership fails.

In particular, at the first logarithmic level,
\[
-(-\log|f|)^{1/n}
\bigl(\log(-\log|f|)\bigr)^{-\beta_1}
\in\mathcal D(U)
\quad\Longleftrightarrow\quad
\beta_1>1/n.
\]
At the endpoint \(\beta_1=1/n\), a second iterated logarithm repairs membership exactly when \(\beta_2>1/n\), and this continues through every finite depth.

When membership holds, the source theorem also yields
\[
(dd^cv_\beta)^n=0,
\qquad
\nu(v_\beta,x)=0
\quad(x\in U).
\]

## Assumptions and scope

The construction uses the logarithmic holomorphic-singularity framework
\[
v=\chi(\log|f|)
\]
for a nonzero holomorphic germ vanishing at the origin. The neighborhood is chosen small enough that all iterated logarithms are defined and that the eventual convexity and monotonicity of \(\chi_\beta\) hold.

The result is local. It concerns the classical local domain \(\mathcal D(U)\) of definition of the complex Monge–Ampère operator. No claim is made about global compact-Kähler energy classes.

## Proof

Put
\[
a=1/n,
\qquad
g(t)=t^a\prod_{j=1}^mL_j(t)^{-\beta_j}.
\]
Its logarithmic derivative satisfies
\[
q(t):=\frac{tg'(t)}{g(t)}
=
\frac1n-
\sum_{j=1}^m
\frac{\beta_j}{L_1(t)\cdots L_j(t)}.
\]
Hence
\[
q(t)\longrightarrow\frac1n.
\]
For sufficiently large \(t\), \(q(t)>0\), so \(g'(t)>0\). Moreover
\[
g''(t)
=
\frac{g(t)}{t^2}
\bigl(q(t)^2-q(t)+tq'(t)\bigr).
\]
Because \(tq'(t)\to0\), the factor in parentheses tends to
\[
\frac1{n^2}-\frac1n<0.
\]
Thus \(g''(t)<0\) eventually. Since \(\chi(s)=-g(-s)\), this proves that \(\chi'\ge0\) and \(\chi''\ge0\) on a sufficiently far left half-line.

The source Monge–Ampère criterion is
\[
v\in\mathcal D(U)
\quad\Longleftrightarrow\quad
\int_{-\infty}^{A}
(-\chi(s))^{n-2}\chi'(s)^2\,ds<\infty.
\]
Changing variables \(t=-s\) gives
\[
\int^{\infty}g(t)^{n-2}g'(t)^2\,dt
=
\int^{\infty}
q(t)^2
\frac{dt}{t\prod_{j=1}^mL_j(t)^{n\beta_j}}.
\]
Since \(q(t)\to1/n\), convergence is exactly that of the generalized logarithmic integral
\[
\int^{\infty}
\frac{dt}{t\prod_{j=1}^mL_j(t)^{n\beta_j}}.
\]
Repeated substitutions
\[
u_1=\log t,
\quad
u_2=\log u_1,
\quad\ldots
\]
show the standard lexicographic rule: the first exponent \(n\beta_k\) that differs from \(1\) decides convergence, with convergence precisely when it is greater than \(1\); if all exponents equal \(1\), the final integral is logarithmically divergent. This proves the stated \(\mathcal D(U)\) criterion.

For the first-order Sobolev condition, the source theorem at \(p=2\) gives
\[
v\in W^{1,2}_{\mathrm{loc}}(U)
\quad\Longleftrightarrow\quad
\int_{-\infty}^{A}\chi'(s)^2\,ds<\infty.
\]
Here
\[
g'(t)^2
=
q(t)^2
t^{2/n-2}
\prod_{j=1}^mL_j(t)^{-2\beta_j}.
\]
For \(n\ge3\),
\[
2/n-2<-1,
\]
so every fixed finite product of iterated-log powers is dominated by the integrable power. Hence every \(v_\beta\) lies in \(W^{1,2}_{\mathrm{loc}}\).

The endpoint second-order criterion is
\[
v\in W^{2,1}_{\mathrm{loc}}(U)
\quad\Longleftrightarrow\quad
\chi'\in L^1(( -\infty,A)).
\]
But
\[
\int^{\infty}g'(t)\,dt
=
\lim_{T\to\infty}g(T)-g(T_0)
=\infty,
\]
because the positive power \(t^{1/n}\) dominates every finite product of iterated logarithms. Thus no member lies in \(W^{2,1}_{\mathrm{loc}}\).

Finally, \(g'(t)\to0\), so the residual divisor coefficient \(\ell_\chi\) vanishes. Since \(g''(t)<0\) eventually,
\[
\int^{\infty}|g''(t)|\,dt<\infty.
\]
The source Laplacian criterion therefore gives
\[
\Delta v_\beta\in L^1_{\mathrm{loc}}(U)
\]
for every \(\beta\).

When the Monge–Ampère integral converges, the same source theorem gives the vanishing Monge–Ampère measure and zero Lelong numbers.

## Verification

The fresh primary paper was checked at its four relevant inputs: the \(L^1\) Laplacian criterion, the \(W^{1,2}\) criterion, the endpoint \(W^{2,1}\) criterion, and the local Monge–Ampère-domain criterion. Its application section separately treats pure powers and pure iterated logarithms, but not the critical-power times iterated-log family above.

The asymptotic derivative calculation is exact up to factors tending to nonzero constants. The decisive Monge–Ampère integral is reduced to a classical iterated-log integral, whose convergence follows by successive substitutions. No finite experiment or numerical evidence is used.

At \(n=2\), the power in the Sobolev integral becomes \(t^{-1}\), and the source explicitly notes that its Monge–Ampère criterion coincides with \(W^{1,2}_{\mathrm{loc}}\). For \(n\ge3\), the strict inequality \(2/n-2<-1\) is exactly what separates the Sobolev and Monge–Ampère thresholds.

## Relationship to prior work

Chen, Shao and Wang give the sharp integral criteria for \(v=\chi(\log|f|)\), list the pure power family \(-(-s)^\alpha\), and separately list iterated-logarithmic examples. They also state that in complex dimension two the Monge–Ampère criterion coincides with the \(W^{1,2}_{\mathrm{loc}}\) criterion. The present result identifies the unresolved endpoint geometry obtained by multiplying the critical power \(t^{1/n}\) by arbitrary finite iterated-log corrections.

Błocki's characterization supplies the broader local Monge–Ampère framework and the special dimension-two Sobolev coincidence. His later survey recalls classical critical-power obstructions such as Kiselman's example, showing that the exponent \(1/n\) is structurally natural in higher-dimensional pluripotential theory. Those results do not state the lexicographic repair law for logarithmic holomorphic compositions.

Targeted searches for the critical-power product, iterated-log repairs, and higher-dimensional \(W^{1,2}\)-versus-Monge–Ampère separation did not locate a published statement with the same conclusion.

## Limitations

The theorem treats finite iterated-log products. It does not classify arbitrary slowly varying corrections to the critical power, although the proof suggests a regular-variation formulation.

The construction is local near a holomorphic zero divisor. It does not assert that every higher-dimensional \(W^{1,2}\) plurisubharmonic function outside \(\mathcal D\) has this form.

No quantitative stability statement is claimed near the lexicographic threshold.

## References

1. H. Chen, G. Shao and W. Wang, *Characterization of Sobolev regularity of plurisubharmonic functions*, arXiv:2609.39136v1, 2026.
2. Z. Błocki, *The domain of definition of the complex Monge–Ampère operator*, American Journal of Mathematics 128 (2006), 519–530. DOI: 10.1353/AJM.2006.0010.
3. Z. Błocki, *Cauchy–Riemann meet Monge–Ampère*, Bulletin of Mathematical Sciences 4 (2014), 433–480. DOI: 10.1007/s13373-014-0058-2.
4. Y. Pan, G. Shao, J. Wang and J. Wu, *Energy estimates for level sets of holomorphic functions and universal counterexamples to Calderón–Zygmund theory*, arXiv:2604.01559v2, 2026.
