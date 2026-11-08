# Upper Banach means govern power growth of positive-coupling shift blocks

## Finding
Let \(S\) be the unilateral forward shift on \(\ell^2(\mathbb N_0)\), and let \(D_c e_j=c_j e_j\), where \(0<c_j\le M<\infty\) for every \(j\). Define the invertible block operator
\[
T_c=\begin{pmatrix}S&D_c\\0&S^*\end{pmatrix},\qquad
\beta(c)=\lim_{n\to\infty}\sup_{m\ge0}\frac1n\sum_{j=0}^{n-1}c_{m+j}.
\]
The limit exists and equals the infimum of the displayed moving averages over positive \(n\). The **exact linear power-growth coefficient** is
\[
\boxed{\lim_{n\to\infty}\frac{\|T_c^n\|}{n}=\beta(c).}
\]
In particular \(\|T_c^n\|=o(n)\) if and only if \(\beta(c)=0\). If \(c_j=t>0\) for all \(j\), then, for every integer \(n\ge1\),
\[
\boxed{\|T_c^n\|=\tfrac12\bigl(nt+\sqrt{n^2t^2+4}\bigr).}
\]
The invariant \(\beta\) distinguishes high coupling on increasingly long intervals from isolated high coefficients. This is a power-growth result, not a new claim about existence of inverse-invariant subspaces.

## Assumptions and scope
The Hilbert space is complex \(\ell^2(\mathbb N_0)\oplus\ell^2(\mathbb N_0)\); \(S e_j=e_{j+1}\), so \(S^*e_0=0\). The real scalar sequence \(c=(c_j)\) is bounded and strictly positive at each coordinate but need not be bounded away from zero. \(D_c\) is its diagonal multiplier, and \(\|\cdot\|\) denotes the Hilbert-space operator norm. Powers are integer powers \(n\ge1\).

## Proof
**1. The mean exists.** Put \(b_n=\sup_{m\ge0}\sum_{j=0}^{n-1}c_{m+j}\). Positivity and boundedness give \(0<b_n\le nM\), while \(b_{m+n}\le b_m+b_n\). Fekete's subadditive lemma proves that \(\beta=\lim_n b_n/n=\inf_n b_n/n\).

**2. Exact block power and Schur upper bound.** Direct induction gives
\[
T_c^n=\begin{pmatrix}S^n&H_n\\0&(S^*)^n\end{pmatrix},\qquad
H_n=\sum_{j=0}^{n-1}S^{n-1-j}D_c(S^*)^j.
\]
For output row \(i\) and input column \(m\), each nonzero entry of \(H_n\) is \(c_{i-n+1+j}\), with \(m=i-n+1+2j\) and \(0\le j<n\); any term with a negative index is omitted. Each row has at most \(n\) nonnegative entries from a consecutive segment of length at most \(n\), so its sum is at most \(b_n\). Each column likewise has at most \(n\) entries \(c_{m-j}\) from a consecutive segment of length at most \(n\); its sum is at most \(b_n\). Schur's test therefore yields \(\|H_n\|\le b_n\). Since both diagonal blocks have norm one, the scalar triangular-majorant inequality yields
\[
\|T_c^n\|\le \Bigl\|\begin{pmatrix}1&b_n\\0&1\end{pmatrix}\Bigr\|=\frac{b_n+\sqrt{b_n^2+4}}2.
\]

