# Exact two-outcome erasure fibers of symmetric informationally complete measurements

## Finding

**Theorem (conditional on existence of a SIC).** Let \(d\ge2\), and let \(u_1,\ldots,u_{d^2}\) be unit vectors in \(\mathbb C^d\) satisfying \(|\langle u_j,u_k\rangle|^2=1/(d+1)\) for distinct indices. Write \(P_j=u_ju_j^*\), \(E_j=P_j/d\), and \(p_j(\psi)=\langle\psi,E_j\psi\rangle\) for unit vectors \(\psi\). Fix distinct erased indices \(r,s\). Retain all \(d^2-2\) probabilities other than \(p_r,p_s\), **without renormalizing the retained outcomes**.

(a) Removing any single outcome leaves normalized pure states uniquely identifiable up to global phase. Removing two never does. Set \(W=\operatorname{span}\{u_r,u_s\}\). The operator \(H=P_r-P_s\) has simple eigenvalues \(\pm\lambda\) on \(W\), with \(\lambda=\sqrt{d/(d+1)}\). Choose orthonormal eigenvectors \(e_+,e_-\), and define the projective involution
\[
[\alpha e_+ +\beta e_-]\longmapsto
[\overline\beta e_+ +\overline\alpha e_-]
\qquad (|\alpha|^2+|\beta|^2=1).
\]
Its projective definition does not depend on phases chosen for \(e_+\) and \(e_-\). Every ambiguous fiber of the retained-probability map consists of exactly the two distinct projective states paired by this involution, for \(\psi\in W\) with \(|\alpha|\ne|\beta|\). All states outside \(\mathbb P(W)\), and all states on the equator \(|\alpha|=|\beta|\) within \(\mathbb P(W)\), have singleton fibers.

