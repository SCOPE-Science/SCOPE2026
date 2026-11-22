# Sharp finite-tolerance Lipschitz numerical index for real Hilbert isometries

## Finding

Let \(0<\delta<1\), and set \(s_\delta=\sqrt{2\delta-\delta^2}\). For every pointed metric space \(M\) having at least two points and every isometric embedding \(g:M\longrightarrow H\) into a **real** Hilbert space \(H\) of dimension at least two, the finite-tolerance Lipschitz numerical index defined below is exactly

\[
 n_{g,\delta}(M,H)=s_\delta.
\]

Moreover, the optimal uniform error for replacing the ordinary \(g\)-Lipschitz numerical radius by its finite-tolerance version is exactly

\[
 \sup_{\|f\|_{\mathrm{Lip}}=1}\bigl(\nu_g^\delta(f)-\nu_g(f)\bigr)=s_\delta.
\]

Both equalities are attained by a single explicit rank-two skew rotation composed with \(g\). If \(H\) has dimension one, the two constants instead are \(1\) and \(0\), respectively. For **any** norm-one Lipschitz reference \(g:M\to H\) (not necessarily isometric) into real \(H\) of dimension at least two, the universal upper bound \(n_{g,\delta}(M,H)\le s_\delta\) still holds. In particular, the exact regularization rate is \(s_\delta\sim\sqrt{2\delta}\) as \(\delta\downarrow0\).

## Assumptions and scope

All scalar products and Lipschitz maps are over the real field. Let \((M,d,p_0)\) be a pointed metric space with at least two elements. For a map \(h:M\to H\) with \(h(p_0)=0\), put

\[
 \|h\|_{\mathrm{Lip}}=\sup_{p\ne q}\frac{\|h(p)-h(q)\|}{d(p,q)}.
\]

Translations of the target may be subtracted so that \(g(p_0)=0\). Fix \(g\) of Lipschitz norm one. For \(f(p_0)=0\) and finite Lipschitz norm, define

\[
 \nu_g^\delta(f)=\sup_{\substack{p\ne q,\ u\in S_H\\
 \langle u,(g(p)-g(q))/d(p,q)\rangle>1-\delta}}
 \left|\left\langle u,\frac{f(p)-f(q)}{d(p,q)}\right\rangle\right|,
 \qquad
 n_{g,\delta}(M,H)=\inf_{\|f\|_{\mathrm{Lip}}=1}\nu_g^\delta(f).
\]

Here \(S_H\) denotes the unit sphere, and \(\nu_g(f)=\inf_{0<\varepsilon<1}\nu_g^\varepsilon(f)\) is the usual limiting radius. The admissible set is nonempty because \(\|g\|_{\mathrm{Lip}}=1\). For the exact index and sharp error identities we assume \(g\) is an isometric embedding, meaning \(\|g(p)-g(q)\|=d(p,q)\) for all distinct \(p,q\). Neither finite cardinality nor a finite-dimensional target is required.

## Proof

**Step 1: spherical-cap lemma.** Let \(a\in S_H\), \(b\in H\), \(c=1-\delta\), and \(s=\sqrt{1-c^2}\). If \(\dim H\ge2\), then

\[
 \sup_{u\in S_H:\ \langle u,a\rangle>c}|\langle u,b\rangle|\ \ge\ s\|b\|.
\]

For \(b=0\) this is immediate. Otherwise set \(r=\|b\|\), \(x=|\langle a,b\rangle|/r\), and let \(b_\perp=b-\langle a,b\rangle a\). When \(x\ge c\), a choice of \(u\) parallel to \(b\), with its sign chosen for positive pairing with \(a\), yields the supremum \(r\). At the equality boundary \(x=c\), use an approaching sequence inside the open cap. When \(x<c\), the boundary point obtained by adding \(s b_\perp/\|b_\perp\|\) to \(c a\), with the appropriate sign, yields in the supremum the lower bound

\[
 r\bigl(cx+s\sqrt{1-x^2}\bigr).
\]

The function \(x\mapsto cx+s\sqrt{1-x^2}\) is concave on \([0,c]\), with endpoint values \(s\) and \(1\). Its minimum is \(s\). Again the boundary value is obtained by an inner-cap sequence. This proves the lemma; for nonzero \(b\) the lower bound is achieved as a cap supremum when \(b\perp a\).

**Step 2: index lower bound.** If \(g\) is isometric, each normalized reference increment \(a=(g(p)-g(q))/d(p,q)\) has norm one. Put \(b=(f(p)-f(q))/d(p,q)\). Applying Step 1 to every pair and then taking the supremum proves

\[
 \nu_g^\delta(f)\ge s_\delta\|f\|_{\mathrm{Lip}}.
\]

Thus \(n_{g,\delta}(M,H)\ge s_\delta\).

**Step 3: skew witness, both sharpness claims, and general reference maps.** Choose a two-dimensional subspace of \(H\) with orthonormal basis \(e_1,e_2\), and define the bounded real-linear rank-two map \(J\) by \(Je_1=e_2\), \(Je_2=-e_1\), and \(J=0\) on their orthogonal complement. Then \(\|J\|=1\) and \(\langle z,Jz\rangle=0\) for all \(z\in H\). Select \(e_1\) parallel to one nonzero increment of \(g\), so that \(Jg\) has positive Lipschitz norm. In the isometric case it has norm exactly one.

