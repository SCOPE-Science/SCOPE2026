# Optimal constant-weight-three binary non-overlapping codes are primitive-necklace transversals

## Finding

For every integer \(n\ge3\), let \(M_3(n)\) be the maximum number of binary length-\(n\) words of Hamming weight exactly three that form a non-overlapping (cross-bifix-free) code. That is, for every two codewords \(u,v\), including \(u=v\), and every \(1\le k<n\), the length-\(k\) prefix of \(u\) must differ from the length-\(k\) suffix of \(v\). Then

\[
M_3(n)=\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]

An explicit optimal family contains exactly one representative of every primitive binary rotation class (aperiodic necklace) of length \(n\) and weight three, and no representatives of nonprimitive classes. Conversely, *every* optimal family selects one representative from each such primitive class.

## Assumptions and scope

Positions in words are indexed \(0,1,\ldots,n-1\), and rotations are cyclic rotations of positions; reversing words or complementing symbols is not part of the equivalence. A word is *primitive* if it is not a proper integer power of a shorter word. The code may be empty, as it must be at \(n=3\). The theorem concerns fixed Hamming weight three and fixed common blocklength, not arbitrary Hamming weights, minimum Hamming distance, or the weaker ordinary comma-free condition.

Put

\[
h=\lfloor n/3\rfloor,\qquad b=n-h-1.
\]

Define \(\mathcal C_n\) to contain, for every pair of integers

\[
1\le i\le h,\qquad i<j\le b,
\]

the unique length-\(n\) word whose ones occur at positions \(0,i,j\) and whose other positions are zero. This specifies the entire code without optimization or search.

## Proof

**1. Rotation-orbit upper bound.** If \(w\) is a proper power \(t^e\) for an integer \(e\ge2\), its prefix and suffix of length \(|t|\) are both \(t\). It cannot belong to any non-overlapping code. If two distinct codewords are cyclic rotations of one another, write the first as \(xy\) and the second as \(yx\), with both parts nonempty. The suffix \(y\) of the first equals the prefix \(y\) of the second, which is forbidden. Therefore a non-overlapping code contains at most one member of each primitive rotation class.

All \(\binom n3\) binary words of length \(n\) and weight three are primitive except those that repeat a shorter word exactly three times. Indeed, any nontrivial exponent must divide the number of ones, which is three. Such words exist precisely if \(3\mid n\); they are the \(n/3\) distinct cyclic placements of the period consisting of one one and \(n/3-1\) zeros. Each primitive class contains exactly \(n\) distinct words. Hence

\[
M_3(n)\le\frac1n\left(\binom n3-\mathbf1_{\{3\mid n\}}\frac n3\right)
=\left\lfloor\frac{(n-1)(n-2)}6\right\rfloor.
\]

The last identity uses the three residues of \(n\) modulo three. This is the classical orbit upper bound, specialized to weight three; its attainability is established next.

**2. No prefix-suffix matches in the construction.** Every word of \(\mathcal C_n\) begins with one and ends with zero. Consequently a suffix could equal a proper prefix of another codeword only if that suffix begins with one, at the second or third one-position of its word.

For a source word with ones at \(0,i,j\), if the suffix begins at \(i\), its length is \(n-i\ge n-h=b+1\), and it contains exactly two ones. Any prefix of this length in any target codeword contains all three of its ones, because the target's final one is at position at most \(b\). The suffix and prefix therefore cannot agree.

If instead the suffix begins at \(j\), its length is \(n-j\ge n-b=h+1\), and it contains exactly one one. Any prefix of this length in any target codeword contains at least two ones, because the target's second one is at position at most \(h\). Again there is no match. The argument includes the possibility that source and target are the same word. Hence \(\mathcal C_n\) is non-overlapping.

**3. Exact count and optimality.** For each \(i\), there are \(b-i\) choices of \(j\). Therefore

\[
|\mathcal C_n|=\sum_{i=1}^h(b-i)
=hb-\frac{h(h+1)}2.
\]

For \(n=3m\), \(3m+1\), and \(3m+2\), this expression becomes, respectively,

\[
\frac{3m(m-1)}2,\qquad \frac{m(3m-1)}2,\qquad \frac{m(3m+1)}2.
\]

In each case it equals the orbit upper bound above. Hence the asserted formula holds for all \(n\ge3\). Since the code uses the maximum possible number of disjoint primitive rotation classes, it contains precisely one word from every primitive class. The same saturation argument shows that every optimal code does so, whether or not it uses the displayed construction. \(\square\)

## Verification

The standalone file `verify.py` constructs \(\mathcal C_n\), compares every ordered codeword pair at every proper prefix/suffix length, enumerates all primitive weight-three binary rotation classes, and verifies exact transversal equality, for every \(3\le n\le26\). It additionally checks the closed count identity for all \(3\le n\le1000\).

Run `python3 verify.py` using a standard Python installation. The expected terminal line is:

```
VERIFY_OK lengths=3..26 total_weight_three_words=17550 primitive_necklaces=864 codeword_pair_tests=53940 formula_lengths=3..1000
```

All finite checks supplement, rather than replace, the proof covering arbitrary \(n\).

## Relationship to prior work

The primitive-necklace orbit upper bound is not claimed as new. In particular, Proposition 5 of Stanovnik, Moškon and Mraz (arXiv:2410.18458v1) bounds constrained non-overlapping codes by counting primitive cyclic rotation classes. The present contribution is a **sharp all-length fixed-weight-three saturation theorem**, including a simple non-overlap construction that chooses one word from each primitive weight-three class. That saturation does not follow from an orbit upper bound alone. Their paper concentrates on near-half-balanced words and restricted run lengths, rather than stating this sparse exact extremum.

Earlier work develops general maximal constructions, unrestricted code bounds, and variable-length bounds. Fixed-density necklace-generation algorithms list rotation representatives, but being a transversal alone does not ensure prefix-suffix non-overlap. The new extra property is the simultaneous non-overlap of the complete primitive transversal. References below distinguish these threads.

## Limitations

This is not a claim about every fixed weight, nor about decoding under arbitrary corruption. The orbit upper-bound technique is established prior work, and a historically unlocated equivalent specialization or code construction could remain in the large literature on strongly regular, comma-free, mutually uncorrelated, and cross-bifix-free codes. Finite software checks cannot independently establish the infinite theorem; only the displayed combinatorial proof does. No independent scientific validation has been performed.

## References

1. L. Stanovnik, M. Moškon, M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, arXiv:2410.18458v1, 24 October 2024. https://arxiv.org/html/2410.18458v1
2. L. Stanovnik, M. Moškon, M. Mraz, *In search of maximum non-overlapping codes*, *Designs, Codes and Cryptography* 92 (2024), 1299–1326, doi:10.1007/s10623-023-01344-z. https://link.springer.com/article/10.1007/s10623-023-01344-z
3. G. Wang, Q. Wang, *On the maximum size of variable-length non-overlapping codes*, arXiv:2402.18896v1, 29 February 2024. https://arxiv.org/html/2402.18896v1
4. S. Blackburn, *Non-overlapping codes*, arXiv:1303.1026. https://arxiv.org/abs/1303.1026
5. F. Ruskey, J. Sawada, *An efficient algorithm for generating necklaces with fixed density*, *SIAM Journal on Computing* 29 (1999), 671–684, doi:10.1137/S0097539798344112. https://doi.org/10.1137/S0097539798344112
6. Qin, Chen and Luo, *On non-expandable cross-bifix-free codes*, arXiv:2309.08915. https://arxiv.org/abs/2309.08915
