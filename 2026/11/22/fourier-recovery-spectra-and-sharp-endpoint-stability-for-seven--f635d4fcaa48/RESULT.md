# Fourier recovery spectra and sharp endpoint stability for seven-point masks on the seven-by-seven plane

## Finding
Let \(G=\mathbb F_7^2\) with counting measure, let \(S\subset G\) have exactly seven points, and let \(T_Su=\mathbf1_S*u\) act on complex functions on \(G\). For \(r=\operatorname{rank}_{\mathbb C}(T_S)\), the **complete** distribution among all \(\binom{49}{7}=85{,}900{,}584\) masks is

| \(r\) | Number of masks |
|---:|---:|
| \(7\) | \(56\) |
| \(31\) | \(5{,}488\) |
| \(37\) | \(123{,}480\) |
| \(43\) | \(6{,}324{,}528\) |
| \(49\) | \(79{,}447{,}032\) |

All unlisted ranks are impossible. Rank \(7\) occurs precisely for affine lines; every rank-\(31\) mask is an affine image of the seven-point graph \(C=\{(t,t^4):t\in\mathbb F_7\}\), and no other non-line mask has as small a rank. For **each** of the \(5{,}488\) rank-\(31\) masks, the complete squared singular-value distribution of \(T_S\) (counting multiplicity) is
\[
\boxed{0:18,\qquad 7:18,\qquad 14:12,\qquad 49:1.}
\]
Let \(W_S=\operatorname{ran}(T_S)\), regarded as a subspace of either \(\ell^1(G)\) or \(\ell^\infty(G)\). Among **all** complex-linear projections \(P\) onto \(W_S\), including ones not commuting with translations, the sharp norm is
\[
\boxed{\inf_{P^2=P,\ \operatorname{ran}P=W_S}\|P\|_{1\to1}
=\inf_{P^2=P,\ \operatorname{ran}P=W_S}\|P\|_{\infty\to\infty}
=\frac{193}{49}.}
\]
The minimum is realized by the Fourier spectral projection. Consequently the smallest positive convolution singular value is \(\sqrt7\) and its Moore–Penrose inverse has \(\ell^2\)-operator norm \(1/\sqrt7\). These constants are for **unit-coefficient indicator convolution**, not arbitrary complex coefficients on a fixed support.

## Assumptions and scope
Fourier characters are \(\chi_\xi(x)=\exp(2\pi i\langle \xi,x\rangle/7)\) for \(\xi,x\in G\). The unnormalized Fourier transform is \(\widehat f(\xi)=\sum_{x\in G}f(x)\overline{\chi_\xi(x)}\). Convolution is the unnormalized sum \((f*u)(x)=\sum_yf(y)u(x-y)\). Thus \(\widehat{T_Su}(\xi)=\widehat{\mathbf1_S}(\xi)\widehat u(\xi)\), and the singular values on the unnormalized \(\ell^2\) space are \(|\widehat{\mathbf1_S}(\xi)|\). No probability, continuous interpolation, nonlinear phase-retrieval or arbitrary-weight assertion is included.

A projective direction is one of the eight one-dimensional subspaces of \(G\). Call a direction *blind* for \(S\) when no difference of two distinct points of \(S\) lies in that direction. For \(|S|=7\), this is equivalent to meeting every parallel affine line in that direction exactly once.

## Proof
**1. From Fourier zeros to missing directions.** Fix a nonzero \(\xi\). Let \(c_j\) count the points of \(S\) for which \(\langle\xi,x\rangle=j\). Then \(\widehat{\mathbf1_S}(\xi)=\sum_{j=0}^6c_j\zeta^{-j}\), where \(\zeta=\exp(2\pi i/7)\) and \(\sum_jc_j=7\). The only rational relation among \(1,\zeta,\dots,\zeta^6\) is a multiple of \(\Phi_7=1+\cdots+z^6\); hence this transform vanishes exactly when every \(c_j=1\). That means the direction \(\ker\xi\) is blind. Each of the eight possible blind directions accounts for six nonzero Fourier characters, and the character families are disjoint. Consequently
\[
\operatorname{rank}(T_S)=49-6k(S),
\]
where \(k(S)\) is the number of blind directions.

