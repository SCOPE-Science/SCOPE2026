# Power-snowflake exact \(\varepsilon\)-isometries for every separable non-Schur Banach space
## Finding
Let \(X\) be a separable real Banach space that does not have the Schur property, and fix \(0<\alpha<1\). Define
\[
\omega_\alpha(t)=\max\{t,t^\alpha\},\qquad
Y_\alpha(X)=\mathcal F_{\omega_\alpha}(X).
\]
Here the free space is formed over \(X\) with metric \(d_\alpha(x,y)=\omega_\alpha(\|x-y\|)\). Set
\[
K_\alpha=(1-\alpha)\alpha^{\alpha/(1-\alpha)}.
\]
For every \(\varepsilon>0\), put \(a=\varepsilon/K_\alpha\) and
\[
f_{\varepsilon,\alpha}(x)=a\,\delta(x/a),
\]
where \(\delta:X\to Y_\alpha(X)\) is the canonical free-space embedding. Then, for every \(x,y\in X\),
\[
0\le
\|f_{\varepsilon,\alpha}(x)-f_{\varepsilon,\alpha}(y)\|-\|x-y\|
\le\varepsilon.
\]
Moreover the upper bound is sharp: equality occurs exactly when
\[
\|x-y\|=\frac{\alpha}{1-\alpha}\,\varepsilon.
\]
Thus \(f_{\varepsilon,\alpha}\) is a standard exact \(\varepsilon\)-isometry. The target \(Y_\alpha(X)\) is separable and Schur, is independent of \(\varepsilon\), and admits no isometric copy of \(X\), even via a nonlinear isometric embedding.

## Assumptions and scope
The result is for separable real Banach spaces \(X\) failing the Schur property and power parameters \(0<\alpha<1\). No assertion is made for Schur source spaces, for \(\alpha\) at either endpoint, or for arbitrary gauges outside this power family.

The gauge \(\omega_\alpha\) is increasing, continuous and subadditive. Indeed both \(t\) and \(t^\alpha\) are increasing and subadditive on \([0,\infty)\), and the pointwise maximum of two nonnegative increasing subadditive functions is subadditive. Also
\[
\frac{\omega_\alpha(t)}t=t^{\alpha-1}\longrightarrow\infty
\qquad (t\downarrow0),
\]
so this is a nontrivial strongly normalized gauge in the sense used for the free-space Schur theorem.

## Proof
For \(r=\|x-y\|\), the defining isometry of the free-space Dirac map gives
\[
\begin{aligned}
\|f_{\varepsilon,\alpha}(x)-f_{\varepsilon,\alpha}(y)\|
&=a\,\omega_\alpha(r/a)\\
&=\max\{r,a^{1-\alpha}r^\alpha\}.
\end{aligned}
\]
Hence the additive error is
\[
E_a(r)=\max\{0,a^{1-\alpha}r^\alpha-r\}.
\]
It vanishes for \(r\ge a\). On \((0,a)\), differentiating the positive branch gives
\[
E_a'(r)=\alpha a^{1-\alpha}r^{\alpha-1}-1.
\]
There is one critical point,
\[
r_*=\alpha^{1/(1-\alpha)}a,
\]
and the derivative changes from positive to negative there. Thus this is the unique positive maximizer. Using the critical-point identity \(a^{1-\alpha}r_*^\alpha=r_*/\alpha\),
\[
\max_{r\ge0}E_a(r)
=E_a(r_*)
=(1-\alpha)\alpha^{\alpha/(1-\alpha)}a
=K_\alpha a.
\]
Choosing \(a=\varepsilon/K_\alpha\) makes the maximum exactly \(\varepsilon\). A cancellation of the powers of \(\alpha\) gives
\[
r_*=\frac{\alpha}{1-\alpha}\varepsilon.
\]
This proves both the standard \(\varepsilon\)-isometry inequality and its exactness.

The same distance formula also yields
\[
\|f_{\varepsilon,\alpha}(x)-f_{\varepsilon,\alpha}(y)\|\ge\|x-y\|,
\]
so the map is injective and its inverse on its range is \(1\)-Lipschitz. Since \(r\mapsto\max\{r,a^{1-\alpha}r^\alpha\}\) tends to zero with \(r\), the forward map is uniformly continuous.

Kalton's free-space theorem says that \(\mathcal F_\omega(M)\) has the Schur property for every metric space \(M\) and every nontrivial gauge of the relevant type; it applies to \(\omega_\alpha\). Separability of \(X\) gives separability of the corresponding free space. Finally, suppose an isometric embedding \(X\to Y_\alpha(X)\) existed. By the Godefroy-Kalton theorem, because \(X\) is separable, the target would contain a linearly isometric copy of \(X\). Every subspace of a Schur space is Schur, contradicting the hypothesis on \(X\). Therefore no isometric embedding exists.

## Verification
The quantitative part reduces to the single-variable error function \(E_a\) above. Its support, critical point, maximum and equality radius were derived directly and independently checked numerically over representative values of \(\alpha\) and \(\varepsilon\). The endpoint behavior is consistent: the proof only uses \(0<\alpha<1\), where the critical point lies strictly between \(0\) and \(a\).

At \(\alpha=1/2\), one obtains \(K_{1/2}=1/4\), hence \(a=4\varepsilon\), and the equality radius is \(\varepsilon\). This exactly reproduces the normalization and sharp error point in the Sun-Zhang example.

## Relationship to prior work
Sun and Zhang construct, for every \(\varepsilon>0\), a standard exact \(\varepsilon\)-isometry from \(\ell_2\) into the fixed Schur space \(\mathcal F_\omega(\ell_2)\) for \(\omega(t)=\max\{t,\sqrt t\}\), while proving that no isometric embedding exists. Their proof exhibits the free-space mechanism and the scale \(4\varepsilon\), but its theorem is stated for the single source \(\ell_2\) and the square-root gauge.

The present statement isolates the mechanism that is actually needed: separability plus failure of the Schur property on the source, together with any power snowflake exponent \(0<\alpha<1\). It also computes the sharp normalization and the exact distance at which the additive error is attained throughout the full power family.

Kalton's earlier free-space work supplies the Schur theorem for nontrivial gauges, and Godefroy-Kalton supplies the isometric linearization theorem for separable Banach sources. Those results are ingredients rather than covering statements: neither states the exact additive \(\varepsilon\)-isometry construction above, its sharp constant, or the full non-Schur-source conclusion.

## Limitations
The theorem gives a broad obstruction to passing from arbitrarily small additive distortion to exact isometric embeddability, but it does not characterize which Schur spaces admit analogous constructions. It does not address multiplicative distortion, almost-isometric linear embeddings, or nonseparable sources. The originality search found no covering statement, but the proof is short once the three cited ingredients are juxtaposed, so an unindexed equivalent observation remains a residual literature risk.

## References
1. Longfa Sun and Yipeng Zhang, *\(\varepsilon\)-isometries without isometric embeddings*, arXiv:2609.13937v1, first public 2026-09-12.
2. Nigel J. Kalton, *Spaces of Lipschitz and Hölder functions and their applications*, Collectanea Mathematica 55 (2004), especially Theorem 4.6 and Proposition 5.2.
3. Gilles Godefroy and Nigel J. Kalton, *Lipschitz-free Banach spaces*, Studia Mathematica 159 (2003), DOI 10.4064/sm159-1-6.
