# A one-matrix-scale mixing cutoff and an explicit chi-square window for nilpotent rank-one addition

## Finding
Fix a prime power \(q\ge 2\). For \(n\ge2\), put
\[
H_n=\mathfrak{sl}_n(\mathbb F_q)=\{A\in M_n(\mathbb F_q):\operatorname{tr}(A)=0\}.
\]
Let \(S_n\) be the set of **nonzero** rank-one square-zero matrices in \(H_n\). Starting at \(0\), form a discrete-time walk \(X_{n,t}\) by adding \(t\) independent uniformly sampled elements of \(S_n\). Write \(P_{n,t}\) for its distribution and \(U_n\) for uniform measure on \(H_n\). There are no holding steps.

**Theorem (sharp cutoff with an explicit chi-square profile).** For each fixed \(q\), the walk has a total-variation cutoff at time \(n\) in an \(O_q(1)\) window: if \(a_n\to\infty\) is integral with \(0\le a_n\le n\), then
\[
\|P_{n,n-a_n}-U_n\|_{\mathrm{TV}}\longrightarrow1,
\qquad
\|P_{n,n+a_n}-U_n\|_{\mathrm{TV}}\longrightarrow0.
\]
For every fixed integer \(s\), its **exact limiting chi-square window** is
\[
\boxed{\lim_{n\to\infty}\chi^2(P_{n,n+s}\Vert U_n)
=\Phi_q(s):=\sum_{c=1}^{\infty}
\frac{q^{-c^2-2cs}}{\prod_{j=1}^{c}(1-q^{-j})}.}
\]
The series is absolutely convergent for every integer \(s\). For example, \(\Phi_2(0)\) is approximately \(1.17266875\). In particular, the cutoff is not obtained by retaining only the largest nontrivial Fourier eigenvalue: every fixed eigen-codimension \(c\ge1\) contributes one term of the profile.

For completeness, the walk has the following finite-dimensional Fourier formula. Let \(B\in M_n(\mathbb F_q)\) represent a character of \(H_n\), where \(B\) and \(B+\alpha I\) are identified. Write
\[
d_\alpha(B)=\dim\ker(B-\alpha I),\quad
E(B)=\sum_{\alpha\in\mathbb F_q}\frac{q^{d_\alpha(B)}-1}{q-1},\quad
P_n=\frac{q^n-1}{q-1}.
\]
Then the normalized convolution multiplier and the exact chi-square divergence, for every integer \(t\ge0\), are
\[
\widehat\mu_n(B)=\frac{q^{n-1}E(B)-P_n}{(q^{n-1}-1)P_n},\qquad
\chi^2(P_{n,t}\Vert U_n)=\sum_{[B]\ne[0]}\widehat\mu_n(B)^{2t}.
\]
Here \([0]\) denotes the scalar-matrix character class. The eigenline multiplier itself is a known spectral ingredient; the contribution of the theorem is the exact infinite-dimensional critical-window sum and the matching sharp total-variation transition.

## Assumptions and scope
The field order \(q\) is fixed while the matrix size \(n\) tends to infinity; it may be an arbitrary prime power, including characteristic two. The total-variation statement allows any integral sequence \(a_n\to\infty\) satisfying the displayed range. The chi-square statement is at each fixed integral offset \(s\), with \(n+s\ge0\) automatically for all sufficiently large \(n\). The walk is an additive, **abelian** walk on \(H_n\), not a random product in a matrix group. For isolated small dimensions the non-lazy chain can be periodic (notably \(q=2,n=2\)); this does not affect the large-\(n\) claims.

For \(n\ge2\), each step has rank one and trace zero. The number of possible steps is
\[
|S_n|=(q^{n-1}-1)P_n.
\]
The sum of these steps spans \(H_n\) as an additive group, since all elementary off-diagonal matrices lie in \(S_n\) and each diagonal difference is an additive combination of such elements and a rank-one square-zero element. The invariant distribution is therefore uniquely uniform.

## Proof
**1. Character formula.** Every step has a representation \(vu^{\mathsf T}\) with \(v\ne0\), \(u\ne0\), and \(u^{\mathsf T}v=0\), with exactly \(q-1\) representations per step. For any nontrivial additive character \(\psi\) of \(\mathbb F_q\), the additive characters of \(H_n\) are \(\chi_B(A)=\psi(\operatorname{tr}(BA))\), where the label \(B\) is taken modulo scalar matrices. Summing \(\psi(u^{\mathsf T}Bv)\) first over \(u\in v^\perp\) gives \(q^{n-1}\) if \(Bv\in\mathbb F_qv\), and zero otherwise. Subtract \(u=0\), then sum over \(v\ne0\), and divide by \(q-1\). Exactly \((q-1)E(B)\) nonzero vectors span rational eigenlines of \(B\), yielding the stated multiplier. Fourier Plancherel on \(H_n\) gives the stated exact chi-square identity. The multiplicative symmetry \(S_n=-S_n\) ensures real multipliers.

