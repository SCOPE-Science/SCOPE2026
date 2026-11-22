# Local rigidity, exceptional flats, and weighted ascent for simplex-midpoint Parseval frames

## Finding
For every integer \(m\ge4\), let \(N=\binom{m+1}{2}\), index the coordinates of \(\mathbb R^N\) by edges of the complete graph on \(m+1\) vertices, and let \(P_0\) be the rank-\(m\) orthogonal Gram projection of the regular-simplex edge-midpoint Parseval frame. For a rank-\(m\) orthogonal projection \(P\), define the equal-weight and optimally weighted frame objectives
\[
F(P)=\frac1N\sum_{e,f}|P_{ef}|,\qquad L(P)=\max_{t\in\mathbb R^N_{\ge0},\ \|t\|_2=1}\sum_{e,f}t_et_f|P_{ef}|.
\]
Write \(C\) for the projection onto the constant edge vector, \(E=\operatorname{ran}P_0\), \(W=(E\oplus\operatorname{ran}C)^\perp\), and \(P_W\) for projection onto \(W\). In the open neighborhood of \(P_0\) where every entry of \(P\) retains the sign of the corresponding entry of \(P_0\), there is an **exact identity**:
\[
\boxed{F(P_0)-F(P)=\frac{(m-4)(m+1)}{2N}\operatorname{tr}(PC)+\frac{2(m-1)}N\operatorname{tr}(PP_W).}\tag{1}
\]
In particular, for every \(m\ge5\),
\[
\boxed{F(P_0)-F(P)\ge\frac{\gamma_m}{2N}\|P-P_0\|_F^2,\qquad
\gamma_m=\begin{cases}\frac{(m-4)(m+1)}2,&5\le m\le7,\\2(m-1),&m\ge7.\end{cases}}\tag{2}
\]
The coefficient is sharp in each dimension, in arbitrarily small neighborhoods. The only local maximizer of \(F\) for \(m\ge5\) is \(P_0\). Equality in the stability inequality, within the sign neighborhood, holds precisely for \(\operatorname{ran}P\subset E\oplus\operatorname{ran}C\) when \(m=5,6\); for every such \(P\) when \(m=7\); and for \(\operatorname{ran}P\perp\operatorname{ran}C\) when \(m\ge8\). Thus at \(m=7\) the loss is exactly isotropic in the squared Frobenius distance.

There is a contrasting **dimension-four phenomenon**. Here \(H=E\oplus\operatorname{ran}C\) is five-dimensional, and the entire four-dimensional local manifold of hyperplanes \(\operatorname{ran}P\subset H\) has the identical equal-weight value \(F(P)=F(P_0)=8/5\); these and only these nearby projections have that value. However, **every nontrivial member of this flat manifold strictly increases the optimally weighted objective**, \(L(P)>L(P_0)=8/5\). More quantitatively, if \(c=N^{-1/2}\mathbf1\), \(u\in E\) is any unit vector, and \(P_\theta\) projects onto the hyperplane in \(H\) perpendicular to \(\cos\theta\,c+\sin\theta\,u\), then
\[
\boxed{F(P_\theta)=\frac85,\qquad L(P_\theta)=\frac85+\frac{48}{125}\theta^2+O(|\theta|^3)\quad(\theta\to0).}\tag{3}
\]
The quadratic ascent coefficient is independent of \(u\). The theorem concerns local perturbations of Parseval-frame Gram projections, not a global maximum over all frames.

## Assumptions and scope
All spaces and projections are real. Let \(q=m+1\), \(\mathcal E=\{\{i,j\}:1\le i<j\le q\}\), and \(N=|\mathcal E|\). Define the unsigned edge-vertex incidence matrix \(B\in\mathbb R^{N\times q}\) by \(B_{e,i}=1\) when vertex \(i\) belongs to edge \(e\), and zero otherwise. Put \(J_q=\mathbf1_q\mathbf1_q^\top\) and
\[
P_0=\frac{1}{q-2}B\left(I_q-\frac1qJ_q\right)B^\top,\qquad c=\frac{\mathbf1_N}{\sqrt N},\quad C=cc^\top,\quad H=\operatorname{ran}B,\quad P_W=I_N-P_0-C.
\]
Here \(P_0\) is an orthogonal projection onto \(E=B(\mathbf1_q^\perp)\), and \(H=E\oplus\mathbb Rc\). Every rank-\(m\) orthogonal projection \(P\) is the Gram matrix of a real Parseval frame of \(N\) vectors in \(\mathbb R^m\); its objective \(F\) is the fixed uniform-weight frame value, and \(L\) is the optimized nonnegative-weight value. They coincide at \(P_0\) because its absolute Gram matrix has constant positive row sum. The sign neighborhood is nonempty for \(m\ge4\) because each entry of \(P_0\) is nonzero. No claims are made for complex frames, \(m=3\), rank-changing perturbations, or global optimality of \(P_0\).

