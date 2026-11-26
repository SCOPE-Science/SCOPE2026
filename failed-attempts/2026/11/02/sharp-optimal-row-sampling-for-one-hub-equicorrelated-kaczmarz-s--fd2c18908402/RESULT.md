# Sharp optimal row sampling for one-hub equicorrelated Kaczmarz systems

## Finding

**Theorem (exact fixed-probability Kaczmarz design).** For each integer \(m\ge3\), suppose a square, nonsingular real row system \(A\in\mathbb R^{(m+1)\times(m+1)}\) has unit-norm rows \(u_0,u_1,\ldots,u_m\) with Gram matrix
\[
G=AA^{\mathsf T}=\begin{pmatrix}
1&a\mathbf1_m^{\mathsf T}\\
a\mathbf1_m&(1-b)I_m+b\mathbf1_m\mathbf1_m^{\mathsf T}
\end{pmatrix},
\qquad a>0,\quad -\frac1{m-1}<b<1,\quad ma^2<c:=1+(m-1)b.
\]
These conditions are precisely the stated strict positivity assumptions ensuring \(G\succ0\). For independently sampled row index \(i\) with fixed probabilities \(p_i\ge0\), \(\sum_{i=0}^mp_i=1\), let
\[
\rho(p)=\lambda_{\min}\!\left(A^{\mathsf T}\operatorname{diag}(p)A\right).
\]
Define
\[
t_0=\frac{c+ma}{1+a},\qquad
 t_1=\begin{cases}
\dfrac{b(1-b)}{b-a^2},&b>a^2,\\
+\infty,&b\le a^2,
\end{cases}
\qquad t_*=\min\{t_0,t_1\}.
\]
Then the **unique** maximizer on the entire \((m+1)\)-coordinate probability simplex is
\[
\boxed{p_0^*=\frac{t_*}{m+t_*},\qquad p_j^*=\frac1{m+t_*}\quad(1\le j\le m).}
\]
Its exact minimum-eigenvalue rate is
\[
\boxed{\rho_*=
\begin{cases}
\dfrac{c-ma^2}{m+c+2ma},&t_0\le t_1,\\[4pt]
\dfrac{1-b}{m+t_1},&t_1\le t_0.
\end{cases}}
\]
The two expressions agree when \(t_0=t_1\). If \(b>a^2\), the second branch is optimal precisely when
\[
\boxed{m(b-a^2)\ge a(1-b).}
\]
Consequently, for any fixed \(0<a^2<b<1\) and integer \(m\ge\max\{2,a(1-b)/(b-a^2)\}\), the optimal hub-to-individual-leaf sampling ratio is the dimension-independent \(t_1\). At the boundary \(b=a^2\), where \(0<a<1\), instead \(t_*=ma+1-a\) and \(p_0^*\to a/(1+a)>0\) as \(m\to\infty\). For fixed \(0<a^2<b<1\), \(p_0^*\to0\). Thus the large-dimension hub-probability behavior changes sharply across the coherence boundary.

## Assumptions and scope

The system \(Ax=y\) is consistent, has \(m+1\) independent rows, and uses exact row projections without relaxation. Each iteration chooses one row independently from the same fixed probability distribution. The matrix \(A\) denotes a row coefficient matrix, not a Gram matrix. The one-step Euclidean error obeys, for any error \(e\),
\[
\mathbb E[\|e^+\|_2^2\mid e]=\|e\|_2^2-e^{\mathsf T}A^{\mathsf T}\operatorname{diag}(p)Ae.
\]
Hence \(1-\rho(p)\) is the **sharp worst-direction conditional one-step expected squared-error contraction factor**. Nothing here asserts an optimal finite-horizon policy, asymptotic mean-square exponent, adaptive sampling law, or practical computation-time advantage.

## Proof

**1. Spectral reduction and existence of a symmetric optimum.** Any permutation of leaf rows preserves \(G\). Because \(A\) is invertible, this row permutation is realized by an orthogonal map on \(\mathbb R^{m+1}\): if \(P\) permutes leaves then \(PA=AU\) and \(U\) is orthogonal because \((AU)(AU)^{\mathsf T}=PAA^{\mathsf T}P^{\mathsf T}=AA^{\mathsf T}\). The function \(p\mapsto\rho(p)\) is concave as a smallest eigenvalue of a linear symmetric pencil. Average any sampling distribution over leaf permutations; the result has no smaller \(\rho\). Thus some global maximizer has common leaf probability \(q\), hub probability \(p\), and \(p+mq=1\).

