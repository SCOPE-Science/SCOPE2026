# One shortcut nearly doubles the Krylov spectral grade of a Boolean cube, with one parity-controlled resonance

## Finding
For every integer \(d\ge3\), join two previously nonadjacent vertices of the unweighted Boolean cube \(Q_d\), at Hamming distance \(2\le r<d\), by a positive-conductance edge of weight \(t>0\). Let \(L_d\) be its ordinary combinatorial Laplacian, \(v=e_u-e_v\), and let
\[
 A_{d,r}(t)=I+L_d+t vv^{\mathsf T}.
\]
The number \(N_{d,r}(t)\) of **distinct eigenvalues** of this positive-definite matrix is exactly
\[
 N_{d,r}(t)=\begin{cases}
 2d,&r\text{ odd, for every }t>0,\\
 2d-1,&r\text{ even and }t=t_{d,r},\\
 2d,&r\text{ even and }t\ne t_{d,r},
 \end{cases}
\]
where the unique positive resonant conductance for even \(r\) is
\[
 t_{d,r}=\left[\sum_{k=1}^{d-1}\frac{w_k(d,r)}{2(d-k)}\right]^{-1},\qquad
 w_k(d,r)=2^{2-d}\sum_{\substack{j\ \mathrm{odd}\\0\le j\le r\\0\le k-j\le d-r}}
 \binom rj\binom{d-r}{k-j}.
\]
In particular, for the shortest new shortcut, \(r=2\),
\[
 t_{d,2}=\frac{d-1}{2-2^{2-d}}\sim\frac d2.
\]
Without the shortcut, \(I+L_d\) has exactly \(d+1\) eigenvalues. Therefore a single nonlocal edge raises the maximal exact-arithmetic conjugate-gradient termination degree from \(d+1\) to \(2d\) generically, while one positive resonant weight reduces the degree by exactly one if and only if the Hamming distance is even.

## Assumptions and scope
Vertices are bit strings in \(\{0,1\}^d\); two are adjacent when they differ in exactly one bit. The cube edges have unit conductance. The added edge has weight \(t>0\) and connects vertices at distance \(r\) satisfying \(2\le r<d\). The shifted matrix is symmetric positive definite for every permitted choice. The quantity \(N_{d,r}(t)\) counts distinct eigenvalues, not multiplicity. The CG conclusion is about exact arithmetic, zero initial guess, and right-hand sides with nonzero projection onto every eigenspace; it does not assert a worst-case finite-precision iteration count at any fixed tolerance. Antipodal shortcuts \(r=d\), multiple added edges, and negative conductances are not included.

## Proof
**Walsh spectral masses.** For each subset \(S\subseteq[d]\), the normalized Walsh character \(\psi_S(x)=2^{-d/2}(-1)^{\sum_{j\in S}x_j}\) is an eigenvector of \(L_d\) with eigenvalue \(2|S|\). Consequently the original eigenspace at \(2k\) has multiplicity \(\binom dk\), for \(k=0,\ldots,d\). By cube automorphisms, set \(u=0\) and let \(v\) have its first \(r\) bits equal to one. The squared length of the spectral projection of \(e_u-e_v\) onto level \(2k\) is
\[
 \sum_{|S|=k}|\langle\psi_S,e_u-e_v\rangle|^2
 =2^{2-d}\sum_{\substack{j\ \mathrm{odd}\\0\le j\le r\\0\le k-j\le d-r}}\binom rj\binom{d-r}{k-j}=w_k(d,r).
\]
Thus \(w_0=0\) and \(\sum_kw_k=2\). Every \(w_k>0\) for \(1\le k\le d-1\). Indeed, for \(k\le d-r+1\), choose exactly one of the \(r\) differing coordinates and \(k-1\) unchanged coordinates. For \(k>d-r+1\), the allowable intersection counts form a block of at least two consecutive integers, because \(r\le d-1\) and \(k\le d-1\), so at least one allowable count is odd. Finally \(w_d>0\) exactly when \(r\) is odd, because the sole subset at level \(d\) meets the differing coordinates in \(r\) positions.

