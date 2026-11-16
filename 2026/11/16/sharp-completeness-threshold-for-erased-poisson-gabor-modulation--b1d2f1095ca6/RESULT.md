# Sharp completeness threshold for erased Poisson Gabor modulation rows

## Finding
For every \(w>0\), let \(g_w(t)=(t^2+w^2)^{-1}\), and consider the half-frequency-sampled Gabor family
\[
\mathcal G_{w,E}=\{e^{\pi i m t}g_w(t-n):n\in\mathbb Z,\ m\in\mathbb Z\setminus E\},
\]
where \(E\) is a finite set of *entire erased modulation rows*; one row contains all integer translates at the specified modulation. The following completeness statements are exact:

1. For every \(E\) with \(|E|\le3\), the surviving family is complete in \(L^2(\mathbb R)\).
2. For every \(E\) with \(|E|=4\), the family is incomplete **if and only if** \(E\) consists of four consecutive integers.
3. For a block of four consecutive erased modulation indices, the orthogonal complement of the surviving closed span is canonically isomorphic to \(L^2(0,1/2)\), and an explicit three-tap formula describes every vector in it.
4. Removing three consecutive rows yields a **complete but nonframe** family. This is the sharp stability/completeness distinction: there is no positive lower frame bound despite completeness, whereas four consecutive missing rows cause an infinite-dimensional defect.

The new contributions are the sharp **completeness** classification through four erased rows and the explicit defect space. The frame/nonframe transition for three consecutive missing rows is compatible with, and also follows from, the broader frame criterion of Belov–Semenov; it is not asserted as a new frame classification.

## Assumptions and scope
The Fourier transform is \(\widehat f(\xi)=\int_{\mathbb R}f(t)e^{-2\pi i t\xi}\,dt\). It sends \(g_w\) to \((\pi/w)e^{-2\pi w|\xi|}\). Write
\[
\lambda=2\pi w,\qquad r=e^{-\lambda}\in(0,1),\qquad h(t)=e^{-\lambda|t|}.
\]
Fourier conjugacy converts the completeness question, without changing any nullity, to the system \(\{M_nT_{m/2}h:n\in\mathbb Z,m\notin E\}\); phases of individual atoms are immaterial. The original lattice is a frame before erasure. Our assertion treats the number and positions of *whole modulation rows*, not deletion of finitely many individual atoms and not deletion of translation columns.

To describe the defect for the canonical block \(E_0=\{-1,0,1,2\}\), use the unitary fiberization
\[
\mathcal U F(x)=\bigl(F(x+k)\bigr)_{k\in\mathbb Z},\quad 0\le x<1.
\]
In Fourier coordinates, the exact orthogonal complement for the erased system consists of the functions \(F\in L^2(\mathbb R)\) for which, for some arbitrary \(c\in L^2(0,1/2)\),
\[
F(x+k)=
\begin{cases}
c(x)\bigl((1+r^2)\mathbf1_{k=0}-r\mathbf1_{k=-1}-r\mathbf1_{k=1}\bigr),&0<x<1/2,\\
0,&1/2<x<1,
\end{cases}
\]
for almost every \(x\) and every \(k\in\mathbb Z\). In the original variables these are the inverse Fourier transforms of such \(F\). Their squared norms are \((1+4r^2+r^4)\|c\|_{L^2(0,1/2)}^2\). Any consecutive four-row block is reduced to \(E_0\) by a frequency modulation, which is unitary.

## Proof
**1. Fiber analysis and the two parity filters.** Let \(F\in L^2(\mathbb R)\) and put \(u_k(x)=F(x+k)\). Parseval for the integer modulation family yields
\[
\sum_{n\in\mathbb Z}|\langle F,M_nT_{m/2}h\rangle|^2
=\int_0^1\left|\sum_{k\in\mathbb Z}u_k(x)h(x+k-m/2)\right|^2\,dx.
\]
The sequences \(\{h(x+k-m/2)\}\) have uniformly summable tails. Thus the displayed analysis fiber is bounded, norm-continuous in \(x\), and admits the Laurent transform \(U_x(z)=\sum_k u_k(x)z^k\) in \(L^2(\mathbb T)\). For \(j\in\mathbb Z\), the coefficient corresponding to the even row \(m=2j\) equals the coefficient of \(z^j\) in \(U_x(z)\overline{V_0(x,z)}\), while the odd row \(m=2j+1\) is the coefficient of \(z^j\) in \(U_x(z)\overline{V_1(x,z)}\), where
\[
V_0(x,z)=\sum_{k\in\mathbb Z}h(x+k)z^k,\qquad
V_1(x,z)=\sum_{k\in\mathbb Z}h(x+k-1/2)z^k.
\]
The products and conjugates are taken on \(|z|=1\).

