# Sharp norm-equivalence constants for root-of-unity Dirichlet and de Branges–Rovnyak spaces

## Finding
For every integer \(m\ge 1\), let \(b_m(z)=(1+z^m)/2\), let \(\mathcal H(b_m)\) be the de Branges–Rovnyak space with its canonical reproducing-kernel norm, and let \(\mu_m=m^{-1}\sum_{\zeta^m=1}\delta_\zeta\). Equip the harmonically weighted Dirichlet space \(\mathcal D(\mu_m)\) with its canonical squared norm \(\|f\|_{H^2}^2+\int_{\mathbb T}\|(f-f(\zeta))/(z-\zeta)\|_{H^2}^2\,d\mu_m(\zeta)\). Then these two spaces coincide as sets, and the following two-sided comparison is sharp:
\[
L_m\|f\|_{\mathcal H(b_m)}^2\le\|f\|_{\mathcal D(\mu_m)}^2\le U_m\|f\|_{\mathcal H(b_m)}^2\quad(f\in\mathcal H(b_m)),
\]
where
\[
L_m=\frac{m+2-\sqrt{m^2+4}}4,\qquad
U_m=\begin{cases}5/4,&m=1,\\[2mm]
\dfrac{m+2+\sqrt{(m-2)^2+4}}4,&m\ge2.
\end{cases}
\]
The lower bound is attained by a nonzero multiple of \(f_-(z)=(1-q_-z^m)^{-1}\), with \(q_-=(\sqrt{m^2+4}-m)/2\in(0,1)\). For \(m\ge3\), the upper bound is attained by nonzero multiples of \(f_+(z)=z^{m-1}(1-q_+z^m)^{-1}\), where \(q_+=(m-2-\sqrt{(m-2)^2+4})/2\in(-1,0)\). For \(m=1,2\), the upper bound is not attained by a nonzero function. In particular, the optimal norm-equivalence distortion is \(\sqrt{U_m/L_m}\sim\sqrt m\) as \(m\to\infty\).

## Assumptions and scope
The Hardy space \(H^2\) has norm \(\|\sum_{j\ge0}c_jz^j\|_{H^2}^2=\sum_{j\ge0}|c_j|^2\). The de Branges–Rovnyak kernel is \(k^{b_m}(z,w)=(1-b_m(z)\overline{b_m(w)})/(1-z\overline w)\), with its canonical Hilbert norm. The Dirichlet norm uses *probability* measure \(\mu_m\), not the counting measure, and the local difference quotient convention \(Q_\zeta f=(f(z)-f(\zeta))/(z-\zeta)\). For polynomials all boundary evaluations are classical; general assertions follow by completion. All comparisons concern the squares of the norms and allow complex coefficients. No equality of these two norm structures is claimed.

## Proof
**1. The coefficient identities.** The Pythagorean mate of \(b_m\) is the outer polynomial \(a_m=(1-z^m)/2\), because \(|a_m|^2+|b_m|^2=1\) on \(\mathbb T\). The standard non-extreme de Branges–Rovnyak norm formula is \(\|f\|_{\mathcal H(b_m)}^2=\|f\|_{H^2}^2+\|f^+\|_{H^2}^2\), where \(T_{\overline{a_m}}f^+=T_{\overline{b_m}}f\). For a polynomial this relation is \((I-S^{*m})f^+=(I+S^{*m})f\), hence \(f^+=f+2\sum_{\ell\ge1}S^{*m\ell}f\), with only finitely many nonzero terms.

Split a polynomial into its \(m\) residue components \(f(z)=\sum_{r=0}^{m-1}z^r\sum_{j\ge0}c_{r,j}z^{mj}\), and set \(t_{r,j}=\sum_{k\ge j}c_{r,k}\) (eventually zero). The coefficient of \(z^{r+mj}\) in \(f^+\) equals \(t_{r,j}+t_{r,j+1}\), whereas the coefficient in \(f\) is \(t_{r,j}-t_{r,j+1}\). Consequently,
\[
\|f\|_{\mathcal H(b_m)}^2
=\sum_{r=0}^{m-1}\left(2|t_{r,0}|^2+4\sum_{j\ge1}|t_{r,j}|^2\right).\tag{1}
\]
For nonnegative integers \(p,q\), the polarization of the local Dirichlet identity gives
\[\langle Q_\zeta z^p,Q_\zeta z^q\rangle_{H^2}=\min(p,q)\,\zeta^{p-q}\]
(up to the immaterial order of conjugation). The root-of-unity average annihilates different residue classes. For \(p=r+mi\) and \(q=r+mj\), the averaged Dirichlet Gram contribution is \(r+m\min(i,j)\). Using \(\min(i,j)=\sum_{k\ge1}\mathbf1_{i\ge k}\mathbf1_{j\ge k}\), it follows that
\[
\|f\|_{\mathcal D(\mu_m)}^2
=\sum_{r=0}^{m-1}\left(r|t_{r,0}|^2+m\sum_{j\ge1}|t_{r,j}|^2+\sum_{j\ge0}|t_{r,j}-t_{r,j+1}|^2\right).\tag{2}
\]
Formulae (1)–(2) show directly that both completions have the same vectors: in each residue component, both norms are equivalent to the \(\ell^2\)-norm of the tail sequence \((t_{r,j})_{j\ge0}\). Polynomials are dense for the non-extreme \(b_m\), and for finitely atomic \(\mu_m\), so the identities extend from polynomial cores to the full spaces.