**2. Three specified blind directions.** An invertible linear change of coordinates takes any three distinct blind directions to those whose transversals have the form \(S=\{(x,f(x)):x\in\mathbb F_7\}\), with \(f\) and \(f-x\) both permutations. Write the unique interpolating polynomial for \(f\) with degree at most six. Since every permutation has first two power sums equal to \(\sum_xx=\sum_xx^2=0\), applying these sums to \(f\) and \(f-x\) yields \(\sum_xf(x)=0\) and \(\sum_xxf(x)=0\). The finite-field power-sum identity \(\sum_xx^j=0\) for \(0\le j\le5\), while \(\sum_xx^6=-1\), removes the degree-six and degree-five coefficients. Thus \(\deg f\le4\).

A genuine cubic, after input and output translations, has shape \(Ax^3+Dx\), with \(A\ne0\). But its square has sum \(-A^2\ne0\), contradicting the permutation condition. Quadratics cannot permute an odd field by reflection about their vertex. Therefore \(f\) is affine or quartic. In the quartic case, an input translation kills the cubic term, an output translation kills the constant, and the square-sum condition removes the quadratic term, leaving \(Ax^4+Dx\) with \(A\ne0\).

For nonzero \(x\), the value of \(x^3\) is \(1\) on \(H=\{1,2,4\}\) and \(-1\) on \(-H=\{3,5,6\}\). Accordingly \(Ax^4+Dx\) permutes the field precisely when \(D+A\) and \(D-A\) are nonzero and \((D+A)/(D-A)\in H\). Direct substitution into the six possibilities for nonzero \(A\) gives the exact permitted \(D\) pairs
\[
A=1,2,3,4,5,6:\quad (3,4),(1,6),(2,5),(2,5),(1,6),(3,4).
\]
Requiring the same for \(Ax^4+(D-1)x\) forces \(A=\pm1\), \(D=4\). Undoing translations gives exactly the \(98\) nonlinear graphs
\[
 f(x)=b+4(x-a)+\epsilon(x-a)^4,
 \quad a,b\in\mathbb F_7,\quad \epsilon\in\{1,-1\}.
\]
There are also exactly \(35\) affine graphs \(f(x)=b+cx\) with \(b\in\mathbb F_7\), \(c\in\{2,3,4,5,6\}\). Thus a prescribed triple of directions is blind for exactly \(133\) masks. Each of the \(98\) nonlinear masks has **no fourth** blind direction: for an additional slope \(m\), the requirement that \(f-mx\) permute would require \(4-m\in\{3,4\}\), so only the two slopes already chosen work. Every affine line has seven blind directions.

**3. Whole-population counting.** There are \(8\cdot7=56\) affine lines, each with seven blind directions. For any prescribed single blind direction there are \(7^7=823{,}543\) masks, since each of the seven parallel lines contributes one independently selected point. For two specified blind directions there are \(7!=5040\) masks, since the set is a permutation graph. By the preceding classification, a prescribed pair lies in \(6\cdot98\) nonlinear triple-blind masks and in \(6\cdot7\) affine lines. It therefore lies in precisely \(5040-6\cdot98-6\cdot7=4410\) masks with exactly two blind directions. The counts with exactly three and exactly two blind directions are
\[
N_3=\binom83\cdot98=5488,\qquad N_2=\binom82\cdot4410=123480.
\]
For a fixed direction, the number of masks with **exactly that one** blind direction is
\[
7^7-7\cdot4410-\binom72\cdot98-7\cdot7=790566.
\]
Thus \(N_1=8\cdot790566=6{,}324{,}528\), and subtraction from \(\binom{49}{7}\) gives \(N_0=79{,}447{,}032\). No four-, five-, six- or eight-blind-direction masks exist. The rank distribution follows from step 1. The affine equivalence of the \(5488\) nonlinear extremizers follows from the coordinate normalization and the displayed quartic family; it also agrees with the classical equality classification for the Rédei direction bound.

