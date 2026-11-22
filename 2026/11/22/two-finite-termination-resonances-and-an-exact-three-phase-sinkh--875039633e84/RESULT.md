# Two finite-termination resonances and an exact three-phase Sinkhorn-rate optimum on hub–clique kernels

## Finding

For every integer \(m\ge2\) and real parameter \(t>0\), consider the strictly entrywise-positive symmetric matrix
\[
A_m(t)=\begin{pmatrix}1&t\mathbf1_m^{\mathsf T}\\t\mathbf1_m&I_m+J_m\end{pmatrix},
\]
where \(J_m=\mathbf1_m\mathbf1_m^{\mathsf T}\). Let \(B_m(t)\) be the unique doubly stochastic diagonal scaling of \(A_m(t)\). The local asymptotic factor for one complete row–column Sinkhorn sweep on *arbitrary projective factor perturbations* is
\[
\rho_m(t)=\max\left\{\left(\frac{1-c}{m+1}\right)^2,\left(1-(m+1)c\right)^2\right\},
\quad
 t^2=\frac{(m+1)c^2}{(1-mc)(1-c)},\quad 0<c<\frac1m.
\]
The scalar equation has exactly one solution \(c=c_m(t)\). The active spectral mode switches at two sharp parameter values:
\[
t_1=\frac1{\sqrt2},\qquad t_2=\frac{m+2}{\sqrt{2m}}.
\]
For \(0<t<t_1\) the hub–leaf contrast eigenvalue is positive and controls the factor; for \(t_1<t<t_2\) leaf-difference modes control it; for \(t>t_2\) the negative hub–leaf contrast eigenvalue controls it. Consequently, **the unique globally optimal parameter** over all \(t>0\) is
\[
\boxed{t_{\mathrm{opt}}=\frac{m+2}{\sqrt{2m}},\qquad
\min_{t>0}\rho_m(t)=\frac{m^2}{(m^2+2m+2)^2}.}
\]
At the optimizer the two kinds of nontrivial eigenvalues have equal absolute values and opposite signs.

Separately, apply ordinary alternate *whole-matrix* row normalization and column normalization to \(A_m(t)\), starting with row normalization and **no arbitrary preliminary diagonal scaling**. The iteration reaches an exactly doubly stochastic matrix in finitely many normalizations **if and only if**
\[
\boxed{t=\sqrt{\frac{m+1}{m}}\quad\text{or}\quad t=\frac{m}{m-1}.}
\]
The second parameter terminates after exactly one row normalization, whereas the first terminates after exactly one row and one subsequent column normalization. For \(m=2\), the one-step termination parameter coincides with \(t_{\mathrm{opt}}\); for every \(m\ge3\), neither finite-termination parameter is rate-optimal. The two-normalization parameter is nevertheless asymptotically rate-optimal:
\[
\frac{\rho_m(\sqrt{(m+1)/m})}{\rho_m(t_{\mathrm{opt}})}
=\left(1+\frac1{(m+1)^2}\right)^2\longrightarrow1.
\]
Finite termination for this specifically initialized orbit and worst-case local convergence over *all* nearby factors are distinct performance criteria; there is no assertion that the latter controls the former sharply.

## Assumptions and scope

Throughout, \(m\in\{2,3,\ldots\}\), \(t\in(0,\infty)\), and the matrix has exactly one hub index and \(m\) interchangeable leaf indices. Every matrix entry is positive; positive definiteness is neither asserted nor required. Doubly stochastic means each row and column sums to one. The local factor is the spectral radius of the derivative of one full row–column factor sweep on the logarithmic factor space modulo constant vectors, not a global uniform contraction constant. The finite-termination assertion refers to the unmodified alternating row-first scaling sequence initialized with \(A_m(t)\). All statements are in exact arithmetic.

## Proof

