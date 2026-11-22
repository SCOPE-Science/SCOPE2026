# Exact 2-binomial reconstruction spectra with three doubled letters and singleton markers

## Finding

For every integer \(r\ge0\), use the labeled alphabet \(\{0,1,2,3,\ldots,r+2\}\) and the family \(\mathcal W_r\) of length-\(r+6\) words having exactly two copies of each of \(0,1,2\) and exactly one of each marker \(3,\ldots,r+2\). Empty marker sets are allowed. The **complete 2-binomial deck** records the number of scattered occurrences of every word of length at most two. Let \(N_s(r)\) count distinct decks with exactly \(s\) preimages in \(\mathcal W_r\).

**Theorem.** Every nonempty deck fiber has size \(1\), \(2\), or \(6\). For all \(r\ge0\), their exact populations are

\[
\begin{aligned}
N_1(r)&=\frac{r!(r+1)(r+2)}8\bigl(r^4+18r^3+107r^2+258r+192\bigr),\\
N_2(r)&=\frac{3r!(r+1)(r+2)(r+3)(r+4)}4,\\
N_6(r)&=\frac{r!(r+1)(r+2)}2.
\end{aligned}
\]

No other \(N_s(r)\) is nonzero. In particular, the exact number of distinguishable decks is

\[
N(r)=\frac{r!(r+1)(r+2)}8\bigl(r^4+18r^3+113r^2+300r+268\bigr).
\]

A uniformly sampled source is uniquely reconstructed from its full deck with probability

\[
\frac{N_1(r)}{|\mathcal W_r|}=1-\frac{12(r^2+7r+14)}{(r+3)(r+4)(r+5)(r+6)}
=1-\frac{12}{r^2}+O(r^{-3}),
\]

where \(|\mathcal W_r|=(r+6)!/8\) and the asymptotic expression concerns \(r\to\infty\).

## Assumptions and scope

