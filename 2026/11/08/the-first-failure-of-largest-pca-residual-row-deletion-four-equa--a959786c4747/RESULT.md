# The first failure of largest-PCA-residual row deletion: four equal-norm rows in three dimensions

## Finding

**Theorem (sharp sample-and-ambient-dimension boundary).** Let \(W\in\mathbb R^{m\times d}\), with \(m,d\ge1\), have rows \(w_i\) of the same positive Euclidean length \(a\). Take **any** unit leading right singular vector \(v\) of \(W\), and define the pilot residual scores
\[
h_i=\|w_i\|_2^2-|w_i v|^2.
\]
Delete any row \(i_*\) attaining \(\max_i h_i\), and refit the other rows by the best rank-at-most-one approximation; call its squared Frobenius error
\[
E_i=\min_{\operatorname{rank}(B)\le1}\|W_{-i}-B\|_F^2.
\]
If \(d\le2\), or if \(m\le3\), then **every** maximizing \(i_*\) minimizes \(E_i\) over all possible single-row deletions, including all singular-value tie cases. The conclusion fails for some equal-norm input with \(m=4\) and \(d=3\), where the maximizing pilot residual is unique. Consequently \((m,d)=(4,3)\) is the first possible size of a failure in this family, in both coordinates.

Here the rule is *one raw, unrecomputed full-matrix PCA residual followed by a single deletion and optimal refit*. It is not asserted to be the multistage D-SLR algorithm, or a general robust-PCA algorithm.

## Assumptions and scope

Real matrices, uncentered rank-one SVD approximation in squared Frobenius norm, and exact arithmetic are used. There are no distributional assumptions. All rows have the same strictly positive norm; all possible choices of a leading right singular vector and of a maximum-score row are included. If there are no remaining rows, their rank-one fitting error is zero. The ambient dimension can exceed the row count.

The motivating combinatorial objective is to select one row for exact storage while fitting the remaining rows with a rank-one model. The cost \(E_i\), after refitting, is distinct from the fixed-subspace surrogate \(\sum_{j\ne i}h_j\).

## Proof

**1. At most two columns.** The case \(d=1\) is immediate. For \(d=2\), write each row as
\[
w_i=a(\cos\theta_i,\sin\theta_i),\qquad z_i=e^{2\mathrm i\theta_i},\qquad Z=\sum_{j=1}^m z_j.
\]
The squared singular values of \(W\) are \(a^2(m\pm |Z|)/2\). When \(Z\ne0\), its unique top right singular line has doubled angle \(Z/|Z|\); therefore
\[
h_i=\frac{a^2}{2}\left(1-\frac{\Re(z_i\overline Z)}{|Z|}\right).
\]
After deleting row \(i\), the sum of doubled-angle phases is \(Z-z_i\), and the smaller squared singular value of the remaining rows is
\[
E_i=\frac{a^2}{2}\left(m-1-|Z-z_i|\right).
\]
Because \(|Z-z_i|^2=|Z|^2+1-2\Re(z_i\overline Z)\), a maximum of \(h_i\) is exactly a minimum of \(E_i\), including all score ties. If \(Z=0\), the full-matrix top singular value is tied, but \(|Z-z_i|=1\) for every \(i\). Hence all deletion errors coincide and every choice is optimal, whatever leading vector was selected. The formula remains valid when \(m=1\).

