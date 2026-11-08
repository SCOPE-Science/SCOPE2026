# Two singular values distinguish branching in equilateral two-tier metric trees

## Finding

Let \(d,e\ge2\) be integers. Start with a unit-length stem from a root \(o\) to a hub. Attach \(d\) unit-length edges from that hub to separate second-generation hubs, and attach \(e\) unit-length terminal edges to each second-generation hub. Denote the resulting rooted metric tree by \(T_{d,e}\). All integrals and norms use arclength measure. For real \(f\in L^2(T_{d,e})\), put
\[
(H_{d,e}f)(x)=\int_{[o,x]}f(y)\,dy.
\]
Write \(s_1(H_{d,e})\ge s_2(H_{d,e})\ge\cdots\) for its singular values, with multiplicity, and let \(Q=de+d+e=(d+1)(e+1)-1\). Then
\[
\boxed{s_1(H_{d,e})=\frac{1}{\arctan(1/\sqrt Q)},\qquad
s_2(H_{d,e})=\frac{1}{\arctan(1/\sqrt e)}.}
\]
The largest singular value is simple. The second singular value has multiplicity **exactly** \(d-1\). In fact, the associated rooted Dirichlet--Kirchhoff Laplacian has no other eigenfrequencies in \((0,\pi/2)\): the two values are \(\arctan(1/\sqrt Q)\) and \(\arctan(1/\sqrt e)\), with the stated multiplicities.

This yields a complete collision/rigidity classification. Two parameter pairs have the same largest singular value if and only if
\[
(d+1)(e+1)=(d'+1)(e'+1).
\]
Nevertheless, the **ordered pair** of largest singular values uniquely determines the ordered branching parameters: equality of both values implies \(e=e'\) and \(d=d'\). Indeed, the value and multiplicity of the second singular value alone recover \(e\) and \(d\). The positive first singular input is unique up to scalar multiplication.

For example, \((d,e)=(2,7)\) and \((3,5)\) both have \(Q=23\), hence the same largest singular value, but their second singular values differ. Their trees have respectively \(17\) and \(19\) unit edges. Thus even different total lengths do not prevent a sharp Hardy-norm collision. At fixed total edge count \(E=1+d+de\), the largest singular value is strictly increasing in the feasible deeper branching number \(e\), since \(Q=E+e-1\).

## Assumptions and scope

Each of the \(1+d+de\) edges is a nondegenerate interval of length exactly one; the root is the pendant endpoint of the initial stem. Vertex masses are zero. The function space is real \(L^2\) with arclength measure. The rank-two branching assumptions \(d,e\ge2\) are essential to the second singular-value statement. At the root, eigenfunctions satisfy Dirichlet trace zero; at terminal leaves they satisfy Neumann conditions; at all branching vertices they are continuous and satisfy the outward Kirchhoff derivative condition. No assertion is made for different lengths, potentials, or measure weights.

## Proof

