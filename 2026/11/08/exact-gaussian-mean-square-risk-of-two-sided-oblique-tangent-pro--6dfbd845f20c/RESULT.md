# Exact Gaussian mean-square risk of two-sided oblique tangent projection

## Finding

Fix integers \(1\le r<\min(m,n)\) and \(r\le\ell\le\min(m,n)\). Let \(U\in\mathbb R^{m\times r}\) and \(V\in\mathbb R^{n\times r}\) have orthonormal columns, and let independent \(\Theta\in\mathbb R^{\ell\times m}\) and \(\Omega\in\mathbb R^{\ell\times n}\) have independent \(N(0,1/\ell)\) entries. Define the almost-surely well-defined oblique projectors
\[
Q=U(\Theta U)^\dagger\Theta,\qquad R=V(\Omega V)^\dagger\Omega,
\]
and the two tangent-space projectors, acting on any fixed \(F\in\mathbb R^{m\times n}\),
\[
\mathcal P F=UU^{\mathsf T}F+FVV^{\mathsf T}-UU^{\mathsf T}FVV^{\mathsf T},\quad
\widetilde{\mathcal P}F=QF+FR^{\mathsf T}-QFR^{\mathsf T}.
\]
Write \(N=(I-UU^{\mathsf T})F(I-VV^{\mathsf T})\), the component normal to the rank-\(r\) matrix manifold. Then:

1. When \(\ell>r+1\), the error \(E=\widetilde{\mathcal P}F-\mathcal P F\) is unbiased and obeys the **exact** rank- and dimension-uniform identity
\[
\mathbb E E=0,\qquad
\mathbb E\|E\|_F^2=
\left[\frac{2r}{\ell-r-1}+\left(\frac{r}{\ell-r-1}\right)^2\right]\|N\|_F^2.
\]
Consequently \(\mathbb E\|\widetilde{\mathcal P}F\|_F^2=\|\mathcal P F\|_F^2+\mathbb E\|E\|_F^2\).
2. If \(N\ne0\) and \(\ell=r+1\), the error still has a well-defined zero expectation, but \(\mathbb E\|E\|_F^2=+\infty\). For \(\ell=r\), the squared expectation is again infinite; no ordinary first-moment assertion is made at this endpoint.
3. If \(N=0\), the error vanishes almost surely for every \(\ell\ge r\).
4. For any sequence \(r\to\infty\) with \(\ell/r\to\gamma>1\), the normalized mean-square risk (when \(N\ne0\)) tends to \(2/(\gamma-1)+1/(\gamma-1)^2\). In particular, the widely used scaling \(\ell=2r\) has limiting normalized risk \(3\), **even when \(N\) has rank one**. Thus a fixed sketch-to-rank ratio cannot make this worst-case-normal-component mean-square error vanish.

## Assumptions and scope

All spaces, sketches, matrix entries, pseudoinverses, and projectors are real and exact-arithmetic. The vector field value \(F\) and frames \(U,V\) are deterministic, or are fixed conditional on information independent of both sketches. Gaussian sketch rows are independent; the two sketches themselves are independent. The result is pointwise for the lifted oblique tangent projector, not a global error bound for an integrated matrix ODE. A change of sketch normalization does not affect the oblique projector because pseudoinversion cancels scalar factors.

## Proof

**Deterministic decomposition.** Since \(QU=U\), \(RV=V\), and both \(Q\) and \(R\) are idempotent, the two tangent projectors agree on every tangent matrix \(UA^{\mathsf T}+BV^{\mathsf T}\). They may therefore differ only on \(N\). Direct substitution yields
\[
E=QN+NR^{\mathsf T}-QNR^{\mathsf T}.
\]
Each of these three matrices is mutually Frobenius-orthogonal to the others: their row and column supports belong respectively to \((\operatorname{im}U,\operatorname{im}V^\perp)\), \((\operatorname{im}U^\perp,\operatorname{im}V)\), and \((\operatorname{im}U,\operatorname{im}V)\). In particular
\[
\|E\|_F^2=\|QN\|_F^2+\|NR^{\mathsf T}\|_F^2+\|QNR^{\mathsf T}\|_F^2.
\]
Choose orthogonal completions \([U\ U_\perp]\) and \([V\ V_\perp]\), and write \(N=U_\perp C V_\perp^{\mathsf T}\). Denote
\[
G=\Theta U,\quad H=\Theta U_\perp,\quad A=G^\dagger H;
\qquad J=\Omega V,\quad K=\Omega V_\perp,\quad B=J^\dagger K.
\]
The Gaussian blocks \(G,H,J,K\) are independent except for the intentional shared left inverse within \(A\) or \(B\); the matrices \(A\) and \(B\) are independent. The three squared terms above reduce to \(\|AC\|_F^2\), \(\|CB^{\mathsf T}\|_F^2\), and \(\|ACB^{\mathsf T}\|_F^2\).

