# Complete palindromic factor language of an aperiodic Parikh-collinear fixed point

## Finding

Let \(\varphi\) be the nonuniform binary morphism \(\varphi(0)=010011\) and \(\varphi(1)=1001\), and let \(\mathbf w=\varphi^\omega(0)\). There are **exactly 37 distinct nonempty palindromic factors** of \(\mathbf w\). Their largest length is **23**. The exact palindromic complexity \(P_{\mathbf w}(n)\), which counts distinct nonempty length-\(n\) factors equal to their reversal, is

\[
P_{\mathbf w}(n)=
\begin{cases}
3,&n\in\{3,13\},\\
1,&n=12,\\
2,&n\in\{1,2,4,5,6,7,8,9,10,11,15,17,19,21,23\},\\
0,&\text{otherwise},
\end{cases}\qquad(n\ge1).
\]

The complete language (each word is written explicitly rather than represented by a frequency) is:

| Length | Palindromic factors | Count |
|---:|---|---:|
| 1 | `0`, `1` | 2 |
| 2 | `00`, `11` | 2 |
| 3 | `010`, `101`, `111` | 3 |
| 4 | `0110`, `1001` | 2 |
| 5 | `01010`, `01110` | 2 |
| 6 | `001100`, `110011` | 2 |
| 7 | `0010100`, `0011100` | 2 |
| 8 | `01100110`, `10011001` | 2 |
| 9 | `100101001`, `100111001` | 2 |
| 10 | `0011001100`, `1100110011` | 2 |
| 11 | `01001110010`, `11001010011` | 2 |
| 12 | `100110011001` | 1 |
| 13 | `0110010100110`, `1010011100101`, `1110010100111` | 3 |
| 15 | `010100111001010`, `011100101001110` | 2 |
| 17 | `00101001110010100`, `00111001010011100` | 2 |
| 19 | `1001010011100101001`, `1001110010100111001` | 2 |
| 21 | `010011100101001110010`, `110010100111001010011` | 2 |
| 23 | `01100101001110010100110`, `10100111001010011100101` | 2 |

Exactly six of these palindromes are **center-maximal**: they have no extension of the form \(apa\) that is also a factor of \(\mathbf w\), where \(a\in\{0,1\}\) and \(p\) is the palindrome. They are:

- `010`
- `1100110011`
- `100110011001`
- `0110010100110`
- `01100101001110010100110`
- `10100111001010011100101`

The two palindromes of length 23 are the longest possible, and neither has a symmetric one-letter extension.

## Assumptions and scope

Words are one-sided indexed from zero over \(\{0,1\}\); a factor is any contiguous finite substring occurring anywhere. A palindrome is a nonempty word identical to its reversal. The fixed point exists because \(\varphi(0)\) begins with 0 and has length greater than 1; no periodicity, synchronization, or positivity assumptions are added. The statement applies to this **specific** morphism, not to every Parikh-collinear morphism. Center-maximal means no symmetric one-letter extension in the full infinite factor language; it does not mean that the palindrome occurs only in that form or cannot extend asymmetrically.

## Proof

**Step 1 (all source pairs occur).** The length-two factors of \(\varphi(0)=010011\) are exactly \(\{00,01,10,11\}\). Since this word is a prefix of \(\mathbf w\), all four source pairs \(ab\in\{0,1\}^2\) occur in \(\mathbf w\).

**Step 2 (exact finite-factor reduction).** Direct substitution gives \(|\varphi^3(0)|=150\) and \(|\varphi^3(1)|=100\). Using the fixed-point identity \(\mathbf w=\varphi^3(\mathbf w)\), split \(\mathbf w\) into adjacent level-three substitution blocks \(\varphi^3(\mathbf w_i)\). Every contiguous factor with length at most 25 crosses **at most one** boundary between these blocks: each complete block has length at least 100. Thus that factor belongs to the length-25-or-shorter factor language of \(\varphi^3(ab)\) for some adjacent source pair \(ab\). Conversely, by Step 1 every \(ab\) occurs in \(\mathbf w\), so every factor of any \(\varphi^3(ab)\) occurs in \(\mathbf w\). Therefore for **every** integer \(1\le n\le25\):

\[
\mathcal F_n(\mathbf w)=\bigcup_{a,b\in\{0,1\}}\mathcal F_n\bigl(\varphi^3(ab)\bigr),
\]

