# Sharp inertia obstruction to diagonal bimodal preconditioning and a rank-one escape

## Finding
For a real symmetric nonsingular matrix \(A\in\mathbb R^{n\times n}\) with zero diagonal and inertia \((r,s)\), where \(r,s\ge1\) and \(r+s=n\), consider a positive diagonal preconditioning factor \(G\) and the unsmoothed two-well spectral loss
\[
\mathcal L_0(G;A)=\frac1n\sum_{i=1}^n\bigl(|\lambda_i(G^{\mathsf T}AG)|-1\bigr)^2.
\]
Then every such factor satisfies the sharp lower bound
\[
\boxed{\mathcal L_0(G;A)\ge \frac{(r-s)^2}{n^2}.}
\]
Equality occurs precisely when the positive eigenvalues of \(G^{\mathsf T}AG\) all equal \(2s/n\) and its negative eigenvalues all equal \(-2r/n\). For every \(n,r,s\) as above, some real symmetric nonsingular zero-diagonal matrix realizes equality.

There is a sharp global factor-support separation for every positively weighted complete-graph adjacency matrix
\[
A=W(\mathbf1\mathbf1^{\mathsf T}-I)W,\qquad W=\operatorname{diag}(w_1,\ldots,w_n),\quad w_i>0,\quad n\ge3.
\]
For these matrices the global minimum over **all positive diagonal** factors is
\[
\boxed{\min_{G\;\mathrm{positive\ diagonal}}\mathcal L_0(G;A)=\left(\frac{n-2}{n}\right)^2,\qquad G_{\rm opt}=\sqrt{\frac2n}\,W^{-1},}
\]
and the indicated factor is unique. Yet adding a *single rank-one correction* to a diagonal factor makes the same target loss exactly zero. With \(P=\mathbf1\mathbf1^{\mathsf T}/n\), the factor
\[
G_{\rm lr}=W^{-1}\left[I+\bigl((n-1)^{-1/2}-1\bigr)P\right]
\]
satisfies \(G_{\rm lr}^{\mathsf T}AG_{\rm lr}=2P-I\), whose eigenvalues are exactly \(+1\) and \(-1\).

## Assumptions and scope
The matrices are real, symmetric, nonsingular, and of order \(n\ge2\) with zero diagonal. For the universal lower bound, \(G\) is any nonsingular real diagonal factor (positive diagonal factors suffice), and its congruence preserves the inertia. The uniqueness and rank-one claims require \(n\ge3\) and positive weights \(w_i\). This result analyzes **only** the unsmoothed clustering component \((|\lambda|-1)^2\) of a bimodal spectral objective. It does not solve the smoothed/logarithmically regularized objective proposed in the motivating paper, nor does it imply a particular Krylov iteration count.

## Proof
**Inertia/trace bound.** Write \(B=G^{\mathsf T}AG\). Since \(A_{ii}=0\) and \(G\) is diagonal, \(B_{ii}=0\) and hence \(\operatorname{tr}B=0\). Sylvester's inertia law gives exactly \(r\) positive and \(s\) negative eigenvalues. Let their magnitudes be \(u_1,\ldots,u_r>0\) and \(v_1,\ldots,v_s>0\). Trace zero forces
\[
S=\sum_{i=1}^r u_i=\sum_{j=1}^s v_j>0.
\]
Applying Cauchy–Schwarz independently to the positive and negative branches,
\[
\begin{aligned}
n\mathcal L_0&=\sum_i(u_i-1)^2+\sum_j(v_j-1)^2\\
&\ge S^2\left(\frac1r+\frac1s\right)-4S+n\\
&=\frac{n}{rs}\left(S-\frac{2rs}{n}\right)^2+\frac{(r-s)^2}{n}.
\end{aligned}
\]
Equality requires \(S=2rs/n\) and equality in both Cauchy–Schwarz inequalities, hence all \(u_i=S/r=2s/n\) and all \(v_j=S/s=2r/n\). Conversely, those conditions give equality.

**Sharpness for each inertia.** There exists a real rank-\(r\) orthogonal projection \(\Pi\) on \(\mathbb R^n\) with diagonal entries all \(r/n\). One explicit construction uses the real discrete Fourier orthonormal basis: choose complete sine/cosine frequency pairs, each contributing squared row norm \(2/n\), and when the requested rank is odd include the constant vector, which contributes \(1/n\). For even \(n\), a rank-\(n\) projection also uses the Nyquist vector. Such choices realize every rank \(0\le r\le n\). Put
\[
B_*=2\Pi-\frac{2r}{n}I.
\]
Its diagonal vanishes; on \(\operatorname{ran}\Pi\) it has eigenvalue \(2s/n\), and on the orthogonal complement eigenvalue \(-2r/n\). For \(1\le r<n\) it is nonsingular and attains the bound with \(A=B_*\), \(G=I\).

