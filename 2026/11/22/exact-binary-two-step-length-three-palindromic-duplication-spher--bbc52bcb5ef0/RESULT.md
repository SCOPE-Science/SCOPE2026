# Exact binary two-step length-three palindromic-duplication spheres through length twenty-two

## Finding

Let \(\Sigma=\{0,1\}\), and let \(D^{(2)}_3(w)\) consist of the **distinct** words obtained from \(w\in\Sigma^n\) by exactly two successive palindromic duplications, each copying a contiguous three-symbol factor, reversing the copy, and inserting it immediately after that factor. The second operation may act on letters inserted by the first. Put \(M(n)=\max_{w\in\Sigma^n}|D^{(2)}_3(w)|\).

**Finite exact theorem.** For every integer \(3\le n\le22\),
\[
M(n)=\begin{cases}
4,&n=3,\\
9,&n=4,\\
16,&n=5,\\
\dfrac{n(n+3)}2-3,&6\le n\le22.
\end{cases}
\]
The respective numbers of **labeled** maximizers are \(2,4,4\) for lengths \(3,4,5\). For **every integer** \(6\le n\le22\), there are exactly two labeled maximizers: the length-\(n\) prefix of \(011001100110\cdots\), and its bitwise complement (the corresponding prefix of \(100110011001\cdots\)). This is a complete finite classification, not an all-length conjecture.

The universal disjoint-window-commutation bound is
\[
U(n)=(n-2)(n+1)-\binom{\max\{n-4,0\}}2.
\]
For all \(6\le n\le22\), the exact binary deficit is \(U(n)-M(n)=2n-9\). For illustration, \(M(20)=227\), \(M(21)=249\), and \(M(22)=272\), whereas \(U(22)=307\).

## Assumptions and scope