For \(0<p<1\), the nonzero eigenvalues of \(A^{\mathsf T}\operatorname{diag}(p,q,\ldots,q)A\) equal those of \(\operatorname{diag}(\sqrt p,\sqrt q,\ldots,\sqrt q)G\operatorname{diag}(\sqrt p,\sqrt q,\ldots,\sqrt q)\). The leaf-difference eigenvalue is \(q(1-b)\), with multiplicity \(m-1\), and the two radial eigenvalues are those of
\[
M_2(p)=\begin{pmatrix}p&a\sqrt{mpq}\\a\sqrt{mpq}&cq\end{pmatrix}.
\]
Write \(\alpha=c/m\), \(\delta=\alpha-a^2>0\), \(q=(1-p)/m\), and let \(h(p)\) be the smaller eigenvalue of \(M_2(p)\). The objective is
\[
\rho(p)=\min\{h(p),(1-b)(1-p)/m\}.
\]
At simplex-boundary probabilities the Gram pencil is singular and its minimum eigenvalue is zero. The interior optimum is positive because \(G\succ0\).

**2. Exact radial optimum.** The characteristic polynomial of \(M_2(p)\) is
\[
F(p,\lambda)=\lambda^2-\lambda[\alpha+(1-\alpha)p]+\delta p(1-p).
\]
Set
\[
p_R=\frac{\alpha+a}{1+\alpha+2a},\qquad
\lambda_R=\frac{\delta}{1+\alpha+2a}.
\]
A direct expansion gives the *global algebraic certificate*
\[
\boxed{F(p,\lambda_R)=-\delta(p-p_R)^2.}
\]
At \(p=p_R\), \(\lambda_R\) is the smaller radial eigenvalue: it is a root and \(0<\lambda_R<p_R\), while the larger eigenvalue exceeds the first diagonal entry \(p_R\) because the off-diagonal entry is positive. For every \(p\ne p_R\) in \((0,1)\), the certificate makes \(F(p,\lambda_R)<0\), placing \(\lambda_R\) strictly between the two radial eigenvalues; hence \(h(p)<\lambda_R\). Therefore \(h\) has unique maximizer \(p_R\), and its corresponding hub-to-leaf ratio is \(p_R/q_R=(c+ma)/(1+a)=t_0\). Moreover \(h(p)\) is concave (the two-dimensional radial covariance is a linear Hermitian pencil in a fixed orthonormal basis), and strictly increases until \(p_R\).

**3. Competition with the leaf-difference eigenvalue.** Put \(t=p/q=mp/(1-p)\), so that \(q=1/(m+t)\). Divide the two radial eigenvalues by \(q\); they are eigenvalues of
\[
N(t)=\begin{pmatrix}t&a\sqrt{mt}\\a\sqrt{mt}&c\end{pmatrix}.
\]
At the leaf-difference level \(1-b\), the radial characteristic polynomial evaluates exactly to
\[
\boxed{\det(N(t)-(1-b)I)=m[t(b-a^2)-b(1-b)].}
\]
If \(b\le0\), the smaller eigenvalue of \(N(t)\) is at most \(c\le1-b\), so the radial eigenvalue always limits \(\rho\). If \(0<b\le a^2\), then \(c>1-b\), and the displayed determinant is strictly negative for all \(t>0\), so again the smaller radial eigenvalue is below \(1-b\). If \(b>a^2\), the larger radial eigenvalue exceeds \(c>1-b\), and the determinant changes sign exactly at \(t_1=b(1-b)/(b-a^2)\): below \(t_1\), the radial eigenvalue is limiting, and above it the decreasing leaf-difference eigenvalue is limiting. Since \(h\) increases up to its unique maximizer \(t_0\), this proves that the unique symmetric optimum is at \(t_* =\min\{t_0,t_1\}\), with the claimed exact optimal values. The factorization
\[
(c+ma)(b-a^2)-b(1-b)(1+a)=(a+b)[m(b-a^2)-a(1-b)]
\]
proves the sharp threshold for \(b>a^2\).

