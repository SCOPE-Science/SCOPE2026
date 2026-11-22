# A sharp circulation-controlled stability frontier in balanced two-stage ecological networks

## Finding
A two-stage ecological community can have **zero stage-aggregated interaction for every pair of species** while retaining a sharp, network-dependent local coexistence instability. In the balanced quadratic stage-structured population model below, every positive homogeneous equilibrium is linearly asymptotically stable exactly when, for every complex eigenvalue \(z=a+ib\) of the species-level coefficient matrix \(G\),
\[
\boxed{\quad b^2<\frac{(\Delta+1)^2(4\Delta+a^2)}{(\Delta+1)^2+a^2}.\quad}
\]
Here the fixed demographic exchange rate is \(\Delta>2\). If at least one eigenvalue violates this inequality strictly in the opposite direction, the equilibrium is linearly unstable. At equality, a linear eigenvalue is purely imaginary, with frequency \(-ab/(\Delta+1)\); zero frequency occurs when \(ab=0\). Thus the result classifies the complete finite-demography linear-stability region for arbitrary balanced, possibly nonnormal species networks.

In particular, if \(G\) is symmetric, coexistence is locally exponentially stable at **every interaction strength**. If \(G\) is skew-symmetric, coexistence is locally exponentially stable precisely when \(\|G\|_2<2\sqrt\Delta\), and is unstable when \(\|G\|_2>2\sqrt\Delta\). These statements use exactly the same stage-interaction mechanism and demographic parameters; their distinction comes from the reciprocity of the species-network coefficients.

An explicit **four-species minimum-size comparison** uses a balanced signed reciprocal cycle and a balanced circulating cycle having precisely the same underlying edges and the same absolute coefficients. The reciprocal cycle is stable for every \(g>0\), whereas the circulating cycle has the sharp threshold \(g=\sqrt\Delta\). With \(\Delta=9\) and \(g=4\), the reciprocal cycle has spectral abscissa \(-2\), while the circulating cycle has spectral abscissa \(-10+8\sqrt2>0\). No nonzero symmetric, zero-diagonal, row-balanced species matrix exists on fewer than four species. A different balanced directed four-cycle exhibits a strictly oscillatory boundary: at \(\Delta=9\) its leading pair crosses at \(g=\sqrt{60}\), with imaginary parts \(\pm6\). Four species are also the minimum size for this nonzero-frequency crossing within the balanced zero-diagonal class.

## Assumptions and scope
Fix an integer \(S\ge2\), a real matrix \(G=(g_{ij})\in\mathbb R^{S\times S}\) with \(g_{ii}=0\) and \(G\mathbf 1=0\), and a common rate \(\Delta>2\). For each species \(i\), write \(v_i=(u_i,w_i)^\mathsf T\) for its strictly positive first- and second-stage densities. Define
\[
 R=\begin{pmatrix}2-\Delta&\Delta\\\Delta&2-\Delta\end{pmatrix},\quad
 H=\begin{pmatrix}-1&-1\\-1&-1\end{pmatrix},\quad
 K=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]
The autonomous equations are, for every \(i=1,\ldots,S\),
\[
 \boxed{\quad \dot v_i=R v_i+\operatorname{diag}(v_i)\left(Hv_i+\sum_{j\ne i}g_{ij}K v_j\right).\quad}
\]
The two diagonal demographic entries \(2-\Delta\) are strictly negative; the two demographic conversion entries are strictly positive. The within-species density-dependent competition coefficients are all \(-1\). For each distinct pair \((i,j)\), the four stage-interaction coefficients are \((0,g_{ij},-g_{ij},0)\), so their sum is exactly zero. The coefficients \(g_{ij}\) are signed deterministic numbers; this is **not** asserted to be a sample from any random equicorrelation ensemble.

