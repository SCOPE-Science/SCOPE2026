# Sharp coordinate Fourier spectrum on \(\mathrm{GL}_m(\mathbb F_q)\) and a dimension–field transition

## Finding
Let \(q\ge2\) be any prime power, \(m\ge2\) an integer, and \(\psi:\mathbb F_q\to\mathbb C^\times\) any nontrivial additive character. Equip \(X=\mathrm{GL}_m(\mathbb F_q)\) with normalized counting measure. Consider the \(K=1+m^2(q-1)\) unit-norm functions
\[
\mathcal F=\{1\}\cup\{A\mapsto\psi(aA_{ij}):1\le i,j\le m,\ a\in\mathbb F_q^\times\}.
\]
Write \(t=q^m\), \(c=q-1\), \(u=-1/(t-1)\), \(v=1/[(t-1)(q^{m-1}-1)]\), and define
\[
\begin{aligned}
\alpha&=\frac{t[t-1-m(q-1)]}{(t-q)(t-1)},\\
\beta&=\frac{t}{t-1},\qquad \gamma=\frac{t}{t-q},\\
 h&=1-u+c[(2m-1)u+(m-1)^2v],\\
H&=\begin{pmatrix}1&m\sqrt c\,u\\m\sqrt c\,u&h\end{pmatrix},\qquad
\ell_\pm=\frac{1+h\pm\sqrt{(1-h)^2+4m^2cu^2}}2.
\end{aligned}
\]
The **complete Gram spectrum**, with multiplicities, is
\[
\boxed{\ell_-^{[1]},\quad\alpha^{[2(m-1)]},\quad
\beta^{[m^2(q-2)]},\quad\gamma^{[(m-1)^2]},\quad\ell_+^{[1]}.}
\]
A zero multiplicity is omitted (it occurs for \(q=2\)). These five labeled spectral values are otherwise strictly ordered except that \(\gamma\) and \(\ell_+\) exchange their order. In all cases \(\ell_-<\alpha<\beta<\min\{\gamma,\ell_+\}\) and \(\ell_->0\), so all functions in \(\mathcal F\) are linearly independent.

The **sharp lower Riesz bound** is always \(\ell_-\). The **sharp upper Riesz bound** has the exact transition
\[
\boxed{\lambda_{\max}=\begin{cases}\gamma,&2\le m\le 2q-1,\\\ell_+,&m\ge2q.\end{cases}}
\]
Both alternatives are strict. In particular, the sharp squared condition number is \(\gamma/\ell_-\) in the first range and \(\ell_+/\ell_-\) in the second. For each fixed prime power \(q\),
\[
\frac{\lambda_{\max}}{\ell_-}=1+\frac{2m\sqrt{q(q-1)}}{q^m}+O_q(q^{-m})\qquad(m\to\infty).
\]

## Assumptions and scope
This concerns the constant plus all **single-entry** additive characters and the coefficient Gram operator on their span, not an entire Fourier basis on \(X\). The Hermitian inner product is \(\langle f,g\rangle=|X|^{-1}\sum_{A\in X}\overline{f(A)}g(A)\); hence every Gram diagonal entry is \(1\). The field may have characteristic two or be a nonprime extension field; no ordering of its nonzero scalars enters the statement.

Equality spaces are explicit. The \(\alpha\)-eigenspace consists of color-uniform coefficients \(z_{ij,a}=r_i+s_j\) with \(\sum_i r_i=\sum_j s_j=0\). The \(\beta\)-eigenspace consists of coefficients whose sum over \(a\in\mathbb F_q^\times\) is zero **separately at every coordinate**. The \(\gamma\)-eigenspace consists of color-uniform \(z_{ij,a}=w_{ij}\) with all row and column sums of \(w\) zero. Both \(\ell_\pm\) are simple: their coefficient vectors mix the constant with equal coefficients across all nonconstant characters, according to the respective eigenvectors of \(H\) in the normalized basis described below. Thus the upper-bound equality space is the row/column-zero interaction space for \(m<2q\) and the one-dimensional \(\ell_+\)-space for \(m\ge2q\); the lower-bound equality space is always the one-dimensional \(\ell_-\)-space.