**4. Unrestricted uniqueness, not just symmetric uniqueness.** Suppose an arbitrary probability vector \(w\) is globally optimal. Averaging its leaf-permutation orbit gives a symmetric optimum without reducing the objective. The symmetric optimum is unique by steps 2–3; therefore \(w_0=p_0^*\). Let \(v\) be a unit radial eigenvector at the symmetric optimum, with eigenvalue \(\rho_*\). Such a vector exists in both branches: at a leaf/radial crossing it is the smaller radial eigenvector, and otherwise it is the unique smallest radial eigenvector. By invariance, \(u_1^{\mathsf T}v=\cdots=u_m^{\mathsf T}v\), so
\[
v^{\mathsf T}A^{\mathsf T}\operatorname{diag}(w)Av
=w_0(u_0^{\mathsf T}v)^2+(1-w_0)(u_1^{\mathsf T}v)^2=\rho_*.
\]
As \(\lambda_{\min}(A^{\mathsf T}\operatorname{diag}(w)A)=\rho_*\), equality in the Rayleigh bound implies \(v\) is also an eigenvector for \(w\). Subtracting the two eigenvalue equations yields
\[
A^{\mathsf T}\operatorname{diag}(w-p^*)Av=0.
\]
Both types of row response are nonzero. Indeed, if \(u_0^{\mathsf T}v=0\), the eigenvalue equation at the symmetric probabilities and its inner product with \(u_0\) force the common leaf response to vanish because \(a>0\), contradicting \(\rho_*>0\); the reverse argument applies if the leaf response vanishes. Since \(A\) is invertible and every coordinate of \(Av\) is nonzero, the last displayed equation implies \(w=p^*\). This proves global uniqueness with completely independent edge/row probabilities.

**5. Dimension threshold and boundary.** For fixed \(a^2<b\), the switch criterion gives \(m\ge a(1-b)/(b-a^2)\) and thereafter \(t_*\) is the fixed value \(t_1\). If \(b=a^2\), then \(c=1+(m-1)a^2\), \(t_*=t_0=ma+1-a\), and the stated nonzero hub-probability limit follows directly. For example, with \(a=3/10\) and \(b=1/10\), the exact transition is at \(m=27\); for all \(m\ge27\), \(t_*=9\).

## Verification

The accompanying standalone Python file `artifacts/verify_kaczmarz.py` checks the square-completion identity, both crossing and switch factorizations symbolically; reconstructs the full Gram spectrum for admissible parameters with leaf coherences of either sign; checks arbitrary independent probability perturbations; and checks an exact rational phase-boundary instance. The script records its actual count and output when executed. Numerical sampling is supplementary; the proof above is analytical and covers all permitted real parameters and all integers \(m\ge3\).

## Relationship to prior work

Dai, Soltanalian and Pelckmans (2014) give the exact one-step randomized Kaczmarz smallest-eigenvalue criterion and its general SDP (Theorem 2, equations (13)–(16)); the present theorem explicitly solves that program for a nontrivial all-dimensional Gram family. Gower and Richtárik (2015) place randomized Kaczmarz and related methods in a general sketch-and-project framework without the particular algebraic allocation threshold. Pukelsheim and Torsney (1991) characterize saturated experimental-design optimal weights via an implicit nonlinear matrix condition; their closed expression on pp. 1616–1620 is for A-optimality, not this explicit E-optimal family. In equivalent E-design language, the current claim is the exact all-parameter optimal-weight formula and its unrestricted uniqueness and phase boundary, not the earlier general equivalence principle.

A separate published result on optimal sampling under the condition \(G^{-1}\ge0\) entrywise does not apply: in this setting \((G^{-1})_{0j}=-a/(c-ma^2)<0\) for every leaf. A previous generic three-row solution already covers the case of two leaves, which is excluded from the present novelty claim; earlier special four-row patterns and two-nonsingleton-community designs do not state the current arbitrary-\(m\ge3\) one-hub formula. These comparisons do not rule out an equivalent unindexed earlier specialization.

## Limitations

The case of two leaves is omitted because it is covered by an earlier fully general three-row result. This is a one-step worst-direction expected **squared-error** guarantee for fixed iid row sampling, not an optimal mean error over every starting vector, an asymptotic rate equality for all initial errors, a nonstationary control policy, or an empirical performance benchmark. The rows must be normalized, independent, and have the specified Gram structure with positive hub correlation; when \(a=0\), uniqueness can change and is excluded. The theorem gives the exact optimum but not a general computationally cheaper routine for arbitrary inputs. The broader literature of E-optimal design and diagonal matrix scaling leaves a residual risk of an earlier equivalent formulation; the checked sources do not directly give the threshold.

## References

1. L. Dai, M. Soltanalian and K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863v1, first public 12 February 2014, https://arxiv.org/abs/1402.2863.
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296v1, first public 10 June 2015, https://arxiv.org/abs/1506.03296; SIAM J. Matrix Anal. Appl. 36 (2015), 1660–1690.
3. F. Pukelsheim and B. Torsney, *Optimal weights for experimental designs on linearly independent support points*, Ann. Statist. 19 (1991), 1614–1625, https://doi.org/10.1214/aos/1176348265; lawful manuscript https://www.math.uni-augsburg.de/htdocs/emeriti/pukelsheim/1991d.pdf.
4. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics* (2026), public mathematical result, https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995.
