# Three-level singular spectra of self-involutive quadratic-graph Walsh minors

## Finding
Let \(d\ge 2\) be even, \(N=2^d\), and \(Q:\mathbb F_2^d\to\mathbb F_2\) a polynomial of degree at most two. Its polar bilinear form is \(Q(x+y)+Q(x)+Q(y)+Q(0)=x^{\mathsf T}Py\). Assume that its symmetric alternating polar matrix obeys \(P^2=I_d\) over \(\mathbb F_2\). Define the quadratic graph \(S_Q=\{(x,Q(x)):x\in\mathbb F_2^d\}\subset\mathbb F_2^{d+1}\). The square, unnormalized principal Walsh–Fourier matrix indexed by \(S_Q\) is
\[
K_Q(x,y)=(-1)^{x\cdot y+Q(x)Q(y)}\qquad (x,y\in\mathbb F_2^d).
\]
Its **complete singular-value spectrum**, with multiplicities, is
\[
\begin{array}{c|c}
\text{singular value}&\text{multiplicity}\\ \hline
\frac{\sqrt N(\sqrt3+1)}2&\frac{N-1}3\\
\sqrt N&\frac{N+2}3\\
\frac{\sqrt N(\sqrt3-1)}2&\frac{N-1}3
\end{array}
\]
(in descending order). In particular every such principal Fourier minor is invertible, with the exact dimension-independent spectral condition number and determinant magnitude
\[
\kappa_2(K_Q)=2+\sqrt3,\qquad
|\det K_Q|=N^{N/2}2^{-(N-1)/3}.
\]
The conclusion is invariant under affine perturbations of \(Q\), including changing its constant coefficient. Matching-pair quadratics \(Q=\sum_{j=1}^{d/2}x_{2j-1}x_{2j}\) and complete-graph quadratics \(Q=\sum_{i<j}x_ix_j\) both satisfy the hypothesis in every even dimension.

## Assumptions and scope
All field operations involving \(Q,P\) are in \(\mathbb F_2\); real matrix products, singular values, and norms are over \(\mathbb R\). The dot product is the standard coordinate bilinear form, and \(P^2=I_d\) is basis-dependent relative to that coordinate pairing. There is no large-dimension limit in the exact statement: every positive even \(d\) is included. The rows and columns of \(K_Q\) correspond to the same graph \(S_Q\), and the character normalization is unnormalized (entries are signs). The assumption forces \(P\) to be nonsingular and hence forces \(d\) even; merely assuming nonsingularity does not yield the stated three-level theorem.

## Proof
**1. Reduction and quadratic Gauss identity.** Changing \(Q\) to \(Q+1\) changes \(K_Q\) to \(-D_QK_QD_Q\), where \(D_Q(x,x)=(-1)^{Q(x)}\). Thus the singular values are unchanged and we may assume \(Q(0)=0\). Put \(U(x,y)=N^{-1/2}(-1)^{x\cdot y}\), \(D=D_Q\), and \(L=DU\). Both \(U\) and \(D\) are real symmetric involutions. Since \(P^{-1}=P\), \(Q\) is a nondegenerate quadratic Boolean function. Squaring the sum and applying character orthogonality gives
\[
\sum_z(-1)^{Q(z)}=\varepsilon\sqrt N,\qquad
\sum_z(-1)^{Q(z)+w\cdot z}=\varepsilon\sqrt N(-1)^{Q(Pw)},\quad
\varepsilon\in\{\pm1\}.
\]
Indeed the difference under translation by \(Pw\) is the linear form \(w\cdot z\), and the square of the first sum is \(N\) because the polar is nonsingular.

**2. An order-three orthogonal operator.** The quadratic functions \(Q(Pw)\) and \(Q(w)\) have the same polar matrix: the first has polar \(P^{\mathsf T}PP=P^3=P\). Their difference is therefore linear, say \(Q(Pw)+Q(w)=\ell\cdot w\). Applying \(P\) again shows \(P\ell=\ell\). Since \(P\) is alternating and \(P\ell=\ell\), we also have \(\ell\cdot\ell=\ell^{\mathsf T}P\ell=0\). Substitution of the Gauss identity into the threefold product gives the **exact** permutation formula
\[
L^3(x,y)=\varepsilon(-1)^{\ell\cdot x}\,\mathbf 1_{\{y=Px+\ell\}}.
\]
The permutation \(x\mapsto Px+\ell\) has order two, and its two associated signs multiply to one. Hence \(L^6=I\) and \(W:=L^2=DUDU\) obeys \(W^3=I\). Moreover
\[
\operatorname{tr}W
=\frac1N\left(\sum_x(-1)^{Q(x)}\right)^2=1.
\]
As \(W\) is real orthogonal, its eigenvalues lie in \(\{1,\omega,\overline\omega\}\) with \(\omega=e^{2\pi i/3}\). Complex conjugation equates the two nonreal multiplicities. The trace and dimension equations give respectively \(m_1=(N+2)/3\) and \(m_\omega=m_{\overline\omega}=(N-1)/3\).

