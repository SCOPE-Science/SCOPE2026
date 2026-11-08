# Complete horizontal-line tomography spectrum on finite Heisenberg groups

## Finding

For every odd prime power \(q\) and every integer \(n\ge1\), let \(\mathcal R\) sum a complex function over **each distinct horizontal line exactly once** in the finite Heisenberg group \(H_n(\mathbb F_q)\). With counting measures on points and lines, put
\[
D=\frac{q^{2n}-1}{q-1},\qquad c=D-1.
\]
The full eigenvalue table of its normal operator \(\mathcal R^*\mathcal R\) is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\ \hline
c+q^{2n}&1\\
c&q^{2n}-1\\
c+q^n&\frac{(q-1)(q^{2n}+q^n)}2\\
c-q^n&\frac{(q-1)(q^{2n}-q^n)}2
\end{array}.
\]
In particular, this all-horizontal-line transform is injective **if and only if** \(n\ge2\). For \(n=1\) its nullity is \(q(q-1)^2/2\). In the injective ranks \(n\ge2\), its exact squared smallest singular value is \(c-q^n\), its exact squared largest singular value is \(c+q^{2n}\), and its squared spectral condition number is
\[
\kappa(\mathcal R)^2=\frac{c+q^{2n}}{c-q^n}.
\]
The theorem supplies explicit orthogonal Fourier spectral projectors, hence an exact inverse for \(n\ge2\) and a Moore–Penrose reconstruction on the observable subspace for \(n=1\).

## Assumptions and scope

Fix \(q=p^s\), where \(p\) is an odd prime and \(s\ge1\), and \(n\ge1\). Let \(V=\mathbb F_q^n\oplus\mathbb F_q^n\) and let
\[
\sigma((x,y),(x',y'))=x\cdot y'-y\cdot x'
\]
be its nondegenerate alternating form. Define \(H_n=V\times\mathbb F_q\) with multiplication \((z,t)(w,s)=(z+w,t+s+\sigma(z,w))\). For each nonzero \(v\in V\), spatial projective direction \([v]\), and base point \((z,t)\), the horizontal line is
\[
L_{(z,t),[v]}=\{(z+a v,t+a\sigma(z,v)):a\in\mathbb F_q\}.
\]
Take \(\mathcal L\) to contain each **distinct subset** of this form once; it has \(|\mathcal L|=q^{2n}D\) lines, while \(|H_n|=q^{2n+1}\) points. Define
\[
(\mathcal R f)(L)=\sum_{h\in L} f(h),\qquad
\|f\|_2^2=\sum_{h\in H_n}|f(h)|^2,\quad
\|y\|_2^2=\sum_{L\in\mathcal L}|y(L)|^2.
\]
All displayed eigenvalues, singular values and bounds use these **unaveraged** line sums and **unnormalized** counting measures. Restricting to one line per direction, averaging over lines, or adding vertical lines produces different operators and is not covered.

## Proof

**1. Incidence kernel.** Every point lies on exactly \(D\) horizontal lines, one per spatial projective direction. If \((z,t)\ne(w,s)\), they lie on a common horizontal line exactly when
\[
z\ne w\quad\text{and}\quad s-t=\sigma(z,w).
\]
Indeed the spatial difference fixes \([v]=[w-z]\), and the central coordinate then has precisely the displayed necessary-and-sufficient relation. Consequently any two distinct points share at most one horizontal line. Writing \(K=\mathcal R^*\mathcal R\), the common-line counts give the **exact** identity
\[
(Kf)(z,t)=c f(z,t)+\sum_{w\in V} f(w,t+\sigma(z,w)). \tag{1}
\]
The sum includes \(w=z\), restoring the diagonal degree \(D=c+1\).

**2. Central Fourier decomposition.** Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C\) and let \(\chi_\eta(t)=\psi(\eta t)\), for \(\eta\in\mathbb F_q\). Write
\[
\widehat f_\eta(z)=\sum_{t\in\mathbb F_q}f(z,t)\overline{\chi_\eta(t)}.
\]
Applying this transform to (1) produces \(cI+F_\eta\) on each central-frequency fiber, where
\[
(F_\eta h)(z)=\sum_{w\in V}\chi_\eta(\sigma(z,w))h(w).
\]
For \(\eta=0\), \(F_0\) is the all-ones matrix of order \(q^{2n}\); its eigenvalues are \(q^{2n}\) once and \(0\) with multiplicity \(q^{2n}-1\).

For each \(\eta\ne0\), skew symmetry of \(\sigma\) gives \((F_\eta)_{wz}=\overline{(F_\eta)_{zw}}\), so \(F_\eta\) is Hermitian. Orthogonality of additive characters and nondegeneracy of \(\sigma\) give
\[
(F_\eta^2)_{zu}
=\sum_{w\in V}\chi_\eta(\sigma(z-u,w))
=q^{2n}\mathbf1_{z=u}.
\]
Thus all its eigenvalues are \(+q^n\) or \(-q^n\). Its trace is exactly \(q^{2n}\), because \(\sigma(z,z)=0\) for every \(z\). Together with its dimension \(q^{2n}\), this fixes their multiplicities at
\[
\frac{q^{2n}+q^n}{2}\quad\text{and}\quad\frac{q^{2n}-q^n}{2},
\]
respectively. There are \(q-1\) nonzero central frequencies, giving the entire eigenvalue table, with multiplicities summing to \(q^{2n+1}\).

