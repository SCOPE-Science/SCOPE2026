# Sharp discrete-Sobolev sensitivity of bounded-slope isotonic projection

## Finding
For each integer \(n\ge 2\) and each vector of caps \(\boldsymbol{b}=(b_1,\ldots,b_{n-1})\), where every \(b_i\in(0,\infty]\), consider Euclidean least-squares projection \(P_{\boldsymbol b}:\mathbb R^n\to C_{\boldsymbol b}\) onto
\[
C_{\boldsymbol b}=\{y\in\mathbb R^n:0\le y_{i+1}-y_i\le b_i\quad(1\le i<n)\}.
\]
The upper inequality is absent if its cap is infinite. Equip real signals modulo constants with the discrete first-difference Sobolev seminorm
\[
H_n(h)=\left(\sum_{i=1}^{n-1}(h_{i+1}-h_i)^2\right)^{1/2}.
\]
Then the **sharp attained two-input coefficient** for every permitted cap vector is independent of the caps and equals
\[
\operatorname{Lip}_{H_n}(P_{\boldsymbol b})
:=\sup_{H_n(x-z)>0}\frac{H_n(P_{\boldsymbol b}x-P_{\boldsymbol b}z)}{H_n(x-z)}
=\begin{cases}
1,&n=2,\\
\sqrt{5}/2,&n=3,\\
\sqrt{14}/3,&n=4,\\
\sqrt{(n-1)/2},&n\ge5.
\end{cases}
\]
Each value is realized by an input pair arbitrarily close to one another, with strictly complementary active constraints. In particular, bounded-slope isotonic least squares is contractive in its fitting \(\ell_2\) metric but can amplify **differences of slopes** at rate \(\sqrt{n/2}\), independently of the strength or spatial variation of the positive slope caps.

## Assumptions and scope
The objective is \(\frac12\sum_{i=1}^{n}(y_i-x_i)^2\), with equal positive observation masses, on an ordered chain of \(n\) vertices. The constraints are increasing and locally capped, with each cap **strictly positive** and possibly infinite. All signals and coefficients are real. The denominator is the first-difference seminorm of the **difference of two inputs**; this is not the one-input energy of the fitted signal or the ordinary Euclidean norm. Because \(P_{\boldsymbol b}(x+c\mathbf 1)=P_{\boldsymbol b}x+c\mathbf1\), a constant input perturbation induces a constant output perturbation, so the quotient is well defined on constants modulo \(\mathbf1\).

## Proof
**1. Active-face linearization.** Let \(P=P_{\boldsymbol b}\). The projection onto a polyhedron is a continuous piecewise-affine map. On any full-dimensional affine cell, declare an edge active when the fitted increment equals either zero or a finite upper cap. Connected runs of active edges give consecutive vertex blocks \(I_1,\ldots,I_m\). On such a block, all fitted coordinate differences are prescribed by the active equalities, so the fitted coordinates have the form \(y_i=c_j+d_i\), where the offsets \(d_i\) are fixed on that cell. Minimizing the Euclidean objective over the free block shift gives
\[
c_j=\frac1{|I_j|}\sum_{i\in I_j}(x_i-d_i).
\]
Consequently the derivative of \(P\) on this cell is exactly the linear map \(B\) which averages the input separately over each consecutive block. This includes upper-slope active constraints: their offsets do not affect the derivative. At boundaries between cells, continuity and subdivision of a line segment give the global Lipschitz upper bound from the maximum of these finitely many block-averaging derivative norms.

Conversely, **every** consecutive-block partition can occur as a strictly complementary local derivative for any cap vector under consideration. Choose a feasible fitted vector \(y\) with zero increments inside each proposed block and strictly intermediate increments across blocks, e.g. half the cap for finite caps or a positive fixed value for an infinite cap. For every within-block active edge \(i\), choose a strictly positive multiplier \(\lambda_i\) for the inequality \(y_i-y_{i+1}\le0\), and set
\[
x=y+\sum_{i\text{ within a block}}\lambda_i(e_i-e_{i+1}).
\]
The KKT stationarity condition, feasibility and complementary slackness make \(P(x)=y\); the active inequalities are linearly independent and have strictly positive multipliers, with all inactive inequalities slack. Hence in a neighborhood of \(x\) the derivative is the specified block-averaging map. The global sharp seminorm is therefore exactly the maximum of the \(H_n\)-operator norms of *all* consecutive-block averaging matrices.

**2. Gradients of consecutive-block means.** Write \(q_i=h_{i+1}-h_i\), \(1\le i<n\). Let the blocks have lengths \(\ell_1,\ldots,\ell_m\). For a block-averaging matrix \(B\), the gradient \(D(Bh)\) vanishes on edges internal to blocks and on the \(m-1\) interblock edges equals the difference of two neighboring block means. Thus the nonzero part of \(D B h\) is \(Aq\), for an \((m-1)\)-by-\((n-1)\) matrix \(A\) with **nonnegative** entries. On the row between adjacent blocks of lengths \(a,b\), the weights on the original gradient are, in order,
\[
\frac1a,\frac2a,\ldots,\frac{a-1}{a},\quad 1,\quad
\frac{b-1}{b},\ldots,\frac1b,
\]
with zeros outside those blocks. The row sum is \((a+b)/2\). Each input gradient edge belongs either to a block boundary (where its one coefficient is \(1\)), to an interior block (where its coefficients in the two neighboring rows add to \(1\)), or to an endpoint block (where the single coefficient is at most \(1\)). Therefore
\[
\|A\|_1=1\quad(m\ge2),\qquad
\|A\|_\infty=\max_{1\le j<m}\frac{\ell_j+\ell_{j+1}}2.
\]
Here the matrix norms on the right are the maximum column and row sums. For \(m\ge3\), every neighboring pair excludes at least one vertex, so
\[
\|A\|_{2\to2}^2\le\|A\|_1\|A\|_\infty\le\frac{n-1}{2}.
\]
For \(m=1\), the gradient output is zero. For \(m=n\), the map is the identity, as is also covered by the preceding bound for \(n\ge3\).

