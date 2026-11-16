# Parity rigidity and volume-optimal placement for radial cyclic Gabor bases

## Finding

**Theorem (exact rank, spectrum, and sharp placement).** Let \(N=2m\) with integer \(m\ge2\). On \(\mathbb Z_N\), define the geodesic distance \(\ell(j)=\min\{j,N-j\}\) for \(0\le j<N\). Let \(g(j)=w_{\ell(j)}\), with strictly decreasing positive radial profile \(w_0>w_1>\cdots>w_m>0\). For any two distinct translates \(a,a+d\), use all \(m\) even modulations, and write \(d\) for the shorter cyclic distance of the two translates, so \(1\le d\le m\). The \(N\) *unnormalized* vectors

\[
 \mathcal G_d(g)=\{M_{2k}T_b g:\ 0\le k<m,\ b\in\{a,a+d\}\}
\]

have rank exactly \(N\) if \(d\) is odd, and exactly \(N-1\) if \(d\) is even. Precisely \(m^2\) of the \(m(2m-1)\) unordered two-translate designs are bases. When \(d\) is even, there is exactly one singular two-dimensional sampling fiber.

For any profile as above, let

\[
 B_{r,d}=\begin{pmatrix}g(r)&g(r-d)\\g(r+m)&g(r+m-d)\end{pmatrix},\quad
 \tau_{r,d}=\sum_{i,j=1}^2 |(B_{r,d})_{ij}|^2,\quad
 \Delta_{r,d}=\det B_{r,d}.
\]

All arguments of \(g\) are reduced modulo \(N\). The complete frame-operator spectrum, including any zeros, is the multiset

\[
 \left\{\frac m2\left[\tau_{r,d}\pm\sqrt{\tau_{r,d}^2-4\Delta_{r,d}^2}\right]:0\le r<m\right\}.
\]

**Sharp volume theorem.** Specialize to \(g_\rho(j)=\rho^{\ell(j)}\) with \(0<\rho<1\), and set \(t=-\log\rho>0\). For any odd \(1\le d\le m\), the modulus of the determinant of the \(N\)-by-\(N\) Gabor synthesis matrix is

\[
 V_d=m^m(2\rho^m)^m\,[\sinh(td)]^{m-d+1}
 \prod_{\substack{1\le j\le d-2\\j\ \mathrm{odd}}}\sinh(tj)^2.
\]

The empty product equals one. For even \(d\), \(V_d=0\). For consecutive allowed odd distances,

\[
 \frac{V_{d+2}}{V_d}=\left(\frac{\sinh((d+2)t)}{\sinh(dt)}\right)^{m-d-1}>1
 \quad\text{when }d+2\le m.
\]

Thus the **unique optimal shorter distance** maximizing the synthesis volume, equivalently the Gram determinant, is the largest odd integer at most \(m\): \(d_*=m\) when \(m\) is odd and \(d_*=m-1\) when \(m\) is even. There are \(m\) optimal unordered translation pairs if \(m\) is odd, and \(2m\) if \(m\) is even.

## Assumptions and scope

Take the standard Hermitian inner product on \(\mathbb C^N\), define \((T_b g)(j)=g(j-b)\), and \((M_{2k}g)(j)=e^{2\pi i(2k)j/N}g(j)\). The synthesis columns have **no** \(N^{-1/2}\), unit-energy, or Fourier normalization. The profile is real, strictly positive, symmetric about the origin on the cycle, and strictly decreasing with geodesic radius. Translation of both sites and reflection of their difference preserve all rank and volume statements. The rank and spectrum conclusions hold for every such radial profile; the exact volume product and D-optimal placement conclusion are only asserted for the specified geodesic exponential family. Integer \(m\ge2\), all allowed cyclic distances, and every real \(0<\rho<1\) are included.

## Proof