## Proof
**1. Character sums.** For \(B\in M_m(\mathbb F_q)\) of rank \(r\), let \(S(B)=\sum_{A\in\mathrm{GL}_m(\mathbb F_q)}\psi(\sum_{ij}B_{ij}A_{ij})\). Matrix left/right multiplication makes the sum depend only on \(r\). Independently, Möbius inversion on the lattice of subspaces of \(\mathbb F_q^m\) yields
\[
S(B)=\sum_{d=r}^{m}{m-r\brack d-r}_q(-1)^dq^{\binom d2+m(m-d)}
=(-1)^r q^{\binom m2}\prod_{j=1}^{m-r}(q^j-1).
\]
Here \({n\brack k}_q\) is the Gaussian binomial coefficient; the final equality is the finite \(q\)-binomial product identity. Indeed, summing over maps vanishing on a fixed \(d\)-space gives \(q^{m(m-d)}\) when that space contains the row space of \(B\), and zero otherwise. Since \(|\mathrm{GL}_m(\mathbb F_q)|=q^{\binom m2}\prod_{j=1}^m(q^j-1)\), the normalized transforms for ranks \(0,1,2\) are respectively \(1,u,v\). This exact character-sum evaluation also appears in Li–Hu, Theorem 2.1 [1]. It was checked directly for seven finite-field cases in the attached checker.

The difference between two single-entry coefficient matrices has rank one when the positions coincide or share a row or column, and rank two otherwise. It follows that a Gram entry is \(u\) for rank-one differences, \(v\) for rank-two differences, and \(1\) on the diagonal. Every constant/nonconstant entry is \(u\).

**2. The three scalar eigenspaces and the two-dimensional block.** Set \(c=q-1\). At each matrix coordinate there are \(c\) scalar labels. A color-zero-sum vector at any one coordinate has eigenvalue \(1-u=\beta\), independently of the others, giving multiplicity \(m^2(q-2)\). On the color-uniform sector, normalize each coordinate fiber to a vector of length one. Its Gram block on the \(m\times m\) coordinate grid has diagonal \(1+(c-1)u\), off-diagonal \(cu\) for cells sharing a row or column, and off-diagonal \(cv\) otherwise.

The rook graph on the \(m\times m\) grid has adjacency eigenvalues \(m-2\) (row/column fluctuations, dimension \(2(m-1)\)), \(-2\) (zero row and column sums, dimension \((m-1)^2\)), and \(2(m-1)\) (all-ones, dimension one). The non-neighbor adjacency is \(J-I-A_{\mathrm{rook}}\). Substitution gives \(\alpha\) on the row/column fluctuations and \(\gamma\) on the zero-sum interactions, with the multiplicities and coefficient descriptions above. The all-ones cell direction couples only to the constant; writing the normalized all-character sum as \(e=(m\sqrt c)^{-1}\sum_{i,j,a}e_{ij,a}\) gives the remaining symmetric matrix \(H\). This determines the complete spectrum and all equality spaces.

**3. Strict positivity and the least eigenvalue.** The finite-field binomial inequality \(q^m>1+m(q-1)\) holds for \(m\ge2\); thus \(\alpha>0\). A direct calculation gives
\[
\det H=\frac{t[t-1-m(q-1)]^2}{(t-q)(t-1)^2}>0.
\]
Because the top-left entry of \(H\) is \(1\), both \(\ell_\pm\) are positive. The nonzero off-diagonal entry implies \(\ell_-<1<\ell_+\). Further exact determinant identities are
\[
\begin{aligned}
\det(\alpha I-H)&=\frac{mqt(m-1)(q-1)[m(q-1)-t+1]}{(t-q)^2(t-1)^2}<0,\\
\det(\beta I-H)&=-\frac{t(m-1)^2(q-1)}{(t-q)(t-1)^2}<0.
\end{aligned}
\]
Therefore \(\ell_-<\alpha\) and \(\beta<\ell_+\). From \(u<v\), \(\alpha=\beta+(q-1)(m-1)(u-v)<\beta\), while \(\gamma=\beta+(q-1)(v-u)>\beta\). This proves the asserted strict ordering and the lower bound.