**3. Sharp asymptotic lower bound.** Fix \(n\), take arbitrarily large \(L>4n\), and select a block of \(L\) consecutive entries, indexed \(a,\ldots,a+L-1\), whose sum is at least \(b_L-1\). Let \(x\) be the constant normalized positive vector on \([\max\{0,a-n\},a+L+n]\), and let \(y\) be the constant normalized positive vector on \([a+n,a+L-n-1]\). Their support cardinalities are at most \(L+2n+1\) and exactly \(L-2n\). Every coefficient \(c_k\) with \(a+n\le k\le a+L-2n-1\) occurs at least \(n\) times in the positive bilinear form \(\langle H_nx,y\rangle\); all contributing columns are in the support of \(x\), and all corresponding rows in that of \(y\). Thus
\[
\|H_n\|\ge \frac{n\,[b_L-1-3nM]}{\sqrt{(L+2n+1)(L-2n)}}.
\]
Let \(L\to\infty\). Since \(b_L/L\to\beta\), this proves \(\|H_n\|\ge n\beta\) for every fixed \(n\). The norm of \(T_c^n\) is at least the norm of its upper-right corner, so combining with step 2 gives
\[
 n\beta\le\|H_n\|\le b_n,\quad
 n\beta\le\|T_c^n\|\le\tfrac12\left(b_n+\sqrt{b_n^2+4}\right).
\]
Division by \(n\), followed by \(n\to\infty\), proves the claimed limit.

**4. Invertibility.** Writing \(u_0=\langle u,e_0\rangle\), direct substitution gives the bounded inverse
\[
T_c^{-1}(u,v)=\left(S^*u-S^*D_c S v,\quad Sv+\frac{u_0}{c_0}e_0\right).
\]
No uniform lower bound on the sequence is required.

**5. Constant coupling sharpness.** When \(c_j=t\), step 2 gives the stated scalar-matrix upper bound. For fixed \(n\), take normalized vectors constant on intervals of length tending to infinity, sufficiently far from index zero. On these vectors \(S^n\), \((S^*)^n\) tend in norm to the identity and \(H_n\) tends in norm to multiplication by \(nt\). Testing arbitrary pairs of scalar coefficients on the same vectors therefore gives the matching lower bound, namely the norm of the displayed scalar triangular matrix.

## Verification
The finite-dimensional companion checker `CHECK.py` verifies the block-power coefficient identities, sliding-window subadditivity, and Schur row/column estimates using exact rational arithmetic. It is corroboration only: the infinite-dimensional limit is established by steps 1–5 above, not by extrapolation from finite sections. The bounds are valid for all bounded strictly positive sequences and all positive integer powers.

## Relationship to prior work
Ji and Wang (arXiv:2610.39605v1, public October 29, 2026) study invertible conjugate bi-geometric blocks with positive coupling and establish existence of nontrivial invariant subspaces for inverses. The present question is instead the exact linear power-growth coefficient for the concrete shift/adjoint block, with potentially nonuniform diagonal coupling. Ji, Jiang and Wang (arXiv:2610.12857, public October 9, 2026) address inverse-invariant subspaces under subexponential power growth, not a sharp linear coefficient. Garcia's *The norm and modulus of a Foguel operator* treats related but differently oriented shift/adjoint triangular operators, an important nearest norm-computation precedent. The scalar block bound used above is elementary; the substantive invariant is the exact upper Banach mean for arbitrary positive diagonal couplings.

## Limitations
Only the specific shift/adjoint pair and bounded strictly positive diagonal couplings are treated. No growth coefficient is asserted for general non-diagonal positive couplings, arbitrary Cowen–Douglas operators or operator-norm-normalized inverse powers. A general existing theorem on banded weighted Foguel blocks might contain an equivalent formulation; priority has not been independently certified. The example \(c_j=(j+1)^{-1}\) has \(\beta=0\), whereas arbitrarily long intervals with \(c_j=1\) give \(\beta=1\) even if their asymptotic density is zero.

## References
- K. Ji and Z. Wang, *Riccati Equations and the Third Problem of Halmos*, arXiv:2610.39605v1 (October 29, 2026), https://arxiv.org/html/2610.39605v1.
- K. Ji, C. Jiang and Z. Wang, *Geometric operators and the third problem of Halmos*, arXiv:2610.12857 (October 9, 2026), https://arxiv.org/abs/2610.12857.
- S. R. Garcia, *The norm and modulus of a Foguel operator*, 2009 (classical related norm-computation framework).
