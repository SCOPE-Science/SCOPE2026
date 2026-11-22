# Antipodal rigidity and exact phase classification for six-tap two-channel cyclic Gabor tight frames

## Finding

Let \(N\ge12\) be an integer. Take a window \(g\in\mathbb C^N\) whose only nonzero entries are six consecutive taps \(g_0,\ldots,g_5\), each of absolute value one. For \(1\le k<N\), form the \(2N\)-vector cyclic Gabor family
\[
\mathcal G(g,k)=\{T_tg,\ M_kT_tg:t\in\mathbb Z_N\}.
\]
It is a tight frame **if and only if** \(N\) is even, \(k=N/2\), and its ordered six-tap window is
\[
\boxed{(g_0,g_1,g_2,g_3,g_4,g_5)
=(a,b,ax,\varepsilon i bx,-ax^2,bx^2),\quad
 a,b,x\in\mathbb T,\quad\varepsilon\in\{-1,1\}.}
\]
Every such frame has frame bound exactly \(12\). The full complex-phase solution space is the disjoint union of two three-dimensional tori, parametrized without redundancy by \((a,b,x)\) in the two sign families. In particular, the apparent possibility of a modulation character of order ten never gives a tight frame with six unimodular consecutive taps.

If, in addition, every tap must belong to the \(q\)-th roots of unity \(\mu_q\), for an integer \(q\ge2\), such a tight frame exists **if and only if** \(N\) is even and \(4\mid q\). For the only possible modulation separation \(k=N/2\), there are exactly
\[
\boxed{2q^3}
\]
ordered, indexed six-tap windows, without quotienting by phase or any time-frequency symmetries. The quaternary count \(128\) is already known from the length-three complex Golay-pair census; the new statement is the all-order Gabor modulation rigidity and continuous/all-alphabet classification together, not the rediscovery of that count.

## Assumptions and scope

Write \(\zeta=\exp(2\pi i/N)\), and use the counting inner product on \(\mathbb C^N\). Translations and modulations are defined by
\[
(T_tg)[j]=g[j-t],\qquad (M_kg)[j]=\zeta^{kj}g[j],
\]
with every index taken modulo \(N\). The window is supported **exactly** at \(\{0,1,2,3,4,5\}\); no zeros or variable magnitudes are allowed on these six sites. The two modulation channels are \(0\) and \(k\), the entire translation group is sampled, and the \(2N\) atoms are retained with their indices. Each atom has squared norm \(6\). Tightness means that their frame operator is a positive scalar multiple of the identity; the scalar is fixed to \(12\) by trace. The restriction \(N\ge12\) guarantees that autocorrelation lags \(\pm1,\ldots,\pm5\) are distinct modulo \(N\).

The unit circle is \(\mathbb T=\{z\in\mathbb C:|z|=1\}\) and \(\mu_q=\{\exp(2\pi i r/q):0\le r<q\}\). A pair of complementary length-three sequences is understood in the standard aperiodic autocorrelation sense, not as a previously unknown family.

## Proof

**Step 1: a diagonal Fourier criterion.** Put \(P(z)=\sum_{j=0}^5g_jz^j\) and \(\chi=\zeta^k\). Summing rank-one operators over all translations and using Fourier orthogonality diagonalizes the Gabor frame operator in the Fourier basis, with eigenvalues
\[
\lambda_\xi=|P(\zeta^{-\xi})|^2+|P(\chi\zeta^{-\xi})|^2,
\qquad 0\le\xi<N.
\]
The trace is \(12N\), so tightness is equivalent to \(\lambda_\xi=12\) for every \(\xi\). For \(1\le s\le5\), define the positive-lag aperiodic autocorrelation
\[
r_s=\sum_{j=0}^{5-s}g_{j+s}\overline{g_j}.
\]
Expanding the squared moduli and using \(N\ge12\), the Fourier characters at lags \(0,\pm1,\ldots,\pm5\) are distinct. Consequently the exact necessary and sufficient equations are
\[
\boxed{(1+\chi^s)r_s=0\quad(1\le s\le5).}\tag{1}
\]
Here \(r_5=g_5\overline{g_0}\ne0\), so \(\chi^5=-1\). The order of \(\chi\) is therefore either \(2\) or \(10\).

