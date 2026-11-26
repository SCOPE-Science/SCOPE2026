# Sharp cubic-coset triple universality over proper finite-field extensions

## Finding
Let \(q=p^e\) be a prime power with \(e\ge2\) and \(q\equiv1\pmod3\). Write \(C=(\mathbb F_q^\times)^3\), and choose either generator \(gC\) of the cyclic quotient \(\mathbb F_q^\times/C\) of order three. Color \(u\ne0\) by \(c(u)=j\in\{0,1,2\}\) when \(u\in g^jC\). Form the set of admissible length-three words
\[
W(q)=\{(c(x),c(x+1),c(x+2)):x,x+1,x+2\ne0\}.
\]
Then **all twenty-seven cubic-coset words are realized if and only if the characteristic is odd and \(q\ge121\)**:
\[
\boxed{W(q)=\{0,1,2\}^3\ \Longleftrightarrow\ p\ne2\text{ and }q\ge121.}
\]
The only proper odd-characteristic prime-power exceptions with \(q\equiv1\pmod3\) are \(25\) and \(49\). They realize respectively \(17\) and \(19\) of the twenty-seven words. In characteristic two the first and third positions are identical, so completeness is impossible, regardless of field size. The classification is sharp among eligible extension fields: \(\mathbb F_{49}\) is incomplete, while \(\mathbb F_{121}\) is complete.

## Assumptions and scope
A **proper extension** is \(\mathbb F_{p^e}\) with \(e\ge2\), not a prime field. The condition \(q\equiv1\pmod3\) is necessary for a nontrivial cubic-residue class quotient; there are no characteristic-three fields in that class. A *consecutive triple* uses the canonical prime-subfield elements \(0,1,2\) in the field's additive group, not three consecutive integer representatives in a chosen numerical encoding. Only nonzero triple members receive colors. Choosing \(gC\) rather than \(g^2C\) swaps the colors \(1\) and \(2\), without changing completeness or the number of missing words.

## Proof
**1. Even characteristic.** If \(p=2\), then \(2=0\) in \(\mathbb F_q\). Every admissible word is \((c(x),c(x+1),c(x))\). In particular the word \((0,0,1)\) cannot occur, so \(W(q)\ne\{0,1,2\}^3\).

**2. Uniform odd-characteristic estimate.** Suppose \(p\ge5\). Choose a cubic character \(\chi:\mathbb F_q\rightarrow\{0,1,\omega,\omega^2\}\), with \(\chi(0)=0\), \(\omega^3=1\ne\omega\), and \(\chi(g)=\omega\). For each \(j\in\{0,1,2\}\), define
\[
Q_j(u)=1+\omega^{-j}\chi(u)+\omega^{-2j}\chi(u)^2.
\]
At nonzero \(u\), \(Q_j(u)\) is \(3\) if \(c(u)=j\), and \(0\) otherwise. At \(u=0\), it is \(1\). For a chosen target word \(t=(t_0,t_1,t_2)\) let \(N_t(q)\) count its admissible starting points. Removing the three exceptional starts \(x\in\{0,-1,-2\}\) gives
\[
27N_t(q)=\sum_{x\in\mathbb F_q}\prod_{j=0}^{2}Q_{t_j}(x+j)-E_t,
\qquad 0\le E_t\le27.
\]
The upper bound on \(E_t\) holds because each exceptional product has one factor \(1\) and two factors in \(\{0,3\}\). Expand the main product into \(27\) character sums. Its constant term is \(q\). Six terms involving a single nonzero character exponent sum to zero by character orthogonality. Twelve terms have support at precisely two distinct shifts, and each has modulus at most \(\sqrt q\). Eight terms have support at all three shifts, and each has modulus at most \(2\sqrt q\). These are standard multiplicative-character Weil bounds: the corresponding polynomial \(\prod_{j:e_j\ne0}(X+j)^{e_j}\), with \(e_j\in\{1,2\}\), is not a cube and has two or three distinct roots in the algebraic closure. All character coefficients have complex absolute value one. Consequently, for **every** target word,
\[
27N_t(q)\ge q-(12+16)\sqrt q-27=q-28\sqrt q-27.
\]
For \(q\ge841\), put \(y=\sqrt q\ge29\). Then \(q-28\sqrt q-27=(y-29)(y+1)+2>0\). Every target word therefore occurs in every odd-characteristic eligible field with \(q\ge841\), including proper extensions.

**3. Exhaustive extension-field remainder.** Every odd-characteristic proper prime power below \(841\) and congruent to one modulo three appears exactly once in the list
\[
25,49,121,169,289,343,361,529,625.
\]
Indeed its prime base is at most \(\sqrt{840}\), and direct prime-power generation supplies exactly those nine possibilities. The standalone standard-library Python 3 file `verify.py` constructs each field as \(\mathbb F_p[T]/(F(T))\), verifies the supplied defining polynomial has no monic factor of degree at most half its degree, and hence is irreducible. It enumerates every field element, computing its cubic-coset color in **two ways**: by the cubic-character power \(u^{(q-1)/3}\) and by membership in the three explicit cosets of the independently enumerated cube subgroup. The two colorings are asserted equal. The verifier checks all \(q-3\) admissible starts and produces the following complete counts:

| \(q\) | Realized words | Missing words | Minimum positive multiplicity |
|---:|---:|---:|---:|
| 25 | 17 | 10 | 1 |
| 49 | 19 | 8 | 2 |
| 121 | 27 | 0 | 2 |
| 169 | 27 | 0 | 4 |
| 289 | 27 | 0 | 6 |
| 343 | 27 | 0 | 4 |
| 361 | 27 | 0 | 10 |
| 529 | 27 | 0 | 16 |
| 625 | 27 | 0 | 14 |

The exact results are retained in `certificate.json`, including a witness for every realized word, the canonical defining polynomials, and complete lists of missing words in the two exceptional fields. For each complete field, its twenty-seven witnesses supply direct finite certificates; for each incomplete field, the entire exhaustively computed histogram certifies nonexistence of the missing words. Thus among eligible proper odd-characteristic fields under the analytic cutoff only \(25\) and \(49\) fail. Together with steps 1 and 2 this proves the asserted equivalence.

## Verification
Execute `python3 verify.py` from this directory. The defining polynomials are embedded in the script and checked for irreducibility. The program uses built-in integer arithmetic, finite-field polynomial reduction and a separate cube-coset cross-check of the character colors. It regenerates the full list of eligible extension degrees and prime bases below \(841\), computes word frequencies, and checks the missing-word counts before printing `VERIFY_OK`. In total nine fields are checked and seven are complete. The JSON data are retained in `certificate.json`; `verify_output.txt` gives the final success line. This exhaustive finite certificate is used **only** for the nine fields below the analytic bound; the infinite range is proved by the displayed character-sum estimate.

## Relationship to prior work
Yuan and Zhang study cubic-character counts for special prime-field expressions such as \(a+a^{-1}\) and \(a-a^{-1}\). Bergman, Coulter and Fain investigate consecutive **quadratic** residue/nonresidue patterns related by a linear map in a finite field. Neither comparison supplies the three-color, three-position classification here. The prime-field Resultary record [5a92ab0389ae] gives the sharp prime-field threshold \(307\) using the same character estimate and cutoff \(841\). The estimate applies over proper extensions as well, but that record's finite census is for primes. The separate Resultary classification [25e842088320] concerns three consecutive cubes that are nonsquares, a refinement of just the all-cubic word. Its exception set includes \(121\), although the coarser cubic-coset language is complete there. The inspected passages of Jordan and of Buell and Hudson concern two-term same-class runs and prime-field power-residue runs, respectively.

## Limitations
The distinct content identified in this comparison is the **sharp classification for proper extensions**, especially the complete low-order census and characteristic dichotomy, not a new general Weil estimate or a claim to improve the separate prime-field threshold. This result determines presence/absence, not a simple closed expression for every word's exact frequency in arbitrary fields. The finite certificate uses explicit field arithmetic; it is not a formal proof assistant certificate. Older or unindexed cyclotomic tables might implicitly contain the extension-field census. In particular, the full text of Lehmer's *Patterns of Power Residues* was not available for comparison; the available description discusses the postponement of the first appearance of patterns over primes, which does not settle possible further overlap.

## References
1. X. Yuan and W. Zhang, *On cubic residues and related problems*, Indian Journal of Pure and Applied Mathematics **54** (2023), 806–815; first online 2022-08-02. https://doi.org/10.1007/s13226-022-00299-6.
2. E. Bergman, R. S. Coulter and B. Fain, *On consecutive residues and nonresidues under a linear map in a finite field*, Bulletin of the Australian Mathematical Society **111** (2025), 505–512; first online 2024-10-11. https://doi.org/10.1017/S0004972724000698.
3. D. A. Buell and R. H. Hudson, *Sequences in power residue classes*, International Journal of Mathematics and Mathematical Sciences **9** (1986), 261–266. https://doi.org/10.1155/S0161171286000315. See p. 261 for the prime-field run setting.
4. J. H. Jordan, *Pairs of Consecutive Power Residues or Non-Residues*, Canadian Journal of Mathematics **16** (1964), 310–314. https://doi.org/10.4153/CJM-1964-030-6. Full published mathematical introduction inspected.
5. The classical Weil bound for multiplicative characters of non-perfect-power polynomials with \(r\) distinct roots; the bound is \((r-1)\sqrt q\) for \(r\ge2\) over any finite field of the stated characteristic.
6. [5a92ab0389ae] Prime-field cubic-coset triple completeness, Resultary (2026-11-08). https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-sharp-universal-completeness-threshold-for-three-consecutive-cub--5a92ab0389ae/RESULT.md
7. [25e842088320] Exceptional-field classification for consecutive cubes that are nonsquares, Resultary (2026-11-02). https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-complete-exceptional-field-classification-for-three-consecutive--25e842088320/RESULT.md
8. E. Lehmer, *Patterns of power residues*, Journal of Number Theory (1983). https://doi.org/10.1016/0022-314X(83)90004-5. Available description only.
