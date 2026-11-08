# A sharp volume-versus-uniform reversal for two-coordinate sampling on SPD stars

## Finding

For an arbitrary real symmetric positive-definite matrix \(H\) of order \(n\ge2\), consider exact quadratic block minimization over all but one coordinate. Let \(q_j\) be the fixed probability that coordinate \(j\) is **omitted**. Define \(K=H^{-1}\) and the normalized inverse-Hessian Gram matrix
\[
G_{ij}=\frac{K_{ij}}{\sqrt{K_{ii}K_{jj}}}.
\]
The sharp conditional one-step expected squared-energy retention factor is exactly
\[
\Lambda(q)=\lambda_{\max}(Q^{1/2}GQ^{1/2}),\qquad Q=\operatorname{diag}(q).
\]
Suppose a diagonal sign matrix \(D\) makes \(\widetilde G=DGD\) entrywise nonnegative and \(r=\widetilde G^{-1}{\bf1}\) strictly positive. Then the **unique** probability vector minimizing the sharp factor is
\[
\boxed{q_j^*=\frac{r_j}{\sum_i r_i},\qquad \min_q\Lambda(q)=\frac1{\sum_i r_i}.}
\]
In particular, for the three-variable star
\[
H_c=\begin{pmatrix}1&c&c\\c&1&0\\c&0&1\end{pmatrix},\quad 0<c<1/\sqrt2,\quad s=\frac c{\sqrt{1-c^2}},
\]
the optimum, uniform omission, and determinant-proportional (volume) sampling of updated pairs satisfy the strict comparison
\[
\Lambda(q^*)<\Lambda(q^{\rm unif})<\Lambda(q^{\rm vol})\qquad (0<s<1).
\]
Their probabilities and exact optimal/volume factors are
\[
\begin{aligned}
q^*&=\frac1{3-s}(1-s,1,1),
&\Lambda(q^*)&=\frac{1+s}{3-s},\\
q^{\rm vol}&=\frac1{3+s^2}(1+s^2,1,1),
&\Lambda(q^{\rm vol})&=\frac{1+s^2+\sqrt2\,s\sqrt{1+s^2}}{3+s^2},\\
q^{\rm unif}&=\frac13(1,1,1),
&\Lambda(q^{\rm unif})&=\frac{2+s^2+s\sqrt{s^2+8}}6.
\end{aligned}
\]
The gain in the *sharp expected energy decrement* over volume sampling has the exact limiting value
\[
\lim_{s\uparrow1}\frac{1-\Lambda(q^*)}{1-\Lambda(q^{\rm vol})}=\frac43.
\]
Thus the specifically motivated volume law can be less effective in the worst-case one-step energy metric even than uniform block sampling, despite selecting blocks of identical size and cost.

## Assumptions and scope

Let \(f(x)=\tfrac12x^{\mathsf T}Hx-b^{\mathsf T}x\), \(H=H^{\mathsf T}\succ0\), and \(x_*=H^{-1}b\). Every iteration draws independently from the same distribution \(q\) and exactly minimizes \(f\) in the updated set \([n]\setminus\{j\}\), leaving coordinate \(j\) fixed. All \(q_j\ge0\), \(\sum_jq_j=1\) are allowed; the optimum is interior under the stated Gram hypothesis. The error is the squared \(H\)-energy \(\|x-x_*\|_H^2\), twice the objective gap. Optimization is of the **worst initial error direction** of the **one-step conditional expectation**, not the exact finite-horizon mean-square or asymptotic spectral radius. No implementation-cost benefit from computing the optimizer is asserted.

For the special star, volume sampling of a pair \(S\) uses probability proportional to \(\det H_{SS}\), as in the cited block-coordinate volume-sampling construction. The matrices \(H_c\) are positive definite exactly for the stated \(c\)-range. The dimension-three comparison uses exactly two coordinates per update.

## Proof

