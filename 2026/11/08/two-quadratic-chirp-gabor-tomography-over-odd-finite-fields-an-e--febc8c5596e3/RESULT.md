# Two-quadratic-chirp Gabor tomography over odd finite fields: an exact arithmetic rank dichotomy

## Finding
Let \(q=p^s\) be an odd prime power, \(c,d\in\mathbb F_q\) distinct, and \(\psi(z)=\exp(2\pi i\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(z)/p)\). Define the two-chirp window on the additive group of \(\mathbb F_q\) by
\[
 g(x)=\psi(cx^2)+\psi(dx^2).
\]
Its complete \(q^2\)-entry ambiguity-modulus spectrum is specified below by **four arithmetic sectors**, including multiplicities. Consequently the full Weyl-orbit intensity-lifting operator on complex \(q\times q\) matrices has rank
\[
\boxed{\operatorname{rank}\mathcal L_g=\begin{cases}
q^2,&q\equiv1\pmod4\ \text{or}\ s=1,\\[2mm]
q^2-(q-1)(q/p-1),&q\equiv3\pmod4\ \text{and}\ s>1.
\end{cases}}
\]
In the second case, \(s\) is necessarily odd and at least three. The complete nullspace is spanned by the Weyl matrix directions labeled by \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(-(b-2ca)(b-2da)/(2(c-d)))=0\) with \((b-2ca)(b-2da)\ne0\). In the first case the full Gabor intensity data determine every signal up to a global phase.

Write \(h=c-d\), \(\eta=(-1)^{(q-1)/2}\), and \(G=\sum_{x\in\mathbb F_q}\psi(hx^2)\). Then \(|G|=\sqrt q\), \(\overline G=\eta G\), and \(G\) is real when \(\eta=1\). The complete multiset of the \(q^2\) nonnegative numbers \(|A_g(a,b)|\), for the convention below, is:

1. \(2q+(1+\eta)G\), multiplicity \(1\).
2. \(q+(1+\eta)G\), multiplicity \(2(q-1)\).
3. \(\sqrt q\,|1+\eta|\), multiplicity \((q-1)(q/p-1)\).
4. For each integer \(1\le j\le(p-1)/2\), \(\sqrt q\,|e^{2\pi i j/p}+\eta|\), multiplicity \(2(q-1)q/p\).

The first two displayed values are strictly positive real numbers. When \(q/p=1\), sector 3 is absent. The four sectors count exactly \(q^2\) entries; coincident numerical moduli must have their multiplicities added. The singular values of \(\mathcal L_g\), with these same multiplicities, are \(\sqrt q\) times the displayed moduli.

If \(\mathcal L_g\) is invertible, its sharp Hilbert--Schmidt-to-Euclidean condition number is
\[
\boxed{\kappa(\mathcal L_g)=\frac{2q+(1+\eta)G}{m_{q,h}},\qquad
m_{q,h}=\begin{cases}
\min\{q+2G,\ 2\sqrt q\sin(\pi/(2p))\},&\eta=1,\\[2mm]
2\sqrt p\sin(\pi/p),&\eta=-1\ (\text{thus }q=p).
\end{cases}}
\]
In the last branch this simplifies to \(\kappa=\sqrt p/\sin(\pi/p)\). For \(\eta=-1\) and \(s>1\), \(\mathcal L_g\) is singular so no finite condition number is asserted.

## Assumptions and scope
The group is \((\mathbb F_q,+)\), **not** the cyclic group of order \(q\) when \(s>1\). All operators are complex-linear on the full \(q^2\)-dimensional matrix space. For \(a,b\in\mathbb F_q\), put \((T_af)(x)=f(x-a)\), \((M_bf)(x)=\psi(bx)f(x)\), and \(W_{a,b}=M_bT_a\). The associated complete complex-linear lifted map is
\[
 \mathcal L_g(H)=\left(\operatorname{tr}\bigl(H\,W_{a,b}gg^*W_{a,b}^*\bigr)\right)_{(a,b)\in\mathbb F_q^2}.
\]
Equip matrices with the unnormalized Hilbert--Schmidt inner product and data vectors with the unnormalized Euclidean norm; \(g\) is not normalized. The ambiguity convention is
\[
 A_g(a,b)=\sum_{x\in\mathbb F_q}g(x+a)\overline{g(x)}\,\psi(-bx).
\]
The self-ambiguity coefficient may differ from \(\langle g,W_{a,b}g\rangle\) by a unit phase and index inversion, which does not change its modulus or zero pattern. Rank and nullity refer to the complex-linear lifted operator; the claim in singular cases makes **no assertion that nonlinear pure-state phase retrieval fails**. Distinct slopes \(c\ne d\) and odd characteristic are essential.

