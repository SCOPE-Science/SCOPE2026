# A sharp reentrant persistence window in a three-patch advective stream

## Finding

In a closed three-patch stream with births restricted to the upstream patch, the effect of increasing symmetric migration is not necessarily monotone. For sufficiently strong downstream drift there is a *bounded interval of migration rates* in which the entire nonlinear population tends to zero, although it persists for both weaker and stronger migration. The sharp drift-to-mortality boundary is \(q/a=5/3\); two patches cannot exhibit this extinction–recovery sequence under the same assumptions.

## Assumptions and scope

Let \(a,q,d,r,c>0\). Write the population at upstream, middle, and downstream patches as \(u=(u_1,u_2,u_3)^T\ge0\). All patches have mortality \(a\) and strictly quadratic local crowding \(cu_i^2\). Only patch 1 has births, at low-density per-capita rate \(r\). Movement is conservative within the three patches, with no upstream or downstream boundary loss, and obeys

\[
\dot u=(dD+qQ-aI+rE_11)u-c(u_1^2,u_2^2,u_3^2)^T,
\]

\[
D=\begin{pmatrix}-1&1&0\\1&-2&1\\0&1&-1\end{pmatrix},\qquad
Q=\begin{pmatrix}-1&0&0\\1&-1&0\\0&1&0\end{pmatrix}.
\]

Both matrices have zero column sums. The diffusion rate \(d\) acts bidirectionally on adjacent links; \(q\) transports from patch 1 to 2 and patch 2 to 3. Let \(s(A)\) mean the largest real part among eigenvalues of the real matrix \(A\); for the irreducible Metzler matrix here it is a real, algebraically simple Perron eigenvalue.

Set

\[
R(d)=a\frac{a^2+4ad+2aq+3d^2+3dq+q^2}{a^2+3ad+aq+d^2}.
\]

The exact classification holds for every choice of strictly positive parameters and every nonzero nonnegative initial state:

- If \(r\le R(d)\), all three coordinates converge to zero.
- If \(r>R(d)\), there is exactly one strictly positive equilibrium and it attracts every nonzero nonnegative initial state.
- If \(q\le5a/3\), \(R(d)\) is strictly increasing on \(d>0\).
- If \(q>5a/3\), \(R(d)\) has exactly one strict interior maximum at the positive root of
  \[
  a^2(a+q)+2(a+q)(2a-q)d+(5a-3q)d^2=0.
  \]
  The maximum strictly exceeds both \(\lim_{d\downarrow0}R(d)=a+q\) and \(\lim_{d\to\infty}R(d)=3a\). For every \(r\) strictly between that maximum and the larger of these two endpoint values, ordered appropriately as
  \[
  \max\{a+q,3a\}<r<\max_{d>0}R(d),
  \]
  there are exactly two positive roots of \(R(d)=r\); persistence occurs below the first and above the second, extinction between them.

This last assertion concerns an *existence interval in the birth-rate parameter*, not every birth rate. At equality with either diffusion threshold, extinction occurs in the quadratic-crowding model.

## Proof

**1. Exact persistence frontier.** Let \(M=aI-dD-qQ\). Its negative is a Metzler matrix whose spectral bound is \(-a\): conservative irreducible movement has Perron root zero, and uniform mortality shifts every eigenvalue by \(-a\). Thus \(M\) is invertible and \(M^{-1}\) is nonnegative. Write \(A=-M+rE_{11}\). The Perron eigenvalue of \(A\) increases strictly with \(r\); its unique zero occurs when the determinant lemma gives \(1-r(M^{-1})_{11}=0\).

Direct determinants and cofactors yield

\[
\det M=a(a^2+4ad+2aq+3d^2+3dq+q^2),\qquad
\operatorname{cof}_{11}(M)=a^2+3ad+aq+d^2.
\]

Consequently the unique zero-eigenvalue birth rate is \(R(d)=1/(M^{-1})_{11}\), exactly as displayed. Strict Perron monotonicity implies \(s(A)>0\) exactly if \(r>R(d)\).

**2. From spectral sign to nonlinear fate.** The vector field is cooperative off the diagonal and strongly irreducible for \(d>0\), so every nonzero nonnegative state becomes strictly positive at positive times. If \(s(A)=\lambda\le0\), choose its strictly positive left Perron vector \(w\), normalized by \(\sum_i w_i=1\). Writing \(U=\sum_i w_i u_i\), we have

\[
\dot U=\lambda U-c\sum_i w_i u_i^2\le \lambda U-cU^2,
\]

where the last inequality is Jensen's inequality. Therefore \(U\to0\), hence each coordinate converges to zero.

If \(\lambda>0\), a small multiple of a positive right Perron eigenvector is a strict positive subsolution, and a sufficiently large constant vector is a supersolution because the quadratic losses dominate the linear terms. The cooperative comparison principle and finite-dimensional monotone iteration produce a positive equilibrium \(u^*\). It is unique: if \(v\) is another positive equilibrium and \(t=\max_i v_i/u_i^*>1\), then at an index attaining the maximum, the Metzler off-diagonal property gives \((Av)_i\le t(Au^*)_i=tc(u_i^*)^2\); but \(cv_i^2=ct^2(u_i^*)^2>tc(u_i^*)^2\), a contradiction. Exchanging \(v\) and \(u^*\) rules out distinct equilibria.

For global attraction, every positive initial state is sandwiched between \(k u^*\) and \(K u^*\) with \(0<k<1<K\). If \(m=\min_i u_i^*>0\), the scalar logistic equations \(\dot k=cmk(1-k)\) and \(\dot K=cmK(1-K)\) make \(ku^*\) a subsolution and \(Ku^*\) a supersolution. Both scalar factors converge to 1. Comparison proves \(u(t)\to u^*\) for every nonzero nonnegative initial state.

