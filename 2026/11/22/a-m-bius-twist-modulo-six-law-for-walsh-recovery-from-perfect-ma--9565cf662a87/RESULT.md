# A Möbius-twist modulo-six law for Walsh recovery from perfect matchings

## Finding

For every integer \(n\ge3\), consider the graph \(M_n\) on \(2n\) vertices consisting of a single circumference cycle of length \(2n\) and \(n\) antipodal chords. Let \(\mathcal P_n\subset\mathbb F_2^{3n}\) be the incidence vectors of all its perfect matchings. For \(\omega\in\mathbb F_2^{3n}\), set the *unnormalized* Walsh multiplier
\[
W_n(\omega)=\sum_{P\in\mathcal P_n}(-1)^{\langle\omega,\mathbf1_P\rangle}.
\]
The minimum is taken only over nonzero multipliers. The following statements hold at **every** integer \(n\ge3\):

1. \(W_n(\omega)\ne0\) for **every** \(\omega\) if and only if \(6\nmid n\).
2. \(\min_{\omega:W_n(\omega)\ne0}|W_n(\omega)|=1\) if \(3\nmid n\), and equals \(2\) if \(3\mid n\).
3. For \(n=6k\), at least \(2^{2n-1}8^k\) of the \(2^{3n}\) Fourier characters vanish.

Therefore unnormalized convolution by \(\mathbf1_{\mathcal P_n}\) on the Boolean edge group is invertible exactly when \(6\nmid n\). Its \(\ell^2\) inverse norm is \(1\) for \(3\nmid n\), \(1/2\) for \(n\equiv3\pmod6\), and the Moore–Penrose inverse norm at \(6\mid n\) is \(1/2\).

The stronger comparison with the *untwisted* cycle prism is notable: its perfect-matching convolution has zeros already at all multiples of three, including odd ones [4], whereas a Möbius twist removes every zero when \(n\equiv3\pmod6\).

## Assumptions and scope

The vertices are \(\mathbb Z/(2n)\mathbb Z\). There are distinct cycle edges \(\{i,i+1\}\) for \(0\le i<2n\) and chords \(\{i,i+n\}\) for \(0\le i<n\). All calculations use the unnormalized counting sum and ordinary signs \(\pm1\) assigned independently to edges. The Boolean pairing is the standard dot product modulo two. Every perfect matching uses \(n\) edges.

For a sign pattern \(\sigma_e\in\{+1,-1\}\), the corresponding Walsh multiplier is \(\sum_P\prod_{e\in P}\sigma_e\). A vertex gauge change replaces signs on every edge incident to the chosen vertex by their negatives; it multiplies the contribution of *every* perfect matching by the same factor \(-1\). Its effects preserve all zeros and absolute values.

Gauge-normalize all cycle-edge signs to \(+1\) except the seam edge \(\{2n-1,0\}\), whose sign is \(h\in\{-1,+1\}\). Denote the independently normalized chord signs by \(r_0,\ldots,r_{n-1}\in\{-1,+1\}\). Each reduced sign configuration has exactly \(2^{2n-1}\) full frequency representatives, since a connected graph's vertex-gauge group has size \(2^{2n-1}\).

Define
\[
T(r)=\begin{pmatrix}r&1\\1&0\end{pmatrix},\qquad
P_n(r)=\prod_{j=0}^{n-1}T(r_j)=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
\]

## Proof

**1. Signed matching transfer formula.** Every perfect matching using at least one chord has its remaining vertices covered by two opposite, simultaneously chosen cycle edges. Choosing a chord at position \(i\) is a monomer of weight \(r_i\); choosing two parallel circumference edges between positions \(i\) and \(i+1\) is a dimer of weight \(1\), except at the seam where it has weight \(h\). The standard two-state matching recursion for a cyclic chain is given by the matrices \(T(r_i)\). Its non-wrapping tilings contribute \(a\), and its seam-wrapping tilings contribute \(hd\). When \(n\) is odd, the underlying circumference has two additional perfect matchings using no chords, with weights \(1\) and \(h\). When \(n\) is even, these two circumference matchings have already been represented as cyclic-chain dimer tilings, so there is no additional term. Consequently **every** original multiplier has absolute value equal to that of
\[
F_n(r,h)=a+hd+(1+h)\mathbf1_{\{n\text{ odd}\}}.
\tag{1}
\]
An overall sign from gauge normalization has no effect on zeros or magnitudes. Note that \(\det P_n=(-1)^n\) exactly, for every sign choice.

