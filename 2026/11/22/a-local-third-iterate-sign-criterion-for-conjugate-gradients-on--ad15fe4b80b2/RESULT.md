# A local third-iterate sign criterion for conjugate gradients on weighted trees

## Finding
Let \(T=(V,E,w)\) be any finite connected tree with strictly positive edge weights, let \(\mu>0\), let \(A=\mu I+L_w\), and start exact-arithmetic, unpreconditioned conjugate gradients for \(Ax=e_r\) from \(x^{(0)}=0\). Its first two defined iterates are entrywise nonnegative. When the third Lanczos vector exists, the complete sign of the third iterate is decided by one local inequality for each neighbor of \(r\), explicitly described below. The root and all vertices at distance two have strictly positive third-iterate coordinates; vertices at greater distance have zero coordinates.

For the five-vertex weighted tree with edges \((0,1),(0,2),(0,4),(2,3)\), respective conductances \(5,1,t,2t\), shift \(\mu=1\), and source \(r=0\), the exact third iterate is entrywise nonnegative if and only if \(0<t\le t_*\), where \(t_*\in(28,29)\) is the **unique positive zero** of
\[
P(t)=6t^5-193t^4+732t^3-1715t^2+1200t-1200.
\]
For every \(t>t_*\), exactly one coordinate is negative, namely the coordinate at vertex \(2\). In particular at \(t=30\) this coordinate is \(-77253/484548896\), despite \(A^{-1}e_0\) being strictly positive everywhere.

## Assumptions and scope
Weighted Laplacians use \((L_w)_{ii}=\sum_{j\sim i}w_{ij}\) and \((L_w)_{ij}=-w_{ij}\) for edges. The graph is finite, simple, connected and a tree; \(w_{ij}>0\) and \(\mu>0\) are arbitrary real numbers. Exact arithmetic and the conventional unpreconditioned CG iterates are meant. Let \(N(r)\) denote the neighbors, \(a_i=A_{ii}\), \(w_i=w_{ri}\), and \(S=\sum_{i\in N(r)}w_i^2>0\). Set
\[
\alpha_1=\frac{\sum_{i\in N(r)}w_i^2a_i}{S},
\qquad
v_i=\begin{cases}
-w_i(a_i-\alpha_1),&i\in N(r),\\
w_{ri}w_{ij},&\operatorname{dist}(r,j)=2\text{ and }i\text{ is the unique parent of }j,\\
0,&\text{otherwise}.
\end{cases}
\]
For the second line, \(v_j=w_{ri}w_{ij}\). If \(v=0\), the initial Krylov grade is at most two and CG already yields the exact positive solution by its second iterate. Otherwise put
\[
\alpha_2=\frac{v^{\mathsf T}Av}{v^{\mathsf T}v},\qquad
\Delta=\det\begin{pmatrix}
a_r&\sqrt S&0\\
\sqrt S&\alpha_1&\|v\|/\sqrt S\\
0&\|v\|/\sqrt S&\alpha_2
\end{pmatrix}>0.
\]
The matrix displayed is the sign-adjusted three-step Lanczos matrix; its determinant is positive because it is a compression of the positive-definite \(A\).

## Proof
With \(q_0=e_r\), choose the first Lanczos vector \(q_1=-\sum_{i\in N(r)}w_i e_i/\sqrt S\). Its diagonal Rayleigh quotient is \(\alpha_1\). On a tree, the next unnormalized Lanczos residual equals \(v/\sqrt S\). Thus its normalized direction has diagonal quotient \(\alpha_2\) and the projected tridiagonal matrix is the one defining \(\Delta\).

Let \(\theta_1,\theta_2,\theta_3>0\) be its eigenvalues. CG Galerkin orthogonality gives a residual polynomial \(\prod_{j=1}^3(1-\lambda/\theta_j)\); hence the third iterate is \(p_2(A)e_r\), where
\[
p_2(\lambda)=\frac{\theta_1\theta_2+\theta_1\theta_3+\theta_2\theta_3-(\theta_1+\theta_2+\theta_3)\lambda+\lambda^2}{\Delta}.
\]
The trace of the projected matrix is \(a_r+\alpha_1+\alpha_2\). For each neighbor \(i\), the tree identities \(A_{ir}=-w_i\) and \((A^2)_{ir}=-w_i(a_r+a_i)\) therefore yield the **exact local sign law**
\[
\boxed{\quad x_i^{(3)}=\frac{w_i(\alpha_1+\alpha_2-a_i)}{\Delta},\quad i\in N(r).\quad}
\]
For each vertex \(j\) at distance two, with parent \(i\), \((A^2)_{jr}=w_{ri}w_{ij}>0\), so \(x_j^{(3)}=w_{ri}w_{ij}/\Delta>0\). At distance three or more all first three Krylov vectors vanish. The root coordinate is \((T_3^{-1})_{11}>0\). Hence \(x^{(3)}\) is entrywise nonnegative **if and only if** \(\alpha_1+\alpha_2\ge a_i\) for every neighbor \(i\) of \(r\). The analogous two-step polynomial has positive neighbor coordinates \(w_i/\det T_2\) and a positive root coordinate, proving the stated first-two-step assertion. A degree-one root satisfies \(\alpha_1=a_i\), making its third-step neighbor coordinate strictly positive whenever that step exists.