where \(\mathcal F_n(x)\) denotes the set of length-\(n\) factors of \(x\). This equality is for the infinite word and has no truncation or sample-size hypothesis.

**Step 3 (finite exact computation).** The four words \(\varphi^3(00)\), \(\varphi^3(01)\), \(\varphi^3(10)\), and \(\varphi^3(11)\) have lengths 300, 250, 250, and 200. Exhaustive comparison of every window of each length \(1\le n\le25\) against its reversal (23,800 inspected windows, with repeated windows allowed) gives precisely the 37-palindrome catalogue in the Finding section, and **no palindromes of length 24 or 25**. The attached `verify_palindromes.py` is a standalone exact-language certificate: it independently reconstructs the four morphic blocks, enumerates all windows, and asserts equality with the *explicit* catalogue; it does not infer a general result from a finite prefix.

**Step 4 (global completeness).** Every even palindrome of length at least 24 has a centered palindromic factor of length 24; every odd palindrome of length at least 25 has a centered palindromic factor of length 25. Both are absent by Step 3. Therefore no palindrome of length greater than 23 occurs anywhere in \(\mathbf w\). Counting the catalogue by length yields the stated complexity function and total 37.

**Step 5 (center-maximal factors).** A palindrome \(p\) admits a symmetric one-letter extension precisely when at least one of \(0p0\) or \(1p1\) is a factor. Both proposed extensions are themselves palindromes; they must therefore belong to the complete catalogue. Testing these two extensions for every one of the 37 entries leaves exactly the six stated center-maximal factors. This proves their global maximality and exhaustiveness.

## Verification

Run `python3 verify_palindromes.py` with Python 3; it has no dependencies beyond the standard library and prints:

```text
VERIFY_OK pairs=4 n=1..25 palindromes=37 center_maximal=6 exhaustive_windows=23800 prefix_windows=468450
```

In addition to the exact exhaustive four-pair certificate, the verifier generates an independent 18,750-symbol prefix via six substitutions and confirms that its palindromic factors through length 25 agree with the proved catalogue. This prefix check is a supplementary diagnostic only; the infinite completeness is proved by Steps 1–4.

## Relationship to prior work

Rigo, Stipulanti, and Whiteland introduced and analyzed precisely this morphism in the 2023 paper *Automaticity and Parikh-collinear Morphisms* (Example 1 and the study of aperiodic 5-automatic abelian complexity). Their 2024 extension studies abelian complexity and recognizability rather than palindromic factors. The present claim is an **exact finite palindromic factor-language classification** for their word, not a claim to its definition, automaticity, or aperiodicity. Dvořáková, Ochem, and Opočenská consider critical exponents of binary words with few palindromes, not the exact 37-palindrome language of this fixed point. Frid, Laborde, and Peltomäki prove a general conditional regularity theorem for prefix palindromic length when an automatic word has finitely many palindromes, but their theorem alone neither verifies this condition for the present word nor yields the explicit catalogue. The present result supplies that condition for this particular word and hence makes their theorem applicable to it.

## Limitations

The catalogue describes distinct factors, **not** the number or natural density of their occurrences. It does not classify palindromes for other Parikh-collinear morphisms, compute the prefix palindromic-length function, or prove an independent novelty certificate. The exhaustive finite reduction and all associated computed comparisons are reproducible; independent scientific review has not been performed. Published equivalence outside the inspected sources remains possible.

## References

1. M. Rigo, M. Stipulanti, M. A. Whiteland, *Automaticity and Parikh-collinear Morphisms*, DLT–WORDS (2023), DOI: 10.1007/978-3-031-33180-0_19. Open conference manuscript: https://orbi.uliege.be/bitstream/2268/302523/1/conf-version.pdf (repository publicly available since 2023-05-11).
2. M. Rigo, M. Stipulanti, M. A. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, Theory of Computing Systems (2024), DOI: 10.1007/s00224-024-10197-5. Open full text: https://link.springer.com/article/10.1007/s00224-024-10197-5.
3. Ľ. Dvořáková, P. Ochem, D. Opočenská, *Critical exponent of binary words with few distinct palindromes*, arXiv:2311.13003 (2023). https://arxiv.org/abs/2311.13003.
4. A. E. Frid, E. Laborde, J. Peltomäki, *On prefix palindromic length of automatic words*, arXiv:2009.02934 (2020). https://arxiv.org/abs/2009.02934.