(b) For a paired normalized state \(\psi=\alpha e_++\beta e_-\) and \(\psi'=\overline\beta e_++\overline\alpha e_-\), put \(\delta=|\alpha|^2-|\beta|^2\). Then the two unobserved probabilities differ by
\[
p_r(\psi)-p_r(\psi')=\frac{\delta}{\sqrt{d(d+1)}},\qquad
p_s(\psi)-p_s(\psi')=-\frac{\delta}{\sqrt{d(d+1)}}.
\]
The projective chordal distance is exactly \(|\delta|\). Consequently the missing-probability difference divided by chordal distance has the exact constant \(1/\sqrt{d(d+1)}\) for every nontrivial pair; the maximal invisible chordal distance is one, attained by orthogonal states.

(c) If \(d\ge4\), precisely the same two-point-fiber classification holds for **nonzero signals of unknown norm**, with the retained observations interpreted as unnormalized quadratic intensities. Every indistinguishable pair then has equal norms, and after common rescaling the pairing in (a) applies. This extension is false in dimension three: every qutrit SIC has noncollinear, unequal-norm signals with identical retained intensities after deleting any two outcomes.

The theorem makes no assertion that SIC configurations exist in every dimension: it applies in each dimension admitting such a configuration.

## Assumptions and scope

All Hilbert spaces and vectors are complex; \(P_j\) are rank-one orthogonal projections and \(E_j\) the original POVM effects. For normalized states, projective equivalence means multiplication by a scalar of modulus one. For unknown-norm signals, equivalence means multiplication by a scalar of modulus one **without** changing the norm. The retained output is the unconditioned list \((\langle x,E_jx\rangle)_{j\notin\{r,s\}}\). Conditional probabilities normalized by the sum of retained outcomes define a different inverse problem and are not covered.

## Proof

**1. Tightness and duality.** Let \(S=\sum_jP_j\). The SIC overlap identity gives
\[
\operatorname{tr} S=d^2,\qquad
\operatorname{tr}S^2=d^2+\frac{d^2(d^2-1)}{d+1}=d^3.
\]
Equality in the trace Cauchy--Schwarz inequality implies \(S=dI\), so the \(E_j\) sum to \(I\). The real Gram matrix for the Hermitian projectors has entries
\[
\operatorname{tr}(P_jP_k)=\frac{d\mathbf1_{j=k}+1}{d+1}.
\]
It is strictly positive definite, hence the \(d^2\) projectors form a real basis of all Hermitian \(d\)-by-\(d\) matrices. Its trace-dual basis is
\[
D_j=\frac{(d+1)P_j-I}{d},\qquad
\operatorname{tr}(D_jP_k)=\mathbf1_{j=k},\qquad
\operatorname{tr}D_j=\frac1d.
\]
Thus the kernel of the measurement map after deleting \(r,s\), acting on Hermitian matrices, equals the real plane \(\operatorname{span}_{\mathbb R}\{D_r,D_s\}\). After deleting a single outcome, the missing probability of a normalized state is determined by the sum-one rule, and complete SIC tomography yields uniqueness.

**2. The normalized collision operator.** Suppose unit vectors \(x,y\) have all retained probabilities equal. Then \(X=xx^*-yy^*=aD_r+bD_s\) for real \(a,b\). As \(\operatorname{tr}X=0\) and \(\operatorname{tr}D_j=1/d\), necessarily \(a+b=0\), hence
\[
X=c(P_r-P_s)=cH\quad\text{for a real }c.
\]
If \([x]\ne[y]\), the left side has rank two and range \(\operatorname{span}\{x,y\}\). The right side has range \(W\), since \(0<|\langle u_r,u_s\rangle|<1\). It follows that \(x,y\in W\). Conversely, for any normalized vectors in \(W\), their projectors differ by a multiple of \(H\) exactly when their off-diagonal entries in an eigenbasis of \(H\) are equal.

**3. Classification of all such pairs.** In the eigenbasis \(e_+,e_-\), write \(x=\alpha e_++\beta e_-\), \(y=\gamma e_++\eta e_-\). Their difference is diagonal precisely when \(\alpha\overline\beta=\gamma\overline\eta\). Normalization forces
\[
|\alpha|^2+|\beta|^2=|\gamma|^2+|\eta|^2=1,
\qquad |\alpha\beta|=|\gamma\eta|.
\]
The two possible unordered squared-coordinate magnitudes are therefore the same, because they are the roots of \(z(1-z)=|\alpha\beta|^2\). If the ordered magnitudes agree, equality of off-diagonal entries makes the projectors identical. If they are exchanged, the unique distinct projective solution is \(y=\overline\beta e_++\overline\alpha e_-\), up to phase. At \(|\alpha|=|\beta|\), the exchanged solution coincides projectively with the original. This proves the entire fiber classification, not just the existence of collisions. The same diagonalization shows the projective transformation is unaffected by rephasing its eigenvectors.

**4. Exact gap and distance.** The nonzero eigenvalues of \(H\) are \(\pm\sqrt{1-|\langle u_r,u_s\rangle|^2}=\pm\sqrt{d/(d+1)}\). For the reflected pair, \(xx^*-yy^*=(\delta/\lambda)H\). As \(\operatorname{tr}(P_rH)=d/(d+1)\) and \(\operatorname{tr}(P_sH)=-d/(d+1)\), division by \(d\) gives the formulas for the lost probabilities. Also
\[
|\langle x,y\rangle|=2|\alpha\beta|,
\qquad \sqrt{1-|\langle x,y\rangle|^2}
=\bigl||\alpha|^2-|\beta|^2\bigr|=|\delta|.
\]
Choosing \(x=e_+\) and \(y=e_-\) gives orthogonal, maximally separated indistinguishable pure states.

**5. Signals of unknown norm in dimension at least four.** Let \(X=xx^*-yy^*=aD_r+bD_s\) have rank at most two, for arbitrary nonzero \(x,y\). On the orthogonal complement \(W^\perp\), it acts by the scalar \(-(a+b)/d\). If \(d\ge5\), a nonzero scalar here would already force rank at least three. If \(d=4\), it gives rank two on \(W^\perp\); rank at most two would then require \(X|_W=0\). But \(P_r|_W\) and \(P_s|_W\) are rank-one, neither parallel nor orthogonal. An off-diagonal entry in a basis beginning with \(u_r\) forces \(b=0\), and a diagonal entry then forces \(a=0\), contradicting a nonzero scalar. Thus in all \(d\ge4\), rank at most two implies \(a+b=0\) (or \(X=0\)). The two signals therefore have equal squared norm, and rescaling recovers (a). There are no additional unequal-norm collisions.

**6. The sharp qutrit exception.** For \(d=3\), put \(c=|\langle u_r,u_s\rangle|=1/2\). The sum \(P_r+P_s\) has eigenvalues \(1+c,1-c\) on \(W\) and zero on \(W^\perp\). Consequently
\[
D_r+D_s=\frac{4(P_r+P_s)-2I}{3}
\]
has eigenvalues \(4/3,0,-2/3\). If \(v_+\) and \(v_\perp\) are corresponding orthonormal eigenvectors for \(4/3\) and \(-2/3\), then \(x=\sqrt{4/3}\,v_+\), \(y=\sqrt{2/3}\,v_\perp\) obey
\[
xx^*-yy^*=D_r+D_s.
\]
All retained intensities agree, but their norms differ, proving (c)'s boundary. \(\square\)

## Verification

The proof is a dimension-independent argument in the Hermitian matrix space, conditional on SIC existence. `CHECK.py` independently evaluates a nine-vector Hesse SIC in dimension three, verifies its projector Gram matrix, tests a reflected nontrivial state pair against all seven retained intensities, checks the exact missing-probability/chordal relation, and confirms the unequal-norm qutrit kernel eigenvalues. Run `python CHECK.py` after installing `requirements.txt`. Floating-point calculations are sanity checks only; the all-dimensional theorem follows from the preceding exact algebra.

## Relationship to prior work

Renes, Blume-Kohout, Scott and Caves (2004; preprint 2003) introduced the SIC geometry and its informationally complete projector frame; its dual reconstruction identity is the linear-algebraic starting point here. Edidin, Gonzalez and Tamo (2025) study minimal rank-one pure-state tomography and conditional deletion/renormalization notions; those are not the same map as fixed, unconditioned retained SIC outcomes considered here. Li (2026) constructs robust Gabor-based phase-retrieval frames and analyzes erasure stability for certain signal classes, but does not supply this SIC-specific complete fiber classification. Our theorem concerns the exact exceptional projective line and its two-point fibers rather than construction of a SIC or generic robustness of a Gabor frame.

## Limitations

SIC existence is assumed, not proved. The classification is for exactly two deleted outcomes from a complete SIC, not an arbitrary linearly independent informationally complete POVM. For unknown-norm signals, the full two-point classification is established only in dimensions at least four; the dimension-three counterexample shows the restriction is substantial. The theorem does not give a noisy reconstruction stability estimate for retained measurements. Earlier algebraic quantum tomography literature could contain an equivalent formulation, so publication priority needs independent assessment.

## References

1. J. M. Renes, R. Blume-Kohout, A. J. Scott and C. M. Caves, *Symmetric Informationally Complete Quantum Measurements*, J. Math. Phys. 45 (2004), 2171–2180; arXiv:quant-ph/0310075 (first posted October 13, 2003). https://arxiv.org/abs/quant-ph/0310075
2. D. Edidin, I. Gonzalez and I. Tamo, *Pure-State Quantum Tomography with Minimal Rank-One POVMs*, arXiv:2511.09505 (first posted November 12, 2025). https://arxiv.org/abs/2511.09505
3. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614 (first posted September 9, 2026). https://arxiv.org/abs/2609.09614
