# Axial reducing shifts and the half-Schatten threshold in three pentablock Hardy spaces

## Finding

For each of the three canonical boundary-weight choices in the pentablock Hardy-space construction of Su and Tomar, the first-coordinate multiplier has a natural reducing one-variable summand. Although the three ambient Hardy norms are pairwise inequivalent, these summands are successive tails of the same explicit weighted shift. Their restricted self-commutators have a universal critical Schatten exponent of \(1/2\), and all three axial reproducing kernels have closed forms and the same boundary singularity exponent.

More precisely, let \(m\in\{0,1,2\}\). Define \(h_j=\binom{2j}{j}4^{-j}\) for integers \(j\geq0\), and let \(E_m\) be the closure of polynomials in the coordinate \(a\) alone in the corresponding Hardy space \(H_m\). Let \(S_m=M_a|_{E_m}\). Then \(E_m\) reduces the bounded multiplication operator \(M_a\), and \(S_m\) is a unilateral weighted shift with squared weights

\[
w_{m,k}^{2}=\frac{2(m+k)+1}{2(m+k)+2},\qquad k=0,1,\ldots.
\]

For \(D_m=S_m^*S_m-S_mS_m^*\), its complete nonzero diagonal eigenvalue sequence, in the natural normalized monomial basis, is

\[
d_{m,0}=\frac{2m+1}{2m+2},\qquad d_{m,k}=\frac{1}{2(m+k)(m+k+1)}\quad(k\geq1).
\]

Consequently \(D_m\in S_q\) if and only if \(q>1/2\) for every real \(q>0\); \(\operatorname{Tr}D_m=1\); and

\[
\lim_{t\downarrow0}\sqrt t\,\#\{k:d_{m,k}>t\}=\frac1{\sqrt2},\qquad
\lim_{N\to\infty}\frac1{\log N}\sum_{k=0}^{N-1}\sqrt{d_{m,k}}=\frac1{\sqrt2}.
\]

The axis \(L=\{(a,0,0):|a|<1\}\) has restricted reproducing kernel, for \(|a|,|b|<1\),

\[
K_m((a,0,0),(b,0,0))=\sum_{k=0}^{\infty}\frac{h_m}{h_{m+k}}(a\overline b)^k.
\]

In terms of the analytic function \(F(z)=\sum_{j\geq0}h_j^{-1}z^j\),

\[
F(z)=\frac1{1-z}+\frac{\sqrt z\,\arcsin\sqrt z}{(1-z)^{3/2}},\quad |z|<1,
\]

where the square-root/arcsine expression is interpreted by its analytic power series at \(z=0\), and

\[
K_m|_{L\times L}=\frac{h_m}{z^m}\left(F(z)-\sum_{j=0}^{m-1}\frac{z^j}{h_j}\right),\quad z=a\overline b,
\]

with a removable value at \(z=0\). Thus

\[
\lim_{r\uparrow1}(1-r^2)^{3/2}K_m((r,0,0),(r,0,0))=\frac\pi2 h_m.
\]

All operator statements here concern the **restricted** multiplier \(S_m\) on \(E_m\), not the full multiplier on \(H_m\).

## Assumptions and scope

Let \(\mathcal P\subset\mathbb C^3\) be the pentablock and use its distinguished-boundary parametrization

\[
\Psi(\xi,\lambda_1,\lambda_2)=\left(\frac{\xi(\lambda_1-\lambda_2)}2,\lambda_1+\lambda_2,\lambda_1\lambda_2\right),\quad (\xi,\lambda_1,\lambda_2)\in\mathbb T^3.
\]

