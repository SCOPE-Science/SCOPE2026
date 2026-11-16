# Exact Bargmann-phase histograms and three-column spectra for prime quadratic-chirp bases

## Finding
For every odd prime \(p\), the complete set of canonical quadratic-chirp mutually unbiased bases in \(\mathbb C^p\) has an explicit, all-prime third-order Bargmann-invariant distribution. Restrict to ordered triples of vectors from three **pairwise distinct bases**. Each triple has normalized Bargmann phase
\[
\tau=p^{3/2}\langle u,v\rangle\langle v,w\rangle\langle w,u\rangle\in\mathbb T.
\]
With \(\zeta=e^{2\pi i/p}\), quadratic character \(\chi\) on \(\mathbb F_p^\times\), and \(\epsilon_p=1\) when \(p\equiv1\pmod4\) or \(i\) when \(p\equiv3\pmod4\), the **exact set of distinct phases** is
\[
\{\epsilon_p^3,-\epsilon_p^3\}\ \cup\ \{\epsilon_p^3\chi(s)\zeta^s:s\in\mathbb F_p^\times\}.
\]
Put \(C=p^3(p^2-1)\). Each of the first two phases occurs exactly \(C/2\) times and each nonzero-parameter phase occurs exactly \(C\) times, among all labeled ordered triples from distinct bases. Their total number is \(pC=p^4(p^2-1)\).

Let \(G=[\langle u_i,u_j\rangle]_{i,j=1}^3\) denote the Gram matrix of such a triple. Then \(\operatorname{spec}(G)\) is obtained by taking \(1+\lambda/\sqrt p\) over the three real roots of
\[
\lambda^3-3\lambda-2\operatorname{Re}(\tau)=0.
\]
Exactly \((p+3)/2\) distinct unordered Gram spectra occur when \(p\equiv1\pmod4\), and exactly \((p+1)/2\) when \(p\equiv3\pmod4\).

For completeness, among **all ordered triples of pairwise distinct vectors** from the \(p(p+1)\) vectors, the additional spectral types are \(\{1,1,1\}\) (all from one basis, count \((p+1)p(p-1)(p-2)\)) and \(\{1,1-\sqrt{2/p},1+\sqrt{2/p}\}\) (exactly two from one basis, count \(3(p+1)p^3(p-1)\)).

## Assumptions and scope
Here \(p\ge3\) is any odd prime. Set \(\zeta=\exp(2\pi i/p)\), \(e_t(j)=\mathbf1_{\{t\}}(j)\), and
\[
v_{a,b}(t)=p^{-1/2}\zeta^{at+bt^2},\qquad a,b,t\in\mathbb F_p.
\]
The \(p\) chirps at each fixed \(b\) form an orthonormal basis \(\mathcal B_b\); the \(p\) coordinate vectors form \(\mathcal B_\infty\). These \(p+1\) bases are mutually unbiased by quadratic Gauss-sum evaluation. We count **ordered triples of labeled vectors**; phase conventions for any individual vector cancel in \(\tau\). There is no claim for arbitrary (potentially inequivalent) complete mutually unbiased bases, for even characteristic, or for prime-power dimensions that are not prime.