**1. Exact polyphase reduction.** Choose the unitary inverse discrete Fourier transform on the \(m\) modulation columns belonging to each translate. Because \(e^{2\pi i(2k)(r+m)/N}=e^{2\pi i k r/m}\), Fourier orthogonality sends the transformed column of modulation index \(r\) to a vector supported on the two coordinates \(r\) and \(r+m\), whose two entries are \(\sqrt m\,g(r-b)\) and \(\sqrt m\,g(r+m-b)\). Permute coordinate rows and transformed columns by residue modulo \(m\). The entire synthesis matrix is unitarily right-equivalent and permutation-equivalent to the direct sum \(\bigoplus_{r=0}^{m-1}\sqrt m\,B_{r,d}\), taking the first translation as zero. Consequently its rank is \(\sum_{r}\operatorname{rank} B_{r,d}\), its absolute determinant is \(m^m\prod_r|\Delta_{r,d}|\), and the frame operator has eigenvalues of the blocks \(mB_{r,d}B_{r,d}^*\). The quadratic formula for a Hermitian two-by-two block gives the stated complete spectrum.

**2. The sole possible zero fiber.** Define \(h(j)=g(j)/g(j+m)\), all indices cyclic. Positivity implies

\[
 \Delta_{r,d}=0\quad\Longleftrightarrow\quad h(r)=h(r-d).
\]

For \(0\le j\le m\), symmetry gives \(h(j)=w_j/w_{m-j}\). This ratio is *strictly decreasing*: if \(j<k\), its numerator strictly decreases and its denominator strictly increases. Moreover \(h(-j)=h(j)\), and these are the only equalities because every class modulo \(N\) has a unique representative radius \(\ell(j)\in\{0,\ldots,m\}\). Therefore \(h(r)=h(r-d)\) is equivalent to \(r\equiv -(r-d)\pmod N\), or \(2r\equiv d\pmod{2m}\). Since \(0\le r<m\), this congruence has one solution exactly when \(d\) is even, namely \(r=d/2\), and none when \(d\) is odd. Each two-by-two block has two strictly positive entries in each column and hence rank at least one; the single vanishing determinant therefore reduces the total rank by exactly one. This establishes rank and nullity for *all* strictly decreasing positive radial profiles.

**3. Exact design count.** For \(1\le d<m\), the number of unordered pairs at shorter distance \(d\) is \(N=2m\), whereas for \(d=m\) it is \(m\). If \(m\) is even there are \(m/2\) odd allowed distances, yielding \(m^2\) bases. If \(m\) is odd there are \((m-1)/2\) odd distances below \(m\), plus \(m\) antipodal pairs, again \(m^2\). The denominator of all designs is \(\binom{2m}{2}=m(2m-1)\).

**4. The geodesic exponential determinant.** Write \(g(j)=\rho^{\ell(j)}\), \(0<\rho<1\). For \(0\le r<d\), direct evaluation of the four cyclic distances in \(B_{r,d}\) gives

\[
 \Delta_{r,d}=\rho^{m+2r-d}-\rho^{m+d-2r}
 =2\rho^m\sinh(t(d-2r)).
\]

For \(d\le r<m\), the determinant is

\[
 \Delta_{r,d}=\rho^{m+d}-\rho^{m-d}
 =-2\rho^m\sinh(td).
\]

For odd \(d\), the absolute values of the integers \(d-2r\), \(0\le r<d\), comprise \(d\) once and every odd positive integer strictly smaller than \(d\) exactly twice. The constant block determinant occurs an additional \(m-d\) times. Multiplying the block determinants with the factor \(m^m\) gives exactly the stated product. For even \(d\), the interior index \(r=d/2\) makes the determinant vanish, matching Step 2.

**5. Sharp D-optimality.** Compare the explicit products for odd \(d\) and \(d+2\). The two new interior factors \(\sinh(td)^2\) cancel two of the previous \(\sinh(td)\) factors, yielding

\[
 V_{d+2}/V_d=\big[\sinh((d+2)t)/\sinh(dt)\big]^{m-d-1}.
\]

