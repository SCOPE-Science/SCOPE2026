# The sharp mixed quadratic-character threshold in a Pythagorean parametrization

## Finding

Let \(p\) be any odd prime, let \(\chi_p\) be the Legendre symbol, and set
\[
F(t)=t^2-1,\qquad H(t)=2t,\qquad G(t)=t^2+1
\]
for \(t\in\mathbb F_p\). A *mixed sign word* is a triple \(\varepsilon=(\varepsilon_1,\varepsilon_2,\varepsilon_3)\in\{-1,1\}^3\) whose entries are not all equal. Say the word occurs if there is a \(t\in\mathbb F_p\) for which \(F(t)H(t)G(t)\ne0\) and
\[
\bigl(\chi_p(F(t)),\chi_p(H(t)),\chi_p(G(t))\bigr)=\varepsilon.
\]

**Theorem.** Every one of the six mixed sign words occurs if and only if
\[
p\notin\{3,5,7,13,17,29\}.
\]
In particular, all six words occur for **every prime \(p\ge31\)**; this universal threshold is sharp because \(p=29\) omits \((-1,-1,1)\) and \((1,1,-1)\). In contrast, the case of all-positive and all-negative words is deliberately not included in the theorem.

## Assumptions and scope

The assertion concerns residue classes \(t\) modulo an odd prime, not a positive-integer height restriction on the three entries. The parameter produces the identity \(F(t)^2+H(t)^2=G(t)^2\) over \(\mathbb F_p\). Nonzero entries are mandatory because the Legendre symbol has value zero at zero. All sign words use the fixed order \((F,H,G)\); interchanging the two legs just interchanges the first two signs.

## Proof

For a sign word \(\varepsilon=(a,b,c)\), let \(N_p(a,b,c)\) be its number of admissible parameters. Put \(\chi=\chi_p\), and for every \(t\in\mathbb F_p\) define
\[
I_{a,b,c}(t)=(1+a\chi(F(t)))(1+b\chi(H(t)))(1+c\chi(G(t))).
\]
On an admissible parameter, \(I_{a,b,c}(t)\) is \(8\) precisely when the prescribed word occurs and is zero otherwise. At an inadmissible parameter at least one factor equals one, so \(0\le I_{a,b,c}(t)\le4\). There are at most five inadmissible parameters: \(0,1,-1\) and the at most two roots of \(t^2+1\). Consequently,
\[
8N_p(a,b,c)\ge\sum_{t\in\mathbb F_p}I_{a,b,c}(t)-20.
\]

We now bound the full character expansion uniformly in \((a,b,c)\). The single sums satisfy
\[
\sum_t\chi(F(t))=\sum_t\chi(G(t))=-1,\qquad\sum_t\chi(H(t))=0.
\]
These are the elementary nonzero-constant quadratic-character identities. The products \(F(t)H(t)=2t(t^2-1)\) and \(H(t)G(t)=2t(t^2+1)\) are squarefree cubics in every odd characteristic. The Hasse bound for their smooth genus-one hyperelliptic models yields, for each of them, absolute character sum at most \(2\sqrt p\).

The fourth-degree product \(F(t)G(t)=t^4-1\) is also squarefree. The projective smooth curve \(y^2=t^4-1\) has **two rational points at infinity** because its leading coefficient is a square, so Hasse's bound gives
\[
\left|1+\sum_{t\in\mathbb F_p}\chi(t^4-1)\right|\le2\sqrt p.
\]
Finally, \(F(t)H(t)G(t)=2t(t^4-1)\) is a squarefree quintic, whose smooth projective hyperelliptic model has genus two. The Hasse–Weil bound implies
\[
\left|\sum_{t\in\mathbb F_p}\chi(2t(t^4-1))\right|\le4\sqrt p.
\]
Expanding the eight terms and taking the worst sign for each one therefore gives
\[
\sum_t I_{a,b,c}(t)\ge p-3-10\sqrt p
\quad\Longrightarrow\quad
8N_p(a,b,c)\ge p-23-10\sqrt p.
\]
The right side is positive at \(p=149\) and increases for all real \(p\ge149\). Thus **every** sign word, and in particular all six mixed words, occurs for every prime \(p\ge149\). This is a proof of the infinite range, not a finite-data extrapolation.