**Step 2: exclusion of order ten.** If \(\chi\) has order ten, then \(1+\chi^s\ne0\) for \(1\le s\le4\); in particular \(r_1=r_3=r_4=0\). Multiplying all taps by a common unit scalar, assume \(g_0=1\), and abbreviate the other taps as \((A,B,C,D,E)\). Because all taps are unimodular, \(r_4=D+E\overline A=0\) gives \(E=-DA\). Then \(r_1=0\) simplifies to
\[
u+v+w=0,\qquad u=B/A,\quad v=C/B,\quad w=D/C,
\]
where all three quotients have modulus one. Thus \((u,v,w)\) is an equilateral triple, so \(v/u\) is a primitive cube root of unity, \(|v-u|=\sqrt3\), and \(uvw=u^3\). Hence \(D=Au^3\), \(C=Auv\). Direct substitution into the remaining condition \(r_3=0\) yields
\[
0=C+D\overline A+E\overline B
=A u(v-u)+u^3.
\]
Its two terms have moduli \(\sqrt3\) and \(1\), an impossibility. Therefore the order-ten alternative never occurs. Necessarily \(\chi=-1\), equivalently \(N\) even and \(k=N/2\).

**Step 3: the complete antipodal solution.** When \(\chi=-1\), equation (1) annihilates every odd-lag condition and leaves exactly \(r_2=r_4=0\). Write the taps in two interlaced unit-magnitude triples:
\[
(g_0,g_2,g_4)=(a,au,ay),\qquad
(g_1,g_3,g_5)=(b,bv,bw),
\]
where \(a,b,u,v,y,w\in\mathbb T\). The lag-four equation is \(y+w=0\), while lag two is \(u+v+y/u+w/v=0\). Thus \(w=-y\) and
\[
u+v+y/u-y/v=0.\tag{2}
\]
Set \(h=v/u\) and \(t=y/u^2\). Dividing (2) by \(u\) gives \(1+h+t(1-h^{-1})=0\). The case \(h=1\) would give \(2=0\); otherwise
\[
t=\frac{h(1+h)}{1-h}.
\]
Since \(|t|=|h|=1\), it follows that \(|1+h|=|1-h|\), or \(\operatorname{Re}h=0\). Thus \(h=\varepsilon i\) for \(\varepsilon\in\{-1,1\}\), and substituting forces \(t=-1\). Consequently \(y=-u^2\), \(v=\varepsilon i u\), and \(w=u^2\). Renaming \(u=x\) produces exactly the displayed six-tap parametrization. Conversely, direct substitution gives \(r_2=r_4=0\), and (1) proves that every parameter choice is tight. The parameters \(a,b,x\) and sign \(\varepsilon\) are recovered uniquely from the tap vector, so the two-torus-component classification is exact.

**Step 4: finite phase alphabets and exact count.** For a \(q\)-phase window, \(a=g_0\), \(b=g_1\), and \(x=g_2/g_0\) necessarily lie in \(\mu_q\). The relation \(g_3/(bx)=\varepsilon i\in\mu_q\) forces \(4\mid q\). Conversely, when \(4\mid q\), arbitrary \(a,b,x\in\mu_q\) and either choice of \(\varepsilon\) give valid \(\mu_q\)-valued taps, since \(\mu_q\) is multiplicatively closed. Uniqueness of parameters yields exactly \(2q^3\) indexed windows. No phase-count extrapolation from a few numerical examples enters the proof.

## Verification

