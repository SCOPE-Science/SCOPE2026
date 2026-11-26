# The extremal prime support for runs without adjacent coprime pairs

## Finding

Let \(N\) be a positive odd integer with exactly three distinct prime factors. For an integer start \(a\), call the pair \((a,a+1)\) good if \(\gcd(a(a+1),N)=1\). Let \(L(N)\) be the longest run of consecutive starts that are not good. The only possible prime support for a run of length fourteen is \(\{3,5,7\}\); this support does attain fourteen, and none of its runs goes beyond fourteen. Thus
\[
L(N)\le14,\qquad L(N)=14\quad\Longleftrightarrow\quad\operatorname{rad}(N)=105.
\]
For this support the fourteen-run starts are precisely \(2,89\pmod{105}\), a consequence also obtainable from earlier paired-Jacobsthal data. There are \(2N/105\) such classes modulo \(N\). The new part established here is the classification over **all** odd three-prime supports for the fixed offset one, not the fourteen-run calculation on the smallest support alone.

The coprimality test depends only on the distinct primes of \(N\). A good start exists by the Chinese remainder theorem (CRT), since for each odd prime one can avoid the residues \(0,-1\). Thus the maximum is finite. Prime powers are allowed. No analogous claim is made for even moduli, other offsets or a different number of prime factors.

## Proof

Suppose there is a bad run of fourteen. Write \(I=\{0,\ldots,13\}\) for the index set. At each prime \(p\mid N\), the covered indices are those congruent to \(-a-1\) or \(-a\pmod p\), a pair of adjacent residues. For distinct primes the phases can be set independently by the CRT.

**Supports not containing 3.** The maximum numbers of covered indices for \(p=5,7,11,13\) are respectively \(6,4,4,3\), since each mask consists of two adjacent residue classes in \(I\). For \(p\ge17\) the maximum is two. The only triple of distinct primes not containing 3 whose maxima sum to at least fourteen is \(5,7,11\), whose sum is exactly fourteen. Its masks would have to be disjoint and simultaneously maximal. For \(p=11\), a four-index mask must use adjacent residues among \(0,1,2\), the only classes with two representatives. Thus its indices are either \(\{0,1,11,12\}\) or \(\{1,2,12,13\}\). Both masks hit residues 1 and 2 modulo 5. A six-index mask for \(p=5\) must choose one of \(\{0,1\},\{1,2\},\{2,3\}\) modulo 5, since only \(0,1,2,3\) occur three times. It necessarily intersects the 11-mask, which rules out full coverage.

**Supports containing 3.** The 3-mask leaves one congruence class modulo 3 uncovered. Its indices form a step-three progression in \(I\) of length four or five. Each other prime is at least 5, and the progression has distinct residues modulo that prime (its step is invertible), so each other prime covers at most two of its indices. Therefore the uncovered class must have four indices, namely \(2,5,8,11\); equivalently \(a\equiv 2\pmod3\). If an additional prime were at least 11, the possible positive differences \(3,6,9\) among the four indices could not be congruent to \(0,1,-1\) modulo that prime. It would cover at most one of the four, a contradiction. This forces the support \(\{3,5,7\}\).

Write the four indices as \(i=3q-1\), \(q=1,2,3,4\). The two covered residues in \(q\) for each of 5 and 7 differ by \(\pm 3^{-1}\). The prime 7 must take \(\{1,3\}\) or \(\{2,4\}\). The prime 5 must take the complementary pair, and either such pair is possible for 5. The two residue pairs for each prime are \(\{-a/3,(1-a)/3\}\) modulo the corresponding prime. Solving them and \(a\equiv2\pmod3\) gives \(a\equiv2,89\pmod{105}\). Both assignments cover all fourteen indices. A run of fifteen would require consecutive starts of runs of fourteen, but the two allowed residues modulo 105 are not consecutive. This proves the bound, sharpness, and complete support classification.

## Verification