**2. Parity dichotomy.** Reducing each \(T(r_i)\) modulo two gives the single matrix \(T(1)\), whose order in \(\mathrm{GL}_2(\mathbb F_2)\) is three. If \(3\nmid n\), the trace \(a+d\) is odd, while the last term in (1) is even. Thus *every* multiplier is odd, hence nonzero and of absolute value at least one. If \(3\mid n\), then \(P_n\equiv I\pmod2\); in particular, \(a,d\) are odd, \(b,c\) even, and every multiplier is even.

**3. Determinant obstruction for all orders not divisible by six.** Suppose \(3\mid n\). If \(n\) is odd, then \(\det P_n=-1\). A zero with \(h=-1\) would force \(a=d\), so \(\det P_n=a^2-bc\equiv1\pmod4\), contradicting \(-1\equiv3\pmod4\). A zero with \(h=+1\) would force \(a+d+2=0\). Since \(a,d\) are odd, write \(a=-1+2u\), \(d=-1-2u\), giving \(ad=1-4u^2\equiv1\pmod4\). As \(bc\equiv0\pmod4\), this again contradicts determinant \(-1\). Thus every \(n\equiv3\pmod6\) is entirely zero-free, even though all its coefficients are even.

If \(6\mid n\), then \(\det P_n=+1\). A zero with \(h=+1\) would have \(a+d=0\), hence \(\det P_n=-a^2-bc\equiv3\pmod4\), another contradiction. Therefore any zero in a multiple-of-six order must have \(h=-1\). This is achieved, below.

**4. Six-step identity and exact gap witnesses.** Write \(\texttt{+}\) for chord sign \(+1\), and \(\texttt{-}\) for chord sign \(-1\). Direct multiplication gives
\[
T(+)T(+)T(-)T(+)T(+)T(-)=I.
\tag{2}
\]
The following initial sign words, specified with the seam sign, have the signed multipliers shown (each can be independently checked by (1)):

| \(n\) | chord-sign word | seam \(h\) | \(F_n\) |
|---:|:---:|---:|---:|
| 3 | `+++` | \(-1\) | 2 |
| 4 | `+++-` | \(+1\) | 1 |
| 5 | `++-+-` | \(+1\) | 1 |
| 6 | `+++++-` | \(+1\) | 2 |
| 7 | `++++--+` | \(-1\) | 1 |
| 8 | `+++++--+` | \(-1\) | 1 |

Appending any number of copies of the six-letter identity word in (2) preserves the entire transfer product, the parity of \(n\), and the same seam sign. These six seeds cover all six residue classes modulo six and realize the smallest parity-permitted nonzero magnitude for every \(n\ge3\). This proves the exact minimum \(1\) when \(3\nmid n\) and \(2\) when \(3\mid n\).

**5. Singularity and a quantitative null family.** At \(n=6\), choosing the identity word `++-++-` and \(h=-1\) gives \(a=d=1\) and \(F_6=0\). Repetition shows every \(n=6k\) has a zero. More strongly, direct two-by-two multiplication finds **eight** distinct length-six words with transfer product \(I\) or \(-I\):

`++-++-`, `+-++-+`, `+-+-+-`, `+--+--`, `-++-++`, `-+-+-+`, `-+--+-`, `--+--+`.

An arbitrary concatenation of \(k\) of these blocks has \(P_n=\pm I\), hence \(a=d\); \(h=-1\) gives zero. The \(8^k\) normalized chord words are distinct and have the same seam sign. Each accounts for exactly \(2^{2n-1}\) original Walsh frequencies under vertex gauges. Thus at least \(2^{2n-1}8^k\) distinct coefficients vanish. The determinant obstruction and existence of these witnesses establish singularity **if and only if** \(6\mid n\).

