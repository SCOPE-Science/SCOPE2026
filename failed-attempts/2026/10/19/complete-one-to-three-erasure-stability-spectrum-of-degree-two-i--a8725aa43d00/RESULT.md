# Complete one-to-three erasure stability spectrum of degree-two icosahedral harmonic sampling

## Finding

Let \(X\) be the twelve vertices of a regular icosahedron normalized to the unit sphere. The probability-normalized space \(\mathcal H_{\le 2}\) of spherical harmonics of degrees \(0,1,2\) has dimension nine. For any set \(E\subset X\), define the retained sampling map by \((T_E f)(x)=f(x)/\sqrt{12}\) for \(x\in X\setminus E\). In particular the sample weights remain \(1/12\), not \(1/(12-|E|)\). All squared singular values below are listed with multiplicity, including zeros among the nine domain eigenvalues. Put \(c=1/\sqrt5\).

| Erasures | Number of masks | Squared singular values of \(T_E\) |
|---|---:|---|
| None | 1 | \(1\) (9 times) |
| One point | 12 | \(1\) (8), \(1/4\) (1) |
| Opposite pair | 6 | \(1\) (7), \(1/2\) (1), \(0\) (1) |
| Nonopposite pair | 60 | \(1\) (7), \((1+c)/4\) (1), \((1-c)/4\) (1) |
| Three including an opposite pair | 60 | \(1\) (6), \((3+\sqrt{13/5})/8\) (1), \((3-\sqrt{13/5})/8\) (1), \(0\) (1) |
| Three nonopposite, positive product | 80 | \(1\) (6), \((1-2c)/4\) (1), \((1+c)/4\) (2) |
| Three nonopposite, negative product | 80 | \(1\) (6), \((1+2c)/4\) (1), \((1-c)/4\) (2) |

For a three-point set \(E=\{x,y,z\}\) containing no opposite pair, the *product sign* is the sign of \((x\cdot y)(y\cdot z)(z\cdot x)\); no factor vanishes. The sampling operator is injective for three erasures **exactly if no opposite pair is erased**. Among injective three-erasure patterns the largest spectral condition number is exactly
\[
\kappa_{\rm worst}=\frac{2}{\sqrt{1-2/\sqrt5}},
\]
attained by all and only the 80 positive-product patterns. Every pattern of four or more erasures fails injectivity for dimension reasons, regardless of geometry.

## Assumptions and scope

All functions and singular values use complex scalars. Equip \(S^2\) with rotation-invariant probability measure and \(\mathcal H_{\le2}\) with the induced \(L^2\) norm. Equip a retained sample vector with its ordinary Euclidean norm. The geometry is invariant under rotations. A representative configuration is given by all independent sign choices in
\[
(0,\pm1,\pm\varphi),\qquad(\pm1,\pm\varphi,0),\qquad(\pm\varphi,0,\pm1),\quad
\varphi=(1+\sqrt5)/2,
\]
scaled by \(1/\sqrt{1+\varphi^2}\). The statement treats *unweighted deletion* from equal-probability icosahedral samples, not arbitrary replacement weights or higher harmonic degrees. The condition number refers to the largest divided by smallest **positive** singular value only for injective masks.

## Proof

**The original sampler is an isometry.** The equal-weight icosahedron is a spherical 5-design; for completeness this follows directly by averaging coordinate monomials of total degree at most five over the displayed vertex set, using antipodality for odd degrees and the even spherical moments. Products of harmonics of degrees at most two have degree at most four. Therefore \(T_\varnothing^*T_\varnothing=I_9\). With the degree-two addition kernel
\[
K_2(t)=1+3t+5P_2(t)=1+3t+\frac52(3t^2-1),
\]
the \(12\)-by-\(12\) orthogonal projection \(P=T_\varnothing T_\varnothing^*\) has entries \(P_{xy}=K_2(x\cdot y)/12\). Define the complementary projection \(Q=I_{12}-P\), of rank three. The icosahedron has scalar products \(1,-1,\pm c\). Evaluating the kernel gives
\[
Q_{xx}=\frac14,\qquad Q_{x,-x}=-\frac14,\qquad
Q_{xy}=-\frac{x\cdot y}{4}\quad (y\ne\pm x).
\]

**The deleted minor controls all nontrivial singular values.** For an erasure set \(E\) of size \(r\le3\), let \(A\) be the \(r\)-by-9 rows of the isometry corresponding to \(E\). Then \(T_E^*T_E=I_9-A^*A\). Its spectrum is \(9-r\) copies of \(1\), together with the eigenvalues of \(I_r-AA^*\). But \(AA^*=P_{E,E}\), so the latter is precisely the principal minor \(Q_{E,E}\). For \(r=1\), the minor equals \(1/4\). For \(r=2\) its eigenvalues are \((1\pm1)/4\) for opposite points and \((1\pm c)/4\) otherwise, proving the first four rows.