Here \(t>0\), the hyperbolic sine increases strictly, and \(m-d-1\ge1\) whenever \(d+2\le m\). Hence volumes strictly increase through all odd allowable shorter distances. Even distances have zero volume, so the largest odd distance is uniquely optimal. The count of maximizing pairs follows from the cyclic-distance enumeration in Step 3. This proves the claims without extrapolation from finite samples.

## Verification

The accompanying standalone `CHECK.py` uses exact rational arithmetic to compare block determinants, ranks, complete product volumes, and all consecutive-distance volume ratios for lengths \(N=2m\), \(2\le m\le12\), three rational decay values, and seven independently generated nongeometric strictly radial profiles per length. If NumPy is available, it also constructs the complete complex-valued synthesis matrix for each \(2\le m\le9\) and all nontrivial cyclic translation differences, checking full singular rank and the predicted frame spectrum. On the recorded environment it passed **1,143** individual tests. Invoke `python3 CHECK.py`. These finite tests do not substitute for the proof of the all-length result in the previous section.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez (arXiv:2605.16139, first posted May 15, 2026), Theorem 1.1 and Section 5, establish block equivalence of finite Gabor frame operators whenever one index set is a subgroup, which subsumes the *general decomposition method* in Step 1. This is acknowledged as prior work, not a new decomposition theorem. Their inspected full text does not identify the universal odd-distance rank law for geodesically radial windows, count exactly all surviving two-translate designs, or give the closed sharp volume formula and unique D-optimal distance. A related indexed result classifies **flat phase-only** two-translation cyclic Gabor orthonormal bases, distinguishing additive-order and alphabet divisibility, not strictly decreasing positive radial windows or determinant-optimal placement. A previously recorded one-sided geometric-window classification uses \(g(j)=\rho^j\), a different nonsymmetric window, and a different subgroup-translation geometry, so it does not imply the present radial theorem.

The 2013 discrete Zak-transform characterization by Li and Zhang establishes general frame and Riesz criteria rather than a distance-specific classification. Ulanovskii and Zlotnikov (2026) construct continuous parity-based Gabor nonframes with different phase-space domains. No claim is made to novelty of elementary two-by-two Fourier or hyperbolic-product algebra; the substantive claim is the all-order, window-shape-universal rank rigidity together with the exact optimal placement for a natural geodesic exponential model. Earlier polyphase-filter and finite time-frequency literature might contain an equivalent formulation and remains a priority risk.

## Limitations

The construction is critical (exactly \(N\) atoms), the ambient group has even cyclic order, the modulation channels are exactly all even residues, and the two translations are distinct. Strict radial positivity and decrease are essential hypotheses of the parity/rank theorem; arbitrary nonradial, nonmonotone, signed or complex-phase windows can behave differently. The D-optimal distance conclusion is proved only for \(g_\rho\), not for all monotone radial profiles, nor does determinant optimality imply the same optimizer for the *least frame bound* or condition number. Finite consistency checks are not an independent audit and no independent mathematical validation has occurred.

## References

1. O. Asipchuk, L. De Carli, L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139 (first publicly posted May 15, 2026; full text of v2 inspected, including Theorem 1.1 and Sections 3–5). https://arxiv.org/html/2605.16139v2
2. Y.-Z. Li, Y. Zhang, *Discrete Subspace Multiwindow Gabor Frames and Their Duals*, Abstract and Applied Analysis (2013), article 357242; DOI 10.1155/2013/357242 (Zak-matrix frame characterization, inspected Sections 2–5). https://onlinelibrary.wiley.com/doi/10.1155/2013/357242
3. A. Ulanovskii, I. Zlotnikov, *Periodic Non-uniqueness Sets for Shift-invariant Spaces and Parity-Based Obstructions to the Frame Property for Gabor Systems*, arXiv:2606.31450 (2026; abstract and available full-text sections compared). https://arxiv.org/abs/2606.31450
4. *A phase-alphabet trichotomy for critical two-translation cyclic Gabor bases*, published October 2026, complete result inspected for the same modulation and translation geometry but different window assumptions. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-phase-alphabet-trichotomy-for-critical-two-translation-cyclic--740628e0639c/RESULT.md
