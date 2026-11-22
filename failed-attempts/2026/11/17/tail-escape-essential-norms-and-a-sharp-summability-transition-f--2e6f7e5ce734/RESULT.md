# Tail-escape essential norms and a sharp summability transition for weighted tree Lipschitz multipliers

## Finding
Let \(T\) be an infinite, locally finite rooted tree with root \(o\), and let \(c_v>0\) be arbitrary real edge weights for nonroot vertices \(v\). On the **big** real weighted Lipschitz space
\[
\mathcal L_c(T)=\left\{f:T\to\mathbb R:\ \sup_{v\ne o}c_v|f(v)-f(v^-)|<\infty\right\},\qquad
\|f\|_c=|f(o)|+\sup_{v\ne o}c_v|f(v)-f(v^-)|,
\]
consider a bounded pointwise multiplier \(M_\psi f=\psi f\). For an integer \(N\ge0\), put
\[
\mathcal E_N(\psi)=\sup_{|v|>N}\left(
|\psi(v)|+c_v|\psi(v)-\psi(v^-)|
\sum_{\substack{w\in[o,v^-]\\ |w|>N}}\frac1{c_w}
\right).
\]
The sum excludes the root, and an empty sum is zero. The exact essential norm (distance to **all** compact linear operators on the big space) is
\[
\boxed{\|M_\psi\|_{\mathrm e}=\lim_{N\to\infty}\mathcal E_N(\psi).}
\tag{1}
\]
The limit exists because the quantities decrease as \(N\) grows.

For polynomial weights \(c_v=|v|^\alpha\) with \(\alpha\ge0\), define \(H_{n-1}^{(\alpha)}=\sum_{j=1}^{n-1}j^{-\alpha}\). Formula (1) becomes the sharp dichotomy
\[
\boxed{
\|M_\psi\|_{\mathrm e}=
\begin{cases}
\displaystyle\limsup_{|v|\to\infty}\left(|\psi(v)|+|v|^\alpha H_{|v|-1}^{(\alpha)}|\Delta\psi(v)|\right),&0\le\alpha\le1,\\[5pt]
\displaystyle\limsup_{|v|\to\infty}|\psi(v)|,&\alpha>1.
\end{cases}}
\tag{2}
\]
In particular, for every \(\alpha>1\), a bounded multiplier is compact if and only if \(\psi(v)\to0\) radially. For every \(0\le\alpha\le1\), there are bounded symbols tending to zero whose multipliers are **not** compact; an explicit example below has essential norm exactly \(2\). For \(\alpha>1\) there are compact multipliers on the big space that do **not** preserve the corresponding little weighted Lipschitz space.

## Assumptions and scope
The tree is infinite, countable and locally finite; \(|v|\) is combinatorial depth, \(v^-\) is the parent, and \([o,v^-]\) denotes the nonroot vertices on the path ending at the parent. Scalars are real. The arbitrary edge weights \(c_v\) are positive, without uniform upper or lower bounds. No assumption is made that \(M_\psi\) preserves the little space. The essential norm is the infimum over all compact operators \(K:\mathcal L_c(T)\to\mathcal L_c(T)\), not just compact multipliers. All radial limits use depth, and local finiteness ensures each closed depth ball is finite.

For completeness, writing \(\beta_v=c_v(\psi(v)-\psi(v^-))\) and \(H_c(v)=\sum_{\substack{w\in[o,v^-]\\w\ne o}}c_w^{-1}\), the exact bounded-operator norm is
\[
\|M_\psi\|=\max\left\{
|\psi(o)|+\sup_{v\ne o}|\beta_v|,\quad
\sup_{v\ne o}\bigl(|\psi(v)|+|\beta_v|H_c(v)\bigr)
\right\}.
\tag{3}
\]
Thus boundedness is equivalent to finiteness of the right side; it is not presumed from a pointwise bound on \(\psi\) alone.

## Proof
**1. Isometric coordinates.** For each \(f\in\mathcal L_c(T)\), define
\[
x_o=f(o),\qquad x_v=c_v(f(v)-f(v^-)),\qquad
f(v)=x_o+\sum_{w\in[o,v]}\frac{x_w}{c_w},
\]
where only nonroot vertices occur in the sum. Every finite path sum is defined, so this identifies the big space isometrically with \(E=\mathbb R\oplus_1\ell_\infty(T\setminus\{o\})\), with norm \(|x_o|+\|x\|_\infty\). There is **no** \(c_0\) condition in this identification.