**Rank-one energy residual.** For each omitted index \(j\), the exact updated error is the \(H\)-orthogonal projection of the old error onto \(\operatorname{span}(H^{-1}e_j)\):
\[
e^+=\frac{e_j^{\mathsf T}e}{K_{jj}}Ke_j.
\]
Consequently,
\[
\|e^+\|_H^2=\frac{(e_j^{\mathsf T}e)^2}{K_{jj}}.
\]
Let \(z=H^{1/2}e\) and \(v_j=H^{-1/2}e_j/\sqrt{K_{jj}}\), so \(\|v_j\|_2=1\) and \(v_i^{\mathsf T}v_j=G_{ij}\). Taking the expectation gives \(\mathbb E\|e^+\|_H^2=z^{\mathsf T}(\sum_jq_jv_jv_j^{\mathsf T})z\). Maximization over nonzero \(e\) gives the largest eigenvalue of this positive-semidefinite matrix. Its nonzero eigenvalues equal those of \(Q^{1/2}GQ^{1/2}\). Since \(G\) is positive definite, this also holds for boundary distributions by continuity. The first formula follows, with equality attained by a top eigenvector.

**Global minimax lemma.** Write \(w_j=D_{jj}v_j\), \(W=[w_1\ \cdots\ w_n]\). The matrix \(W\) is invertible, its Gram matrix is \(\widetilde G\), and \(\sum_jq_jw_jw_j^{\mathsf T}\) has the same eigenvalues as the unsigned version. Set \(r=\widetilde G^{-1}{\bf1}>0\) and \(R=\sum_jr_j>0\). The fixed vector \(z_0=W^{-\mathsf T}{\bf1}/\sqrt R\) is a unit vector, because \(\|W^{-\mathsf T}{\bf1}\|^2={\bf1}^{\mathsf T}\widetilde G^{-1}{\bf1}=R\). For every feasible \(q\),
\[
z_0^{\mathsf T}\left(\sum_jq_jw_jw_j^{\mathsf T}\right)z_0
=\sum_jq_j/R=1/R.
\]
Hence \(\Lambda(q)\ge1/R\). Set \(q_j^*=r_j/R\). Then \(\widetilde G r={\bf1}\) implies
\[
Q_*^{1/2}\widetilde GQ_*^{1/2}\sqrt{q^*}=R^{-1}\sqrt{q^*}.
\]
The matrix is entrywise nonnegative and \(\sqrt{q^*}>0\), so its spectral radius equals \(1/R\) by Collatz--Wielandt; this is its largest eigenvalue. Equality therefore holds. If another \(q\) attained \(1/R\), the unit \(z_0\) attaining its Rayleigh upper bound would have to satisfy \((\sum_jq_jw_jw_j^{\mathsf T})z_0=z_0/R\). As \(w_j^{\mathsf T}z_0=1/\sqrt R\), this reduces to \(Wq=z_0/\sqrt R=Wq^*\); invertibility forces \(q=q^*\). This includes boundary \(q\), proving global uniqueness.

**Three-variable star.** A direct inversion of \(H_c\), followed by changing the sign of its center column in the normalized Gram, yields
\[
\widetilde G=\begin{pmatrix}1&s&s\\s&1&s^2\\s&s^2&1\end{pmatrix},\qquad
\widetilde G^{-1}{\bf1}=\frac1{1+s}(1-s,1,1)^{\mathsf T}.
\]
All entries of \(\widetilde G\) and of this inverse-row-sum vector are positive. The minimax lemma gives the displayed \(q^*\) and \(\Lambda(q^*)\). The three updated-pair determinants are \(1,1-c^2,1-c^2\); normalizing them gives the displayed \(q^{\rm vol}\).