**2. Large rational eigenspaces: exact class count.** For an integer \(c\ge1\) with \(n>2c\), the number of nonprincipal character classes whose largest rational eigenspace has dimension exactly \(n-c\) is
\[
N_{n,c}=\begin{bmatrix}n\\c\end{bmatrix}_q
\prod_{j=0}^{c-1}(q^n-q^j).
\]
Indeed, the eigenspace \(W\) of dimension \(n-c>n/2\) and its eigenvalue are unique. Subtract that eigenvalue times \(I\) to choose a unique representative of its scalar class with kernel exactly \(W\). Such representatives are in bijection with injective maps \(\mathbb F_q^n/W\hookrightarrow\mathbb F_q^n\), of which there are \(\prod_{j=0}^{c-1}(q^n-q^j)\). There are \(\begin{bmatrix}n\\c\end{bmatrix}_q\) possible \(W\). This is an exact bijection, not a heuristic about typical matrices.

For fixed \(c\), every matrix in this class has one eigenspace of dimension \(n-c\), and all other rational eigenspaces have total dimension at most \(c\). Uniformly over the class,
\[
E(B)=\frac{q^{n-c}-1+O_q(q^c)}{q-1},\qquad
\widehat\mu_n(B)=q^{-c}\bigl(1+O_q(q^{2c-n}+q^{c+1-n})\bigr).
\]
Moreover, elementary product expansions of the Gaussian binomial coefficient and the injection count give
\[
N_{n,c}=\frac{q^{2nc-c^2}}{\prod_{j=1}^c(1-q^{-j})}\,(1+o_{q,c}(1)).
\]
It follows that the contribution of these classes to the chi-square sum at \(t=n+s\), for each fixed \(c,s\), tends precisely to
\[
\frac{q^{-c^2-2cs}}{\prod_{j=1}^{c}(1-q^{-j})}.
\]

**3. Uniform control of the remaining characters.** Let \(r\) be the largest dimension of a rational eigenspace of a nonscalar \(B\), and write \(c=n-r\). A union bound over all \(r\)-subspaces on which \(B\) acts as one scalar shows that the number of scalar-matrix classes with this \(r\) is at most
\[
\begin{bmatrix}n\\r\end{bmatrix}_q q^{n(n-r)}
\le C_q q^{n^2-r^2}=C_q q^{2nc-c^2},
\]
where \(C_q=\prod_{j\ge1}(1-q^{-j})^{-1}\) is finite. Put \(L(B)=E(B)/P_n\). If \(c\le n/3\), the uniquely largest eigenspace has dimension at least \(2n/3\), and all other eigenspaces together occupy dimension at most \(c\). Consequently,
\[
L(B)\le q^{-c}\frac{1+(q-1)q^{2c-n}}{1-q^{-n}}
=q^{-c}(1+O_q(q^{-n/3})).
\]
In every regime with a rational eigenspace, one has the coarser bound
\[
L(B)\le\frac{q^{1-c}}{1-q^{-n}}\le2q^{1-c}.
\]
The multiplier can be written \(\widehat\mu_n(B)=(L(B)-p_n)/(1-p_n)\), where \(p_n=q^{-(n-1)}\). For sufficiently large \(n\),
\[
|\widehat\mu_n(B)|\le \max\{L(B),2q^{1-n}\}.
\]
The characters without a rational eigenvalue satisfy \(L(B)=0\), so their whole contribution at \(t=n+s\) is bounded by \(q^{n^2-1}(2q^{1-n})^{2(n+s)}\), which tends to zero. For \(c\le n/3\), the preceding bound and the class count dominate the summed contributions by
\[
(1+o(1))C_q\sum_{1\le c\le n/3}q^{-c^2-2cs}.
\]
For \(c>n/3\), the coarser bound gives \(O_q(nq^{-n^2/9+O_s(n)})\), which tends to zero. These estimates justify passing the limit through the Fourier sum. They prove the displayed chi-square profile for every fixed integer \(s\).