The multiplier becomes an operator \(A\) with root output \((Ax)_o=\psi(o)x_o\) and edge output
\[
(Ax)_v=\beta_vx_o+\psi(v)x_v+\beta_v\sum_{w\in[o,v^-]}\frac{x_w}{c_w}.
\tag{4}
\]
The two summands of \(E\) give (3): the norm of the root-input column is \(|\psi(o)|+\sup|\beta_v|\), and the norm of the map on its \(\ell_\infty\) summand is the supremum of the finite absolute row sums \(|\psi(v)|+|\beta_v|H_c(v)\).

**2. Finite-rank upper estimate.** Let \(P_N\) be coordinate truncation to the root and all edge coordinates of depth at most \(N\). The operator
\[
K_N=P_NA+(I-P_N)AP_N
\]
is finite rank: the first term has finite-dimensional range and the second has finite-dimensional input. Furthermore
\[
A-K_N=(I-P_N)A(I-P_N).
\]
By (4), its norm is exactly \(\mathcal E_N(\psi)\), because each remaining output row has a diagonal coefficient \(\psi(v)\) and tail ancestor coefficients \(\beta_v/c_w\) on the retained \(\ell_\infty\) input. Hence \(\|A\|_{\mathrm e}\le\lim_N\mathcal E_N\).

**3. Compact-operator lower estimate.** Write \(L=\lim_N\mathcal E_N\). If \(L=0\), the preceding bound proves the assertion. Otherwise choose recursively increasing integers \(N_j\), each larger than all coordinates used previously, and vertices \(v_j\) of depth greater than \(N_j\), so that the absolute sum of the \(v_j\)-row supported on edges of depth greater than \(N_j\) exceeds \(L-1/j\). This is possible since \(\mathcal E_{N_j}\ge L\). Choose \(x^{(j)}\in E\) with root coordinate zero, supported on those finitely many edge coordinates, and with each coordinate equal to the sign of the corresponding row coefficient. Then \(\|x^{(j)}\|=1\) and \(\|Ax^{(j)}\|\ge L-1/j\). The supports are pairwise disjoint.

**Disjoint-support lemma.** A bounded sequence of vectors in \(\ell_\infty(I)\) with pairwise disjoint supports is weakly null. Indeed, for every bounded linear functional \(\varphi\), choose phases/signs on any finite collection to obtain \(\sum_{j\le m}|\varphi(x^{(j)})|\le\|\varphi\|\sup_{j\le m}\|x^{(j)}\|\). Thus the scalar evaluations are absolutely summable. The same applies to the vectors with root coordinate zero in \(E\).

Consequently \(Kx^{(j)}\to0\) in norm for **any** compact \(K:E\to E\). Therefore \(\|A-K\|\ge\limsup_j(\|Ax^{(j)}\|-\|Kx^{(j)}\|)\ge L\). Infimizing over all compact operators proves (1). The argument does not invoke weak convergence of arbitrary pointwise-null bounded sequences in \(\ell_\infty\), which would be invalid.

**4. Polynomial weights.** Put \(n=|v|\). When \(\alpha>1\), the sums \(\sum_{k>N}k^{-\alpha}\) tend to zero uniformly in their upper endpoint. Boundedness in (3) implies \(\sup|\beta_v|<\infty\), so the second term in \(\mathcal E_N\) tends uniformly to zero and (2) reduces to the radial limsup of \(|\psi|\).

When \(0\le\alpha\le1\), \(H_{n-1}^{(\alpha)}\to\infty\). Boundedness and (3) give \(|\beta_v|H_{n-1}^{(\alpha)}\le\|M_\psi\|\), hence \(|\beta_v|\to0\) uniformly in depth. Removing any fixed finite ancestor prefix from a row therefore changes its norm by an amount tending to zero as \(n\to\infty\). Formula (1) becomes the first line of (2). Since both summands are nonnegative, the compactness criteria follow.