In the stated five-vertex family, direct substitution into the local law and the projected determinant yields
\[
x_2^{(3)}=-\frac{P(t)}{Q(t)},\qquad
Q(t)=72t^6-165t^5-348t^4+9849t^3-8630t^2+3600t+5600.
\]
Here \(Q(t)>0\) for all \(t>0\): the derivation gives \(Q(t)=\Delta(t)D(t)\), where \(D(t)=15t^4-124t^3+415t^2-200t+200\) is the strictly positive scaled squared second Lanczos residual. The other two neighbor coordinates are
\[
 x_1^{(3)}=\frac{5(24t^5-115t^4+594t^3-345t^2+400)}{Q(t)},
\quad
 x_4^{(3)}=\frac{t(9t^5+84t^4-441t^3+1930t^2-1200t+1400)}{Q(t)}.
\]
Exact Sturm-chain sign-variation counts at \(0^+\) and \(+\infty\) are, respectively, \((3,2)\) for \(P\), and \((2,2)\) for each of the two positive numerator polynomials (zero values in a chain omitted). Therefore \(P\) has exactly one positive zero and neither of the latter two polynomials has any. Since \(P(28)<0<P(29)\), the unique root is in \((28,29)\); the two other neighbors stay strictly positive. The root and the distance-two vertex are strictly positive by the general result. This completes the if-and-only-if phase classification. Finally, \(A\) is an irreducible nonsingular symmetric \(M\)-matrix, so \(A^{-1}e_0>0\).

## Verification
Run `python verify.py` using Python 3 and SymPy (tested with the available version). It independently evaluates exact rational CG recurrences at nine positive parameter values, checks each symbolic broom coordinate formula, verifies the three Sturm zero counts, and checks the general local identity on five weighted rooted-tree examples. These finite checks support but do not replace the analytic tree-wide proof. The positivity of \(\Delta\) and \(D\) follows from nonzero Lanczos norms and positive definiteness, not a numerical sampling claim.

## Relationship to prior work
Conjugate gradients, Lanczos tridiagonalization and their energy-error guarantees are classical; see Axelsson (2010), Sections 2--3, and Livne--Brandt (2011), Sections 1--2, for graph-Laplacian solver motivation. An existing research note titled *Three dimensions are minimal for positivity loss in conjugate gradients on Stieltjes systems* establishes the occurrence of sign failure for an **arbitrary nonnegative right-hand side**, but that statement does not imply this point-source-specific exact local criterion, nor the explicit five-vertex one-parameter transition. Another prior note on discrete Poisson paths studies mixed positive sources at the second CG iterate, not a single coordinate source. Neither ordinary CG energy monotonicity nor inverse-positivity implies sign preservation of intermediate iterates.

## Limitations
No claim is made that five vertices is the globally smallest tree size for a point-source third-iterate failure; no classification of all tree families, of higher CG iterates, of round-off behavior, or of preconditioned CG is asserted. The explicit transition is for the specified one-parameter weighted broom, while the local criterion applies to any finite positively weighted tree with positive shift. Literature priority is qualified by incomplete full-text access to some related prior notes; the inspected literature does not establish an independent priority certification.

## References
1. O. Axelsson, *Milestones in the Development of Iterative Solution Methods*, Journal of Electrical and Computer Engineering (2010), https://doi.org/10.1155/2010/972794 (online December 9, 2010).
2. O. E. Livne and A. Brandt, *Lean Algebraic Multigrid (LAMG): Fast Graph Laplacian Linear Solver*, arXiv:1108.0123 (initial public version July 31, 2011), https://arxiv.org/abs/1108.0123.
3. *Three dimensions are minimal for positivity loss in conjugate gradients on Stieltjes systems*, publicly indexed research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-three-dimensions-are-minimal-for-positivity-loss-in-conjugate-gr--a3e3bd9186a5 (summary consulted; full record unavailable).
4. *A parity law for the second conjugate-gradient iterate on discrete Poisson paths*, publicly indexed research note, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-a-parity-law-for-the-second-conjugate-gradient-iterate-on-discre--43379a17501b (summary consulted; full record unavailable).
