# Exact boundary transport defect for change-of-numeraire reweighting
## Finding
Let \(Q_n\) be probability laws of \((A_n,B_n)\in(0,\infty)\times\mathbb R\) and suppose \(Q_n\Rightarrow Q\) on \([0,\infty)\times\mathbb R\). Assume that \(\{A_n}\) and \(\{|B_n|}\) are uniformly integrable and that
\[
m:=\int a\,Q(da,db)>0.
\]
Write \(m_n=\mathbb E[A_n]\). Define the change-of-numeraire law \(\Gamma_n\) by
\[
\int f(z)\,\Gamma_n(dz)=\frac{\mathbb E[A_n f(B_n/A_n)]}{m_n},
\]
and define the weak limit by zero-weighting the boundary,
\[
\int f(z)\,\Gamma(dz)=\frac1m\int_{\{a>0\}}a f(b/a)\,Q(da,db).
\]
Set
\[
c_+=\int_{\{a=0\}}b^+\,dQ,\qquad
c_-=\int_{\{a=0\}}(-b)^+\,dQ,\qquad c=c_++c_-.
\]
Then
\[
W_1(\Gamma_n,\Gamma)\longrightarrow \frac{c}m.
\]
For the call and put transforms,
\[
C_n(K)=\int(z-K)^+\,d\Gamma_n,\qquad P_n(K)=\int(K-z)^+\,d\Gamma_n,
\]
one has, uniformly for \(K\) in every compact interval,
\[
C_n(K)-C(K)\longrightarrow\frac{c_+}m,
\qquad
P_n(K)-P(K)\longrightarrow\frac{c_-}m.
\]
Thus the positive and negative parts of payoff mass carried by the zero-numeraire fiber survive as two one-sided vertical offsets, and their sum is exactly the limiting first-Wasserstein transport defect.

## Assumptions and scope
The assumptions are exactly the first-order setting in which the primitive numeraire and absolute payoff are uniformly integrable, while the weak limit may charge \(\{a=0\}\). No reciprocal-numeraire moment is assumed. The result concerns the one-dimensional ratio marginal and \(W_1\). It does not assert a convergence rate, does not identify \(W_s\) defects for \(s>1\), and does not cover failure of uniform integrability of \(A_n\) or \(|B_n|\).

