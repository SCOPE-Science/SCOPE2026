# Exact binary zero-run spectrum of the five-ary Fuss–Catalan numbers

## Finding
For every nonnegative integer \(n\), define the five-ary Fuss–Catalan (Raney) number
\[
C(n)=R_{5,1}(n)=\frac{1}{4n+1}\binom{5n}{n}.
\]
The number \(C(n)\) is odd if and only if the binary expansion of \(n\) has no pair of set bits two positions apart. Equivalently, \(n\mathbin{\&}(n\ll2)=0\), where \(\&\) and \(\ll\) denote bitwise AND and left shift.

A *zero run* is a maximal, nonempty consecutive block of indices at which \(C(n)\) is even, bounded on both sides by odd terms. Every zero run is finite. The set of **distinct positive zero-run lengths** is exactly
\[
\mathcal L=\left(\left\{\left\lfloor\frac{2^j}{5}\right\rfloor:j\ge0\right\}\cup
\left\{\left\lfloor\frac{3\cdot 2^j}{5}\right\rfloor:j\ge0\right\}\right)\setminus\{0\}.
\]
Every distinct positive length is a *strict* left-to-right record at its first appearance. The first such values are \(1,2,3,4,6,9,12,19,25,38,51,76,\ldots\). The first length \(\lfloor2^j/5\rfloor\) from the first family is realized immediately before the odd term with index \(2^j\), and the first length \(\lfloor3\cdot2^j/5\rfloor\) from the second is realized immediately before index \(3\cdot2^j\). Here the word *first* refers to these respective families, with the duplicate value \(1\) appearing earlier in the second family.

For every integer \(m\ge0\), the exact number of odd terms among \(C(0),\ldots,C(2^m-1)\) is
\[
N(m)=F_{\lceil m/2\rceil+2}F_{\lfloor m/2\rfloor+2}
=\frac{\varphi^{m+4}}5+O(1),
\]
where \(F_0=0,F_1=1\), \(F_{a+2}=F_{a+1}+F_a\), and \(\varphi=(1+\sqrt5)/2\). In particular the odd terms have natural density zero.

## Assumptions and scope
The modulus is the prime \(2\), and the Raney parameters are fixed at \((k,r)=(5,1)\). These parameters satisfy \(2\nmid kr\). The run spectrum is taken over the full infinite sequence \(n\ge0\), not a truncated interval. The theorem determines distinct positive run lengths and their first occurrences, but does not give the number of occurrences of a given length in a finite interval.

## Proof
**Step 1: Exact parity criterion.** The denominator \(4n+1\) is odd. By Kummer's theorem, the \(2\)-adic valuation of \(\binom{5n}{n}\) is the number of carries in the addition \(n+4n\) in base \(2\). A carry occurs if and only if the two binary supports overlap at some digit position, including at the earliest such position if there are potential propagated carries. Thus the binomial coefficient is odd exactly when \(n\) and \(4n\) have disjoint one-bits, equivalently when no two one-bits of \(n\) lie at distance \(2\). Call an index satisfying this condition *admissible* and denote the set by \(S\).

**Step 2: Consecutive admissible indices.** Fix any \(b>0\) in \(S\) and let \(j=\nu_2(b)\). Thus the lowest set bit of \(b\) is at position \(j\), and the bit at position \(j+2\) is necessarily zero. Write \(s\in\{0,1\}\) for its bit at position \(j+1\). Flipping bit \(j\) from one to zero preserves admissibility, so \(b-2^j\in S\). Every index between \(b-2^j\) and \(b\) has the same higher binary prefix as \(b\), a zero at position \(j\), and a freely chosen lower \(j\)-bit suffix. The suffix must have no set bits two positions apart and must also respect the fixed bit \(s\) at position \(j+1\). Hence the greatest admissible predecessor of \(b\) is
\[
a=b-2^j+M_s(j),
\]
where \(M_s(j)\) is the largest integer represented by an allowed suffix in positions \(0,\ldots,j-1\). Maximizing that integer requires greedy assignment from its highest bit downward: choose each bit as one whenever the bit two positions above is zero. This is optimal, since a chosen higher bit outweighs the sum of all lower positions.

For \(s=0\), the successive high-to-low blocks are \(1100,1100,\ldots\); for \(s=1\), the initial pattern is \(0110\), then repeats the same four-step mechanism. The initial values for \(j=0,1,2,3\) are
\[
(M_0(0),M_0(1),M_0(2),M_0(3))=(0,1,3,6),
\quad(M_1(0),M_1(1),M_1(2),M_1(3))=(0,0,1,3).
\]
For every \(j\ge4\), inspection of the top four chosen bits gives
\[
M_0(j)=3\cdot 2^{j-2}+M_0(j-4),\qquad
M_1(j)=3\cdot 2^{j-3}+M_1(j-4).
\]
The unique solutions of these recurrences with the displayed initials are
\[
M_0(j)=2^j-1-\left\lfloor\frac{2^j}{5}\right\rfloor,\qquad
M_1(j)=2^j-1-\left\lfloor\frac{3\cdot2^j}{5}\right\rfloor.
\]
The number of even terms strictly between the consecutive odd terms at \(a\) and \(b\) therefore equals \(b-a-1=2^j-M_s(j)-1\), giving precisely the two asserted length formulas. Conversely every pair \((j,s)\) is realized: \(b=2^j\) gives \(s=0\), while \(b=3\cdot2^j\) gives \(s=1\). The lengths are thus exact, not just upper bounds. Admissible indices include every power of two, so no infinite terminal zero block exists.