**4. The two total-variation sides.** Each nonzero step has rank one, so \(\operatorname{rank}(X_{n,t})\le t\). A uniform traceless matrix has rank at most \(n-a\) with probability at most \(C'_q q^{1-a^2}\): this follows by dividing the standard count \(\#\{A\in M_n(\mathbb F_q):\operatorname{rank}A\le n-a\}\le C'_q q^{n^2-a^2}\) by \(|H_n|=q^{n^2-1}\). Therefore
\[
\|P_{n,n-a}-U_n\|_{\mathrm{TV}}\ge1-C'_q q^{1-a^2},
\]
which proves the lower side whenever \(a\to\infty\). For the upper side, the character bounds in step 3, with \(t=n+b\) and \(b\ge0\), imply a bound asymptotic to a constant times \(\sum_{c\ge1}q^{-c^2-2bc}\), uniformly when \(b\to\infty\) and \(b\le n\). Hence chi-square tends to zero, and \(\|P-U\|_{\mathrm{TV}}\le\tfrac12\sqrt{\chi^2(P\Vert U)}\) completes the proof. For larger times the divergence is nonincreasing because every Fourier multiplier has absolute value at most one. This proves an \(O_q(1)\)-window cutoff.

## Verification
A standalone Python checker named `check.py` independently enumerates every generator and every additive character over \(\mathbb F_2\) in dimensions two and three and over \(\mathbb F_3,\mathbb F_4,\mathbb F_5\) in dimension two. It verifies the Fourier multipliers by direct character sums, the multiplicity of the largest-eigenspace classes when applicable, and the exact Plancherel chi-square identity against independent integer convolution counts for the first three steps. Field order four is implemented using its genuine degree-two extension arithmetic. Run `python3 check.py` using Python 3 and no external dependencies. The expected terminal result is `NILPOTENT_WALK_EXACT_CHECKS_PASS`.

These finite calculations do not certify the all-dimension class counts, the limiting series, or the cutoff: those follow from the algebraic proof above. The numerical value of \(\Phi_2(0)\) is a displayed approximation, not a separate certification.

## Relationship to prior work
Peres and Sly (2011) analyze **multiplicative** upper-unitriangular matrix walks with adjacent row updates and mixing on the order of the square of the dimension, not the present additive uniform nilpotent-orbit walk. Fulman and Goldstein (2012 preprint; 2015 journal) give rank distributions for uniform matrices; their counting bounds support the rank-deficiency context but do not concern sums of constrained rank-one steps. Fulman and Stanton (2015) study fixed-vector distributions in classical **groups**, not the scalar-quotient frequencies of the present additive matrix space. A prior spectral calculation for this same rank-one-nilpotent Cayley graph supplies the eigenline multiplier and extremal adjacency eigenvalues. A separate finite-field Wishart-walk result proves an \(n\)-step cutoff and different characteristic-sensitive chi-square series for sums of symmetric matrices \(vv^{\mathsf T}\). It does not imply the present theorem: the present increments are nonzero traceless square-zero matrices \(vu^{\mathsf T}\) conditioned by \(u^{\mathsf T}v=0\), with Fourier characters indexed modulo scalars and controlled by rational eigenspace codimension rather than quadratic-form rank. Neither earlier result gives the present chi-square series or cutoff directly. The new statement is an asymptotic character multiplicity analysis and mixing theorem, not a claim that the existing eigenline formula is new.

## Limitations
The field size is fixed in the asymptotic. A simultaneous large-field limit is not analyzed. The exact **total-variation profile** within the bounded window is not computed; the result determines its cutoff location and window and supplies an exact **chi-square** profile. The very small periodic case \(n=2,q=2\) is not a counterexample to an asymptotic statement. The proof is a self-contained mathematical argument supported by finite checks, not independent validation. Literature comparisons are bounded; an earlier unindexed theorem for this exact walk or a sufficiently general walk-classification theorem may exist.

## References
1. Y. Peres and A. Sly, *Mixing of the upper triangular matrix walk*, arXiv:1105.4402, first submitted 2011-05-23, https://arxiv.org/abs/1105.4402.
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504, first submitted 2012-11-02; *Annals of Probability* 43 (2015), 1274–1314, https://arxiv.org/abs/1211.0504.
3. J. Fulman and D. Stanton, *On the distribution of the number of fixed vectors for the finite classical groups*, arXiv:1505.06383, first submitted 2015-05-23, https://arxiv.org/abs/1505.06383.
4. Earlier finite-dimensional Fourier calculation on rank-one-nilpotent matrix Cayley graphs, *Sharp Fourier extrema and a Ramanujan dichotomy for rank-one nilpotent matrix Cayley graphs* (prior mathematical note; publication status not asserted).
5. Earlier finite-field Wishart-walk mixing calculation, *Characteristic-sensitive chi-square profiles at the finite-field Wishart mixing cutoff* (prior mathematical note; publication status not asserted).