The row-balance hypothesis ensures that \(v_i^*=\mathbf1_2\) for all \(i\) is a strictly positive equilibrium. The vector field is polynomial; because both stage-conversion rates are positive, solutions starting in the strictly positive orthant remain positive on their maximal existence intervals. Every stability assertion here is local to this prescribed equilibrium; global existence for arbitrary initial states is not claimed in the unstable case.

For the four-species comparison, indices follow the cycle \(1-2-3-4-1\), and the two coefficient matrices, with \(g>0\), are
\[
 G_{\mathrm{rec}}=g\begin{pmatrix}0&1&0&-1\\1&0&-1&0\\0&-1&0&1\\-1&0&1&0\end{pmatrix},\qquad
 G_{\mathrm{circ}}=g\begin{pmatrix}0&1&0&-1\\-1&0&1&0\\0&-1&0&1\\1&0&-1&0\end{pmatrix}.
\]
Both matrices have zero diagonal and row sums, and identical entrywise absolute values. Their symmetric and skew-symmetric structures represent respectively reciprocal signed effects and circulating directed signed effects, with no change in edge strengths.

To exhibit a nonzero-frequency boundary, also consider the balanced directed circulant
\[
 G_{\mathrm{mix}}=g\begin{pmatrix}0&1&-1&0\\0&0&1&-1\\-1&0&0&1\\1&-1&0&0\end{pmatrix}.
\]
Its spectrum is \(\{0,-2g,g(1+i),g(1-i)\}\), so it has both a real and an imaginary component at its critical network mode.

## Proof
**1. Feasibility and exact Jacobian.** Since \(G\mathbf1=0\), for each species \(i\) one has \(R\mathbf1_2=2\mathbf1_2\), \(H\mathbf1_2=-2\mathbf1_2\), and \(\sum_{j\ne i}g_{ij}K\mathbf1_2=\mathbf0\), proving the claimed equilibrium. The derivative of \(\operatorname{diag}(v_i)Hv_i\) at \(v_i=\mathbf1_2\) is \(H+\operatorname{diag}(H\mathbf1_2)=H-2I_2\). The off-species diagonal derivatives vanish because their row sums cancel. Consequently, the \(2\times2\) diagonal blocks of the full Jacobian are
\[
 J_{ii}=\begin{pmatrix}-1-\Delta&\Delta-1\\\Delta-1&-1-\Delta\end{pmatrix},
\]
and the off-diagonal blocks are exactly \(J_{ij}=g_{ij}K\).