**2. A half-line Jacobi spectral problem.** In one residue \(r\), let \(W=\operatorname{diag}(2,4,4,\ldots)\). Relative to the quadratic form (1), (2) is represented by \(W^{-1/2}D_rW^{-1/2}\), where \(D_r\) is tridiagonal with diagonal \((r+1,m+2,m+2,\ldots)\) and nearest-neighbor entries \(-1\). This self-adjoint half-line Jacobi operator has essential spectrum \([m/4,(m+4)/4]\): away from its first row it equals the constant-coefficient Jacobi matrix with diagonal \((m+2)/4\) and off-diagonal \(-1/4\), and the boundary changes are finite rank.

An eigenvalue outside the band has a unique square-summable solution to the interior recurrence of the form \(t_j=Cq^j\), \(|q|<1\). Substituting into the recurrence and boundary equation yields
\[
4\lambda=m+2-q-q^{-1},\qquad 2\lambda=r+1-q,
\qquad q-q^{-1}=2r-m.\tag{3}
\]
If \(2r<m\), exactly one root \(q\in(0,1)\) gives one eigenvalue below the band; if \(2r>m\), exactly one root \(q\in(-1,0)\) gives one eigenvalue above the band; for \(2r=m\), there is no out-of-band eigenvalue. The second-order recurrence excludes additional eigenvalues outside the band. Band endpoints belong to the spectrum but have no square-summable eigenvectors.

**3. Global extrema, optimality, and attainment.** For every fixed tail vector, the \(r\)-dependent quadratic form (2) increases by \(r|t_0|^2\), while (1) is independent of \(r\). Therefore the smallest possible Rayleigh quotient over all residue classes is in \(r=0\), and the largest is in \(r=m-1\). Solving (3) for \(r=0\) gives the positive root \(q_-\) above and the isolated spectral minimum \(L_m\). At \(r=m-1\), an isolated upper eigenvalue occurs precisely when \(m\ge3\), yielding \(q_+\) and \(U_m\). For \(m=2\), the upper root is \(q=-1\), a non-square-summable band-edge solution, and \(U_2=3/2\). For \(m=1\), the sole residue has a lower outlier but no upper outlier, so \(U_1=(1+4)/4=5/4\).

The squared-norm constants are sharp by the spectral theorem. For each isolated edge, the \(\ell^2\) tail \(t_j=q^j\) corresponds to coefficients \(c_j=(1-q)q^j\), hence the stated rational extremizer. At a band endpoint, arbitrarily long truncated near-alternating tails give Rayleigh quotients tending to the top but no \(\ell^2\) eigenvector. The asymptotic expansions \(L_m=1/2-1/(2m)+O(m^{-3})\) and \(U_m=m/2+O(m^{-1})\) yield the distortion \(\sqrt{U_m/L_m}\sim\sqrt m\).

## Verification
`CHECK.py` independently constructs the polynomial Gram matrices from both defining formulas: the de Branges–Rovnyak plus-function Toeplitz relation and the Dirichlet difference-quotient root average. It checks exact coefficient identities and compares finite-section generalized spectra against the proved sharp bounds. Finite sections approximate the spectral endpoints; they are not used to infer infinite-dimensional sharpness. The recurrence calculation (3), including the \(m=1,2\) nonattainment cases, supplies that infinite-dimensional argument. Run `python CHECK.py` with the versions described in `requirements.txt`.

## Relationship to prior work
The 2026 characterization by Bellavita, Dellepiane and Luo (arXiv:2610.36943, Theorem 1.3 and Corollary 5.3) establishes set equality for general admissible de Branges–Rovnyak/Dirichlet pairs, including the inner-function class \(b=(1+u)/2\). Earlier results of Costara–Ransford (2013) and Dellepiane–Peloso–Tabacco (arXiv:2505.16572, 2025) cover finitely atomic equality of sets with *some* equivalent norm. Those set-equality statements are **not** claimed as new. The present finding computes *optimal canonical squared-norm comparison constants*, the precise attainment regime, and their large-\(m\) distortion for a symmetric canonical finite-Clark family. The 2026 paper's proof invokes Corona and potential estimates, not the exact half-line Jacobi comparison (1)–(3).

## Limitations
The calculation uses equal-mass atoms at all \(m\)-th roots of unity and the specific normalized symbol \(b_m=(1+z^m)/2\). Changing atom masses or replacing the inner function by an arbitrary finite Blaschke product changes the comparison operator. No uniform norm equivalence in \(m\) is claimed; indeed the optimal distortion diverges. The full literature may contain an equivalent spectral comparison under different terminology; independent publication-priority verification has not been performed.

## References
1. C. Bellavita, E. Dellepiane, S. Luo, *A characterization of equality between de Branges–Rovnyak and Dirichlet spaces*, arXiv:2610.36943, first posted 2026-10-27, especially Theorem 1.3 and Corollary 5.3. https://arxiv.org/abs/2610.36943
2. E. Dellepiane, M. M. Peloso, A. Tabacco, *On the equality of De Branges-Rovnyak and Dirichlet spaces*, arXiv:2505.16572, first posted 2025-05-22, especially the finite-atomic characterization. https://arxiv.org/html/2505.16572v2
3. C. Costara, T. Ransford, *Which de Branges–Rovnyak spaces are Dirichlet spaces (and vice versa)?*, J. Funct. Anal. 265 (2013), 3204–3218. DOI:10.1016/j.jfa.2013.08.015 (bibliographic context; full text not inspected).
4. C. Bellavita, E. Dellepiane, *Embedding model and de Branges–Rovnyak spaces in Dirichlet spaces*, Complex Variables and Elliptic Equations 70 (2025), 228–246; first online 2024-01-03. DOI:10.1080/17476933.2023.2298837 (abstract inspected).

5. T. Ransford, *On the coefficient formula for de Branges–Rovnyak norms*, arXiv:2605.30114, first posted 2026-05-28 (abstract and coefficient identity inspected). https://arxiv.org/abs/2605.30114