## Proof
**1. The two auto-chirp lines and two cross-chirp Gauss sums.** Expand the four terms in the ambiguity coefficient. Orthogonality of additive characters gives
\[
\sum_x\psi(c((x+a)^2-x^2)-bx)
=q\psi(ca^2)\mathbf1_{\{b=2ca\}},
\]
and similarly for slope \(d\). Completing the square in the two mixed terms yields
\[
\begin{split}
U&=ca^2-\frac{(2ca-b)^2}{4h},\\
V&=da^2+\frac{(2da-b)^2}{4h},\\
A_g(a,b)&=q\psi(ca^2)\mathbf1_{\{b=2ca\}}
+q\psi(da^2)\mathbf1_{\{b=2da\}}+G\bigl(\psi(U)+\eta\psi(V)\bigr).
\end{split}
\]
Here \(\sum_x\psi(-hx^2)=\eta G\), using the quadratic-character evaluation, and \(|G|=\sqrt q\) follows from ordinary Gauss-sum orthogonality. Also \(\overline G=\eta G\). The two line equations intersect only at \((a,b)=(0,0)\). At their intersection, \(U=V=0\) and the modulus is \(2q+(1+\eta)G\). At a point on exactly one line, \(U=V=ca^2\) (respectively \(da^2\)) and the modulus is \(q+(1+\eta)G\). When \(\eta=1\), \(q\ge5\), hence \(q+2G\ge q-2\sqrt q>0\); for \(\eta=-1\) the latter is \(q\). Thus these values are positive, as stated.

**2. Off-line phase difference and exact multiplicities.** Off the two lines, the exact algebraic identity is
\[
 U-V=-\frac{(b-2ca)(b-2da)}{2(c-d)}=:\Delta(a,b),
\]
and therefore \(|A_g(a,b)|=\sqrt q\,|\psi(\Delta(a,b))+\eta|\). The change of variables
\[
 (a,b)\longmapsto(u,v)=(b-2ca,b-2da)
\]
has nonzero determinant \(2(c-d)\) over \(\mathbb F_q\). Off-line pairs correspond exactly to \(u,v\ne0\), and for every \(\delta\in\mathbb F_q^\times\), precisely \(q-1\) such pairs have \(\Delta=\delta\). The finite-field trace is surjective and each fiber has size \(q/p\), so the trace-zero fiber contains exactly \(q/p-1\) nonzero elements, whereas every nonzero trace fiber contains \(q/p\). Thus trace zero gives sector 3, and the two traces \(j\) and \(-j\) for \(1\le j\le(p-1)/2\) give sector 4. Their multiplicities add up to
\[
1+2(q-1)+(q-1)(q/p-1)+(p-1)(q-1)q/p=q^2.
\]

**3. Exact zeros.** For odd \(p\), \(1+\psi(\delta)\ne0\) since a \(p\)-th root of unity is never \(-1\). If \(\eta=1\), no off-line entry vanishes. If \(\eta=-1\), off-line entries vanish exactly when \(\psi(\delta)=1\), or equivalently \(\operatorname{Tr}(\delta)=0\). Therefore there are \((q-1)(q/p-1)\) zeros. When \(q=p\) the trace is the identity and the count is zero; for \(s>1\) it is positive. The congruence \(q\equiv3\pmod4\) forces \(p\equiv3\pmod4\) and odd \(s\), so its nonprime case has \(s\ge3\).

**4. Spectral diagonalization.** The operators \(W_{a,b}/\sqrt q\) form an orthonormal basis of the complex matrix space because \(\operatorname{tr}(W_{a,b}^*W_{a',b'})=q\mathbf1_{\{(a,b)=(a',b')\}}\). Conjugating a Weyl basis vector by \(W_{u,v}\) multiplies it by a symplectic phase-space character. Hence the columns of \(\mathcal L_g\) on the normalized Weyl basis are orthogonal, with column norm \(\sqrt q\,|A_g(a,b)|\). This proves the complete singular-value multiset and that its nullspace is the span of the zero-ambiguity Weyl directions. If every singular value is nonzero, the lifted intensity data are informationally complete on matrices; in particular they recover every rank-one matrix \(ff^*\) and consequently the signal \(f\) up to global phase.