**Exact Gaussian second moment.** The entry variance \(1/\ell\) cancels in \(G^\dagger H\). Conditional on \(G\), the columns of \(A\) are independent centered Gaussians with covariance \((G_0^{\mathsf T}G_0)^{-1}\), where \(G_0\) is standard normal with \(\ell\) rows and \(r\) columns. For each diagonal of this inverse Gram matrix, regression onto the other \(r-1\) columns gives
\[
\big[(G_0^{\mathsf T}G_0)^{-1}\big]_{jj}
\stackrel{d}{=}\big(\chi^2_{\ell-r+1}\big)^{-1}.
\]
Integrating the chi-square density gives \(\mathbb E[(\chi_d^2)^{-1}]=1/(d-2)\) precisely when \(d>2\), and infinity otherwise. Therefore for \(\ell>r+1\), isotropy in the normal coordinates implies
\[
\mathbb E(A^{\mathsf T}A)=a I_{m-r},\quad
\mathbb E(B^{\mathsf T}B)=a I_{n-r},\qquad a=\frac{r}{\ell-r-1}.
\]
It follows that \(\mathbb E\|AC\|_F^2=a\|C\|_F^2\), \(\mathbb E\|CB^{\mathsf T}\|_F^2=a\|C\|_F^2\), and, by conditioning first on \(B\) and then on \(A\), \(\mathbb E\|ACB^{\mathsf T}\|_F^2=a^2\|C\|_F^2\). Orthogonality of the three terms proves the formula.

**Critical threshold and first moment.** For nonzero \(C\), \(\mathbb E\|AC\|_F^2\) is infinite when \(\ell-r+1\le2\): at least one nonzero column of \(C\), combined with row symmetry, contributes a positive multiple of the divergent inverse-chi-square mean. Since the three norm squares add without cancellation, \(\mathbb E\|E\|_F^2=+\infty\). At \(\ell=r+1\), the inverse-chi-square square-root moment is finite because \(\ell-r+1=2>1\), so all entries of \(A,B\) are integrable. Independence makes entries of \(ACB^{\mathsf T}\) integrable as well. Conditional centering of \(A,B\) yields \(\mathbb E E=0\). For \(N=0\), the deterministic decomposition gives \(E=0\).

Finally, substituting \(\ell/r\to\gamma>1\) gives the stated nonzero limiting risk; when \(\ell=2r\) and \(r>1\), the finite-rank normalized risk is exactly \(2r/(r-1)+r^2/(r-1)^2\).

## Verification

Run `python VERIFY.py` with NumPy and SymPy installed. The program performs exact-rational projector and orthogonality identities for several full-rank sketch sizes, and 14,000 seeded Gaussian trials for each of three independent parameter cases. It prints `VERIFY_OK` on success. Observed squared-error means for rank/sketch pairs \((r,\ell)=(1,5),(2,8),(3,11)\) were \(0.796953,0.947570,1.041534\), compared to analytical means \(0.777778,0.960000,1.040816\). These simulations are diagnostics, **not** substitutes for the infinite-moment or all-dimensional proof.

## Relationship to prior work

Carrel and Grigori (2026, arXiv:2607.03402, Lemmas 4.1–4.2 and Section 4.2) define the lifted two-sided oblique tangent projection, show when it agrees with classical dynamical low-rank approximation, and highlight qualitative sensitivity to a normal residual. The present theorem evaluates its **exact Gaussian mean-square deviation**, including a sharp integrability boundary and nonvanishing fixed-oversampling limit. Niu, Garg, Dereziński and Liao (2026, arXiv:2605.24955, Sections 2–3) analyze one-sided oblique projections for random row *sampling* and discuss the classical Gaussian inverse-Wishart moment; their principal results do not specify the two-sided tangent composition considered here. The Gaussian pseudoinverse second moment is standard (Halko, Martinsson and Tropp, 2011, Proposition 10.2) and is an ingredient, not itself the stated projection-risk identity. A possibility of an older formulation obtained by combining these ingredients is a residual historical-priority risk.

## Limitations

The formula assumes independent isotropic **real Gaussian** sketches, orthonormal fixed frames, and a fixed vector-field value independent of the sketches. It does not extend automatically to adaptive sketches, non-Gaussian ensembles, or correlated left/right sketches. The variance is a local instantaneous projection statistic, not a proven trajectory-error bound or a claim of instability for all oblique integrators. Finite simulations do not establish the analytical formula or divergence.

## References

- B. Carrel and L. Grigori, *Sketch low-rank dynamics: orthogonal vs. oblique projections*, arXiv:2607.03402v1 (first public 2026-07-03), https://arxiv.org/html/2607.03402.
- C. Niu, S. Garg, M. Dereziński and Z. Liao, *Debiasing Random Oblique Projections for Subsampled OLS and Fast CUR in High Dimensions*, arXiv:2605.24955v1 (2026), https://arxiv.org/html/2605.24955v1.
- N. Halko, P. G. Martinsson and J. A. Tropp, *Finding Structure with Randomness: Probabilistic Algorithms for Constructing Approximate Matrix Decompositions*, SIAM Review 53(2), 217–288 (2011), Proposition 10.2, https://arxiv.org/abs/0909.4061.
