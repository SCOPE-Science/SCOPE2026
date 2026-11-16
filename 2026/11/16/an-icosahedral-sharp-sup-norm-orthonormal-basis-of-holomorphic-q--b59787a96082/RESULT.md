# An icosahedral sharp sup-norm basis of holomorphic quadratics on the complex three-variable unit sphere

## Finding

Let \(\mathcal H_2(\mathbb C^3)\) be the complex vector space of homogeneous holomorphic quadratic polynomials, with \(L^2\)-norm induced by **probability-normalized** surface measure \(\sigma\) on \(S^5=\{z\in\mathbb C^3:\sum_{a=1}^3|z_a|^2=1\}\). Its dimension is six. The exact orthonormal-basis minimax constant is

\[
\inf_{\{p_1,\ldots,p_6\}\,\mathrm{orthonormal\ basis}}\max_{1\le j\le6}\|p_j\|_{L^\infty(S^5)}=\sqrt2.
\]

An explicit six-element equality basis is built from the six antipodal vertex axes of a regular icosahedron, as follows. Set

\[
\phi=\frac{1+\sqrt5}{2},\qquad \xi=\frac{-7+i\sqrt{15}}8,\qquad L=\sqrt{1+\phi^2},
\]

and let \(v_1,\dots,v_6\in\mathbb R^3\) be the respective vectors

\[
\frac1L(0,1,\phi),\ \frac1L(0,1,-\phi),\ \frac1L(1,\phi,0),\ \frac1L(1,-\phi,0),\ \frac1L(\phi,0,1),\ \frac1L(\phi,0,-1).
\]

Define \(U_j=I_3+(\xi-1)v_jv_j^{\mathsf T}\), and for every \(z\in\mathbb C^3\),

\[
\boxed{p_j(z)=\sqrt2\,z^{\mathsf T}U_jz,\qquad j=1,\dots,6.}
\]

These six polynomials form an orthonormal basis of \(\mathcal H_2(\mathbb C^3)\), with \(\|p_j\|_{L^\infty(S^5)}=\sqrt2\) for every \(j\).

## Assumptions and scope

The bilinear expression \(z^{\mathsf T}Uz\) has **no conjugation** on either occurrence of \(z\). For matrices, \(U^*\) denotes conjugate transpose. The complex sphere carries total mass one. The minimum ranges over all complex orthonormal bases, not just real-coefficient bases. The sole parameter values and the degree are fixed as displayed; no higher-degree conclusion is asserted.

## Proof

**(1) Exact norm and individual lower bound.** Every homogeneous quadratic has a unique representation \(p_M(z)=z^{\mathsf T}Mz\) with \(M\in\mathbb C^{3\times3}\) symmetric. Unitary invariance of probability surface measure gives, for any symmetric \(M,N\),

\[
\int_{S^5}p_M(z)\overline{p_N(z)}\,d\sigma(z)
=\frac{1}{6}\operatorname{tr}(MN^*).
\]

Indeed, for complex dimension \(d\), the fourth-order coordinate moments are

\[
\int_{S^{2d-1}} z_a z_b\overline{z_cz_e}\,d\sigma(z)
=\frac{\delta_{ac}\delta_{be}+\delta_{ae}\delta_{bc}}{d(d+1)},
\]

so the two identical contractions for symmetric matrices yield \(2\operatorname{tr}(MN^*)/[d(d+1)]\), which is \(\operatorname{tr}(MN^*)/6\) at \(d=3\).

The Takagi factorization of a complex symmetric matrix gives \(M=W\operatorname{diag}(s_1,s_2,s_3)W^{\mathsf T}\), with \(W\) unitary and \(s_j\ge0\). Hence

\[
\sup_{\|z\|_2=1}|z^{\mathsf T}Mz|=\max_j s_j=\|M\|_{\mathrm{op}}
\ge\sqrt{\frac{\operatorname{tr}(MM^*)}{3}}.
\]

If \(\|p_M\|_{L^2}=1\), the trace is six, yielding \(\|p_M\|_\infty\ge\sqrt2\). Equality holds precisely when the three singular values of \(M\) are all \(\sqrt2\), equivalently \(M=\sqrt2\,U\) for a symmetric unitary \(U\). Consequently **every** orthonormal basis has maximum sup norm at least \(\sqrt2\).

**(2) Icosahedral equiangularity.** The golden ratio satisfies \(\phi^2=\phi+1\) and \(5\phi^2=(\phi+2)^2\). Inspection of the six explicit vectors shows that for distinct indices \(j,k\), the unnormalized scalar product equals \(\pm\phi\). Therefore

