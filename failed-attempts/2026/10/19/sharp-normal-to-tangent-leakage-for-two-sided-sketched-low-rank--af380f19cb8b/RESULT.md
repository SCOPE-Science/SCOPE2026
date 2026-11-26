# Sharp normal-to-tangent leakage for two-sided sketched low-rank projections

## Finding

Consider the oblique fixed-rank tangent projection used by two-sided sketched Galerkin dynamics. Its difference from the Euclidean orthogonal tangent projection has an **exact**, dimension-independent Frobenius operator norm. Let \(Y\in\mathbb R^{m\times n}\) have rank \(r\), with \(1\le r<\min(m,n)\), and let \(U\in\mathbb R^{m\times r}\), \(V\in\mathbb R^{n\times r}\) have orthonormal columns spanning its column and row spaces. For real sketches \(\Theta\), \(\Omega\) injective on these respective spaces, define

\[
H=\Theta^{\mathsf T}\Theta,\quad G=\Omega^{\mathsf T}\Omega,\quad
L=U(U^{\mathsf T}HU)^{-1}U^{\mathsf T}H,\quad
R=V(V^{\mathsf T}GV)^{-1}V^{\mathsf T}G.
\]

Let \(P\) and \(P_{\rm ob}\) act on matrices by

\[
P(Z)=UU^{\mathsf T}Z+ZVV^{\mathsf T}-UU^{\mathsf T}ZVV^{\mathsf T},\qquad
P_{\rm ob}(Z)=LZ+ZR^{\mathsf T}-LZR^{\mathsf T}.
\]

With \(Q_U=I-UU^{\mathsf T}\), \(Q_V=I-VV^{\mathsf T}\), set

\[
\gamma_L=\left\|(U^{\mathsf T}HU)^{-1}U^{\mathsf T}HQ_U\right\|_2,\qquad
\gamma_R=\left\|(V^{\mathsf T}GV)^{-1}V^{\mathsf T}GQ_V\right\|_2.
\]

Then the **exact Frobenius operator norm**, with no embedding assumption beyond the stated injectivity, is

\[
\boxed{\|P_{\rm ob}-P\|_{F\to F}
=\sqrt{\gamma_L^2+\gamma_R^2+\gamma_L^2\gamma_R^2}.}
\tag{1}
\]

Moreover, let \(Z\) be fixed, put \(N=Q_U ZQ_V\), and suppose the squared-norm embeddings satisfy

\[
(1-\varepsilon_L)\|x\|_2^2\le\|\Theta x\|_2^2\le(1+\varepsilon_L)\|x\|_2^2
\quad\text{for all }x\in\operatorname{span}(U,\operatorname{col}N),
\]

and the analogous inequality for \(\Omega\) on \(\operatorname{span}(V,\operatorname{row}N)\), with \(0\le\varepsilon_L,\varepsilon_R<1\). Then

\[
\boxed{\|(P_{\rm ob}-P)Z\|_F
\le \Phi(\varepsilon_L,\varepsilon_R)\|N\|_F,\qquad
\Phi(\varepsilon_L,\varepsilon_R)=
\sqrt{\frac{1}{(1-\varepsilon_L^2)(1-\varepsilon_R^2)}-1}.}
\tag{2}
\]

For every choice of distortions, this universal coefficient is attained in rank one with \(m=n=2\). Thus no smaller coefficient works in general, even for the instantaneous projected vector fields of a smooth matrix ODE. When both distortions equal \(\varepsilon\), the sharp coefficient is \(\varepsilon\sqrt{2-\varepsilon^2}/(1-\varepsilon^2)\). A prescribed discrepancy ratio \(\tau\ge0\) is guaranteed for all such data if and only if

\[
(1-\varepsilon_L^2)(1-\varepsilon_R^2)\ge\frac{1}{1+\tau^2};
\]

for equal distortions this becomes \(\varepsilon\le\sqrt{1-(1+\tau^2)^{-1/2}}\).

## Assumptions and scope

