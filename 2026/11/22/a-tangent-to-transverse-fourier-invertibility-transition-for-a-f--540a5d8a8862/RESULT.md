# A tangent-to-transverse Fourier invertibility transition for a finite quadratic cone and a parallel plane

## Finding
For every odd prime power \(q\ge3\), put \(G=\mathbb F_q^3\), \(C=\{(x,y,z):xy=z^2\}\), \(H_c=\{(x,c,z):x,z\in\mathbb F_q\}\), and \(S_c=C\cup H_c\). Let \(T_c f=\mathbf1_{S_c}*f\) be the unnormalized counting-convolution operator on \(\ell^2(G;\mathbb C)\). Its spectral behavior undergoes an exact tangent-to-transverse transition:

* At \(c=0\), where the plane is tangent to the cone along a line, the distinct **singular values** and their multiplicities are

  \[
  \begin{array}{c|c}
  \text{singular value}&\text{multiplicity}\\\hline
  0&2q(q-1)\\
  q&q(q-1)^2\\
  q(q-1)&q-1\\
  q(2q-1)&1
  \end{array}
  \]

* At every \(c\ne0\), all Fourier multipliers are nonzero; the **exact** least singular value is \(\sqrt q\), and the exact largest singular value is \(q(2q-1)\). Thus

  \[
  \|T_c^{-1}\|_{2\to2}=q^{-1/2},\qquad
  \kappa_2(T_c)=(2q-1)\sqrt q\quad(c\ne0).
  \]

Every set has \(|S_c|=2q^2-q\). The least nonzero tangent singular value equals \(q\), so the tangent case is genuinely singular rather than merely badly conditioned. The statements hold for **all** nonzero field elements \(c\), including every odd extension field.

## Assumptions and scope
Let \(\psi:\mathbb F_q\to\mathbb C^\times\) be a fixed nontrivial additive character, and normalize the Fourier transform by
\[
\widehat h(u,v,w)=\sum_{x,y,z\in\mathbb F_q}h(x,y,z)\psi(ux+vy+wz).
\]
The Fourier transform is unnormalized, but the Fourier basis diagonalizes convolution unitarily after multiplying the Fourier matrix by \(q^{-3/2}\); consequently singular values of \(T_c\) are precisely the magnitudes of these unnormalized multipliers. Let \(\chi\) denote the quadratic character extended by \(\chi(0)=0\), put \(D=uv-w^2/4\), and write \(\mathcal G=\sum_{t\in\mathbb F_q}\chi(t)\psi(t)\), with \(|\mathcal G|=\sqrt q\) and \(\mathcal G^2=\chi(-1)q\). Because the characteristic is odd, division by \(2\) and \(4\) is valid.

## Proof
**Step 1: exact cone multiplier.** Orthogonality applied to \(xy-z^2=0\) gives the complete identity
\[
\widehat{\mathbf1_C}(u,v,w)=q^2\mathbf1_{(u,v,w)=(0,0,0)}+q\chi(-D).
\]
Indeed, introducing the Lagrange multiplier \(t\) and summing first in \(x,y\), the nonzero-\(t\) contribution becomes \(\mathcal G\sum_{t\ne0}\chi(-t)\psi(-D/t)\). Inversion \(t\mapsto t^{-1}\), the quadratic character Fourier identity, and \(\mathcal G^2=\chi(-1)q\) reduce this to \(q\chi(-D)\). In particular, this formula is exact at the dual cone \(D=0\).

**Step 2: plane and intersection.** The plane has transform
\[
\widehat{\mathbf1_{H_c}}(u,v,w)=q^2\mathbf1_{u=w=0}\psi(vc).
\]
If \(c=0\), the intersection is the line \(\{(x,0,0)\}\), so \(\widehat{\mathbf1_{C\cap H_0}}=q\mathbf1_{u=0}\). If \(c\ne0\), the intersection is the parabola \(\{(z^2/c,c,z):z\in\mathbb F_q\}\); square-completion gives
\[
\widehat{\mathbf1_{C\cap H_c}}(u,v,w)=
\begin{cases}
q\psi(vc),&u=w=0,\\
0,&u=0,\ w\ne0,\\
\chi(u/c)\mathcal G\psi\bigl(vc-cw^2/(4u)\bigr),&u\ne0.
\end{cases}
\]
Thus \(\widehat{\mathbf1_{S_c}}=\widehat{\mathbf1_C}+\widehat{\mathbf1_{H_c}}-\widehat{\mathbf1_{C\cap H_c}}\) is explicit at every frequency. The intersection always has \(q\) points, yielding \(|S_c|=q^2+q^2-q\).