**1. Unique balancing and its complete spectrum.** Positivity gives existence and uniqueness of the doubly stochastic diagonal equivalence class by the classical Sinkhorn–Knopp theorem; since \(A_m(t)\) is symmetric and invariant under leaf permutations, its unique scaling is symmetric and has \(D=\operatorname{diag}(x,y,\ldots,y)\) with \(x,y>0\). Define \(c=txy\). Row sums of \(B=DAD\) yield
\[
x^2+mc=1,\qquad c+(m+1)y^2=1.
\]
Thus \(x^2=1-mc\), \(y^2=(1-c)/(m+1)\), and the displayed scalar relation for \(t^2\). Its right side as a function of \(c\in(0,1/m)\) grows strictly from zero to infinity: its logarithmic derivative is
\[
\frac2c+\frac{m}{1-mc}+\frac1{1-c}>0.
\]
Therefore \(c_m(t)\) exists uniquely and strictly increases with \(t\). The leaf-difference subspace, of dimension \(m-1\), is an eigenspace with eigenvalue \(a=(1-c)/(m+1)>0\). The two-dimensional hub/leaf-constant subspace has eigenvalues \(1\) and \(b=1-(m+1)c\) (hub contrast vector \((m,-1,\ldots,-1)\)). Hence the complete spectrum is \(\{1,b,a^{[m-1]}\}\).

**2. The local Sinkhorn Jacobian.** For positive column scaling factors \(v\), define one complete row–column factor sweep by \(F(v)=[A^{\mathsf T}(Av)^{-1}]^{-1}\), where inversions inside brackets are componentwise. The balancing vector \(d=(x,y,\ldots,y)\) is a fixed point up to scalar. Differentiate first in the logarithms of \(v\), then the intermediate row factors. At \(d\) the two log-Jacobians are \(-B\) and \(-B^{\mathsf T}\), so the full log-Jacobian equals \(B^{\mathsf T}B=B^2\). The scalar direction has eigenvalue one and is removed by projectivization. The remaining eigenvalues are \(a^2\) with multiplicity \(m-1\) and \(b^2\), giving the stated factor. This uses the standard local-rate principle established in Knight's earlier work, independently obtained here by explicit differentiation; the general principle itself is not new.

**3. Exact crossover and rate optimum.** As \(c\) increases, \(a\) decreases strictly and \(b\) decreases strictly, passing zero once. The positive equality \(b=a\) occurs exactly at \(c_1=1/(m+2)\), corresponding to \(t_1^2=1/2\). The negative equality \(b=-a\) occurs at \(c_2=(m+2)/(m^2+2m+2)\), corresponding to \(t_2^2=(m+2)^2/(2m)\). Direct comparison gives \(0<c_1<c_2<1/m\). Thus the larger absolute eigenvalue decreases through the first two regions and strictly increases past the second crossing. At \(c_2\), \(a=-b=m/(m^2+2m+2)\). This establishes all phase boundaries and proves the unique global minimizer, without assuming symmetry of perturbations. The scaling at this optimizer is explicitly
\[
B_m(t_{\mathrm{opt}})=\frac1{m^2+2m+2}
\begin{pmatrix}
2&(m+2)\mathbf1_m^{\mathsf T}\\
(m+2)\mathbf1_m&m(I_m+J_m)
\end{pmatrix}.
\]

**4. Exact row-first finite-termination parameters.** Write \(R_0=1+mt\) and \(R_L=m+1+t\) for the original hub and leaf row sums. After row normalization the two types of column sums are
\[
S_0=\frac1{R_0}+\frac{mt}{R_L},\qquad
S_L=\frac{t}{R_0}+\frac{m+1}{R_L}.
\]
After the subsequent column normalization, the hub and leaf row sums become respectively
\[
\frac1{R_0}\left(\frac1{S_0}+\frac{mt}{S_L}\right),\qquad
\frac1{R_L}\left(\frac t{S_0}+\frac{m+1}{S_L}\right).
\]
The hub row sum minus one simplifies exactly to
\[
\frac{mt\big((m-1)t-m\big)\big(mt^2-(m+1)\big)}
{\big(m^2t^2+mt+m+t+1\big)\big(m^2t+2mt+m+t^2+t+1\big)}.
\]
Its denominator is strictly positive for the stated domain and \(mt>0\). Therefore one row and one column normalization produce a doubly stochastic matrix precisely at \(t=m/(m-1)\) or \(t=\sqrt{(m+1)/m}\). At the first value \(R_0=R_L\), so the initial row normalization already makes the symmetric matrix doubly stochastic. At the second value the first normalized matrix has unequal column sums, so two normalizations are necessary. Cohen and Nathanson's general finite-termination theorem for positive square matrices implies that any finitely terminating alternating sequence must finish within two normalizations. It follows that these are the **only** finitely terminating parameters, not just the only two-step parameters.