**2. At most three rows, in any dimension.** Cases \(m\le2\) are immediate. For \(m=3\), set \(G=WW^T\). Its diagonal entries are all \(a^2\); denote its off-diagonal entries by \(g_{ij}\). The two-row Gram matrix after removing \(i\) has eigenvalues \(a^2\pm |g_{jk}|\), where \(\{i,j,k\}=\{1,2,3\}\). Thus
\[
E_i=a^2-|g_{jk}|.
\]
Suppose the largest eigenvalue \(\lambda\) of \(G\) is simple, and let \(u\) be its unit eigenvector. The chosen full-matrix right singular vector satisfies \(Wv=\sqrt\lambda\,u\) up to sign, so \(h_i=a^2-\lambda u_i^2\). With \(p(t)=\det(tI-G)\), the spectral-projector/cofactor identity gives
\[
u_i^2=\frac{\operatorname{adj}(\lambda I-G)_{ii}}{p'(\lambda)}
=\frac{(\lambda-a^2)^2-|g_{jk}|^2}{p'(\lambda)},
\qquad p'(\lambda)>0.
\]
Therefore the largest pilot residuals are precisely the deletions retaining the largest magnitude \(|g_{jk}|\), hence the minimizers of \(E_i\). If the top eigenvalue is double, then \(G=\lambda I+(\mu-\lambda)zz^T\), where \(\mu<\lambda\) and \(z\) is a unit eigenvector for the simple bottom eigenvalue. Equal diagonal entries of \(G\) imply \(|z_1|=|z_2|=|z_3|\); all \(|g_{jk}|\) coincide. If all eigenvalues tie, \(G=a^2I\), and again all \(|g_{jk}|\) coincide. Thus every deletion is optimal in either tied-leading-eigenvalue case, irrespective of the selected leading right singular vector.

**3. Exact failure with four rows in three dimensions.** Every row of
\[
W_0=\begin{pmatrix}
-3/5&4/5&0\\
-2/3&-2/3&-1/3\\
-2/3&1/3&2/3\\
-1/3&-2/3&-2/3
\end{pmatrix}
\]
has norm one. Put \(C=W_0^TW_0\). Direct multiplication gives
\[
C=\begin{pmatrix}34/25&-8/225&0\\-8/225&41/25&8/9\\0&8/9&1\end{pmatrix},
\quad p(t)=\det(tI-C)=\frac{2025t^3-8100t^2+8989t-2338}{2025}.
\]
The polynomial changes sign across each of \((0,1)\), \((1,2)\), and \((2,3)\), so its eigenvalues are simple. Moreover \(p(9/4)=-3391/129600<0\), hence its largest eigenvalue \(\lambda\) obeys \(\lambda>9/4\). Let
\[
s_i(t)=w_i\operatorname{adj}(tI-C)w_i^T.
\]
Exact cofactor algebra gives
\[
s_2-s_1=\frac{19t-35}{81},\quad
s_3-s_1=\frac{139t-299}{2025},\quad
s_4-s_1=\frac{1064(t-1)}{2025}.
\]
All three differences are strictly positive at \(\lambda>9/4\). By the same simple-eigenvalue projector identity as above, \(|w_iv|^2=s_i(\lambda)/p'(\lambda)\) with \(p'(\lambda)>0\). Therefore \(h_1>h_2,h_3,h_4\): the raw pilot uniquely deletes the **first** row.

Yet deleting the first row leaves a Gram matrix with largest eigenvalue exactly \(1+4\sqrt5/9\), because
\[
\det\bigl(tI-(C-w_1^Tw_1)\bigr)=\frac{(t-1)(81t^2-162t+1)}{81}.
\]
Deleting the third row instead yields
\[
\det\bigl(tI-(C-w_3^Tw_3)\bigr)=\frac{2025t^3-6075t^2+4214t-324}{2025},
\]
which is negative at \(t=999/500\), specifically \(-815503/375000000\). This symmetric matrix therefore has an eigenvalue greater than \(999/500\). Since
\[
1+\frac{4\sqrt5}{9}<\frac{999}{500},
\]
and both matrices have trace three, the optimally refitted rank-one errors obey \(E_3<E_1\) strictly. This completes both the counterexample and the minimality classification.

## Verification

The included `verify.py` rederives the exact rational witness Gram matrix and characteristic polynomials, the three signed cofactor differences, the isolation inequality, and the strict out-of-sample refit comparison. It also checks the symbolic three-row cofactor identity with indeterminate entries and performs 2,625 deterministic-seed supplementary numeric samples across two-column and three-row families. Run from this directory using `python verify.py` with SymPy and NumPy installed. The analytic derivation above, not the numerical samples, proves the claims for all dimensions and inputs.

## Relationship to prior work

Szolnoky [1] studies disjoint exact-row storage plus a low-rank approximation and explicitly distinguishes an easily sorted fixed-basis residual surrogate from the refitted actual error. This is the same objective-level distinction behind the theorem, but the algorithm in [1] also constructs a second basis after initial flagging, performs a shape sweep, and offers optional verification; the theorem analyzes **only** the one-row raw-pilot simplification, not that algorithm's output guarantee. Bhaskara and Kumar [2] treat the broader outlier-removal low-rank approximation problem with approximation algorithms, not this exact equal-row-norm dimensional frontier. The elementary Eckart–Young theorem and cofactor identities supply proof tools, not the dimension-minimal residual-pruning classification.

## Limitations

The equal-row-norm hypothesis is essential to the particular proof and is not claimed necessary. The theorem says nothing about deleting two or more rows, ranks greater than one, centered PCA, other loss functions, approximate singular vectors, or the full multistage algorithm of [1]. The four-by-three example establishes a strict but small loss of optimality; no universal worst-case approximation ratio is claimed. The literature comparison does not prove historical uniqueness, and no independent validation of the theorem has been performed.

## References

[1] Vincent Szolnoky, *D-SLR: The Disjoint Row-Sparse plus Low-Rank Decomposition*, arXiv:2610.10636v1, publicly posted 2026-10-07. https://arxiv.org/abs/2610.10636

[2] Aditya Bhaskara and Srivatsan Kumar, *Low Rank Approximation in the Presence of Outliers*, arXiv:1804.10696, publicly posted 2018-04-27. https://arxiv.org/abs/1804.10696