**6. Operator norm.** Walsh characters are an orthogonal basis for counting-measure \(\ell^2\) on \(\mathbb F_2^{3n}\); unnormalized convolution is diagonal on them with real eigenvalues \(W_n(\omega)\). The exact minimum nonzero multiplier magnitude above gives the stated inverse or Moore–Penrose inverse norm by the spectral theorem. No \(\ell^1\) or \(\ell^\infty\) inverse norm is asserted.

## Verification

The standalone, standard-library-only program `mobius_walsh_verifier.py` independently enumerates perfect matchings on the \(2n\) vertices and performs the exact integer Walsh–Hadamard transform of their seam/chord sign projection for every \(3\le n\le12\). It compares each of the \(2^{n+1}\) reduced Walsh coefficients with formula (1), verifies the sign counts, and checks invertibility, precise spectral gaps, and reduced zero counts \(36\) at \(n=6\) and \(1392\) at \(n=12\). It also verifies all eight identity blocks and the sharpness witnesses after six-step extensions through \(n=206\). It prints `MOBIUS_WALSH_EXACT_TESTS_PASS` when all 16,664 exact assertions pass.

These finite computations corroborate, but do not replace, the all-order determinant, recurrence, and witness proofs.

## Relationship to prior work

McSorley's 1998 Möbius-ladder paper [1] establishes a broad framework for counting structures on the same graphs; it supplies the archival geometric setting, not a verified signed all-character convolution classification in the accessible abstract. Lekshmi and West [2] prove the **unsigned** matching count \(L_n+2\mathbf1_{\{n\text{ odd}\}}\), recovered from (1) by setting all signs positive, but their accessed abstract does not establish the full signed spectrum. Cimasoni and Pham [3] present general twisted dimer partition function identities on nonorientable surfaces; these do not, in the inspected full text, supply the residue-wise Fourier invertibility and exact smallest multiplier for the present graph family. The directly comparable published cycle-prism result [4] treats an *untwisted* graph: its zero criterion \(3\mid n\) and even-order spectral gap \(4\) differ from the Möbius-ladder criterion \(6\mid n\) and sharp gap \(2\). The twist is not a relabeling or consequence of the prism theorem.

## Limitations

The null-family bound is a constructive **lower** bound, not an exact nullity formula for all \(n\). The theorem concerns the **unnormalized** all-edge signed matching enumerator, not the probability-normalized transform, nor arbitrary graphs or weighted real parameters. No exact endpoint \(\ell^1\)/\(\ell^\infty\) projection or inversion norms are asserted. McSorley's 1998 full text was unavailable from attempted arXiv/OA/publisher-access routes, and the 2020 enumerative paper was available only in abstract through the inspected path; an unindexed equivalent in their full texts or older statistical-mechanical literature remains a priority risk. Independent mathematical audit has not been performed.

## References

1. J. P. McSorley, *Counting structures in the Möbius ladder*, Discrete Mathematics 184 (1998), 137–164; publicly dated 1998-04-06 in the institutional record. https://digitalcommons.mtu.edu/michigantech-p/7264/ ; DOI https://doi.org/10.1016/S0012-365X(97)00086-1
2. R. S. Lekshmi and D. B. West, *The Number of Perfect Matchings in Möbius Ladders and Prisms*, arXiv:2003.09602 (first submitted 2020-03-21). https://arxiv.org/abs/2003.09602
3. D. Cimasoni and A. M. Pham, *Identities between dimer partition functions on different surfaces*, arXiv:1608.00741 (first submitted 2016-08-02). https://arxiv.org/abs/1608.00741
4. *A modulo-six Walsh stability law for perfect matchings of cycle prisms*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-a-modulo-six-walsh-stability-law-for-perfect-matchings-of-cycle--ed342431e104
