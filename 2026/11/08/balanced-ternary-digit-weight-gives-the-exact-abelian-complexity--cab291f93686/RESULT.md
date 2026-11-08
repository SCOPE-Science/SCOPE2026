# Balanced-ternary digit weight gives the exact abelian complexity of every Stewart word

## Finding

For **every** infinite directive word over the six Stewart patterns and for either permissible binary completion of a persistent hole, the abelian complexity of its binary Toeplitz word at every positive factor length \(n\) is

\[
\boxed{\rho_{\mathrm{ab}}(n)=1+H_3(n)},
\]

where \(H_3(n)\) is the number of nonzero digits in the unique *balanced ternary* expansion
\[
n=\sum_{j\ge0}\epsilon_j3^j,\qquad \epsilon_j\in\{-1,0,1\},
\]
with finitely many nonzero digits. More precisely, if \(\mathcal P(n)\) is the set of Parikh vectors of its length-\(n\) factors (the first coordinate counts zeros), then

\[
\boxed{\mathcal P(n)=\left\{(n-j,j):\ j\in\mathbb Z,\quad
\frac{n-H_3(n)}2\le j\le\frac{n+H_3(n)}2\right\}.}
\]

Thus every word in this uncountable family has the *same entire Parikh-vector spectrum at each length*, even though the words need not share their ordinary factor languages. For every \(k\ge1\),
\[
\rho_{\mathrm{ab}}(3^k)=2,\qquad
\rho_{\mathrm{ab}}\!\left(\frac{3^k+1}{2}\right)=k+2.
\]
Consequently every such Stewart word has unbounded abelian complexity and is not \(C\)-balanced for any fixed constant \(C\).

## Assumptions and scope

Take the alphabet \(\{0,1\}\) and the six ternary templates

| Code | Template |
|:--:|:--:|
| `a` | `01?` |
| `b` | `10?` |
| `c` | `0?1` |
| `d` | `1?0` |
| `e` | `?01` |
| `f` | `?10` |

Let \(\tau=(\tau_0,\tau_1,\ldots)\) be any infinite sequence of these templates. Starting with a periodic repetition of \(\tau_0\), fill its holes in order with periodic repetitions of \(\tau_1\), then \(\tau_2\), and so forth. The limit is a binary infinite word except possibly at one position that remains a hole; if this happens assign either bit there. Every such choice is included. Index letters from zero. For a finite factor \(u\), its Parikh vector is \((|u|_0,|u|_1)\); \(\rho_{\mathrm{ab}}(n)\) counts the distinct vectors of length-\(n\) factors. The result concerns contiguous factors and all positive integers \(n\), with no periodicity assumption on \(\tau\).

## Proof

**1. Triple-block identity.** Encode the letters by signs \(\chi(i)=2s(i)-1\in\{-1,1\}\). If the first template has its hole at residue \(q\in\{0,1,2\}\), the other two residues carry the signs \(-1\) and \(+1\) in some order, while
\[
\chi(3j+q)=\chi_{\sigma\tau}(j),\qquad j\ge0,
\]
where \(\sigma\tau\) removes the first directive symbol. The identity also holds with either completion of a persistent hole, by propagating the same completed symbol to the residual descendant.

**2. Extremal factors can be used at every phase.** Every finite factor of any completed Stewart word occurs infinitely often. Indeed, fix a factor at start \(i\) of length \(n\) and choose \(K\) with \(3^K>i+n\). Within its window, at most one position has the first \(K\) ternary digits equal to all \(K\) hole residues. Every other symbol is fixed by a level below \(K\), so remains unchanged under translating the start by multiples of \(3^K\). If the one exceptional position exists, choose the next ternary digit of the translation at level \(K\) to be the non-hole residue whose template symbol matches its original completed bit; either bit is available because each template contains both. All translations with that level-\(K\) digit and arbitrary higher digits reproduce the entire factor. In particular, omitting finitely many initial start positions never changes the largest or smallest sum of a fixed factor length.

**3. Exact phase decomposition.** Let \(U_\tau(n)\) and \(L_\tau(n)\) denote the maximum and minimum of the signed sum \(\sum_{h=0}^{n-1}\chi(i+h)\) over all starts \(i\ge0\). They are attained, since sums are integers in a finite range. Put \(U_\tau(0)=L_\tau(0)=0\). Both letters occur already at non-hole residues of every triple, hence \(U_\tau(1)=1\) and \(L_\tau(1)=-1\).

For each length \(n=3m+r\), the number \(q\) of hole positions inside an interval, together with the signed sum \(c\) of its non-hole template symbols, runs through the following *complete* phase multisets, independent of the chosen template:

| Length | Three pairs \((q,c)\) |
|:--|:--|
| \(3m\) | \((m,0),(m,0),(m,0)\) |
| \(3m+1\) | \((m,-1),(m,1),(m+1,0)\) |
| \(3m+2\) | \((m,0),(m+1,-1),(m+1,1)\) |

The hole symbols form a *contiguous factor* of the tail word, starting at a tail position \(j\) or \(j+1\). By Step 2, every extremal tail factor may be realized in either case. Therefore, for \(n\ge2\),
\[
\begin{aligned}
U_\tau(3m)&=U_{\sigma\tau}(m),\\
U_\tau(3m+1)&=\max\{U_{\sigma\tau}(m)+1,U_{\sigma\tau}(m+1)\},\\
U_\tau(3m+2)&=\max\{U_{\sigma\tau}(m),U_{\sigma\tau}(m+1)+1\}.
\end{aligned}
\]
The corresponding minimum recurrences replace \(U\) with \(L\), \(\max\) with \(\min\), and reverse the added sign \(+1\) to \(-1\) in the extremal term. Explicitly, their candidate sets are \(\{L(m)-1,L(m)+1,L(m+1)\}\) for residue one and \(\{L(m),L(m+1)-1,L(m+1)+1\}\) for residue two, with the appropriate tail subscript.