Let \(dm_3\) be normalized Haar probability measure. Put \(t=|\lambda_1-\lambda_2|^2/4\). Since \(|J_\Psi|=2t\), the probability measures \(\mu_m=\Psi_*[(t^m/h_m)dm_3]\) are exactly the canonical unweighted, Jacobian-weighted, and Jacobian-squared-weighted measures for \(m=0,1,2\). Indeed \(h_0=1\), \(h_1=1/2\), and \(h_2=3/8\), so the multipliers for \(|J_\Psi|^m\) are respectively \(1\), \(1\), and \(2/3\). Define \(H_m=\overline{\mathbb C[a,s,p]}^{L^2(\mu_m)}\). These are the three Hardy spaces of the cited construction. For \(m=1,2\), this uses the corresponding holomorphic realizations described there. The analytic coordinate multiplier \(M_a\) is bounded, with \(\|M_a\|\leq1\), by the boundary norm.

The statements hold for each of the three listed values of \(m\), with no assertion about other weights, other coordinate multipliers, or the full space's self-commutator. The compact-operator Schatten ideal \(S_q\) is defined for every \(q>0\) by summability of the \(q\)-th powers of singular values, including quasi-norm exponents below one.

## Proof

**Step 1 (moments and orthogonality).** The difference angle between \(\lambda_1\) and \(\lambda_2\) is uniform, so

\[
\int_{\mathbb T^3}t^j\,dm_3
=\frac1{2\pi}\int_0^{2\pi}\sin^{2j}(\theta/2)\,d\theta
=\frac{\binom{2j}{j}}{4^j}=h_j
\]

for every integer \(j\geq0\). The \(\xi\)-Haar character makes distinct powers of \(a\) orthogonal. For integers \(k,u,v,w\geq0\), the inner product of \(a^k\) with \(a^u s^v p^w\) first vanishes unless \(u=k\). In that case, rotate \((\lambda_1,\lambda_2)\) simultaneously by a unimodular scalar. The factors \(t^m\) and \(|a|^{2k}\) remain invariant, while \(s^vp^w\) picks up degree \(v+2w\), so the inner product vanishes unless \(v=w=0\). This argument also holds for the normalized weighted measures, which share both torus symmetries. Thus

\[
\mathbb C[a,s,p]=\mathbb C[a]\oplus^{\perp}(s,p)\mathbb C[a,s,p]
\]

as a polynomial vector-space decomposition. Both summands are invariant under multiplication by \(a\). Taking closures shows \(E_m\) and its orthogonal complement are invariant, hence \(E_m\) reduces \(M_a\). The normalized moments are

\[
\|a^k\|_{H_m}^2=\int t^k\,d\mu_m=\frac{h_{m+k}}{h_m}.
\]

**Step 2 (shift model and tail equivalence).** The orthonormal basis \(e_{m,k}=a^k\sqrt{h_m/h_{m+k}}\) satisfies \(S_me_{m,k}=w_{m,k}e_{m,k+1}\), and

\[
\frac{h_{j+1}}{h_j}=\frac{2j+1}{2j+2}.
\]

For \(m=1,2\), the map \(a^k\mapsto a^{k+m}/\sqrt{h_m}\) is an isometry from \(E_m\) onto the closed invariant tail \(\overline{\operatorname{span}}\{a^j:j\geq m\}\subset E_0\), and it intertwines multiplication by \(a\). This identifies all three axial multiplier models. The tail in \(E_0\) is not claimed to reduce \(S_0\).

**Step 3 (self-commutator).** In the normalized basis, \(S_m^*S_m\) is diagonal with entries \(w_{m,k}^2\), while \(S_mS_m^*\) has entries \(0,w_{m,0}^2,w_{m,1}^2,\ldots\). The ratio above gives the displayed \(d_{m,k}\), all strictly positive. For \(k\geq1\), \(d_{m,k}\sim(2k^2)^{-1}\), proving \(D_m\in S_q\) exactly for \(2q>1\). The trace telescopes:

\[
\sum_{k=0}^{N}d_{m,k}=w_{m,N}^2\longrightarrow1.
\]