**5. Sharpness and failure to preserve the little space.** Fix any infinite locally finite rooted tree and define symbols depending only on depth. For \(0\le\alpha\le1\), put \(S_n=\sum_{k=1}^n k^{-\alpha}\) and
\[
\psi(o)=0,\qquad \psi(v)=\frac{(-1)^{|v|}}{|v|^\alpha S_{|v|}}\quad(|v|\ge1).
\]
Then \(\psi(v)\to0\). For \(n\ge2\), direct cancellation gives
\[
n^\alpha H_{n-1}^{(\alpha)}|\Delta\psi(v)|
=\frac{S_{n-1}}{S_n}+\left(\frac n{n-1}\right)^\alpha\longrightarrow 2.
\]
Thus (3) proves boundedness and (2) proves \(\|M_\psi\|_{\mathrm e}=2\), despite \(\psi\to0\).

For \(\alpha>1\), put \(\psi(o)=0\) and \(\psi(v)=(-1)^{|v|}|v|^{-\alpha}\) at every nonroot vertex. Then \(|\beta_v|=1+(n/(n-1))^\alpha\to2\), \(\psi(v)\to0\), and (3) proves boundedness. Formula (2) proves **compactness** on the big space. But the constant function \(1\) belongs to the little weighted space, while \(M_\psi1=\psi\) does not, because \(c_v|\Delta\psi(v)|\to2\). This demonstrates that the big-space compactness theorem cannot be deduced by pretending that a bounded big-space multiplier acts on the little space.

## Verification
A standalone exact-rational checker accompanies this result. It reconstructs multiplier matrices in weighted difference coordinates on several small rooted trees; compares the claimed operator norm with unrestricted sign-vector maximization; and checks every finite-section row-tail identity for three polynomial weights and 90 rational symbol profiles, totaling 510 nonroot row profiles. It also verifies the explicit critical-symbol identity for \(\alpha=0,1\) and quantitative summable-tail bounds for \(\alpha=2\). Exact finite checks corroborate the row algebra. The compact-operator assertion and the polynomial sharpness claims are proved by the analytic arguments above, not by finite enumeration.

Run using `python3 check_big_tree_multipliers.py` from this package. Only Python standard-library modules are required.

## Relationship to prior work
Allen, Colonna and Easley established boundedness, compactness and **two-sided estimates**, not an exact essential norm, for the ordinary big and little weighted tree Lipschitz multiplier at \(c_v=|v|\). Colonna and Martínez-Avendaño (first public October 9, 2024) develop operator theory on the **little** tree Lipschitz space. A previously published published-finding corpus result, *Exact essential norms for multipliers on little weighted Lipschitz spaces of rooted trees* (2026), gives an arbitrary-weight tail-row formula on the little space \(c_0\); its explicit scope excludes the big \(\ell_\infty\) spaces. The present theorem treats the big spaces and the unrestricted compact-operator distance, supplies a disjoint-support weakly null argument suitable for \(\ell_\infty\), and exhibits a summable-weight regime with compact big-space multipliers that do not even preserve the little space. The row-coordinate identity itself and finite-rank truncation are elementary tools and are **not** asserted to be original in isolation.

## Limitations
Originality is a best-knowledge claim, not a proof that no equivalent formula exists under operator-matrix, weighted \(\ell_\infty\), or summability terminology. The general tail formula assumes an infinite locally finite rooted tree and the stated sum norm. There is no claim about arbitrary graphs with cycles, other Banach norms, nonmultiplication operators, or noncompactness of a symbol merely because it fails to preserve the little space. The theorem is analytically proved and finitely checked; independent mathematical validation has not been performed.

## References
1. F. Colonna and R. A. Martínez-Avendaño, *Composition Operators on the Little Lipschitz Space of a Rooted Tree*, first arXiv public submission 2024-10-09, arXiv:2410.14714. https://arxiv.org/abs/2410.14714
2. R. F. Allen, F. Colonna and G. R. Easley, *Multiplication Operators on the Weighted Lipschitz Space of a Tree*, Journal of Operator Theory 69 (2013), 209–231, DOI:10.7900/jot.2010sep22.1885. Open manuscript https://arxiv.org/abs/2207.12616 (the paper predates that manuscript upload).
3. *Exact essential norms for multipliers on little weighted Lipschitz spaces of rooted trees*, published published-finding corpus record (2026), https://github.com/published-finding corpus/2026/blob/main/2026/9/21/SCOPE-exact-essential-norm-little-tree-lipschitz-multipliers--6b05c4d0072a/RESULT.md