**3. Two blocks and the small-dimensional exceptions.** For exactly two blocks of lengths \(a,b\ge1\) with \(a+b=n\), the matrix \(A\) has one nonzero row, and direct summation of its squared entries gives
\[
\|A\|_{2\to2}^2=1+\sum_{j=1}^{a-1}\left(\frac ja\right)^2+\sum_{j=1}^{b-1}\left(\frac jb\right)^2
=\frac n3+\frac16\left(\frac1a+\frac1b\right).
\]
At fixed \(n\), the maximum occurs for \(\{a,b\}=\{1,n-1\}\), giving \(n/3+n/[6(n-1)]\). It equals \(1,5/4,14/9\) at \(n=2,3,4\), respectively. For every integer \(n\ge5\), the inequality
\[
\frac n3+\frac{n}{6(n-1)}\le\frac{n-1}2
\]
is equivalent to \(n^2-5n+3\ge0\) and is valid. At \(n=3\), a partition into three singleton blocks has norm one; at \(n=4\), any partition into at least three blocks has squared norm at most \(3/2<14/9\). This proves the stated upper bound in every dimension.

**4. Sharp witnesses.** At \(n=2\), the singleton partition is the identity. At \(n=3,4\), use the two-block partition \(I_1=\{1\}\), \(I_2=\{2,\ldots,n\}\) and choose the input perturbation \(h\) with successive increments equal to the displayed single row of \(A\). The ratio squared is exactly its row squared norm, \(5/4\) or \(14/9\).

For all \(n\ge5\), use three blocks of lengths \(1,n-2,1\) and choose the perturbation \(h_i=i-1\). Its input increments are all one. Each of its two output jumps after block averaging is \((n-1)/2\), so
\[
\frac{H_n(Bh)^2}{H_n(h)^2}
=\frac{2((n-1)/2)^2}{n-1}=\frac{n-1}{2}.
\]
The strictly complementary construction in step 1 realizes these derivative actions as \(P(x+\varepsilon h)-P(x)=\varepsilon Bh\) for all sufficiently small \(\varepsilon>0\), with any positive cap vector. Therefore all of the coefficients are genuinely attained by arbitrarily close **two-input** pairs. \(\square\)

## Verification
The standalone standard-library Python program `verify.py` checks every consecutive-block partition in dimensions \(2\) through \(10\) using exact rational arithmetic; the row/column inequalities, the special two-block sum-of-squares identities, and equality witnesses are checked independently of floating-point eigensolvers. It additionally solves two hundred small bounded-slope projection pairs by exact KKT active-set enumeration, checking four hundred individual quadratic programs and the claimed two-input bounds. A separate exact KKT test constructs strictly complementary sharp input pairs for every \(2\le n\le34\). Run `python verify.py` from the directory containing the extracted file. Finite checks corroborate, but do not prove, the unrestricted statements; those follow from the algebraic argument above.

## Relationship to prior work
Yeganova and Wilbur (2009) develop bounded-slope isotonic regression and its LPAV algorithm. Agarwal, Phillips, and Sadri (2009) investigate Lipschitz isotonic regression on paths and trees using squared-error fitting. Their primary contributions concern algorithms, feasible geometries and computational complexity, rather than the sharp two-input discrete-gradient seminorm considered here. Yang and Barber (2017) characterize seminorms for which ordinary isotonic regression is contractive, using neighbor averaging; the first-difference quadratic seminorm here is generally **not** one of the contractive seminorms. Their criterion does not provide these sharp superunit amplification factors or their cap independence. The statement and proof here quantify a distinct stability question, and include spatially varying finite or infinite upper slope caps.

## Limitations
Equal observation masses and a chain order are essential to the stated formula and proof. Positive upper caps are necessary for the proposed unconstrained-face realization; a zero cap can force a completely different derivative family. No result is claimed for weighted least squares, general trees, periodic chain constraints, different gradient \(\ell_p\) metrics, or statistical estimation risk. A search and material inspection of relevant literature do not establish absolute historical priority; unindexed equivalents remain possible. Independent external validation has not been performed.

## References
1. L. Yeganova and W. J. Wilbur, *Isotonic Regression under Lipschitz Constraint*, Journal of Optimization Theory and Applications 141 (2009), 429–443, first online 2009-01-07, DOI: 10.1007/s10957-008-9477-0. Open primary text: https://link.springer.com/content/pdf/10.1007/s10957-008-9477-0.pdf .
2. P. K. Agarwal, J. M. Phillips, and B. Sadri, *Lipschitz Unimodal and Isotonic Regression on Paths and Trees*, preprint first submitted 2009-12-28, arXiv:0912.5182, https://arxiv.org/abs/0912.5182 .
3. F. Yang and R. Foygel Barber, *Contraction and uniform convergence of isotonic regression*, preprint first submitted 2017-06-06, arXiv:1706.01852, https://arxiv.org/abs/1706.01852 .