**Secular spectrum.** Write \(B_t=L_d+t vv^{\mathsf T}\); shifting by \(I\) does not affect the number of distinct eigenvalues. By the matrix determinant lemma, away from the poles of the resolvent the new eigenvalues satisfy
\[
 F_t(z)=1+t\sum_{k:w_k>0}\frac{w_k(d,r)}{2k-z}=0.
\]
On each interval between adjacent active poles, \(F_t'(z)=t\sum w_k/(2k-z)^2>0\); its endpoint limits have opposite infinite signs. Thus there is exactly one simple root in every such interval, and exactly one simple root strictly above the largest active pole. There is no root below the smallest active pole for \(t>0\). Each old eigenspace retains the hyperplane perpendicular to \(v\); hence the old levels \(2,4,\ldots,2d-2\) remain with positive multiplicity \(\binom dk-1\), and the old level \(0\) remains. For odd \(r\), the one-dimensional top eigenspace at \(2d\) is active and does not persist. There are \(d\) retained old values and \(d\) new roots, all distinct, giving \(2d\) distinct values.

For even \(r\), the top level is inactive, so \(2d\) also remains. The largest of the \(d-1\) new roots lies in \((2d-2,\infty)\). Its equation at the retained top level is
\[
 F_t(2d)=1-t\sum_{k=1}^{d-1}\frac{w_k(d,r)}{2(d-k)}.
\]
The sum is strictly positive; therefore it vanishes at precisely one positive \(t=t_{d,r}\). At this weight the new root coincides with the retained top eigenvalue, increasing its multiplicity from one to two. The number of distinct eigenvalues is consequently \(2d-1\), and it is \(2d\) at all other positive weights. This also shows the resonance is an ordinary eigenvalue collision, not a loss of positive definiteness.

**Distance-two closed form.** With \(r=2\), the only odd intersection size is one, hence
\[
 w_k(d,2)=2^{3-d}\binom{d-2}{k-1},\qquad
 \sum_{k=1}^{d-1}\frac{w_k(d,2)}{2(d-k)}
 =\frac{2-2^{2-d}}{d-1}.
\]
The last equality follows from
\[
 \sum_{j=0}^{d-2}\frac{\binom{d-2}{j}}{d-1-j}
 =\frac{2^{d-1}-1}{d-1},
\]
which is obtained by integrating \((1+x)^{d-2}\) on \([0,1]\). Inverting gives the stated closed form and asymptotic.

**Krylov consequence.** For a real symmetric positive-definite matrix, the degree of the minimal polynomial equals the number of its distinct eigenvalues; the minimal polynomial relative to a generic right-hand side has the same degree. Exact-arithmetic CG with zero initial guess therefore terminates after precisely \(N_{d,r}(t)\) iterations on a generic right-hand side. The original cube matrix takes \(d+1\) iterations in the same sense.

## Verification
A standalone Python verifier, `verify_hypercube_edge.py`, independently evaluates Walsh masses by direct character summation and by the binomial formula; tests the predicted number of distinct eigenvalues through numerical diagonalization on all \(d=3,\ldots,8\) and \(2\le r<d\); checks resonance positions on either side of each even-distance threshold; checks the distance-two formula for \(d=3,\ldots,29\) in exact rational arithmetic; and uses exact symbolic matrix ranks to check the top-eigenspace collision in dimensions three and four. It reports `PASS: 524 spectral masses, eigenvalue and exact-rank assertions`. Finite verification is supplementary to the complete analytical proof above, and the numerical eigenvalue clustering tolerance is not used to prove the infinite statement.

Reproduce using `OPENBLAS_NUM_THREADS=1 python verify_hypercube_edge.py` with Python 3, NumPy, and SymPy.

## Relationship to prior work
Farrell's 2015 rank-one eigenvalue-count theorem bounds the total number after rank-one perturbation of a diagonalizable matrix by twice the original number; it does not identify the all-distance Boolean-cube counts or their resonant conductances. Xu's 2016 bound refines general eigenvalue-count estimates but likewise does not specialize them to this exact combinatorial family. So's earlier edge-addition paper and the later general preserved-eigenspace theorem of Bueno, Furtado and Pérez establish the framework for how a single added edge can preserve or generate an existing Laplacian eigenvalue. In particular, Corollary 7.5 of the latter gives a general criterion and uniqueness of a single-edge exceptional weight; the novelty here is not the general uniqueness mechanism but the explicit Hamming-distance parity classification, complete eigenvalue-count formula and closed distance-two resonance. The Klee–Stamps rank-one operation is instead of the form \(L+u\mathbf1^{\mathsf T}\) and leaves all nonzero eigenvalues unchanged. The cube Walsh spectrum is classical; no new spectral decomposition of the unmodified cube is claimed.

## Limitations
An unindexed treatment of the same hypercube shortcut could predate this result; priority is not independently established. The six-page 1999 paper of So was located by abstract and bibliographic record but its complete text was not accessible during comparison, presenting a specific residual originality risk. A 2026 theorem about general exceptional weights gives a broader mechanism, although its inspected main text contains no hypercube specialization. The theorem counts exact eigenvalues and exact-arithmetic CG termination for generic right-hand sides, not practical runtime, finite-precision convergence speed, spectral condition numbers, or termination for arbitrary right-hand sides. No claim is made for antipodal shortcuts or several added edges.

## References
1. Patrick E. Farrell, *The number of distinct eigenvalues of a matrix after perturbation* (first public 2015-08-30), https://arxiv.org/abs/1508.07633 ; SIAM Journal on Matrix Analysis and Applications 37 (2016), DOI https://doi.org/10.1137/15M1037603.
2. Xuefeng Xu, *An improved upper bound for the number of distinct eigenvalues of a matrix after perturbation* (2016-07-04), https://arxiv.org/abs/1607.00766.
3. Wasin So, *Rank one perturbation and its application to the Laplacian spectrum of a graph*, Linear and Multilinear Algebra 46 (1999), DOI https://doi.org/10.1080/03081089908818613 (full text not accessed).
4. Maribel Bueno, Susana Furtado, Javier Pérez, *Eigenspaces of Preserved Graph Laplacian Eigenvalues under Positive Edge-Weight Addition* (2026), https://arxiv.org/abs/2610.14310 (particularly Corollary 7.5).
5. Steven Klee and Matthew T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations* (2020), https://arxiv.org/abs/2008.01669.
6. Bojan Mohar, *Some Applications of Laplace Eigenvalues of Graphs* (1997), https://www.math.ucdavis.edu/~saito/data/LapEig/mohar-graphlapeig-apps.pdf (cube spectrum in Example 2.5).