It remains to classify odd primes below \(149\). For each such prime, the attached `checker.py` enumerates all \(t=0,\ldots,p-1\), rejects parameters for which any of \(F,H,G\) vanishes, and computes each remaining Legendre sign independently via modular exponentiation and via a quadratic-residue set. The two calculations agree for all \(33\) odd primes below \(149\). The complete list of failures for at least one **mixed** word is precisely \(3,5,7,13,17,29\). Their missing mixed patterns are printed in `checker-output.txt`. Every other prime below \(149\) realizes all six. This proves both directions of the theorem.

## Verification

Run `python3 checker.py` with Python 3 and no third-party packages. It tests the two independent residue criteria at every relevant prime below the proven analytic cutoff, asserts the exact exceptional-prime and missing-word sets, records six witnesses at \(p=31\), and additionally tests \(17\) larger primes as nonessential stress tests. `checker-output.txt` contains actual output from this execution. All prime testing is exact trial division; the modular Legendre method is Euler's criterion. The finite checks are exhaustive **only** over the \(33\) primes below \(149\), while the analytic estimate covers all larger primes.

## Relationship to prior work

Hu and Zhan (first published October 19, 2021) prove asymptotic equidistribution of eight quadratic-character sign patterns for a two-parameter Euclidean Pythagorean family. Their Theorems 1–2 yield eventual occurrence but do not classify exceptional primes for the one-parameter normalized family used here. The reduction of their two-parameter form by a nonzero square factor makes the connection substantive, not merely titular. Xi and Zheng (2024) establish eventual eight-sign existence for a broader class of Pythagorean solutions, without the sharp threshold for the specific normalized family. Li and Wang (published November 25, 2025) explicitly count the **two monochromatic words** for exactly this normalized family, whereas the present statement deals with the complementary **six mixed words**; their publicly accessible abstract and opening page do not state this exact six-pattern classification. The full Li–Wang article was not obtained, so an implicit derivation from its Jacobi-sum evaluations remains a priority risk.

OEIS A344620 describes an additional **height-restricted** condition on the positive parameter, requiring all three integer entries to be smaller than the prime, and only the all-positive pattern. Its prime exception list is therefore not a table for the present finite-field problem.

## Limitations

The theorem does **not** assert an optimal effective lower bound for arbitrary pattern counts, a complete enumeration of all eight words, or the existence of positive integer Pythagorean triples satisfying a height bound. The uniform \(149\) analytic cutoff is deliberately nonsharp; the exact \(31\) mixed cutoff depends on a fully enumerated finite range. Scientific priority is based on the inspected sources, not on an independent or exhaustive literature certification. A more comprehensive Jacobi-sum treatment could imply the classification even if it does not state it explicitly.

## References

1. J. Hu and Y. Zhan, *Pythagorean triples and quadratic residues modulo an odd prime*, AIMS Mathematics 7 (2022), 957–966, DOI: `10.3934/math.2022057`; first public date in PDF: October 19, 2021. Full text: https://www.aimspress.com/aimspress-data/math/2022/1/PDF/math-07-01-057.pdf.
2. P. Xi and J. Zheng, *Pythagoras equations and quadratic residues*, Acta Mathematica Sinica, Chinese Series 67 (2024), 220–226, DOI: `10.12386/A20220113`. https://actamath.cjoe.ac.cn/Jwk_sxxb_cn/EN/10.12386/A20220113.
3. Y. Li and H. Wang, *The number of quadratic residue Pythagorean triples*, International Journal of Number Theory 22 (2026), 407–418, DOI: `10.1142/S1793042126500247`, first published November 25, 2025. https://doi.org/10.1142/S1793042126500247.
4. OEIS A344620, https://oeis.org/A344620 (height-restricted monochromatic pattern only).
5. Classical Hasse–Weil bounds for quadratic-character sums of squarefree cubic, quartic, and quintic polynomials; genus one and two smooth projective curves.