For every symmetric omission law \(q=(1-2p,p,p)\), \(0\le p\le1/2\), the Gram spectrum has antisymmetric-leaf eigenvalue \(p(1-s^2)\) and two symmetric-mode eigenvalues
\[
\lambda_\pm(p)=\frac{1-(1-s^2)p\pm\sqrt{[1-(3+s^2)p]^2+8s^2p(1-2p)}}2.
\]
Since \(\lambda_+(p)\ge p(1+s^2)>p(1-s^2)\) whenever \(p>0\), the top eigenvalue is \(\lambda_+(p)\); the endpoint \(p=0\) is immediate. Substitution of \(p=1/(3+s^2)\) and \(p=1/3\) yields the displayed closed forms. To compare these laws, write the radicand as \(\Delta(p)\). Its derivative is affine in \(p\), and
\[
\Delta'\!\left(\frac1{3+s^2}\right)=\frac{8s^2(s^2-1)}{3+s^2}<0,\qquad
\Delta'\!\left(\frac13\right)=\frac{2s^2(s^2-1)}3<0.
\]
Therefore throughout \([1/(3+s^2),1/3]\),
\[
\lambda_+'(p)=-(1-s^2)/2+\Delta'(p)/(4\sqrt{\Delta(p)})<0.
\]
Thus uniform omission strictly improves over volume omission. The unique global minimizer \(p=1/(3-s)>1/3\) is distinct from uniform, so \(\Lambda(q^*)<\Lambda(q^{\rm unif})\). Finally, direct differentiation at \(s=1\) gives the left derivatives \(1\) and \(3/4\) of \(\Lambda(q^*)\) and \(\Lambda(q^{\rm vol})\), respectively, proving the \(4/3\) limiting gain in decrement. All assertions hold for every real \(s\in(0,1)\).

## Verification

The accompanying `artifacts/verify_sampling.py` independently reconstructs the star Gram, omission laws, optimizing row sums, and exact block-residual identities on rational SPD test matrices. It checks weighted-Gram spectral equivalences numerically and multiple rational instances of the strict comparison, as well as the general nonnegative-Gram optimizer. The deterministic run passed 62 checks (symbolic identities, exact arithmetic, and numerical spectral checks). These finite checks are supplementary: all real-parameter claims, strictness and uniqueness follow from the analytic proof above. Run with Python 3 and the dependencies recorded in `artifacts/requirements.txt`.

## Relationship to prior work

Rodomanov and Kropotov (arXiv:1904.04587, first posted 2019-04-09) study determinant-proportional (volume) sampling for randomized block coordinate descent and give convergence bounds, but their displayed results do not optimize the fixed pair-selection law for the sharp quadratic one-step energy eigenvalue or identify the star-family volume-versus-uniform reversal. Qu, Richtárik, Takáč and Fercoq (arXiv:1502.02268) treat stochastic block Newton/coordinate subproblems and general sampled Hessian bounds, not this minimax classification.

A published 2026 result, *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, gives an explicit optimizer for **one-coordinate** updates using a **smallest** eigenvalue objective. This differs from the **all-but-one-coordinate**, inverse-Hessian, **largest** eigenvalue problem here. Related existing three-variable pair-sampling calculations already supply the optimal weights on a three-node path; that special optimizer is stated for reproducibility and **not claimed as a novel independent finding**. The specifically new comparison concerns determinant-proportional volume sampling being strictly worse than uniform sampling along an entire SPD star family, with the exact near-singular \(4/3\) decrement gap, alongside the stated general sufficient condition for complement-block minimax weights. The shared Gram/Perron structure is acknowledged. Standard saturated E-optimal-design and diagonal-scaling results are a possible equivalence route for the general lemma; their broader literature has not been exhaustively classified. Claim of precedence is limited to the inspected materials.

## Limitations

The theorem optimizes sharp one-step worst-direction expected \(H\)-energy retention, not any fixed initial direction or the exact \(m\)-step distribution for \(m>1\). It assumes an exact solve of an \((n-1)\)-coordinate block and iid fixed selection. No randomized-solver wall-clock comparison or claim for approximate solves, nonquadratic objectives, adaptive distributions, or other curvature classes is made. The signability/nonnegative-Gram and positive inverse-row-sum assumptions are **sufficient** for the closed form, not asserted necessary. Volume sampling retains its known benefits for different metrics and problem classes. The proof is self-contained; an older equivalent optimal-design characterization remains a residual precedence risk.

## References

1. A. Rodomanov and D. Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587 (first public version 2019-04-09), https://arxiv.org/abs/1904.04587.
2. Z. Qu, P. Richtárik, M. Takáč and O. Fercoq, *SDNA: Stochastic Dual Newton Ascent for Empirical Risk Minimization*, arXiv:1502.02268, https://arxiv.org/abs/1502.02268.
3. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995.
4. F. Pukelsheim and B. Torsney, *Optimal weights for experimental designs on linearly independent support points*, Annals of Statistics 19(3) (1991), 1614–1625, https://doi.org/10.1214/aos/1176348265.