The accompanying `verify_paired_sieve_14.py` (Python standard library) gives an alternative exact exhaustion. It represents the masks for \(3,5,7,11,13\) by their actual congruence classes and any prime at least 17 by the permissive family consisting of the empty set, singleton indices and neighboring two-index sets. In a window of fourteen, no other mask is possible for a prime at least 17. Exactly twenty-six class triples arise, with no repeated small-prime slot. The verifier computes all their mask unions and checks that the only fully covered windows arise in the \((3,5,7)\) triple, in two phases. It independently checks both start residues modulo 105; sample scans at other prime supports are illustrative only. The argument above does not require executing the certificate.

## Relationship to prior work and limitations

Ziller and Morack's paired Jacobsthal function \(j_2(N)\) uses pairs with an even integer difference. When \(N\) is odd, any offset has an even representative modulo \(N\); in particular \(1+N\) represents offset one. Thus \(L(N)\le j_2(N)-1\). Their 2017 computation gives \(j_2(210)=30\); Lemma 1.1 of its `full_details.pdf` gives \(j_2(2M)=2j_2(M)\) for odd \(M\), hence \(j_2(105)=15\). Lemma 1.2 similarly implies \(j_2(3M)=3j_2(M)\) for \(3\nmid M\), which bounds \(L(3pq)\) by fourteen for distinct primes \(p,q\ge5\): two primes cover at most four indices in a window of length five.

For support \(\{3,5,7\}\), the earlier `remainders_2.txt` block at \(n=4\) contains all six maximal coverings of \(q=1,\ldots,4\) by two arbitrary residue classes for each of 5 and 7. Filtering with class differences \(\pm 3^{-1}\) keeps exactly rows 2 and 5, the two complementary pairs above. Matching the remaining residue modulo 3 and applying CRT gives the same starts \(2,89\pmod{105}\). The difference between that prior computation and this fixed-offset question is not parity: it is the requirement that all phases come from the same offset one, together with the universal quantifier over distinct prime supports. The primorial data do not by themselves rule out fixed-offset equality at other supports. OEIS A072753 tabulates the arbitrary-class version on the primorial range of primes starting at 5, not the universal fixed-offset classification.

The polynomial Jacobsthal function of Kalmynin–Konyagin concerns additive output shifts \(x+f(i)\), whereas the present translation changes the polynomial input. A fixed-center symmetric-pair calculation can be relevant, because \((C-q,C+q)\) has the same divisibility test as \((q-C,q+C)\), with offset \(2C\). The inspected bibliographic material for Nguyen's finite-window study does not settle whether its full text contains a matching special case. The coverage comparison does not prove historical priority.

## References

1. M. Ziller and J. F. Morack, *Divisibility in paired progressions, Goldbach's conjecture, and the infinitude of prime pairs*, [arXiv:1706.00317v1](https://arxiv.org/html/1706.00317v1), §2.
2. M. Ziller and J. F. Morack, *A short note on the computation of the generalised Jacobsthal function for paired progressions*, [arXiv:1706.03668v1](https://arxiv.org/html/1706.03668v1), Table 1; ancillary [full_details.pdf](https://arxiv.org/src/1706.03668v1/anc/full_details.pdf), §§1 and 3.3; ancillary [remainders_2.txt](https://arxiv.org/src/1706.03668v1/anc/remainders_2.txt), \(n=4\) block.
3. A. Kalmynin and S. Konyagin, *A polynomial analogue of Jacobsthal function*, [arXiv:2302.00459v2](https://arxiv.org/html/2302.00459v2), §1.
4. [OEIS A072753](https://oeis.org/A072753), *Maximum gap in two-stage prime-sieves*, comments and formula.
5. T. T. K. Nguyen, *Finite-Window Noncovering on Primorial Wheels: Higher-Order CRT Bounds and Shift Correlations*, [DOI 10.20944/preprints202608.1299.v1](https://doi.org/10.20944/preprints202608.1299.v1) (full text not inspected).