**4. The exact maximum transition.** As \(\gamma>1>\ell_-\), the sign of \(\det(\gamma I-H)\) determines whether \(\gamma\) lies above or below \(\ell_+\). The exact identity is
\[
\det(\gamma I-H)=-\frac{mt(q-1)}{(t-q)^2(t-1)^2}
\bigl[(m-2q)t+mq(q-2)+2q\bigr].
\]
For \(m\ge2q\), the bracket is strictly positive. For \(m=2\), it equals \(-2q(q-1)^2<0\). For \(3\le m<2q\), put \(k=2q-m\ge1\). Then the bracket equals \(-kq^m+mq(q-2)+2q<0\), because \(q^m>mq(q-2)+2q\) holds for \(m\ge3\): at \(m=3\) it follows from \(q^2-3q+4>0\), and the inequality propagates by multiplying by \(q\). Thus \(\gamma>\ell_+\) exactly when \(m<2q\), and \(\ell_+>\gamma\) exactly when \(m\ge2q\), with no equality at integer parameters.

**5. Large-dimensional behavior.** For fixed \(q\), as \(m\to\infty\), the matrix \(H\) is \(I_2\) plus \(q^{-m}\) times a symmetric matrix whose leading terms in \(m\) are \(\bigl(\begin{smallmatrix}0&-m\sqrt{q-1}\\-m\sqrt{q-1}&-2m(q-1)\end{smallmatrix}\bigr)\). Hence
\[
\ell_\pm=1+\frac{m[-(q-1)\pm\sqrt{q(q-1)}]}{q^m}+O_q(q^{-m}),
\]
and the stated condition-number asymptotic follows because \(\ell_+\) is eventually maximal.

## Verification
Run `python3 verify.py` with Python 3.10 or later; it uses only the standard library. It independently enumerates all invertible matrices for \((q,m)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)\), constructs every distinct Gram entry via exact Fourier-zero counts, and checks all labeled eigenspaces and the two-dimensional block. It also checks determinant and crossover signs over a large **finite** parameter grid. The printed `VERIFY_OK` is computational corroboration, not a proof of the universally quantified theorem. The universal proof is Steps 1–5.

## Relationship to prior work
The rank-invariant Fourier transform of the indicator of \(\mathrm{GL}_m(\mathbb F_q)\), including the rank-one and rank-two coefficients used here, is known: see Li–Hu [1] and the earlier bilinear-forms association-scheme theory [2]. Kawamura [3], §4.2, gives more general rank-orbit Fourier matrices. Those results supply the character-sum inputs, not the stated compressed **single-entry coefficient Gram** eigenspaces, sharp Riesz bounds, strict \(m=2q\) crossover, or conditioning asymptotic. General harmonic-frame and ETF restrictions in Sustik–Tropp–Dhillon–Heath [4] concern a different global class and do not imply this non-ETF restricted family spectrum. These are statement-and-implication distinctions; independence from all unindexed historical formulations is not claimed.

## Limitations
No claim is made for higher-degree coordinate characters or full Fourier reconstruction on the matrix group. The all-dimension statement requires the algebraic proof, not the finite enumerations. The known rank-metric transform and elementary rook-graph diagonalization make historical equivalence of this precise compression a residual priority risk; an independent review has not occurred. The result determines Gram/Riesz stability on a specific natural restricted-character family, not optimally selected frequency sets.

## References
[1] Yan Li and Su Hu, *Gauss sums over some matrix groups*, arXiv:1105.4513v1 (public 2011-05-23), especially Theorem 2.1 and equations (2.14)–(2.16). https://arxiv.org/html/1105.4513v1

[2] Philippe Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, J. Combin. Theory Ser. A 25 (1978), 226–241, doi:10.1016/0097-3165(78)90015-8.

[3] Koei Kawamura, *\(q\)-Hypergeometric polynomials and group-invariant Fourier transformations over a finite field*, arXiv:2008.13408v1 (2020), especially §4.2. https://arxiv.org/html/2008.13408v1

[4] Mátyás A. Sustik, Joel A. Tropp, Inderjit S. Dhillon, and Robert W. Heath Jr., *On the existence of equiangular tight frames*, Linear Algebra Appl. 426 (2007), 619–635, doi:10.1016/j.laa.2007.05.043. https://www.cs.utexas.edu/users/inderjit/public_papers/equiangular.pdf