All words have a **labeled binary alphabet** and contain exactly \(n\) input symbols. If \(w=uvw'\), with \(|u|=i\) and \(|v|=3\), define
\[
T_i(w)=uvv^{\mathrm R}w'.
\]
Positions begin at zero. Valid first starts are \(0\le i\le n-3\); valid second starts are \(0\le j\le n\), because the intermediate word has length \(n+3\). Thus
\[
D^{(2)}_3(w)=\{T_j(T_i(w)):0\le i\le n-3,\ 0\le j\le n\}.
\]
We count distinct resulting strings, not ordered histories. The claim is solely for \(3\le n\le22\). Its only asymptotic-looking polynomial expression is a finite-range identity; no extrapolation beyond this range is asserted.

## Proof

The proof is finite **complete enumeration**, with the executable C++17 certificate `verify.cpp` and its actual successful output `verify_output.txt` included. The following establishes that the program exhausts the stated domain and that its operations implement precisely the mathematical channel.

**Correct bit encoding.** Store a length-\(m\) binary word \(w_0\ldots w_{m-1}\) as the nonnegative integer \(x=\sum_{r=0}^{m-1}w_r2^r\). For a legal start \(i\), let \(t=\lfloor x/2^i\rfloor\bmod8\), and let \(R(t)\) reverse its three bits. Then the exact integer encoding of \(T_i(w)\) is
\[
(x\bmod2^{i+3})+2^{i+3}R(t)
+2^{i+6}\left\lfloor\frac{x}{2^{i+3}}\right\rfloor.
\]
The low \(i+3\) bits retain the original prefix, the next three bits are the reversed inserted factor, and the high bits contain the original suffix shifted three positions. `duplicate_bits` implements this equality using masks and shifts; it works for both operations. The largest resulting length in the stated domain is \(28\), so every shift and encoded word fits the 32-bit unsigned type, with no overflow or undefined shift.

**Exhaustive count.** For each source \(x\), the routine `exact_sphere` enumerates **every** ordered pair of legal starts in the Cartesian product of sizes \(n-2\) and \(n+1\). It generates their encoded output, sorts the entire output array, and counts its distinct integers by the exact adjacent-unique operation. Since the fixed output length is \(n+6\), two integers agree exactly when the two output strings agree. Thus this count equals \(|D^{(2)}_3(w)|\), without a sampling, integer program, heuristic, or optimization solver.

**Safe symmetry reduction.** Complementation commutes with every duplication: \(T_i(\overline w)=\overline{T_i(w)}\), by the operation's letter-independent copying and reversal. Consequently complementary sources have identical sphere sizes. Among every complementary pair, exactly one source has first bit zero. The loop visits all and only these \(2^{n-1}\) sources, using the half-open integer progression of even encodings from zero to \(2^n\). It doubles their observed maximizing count to recover the **entire labeled domain**, never assuming reversal symmetry or period-four structure. Across the twenty source lengths, it examines exactly \(2^{22}-4=4,194,300\) complement representatives, which cover all \(8,388,600\) labeled source words.

**Computed equality layers.** The completed certificate returned the following exact maximum sizes and labeled maximizing populations, computed independently for each length:

| \(n\) | \(M(n)\) | Maximizers |
|---:|---:|---:|
| 3 | 4 | 2 |
| 4 | 9 | 4 |
| 5 | 16 | 4 |
| 6 | 24 | 2 |
| 7 | 32 | 2 |
| 8 | 41 | 2 |
| 9 | 51 | 2 |
| 10 | 62 | 2 |
| 11 | 74 | 2 |
| 12 | 87 | 2 |
| 13 | 101 | 2 |
| 14 | 116 | 2 |
| 15 | 132 | 2 |
| 16 | 149 | 2 |
| 17 | 167 | 2 |
| 18 | 186 | 2 |
| 19 | 206 | 2 |
| 20 | 227 | 2 |
| 21 | 249 | 2 |
| 22 | 272 | 2 |

For each length \(6\le n\le22\), the verifier separately generates the length-\(n\) prefix of \(0110\) repeated and checks it attains the computed maximum. Since the full census finds only two maximizing words and complementation gives the second, these are **all** maximizers. The displayed expressions and populations follow by direct evaluation of the twenty certified rows. This establishes the stated finite theorem.

Finally, there are \((n-2)(n+1)\) histories. For each unordered pair of disjoint original three-symbol windows at starts \(a<b\) with \(b-a\ge3\), duplicating \(a\) and then the shifted \(b\) is equivalent to duplicating \(b\) and then \(a\). These disjoint pairs of histories total \(\binom{\max\{n-4,0\}}2\). Hence the asserted universal upper bound \(U(n)\) holds. Its difference from the finite binary capacities is the displayed exact arithmetic identity.

## Verification

From the directory containing the two supplied files, compile and run:

```sh
g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify.cpp -o verify
./verify 22 > verify_output.txt
```

The included `verify_output.txt` is the actual successful output. The final line reports `EXHAUSTIVE_PASS complement_representatives=4194300 lengths=3..22`. An independent **string-based** implementation in the same verifier constructs \(uvv^{\mathrm R}w'\) without any bitwise arithmetic and compares every complete history, for **all** binary sources at lengths \(3\) through \(10\). Its initial line reports `REFERENCE_OK words=2040 n=3..10`. Both the exhaustive counts and the small independent string reference must pass, or the program returns a nonzero exit code. The reference check is a coding cross-check, not a replacement for the exhaustive certificate.

## Relationship to prior work

Zabokritskiy [1] studies exactly two sequential duplications and proves the universal commutation bound is attained for **even** duplication lengths, not the length-three binary capacity here. The related all-odd-length theorem for large alphabets [2] assumes \(q\ge n\), which cannot apply to a binary input at lengths \(n\ge3\). The length-two palindromic-duplication extremizer classification [3] likewise concerns a different channel. Lenz, Wachter-Zeh and Yaakobi [4] provide earlier single-duplication coding bounds. Neither an even-length result, the large-alphabet odd-length result, nor a single-step theorem implies this finite binary maximum or its optimizer census. The universal upper bound is shared background, not claimed as a new result.

## Limitations

The polynomial formula and unique two-word optimizing structure are **not proved for \(n>22\)**. Tests outside the stipulated range, the apparent period-four pattern, or agreement with a proposed all-length formula do not extend this theorem. The exhaustive checker is a finite correctness certificate for the explicitly bounded domain, not an infinite mathematical proof. The result describes the largest **descendant sphere**, not the largest error-correcting code or its decoding complexity. A previously unlocated equivalent finite census could affect historical priority. Independent scientific audit has not been performed.

## References

[1] A. L. Zabokritskiy (Yohananov), *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, first publicly posted 2026-09-01; especially Section 5. https://arxiv.org/abs/2609.00779

[2] *Sharp exact-two palindromic-duplication spheres for odd block lengths over large alphabets*, public research record dated 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-exact-two-palindromic-duplication-spheres-for-odd-block-le--c4b4c103f5f1/RESULT.md

[3] *All maximizers of two-step length-two palindromic-duplication spheres*, public research record dated 2026-11-02. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-all-maximizers-of-two-step-length-two-palindromic-duplication-sp--b6dda3c39b4f/RESULT.md

[4] A. Lenz, A. Wachter-Zeh, and E. Yaakobi, *Duplication-Correcting Codes*, arXiv:1712.09345, first publicly posted 2017-12-24. https://arxiv.org/abs/1712.09345