For the counting function, the tail condition \(1/[2(m+k)(m+k+1)]>t\) is equivalent to an interval condition \(m+k<(-1+\sqrt{1+2/t})/2\) up to a strict endpoint. Counting positive integers in this interval gives \(N_m(t)=(2t)^{-1/2}+O_m(1)\), proving the counting limit. Finally \(\sqrt{d_{m,k}}=(\sqrt2\,k)^{-1}+O_m(k^{-2})\), so harmonic summation gives the logarithmic limit. These are infinite-sequence arguments, not extrapolations from finite sampling.

**Step 4 (axial kernel).** Every polynomial in \((s,p)\mathbb C[a,s,p]\) vanishes on \(L\), hence so does its Hilbert-space closure by continuity of point evaluation. Therefore the full reproducing kernel at points of \(L\) is exactly the kernel of the orthogonal summand \(E_m\). Summing the normalized monomial basis yields the claimed series. Since \(h_j^{-1}=4^j/\binom{2j}{j}\), its coefficients satisfy

\[
(2j+1)h_{j+1}^{-1}=2(j+1)h_j^{-1}.
\]

Therefore the generating function \(F\) satisfies

\[
2z(1-z)F'(z)=(1+2z)F(z)-1,\qquad F(0)=1.
\]

The displayed arcsine expression has the same analytic initial condition and solves the differential equation on \(|z|<1\), so it equals \(F\) by power-series uniqueness. Reindexing gives the formula for \(K_m\). As \(z\uparrow1\), \(\sqrt z\arcsin\sqrt z\to\pi/2\) and the \((1-z)^{-3/2}\) term dominates the \((1-z)^{-1}\) term and finite reindexing corrections. This gives the sharp boundary constant.

## Verification

A standalone Python standard-library exact-rational checker, `pentablock_axial_check.py`, tests the central-binomial moment recurrences, weighted-shift ratios, self-commutator differences, telescoping identities, and first coefficients of the analytic kernel for \(m=0,1,2\). Its recorded execution was `PENTABLOCK_AXIAL_EXACT_CHECKS_OK 3723` (3,723 assertions); five floating-point comparisons of the kernel closed form are supplemental. The universal statements use the proofs above. Finite arithmetic does not certify the absence of all possible prior equivalent publications.

## Relationship to prior work

Su and Tomar [1] construct all three boundary Hardy spaces, establish their distinct norms, give weighted homogeneous and fibre decompositions, prove that the unweighted space is a reproducing kernel Hilbert space, and establish **joint** irreducibility of its coordinate multipliers. This result uses their boundary normalizations but computes a different, individual-operator invariant: an explicit common axial reducing model, its complete restricted self-commutator spectrum and sharp critical Schatten threshold, and the axial kernel's exact closed form and boundary asymptotics. A reducing space for the **single** multiplier \(M_a\) does not contradict irreducibility for the **joint** triple \((M_a,M_s,M_p)\). The formulas for a generic weighted shift after its weights are known are elementary; originality concerns the combined pentablock-specific identification and quantitative consequence, not that general operator formula. Pal and Tomar [2] study the Toeplitz corona problem on the pentablock through admissible kernels, not these three canonical axial models.

## Limitations

Only the axes \(L\), the restrictions of the first-coordinate multipliers to \(E_m\), and three specified measure weights are treated. No compactness or Schatten assertion is made for the full operator self-commutator \([M_a^*,M_a]\) on \(H_m\), or for the other coordinate multipliers. Generic weighted-shift spectral formulas and central-binomial identities are standard tools. Publication priority against every older source remains subject to independent literature scrutiny. No independent mathematical audit has been performed.

## References

[1] G. Su and N. Tomar, *Hardy Spaces and Toeplitz operators on the Pentablock*, arXiv:2610.17729, first posted 2026-10-13, https://arxiv.org/abs/2610.17729. In particular, Sections 2, 4 and 5.

[2] S. Pal and N. Tomar, *A Toeplitz corona theorem for the pentablock and applications*, arXiv:2606.00850, first posted 2026-05-30, https://arxiv.org/abs/2606.00850.