**Weighted complete graphs and uniqueness.** Let \(J=\mathbf1\mathbf1^{\mathsf T}\). Since \(J-I\) has eigenvalues \(n-1\) once and \(-1\) with multiplicity \(n-1\), \(A=W(J-I)W\) has inertia \((1,n-1)\). At \(G_{\rm opt}=\sqrt{2/n}\,W^{-1}\), the transformed matrix is \((2/n)(J-I)\), with exactly the equality eigenvalues \(2(n-1)/n\) and \(-2/n\).

Suppose another positive diagonal \(G\) attains the same minimum. Writing \(u_i=w_iG_{ii}>0\), its transformed matrix is \(B=uu^{\mathsf T}-\operatorname{diag}(u_i^2)\). By equality, \(B+(2/n)I\) is positive semidefinite of rank one, so it is \(vv^{\mathsf T}\). Every off-diagonal entry yields \(v_iv_j=u_iu_j>0\). Because \(n\ge3\), all ratios \(v_i/u_i\) have the same sign and satisfy every pair-product equal to one, hence \(v_i=\pm u_i\) with a common sign. From diagonal entries \(v_i^2=2/n\) we get \(u_i=\sqrt{2/n}\) for every \(i\); thus the diagonal optimum is unique.

**One rank-one direction removes the gap.** Write \(J-I=(n-1)P-(I-P)\), and \(Q=I+((n-1)^{-1/2}-1)P\). Then \(Q\) acts by \((n-1)^{-1/2}\) on \(\operatorname{ran}P\) and by one on \(\ker P\). Taking \(G_{\rm lr}=W^{-1}Q\) gives
\[
G_{\rm lr}^{\mathsf T}AG_{\rm lr}=Q(J-I)Q=P-(I-P)=2P-I,
\]
which proves exact two-well clustering. The factor is a diagonal matrix plus one outer product, though it is not generally diagonal or sparse entrywise.

## Verification
The accompanying `verify.py` tests the global lower bound with fixed-seed numerical examples of general hollow symmetric matrices, checks the weighted complete-graph equality and unique-scaling signature, and evaluates the explicit rank-one correction for several dimensions and positive weight profiles. Exact computations in the proof, not finite tests, establish the universal statements. Run with `python verify.py`; Python 3 and NumPy are required.

## Relationship to prior work
Brarda, Xu, Kalantzis, Li and Xi (arXiv:2606.22742, first posted June 22, 2026) formulate factor-support spectral optimization and an indefinite bimodal penalty using a smoothed absolute value plus logarithmic anti-zero regularization. Their Section 3 introduces the two-sided target and notes that prescribed sparse supports can prevent exact clustering. The present result isolates the *unsmoothed quadratic clustering term* and proves an explicit sharp inertia-dependent obstruction, equality spectra, a globally unique diagonal optimum for weighted complete graphs, and exact elimination by one rank-one augmentation. No claim is made that the regularized objective itself has the displayed minimum. Classical ingredients are Sylvester's inertia law, Cauchy–Schwarz, Schur–Horn/real Fourier constant-diagonal projections, and the elementary complete-graph adjacency spectrum.

## Limitations
This is a spectral-target result in exact arithmetic, not a residual, stability, iteration-count, or floating-point performance guarantee. The general inertia floor may be strict for a fixed matrix. The escape factor is diagonal plus rank one but generally dense. The uniqueness assertion is only for positive diagonal factors of the specified weighted complete-graph family. No novelty claim is made for the classical ingredients individually. The possibility of older unindexed special cases of the combined result remains a historical-priority risk; independent mathematical review has not been conducted.

## References
1. F. Brarda, T. Xu, V. Kalantzis, R. P. Li, Y. Xi, *Factored Sparse Approximate Inverse Preconditioning via Spectral Optimization*, arXiv:2606.22742 (first posted 2026-06-22), https://arxiv.org/abs/2606.22742 ; primary full-text reproduction: https://www.researchgate.net/publication/407509177_Factored_Sparse_Approximate_Inverse_Preconditioning_via_Spectral_Optimization .
2. Sylvester's law of inertia (classical congruence-invariance theorem), https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia .
3. Schur–Horn theorem (classical diagonal/eigenvalue realization theorem), https://en.wikipedia.org/wiki/Schur%E2%80%93Horn_theorem .
4. C. Bordenave, *Lecture notes on spectral graph theory*, complete graph adjacency spectrum, https://www.i2m.univ-amu.fr/perso/charles.bordenave/_media/courssrg.pdf .
5. V. Balakrishnan, S. Boyd, *Existence and Uniqueness of Optimal Matrix Scalings*, SIAM J. Matrix Anal. Appl. (1994), https://doi.org/10.1137/S0895479892235393 (comparison only: diagonal similarity scaling, different objective).