## Proof
First, a general one-dimensional transport lemma is useful. Suppose \(\mu_n\Rightarrow\mu\), all laws belong to \(\mathcal P_1(\mathbb R)\), and
\[
\int |x|\,d\mu_n\longrightarrow L<\infty.
\]
Let \(M=\int|x|\,d\mu\). Then
\[
W_1(\mu_n,\mu)\longrightarrow L-M.
\]
Indeed, the Kantorovich--Rubinstein dual test \(x\mapsto |x|\) gives
\[
\liminf_n W_1(\mu_n,\mu)\ge L-M.
\]
For the reverse bound, let \(T_R(x)=\max(-R,\min(x,R))\). The triangle inequality gives
\[
W_1(\mu_n,\mu)
\le
\int(|x|-R)^+\,d\mu_n
+W_1((T_R)_\#\mu_n,(T_R)_\#\mu)
+\int(|x|-R)^+\,d\mu.
\]
The middle term tends to zero because the clipped laws are supported on the compact interval \([-R,R]\) and converge weakly. Since \(x\mapsto\min(|x|,R)\) is bounded and continuous,
\[
\int(|x|-R)^+\,d\mu_n
\longrightarrow
L-\int\min(|x|,R)\,d\mu.
\]
Taking \(\limsup\) and then \(R\to\infty\) yields at most \(L-M\), proving the lemma.

Now apply the perspective cancellation identity to \(\Gamma_n\):
\[
\int |z|\,d\Gamma_n=\frac{\mathbb E|B_n|}{m_n}.
\]
Uniform integrability and weak convergence imply
\[
m_n\to m,
\qquad
\mathbb E|B_n|\to\int |b|\,dQ.
\]
The weak-limit law satisfies
\[
\int|z|\,d\Gamma=\frac1m\int_{\{a>0\}}|b|\,dQ.
\]
Therefore the preceding lemma gives
\[
\lim_n W_1(\Gamma_n,\Gamma)
=
\frac1m\int_{\{a=0\}}|b|\,dQ
=
\frac{c_++c_-}m.
\]

For calls, perspective cancellation gives
\[
C_n(K)=\frac{\mathbb E[(B_n-KA_n)^+]}{m_n}.
\]
For any fixed bounded strike interval \(|K|\le R\), the integrands satisfy
\[
0\le(B_n-KA_n)^+\le |B_n|+R A_n.
\]
The right-hand family is uniformly integrable, so weak convergence plus uniform integrability gives, pointwise in \(K\),
\[
\mathbb E[(B_n-KA_n)^+]\to\int(b-Ka)^+\,dQ.
\]
On \(\{a=0\}\) this limiting integrand equals \(b^+\), whereas the zero-weighted limit law contains only the contribution from \(\{a>0\}\). Hence
\[
C_n(K)-C(K)\to \frac{c_+}m.
\]
Every call transform is \(1\)-Lipschitz in \(K\), so the differences are equicontinuous; pointwise convergence to a constant therefore upgrades to uniform convergence on each compact strike interval. Replacing \((B_n-KA_n)^+\) by \((KA_n-B_n)^+\) gives the put statement and the boundary contribution \((-b)^+\).

## Verification
The proof uses only weak convergence, uniform integrability, the perspective identities, clipping, and the Kantorovich--Rubinstein lower bound. The accompanying deterministic checker evaluates a three-atom family whose weak limit has both positive and negative payoff mass at \(a=0\). It verifies the exact weighted law, the predicted limiting \(W_1\) defect, and uniform-on-grid convergence of call and put offsets over a bounded strike range. The checker is a finite sanity test; the theorem itself is established analytically above.

## Relationship to prior work
Huang's first public version, arXiv:2609.30329v1, defines this reweighting, proves weak stability under the stated primitive assumptions, and shows that under uniform integrability of \(|B_n|\), \(W_1(\Gamma_n,\Gamma)\to0\) if and only if \(\int_{\{a=0\}}|b|\,dQ=0\). The same paper records the limiting first-moment residue and the call perspective identity, but its stated boundary theorem is binary: it identifies when the distance vanishes, not the exact nonzero limit of the distance, nor the positive/negative decomposition into strike-independent call and put offsets.

The earlier change-of-numeraire literature, including Beiglböck--Pammer--Riess on weak martingale transport, concerns structural transport correspondences and transformed-moment assumptions. Those results do not state the boundary-residue formula above. The generic weak-plus-first-moment characterization of \(W_1\) is standard; no novelty is claimed for that characterization or for the clipping lemma in isolation. The contribution is the exact quantitative identification of Huang's vanishing-numeraire obstruction after the ratio-and-reweight map, together with its one-sided price-transform decomposition.

## Limitations
The conclusion is asymptotic and first-order. It supplies no finite-\(n\) error bound. For \(s>1\), the relevant primitive quantity is \(|B|^s A^{1-s}\), so there is no asserted analogue obtained merely by replacing \(|b|\) with \(|b|^s\) on \(a=0\). If \(|B_n|\) is not uniformly integrable, first moments can have additional escaping mass not determined by the weak limit; if \(A_n\) is not uniformly integrable, even the weak stability of the reweighted laws can fail.

## References
1. S. Huang, *Stability of Change-of-Numéraire Reweighting: An Exact Wasserstein Boundary*, arXiv:2609.30329v1, first public 2026-09-24. Primary MSC 60B10.
2. M. Beiglböck, G. Pammer, and L. Riess, *Change of numeraire for weak martingale transport*, Stochastic Processes and their Applications 192 (2026), 104779; preprint arXiv:2406.07523.
3. C. Villani, *Optimal Transport: Old and New*, Springer, 2009, Theorem 6.9, for the standard weak-plus-moment characterization of Wasserstein convergence.
