# Exact symmetry-plane basins of iterated three-variable Pearson correlation

## Finding

Let \(\mathcal{C}\) be the map replacing a real \(3\times3\) correlation matrix by the matrix of Pearson correlations of its rows. On the entire transposition-fixed correlation-matrix slice
\[
A(r,s)=\begin{pmatrix}1&r&r\\r&1&s\\r&s&1\end{pmatrix},\quad -1\le s\le1,\quad 2r^2\le1+s,
\]
excluding the all-ones matrix, every orbit is defined and converges, with the following **complete, sharp basin trichotomy**:
\[
\begin{array}{ll}
r<s: & \mathcal{C}^{n}(A(r,s))\longrightarrow A(-1,1),\\
r=s: & \mathcal{C}(A(r,r))=A(-\tfrac12,-\tfrac12),\\
r>s: & \mathcal{C}^{n}(A(r,s))\longrightarrow A(0,-1).
\end{array}
\]
In the first case the off-diagonal dynamical coordinate converges quadratically to \(-1\) (with exact leading coefficient \(3/2\)); in the third case it approaches zero with limiting one-step ratio \(1/\sqrt3\). In particular, the rank-two mixed fixed point \(A(0,-1)\), unstable on the full three-dimensional elliptope, attracts a relatively open two-dimensional subset of this natural symmetry plane. The equicorrelation line \(r=s\) is the exact separator within the plane.

## Assumptions and scope

A correlation matrix is real, symmetric, positive semidefinite with all diagonal entries \(1\). For a row vector \(u\) of length three, let \(u^\circ=u-\frac13(u_1+u_2+u_3)(1,1,1)\). For nonconstant rows \(u,v\), Pearson correlation is \(\langle u^\circ,v^\circ\rangle/(\|u^\circ\|\|v^\circ\|)\). The model is exactly the row-correlation map, not ordinary entrywise matrix iteration. The two-coordinate section consists of *all* admissible matrices fixed by interchange of the last two labels; the excluded \(A(1,1)\) has constant rows and undefined correlations. The parameter condition is equivalent to positive semidefiniteness, because \(\det A(r,s)=(1-s)(1+s-2r^2)\), together with the indicated bounds.

## Proof

**Step 1: exact one-step reduction.** Put \(d=1-s\), \(B=2r-1-s\), and \(R=\sqrt{B^2+3d^2}\). On the admissible nonconstant domain \(R>0\) and \(r<1\). Centering the first row gives \(\frac{1-r}{3}(2,-1,-1)\), and centering the second and third rows gives vectors whose mutual normalized inner product is \(2(B/R)^2-1\). Their normalized inner products with the first row are both \(B/R\). Therefore, writing
\[
Q(r,s)=\frac{2r-1-s}{\sqrt{(2r-1-s)^2+3(1-s)^2}},\quad \Gamma(q)=A(q,2q^2-1),
\]
we have the **exact identity** \(\mathcal{C}(A(r,s))=\Gamma(Q(r,s))\). A direct Gram calculation shows \(\Gamma(q)\) is admissible for \(-1\le q<1\); at \(q=1\) it is the excluded all-ones matrix. Thus the entire two-dimensional slice maps into the same invariant rank-two meridian after one iterate.

**Step 2: scalar dynamics.** Substituting \(r=q\), \(s=2q^2-1\) into \(Q\) gives, since \(q<1\),
\[
\mathcal{C}(\Gamma(q))=\Gamma(f(q)),\qquad f(q)=\frac{q}{\sqrt{4q^2+6q+3}}\quad (-1\le q<1).
\]
Here \(f\) is strictly increasing on \((-1,1)\), \(f(-1)=-1\), and its only fixed points in the domain are \(-1,-\frac12,0\). Indeed,
\[
\operatorname{sgn}(f(q)-q)=-\operatorname{sgn}\big(q(2q+1)(q+1)\big),
\]
for nonfixed \(q\), because \(4q^2+6q+3-1=2(q+1)(2q+1)\). Hence each orbit from \(-1\le q<-\frac12\) decreases to \(-1\), each orbit from \(-\frac12<q<0\) increases to \(0\), and each from \(0<q<1\) decreases to \(0\). The point \(-\frac12\) stays fixed. Positivity of the normalizing denominator and \(f([-1,1))\subseteq[-1,1)\) prove all forward iterates exist.