**3. From the order-three operator to the singular values.** Write \(P_\pm=(I\pm D)/2\) for the two orthogonal diagonal projections. The normalized principal Fourier minor is
\[
T:=N^{-1/2}K_Q=P_+U+P_-UD.
\]
Set \(B=UDU\), another symmetric involution. Multiplying the two summands shows
\[
TT^{\mathsf T}=I+E,\qquad
E=P_+BP_-+P_-BP_+=\frac{B-DBD}{2}
=\frac{D(W-W^{-1})}{2}.
\]
It follows from involutivity and \(W^3=I\) that
\[
E^2=\frac{2I-W-W^{-1}}4,\qquad
E^3=\frac34 E,\qquad DED=-E.
\]
On the \(W=1\) subspace, \(E^2=0\), so symmetry makes \(E=0\) there. On both nonreal eigenspaces of \(W\), \(E^2=3I/4\). Since conjugation by \(D\) negates \(E\), its positive and negative eigenvalues have the same multiplicity, namely \((N-1)/3\) each. Consequently \(TT^{\mathsf T}\) has eigenvalues \(1+\sqrt3/2\), \(1\), and \(1-\sqrt3/2\), with the asserted multiplicities. Their positive square roots are \((\sqrt3+1)/2\), \(1\), and \((\sqrt3-1)/2\). Multiplication by \(\sqrt N\) proves the spectrum and condition number. The products of each high-low singular-value pair equal \(N/2\); the determinant formula follows.

**4. Examples and a genuine boundary.** The matching polar is block-diagonal with \(2\times2\) exchange blocks, so its square is the identity. For the complete-graph quadratic, \(P=I+J\) over \(\mathbb F_2\), where \(J\) is the all-ones matrix. Since \(d\) is even, \(J^2=dJ=0\) and \(P^2=I\). In contrast, the four-variable path quadratic \(x_1x_2+x_2x_3+x_3x_4\) has a nonsingular polar matrix but \(P^2\ne I\) and five distinct singular values in its graph principal Walsh minor; therefore ordinary bentness alone does not imply the theorem.

## Verification
The standalone `verify.py` checks the exact integer identity \(4(G-NI)^3=3N^2(G-NI)\) for \(G=K_QK_Q^{\mathsf T}\) and compares numerically computed singular values with the stated multiplicities. It covers \(d=2,4,6\), matching and complete polar graphs, affine linear masks, both constant coefficients, and **all** four-variable alternating polar matrices satisfying \(P^2=I\). It passed 80 finite test cases and identified four such four-variable polar matrices; output ends `QUADRATIC_GRAPH_WALSH_EXACT_PASS cases= 80 involutive_four_dim_polar_matrices= 4`. No finite test is treated as a proof of the theorem for arbitrary \(d\); that conclusion follows from the preceding identities.

## Relationship to prior work
Dehaene and De Moor (arXiv:quant-ph/0304125, first posted 18 April 2003) develop binary quadratic-form and Clifford-operator descriptions. Riera and Parker (arXiv:cs/0502049, first posted 9 February 2005) study quadratic graph states and local-Hadamard/related transform spectra; Riera, Danielsen and Parker (arXiv:math/0604396) study graph-pivot orbits and bentness. These supply the quadratic Fourier/Clifford framework but do not state a three-level **singular-value classification of the principal Fourier matrix indexed by the quadratic graph**. The latter is a distinct, nonunitary compression: flat Walsh coefficients for \(Q\) by themselves cannot imply its singular-value spectrum. The proof here derives the spectrum through a specific order-three product and cross-sector Gram analysis. No global historical-priority assertion is made; an unlocated general principal-compression or Clifford spectral theorem could imply this result.

## Limitations
This is an exact result only for quadratic functions whose polar matrix is self-inverse in the chosen standard coordinates; arbitrary nonsingular/bent quadratic polars are outside the claim. It does not classify all singular spectra for arbitrary Boolean graphs, all graph-based Fourier minors, nonquadratic graphs, or arbitrary row/column subsets. Numerical checks cover only small dimensions. Independent mathematical assessment and comprehensive historical-priority verification have not been performed.

## References
1. J. Dehaene and B. De Moor, *The Clifford group, stabilizer states, and linear and quadratic operations over GF(2)*, arXiv:quant-ph/0304125 (first public preprint 2003-04-18), https://arxiv.org/abs/quant-ph/0304125.
2. C. Riera and M. G. Parker, *Generalised Bent Criteria for Boolean Functions (I)*, arXiv:cs/0502049 (first public preprint 2005-02-09), https://arxiv.org/abs/cs/0502049.
3. C. Riera, L. E. Danielsen and M. G. Parker, *On Pivot Orbits of Boolean Functions*, arXiv:math/0604396 (first public preprint 2006-04-18), https://arxiv.org/abs/math/0604396.