**5. Sharp endpoints.** The largest ambiguity modulus is \(A_g(0,0)=\|g\|_2^2=2q+(1+\eta)G\), by Cauchy--Schwarz, with equality at the origin. For \(\eta=1\), sector-4 moduli have minimum \(2\sqrt q\sin(\pi/(2p))\) (achieved at trace \(\pm(p-1)/2\)); sector 3 has modulus \(2\sqrt q\), and sector 2 has modulus \(q+2G\). For \(\eta=-1\) with \(q=p\), sector 3 is absent and the smallest sector-4 modulus equals \(2\sqrt p\sin(\pi/p)\), attained at traces \(\pm1\); it is at most the sector-2 value \(p\), including equality when \(p=3\). Multiplying all singular values by \(\sqrt q\) cancels in the condition-number ratio. This proves the claimed sharp formula.

## Verification
The companion standard-library `checker.py` independently constructs prime fields of orders \(3,5,7,11,13,17,19\) and extension fields of orders \(9,25,27,49\), including irreducible-polynomial multiplication. For multiple distinct slope pairs in every field it directly enumerates every \((a,b)\), recomputes the ambiguity by its defining \(q\)-term sum, checks the explicit complex formula, its modulus, every trace multiplicity, all zeros, largest and smallest moduli, and the complete Moyal energy identity. The output ends with `ALL_QUADRATIC_PAIR_AMBIGUITY_CHECKS_PASS`. In particular the predicted lifted nullity is \(208\) at \(q=27\) (rank \(521\)), but zero at \(q=3,9,25,49\). Floating-point root-of-unity checks are tolerance-based, while field operations and trace counts use exact integer residues. Finite computation corroborates rather than proves the universal claim.

## Relationship to prior work
Casazza and Fickus [1] analyze single finite chirps and their Fourier transforms, not the ambiguity and operator-span rank for a **sum of two distinct quadratic chirps over extension fields**. Bojarovska and Flinth [2] supply the general Fourier-diagonal Gabor phase-retrieval principle, but their inspected criterion does not calculate this window's finite-field trace fibers, spectral multiplicities, sharp conditioning, or the prime-versus-extension obstruction. The published single-impulse chirp work [3] treats \(\psi(cx^2)+t\mathbf 1_{\{0\}}\), not a second chirp, and obtains a cyclic-group parity obstruction; it cannot imply the present trace-based rank dichotomy by substituting an impulse. The single-chirp local phase-Hessian result [4] concerns infinitesimal constant-amplitude deformations rather than full quadratic-pair Gabor tomography. The hyperbolic-shell indicator result [5] uses a different matrix signal, quadratic level sets, and a different zero mechanism. The later algebraic perturbation construction [6] is broader for stable window existence and may have better margins, but its accessible abstract does not address the exact spectral problem here; full-text comparison remains outstanding.

## Limitations
The theorem is for equal unit coefficients of two distinct quadratic chirps, with the canonical additive character, over odd finite fields. It does not classify unequal coefficients, composite cyclic rings, or even characteristic. Full operator-span noninjectivity at odd extension fields with \(q\equiv3\pmod4\) does not imply failure of nonlinear phase retrieval. The proof gives sharp conditioning only for invertible cases and does not optimize among all windows. Historic radar and coded-waveform literature may contain a formula equivalent to the cross-chirp ambiguity; an unidentified result of that kind remains a priority risk. No independent mathematical audit has been performed.

## References
1. P. G. Casazza and M. Fickus, *Fourier Transforms of Finite Chirps*, EURASIP Journal on Applied Signal Processing (public issue dated 2006-12-01), DOI:10.1155/ASP/2006/70204; primary article text and Fourier/chirp sections inspected.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (first posted 2015-03-19), especially Theorems 2.2 and 2.3; full open preprint inspected.
3. *Single-impulse quadratic chirps: exact cyclic Gabor tomography spectrum and arithmetic rank obstruction*, published-finding identifier `2026/10/11/SCOPE-single-impulse-quadratic-chirps-exact-cyclic-gabor-tomography-sp--03361b3cff9c`; RESULT.md read in full.
4. *Quadratic chirp phase Hessians over odd finite vector spaces*, published-finding identifier `2026/10/11/SCOPE-quadratic-chirp-phase-hessians-over-odd-finite-vector-spaces--aface8382344`; RESULT.md read in full.
5. *Exact Gabor tomography rank for hyperbolic quadratic shells over odd finite fields*, published-finding identifier `2026/10/11/SCOPE-exact-gabor-tomography-rank-for-hyperbolic-quadratic-shells-over--b9e240edb677`; RESULT.md read in full.
6. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614v1 (2026); only abstract accessible for comparison.