**2. Mean-versus-stage-contrast reduction.** Apply the orthogonal basis vectors \(2^{-1/2}(1,1)^\mathsf T\) and \(2^{-1/2}(1,-1)^\mathsf T\) to each species, and group the species-total variables before the stage-contrast variables. Since
\[
 \begin{pmatrix}1&1\\1&-1\end{pmatrix}^{-1}K
 \begin{pmatrix}1&1\\1&-1\end{pmatrix}
 =\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
the Jacobian is orthogonally similar to
\[
\boxed{\quad \mathcal J=\begin{pmatrix}-2I_S&-G\\G&-2\Delta I_S\end{pmatrix}.\quad}
\]
For every complex spectral parameter \(\lambda\), the block-determinant identity (first away from the finitely many exceptional values, then by polynomial identity) yields
\[
 \det(\lambda I_{2S}-\mathcal J)
 =\det\left((\lambda+2)(\lambda+2\Delta)I_S+G^2\right).
\]
It follows without any diagonalizability assumption on \(G\) that the eigenvalues of \(\mathcal J\), with algebraic multiplicity, are the roots of
\[
 (\lambda+2)(\lambda+2\Delta)+z^2=0,\qquad z\in\sigma(G),
\]
namely \(\lambda_\pm(z)=-(1+\Delta)\pm\sqrt{(\Delta-1)^2-z^2}\). This polynomial factorization remains valid for defective species matrices.

**3. Exact complex spectral frontier.** Put \(z=a+ib\), \(s=1+\Delta>0\), and \(q=(\Delta-1)^2-z^2=p+it\), where \(p=(\Delta-1)^2-a^2+b^2\) and \(t=-2ab\). For either complex square-root branch, the larger of the two real parts is
\[
 -s+\sqrt{\frac{\sqrt{p^2+t^2}+p}{2}}.
\]
Therefore both roots have negative real part precisely when \(\sqrt{p^2+t^2}<2s^2-p\). The latter inequality is equivalent to
\[
 s^2(4\Delta+a^2)>(s^2+a^2)b^2.
\]
To verify equivalence even at the squaring step, observe that the displayed strict quadratic inequality implies \(b^2<s^2\), because \(4\Delta\le s^2\). Thus \(2s^2-p>0\), and squaring is reversible. Conversely stability implies the first strict inequality and therefore the displayed quadratic inequality. Equality gives the stated imaginary-axis contact. At contact the purely imaginary eigenvalue is \(\lambda=-iab/(1+\Delta)\), obtained by equating the imaginary parts of the quadratic characteristic equation. Strict reversal supplies positive real part. Taking this condition over all eigenvalues of \(G\) proves the complete criterion.

**4. Reciprocal and circulating cases.** For real symmetric \(G\), every spectral value \(z\) is real, so the condition is automatic. For real skew-symmetric \(G\), all spectral values are purely imaginary, and the strict condition is \(\max_{z\in\sigma(G)}|\Im z|<2\sqrt\Delta\). Skew-symmetric matrices are normal, so this maximum is their operator two-norm. At equality the linearization has a zero eigenvalue; no claim is made about nonlinear stability on this boundary.

**5. Matched cycle witness and minimality.** Direct calculation gives \(\sigma(G_{\mathrm{rec}})=\{-2g,0,0,2g\}\) and \(\sigma(G_{\mathrm{circ}})=\{-2ig,0,0,2ig\}\), including multiplicities. Their characteristic polynomials are respectively
\[
 [ (\lambda+2)(\lambda+2\Delta)]^2
 [ (\lambda+2)(\lambda+2\Delta)+4g^2]^2
\]
and
\[
 [ (\lambda+2)(\lambda+2\Delta)]^2
 [ (\lambda+2)(\lambda+2\Delta)-4g^2]^2.
\]
The sharp threshold and the stated \(\Delta=9\), \(g=4\) numbers follow immediately. For \(S=2\), a symmetric zero-diagonal matrix with zero row sums is zero. For \(S=3\), writing its off-diagonal entries as \(a,b,c\) gives \(a+b=a+c=b+c=0\), hence \(a=b=c=0\). The displayed four-species reciprocal matrix is nonzero; therefore four species are the minimum possible for a balanced nontrivial reciprocal/circulating comparison of this kind.
For the additional directed circulant, the two nonreal eigenvalues have \(a^2=b^2=g^2\). The general stability inequality becomes \(g^4<4\Delta(\Delta+1)^2\). Therefore at \(\Delta=9\) the unique positive stability crossing is \(g=\sqrt{60}\), and its imaginary-axis pair is \(\lambda=\pm6i\). For fewer than four species, any real, zero-diagonal, row-balanced \(G\) has eigenvalue zero and trace zero; its at most two remaining eigenvalues are either real opposites or purely imaginary opposites. Thus \(ab=0\) for every eigenvalue on such a network, so a nonzero-frequency contact is impossible. The directed four-cycle proves sharpness of this minimum.

## Verification
The independent-of-proof, standalone Python checker `check_stage_circulation.py` uses SymPy and NumPy. It directly constructs the original nonlinear system's Jacobian, verifies the orthogonal sum/contrast transformation, symbolically factors the complete two cycle characteristic polynomials, checks positive-equilibrium balance and identical absolute edge weights, and compares exact spectral predictions with direct numerical eigensolutions. It also verifies the full spectral inequality for hundreds of nonnormal, random zero-row-sum deterministic matrices. Run `python check_stage_circulation.py` in an environment with Python 3, NumPy and SymPy. These finite tests corroborate algebra; the infinite-size-in-\(S\) matrix assertion is proved by the general determinant identity and square-root argument, not by random sampling.

For the exact matched-network witness \(\Delta=9\), \(g=4\), direct eigenvalue computation gives spectral abscissa \(-2\) for the reciprocal network and \(-10+8\sqrt2=1.3137084989\ldots\) for the circulating network. The critical circulating value is \(g=3\), where the leading eigenvalue is zero. For the directed mixed-mode cycle at \(\Delta=9\), direct spectral evaluation verifies the nonzero-frequency contact at \(g=\sqrt{60}\).

## Relationship to prior work
Garmire and O'Dwyer (2026) develop the two-stage generalized Lotka–Volterra framework, analyze stage-correlated random interactions, and derive a large-demography, large-community May-style stability threshold. Their paper discusses finite demographic speeds and does not provide the present exact finite-\(S\), finite-\(\Delta\), all-matrix spectral region or the matched-strength reciprocal/circulating contrast. This result is a **deterministic** complementary-stage specialization; the zero sum of each stage block is not a claim that the deterministic matrices are samples from the paper's extreme random-correlation ensemble.

Giménez-Romero and coauthors (2025) give a general structured community matrix and simulation-based stability comparisons among interaction types. Their framework encompasses the *method* of computing a structured Jacobian, but their examined random interaction families do not state the all-network rational spectral frontier, the exact maturation-versus-circulation threshold, or the four-species minimal balanced comparison.

Published work on supercritical oscillations from zero-aggregate stage interactions establishes a different two-species nonlinear Hopf mechanism and does not imply the arbitrary-network spectral criterion or the stationary circulating threshold here. A published global-entropy result for balanced skew ecological interactions supplies a stronger stability conclusion in a different dissipative sign structure: the reciprocal, globally skew subcase here is consistent with that antecedent, and **unconditional reciprocal stability by itself is not claimed as new**. Classical Schur complements, spectral mapping, and Hermitian/skew-Hermitian matrix theory are also prior tools; originality is restricted to their complete sharp interpretation for the specified two-stage ecological network and the minimal matched-network contrast.

## Limitations
The conclusions are local linear-stability statements at the homogeneous positive equilibrium, not global persistence, bifurcation existence beyond linear imaginary-axis contact, or stability of other equilibria. A zero real-part eigenvalue does not establish stability, instability, or a nonlinear bifurcation at equality. The model uses equal maturation and reproduction exchange, uniform within-species competition and a restrictive complementary signed interaction matrix. It is not an empirical prediction and makes no assertion about typical random networks. Earlier matrix-theory treatments could contain a formally equivalent block-system theorem; such a theorem would limit historical priority despite the applied-network formulation. Independent scientific review has not been performed.

## References
1. Grace Garmire and James P. O'Dwyer, *Heterogeneity among and competition between life stages together extend the stability boundary of complex ecological communities*, arXiv:2610.23557v1, initially public 2026-10-16. https://arxiv.org/abs/2610.23557
2. Àlex Giménez-Romero, Christina Hernández, Meritxell Genovart, Roberto Salguero Gómez, *Population Structure Plays a Key Role in Community Stability*, Ecology Letters 28 (2025), e70272. https://doi.org/10.1111/ele.70272
3. Anju Susan Anish, Bernard De Baets, Shodhan Rao, *Metapopulation models with anti-symmetric Lotka–Volterra systems*, Journal of Biological Dynamics 18 (2024), 2397404. https://doi.org/10.1080/17513758.2024.2397404
4. *Supercritical oscillations from zero-mean stage interactions in a two-species community* (2026), public research note. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-supercritical-oscillations-from-zero-mean-stage-interactions-in--2f73bdd1134a
5. *Uniform global entropy decay under arbitrarily switching stage-antagonistic ecological interactions* (2026), public research note. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-uniform-global-entropy-decay-under-arbitrarily-switching-stage-a--14bce1e25823