**1. Singular-value correspondence.** Let \(\mathcal H\) be the Sobolev space of continuous, edgewise \(H^1\) functions vanishing at \(o\), with Hilbert norm \(\|u'\|_{L^2(T_{d,e})}\). Because the underlying graph is a tree, the derivative map \(D:\mathcal H\to L^2(T_{d,e})\) is an isometric isomorphism: its inverse integrates along each root-to-point path. Consequently \(H_{d,e}=J D^{-1}\), where \(J:\mathcal H\hookrightarrow L^2(T_{d,e})\) is the compact Sobolev inclusion. The singular values of \(H_{d,e}\) are the reciprocals of the positive square roots of the Dirichlet--Kirchhoff Laplacian eigenvalues. Compactness follows also directly from the Hilbert--Schmidt path-indicator kernel on the finite tree.

**2. Exhaust all eigenfrequencies below \(\pi/2\).** Write \(k=\sqrt\lambda\in(0,\pi/2)\), \(s=\sin k\), \(c=\cos k\). On the initial stem, the root Dirichlet condition gives \(u_0(x)=C\sin(kx)\). Its distal hub value is \(U=Cs\). On middle branch \(j=1,\ldots,d\), use the coordinate \(y\) directed away from the first hub:
\[
u_j(y)=U\cos(ky)+B_j\sin(ky).
\]
Its distal value is \(W_j=Uc+B_js\). On each of the \(e\) terminal edges incident to this second hub, the Neumann endpoint condition uniquely forces
\[
u_{j,h}(z)=W_j\frac{\cos(k(1-z))}{c},\qquad h=1,\ldots,e.
\]
(The denominator is nonzero because \(0<k<\pi/2\).) The Kirchhoff conditions at the second-generation hubs and the first hub are, respectively,
\[
B_j(c^2-es^2)=U(e+1)sc\quad(1\le j\le d),
\qquad Cc=\sum_{j=1}^d B_j.
\tag{1}
\]
If \(c^2-es^2\ne0\), a nonzero eigenfunction must have \(C\ne0\), and all \(B_j\) are equal. Substituting into the second condition yields
\[
 c^2=[e+d(e+1)]s^2=Qs^2.
\tag{2}
\]
This has exactly one solution in \((0,\pi/2)\), namely \(k_0=\arctan(1/\sqrt Q)\). Its eigenspace has dimension one, and its edgewise eigenfunction is strictly positive away from \(o\) for \(C>0\): in (1), \(c^2-es^2=d(e+1)s^2>0\) forces every \(B_j>0\).

If \(c^2-es^2=0\), the first condition of (1) forces \(U=0\), hence \(C=0\), and the second becomes \(\sum_j B_j=0\). Thus the only eigenfrequency in this case is \(k_1=\arctan(1/\sqrt e)\), and its eigenspace has dimension \(d-1\). Since \(Q>e\), we have \(0<k_0<k_1<\pi/2\). Conditions (1) are necessary and sufficient, and cover *every* candidate eigenfunction in the entire interval; hence no third frequency lies below \(\pi/2\). Because the Laplacian has discrete positive spectrum, these are its first and second distinct eigenfrequencies, including all multiplicities. The singular-value formulas follow from Step 1.

**3. Equality cases and inverse rigidity.** The eigenspace of \(k_0\) is one-dimensional; its derivative, via Step 1, gives all functions attaining \(\|H_{d,e}\|\), up to scalar multiplication. The function \(q\mapsto1/\arctan(1/\sqrt q)\) is strictly increasing on \((0,\infty)\). Thus equality of first singular values is equivalent to equality of \(Q\), or of \((d+1)(e+1)\). Equality of the second singular values forces equality of \(e\), after which equality of \(Q\) forces equality of \(d\). Explicitly,
\[
 e=\frac{1}{\tan^2(1/s_2)},\qquad
 d=\frac{1/\tan^2(1/s_1)-e}{e+1}.
\]
Also, the multiplicity \(d-1\) of \(s_2\) alone recovers \(d\), while its numerical value recovers \(e\). Finally \(E=1+d+de\) implies \(Q=E+e-1\), giving the asserted strict ordering at fixed \(E\).

## Verification

The accompanying script `verify_two_tier_hardy.py` symbolically checks the secular-determinant factorization
\[
\det\begin{pmatrix}1&-t\mathbf 1^{\mathsf T}\\-(e+1)t\mathbf 1&(1-et^2)I_d\end{pmatrix}
=(1-et^2)^{d-1}(1-(de+d+e)t^2)
\]
for eight different parameter pairs. The universal factorization is also proved directly by the two cases of (1), so finite symbolic instances are not the infinite proof. The script separately constructs conforming piecewise-affine finite-element stiffness and mass matrices on the **actual trees** and numerically checks the lowest \(d+1\) eigenvalues for the same eight pairs, including the multiplicity and lower bound on the next frequency. These discretizations are consistency checks, not proofs of the exact infinite-dimensional claim. Run with `python verify_two_tier_hardy.py` after installing the packages in `requirements.txt`.

## Relationship to prior work

Evans, Harris and Lang (arXiv:math/0003215v1, posted March 30, 2000) developed Hardy-type operators on trees and analyzed their approximation numbers, without the present two-tier inverse classification. Naimark and Solomyak (2000), especially Section 7 and Theorem 7.2, developed a very general orthogonal reduction of regular-tree Laplacian spectra to one-dimensional weighted problems. That foundational reduction does apply here; it is not claimed as new. The present statement evaluates the first *two* singular values explicitly and compares *different* branching sequences to prove a complete collision law and two-value inverse rigidity. Solomyak (arXiv:math/0201015v1, 2002) provided general graph spectral estimates rather than these exact distinctions. Pivovarchik (arXiv:2301.05939, 2023), in particular Theorem 2.2, gives a general characteristic-polynomial representation for equilateral rooted-tree Dirichlet spectra and discusses recovery from two *full spectra*. The present inverse assertion uses only two singular values of **one** rooted boundary problem. The generic determinant representation is acknowledged as a possible way to derive the low-frequency calculations; the special comparison and rigidity classification are the asserted additions.

## Limitations

The result is specific to unit-length edges, two nontrivial regular branching generations, and the root-to-point \(L^2\) integration operator. No claim is made about the full singular spectrum or recovery of arbitrary trees. A general characteristic-polynomial theorem already determines the spectrum computationally for equilateral trees; an unindexed prior closed-form application or inverse characterization is a residual originality risk. Independent mathematical audit has not been performed.

## References

- W. D. Evans, D. J. Harris, J. Lang, *The approximation numbers of Hardy-type operators on trees*, arXiv:math/0003215v1 (public March 30, 2000), https://arxiv.org/pdf/math/0003215.
- K. Naimark and M. Solomyak, *Eigenvalue Estimates for the Weighted Laplacian on Metric Trees*, Proc. Lond. Math. Soc. 80 (2000), 690–724, https://www.math.ucdavis.edu/~saito/data/LapEig/naimark-solomyak-lapeig-metrictree.pdf.
- M. Solomyak, *On the eigenvalue estimates for the weighted Laplacian on metric graphs*, arXiv:math/0201015v1 (2002), https://arxiv.org/pdf/math/0201015.
- V. Pivovarchik, *Recovering the shape of a quantum tree by two spectra*, arXiv:2301.05939 (2023), https://arxiv.org/pdf/2301.05939.
- V. Pivovarchik and N. Rozhenko, *Inverse Sturm–Liouville problem on equilateral regular tree*, Applicable Analysis 92 (2013), 784–798, https://doi.org/10.1080/00036811.2011.639765.