Every alphabet symbol has an individual label, and positions are indexed linearly, not cyclically. The deck counts **scattered** ordered pairs: for symbols \(a,b\), \(\binom{w}{ab}=\#\{(i,j):i<j,\ w_i=a,\ w_j=b\}\). It also includes one-letter counts, and hence all equality-pair counts \(\binom{w}{aa}=\binom{|w|_a}{2}\). In particular, this is neither contiguous 2-Abelian equivalence nor the weaker conventional Parikh-matrix observation. Fibers are taken **within** \(\mathcal W_r\), not among unconstrained words.

## Proof

**1. Recover marker order and gap contents.** Each marker occurs exactly once. For any two distinct markers \(i,j\), precisely one of \(\binom{w}{ij}\) and \(\binom{w}{ji}\) equals one; therefore the marker order is determined by the deck. After fixing this order, mark the \(r+1\) gaps before, between and after the markers. For each core letter \(a\in\{0,1,2\}\), the counts \(\binom{w}{a i}\) determine how many \(a\)'s occur before every marker \(i\). Taking successive differences recovers the complete three-component Parikh vector of each gap. Conversely, these vectors and the marker order determine all marker-involving pair counts. The remaining independent data are the three oriented core pair counts \(\binom{w}{01}\), \(\binom{w}{02}\), and \(\binom{w}{12}\). Their reversed counterparts follow from \(\binom{w}{ab}+\binom{w}{ba}=4\) for distinct core letters.

**2. A finite universal certificate.** Delete the singleton markers and obtain one of the \(6!/(2!)^3=90\) ordered core words. If exactly \(k\) of the \(r+1\) gaps are nonempty, the core word is cut into \(k\) nonempty consecutive segments, using one of \(\binom5{k-1}\) possible cut sets. Group the resulting \((\text{core word},\text{cut set})\) pairs by (i) the ordered Parikh vectors of the segments and (ii) the full three-dimensional oriented core pair vector. Direct exact-integer enumeration of all \(90\cdot2^5=2880\) cases gives the following complete fiber-size table; entries count observable classes, not source words:

| Nonempty gaps \(k\) | Fiber size \(1\) | Fiber size \(2\) | Fiber size \(6\) |
|---:|---:|---:|---:|
| 1 | 48 | 18 | 1 |
| 2 | 336 | 54 | 1 |
| 3 | 792 | 54 | 0 |
| 4 | 864 | 18 | 0 |
| 5 | 450 | 0 | 0 |
| 6 | 90 | 0 | 0 |

This table is fully and reproducibly certified by `verify_spectrum.py`, including independent word/cut enumeration, exact grouping keys, all fiber sizes, and the mass equality \(\sum_s s\,d_{k,s}=90\binom5{k-1}\). It is a finite exhaustive lemma, not an extrapolation from values of \(r\).

**3. Lift the certificate to every \(r\).** Every marker order contributes the same spectrum, so there are \(r!\) marker orders. To choose exactly \(k\) nonempty core gaps among the \(r+1\) available positions, there are \(\binom{r+1}{k}\) choices. Consequently, for \(s\in\{1,2,6\}\),

\[
N_s(r)=r!\sum_{k=1}^6 d_{k,s}\binom{r+1}{k},
\]

where a binomial coefficient vanishes when \(k>r+1\). The polynomial identities in `verify_spectrum.py` reduce these finite binomial sums **symbolically** to the three displayed exact formulas, for every nonnegative integer \(r\). The certificate shows there are no other possible fiber sizes.

**4. Reconstructibility.** The number of sources is \((r+6)!/8\), because each of three letters repeats twice. Every size-one class contains one source. Dividing the formula for \(N_1(r)\) by the source count and simplifying gives the exact displayed probability; expansion at infinity gives the coefficient \(12\) and the order \(r^{-2}\).

## Verification

Run `python3 verify_spectrum.py` and `python3 verify_independent.py` with Python 3 and SymPy. The first script independently constructs the 90 core words, all 32 cut sets, the complete finite six-row fiber-size table and an exact symbolic polynomial identity, and verifies total source mass. The second does **not** use the cut table: it constructs full marker-containing words and measures every one-letter and ordered-two-letter subsequence count, verifying the fiber-size spectra separately for \(r=0,1,2,3,4,5\). For example, the triple \((N_1,N_2,N_6)\) at \(r=0\) is \((48,18,1)\), and at \(r=2\) is \((3888,540,12)\). The finite certificate together with the general bijection proves the theorem for **all** \(r\); the direct small-\(r\) runs are independent checks, not the basis for extrapolation.

## Relationship to prior work

Rigo–Salimov (2013) introduced binomial equivalence and its interpretation by scattered-subword counts. Lejeune–Rigo–Rosenfeld (2020) study general classes, give an algorithm for constructing a class and prove general growth-order results. Lejeune (2021, Chapter 2) develops the general framework and non-context-free results. None of the inspected relevant sections states a complete fixed-content all-\(r\) fiber spectrum for three doubled core letters and arbitrarily many *distinct* singleton markers. A related publicly indexed result provides an exact formula for **two** repeated core symbols and singleton markers; that statement does not imply the present three-letter joint three-pair spectrum or its six-element fibers. General generation algorithms imply finite computability, not the stated closed spectrum or asymptotic reconstruction probability.

## Limitations

The claim is restricted to precisely three core symbols each of multiplicity two; it does not classify arbitrary Parikh compositions or higher-order binomial decks. Historical priority may be affected by unindexed literature or computations; the stated exact spectrum is not independently audited. The code requires a standard Python 3 environment and SymPy only for the exact symbolic polynomial check.

## References

1. M. Rigo and P. Salimov, *Another Generalization of Abelian Equivalence: Binomial Complexity of Infinite Words*, WORDS 2013. Public author preprint available from 27 May 2013: https://orbi.uliege.be/handle/2268/149313 .
2. M. Lejeune, M. Rigo and M. Rosenfeld, *On the binomial equivalence classes of finite words*, International Journal of Algebra and Computation (2020), https://arxiv.org/abs/2001.11732 .
3. M. Lejeune, *On the k-binomial equivalence of finite words and k-binomial complexity of infinite words*, doctoral thesis (2021), https://orbi.uliege.be/handle/2268/259266 .
4. *Exact two-deck spectra and fiber multiplicities with distinct marker letters*, publicly indexed mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-two-deck-spectra-and-fiber-multiplicities-with-distinct-ma--26e221758afc .