## Proof
**1. Gauss-sum reduction.** For \(b\ne b'\), evaluation of the nonzero quadratic Gauss sum gives
\[
\langle v_{a,b},v_{a',b'}\rangle=\frac{\epsilon_p\chi(b'-b)}{\sqrt p}\zeta^{-(a'-a)^2/[4(b'-b)]}.
\]
The brackets indicate the inverse in \(\mathbb F_p\). For three finite distinct basis labels \((b_0,b_1,b_2)\), put
\[
B=(b_1-b_0)(b_2-b_1)(b_0-b_2),\qquad
D=(b_2-b_0)(a_1-a_0)-(b_1-b_0)(a_2-a_0).
\]
Expanding three completed squares, with \(B\ne0\), yields the **exact** phase identity
\[
\tau=\epsilon_p^3\chi(B)\zeta^{D^2/(4B)}.
\]
If one basis is computational, cyclically rotate the ordered triple to \((e_t,v_{a_1,b_1},v_{a_2,b_2})\). With \(d=b_2-b_1\ne0\) and \(h=a_2-a_1\), direct multiplication gives
\[
\tau=\epsilon_p\chi(d)\zeta^{-d(t+h/(2d))^2}
=\epsilon_p^3\chi(-d)\zeta^s,\qquad s=-d(t+h/(2d))^2.
\]
These expressions use \(\epsilon_p^2=\chi(-1)\), an identity of the quadratic Gauss sum. For either type, when the exponent \(s\ne0\), its Legendre symbol equals the sign multiplying \(\epsilon_p^3\). When \(s=0\), the sign may be either \(+1\) or \(-1\). This proves the asserted list; its \(p+1\) values are distinct since \(-1\) is not a \(p\)-th root of unity for odd \(p\), and distinct powers of \(\zeta\) are distinct.

**2. Exact multiplicities.** There are \(M=(p+1)p(p-1)=p(p^2-1)\) ordered triples of distinct basis labels. For each such triple, \(D\) or \(t+h/(2d)\) is a nonzero linear form in the three vector labels. Each of its \(p\) values occurs exactly \(p^2\) times. Therefore the phase of exponent zero occurs \(p^2\) times for each basis triple. For each nonzero \(s\) with the correct quadratic-character sign, its quadratic equation has two roots and contributes \(2p^2\) labeled triples. Multiplication of every finite basis label \(b\) by a fixed quadratic nonresidue (keeping the computational basis fixed) is a bijection of the ordered distinct-base triples. It flips \(\chi(B)\) in the all-finite case and \(\chi(-d)\) in the computational case. Thus precisely \(M/2\) ordered basis triples have either sign. The two exponent-zero phases occur \(Mp^2/2=C/2\) times each; each nonzero \(s\) occurs \((M/2)2p^2=C\) times. The total is \(pC=Mp^3\), as required.

**3. Gram spectral classification.** The off-diagonal entries of \(G-I\) all have modulus \(p^{-1/2}\). Put \(H=\sqrt p(G-I)\). Its diagonal is zero; the three off-diagonal cycles have product \(\tau\) and \(\overline\tau\). Thus \(\operatorname{tr}H=0\), \(\operatorname{tr}H^2=6\), and \(\det H=2\operatorname{Re}\tau\), which proves the cubic. If \(p\equiv1\pmod4\), the values \(\pm\epsilon_p^3\) give distinct real parts \(\pm1\), while the \(p-1\) other phases have real parts paired exactly by \(s\leftrightarrow -s\), producing \(2+(p-1)/2\) types. If \(p\equiv3\pmod4\), the first two phases both have real part zero and the other phases again pair by \(s\leftrightarrow-s\), giving \(1+(p-1)/2\) types. No additional coincidences occur, by the elementary cosine and sine identities and the fact that \(p\) is odd.

**4. Other three-vector configurations.** Three distinct vectors from one orthonormal basis have Gram matrix \(I_3\). For two vectors of one basis and one from a different basis, orthogonality kills one off-diagonal pair; the other two have modulus \(p^{-1/2}\), giving eigenvalues \(1,1\pm\sqrt{2/p}\). The counts follow by choosing bases and ordered column positions. The three regimes exhaust the ordered triples of distinct vectors.

## Verification
The standalone `check_mub_phase.py` enumerates every ordered distinct-base triple of labels for \(p=3,5,7,11\), comparing the complete exact phase histogram with its formula. It also evaluates the defining complex inner products independently in 3,600 sampled labeled cases. The tested nonzero-triple totals are 648, 15,000, 115,248 and 1,756,920, respectively. Numerical inner-product residuals are less than \(2\times10^{-15}\). The all-prime theorem is proved by the identities and counting argument above; the tests do not assert infinite verification. Reproduce with `python3 check_mub_phase.py`.

For comparison with the full third-order tensor, if phases of zero triple products are assigned angle zero, there are \(N^3-pC\) triples outside the three-distinct-bases stratum, where \(N=p(p+1)\). When \(p\equiv1\pmod4\), the \(\tau=1\) stratum adds another \(C/2\) phase-zero triples; otherwise it does not. This reproduces the published phase-zero counts 1,080 at \(p=3\) and 13,500 at \(p=5\).

## Relationship to prior work
Quadratic Gauss-sum constructions of prime-dimensional mutually unbiased bases are classical (Klappenecker–Rötteler); harmonic frame structure and character sums are surveyed in Fickus–Iverson–Jasper–Mixon (arXiv:2112.14267, first posted 28 December 2021). Gültekin–Samuel–Gedik (arXiv:2604.04164, 2026, §4 and Table 2) explicitly give **numerical** third-order phase histograms for dimensions 3, 4 and 5, including the dimension-3 and dimension-5 histograms recovered here. Those small cases and the Gauss-sum construction are prior results. The claim here is the symbolic all-odd-prime phase and multiplicity law, together with the complete associated three-column Gram spectral-type classification. The available primary treatments did not exhibit this full parameter-uniform formula; equivalence under finite-geometric triple-product terminology is a residual historical-priority risk.

## Limitations
The theorem addresses one specified complete family of prime-dimensional MUBs and does not imply classification of all MUB structures or larger Gram submatrices. The spectral types are unordered eigenvalue multisets, not similarity classes of the full Gram matrices. The source-date anchor is the first public version of the 2021 harmonic frame paper, not a claim that the all-prime histogram appeared there. Direct comparison with all obscure MUB geometry papers is not exhaustive. No independent mathematical audit has been performed.

## References
- M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Harmonic Grassmannian codes*, arXiv:2112.14267 (first public 2021-12-28), https://arxiv.org/html/2112.14267v1 .
- A. Klappenecker and M. Rötteler, *Constructions of Mutually Unbiased Bases*, arXiv:quant-ph/0309120 (2003), https://arxiv.org/abs/quant-ph/0309120 .
- B. Gültekin, S. B. Samuel, Z. Gedik, *Generalized Numerical Construction of MUBs: A Group Theoretical Investigation*, arXiv:2604.04164 (first public 2026-04-05), §4.1 and Table 2, https://arxiv.org/html/2604.04164v2 .
- H. Zhu, *Mutually unbiased bases as minimal Clifford covariant 2-designs*, arXiv:1505.01123 (2015), https://arxiv.org/abs/1505.01123 .