## Proof
**1. Incidence projector and signs.** The identity
\[
B^\top B=(q-2)I_q+J_q
\]
shows that \(P_0\) is a rank-\(q-1\) orthogonal projector and that \(H\) has dimension \(q\). Direct multiplication gives
\[
(P_0)_{ef}=\begin{cases}2/q,&e=f,\\ (q-4)/(q(q-2)),&|e\cap f|=1,\\-4/(q(q-2)),&e\cap f=\varnothing.\end{cases}
\]
For \(q\ge5\), all entries are nonzero. Let \(A_D\) be the adjacency matrix of disjoint edges (the Kneser graph on the two-subsets of \(\{1,\ldots,q\}\)), and put \(S=\operatorname{sgn}(P_0)=J_N-2A_D\). Since \(BB^\top=2I_N+A_{\mathrm{share}}\) and \(A_D=J_N+I_N-BB^\top\),
\[
S=2BB^\top-2I_N-J_N.
\]
On \(\mathbb Rc\), the incidence eigenvalue is \(2(q-1)\); on \(E\), it is \(q-2\); and on \(W=\ker B^\top\), it is zero. Consequently \(S\) acts by
\[
\alpha_m=\frac{-m^2+7m-4}{2}\ \text{on }\mathbb Rc,\quad
\beta_m=2(m-2)\ \text{on }E,\quad -2\ \text{on }W.
\]
The three subspaces are orthogonal and exhaust \(\mathbb R^N\). Their dimensions are \(1,m,N-m-1\). In the sign neighborhood, \(F(P)=\operatorname{tr}(SP)/N\), while \(F(P_0)=m\beta_m/N=4(m-2)/(m+1)\).

**2. Exact leakage and sharpness.** Since \(\operatorname{tr}P=m\),
\[
m-\operatorname{tr}(P_0P)=\operatorname{tr}(CP)+\operatorname{tr}(P_WP)=\frac12\|P-P_0\|_F^2.
\]
Taking the trace against the three spectral projections of \(S\), subtracting the value at \(P_0\), and using
\[
\beta_m-\alpha_m=\frac{(m-4)(m+1)}2,\qquad\beta_m+2=2(m-1),
\]
gives (1). These nonnegative coefficients have minimum \(\gamma_m\) in (2) for \(m\ge5\). The equality conditions follow because both leakage traces are nonnegative, and a leakage trace vanishes exactly when the range of \(P\) is orthogonal to its corresponding subspace. For sharpness, choose a unit vector \(e\in E\) and rotate it through an arbitrarily small angle toward a unit vector in the cheapest complementary eigenspace (toward \(\mathbb Rc\) for \(m=5,6\), toward \(W\) for \(m\ge8\), and either for \(m=7\)). The resulting rank-\(m\) projector remains in the sign neighborhood and attains equality. Strict positivity of \(\gamma_m\) makes \(P_0\) the unique local maximum for \(m\ge5\), while the two coefficients coincide at \(m=7\).

**3. The dimension-four flat manifold.** When \(m=4\), \(\alpha_4=\beta_4=4\). Therefore (1) reduces to \(F(P_0)-F(P)=(6/N)\operatorname{tr}(P_WP)\), which vanishes precisely when \(\operatorname{ran}P\subset H\). In the sign neighborhood these projections form the local Grassmannian \(\mathrm{Gr}(4,H)\cong\mathrm{Gr}(4,5)\) of real dimension four. Let \(P_H=P_0+C\). Each such projector close to \(P_0\) can be written uniquely as \(P=P_H-ww^\top\), with \(w\) a unit vector of \(H\) chosen near \(c\). Since \(Sw=4w\), and the sign chamber gives \(|P|=S\circ P\) (entrywise product), the row sums of the nonnegative matrix \(|P|\) are
\[
|P|\mathbf1_N=\left(\frac85+\frac4N\right)\mathbf1_N-4(w_e^2)_{e\in\mathcal E}.
\]
The Rayleigh quotient at \(c\) is still \(F(P)=8/5\). If \(L(P)=8/5\), then this Rayleigh quotient attains the largest eigenvalue of the symmetric matrix \(|P|\); hence \(c\) is an eigenvector, so all row sums are equal and the squares \(w_e^2\) are constant. As \(w\) is close to the strictly positive vector \(c\), this forces \(w=c\), equivalently \(P=P_0\). Otherwise \(L(P)>8/5\). Here the nonnegative-vector optimization in \(L(P)\) equals the largest eigenvalue of the strictly positive entrywise matrix \(|P|\) by the Perron eigenvector theorem.