**5. Comparing the two objectives.** The two-step resonance corresponds to \(c=1/(m+1)\), for which \(b=0\), \(a=m/(m+1)^2\), and \(\rho_m=m^2/(m+1)^4\). Dividing by the optimal rate gives the exact displayed ratio. The inequality \(\sqrt{(m+1)/m}<m/(m-1)\) holds for every \(m\ge2\), and \(m/(m-1)\le(m+2)/\sqrt{2m}\) with equality exactly at \(m=2\). This proves the stated exceptional coincidence and asymptotic separation of parameter values.

## Verification

The independent-from-derivation finite script `verify.py`, included with this result, checks the exact rational crossing identities and spectral-mode algebra for integers \(2\le m\le80\), numerical doubly stochastic scaling at specified test parameters, the one- versus two-normalization resonances, and numerical differentiation of the full factor map against \(B^2\). Running `python3 verify.py` with only the Python standard library produces `PASS: 5605 finite exact-rational and numerical assertions`. These finite checks support reproducibility but do **not** prove the claims for arbitrarily large \(m\) or every real \(t>0\); the preceding algebraic argument does.

## Relationship to prior work

Knight's 2007 analysis proves the general Sinkhorn–Knopp linearized convergence factor in terms of the subdominant singular value of the balanced matrix; no novelty is claimed for that general theorem. Knight and Ruiz study accelerated matrix balancing, not a three-phase tuning classification for the present affinity matrix. Nathanson's explicit-scalings papers develop related positive-matrix examples, and Cohen–Nathanson prove the general at-most-two-normalizations theorem; both facts are credited. The present contribution is the **joint exact parameter classification for the specified nontrivial leaf-difference family**: its full robust mode-switch phase diagram and unique optimal affinity, together with the two starting-matrix finite termination resonances and their precise quantitative relation. A search of the cited primary works and a mathematical-claims index found no statement directly covering this joint classification; failure to find an indexed equivalent is not a proof of global novelty.

## Limitations

Only the hub–clique family with its fixed leaf matrix \(I_m+J_m\), one free hub affinity, unit stochastic targets, and exact row-first Sinkhorn is considered. The optimality claim is **within this family**, not among arbitrary positive kernels or alternative algorithms. The local spectral radius describes the worst perturbation direction, not the observed convergence of every special initialization. Indeed the exactly terminating initialization can finish in two steps while the local robust factor remains nonzero. Floating-point iteration generally loses exact finite termination. Formal independent mathematical validation has not been performed. Broader unindexed related literature could affect publication priority.

## References

1. P. A. Knight, *The Sinkhorn–Knopp Algorithm: Convergence and Applications*, Dagstuhl Seminar Proceedings 07071, published 2007-06-28. DOI: https://doi.org/10.4230/DagSemProc.07071.16 . In particular, Sections 2–4 and Theorems 4.4–4.5.
2. P. A. Knight and D. Ruiz, *A Fast Algorithm for Matrix Balancing*, Dagstuhl Seminar Proceedings 07071 (2007), https://doi.org/10.4230/DagSemProc.07071.4 .
3. A. Cohen and M. B. Nathanson, *Sinkhorn Limits in Finitely Many Steps*, arXiv:1912.00095 (first publicly posted 2019-11-29), https://arxiv.org/abs/1912.00095 .
4. M. B. Nathanson, *Matrix Scaling and Explicit Doubly Stochastic Limits*, arXiv:1905.09426 (2019), https://arxiv.org/abs/1905.09426 .
5. M. B. Nathanson, *Matrix Scaling Limits in Finitely Many Iterations*, arXiv:1903.06778 (2019), https://arxiv.org/abs/1903.06778 .