All matrices and sketches are real and finite-dimensional; the ambient dimensions satisfy \(m,n\ge2\) and \(1\le r<\min(m,n)\). The sketches may be rectangular, including dimension-reducing ones, and need only be injective on \(\operatorname{col}(Y)\) and \(\operatorname{row}(Y)\) for (1). Frobenius operator norm refers to the linear map on \(\mathbb R^{m\times n}\) with its Frobenius inner product. For (2), the stated bounds must hold on each *combined* trial-plus-normal-residual subspace, not merely on the trial spaces separately. If \(N=0\), both sides of (2) vanish without further residual-side assumptions. There is no randomness assumption; these are deterministic, per-realization statements. The sources' sketch-orthonormal parameterization and the Euclidean \(U,V\) parameterization give the same oblique projectors.

## Proof

**1. Tangent/normal splitting.** Put \(P_U=UU^{\mathsf T}\), \(P_V=VV^{\mathsf T}\). The Euclidean tangent space is the orthogonal sum of \(U\otimes V\), \(U\otimes V^\perp\), and \(U^\perp\otimes V\); its normal space is \(U^\perp\otimes V^\perp\). Since \(LU=U\), \(RV=V\), and \(L^2=L\), \(R^2=R\), both tangent projectors act as the identity on the tangent space. Hence

\[
(P_{\rm ob}-P)Z=P_{\rm ob}(N),\qquad N=Q_UZQ_V.
\]

Let \(C=(U^{\mathsf T}HU)^{-1}U^{\mathsf T}HQ_U\) and \(D=(V^{\mathsf T}GV)^{-1}V^{\mathsf T}GQ_V\). For normal \(N\), direct substitution gives

\[
P_{\rm ob}(N)=UCN+ND^{\mathsf T}V^{\mathsf T}-UCND^{\mathsf T}V^{\mathsf T}.
\tag{3}
\]

The three terms in (3) lie in pairwise orthogonal subspaces. Therefore

\[
\|P_{\rm ob}(N)\|_F^2
=\|CN\|_F^2+\|ND^{\mathsf T}\|_F^2+\|CND^{\mathsf T}\|_F^2
\le(\gamma_L^2+\gamma_R^2+\gamma_L^2\gamma_R^2)\|N\|_F^2.
\]

If \(a\in U^\perp\) and \(b\in V^\perp\) are unit right singular vectors attaining the respective operator norms of \(C\) and \(D\), then \(N=ab^{\mathsf T}\) makes all three inequalities equalities simultaneously. This also covers zero singular norms by selecting arbitrary unit normal vectors. This proves (1).

**2. Sharp one-sided distortion lemma.** Suppose a symmetric form \(H\) differs from the Euclidean inner product by at most \(\varepsilon<1\) on the orthogonal sum of a trial subspace and a specified normal subspace. In orthonormal block coordinates its trial/normal blocks are \(A,B\), with \(A\succ0\). Then

\[
\|A^{-1}B\|_2\le \frac{\varepsilon}{\sqrt{1-\varepsilon^2}}.
\tag{4}
\]

To prove (4), for an arbitrary unit normal vector \(y\), put \(w=A^{-1}By\). If \(w\ne0\), take \(x=w/\|w\|\) in the trial coordinates. Let \(a=x^{\mathsf T}Ax\) and \(b=x^{\mathsf T}By\). By definition, \(b=\|w\|a\). The restriction of \(H-I\) to the orthonormal pair \((x,y)\) has operator norm at most \(\varepsilon\); applying this compression to its first basis vector gives

\[
(a-1)^2+b^2\le\varepsilon^2.
\]

Thus \(\|w\|^2\le[\varepsilon^2-(a-1)^2]/a^2\). Maximizing the right-hand side over \(a\in[1-\varepsilon,1+\varepsilon]\) gives \(\varepsilon^2/(1-\varepsilon^2)\), attained at \(a=1-\varepsilon^2\). The case \(w=0\) is immediate. This proves (4), including its exact best coefficient.

**3. Two-sided bound.** Apply (4) on \(\operatorname{span}(U,\operatorname{col}N)\) to bound the restriction of \(C\) to \(\operatorname{col}N\) by \(t_L=\varepsilon_L/\sqrt{1-\varepsilon_L^2}\), and analogously the restriction of \(D\) to \(\operatorname{row}N\) by \(t_R\). The three squared terms in (3) are then bounded by \(t_L^2\|N\|_F^2\), \(t_R^2\|N\|_F^2\), and \(t_L^2t_R^2\|N\|_F^2\). Their sum is (2), since \(1+t_i^2=1/(1-\varepsilon_i^2)\).