**Step 3: First occurrences and records.** For fixed \(j,s\), any admissible \(b\) with the specified lowest set bit and bit above it satisfies \(b\ge2^j\) for \(s=0\) and \(b\ge3\cdot2^j\) for \(s=1\); both lower bounds occur, as above. Every positive length from the second family first appears at \(b=3\cdot2^j\) for \(j\ge1\); every positive new length from the first family appears at \(b=2^j\) for \(j\ge4\). At \(j=3\), the first-family value equals the second-family value at \(j=1\), namely \(1\). For all \(j\ge2\), the strict inequalities
\[
\left\lfloor\frac{3\cdot2^j}{5}\right\rfloor <
\left\lfloor\frac{2^{j+2}}{5}\right\rfloor <
\left\lfloor\frac{3\cdot2^{j+1}}{5}\right\rfloor
\]
interlace the distinct values in exactly the same order as their first endpoints \(3\cdot 2^j<2^{j+2}<3\cdot2^{j+1}\). Starting with \(1\) at endpoint \(6\), every first occurrence consequently exceeds every earlier gap length, proving the strict-record assertion.

**Step 4: The odd-support census.** In a binary string of \(m\) bits, the prohibition of ones two places apart separates into two independent prohibitions of adjacent ones on its even-position and odd-position subsequences. These have lengths \(\lceil m/2\rceil\) and \(\lfloor m/2\rfloor\). The number of binary strings of length \(t\) without adjacent ones is \(F_{t+2}\), yielding the formula for \(N(m)\). Binet's formula gives the displayed asymptotic, and since \(\varphi<2\), the fraction \(N(m)/2^m\) tends to zero. The same bound between neighboring powers of two proves natural density zero over all indices.

## Verification
The accompanying standalone `verify.py` uses exact Python integers to compare the literal binomial-quotient parity with the binary carry condition for indices \(0\) through \(1199\), checks both predecessor formulas through \(j=32\), exhaustively compares the predicted and observed spectra for all \(m\le18\), and checks the strict-record list. These finite computations test the proof; the four exact arguments above establish its unrestricted conclusions. The verification output includes `VERIFY_OK exact_finite_checks=yes infinite_proof_is_structural=yes`.

## Relationship to prior work
Eu, Huang, and Kao (2026), arXiv:2609.25742v1, determine the complete spectra of \(R_{3,2}\) modulo primes and formulate Conjecture 7.1 on finite exponential families of records for general Raney numbers. The present theorem is the explicit full spectrum for the *different* parameters \((5,1,2)\), with an exact odd-support census. A publicly available general Raney zero-run family-containment theorem also states a finite-family existence result for all eligible parameters. That broad result is **not** an explicit classification: it neither supplies these two exact families nor proves converse realization, first-occurrence positions, or this support count. The present claim is therefore the sharper explicit calculation for this fixed natural Fuss–Catalan case; it does **not** assert priority for the qualitative finite-family conjecture. Bobrowski, He, and Shiue (2019) study divisibility of generalized Catalan and Raney numbers but not this run spectrum. OEIS A002294 lists values of the underlying Fuss–Catalan sequence, not the proven run spectrum.

## Limitations
The exact two-family spectrum is specific to \(R_{5,1}\) modulo \(2\). It makes no claim for other primes, other Raney parameters, or multiplicities of finite-scale gap lengths. The literature priority comparison is bounded to the sources listed here and mathematical-record searches; an unindexed earlier equivalent theorem cannot be ruled out. Finite checks are not an independent mathematical audit.

## References
1. S.-P. Eu, Z.-T. Huang, L. Kao, *Zero-Run Spectra of the \((3,2)\) Raney Numbers Modulo Primes*, arXiv:2609.25742v1 (first posted 2026-09-22), especially Sections 1, 3, 6, 7 and Conjecture 7.1. https://arxiv.org/abs/2609.25742
2. *Raney Conjecture 7.1: zero-run record families*, public mathematical research dossier describing a general finite-family containment result (accessed 2026-11-04). https://www.trureturing.org/research/raney-conjecture-7-1-zero-run-record-families/
3. J. Bobrowski, T.-X. He, P. J.-S. Shiue, *Divisibility of Generalized Catalan Numbers and Raney Numbers*, J. Comput. Anal. Appl. 26 (2019), 1047–1058. https://scholars.iwu.edu/ws/portalfiles/portal/39724414/144%20divisibility%20of%20generalized%202019.pdf
4. OEIS A002294, fifth-order Fuss–Catalan numbers. https://oeis.org/A002294