**Three-point minors.** If \(E=\{x,-x,z\}\), the two rows indexed by \(x,-x\) have opposite correlations with \(z\), so \((1,1,0)\) is in the nullspace of \(Q_{E,E}\). On its perpendicular complement the matrix is unitarily equivalent to
\[
\frac14\begin{pmatrix}2&\sqrt2c\\\sqrt2c&1\end{pmatrix},
\]
giving the nonzero eigenvalues \((3\pm\sqrt{1+8c^2})/8=(3\pm\sqrt{13/5})/8\). For a triple with no opposite pair, signed diagonal conjugation makes \(Q_{E,E}\) equal to either \(((1+c)I_3-cJ_3)/4\) when the product sign is positive, or \(((1-c)I_3+cJ_3)/4\) when negative. The matrices have the eigenvalues listed in the table. Since \(0<2c<1\), both nonantipodal classes are invertible, and the positive class has the smallest lower eigenvalue.

**Number of patterns.** There are six antipodal pairs, hence six opposite two-masks and \(\binom{12}{2}-6=60\) other pairs. A three-mask containing an opposite pair is uniquely determined by the pair and a third vertex, so there are \(6\cdot10=60\) such masks. The remaining \(\binom{12}{3}-60=160\) choose three different axes among the six opposite pairs; there are \(\binom63=20\) axis triples with eight sign lifts each. The sign of the pair-product is invariant under each of the eight sign lifts. Exactly ten axis triples admit three mutually adjacent representatives: these are the opposite pairs among the 20 triangular faces of the icosahedron. Such a triple has positive pair-product. Any positive-product axis triple has representatives with all three positive inner products (choose signs successively), hence its representatives form a face; thus there are precisely ten positive and ten negative axis triples. This yields \(80\) masks of each sign.

**Conditioning and exhaustion.** For every injective nonempty deletion pattern in the table, the largest squared singular value stays \(1\). The smallest squared singular value among the injective three-masks is \((1-2c)/4\), which proves the exact worst-case conditioning and equality class. Four erasures leave at most eight samples for nine harmonic coefficients, so injectivity is impossible; larger erasures are likewise impossible. This completes the full recovery/instability classification for up to three losses.

## Verification

The accompanying `icosa_erasure_check.py` constructs all 12 vertices using exact algebraic numbers, checks their spherical moments through degree five, verifies the rank-nine addition-kernel projection and rank-three complementary projection, tests every one-point and two-point minor, and exhaustively checks the trace, quadratic trace and determinant of all \(\binom{12}{3}=220\) three-point minors. The exact output is `all exact checks passed`. Run with `python icosa_erasure_check.py` after installing the public SymPy package. Exhaustive computation verifies the finite configuration; the analytic reduction and the proof of the 80/80 counts above explain why those computations are exhaustive rather than numerical guesses.

## Relationship to prior work

The spherical design sampling identity, addition kernel, and projection-complement duality are established general mechanisms, not claimed here as new. Hitchin's work analyzes the icosahedron in relation to harmonic cubics; its geometry includes the six antipodal vertex axes and the twenty faces, but its theorems address cubic nodal sets rather than robustness of degree-two harmonic interpolation under erasures. General irregular spherical sampling and antipodally symmetric spherical transforms study different reconstruction regimes. A later general finite-defect study derives a Naimark coupling for spherical designs; that broad mechanism is consistent with the projection identity used here. The specific output claimed here is the complete, exact **mask-level erasure spectrum, count, and sharp stability geometry** for the critical nine-mode icosahedral sampler, not the general complement identity.

## Limitations

The theorem concerns the fixed icosahedron and exactly degree-zero-to-two harmonic sampling; it does not establish sharp sampling under reweighting, perturbation of sites, or other polyhedra. The literature comparison could not include the full text of every relevant recent finite-defect manuscript, which remains an originality risk. Equality and stability statements are exact for the stated probability normalization; rescaling retained weights changes absolute singular values. No independent audit is claimed.

## References

- N. Hitchin, *Spherical harmonics and the icosahedron*, arXiv:0706.0088 (first posted 2007-06-01), especially Sections 1–3 (vertex coordinates, antipodal axes and faces). https://arxiv.org/abs/0706.0088
- A. P. Bates, Z. Khalid, R. A. Kennedy, *An Optimal Dimensionality Sampling Scheme on the Sphere for Antipodal Signals in Diffusion Magnetic Resonance Imaging*, arXiv:1502.07099 (2015); a different antipodally symmetric spherical-sampling setting. https://arxiv.org/abs/1502.07099
- K. Ivanov and P. Petrushev, *Irregular sampling of band-limited functions on the sphere*, Applied and Computational Harmonic Analysis 37 (2014), 545–562, DOI: 10.1016/j.acha.2014.05.001; general irregular-sampling reconstruction.
- S. Singh and V. Singh, *Finite-Defect Rigidity and the Minimum Spherical 4-Design on the Two-Sphere*, arXiv:2609.31689 (2026); abstract reports a general Naimark complement and spherical-design coupling. https://arxiv.org/abs/2609.31689