**3. Exact rank and bounds.** For \(n=1\), \(D=q+1\), hence \(c=q\); precisely the \(c-q^n\) modes vanish, and their number is \((q-1)(q^2-q)/2=q(q-1)^2/2\). In particular, for any nontrivial character \(\chi_\eta\), the nonzero function
\[
 f(z,t)=\chi_\eta(t)\left(\mathbf1_{\{z=0\}}-\frac1q\right)
\]
is in the kernel: its central-frequency fiber is an eigenvector of \(F_\eta\) with eigenvalue \(-q\). For \(n\ge2\), \(c=q+q^2+\dots+q^{2n-1}>q^n\), so every eigenvalue is positive. The least and largest eigenvalues are \(c-q^n\) and \(c+q^{2n}\). Finite-dimensional singular-value theory yields the stated sharp frame bounds and condition number; all eigenvalues have explicit nonzero-multiplicity eigenspaces, so the bounds are attained.

**4. Reconstructing Fourier fibers.** Put \(Q=q^{2n}\) and let \(P_0 h=Q^{-1}\sum_{w\in V}h(w)\) denote projection onto the constant functions on \(V\). For \(\eta\ne0\), define the orthogonal projectors
\[
P_\eta^\pm=\frac12\left(I\pm q^{-n}F_\eta\right).
\]
Given line data \(y=\mathcal Rf\), form \(b=\mathcal R^*y\). If \(n\ge2\), then
\[
\widehat f_0=\frac{P_0\widehat b_0}{c+Q}+\frac{(I-P_0)\widehat b_0}{c},
\qquad
\widehat f_\eta=\frac{P_\eta^+\widehat b_\eta}{c+q^n}+\frac{P_\eta^-\widehat b_\eta}{c-q^n}\quad(\eta\ne0).
\]
Recover \(f(z,t)=q^{-1}\sum_{\eta\in\mathbb F_q}\chi_\eta(t)\widehat f_\eta(z)\). When \(n=1\), omitting the term with denominator \(c-q^n=0\) instead gives the Moore–Penrose reconstruction of the component perpendicular to the kernel. No recovery claim is made for its invisible component.

## Verification

The accompanying `CHECK.py` separately constructs every distinct horizontal line in three small cases, builds the incidence matrix directly, checks all pairwise common-line multiplicities, compares the actual Gram eigenvalues against the complete table, and checks a nonzero rank-one null witness. Tested prime-field cases are \((q,n)=(3,1),(5,1),(3,2)\); the program checks **86,391 assertions** when run with a compatible NumPy installation. These finite computations supplement, but do not replace, the exact proof for every odd prime power and every \(n\ge1\). Execute with `python CHECK.py` after installing `requirements.txt`.

## Relationship to prior work

Pham, Pinamonti, Tran and Xue introduced and studied finite-Heisenberg horizontal-line Kakeya maximal operators, including refined-direction variants, in [1] and [2]. Their analysis selects or maximizes over lines indexed by directions and derives sharp growth exponents; it does not state the **normal-operator spectrum of the sum over every distinct horizontal line**, nor the injective-rank transition and exact inverse above. In particular, a maximal operator cannot be identified with the linear all-line analysis operator without a separate argument.

Kong and Tamo [3] compute singular spectra of a different point–variety incidence family consisting of graphs of coordinatewise polynomial expressions; that family is not the family of all horizontal Heisenberg lines. The present derivation independently uses common-line counts and a central symplectic Fourier involution. General character orthogonality and matrix spectral decomposition are standard tools and are not claimed as new. Earlier unindexed equivalent incidence-spectrum calculations remain a priority risk.

## Limitations

The result concerns **all distinct horizontal lines** with counting measures, **odd characteristic**, and the full ambient finite group, not sparse direction selections, characteristic two, arbitrary weights, or the nonlinear maximal operator. The finite-field proof is exact; the embedded numeric checks are limited to the three stated small prime-field cases. The general inverse holds only at ranks \(n\ge2\); at \(n=1\) only the observable projection is reconstructed. No noise-minimax property beyond the stated sharp Hilbert-space condition number is asserted. The literature comparison cannot exclude all unindexed prior work, and no independent mathematical audit has been performed.

## References

[1] T. Pham, A. Pinamonti, D. T. Tran, and B. Xue, *Horizontal Kakeya maximal operators in finite Heisenberg groups: Exact exponents and applications*, arXiv:2603.02111, first posted 2026-03-02; https://arxiv.org/abs/2603.02111.

[2] T. Pham, A. Pinamonti, D. T. Tran, and B. Xue, *Sharp refined-direction Kakeya estimates in finite Heisenberg groups*, arXiv:2608.14059, first posted 2026-08-14; https://arxiv.org/abs/2608.14059.

[3] X. Kong and I. Tamo, *A point-variety incidence theorem over finite fields, and its applications*, arXiv:2408.10977, first posted 2024-08-20; https://arxiv.org/abs/2408.10977.