**4. Exact nonzero singular values at rank \(31\).** Affine translations multiply Fourier coefficients by phases, and invertible affine linear changes permute their frequency labels. Hence it suffices to examine \(C=\{(t,t^4):t\in\mathbb F_7\}\). Since \(t^4=t\) on \(H\) and \(t^4=-t\) on \(-H\), its Fourier multiplier (up to conjugation) is
\[
M(u,v)=1+\sum_{t\in H}\zeta^{(u+v)t}+\sum_{t\in-H}\zeta^{(u-v)t}.
\]
Set \(A=\zeta+\zeta^2+\zeta^4=(-1+i\sqrt7)/2\) and \(B=\overline A\), so \(A+B=-1\), \(AB=2\). The multiplier is \(7\) at the origin. On the two punctured diagonals \(u+v=0\) or \(u-v=0\), its magnitude squared is \(|4+A|^2=|4+B|^2=14\), at twelve points. At the remaining 36 frequencies it is either \(1+2A=i\sqrt7\), \(1+2B=-i\sqrt7\), or \(1+A+B=0\). Exactly eighteen are zero and eighteen have squared magnitude seven, by the two quadratic-character classes. This proves the displayed singular-value multiplicities.

**5. Exact optimal endpoint projection norm.** The zero-frequency set in coordinates \(a=u+v\), \(b=u-v\) consists of the 18 pairs with \(a,b\ne0\) and the *same* quadratic-character sign: \(H\times H\) and \((-H)\times(-H)\). Let \(Z\) be that set. The Fourier transform of its indicator, written in dual coordinates \((r,s)\), is
\[
 h(r,s)=\big(\sum_{t\in H}\zeta^{rt}\big)\big(\sum_{t\in H}\zeta^{st}\big)
 +\big(\sum_{t\in-H}\zeta^{rt}\big)\big(\sum_{t\in-H}\zeta^{st}\big).
\]
The identities for \(A,B\) show that \(h\) has exactly one value \(18\), eighteen values \(4\), and thirty values \(-3\). The canonical Fourier range projection has convolution kernel \(K=\delta_0-\widehat{\mathbf1_Z}/49\); its 49 kernel entries consequently have exactly the values and multiplicities
\[
(31/49):1,\qquad (-4/49):18,\qquad (3/49):30.
\]
Its \(\ell^1\)- and \(\ell^\infty\)-operator norms both equal the \(\ell^1\) sum of this kernel, namely \((31+18\cdot4+30\cdot3)/49=193/49\).

Finally, let \(P\) be any projection onto \(W_S\). Average its conjugates by the 49 translations of \(G\). This yields a translation-invariant projection \(\overline P\) onto \(W_S\), with norm no greater than \(\|P\|\) in either endpoint norm, because translations are isometries. On the Fourier side, every translation-invariant projection with this range must multiply by one on the 31 visible frequencies and by zero on the 18 invisible frequencies. It is therefore exactly the spectral projection just computed. This proves optimality **among all projections**, not just Fourier multipliers.

## Verification
Three standalone exact-arithmetic programs are included. `verify_all_masks.cpp` enumerates each of the \(85{,}900{,}584\) unordered seven-point subsets directly, tracking all determined difference directions using bit masks; it reproduces the five-rank histogram without numerical Fourier operations. `verify_permutation_polynomials.py` independently enumerates all \(5040\) permutations, isolates the \(133\) orthomorphisms, verifies the complete quartic-or-affine formula, and reconstructs the population counts by incidence. `verify_spectral_projection.py` computes all Fourier squared magnitudes in \(\mathbb Z[z]/(\Phi_7(z))\) and all 49 projection-kernel coefficients exactly, recovering \(0:18,7:18,14:12,49:1\) and the sharp kernel norm \(193/49\). Each program was executed successfully after being assembled; the all-mask program is a finite exhaustive check, while the displayed algebraic proof establishes the classification and endpoint optimality.