**4. Universal quadratic weighted ascent.** Set \(w_\theta=\cos\theta\,c+\sin\theta\,u\), where \(u\in E\) is unit, and \(P_\theta=P_H-w_\theta w_\theta^\top\). The strict sign chamber holds for all sufficiently small \(|\theta|\), and Step 3 proves \(F(P_\theta)=8/5\). Put \(G_\theta=|P_\theta|\). The positive matrix \(G_0\) has simple leading eigenvalue \(8/5\), with normalized eigenvector \(c\). Directly from the three entry types in Step 1, its eigenvalue on \(E\) is \(-1/15\), and on \(W\) it is \(8/15\). Differentiating the entrywise-sign expression at zero gives
\[
G_0'c=-\frac45u,\quad \langle c,G_0'c\rangle=0,
\quad\langle c,G_0''c\rangle=0,
\]
where the final identity follows also from the exact constancy of \(F(P_\theta)=\langle c,G_\theta c\rangle\). The standard elementary second-derivative identity for a simple symmetric-matrix eigenvalue (obtained by differentiating the normalized eigenvector equation and projecting onto \(c^\perp\)) yields
\[
L(P_\theta)=\frac85+\frac{\|G_0'c\|_2^2}{\frac85-(-\frac1{15})}\theta^2+O(|\theta|^3)
=\frac85+\frac{48}{125}\theta^2+O(|\theta|^3).
\]
The remainder is valid for each fixed unit \(u\), and can be taken uniformly over unit \(u\in E\) by compactness and the uniform positive spectral gap. This completes the claim.

## Verification
The companion `checker.py` builds the incidence matrices and sign operators for every \(4\le m\le12\), checks idempotence, rank, entry signs, the complete predicted sign spectrum, and the exact leakage identity on randomly perturbed rank-\(m\) projections. It also verifies the dimension-seven exact isotropy and the dimension-four flat family, strict weighted ascent, and the coefficient \(48/125\) for small rotations. Running `python checker.py` with NumPy installed produced `SIMPLEX_LOCAL_SIGN_SPECTRAL_CHECK_OK 2330`. These finite floating-point diagnostics supplement the exact all-dimensions proof; neither sampling nor approximate arithmetic is offered as an infinite certificate.

## Relationship to prior work
Deregowska and Lewandowska, arXiv:2608.08695, introduce the regular-simplex edge-midpoint Parseval frame, calculate its unperturbed value \(4(m-2)/(m+1)\), and study its candidacy for maximal projection constants. Those results do not give the local geometric behavior under perturbing the frame itself. The published result *Sharp weight rigidity and a spectral crossover for regular-simplex midpoint frames* determines a global nonuniform-weight penalty **with the frame held fixed** and explicitly leaves perturbations of the frame vectors outside its scope. The present theorem varies the Gram projection, proves the exact local loss and the dimension-four flat manifold, and shows that optimizing the weights destroys that flatness. The overlapping incidence and triangular-graph spectral ingredients are credited, not claimed as new in isolation.

Kumar–Mohar–Mojallal–Pragada (arXiv:2609.03200) prove stabilization as the number of ambient coordinates grows; Sivashankar–Tang–Wakhare (arXiv:2608.02429) study graph-eigenvalue bounds. The full text of *Hypersimplex frames beyond the simplex bound, and the exact table of quasimaximal projection constants up to \(N=11\)* evaluates several specific frames and enumerates global values at small \(N\), rather than local perturbation rigidity at the specified frame. In particular, the existing larger global \(m=4,N=10\) value is compatible with, not a contradiction to, the present nonglobal local plateau. Ky Fan's spectral variational principle and elementary simple-eigenvalue perturbation theory are standard inputs; the stated local phase diagram and its weighted ascent are the asserted additions.

## Limitations
This is a local theorem on real rank-\(m\) Parseval-frame Gram matrices in the **fixed sign chamber** of the midpoint configuration. It does not prove global optimality of the frame, particularly the proposed dimensions six and eight, nor any general Banach-space projection-constant conjecture. The bound (2) is a local sharp inequality, not global outside the sign chamber. The dimension-four weighted ascent is proved only along the equidistributed flat family and its small rotations, not as a complete Hessian classification in all Grassmannian directions. The source's dimension-three midpoint configuration has zero inner products, so the sign-chamber proof does not apply. Standard spectral variational principles make the argument short, and equivalently formulated unindexed earlier frame-perturbation results remain a publication-priority risk.

## References
[1] B. Deregowska and B. Lewandowska, *Maximal Projection Constants and Extremal Vector Configurations: Some Conjectures and Examples*, arXiv:2608.08695, first public version 9 August 2026, especially Section 2; https://arxiv.org/abs/2608.08695.

[2] *Sharp weight rigidity and a spectral crossover for regular-simplex midpoint frames*, publicly available mathematical research record (2 November 2026); https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-sharp-weight-rigidity-and-a-spectral-crossover-for-regular-simpl--bc57de4b689b/RESULT.md.

[3] H. Kumar, B. Mohar, S. A. Mojallal and S. Pragada, *Stability of maximal relative projection constants*, arXiv:2609.03200, first public 2 September 2026; https://arxiv.org/abs/2609.03200.

[4] V. Sivashankar, Q. Tang and T. Wakhare, *Graph Eigenvalues and Projection Constants*, arXiv:2608.02429, first public 3 August 2026; https://arxiv.org/abs/2608.02429.

[5] *Hypersimplex frames beyond the simplex bound, and the exact table of quasimaximal projection constants up to \(N=11\)*, publicly available manuscript, 7 September 2026; https://ideosphere.ai/papers/projconst-mn-v1.pdf.
