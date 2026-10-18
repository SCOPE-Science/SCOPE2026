# Ultrafilter diagonal coefficients bound strictly singular and essential distances
## Finding
Let \(Z_V\) be an infinite-dimensional Janson--Sobolev or Janson--Sobolev--Hardy space in the setting of Kazaniecki--Lechner, and let \(\mathcal K_1,\ldots,\mathcal K_s\) be the finest bounded partition associated with the basis \(\mathcal B\). Put \(Q_t=Q_{\mathcal K_t}^{\mathcal B}\). For every bounded diagonal operator \(D:Z_V\to Z_V\) and every nonprincipal ultrafilter \(\mathcal U\),
\[
\operatorname{dist}(D,\mathcal{SS}(Z_V))\ge
\max_{1\le t\le s}\frac{\max_{k\in\mathcal K_t}|\lambda_{\mathcal U}^k(D)|}{\|Q_t\|},
\]
and
\[
\operatorname{dist}(I-D,\mathcal{SS}(Z_V))\ge
\max_{1\le t\le s}\frac{\max_{k\in\mathcal K_t}|1-\lambda_{\mathcal U}^k(D)|}{\|Q_t\|}.
\]
Here \(\mathcal{SS}(Z_V)\) denotes the ideal of strictly singular operators. Since compact operators are strictly singular,
\[
\|D\|_e\ge\operatorname{dist}(D,\mathcal{SS}(Z_V)),\qquad
\|I-D\|_e\ge\operatorname{dist}(I-D,\mathcal{SS}(Z_V)),
\]
so the displayed coefficient bounds also lower-bound the corresponding essential norms. In particular, strict singularity of \(D\) forces \(\lambda_{\mathcal U}^k(D)=0\) for every \(k\) and every nonprincipal \(\mathcal U\); strict singularity of \(I-D\) forces all those coefficients to be \(1\).

## Assumptions and scope
The space, basis, coefficient functionals \(\lambda_{\mathcal U}^k\), finest bounded partition, and canonical projections are exactly those of arXiv:2610.01628v1. Every block \(\mathcal K_t\) is nonempty, so \(E_t=Q_t Z_V\) contains basis vectors from infinitely many filtration levels and is infinite-dimensional. No claim is made that vanishing of all ultrafilter coefficients is sufficient for compactness or strict singularity.

## Proof
Fix \(t\) and \(k\in\mathcal K_t\), and abbreviate \(Q=Q_t\) and \(\lambda=\lambda_{\mathcal U}^k(D)\). If \(\lambda=0\), the desired bound for this pair is trivial. Assume \(\lambda\ne0\), and choose \(k\) as the representative of \(\mathcal K_t\) in Theorem A of arXiv:2610.01628v1. That theorem says that
\[
S=\sum_j\lambda_{\mathcal U}^{k_j}(D)Q_j
\]
almost projectionally factors through \(D\) with constant \(1^+\). Thus, for arbitrarily small \(\eta>0\), there are bounded \(A,B:Z_V\to Z_V\) with \(AB=I\), \(\|A\|\,\|B\|\le1+\eta\), and \(\|S-ADB\|\le\eta\).

Let \(J:E_t\hookrightarrow Z_V\) be inclusion. The canonical projections are pairwise disjoint on their basis blocks, so \(QSJ=\lambda I_{E_t}\). Hence
\[
T_\eta=\lambda^{-1}QADB J:E_t\to E_t
\]
satisfies
\[
\|I_{E_t}-T_\eta\|\le \frac{\|Q\|}{|\lambda|}\eta.
\]
For sufficiently small \(\eta\), \(T_\eta\) is invertible. Therefore \(I_{E_t}\) factors exactly through \(D\) as
\[
I_{E_t}=A_\eta' D B_\eta',\qquad
A_\eta'=T_\eta^{-1}\lambda^{-1}QA,\quad B_\eta'=BJ,
\]
and
\[
\limsup_{\eta\downarrow0}\|A_\eta'\|\,\|B_\eta'\|\le\frac{\|Q\|}{|\lambda|}.
\]
More explicitly, the product is bounded by
\[
\frac{\|Q\|(1+\eta)}{|\lambda|\bigl(1-\|Q\|\eta/|\lambda|\bigr)},
\]
which tends to \(\|Q\|/|\lambda|\).

Now let \(R\in\mathcal{SS}(Z_V)\). The operator \(A_\eta'RB_\eta'\) is strictly singular on the infinite-dimensional space \(E_t\). Therefore
\[
\|I_{E_t}-A_\eta'RB_\eta'\|\ge1,
\]
because an operator within distance less than \(1\) of the identity is invertible, whereas a strictly singular operator on an infinite-dimensional space is not invertible. Using the exact factorization of the identity,
\[
1\le\|A_\eta'(D-R)B_\eta'\|\le
\|A_\eta'\|\,\|B_\eta'\|\,\|D-R\|.
\]
Letting \(\eta\downarrow0\) gives
\[
\|D-R\|\ge\frac{|\lambda|}{\|Q\|}.
\]
Taking the infimum over strictly singular \(R\), then maximizing over \(k\in\mathcal K_t\) and over \(t\), proves the first inequality.

For the second inequality, apply the same argument to \(I-D\). The coefficient functionals are linear and the source proves \(\lambda_{\mathcal U}^k(I)=1\), so \(\lambda_{\mathcal U}^k(I-D)=1-\lambda_{\mathcal U}^k(D)\). The essential-norm bounds follow from \(\mathcal K(Z_V)\subseteq\mathcal{SS}(Z_V)\).

## Verification
The proof uses only Theorem A and the coefficient identity \(\lambda_{\mathcal U}^k(I)=1\) from arXiv:2610.01628v1, plus standard operator-ideal facts: strict singularity is stable under two-sided bounded composition; an invertible operator on an infinite-dimensional Banach space is not strictly singular; and compact operators are strictly singular. The Neumann correction is quantitative and its denominator is positive once \(\eta<|\lambda|/\|Q\|\). No finite experiment or unproved asymptotic step is used.

## Relationship to prior work
Kazaniecki--Lechner prove that the canonical combination \(S\) almost projectionally factors through \(D\) with constant \(1^+\), and their later corollary uses nonzero coefficient blocks to obtain identity factorizations with a global projection-sum constant. The present statement instead isolates each bounded canonical block and converts its coefficient into a quantitative lower bound in the strictly-singular quotient and therefore in the Calkin quotient. Full-text inspection of arXiv:2610.01628v1 found no discussion of compact or strictly singular operators. Earlier Haar-multiplier factorization work supplies closely related projectional-factorization machinery but does not state these Janson--Sobolev coefficient/ideal-distance inequalities.

## Limitations
These are lower bounds, not formulas for the two distances. The argument does not establish that the bounds are sharp, does not characterize the kernel of all coefficient functionals, and does not prove that coefficient vanishing implies compactness or strict singularity. The principal originality risk is that the generic factorization-to-operator-ideal estimate may have appeared elsewhere in abstract form; the source-specific blockwise inequalities were not found in the inspected literature or database searches.

## References
[1] K. Kazaniecki and R. Lechner, *Diagonal operators on Janson-Sobolev and Janson-Sobolev-Hardy spaces*, arXiv:2610.01628v1, first public 2026-10-01. Theorem A; coefficient identity used in the proof following Corollary 11.6.

[2] R. Lechner, P. Müller, T. Schlumprecht, and P. Motakis, *Multipliers on bi-parameter Haar system Hardy spaces*, Mathematische Annalen 390 (2024), 5669--5752. Relevant for the preceding approximate projectional-factorization framework.