The standalone `CHECK_EXACT.py` enumerates all \(4^6=4096\) quaternary six-tap windows with exact Gaussian-integer autocorrelations, finding exactly \(128\) antipodal solutions and none satisfying the four order-ten vanishing conditions. It also excludes all \(2^6\) binary windows. Its deterministic output is embedded as `CHECK_EXACT_OUT.txt`.

An independently written `CHECK.py` enumerates normalized windows of phase-alphabet sizes \(2,4,6,8\), checks all modulation gaps at cyclic orders \(12\) and \(20\), and reconstructs the full frame operator directly for explicit examples at orders \(12,14,20\). Counts are respectively \(0,128,0,1024\) for the four phase-alphabet sizes (the \(128\) count also repeats at order \(20\)). The direct Gram matrices differ from \(12I\) by at most \(8\cdot10^{-14}\) in the tested cases. The outputs are embedded as `CHECK_OUT.txt`; those numerical tests are illustrative rather than proofs of all-order assertions.

## Relationship to prior work

The classical finite-Gabor diagonalization and ambiguity-function tightness tests are not claimed as new: see Krahmer–Pfander–Rashkov (2006) and Magsino (2016). Golay complementarity is also classical. Craigen–Holzmann–Kharaghani (2002) already classify the quaternary length-three Golay pairs up to equivalence and count exactly \(128\) indexed pairs; Parker–Paterson–Tellambura (2003) identify the length-three primitive quadriphase pair; Bright–Kotsireas–Heinle–Ganesh (2018) independently tabulate its \(128\) pairs. These establish the known antipodal quaternary slice and are explicitly credited.

The new assertion joins those ingredients to a **complete all-order six-site Gabor frame classification**, excludes the otherwise admissible order-ten modulation gap without assuming a finite alphabet, parametrizes *all continuous unimodular* solutions, and gives the sharp condition and exact count for *every* phase alphabet. A publicly indexed three-tap full-translation/two-modulation design result treats a different six-parameter correlation problem, and an indexed three-translation/half-modulation result treats a different sampling lattice; neither covers the exact claim here. A previously unindexed derivation of the same all-order statement remains possible.

## Limitations

This theorem requires six **consecutive** nonzero taps of **exactly equal magnitude** and \(N\ge12\); it does not classify variable-magnitude windows, cyclic lengths \(6\) through \(11\), fewer or more taps, more than two modulation channels, or arbitrary translation masks. The \(128\)-pair quadriphase Golay enumeration is prior knowledge and not a new discovery.

## References

1. R. Craigen, W. Holzmann, and H. Kharaghani, *Complex Golay sequences: structure and applications*, Discrete Mathematics **252** (2002), 73–89. https://doi.org/10.1016/S0012-365X(01)00162-5
2. M. G. Parker, K. G. Paterson, and C. Tellambura, *Golay Complementary Sequences*, Wiley Encyclopedia of Telecommunications, first published 15 April 2003. https://doi.org/10.1002/0471219282.eot367
3. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time–frequency representations on finite Abelian groups and applications*, 2006. https://arxiv.org/abs/math/0611493
4. M. Magsino, *Constructing Tight Gabor Frames Using CAZAC Sequences*, arXiv:1611.00818v1, first public 2 November 2016. https://arxiv.org/abs/1611.00818
5. C. Bright, I. Kotsireas, A. Heinle, and V. Ganesh, *Enumeration of Complex Golay Pairs via Programmatic SAT*, 2018. https://arxiv.org/abs/1805.05488
6. *Exact phase–frequency design and tightness transition for three-tap cyclic Gabor frames*, public finite-Gabor study. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-phase-frequency-design-and-tightness-transition-for-three--9d47ac973e0f
7. *Arithmetic existence and exact phase-alphabet counts for three-translate cyclic Gabor tight frames*, public finite-Gabor study. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-arithmetic-existence-and-exact-phase-alphabet-counts-for-three-t--9778d67573d4