For **any** norm-one Lipschitz \(g\), let \(a=(g(p)-g(q))/d(p,q)\), so \(\|a\|\le1\), and let \(u\in S_H\) satisfy \(\langle u,a\rangle>c\). If the cap is nonempty then \(a\ne0\), and since \(Ja\perp a\),

\[
 |\langle u,Ja\rangle|
 \le \sqrt{1-\frac{\langle u,a\rangle^2}{\|a\|^2}}\,\|Ja\|
 \le s\|Ja\|.
\]

After taking the supremum over admissible pairs this gives \(\nu_g^\delta(Jg)\le s\|Jg\|_{\mathrm{Lip}}\). Normalize \(Jg\) to Lipschitz norm one: the universal upper bound on the index follows. If \(g\) is isometric, Step 2 gives the opposite bound, hence \(\nu_g^\delta(Jg)=s\) for the norm-one skew witness. Since \(\langle a,Ja\rangle=0\) on every pair, \(\nu_g(Jg)=0\).

**Step 4: sharp finite-tolerance error.** For any isometric \(g\), any pair, and admissible \(u\), decompose \(u=t a+v\) with \(v\perp a\). Since \(t>c>0\), \(\|v\|\le s\). Hence

\[
 |\langle u,b\rangle|
 \le |\langle a,b\rangle|+s\|b\|.
\]

The limiting-radius identity
\(\nu_g(f)=\sup_{p\ne q}|\langle a,b\rangle|\)
 follows from \(u=a\) being admissible and \(\|u-a\|\le\sqrt{2\varepsilon}\) when \(\langle u,a\rangle>1-\varepsilon\), uniformly over pairs. Taking suprema therefore shows

\[
 0\le\nu_g^\delta(f)-\nu_g(f)\le s\|f\|_{\mathrm{Lip}}.
\]

The skew witness from Step 3 has limiting radius zero and finite radius \(s\), so the error coefficient is optimal.

**Step 5: scalar target.** If \(H=\mathbb R\) and \(g\) is isometric, for each pair the unit functional with sign matching \(g(p)-g(q)\) is admissible and evaluates \(f\)'s normalized increment in absolute value exactly. Thus \(\nu_g^\delta(f)=\nu_g(f)=\|f\|_{\mathrm{Lip}}\), proving the one-dimensional assertions.

## Verification

All steps above apply to arbitrary pointed metric spaces and arbitrary real Hilbert spaces of the stated dimension, without a compactness or differentiability assumption. The companion `checker.py` uses a deterministic grid of tolerances and cap directions, independently checks the two branches of the spherical-cap maximum, and tests skew orthogonality and length preservation on a finite noncollinear point set. It prints `HILBERT_CAP_FINITE_DIAGNOSTIC_OK 20136`. These finite checks supplement rather than replace the analytic arguments in Steps 1–5.

## Relationship to prior work

The numerical index and its Lipschitz analogue are classical; the finite-tolerance near-norming sets also appear in the published operator-relative formalism. Pérez-Hernández (2025, Lemma 3.2) uses \(\delta\)-near-norming functionals to recover the limiting Lipschitz radius, with a nonsharp general approximation estimate. Kadets–Martín–Merí–Pérez–Quero (2019/2020, Theorem 4.5) prove the qualitative vanishing of relative indices involving real Hilbert targets. Choi–Han–Jung (2026, Corollary 6.3) similarly establish zero *limiting* index for Hilbert-valued Lipschitz maps. Those results do not themselves specify the sharp finite-\(\delta\) profile, its exact error coefficient, or its metric-isometry scope. The latter 2026 preprint appeared after the first public source underlying this direction and is included only as related literature.

## Limitations

This is a real-Hilbert theorem, not a complex-Hilbert or non-Hilbert Banach-space result. The exact positive index is proved for isometric references; only the stated upper bound is proved for arbitrary norm-one Lipschitz references. The parameter range is strictly \(0<\delta<1\). No mathematical priority claim is made against unindexed papers or uses of another convention for approximate numerical radius. The result is a precise mathematical theorem and does not assert an independent external audit.

## References

1. A. Pérez-Hernández, *Lipschitz vs Linear Numerical Index in certain Banach spaces*, arXiv:2507.18208, first public version 24 July 2025, especially Lemma 3.2. https://arxiv.org/abs/2507.18208
2. V. Kadets, M. Martín, J. Merí, A. Pérez, A. Quero, *On the numerical index with respect to an operator*, arXiv:1905.12257, first public version 29 May 2019, especially Theorem 4.5. https://arxiv.org/abs/1905.12257
3. G. Choi, M. Han, M. Jung, *The numerical index with respect to a Lipschitz map*, arXiv:2611.20406, first public version 16 November 2026, especially Section 6.1 and Corollary 6.3. https://arxiv.org/abs/2611.20406