\[
\|v_j\|_2=1,\qquad |v_j^{\mathsf T}v_k|^2=\frac{\phi^2}{(1+\phi^2)^2}=\frac15\quad(j\ne k).
\]

**(3) Symmetric unitary phase reflections.** Put \(Q_j=v_jv_j^{\mathsf T}\). Because \(v_j\) is real and unit, \(Q_j=Q_j^*=Q_j^2\) and \(\operatorname{tr}(Q_j)=1\). The number \(\xi=(-7+i\sqrt{15})/8\) obeys \(|\xi|=1\) and \(\operatorname{Re}\xi=-7/8\). Thus \(U_j=I_3+(\xi-1)Q_j\) is symmetric, has unitary eigenvalues \(1,1,\xi\), and obeys

\[
\operatorname{tr}(U_jU_k^*)
=3+2(\operatorname{Re}\xi-1)+|\xi-1|^2\operatorname{tr}(Q_jQ_k).
\]

For \(j\ne k\), \(\operatorname{tr}(Q_jQ_k)=1/5\), \(2(\operatorname{Re}\xi-1)=-15/4\), and \(|\xi-1|^2=15/4\). Hence the displayed trace equals \(3-15/4+(15/4)/5=0\). When \(j=k\), it equals \(3\), because \(U_j\) is unitary. Therefore

\[
\operatorname{tr}(U_jU_k^*)=3\delta_{jk}.
\]

The norm identity from step (1) gives \(\langle \sqrt2 p_{U_j},\sqrt2 p_{U_k}\rangle=(2/6)\operatorname{tr}(U_jU_k^*)=\delta_{jk}\). With six vectors in a six-dimensional space, they constitute a basis.

Finally, \(\sup_{\|z\|_2=1}|z^{\mathsf T}U_jz|\le1\) by unitarity and Cauchy–Schwarz. Equality holds on any real unit vector orthogonal to \(v_j\), for which \(U_jz=z\) and \(z^{\mathsf T}U_jz=1\). Thus the sup norm of each basis polynomial is exactly \(\sqrt2\), attaining the universal lower bound.

## Verification

A self-contained standard-library script `CHECK.py` evaluates the six normalized axes, checks their off-diagonal squared inner products against \(1/5\), checks phase unitarity and the Frobenius Gram identity, and checks the moment normalization of the basis. It is numerical corroboration of the fully exact identities above, **not** a substitute for the algebraic proof. The exact equalities use only \(\phi^2=\phi+1\), \(|\xi|=1\), and \(\operatorname{Re}\xi=-7/8\).

## Relationship to prior work

Gonçalves, Ferreira and Radziwiłł (2026, arXiv:2610.14160, first publicly posted October 9, 2026) establish existence of uniformly bounded homogeneous orthonormal bases for every complex dimension and every degree, resolving Rudin's question. Their full text gives a dimension-dependent bound, not the sharp quadratic-basis constant \(\sqrt2\) in dimension three or these six icosahedral polynomials. Wang, Zhang and Zhu (2026, arXiv:2610.29946, first posted October 21, 2026) independently give a dimension-uniform construction and a general dimension-dependent bound, not the exact degree-two optimum. These powerful existence theorems do not logically determine the optimal finite-degree constant.

Sych and Leuchs (2009) construct symmetric and antisymmetric orthogonal unitary matrix families using tensor-product Pauli matrices for dimensions that are **powers of two**, which supplies a related matrix-basis viewpoint but does not give a three-by-three six-element symmetric-unitary family. The six real icosahedral equiangular lines and the Takagi factorization are classical ingredients; no novelty is attributed to them alone.

## Limitations

The optimality assertion concerns precisely homogeneous holomorphic degree two in three complex variables, with normalized sphere measure. It does not classify all equality bases and it says nothing about higher degrees. A presently unidentified older construction of an equivalent six-element symmetric-unitary basis could predate the cited work; consequently historical priority is provisional. These claims have received no independent mathematical audit.

## References

1. F. Gonçalves, J. P. Ferreira and M. Radziwiłł, *Uniformly Bounded Orthonormal Bases of Homogeneous Polynomials on the Complex Sphere*, arXiv:2610.14160 (first posted October 9, 2026), https://arxiv.org/abs/2610.14160.
2. P. Wang, F. Zhang and Z. Zhu, *Rudin's Problem on Uniformly Bounded Homogeneous Orthonormal Bases*, arXiv:2610.29946 (first posted October 21, 2026), https://arxiv.org/abs/2610.29946.
3. D. Sych and G. Leuchs, *A complete basis of generalized Bell states*, New Journal of Physics **11** (2009), 013006, https://doi.org/10.1088/1367-2630/11/1/013006.
4. T. Takagi, classical symmetric-matrix singular-value factorization (standard linear algebra theorem).