**4. Equality and dimension reduction.** For \(0\le e<1\), let

\[
H_e=\begin{pmatrix}
1-e^2&e\sqrt{1-e^2}\\
e\sqrt{1-e^2}&1+e^2
\end{pmatrix}.
\]

Its eigenvalues are precisely \(1-e\) and \(1+e\). Take \(m=n=2\), \(r=1\), \(U=V=(1,0)^{\mathsf T}\), \(N=E_{22}\), and sketches with \(\Theta^{\mathsf T}\Theta=H_{\varepsilon_L}\), \(\Omega^{\mathsf T}\Omega=H_{\varepsilon_R}\). The one-sided normal-to-trial coefficients are exactly \(t_L\) and \(t_R\). Equation (3) gives

\[
P_{\rm ob}(E_{22})=
\begin{pmatrix}-t_Lt_R&t_L\\t_R&0\end{pmatrix},
\qquad
\|P_{\rm ob}(E_{22})\|_F^2=t_L^2+t_R^2+t_L^2t_R^2.
\]

This attains (2), including endpoint cases with zero distortion. Embedding this construction into the leading two coordinates of \(3\times3\) matrices and taking \(2\times3\) sketches \(\Theta=[H_{\varepsilon_L}^{1/2}\ \ 0]\), \(\Omega=[H_{\varepsilon_R}^{1/2}\ \ 0]\) gives a genuinely dimension-reducing equality example: the required combined subspaces are each two-dimensional. Finally, algebraically solving \(\Phi\le\tau\) proves the stated exact embedding-tolerance frontier.

## Verification

The included standard-library `verify.py` computes exact rational witnesses for \((\varepsilon_L,\varepsilon_R)=(3/5,4/5)\) and \((3/5,3/5)\), including the exact Gram spectra, oblique projection entries, and squared Frobenius norm; it also checks the one-sided distortion inequality on a finite rational grid. For the asymmetric witness, \(t_L=3/4\), \(t_R=4/3\), and the squared normal leakage is exactly \(481/144\). For equal distortions \(3/5\), it is \(369/256\). The analytical steps above—not finite sampling—prove the universal results.

## Relationship to prior work

Carrel and Grigori, arXiv:2607.03402v1, Lemma 4.2, derive the two-sided oblique fixed-rank tangent projector. Their Proposition 4.4 identifies when its dynamics coincide with classical DLRA; Section 4.2 bounds sketched Galerkin pairings by a \(2\varepsilon+\varepsilon^2\) perturbation under its stated embedding assumptions, but does not state an exact Frobenius operator norm for the tangent-projector difference, a sharp two-sided normal-residual coefficient, or an equality witness. Equation (1) uses their projector as the **input**, not as a new discovery. Standard one-sided oblique-projection and randomized-orthogonalization theory supplies related background, but the exact combination of the two sketch-side defects on the fixed-rank tangent/normal splitting is the specific assertion here.

## Limitations

This is an instantaneous exact-arithmetic operator statement, not a bound on accumulated ODE trajectory error, randomized failure probability, finite-precision implementation, or physical invariant drift. If the sketch controls only the trial spaces but not the combined trial-plus-normal-residual spaces, (2) is not warranted. The motivating paper's OSE assumptions and rank-compatibility framework are not automatically equivalent to the stronger *realized, residual-specific* hypotheses here. Older oblique-projector literature may contain equivalent formulations; independent scientific audit has not been performed.

## References

1. B. Carrel and L. Grigori, *Sketch low-rank dynamics: orthogonal vs. oblique projections*, arXiv:2607.03402v1, first submitted 2026-07-03. See especially Lemma 4.2, Proposition 4.4, and Section 4.2. https://doi.org/10.48550/arXiv.2607.03402
2. O. Balabanov and L. Grigori, *Randomized Gram–Schmidt Process with Application to GMRES*, SIAM Journal on Scientific Computing 44 (2022), A1450–A1474, DOI:10.1137/20M138870X (background on subspace embeddings and randomized orthogonalization).
3. J. J. Brust, R. F. Marcia, and C. G. Petra, *Computationally Efficient Decompositions of Oblique Projection Matrices*, SIAM Journal on Matrix Analysis and Applications 41 (2020), 852–870, DOI:10.1137/19M1288115 (general oblique-projector spectral analysis; full-text comparison remains unavailable).