**2. Rational, coprime filter symbols.** Let \(D(z)=(1-rz)(1-rz^{-1})\), strictly positive and nonvanishing on \(|z|=1\). For \(0<x<1/2\), summing the two geometric tails gives
\[
\overline{V_0(x,z)}=\frac{A_0+B_0z}{D(z)},\qquad
\overline{V_1(x,z)}=\frac{A_1+B_1z^{-1}}{D(z)},
\]
where
\[
\begin{split}
A_0&=e^{-\lambda x}-r^2e^{\lambda x},&B_0&=r(e^{\lambda x}-e^{-\lambda x}),\\
A_1&=e^{\lambda(x-1/2)}-r^2e^{-\lambda(x-1/2)},&
B_1&=r(e^{-\lambda(x-1/2)}-e^{\lambda(x-1/2)}).
\end{split}
\]
All four coefficients are strictly positive for \(0<x<1/2\). Direct multiplication gives the nonzero determinant
\[
A_0A_1-B_0B_1=\sqrt r\,(1-r)^2(1+r)>0.
\]
Hence the two Laurent binomials \(N_0=A_0+B_0z\) and \(N_1=A_1+B_1z^{-1}\) are coprime in \(\mathbb C[z,z^{-1}]\), uniformly in the interior \(x\). For \(1/2<x<1\), writing \(y=x-1/2\), the identities \(V_0(x,z)=z^{-1}V_1(y,z)\) and \(V_1(x,z)=V_0(y,z)\) give
\[
\overline{V_0(x,z)}=\frac{B_1(y)+A_1(y)z}{D(z)},\quad
\overline{V_1(x,z)}=\frac{A_0(y)+B_0(y)z}{D(z)}.
\]
These are again coprime genuine Laurent binomials, this time supported at exponents \(0,1\) in both channels. Endpoint fibers \(x=0,1/2\) do not affect completeness.

**3. Kernel divisibility.** If the fiber input \(U\ne0\) is annihilated by every surviving row, the two products \(U N_0/D=P\) and \(U N_1/D=Q\) are Laurent polynomials: their coefficients are supported only at the finitely many erased even and odd indices respectively. Neither polynomial is identically zero because \(N_j/D\ne0\) almost everywhere on \(\mathbb T\). Thus \(PN_1=QN_0\), and coprimeness in the Laurent polynomial ring forces
\[
P=N_0R,\qquad Q=N_1R,\qquad U=DR
\]
for some nonzero Laurent polynomial \(R\). Conversely every such \(R\) whose two parity outputs are supported in erased rows gives a fiber-kernel vector. This algebraic reduction is exact; no finite truncation is used.

**4. Four outputs are necessary, with equality only for a single monomial.** Suppose first \(0<x<1/2\), and write the minimum and maximum occupied Laurent exponents of \(R\) as \(p\le q\). Because each binomial has nonzero endpoints, \(N_0R\) has nonzero coefficients at \(p,q+1\) and \(N_1R\) has nonzero coefficients at \(p-1,q\). The corresponding four distinct erased row indices are
\[
2p-1,\quad2p,\quad 2q+1,\quad2q+2.
\]
If \(p=q\), these are precisely four consecutive integers and the whole output is supported on them. If \(p<q\), simultaneous cancellation of the two additional coefficients \([z^{p+1}](N_0R)\) and \([z^p](N_1R)\) would require
\[
A_0R_{p+1}+B_0R_p=0,\qquad
A_1R_p+B_1R_{p+1}=0,
\]
which contradicts \(A_0A_1-B_0B_1\ne0\) because \(R_p\ne0\). Therefore at least five distinct rows are needed whenever \(p<q\).

For \(1/2<x<1\), the two binomials both have support \(\{0,1\}\). The four extreme outputs are \(2p,2p+1,2q+2,2q+3\). The two first internal outputs again cannot vanish simultaneously because their coefficient determinant is \(A_0A_1-B_0B_1\ne0\). Thus at most four erased rows permit a nonzero fiber kernel **only** when \(R\) is a monomial, and then the erased four rows must be consecutive. In particular, any erasure of at most three rows and any nonconsecutive four-row erasure has a trivial fiber kernel for almost every \(x\), hence is complete.