**Step 3: tangent multiplicities.** Set \(c=0\). The origin frequency gives \(q(2q-1)\). The \(q-1\) frequencies \(u=w=0,v\ne0\) yield \(q(q-1)\). The \(q(q-1)\) frequencies \(u=0,w\ne0\) yield zero because the cone contributes \(q\) and the intersection line contributes \(q\). The \(q(q-1)\) frequencies \(u\ne0,D=0\) also vanish. All remaining \(q(q-1)^2\) frequencies have multiplier \(\pm q\). Their counts sum to \(q^3\), proving the four-level spectrum including multiplicities.

**Step 4: translated nonvanishing and sharpness.** Let \(c\ne0\). If \(u=0,w\ne0\), the multiplier equals \(q\); if \(u=w=0,v\ne0\), it has magnitude \(q(q-1)\). If \(u\ne0,D=0\), the cone multiplier vanishes and the intersection Gaussian contribution has modulus **exactly** \(\sqrt q\). There are \(q(q-1)\) such frequencies, so the minimum is at most \(\sqrt q\). For \(u\ne0,D\ne0\), the cone term has magnitude \(q\) and the intersection term magnitude \(\sqrt q\). When \(q\ge5\), the reverse triangle inequality gives \(q-\sqrt q>\sqrt q\). For the remaining odd field \(q=3\), \(\mathcal G\) is purely imaginary of modulus \(\sqrt3\) and every additive character value is a cubic root of unity. Thus each interference has real part, after choosing the sign of the cone term, among \(0,\pm 3/2\) times \(1\) in the rescaled expression; directly
\[
|\pm3-\varepsilon\mathcal G\psi(t)|^2\in\{3,12,21\},\quad \varepsilon\in\{-1,1\}.
\]
In particular every such magnitude is at least \(\sqrt3\). Hence no translated multiplier vanishes and the sharp least magnitude is \(\sqrt q\) for every odd \(q\ge3\). Finally, the trivial Fourier multiplier equals \(|S_c|=q(2q-1)\), and the triangle inequality bounds every multiplier in modulus by \(|S_c|\); this is the exact largest singular value. Unitary Fourier diagonalization proves the operator norm and condition number formulas.

## Verification
The accompanying `checker.py` enumerates every point and every frequency of the four fields \(\mathbb F_3\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\) (the latter constructed as \(\mathbb F_3[i]\) with \(i^2=-1\)). For each, it checks the zero plane and two nonzero parallel planes, compares the direct character sum to the Gaussian decomposition at all frequencies, and verifies nullity and least positive singular magnitude. It passed all \(3\sum_{q\in\{3,5,7,9\}}q^3=3672\) indexed comparisons. This is a finite consistency check, not a proof for arbitrary finite fields; the general proof is Steps 1–4.

Run `python3 checker.py` using Python 3 standard library; no external packages or data are needed.

## Relationship to prior work
Demeter (2026) studies sharp sixth Fourier moments for **Euclidean truncated-cone** measures, providing contemporary motivation for cone-sensitive Fourier stability but neither a finite-field union nor convolution inversion. González-Riquelme and Ismoilov (2025) optimize finite-field cone **extension** \(L^2\to L^4\) inequalities on homogeneous cones in four variables, a different operator, dimension and support. Iosevich, Li and Yu (2026) analyze general spectral-synthesis complexity, not the exact three-dimensional cone-plus-parallel-plane multipliers. Kazhdan and Polishchuk (2000) supply general finite-field Gauss-sum transform identities; these elementary identities underlie, rather than constitute, the new union-specific tangent/transverse spectral comparison. No assertion is made that the constituent Gauss-sum or cone-transform identities are new.

## Limitations
This theorem concerns an unweighted indicator of the specified three-dimensional split quadratic cone union a parallel **affine** plane in odd characteristic, for the full counting-convolution operator on \(\ell^2\). No claim about general smooth cones, arbitrary secant planes, characteristic two, \(L^p\) extension extremizers, or nonlinear recovery is established. The proof uses classical Gauss-sum formulas. Historical priority requires an independent bibliographic check, particularly for older general cone–hyperplane convolution formulas. The motivating Demeter full text was not accessible during the literature review; its abstract concerns Euclidean fractal measures and does not state the finite-field result.

## References
1. C. Demeter, *Sharp \(L^6\) Fourier moments and \((3,\delta)\)-energy estimates for fractal measures on the truncated cone in \(\mathbb R^3\)*, arXiv:2610.23679 (first posted 2026-10-16), https://arxiv.org/abs/2610.23679.
2. C. González-Riquelme and T. Ismoilov, *Maximizers of the \(L^2\to L^4\) Fourier extension inequality for cones in finite fields*, arXiv:2509.05600 (first posted 2025-09-06), https://arxiv.org/abs/2509.05600.
3. A. Iosevich, Z. Li and K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404 (2026), https://arxiv.org/abs/2609.25404.
4. D. Kazhdan and A. Polishchuk, *Fourier transform over finite field and identities between Gauss sums*, arXiv:math/0003011 (2000), https://arxiv.org/abs/math/0003011.