**Step 3: exact original-coordinate separator.** If \(s<1\), the function \(B\mapsto B/\sqrt{B^2+3(1-s)^2}\) is strictly increasing and equals \(-\frac12\) exactly at \(B=-(1-s)\). Since \(B+(1-s)=2(r-s)\), \(Q(r,s)\lessgtr-\frac12\) if and only if \(r\lessgtr s\), and equality occurs only at \(r=s\). If \(s=1\), admissibility and nondegeneracy give \(r<1\), whence \(Q=-1\) and \(r<s\), consistent with the first basin. The face \(s=-1\) gives \(r=0\), \(Q=0\), and \(r>s\), consistent with the third. Since \(\Gamma(-1)=A(-1,1)\), \(\Gamma(-\frac12)=A(-\frac12,-\frac12)\), and \(\Gamma(0)=A(0,-1)\), the trichotomy follows.

**Step 4: sharp rates.** The expansion
\[
1+f(-1+\varepsilon)=\frac32\varepsilon^2+O(\varepsilon^3)\quad(\varepsilon\downarrow0)
\]
gives the quadratic asymptotic constant on nonstationary trajectories converging to \(-1\). Similarly \(f(q)=q/\sqrt3+O(q^2)\) as \(q\to0\), giving the claimed linear ratio on nonstationary trajectories converging to the mixed point. These rates concern the post-first-step scalar coordinate, not every entry or every orbit in the full elliptope.

## Verification

The standalone script `verify.py` verifies symbolic centered-row identities, the determinant and meridian formulas, the scalar derivative and endpoint expansions, and independently evaluates the full Pearson map over 530 reproducibly sampled positive-semidefinite matrices, including exact-symmetry and rank-deficient boundary cases. All sampled trajectories match the analytical basin partition. The finite sample is only corroboration; the proof above establishes the universal claim.

## Relationship to prior work

The original paper by Chen (2002) provides the iterative-correlation construction and rank-reduction background. The August 2026 preprint of Alhajj Hassan establishes all seven fixed points and relative stability; its August 25 revision establishes **global convergence for all** admissible \(3\times3\) matrices and proves the non-patterned exceptional stable sets have three-dimensional Lebesgue measure zero. It also derives the *same invariant meridian recurrence* \(f\), used there for local Lyapunov instability, and in its projective-kernel proof establishes convergence on equality loci. None of these previously proved statements is claimed new here. The present result supplies an additional explicit **original-coordinate basin partition of the entire two-dimensional transposition-symmetric slice**, including exactly which initial equal-correlation matrices converge to the mixed fixed point and which converge to the patterned vertex, with the complete boundary and rates. The later October 2026 convergence-rate paper provides local patterned bounds and other invariant Gram families; it does not give this full slice partition. This is a partial exact classification of the exceptional stable sets, not a full classification of the three-dimensional exceptional set.

## Limitations

This theorem only classifies the codimension-one symmetry plane \(a=b\) of the full three-dimensional elliptope. It neither determines all exceptional stable sets away from the plane nor improves the existing full-elliptope global convergence theorem. The normal form and meridian recurrence were already published; new content is the global initial-parameter basin partition and exact relative-open mixed basin on the *whole* plane. Priority has been assessed from accessible primary texts and searches, not independently certified. A self-review is not an independent audit.

## References

1. Ishrak Alhajj Hassan, *Fixed Points, Stability, Basin Geometry, and Global Convergence of the \(3\times3\) Correlation Map*, arXiv:2608.03404, versions 1 (2026-08-04) and 2 (2026-08-25), https://arxiv.org/html/2608.03404v2.
2. Ishrak Alhajj Hassan, *Local quadratic convergence of iterated correlation matrices: bounds and counterexamples*, arXiv:2610.24592 (2026-10-17), https://arxiv.org/abs/2610.24592.
3. Chun-Houh Chen, *Generalized Association Plots: information visualization via iteratively generated correlation matrices*, Statistica Sinica 12 (2002), 7–29, https://www3.stat.sinica.edu.tw/statistica/j12n1/j12n11/j12n11.html.
4. J. B. Kruskal, *A theorem about CONCOR*, 1977 manuscript, https://web.osu.cz/~Zusmanovich/files/kruskal/Binder1.pdf.