**5. The four-row defect is exactly one function degree of freedom.** For \(E_0=\{-1,0,1,2\}\), the only possible interior kernel occurs at \(0<x<1/2\), where \(R\) must be a multiple of \(z^0\), because the four obligatory rows are \(\{-1,0,1,2\}\). Thus \(U=D R\), whose three Fourier coefficients are \(-r,1+r^2,-r\) at \(-1,0,1\). For \(1/2<x<1\), every potential four-row block starts at an even integer, whereas \(E_0\) starts at an odd integer; there is no fiber kernel. Therefore the displayed family of \(F\)'s in the scope section exhausts the orthogonal complement. Since \(c\) is an arbitrary \(L^2(0,1/2)\) function, the defect is infinite-dimensional and canonically isomorphic to that space. The harmless overall Fourier scalar \(\pi/w\) does not affect nullity.

**6. The three-row borderline is complete but not a frame.** Take \(E_3=\{-1,0,1\}\). Step 4 proves completeness. Let \(u=( -r,1+r^2,-r)\) supported on fiber coordinates \(-1,0,1\). For \(0<x<1/2\), the output vanishes outside the four rows \(\{-1,0,1,2\}\), and its *only surviving* coefficient for the three-row erased system is
\[
\sum_{k=-1}^1u_kh(x+k-1)=r(e^{\lambda x}-e^{-\lambda x})=2r\sinh(\lambda x).
\]
The squared norm of \(u\) is \(1+4r^2+r^4\). Thus unit fiber test functions supported arbitrarily near \(x=0^+\) have remaining coefficient energy bounded above by \(4r^2\sinh^2(\lambda\delta)/(1+4r^2+r^4)\), which tends to zero with \(\delta\downarrow0\). This excludes a positive frame lower bound. Integer translation of the erased modulation block is achieved by a unitary modulation of the original signals, proving the assertion for every three consecutive erasures.

## Verification
A standalone `CHECK.py` recomputes geometric-series Zak symbols against truncated infinite series, evaluates the nonzero resultant across positive widths and interior positions, verifies the three-tap outputs and the predicted erased supports, and checks that the near-border surviving coefficient vanishes quadratically in energy. The script has no nonstandard dependencies and can be run with `python3 CHECK.py`. Its finite numerical checks illustrate the exact algebra but do not establish the infinite-dimensional theorem; Steps 1–6 do.

## Relationship to prior work
Belov and Semenov, *Irregular Gabor Frames for the Poisson Kernel* (first public version 21 October 2026), Theorem 1, prove a **general criterion for the frame property** for a Poisson window and arbitrary finite-upper-density modulation sets with regular translation lattice. In particular their theorem covers whether the surviving systems here are frames. The present statement explicitly does **not** claim novelty for the frame classification: its new invariant is **completeness**, including the precise four-erasure minimum, all four-row equality cases, the complete-but-nonframe borderline, and the explicit full defect space. Nonframe status alone never proves incompleteness, and the cited frame criterion does not specify the closed-span orthogonal complement.

A separate published result, *Finite-column erasure robustness for Poisson Gabor frames at half-frequency sampling* (published-finding corpus, 2 November 2026), establishes stability under removal of arbitrary finite collections of **translation** columns. Fourier conjugacy exchanges the exponential and Poisson windows, not the same-window erased-row and erased-column questions; the result does not imply the four-modulation-row completeness classification. The complete rectangular-lattice frame property follows from classical totally-positive Gabor theory, recently unified by de Dios Pont et al. (2026), but imposes no such erased-row completeness threshold. These source comparisons are statement/implication comparisons, not mere title matches.

## Limitations
The theorem covers exactly the half-frequency modulation step, unit translation step, and Poisson kernel of arbitrary positive width. No claim is made for general density-two Gabor windows or arbitrary irregular modulation sets. It does not give best lower frame bounds, the complete frame/nonframe pattern for every larger erasure mask, or a full classification of completeness for five or more erased rows. The novelty comparison is relative to accessible primary texts and indexed prior findings, not a proof of publication priority. Independent audit has not been performed.

## References
1. Y. Belov and A. V. Semenov, *Irregular Gabor Frames for the Poisson Kernel*, arXiv:2610.30037v1, 21 October 2026, https://arxiv.org/abs/2610.30037 .
2. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska and M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1, 5 August 2026, https://arxiv.org/abs/2608.04992 .
3. *Finite-column erasure robustness for Poisson Gabor frames at half-frequency sampling*, published-finding corpus research record, 2 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-finite-column-erasure-robustness-for-poisson-gabor-frames-at-hal--7c7db041a86a .
4. K. Gröchenig and S. Koppensteiner, *Gabor frames: characterizations and coarse structure*, arXiv:1803.05271, 2018, https://arxiv.org/abs/1803.05271 .