**4. Balanced ternary recurrence.** Uniqueness of the balanced ternary representation gives
\[
H_3(0)=0,\quad H_3(1)=1,\quad
H_3(3m)=H_3(m),\quad
H_3(3m+1)=H_3(m)+1,\quad
H_3(3m+2)=H_3(m+1)+1.
\]
Also \(|H_3(m+1)-H_3(m)|\le1\). To see this last fact, add one to a balanced ternary expansion: a trailing string of digits \(+1\) is replaced by digits \(-1\) with a carry; its count of nonzero digits stays unchanged, and the first other digit either changes from \(-1\) to \(0\), from \(0\) to \(+1\), or creates a new leading \(+1\). Thus the weight changes by at most one.

Induct simultaneously for **all** directive tails on the integer \(n\). The cases \(n=0,1\) hold. Every index on the right in Step 3 is strictly smaller than \(n\) for \(n\ge2\). Substituting the induction hypothesis \(U=H_3\) and \(L=-H_3\) into the phase recurrences, then applying the Lipschitz inequality, yields the three recurrences in this step for \(U\), and their negatives for \(L\). Hence for every \(\tau,n\),
\[
U_\tau(n)=H_3(n),\qquad L_\tau(n)=-H_3(n).
\]

**5. Every intermediate Parikh vector occurs.** The signed sum of a length-\(n\) window equals \(2|u|_1-n\), so its extrema give respectively \((n-H_3(n))/2\) and \((n+H_3(n))/2\) ones. These endpoints are integers because each balanced ternary power is odd and \(n\equiv H_3(n)\pmod 2\). Moving the start of a window forward by one changes its number of ones by at most one. Between windows attaining the two extrema, every intermediate integer count therefore occurs. This proves the displayed Parikh-vector formula and its cardinality \(H_3(n)+1\).

Finally, the balanced representation of \(3^k\) consists of one nonzero digit, whereas \((3^k+1)/2=3^k-\sum_{j=0}^{k-1}3^j\) has exactly \(k+1\) nonzero balanced digits. This proves the two evaluations and unboundedness.

## Verification

The included standalone `verify.py` uses only Python and NumPy. It independently verifies the complete finite phase table for all six templates and lengths \(1\) through \(299\), balanced-ternary recurrences and digit-weight Lipschitz bounds through \(100000\), and exact finite-window minima and maxima for \(34\) diverse directive samples, lengths \(1\) through \(256\), in prefixes of length \(3^9\). It separately tests both completions of a persistent hole and the two infinite peak families through \(k=11\). The observed run was:

`VERIFY_OK directives=34 phase_cases=1794 digit_cases=100000 window_cases=8960 peaks=11`

Reproduce with `python3 verify.py` in a Python environment with NumPy. These tests are finite diagnostics; the infinite and all-directive assertions follow from the five proof steps, not from finite-window enumeration.

## Relationship to prior work

Fici and Shallit, *Properties of a Class of Toeplitz Words* (first posted 2021-12-22), define the identical six-pattern Stewart family and establish ordinary factor complexity \(2n\), a palindromic-factor classification, critical exponent, square orders and further properties. Their Theorem 9 counts **distinct words**, not their Parikh-vector classes; that result by itself cannot supply the digit-weight identity or the unboundedness asserted here. The exact phase decomposition above is specific to the six permutations of `01?` and does not follow merely from knowing factor complexity.

Shallit's *Abelian Complexity and Synchronization* (2020) treats a computation method requiring **bounded** abelian complexity; the present family has unbounded abelian complexity, so that theorem is inapplicable. Khodier's 2026 thesis reports ordinary subword complexity and critical exponents for several three-uniform binary morphisms, including Stewart choral, without an inspected matching abelian-weight formula. The OEIS entry A116178 gives the classic choral recurrence, not the asserted all-directive Parikh classification.

## Limitations

The exact result is for the six binary length-three Stewart templates, each containing one zero, one one and one hole. It does not assert the same formula for other Toeplitz template lengths or alphabets, and it gives no individual occurrence *frequencies* for different Parikh vectors. Bibliographic novelty has been checked against the named sources and mathematical records but an unindexed equivalent is possible. Independent external audit has not been performed.

## References

1. G. Fici and J. Shallit, *Properties of a Class of Toeplitz Words*, arXiv:2112.12125v1 (2021-12-22), https://arxiv.org/abs/2112.12125 ; Theorems 5, 6, 9, 10, 11.
2. J. Shallit, *Abelian Complexity and Synchronization*, arXiv:2011.00453v3 (2020), https://arxiv.org/abs/2011.00453 ; Theorem 1.
3. G. Fici and S. Puzynina, *Abelian combinatorics on words: A survey*, 2022, https://doi.org/10.1016/j.cosrev.2022.100532 .
4. M. Khodier, *New Methods for Analyzing the Properties of Automatic Sequences*, thesis (2026), https://hdl.handle.net/10012/22844 ; Chapters 3, 5-7.
5. OEIS A116178, *Stewart's choral sequence*, https://oeis.org/A116178 .