**3. Sharp turning-point law.** Differentiating the positive rational frontier gives

\[
R'(d)=\frac{a\left[a^2(a+q)+2(a+q)(2a-q)d+(5a-3q)d^2\right]}{(a^2+3ad+aq+d^2)^2}.
\]

If \(q\le5a/3\), all three polynomial coefficients are nonnegative and the constant and linear ones are strictly positive; hence \(R'>0\). If \(q>5a/3\), the quadratic's leading coefficient is negative and its constant is positive. The product of its two roots is negative, so there is exactly one positive root. The derivative is positive before that root and negative afterward. Thus the frontier has a unique strict maximum. Its endpoint limits are \(a+q\) and \(3a\); strict increase at small \(d\) and strict decrease toward the limit at large \(d\) show the maximum exceeds both. Horizontal lines in the stated open interval meet the frontier exactly twice, with the claimed signs of \(r-R(d)\).

**4. Minimum number of patches and exact witness.** On the analogous two-patch closed stream, the matrices are \(D_2=\begin{psmallmatrix}-1&1\\1&-1\end{psmallmatrix}\) and \(Q_2=\begin{psmallmatrix}-1&0\\1&0\end{psmallmatrix}\). The same determinant argument gives

\[
R_2(d)=a\frac{a+2d+q}{a+d},\qquad R_2'(d)=\frac{a(a-q)}{(a+d)^2},
\]

which is monotone or constant. A one-patch model has no migration. Three patches are therefore minimal in this model family.

For \((a,q,r)=(1,2,25/8)\) one obtains

\[
R(d)=\frac{3d^2+10d+9}{d^2+3d+3},\qquad
R(d)-\frac{25}{8}=\frac{-d^2+5d-3}{8(d^2+3d+3)}.
\]

The two roots are \((5-\sqrt{13})/2\) and \((5+\sqrt{13})/2\). The numerator is strictly positive between the roots and negative outside. The nonlinear system therefore becomes extinct precisely inside the closed interval between these rates, including the two neutral endpoints; it persists strictly outside. Here \(\max R(d)=2+2/\sqrt3\), attained at \(d=\sqrt3\).

## Verification

The standalone standard-library program `checker.py` independently reconstructs symbolic polynomials for the three-patch matrix, verifies the determinant/cofactor and derivative identities, checks the exact rational witness, and verifies two-patch monotonicity on supplementary rational parameter cases. Run it with `python3 checker.py`. Its finite checks do not replace the unrestricted proofs above. Critical mathematics is fully contained in this file; no external dataset, fitted coefficient or numerical eigenvalue is required.

## Relationship to prior work

The closed three-patch directed and undirected movement matrices are those described by Chen, Liu and Wu (2023, arXiv:2301.06640). Their investigated problem concerns a two-species competition model with positive intrinsic growth and heterogeneous carrying capacities, and its resident-invasion curves; the present exact birth-only-source, uniform-mortality nonlinear survival frontier is a different theorem. Chen, Liu and Wu (2023, arXiv:2301.06638) examine competition and spatially varying downstream drift with uniform intrinsic recruitment, rather than this rank-one birth localization. The earlier Karlin–Altenberg spectral monotonicity results, as developed by Chen et al. (arXiv:1911.02232), assume movement intensity multiplies the *whole* movement generator while the other term is diagonal. Varying \(d\) here keeps a separate nonzero drift generator \(qQ\) in the remainder, so that reduction principle does not imply monotonicity. Lutscher, Nisbet and Pachepsky (2010) give a persistence criterion for discrete-time drifting organisms with dispersal kernels; that study does not make the three-patch exact classification. The 2021 three-patch competition study by Jiang, Lam and Lou is a related historical source whose complete text was not available for comparison; its accessible abstract concerns competitive selection and network topology.

## Limitations

The three-patch model is a closed finite corridor with constant rates, identical background mortality and quadratic crowding, birth concentrated only at its upstream endpoint, and no age structure, immigration, stochasticity or seasonal forcing. Persistence means a positive deterministic equilibrium, not guaranteed persistence of a finite stochastic population. The critical ratio is **model-specific**, not a field-derived constant; no management claim follows. The nonlinear theorem requires \(d>0\), although its thresholds have the displayed \(d\downarrow0\) limits. Historical priority for the exact theorem is provisional, especially regarding inaccessible older competition literature and the broader matrix-spectral literature.

## References

1. S. Chen, J. Liu and Y. Wu, *On the impact of spatial heterogeneity and drift rate in a three-patch two-species Lotka-Volterra competition model over a stream*, first preprint 16 January 2023, https://arxiv.org/abs/2301.06640.
2. S. Chen, J. Liu and Y. Wu, *Evolution of dispersal in advective patchy environments with varying drift rates*, first preprint 16 January 2023, https://arxiv.org/abs/2301.06638.
3. S. Chen, J. Shi, Z. Shuai and Y. Wu, *Spectral Monotonicity of Perturbed Quasi-positive Matrices with Applications in Population Dynamics*, first preprint 6 November 2019, https://arxiv.org/abs/1911.02232.
4. H. Jiang, K.-Y. Lam and Y. Lou, *Three-patch Models for the Evolution of Dispersal in Advective Environments: Varying Drift and Network Topology*, Bull. Math. Biol. 83 (2021), article 109, https://doi.org/10.1007/s11538-021-00939-8.
5. F. Lutscher, R. M. Nisbet and E. Pachepsky, *Population persistence in the face of advection*, Theor. Ecol. 3 (2010), 271–284, https://doi.org/10.1007/s12080-009-0068-y.