Run `python3 verify_permutation_polynomials.py`, `python3 verify_spectral_projection.py`, and `c++ -std=c++17 -O3 verify_all_masks.cpp -o verify_all_masks && ./verify_all_masks` in the directory containing the included files. The C++ executable is created locally, not embedded.

## Relationship to prior work
The Fourier transform and finite-field counting normalization follow the framework of Mockenhaupt–Tao (2002). Rédei–Megyesi's lower bound and Lovász–Schrijver's **1981 classification** already prove that a noncollinear seven-point set determines at least five directions and that equality cases are affine images of \(C\). Neither geometric statement is claimed as new. Literature on orthomorphisms/permutation polynomials contains the 133 count, which is likewise **not claimed as a new standalone number**. These results supply (or readily imply) much of the underlying rank-counting geometry. The new quantitative conclusion here is the **complete singular-value law and especially the sharp \(193/49\) endpoint projection constant, optimal even among non-translation-invariant projections**, for every extremal noncollinear convolution mask. The global rank population is included to place that spectral-stability conclusion in its natural complete support population and is not claimed to be independent of the cited finite-geometry theorems.

A previously published exact fourth-moment extension theorem concerns arbitrary complex weights on this *same* quartic curve and the \(\ell^2\)-to-\(L^4\) restriction norm. Its full result and proof were inspected: it studies a different operator and does not assert the spectrum or endpoint projection constant for indicator convolution. A previously published quartic-graph Gabor rank theorem concerns Weyl-projector measurements rather than additive convolution, **but its zero-translation ambiguity block already gives the eighteen vanishing Fourier frequencies for this same curve at characteristic seven**. That overlap is prior knowledge, not a newly claimed kernel count. Its stated limitations explicitly leave the full nonzero singular spectrum undetermined, and it does not discuss the endpoint projection norm. Searches found no covering statement for the sharp endpoint constant, but a hidden equivalent computation in finite-field idempotent literature remains possible.

## Limitations
The exact constant is for the 5488 nonlinearly rank-deficient **seven-point indicator masks** on \(\mathbb F_7^2\). Affine lines have rank seven and are excluded from the \(193/49\) assertion. This does not classify full singular-value or projection-norm spectra for every other mask, nor does it give an asymptotic formula in larger prime fields. The historical-priority assessment is bounded by accessible primary texts, available research records, and targeted equivalence searches. The included finite checks are corroboration of, not replacements for, the exact arguments.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, first public 2002-04-18, https://arxiv.org/abs/math/0204234.
2. L. Lovász and A. Schrijver, *Remarks on a theorem of Rédei*, Studia Sci. Math. Hung. 16 (1981), 449–454, full text https://ir.cwi.nl/pub/10047/10047D.pdf.
3. R. Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407, first public 2003-12-22, https://arxiv.org/abs/math/0312407.
4. G. Somlai, *A new proof of Rédei's theorem on the number of directions*, Archiv der Mathematik 122 (2024), 575–580, https://doi.org/10.1007/s00013-024-01979-x.
5. *Sharp unrestricted fourth-moment extension on the seven-point quartic graph*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-unrestricted-fourth-moment-extension-on-the-seven-point-qu--362930bb4f18.
6. *Exact rank and Weyl-kernel classification for quartic-graph Gabor tomography*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-rank-and-weyl-kernel-classification-for-quartic-graph-gabo--1f76e4a64221.
7. A. B. Evans, *On the number of orthomorphisms of the cyclic group of order nine*, Australas. J. Combin. 86 (2023), 206–221. Its introduction records Euler's \(19\) normalized orthomorphisms at order seven, hence \(133\) without normalization. https://ajc.maths.uq.edu.au/pdf/86/ajc_v86_p206.pdf.
