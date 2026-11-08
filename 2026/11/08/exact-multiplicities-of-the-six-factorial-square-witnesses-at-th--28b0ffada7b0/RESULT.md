# Exact multiplicities of the six-factorial square witnesses at the first Erdős–Graham boundary

## Finding
For strictly increasing integers \(1\le a<b<c<d<e<527\), let \(\mathcal W\) be the collection of ordered index sextuples \((a,b,c,d,e,527)\) for which
\[
a!\,b!\,c!\,d!\,e!\,527!
\]
is a perfect square. Exactly \(132\) such sextuples exist. More precisely, letting \(N(e)\) denote their number with penultimate index \(e\), the complete nonzero profile is
\[
N(523)=5,\qquad N(525)=1,\qquad N(526)=126,
\]
with \(N(e)=0\) at every other penultimate index, including \(e=524\). The explicit canonical complete list is `artifacts/witnesses.csv` and can be regenerated from `artifacts/verify.py`.

The previously established fact that \(527\) is the *least* positive integer requiring six distinct factorials is due to Erdős and Graham (1976), not a contribution of this note. The new finite invariant counts and classifies **all** optimal-size representations at that first boundary.

## Assumptions and scope
All factorial indices are positive integers; their order is strict and every factorial occurs once. We count subsets of six indices, not orderings of the factorial factors and not the associated square roots. The maximum index is exactly \(527\), and the product is required to be a positive integer square. The result is finite and unconditional. It does not characterize such multiplicities at other maxima or prove asymptotic distribution theorems.

## Proof
For a prime \(p\le527\), let \(\nu_p\) denote the usual valuation. Fix the increasing primes \(p_1,\ldots,p_t\le527\), and define the parity signature
\[
\sigma(m)=\sum_{i=1}^{t}\left(\nu_{p_i}(m!)\bmod2\right)2^{i-1}.
\]
Because the exponents refer to distinct binary coordinates, a product of factorials is a square if and only if the bitwise exclusive-or of its signatures is zero. Equivalently, the six-index condition is
\[
\sigma(a)\oplus\sigma(b)\oplus\sigma(c)\oplus\sigma(d)
=\sigma(e)\oplus\sigma(527).
\]

**Reduction to four penultimate indices.** The integer \(523\) is prime. It divides \(527!\) to exponent exactly one, and it divides no \(j!\) with \(j<523\). If the five other indices were all below \(523\), the complete product would have odd \(523\)-adic valuation. Therefore \(523\le e\le526\). This is a proved exhaustiveness bound, not a numerical guess.

**Exact finite enumeration.** For each of the four possible \(e\), form every pair \((a,b)\) with \(1\le a<b<e\), stored under the integer key \(\sigma(a)\oplus\sigma(b)\). Then enumerate every \((c,d)\) with \(1\le c<d<e\). Retrieve the pairs with key
\[
\sigma(e)\oplus\sigma(527)\oplus\sigma(c)\oplus\sigma(d)
\]
and retain precisely those satisfying \(b<c\). Every retained pair gives one valid sextuple. Conversely every sextuple has the unique decomposition into its first pair and next pair and necessarily appears in this retrieval, so the count is exhaustive without duplicate sextuples. Applying this exact integer procedure gives the four counts
\[
(N(523),N(524),N(525),N(526))=(5,0,1,126).
\]
Their sum is \(132\), proving the statement. All arithmetic is over integers and bit operations, with no probabilistic steps.

**Independent calculation of signatures and counts.** The accompanying verifier independently computes signatures both (i) by factoring each integer and accumulating parity signatures of factorials and (ii) by Legendre's formula
\[
\nu_p(m!)=\sum_{j\ge1}\left\lfloor\frac{m}{p^j}\right\rfloor.
\]
It also independently enumerates quadruples by reversing the lookup direction, compares the two full sets of sextuples rather than only their totals, and checks that they agree with every line of the complete witness list. Both calculations return the four counts displayed above. This is a finite exhaustive proof whose transparent loop bounds are part of the supplied source code; no unbounded computational assertion is inferred.

## Verification
With Python 3 standard library, execute `python3 artifacts/verify.py` with `artifacts/witnesses.csv` in the same directory as the verifier. The program independently computes prime valuations, enumerates all eligible pairs and quadruples with strict index inequalities, verifies all \(132\) tuples and the four-part distribution, and prints `VERIFY_OK`. The included CSV gives every counted tuple in increasing lexicographic order. For example, \((16,17,30,31,526,527)\) is included: dividing adjacent factorials into intervals shows the product is a square because \(17\cdot31\cdot527=(17\cdot31)^2\).

## Relationship to prior work
Erdős and Graham, *On Products of Factorials* (1976), Fact 14, identify \(527\) as the first largest argument requiring six factorial factors and exclude all five-factor products there. Their result **does not assert** a number of six-factor representations; this note uses their exact boundary as a canonical object and counts the optimum witnesses. Yudin, *Square products of factorials and a conjecture of Erdős and Graham* (arXiv:2610.01899, first posted 2026-10-01), proves asymptotic results for the counts of integer arguments requiring different numbers of factorials. Direct inspection of the full 2026 manuscript (introduction, the main theorems, Section 7.3, Section 8 and Appendix A, together with a full-document search for the specific boundary) found no exact multiplicity theorem for \(527\); that manuscript establishes asymptotic counts of arguments requiring each number of factors and general affine constructions. General accounts of the same problem, including Wolfram MathWorld's *Factorial Square Product*, list the first six-factor arguments but not the \(132\)-witness profile. Related Jordan–Pólya factorizations count arbitrary products of factorials, not the minimum six-element square representations with fixed maximum \(527\). This document makes no claim to priority over inaccessible or unindexed material.

## Limitations
The result is an exact finite enumeration at one canonical boundary, not a general formula for witness multiplicities. Its significance is as a complete extremal certificate and benchmark for searches involving the Erdős–Graham representation problem. Historical priority is not independently established; the directly relevant 2026 manuscript was inspected, but earlier unindexed computations or equivalent descriptions may exist. The proof relies on a readily reproducible finite census, not on a hand-derived symbolic closed form for the four counts.

## References
- P. Erdős and R. L. Graham, *On Products of Factorials*, Bulletin of the Institute of Mathematics Academia Sinica **4** (1976), 337–355, Fact 14, p. 353. https://users.renyi.hu/~p_erdos/1976-25.pdf
- Fedir Yudin, *Square products of factorials and a conjecture of Erdős and Graham*, arXiv:2610.01899, first public version 2026-10-01. https://arxiv.org/abs/2610.01899
- E. W. Weisstein, *Factorial Square Product*, Wolfram MathWorld, https://mathworld.wolfram.com/FactorialSquareProduct.html
- OEIS A389148, first integers requiring six factorials, https://oeis.org/A389148
