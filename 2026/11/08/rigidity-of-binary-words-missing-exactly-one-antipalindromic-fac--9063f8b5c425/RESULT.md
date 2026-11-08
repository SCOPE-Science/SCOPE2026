# Rigidity of binary words missing exactly one antipalindromic factor

## Finding

For a binary word \(w\) of length \(n\), let \(A(w)\) be the number of **distinct nonempty** contiguous factors fixed by reverse-complementation; such factors are called antipalindromes. Define the shortfall \(D(w)=n-1-A(w)\). Write \(e(w)=e_1\cdots e_{n-1}\), where \(e_i=1\) precisely when adjacent letters of \(w\) are equal. For every integer \(n\ge7\), the condition \(D(w)\le1\) is equivalent to \(e(w)\) belonging to the following five families:

1. \(0^{n-1}\) (family A);
2. \(10^{n-2}\) (family B);
3. \(0^{n-2}1\) (family C);
4. \(10^{n-3}1\) when \(n\) is even (family D);
5. either alternating binary word of length \(n-1\), starting with zero or one (family P).

Each edge word determines two binary words, related by complement. The five edge-language families are disjoint for \(n\ge7\). Exactly two words (family A) have \(D(w)=0\); the remaining **eight** for odd \(n\) and **ten** for even \(n\) have \(D(w)=1\). In particular, the number of words with exactly \(n-2\) distinct nonempty antipalindromic factors is \(8\) for odd \(n\ge7\) and \(10\) for even \(n\ge8\).

As an infinite-word corollary, exactly eight one-sided infinite binary words have all sufficiently long prefixes of shortfall at most one: the two words with constant-zero equality-edge sequence, the two with equality edges \(1000\cdots\), and the four with alternating equality-edge sequence. (The same eight words have the bound on **all** prefixes when the shortfall is defined with the convention for length one.)

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Positions are labeled; words are not identified under reversal, bit complement, or rotation. A factor means a contiguous block, not a subsequence, and distinct means identical factors are counted once. An antipalindrome \(u\) satisfies \(u_i=1-u_{|u|+1-i}\) at each position, so has positive even length. Every assertion on finite words has scope \(n\ge7\), including both parities. The infinite-word corollary concerns prefixes, not a new claim of a language-wide defect bound over all factors.

## Proof

**1. One new factor at most.** If \(v\) is antipalindromic, every even-length antipalindromic suffix \(u\) of \(v\) is also a prefix of \(v\). Indeed, the corresponding prefix is the reverse-complement of \(u\), hence equals \(u\). It follows that appending one letter to a word creates either zero or one distinct antipalindromic factor. A factor is created exactly when the longest nonempty antipalindromic suffix of the extended word has not appeared earlier (a nonexistent such suffix creates none). Consequently \(D(w)\) cannot decrease under right extension.

**2. Equality-edge criterion.** For a length-\(2k\) factor, put \(f_j=1\) when its \(j\)-th and \((j+1)\)-st letters are equal. The factor is antipalindromic **if and only if** its edge word \(f_1\cdots f_{2k-1}\) is a palindrome and its central edge \(f_k\) is zero. The forward implication follows by reflection and by the unequal central letters. Conversely the symmetric edge equalities, together with the unequal central pair, propagate outward and imply complementarity of every reflected letter pair. Thus possible new factors after an append are decided by odd palindromic suffixes of the equality-edge word whose middle entry is zero, with uniqueness decided by earlier occurrences of the factor.

**3. Extension table.** The following exhaustive table follows from the preceding edge criterion. A zero or one in the right column is the increment \(A(wb)-A(w)\). Here \(h\in\{0,1\}\) is the newly appended equality edge, so \(h=0\) means the new letter differs from the last letter. The old length is \(n\ge7\).

| Old edge type | New edge \(h\) | New factor? | Retained type if shortfall \(\le1\) |
|---|---|---|---|
| A: all zeros | 0 | 1 | A |
| A: all zeros | 1 | 0 | C |
| B: initial one then zeros | 0 | 1 | B |
| B: initial one then zeros | 1, odd \(n\) | 1 | D |
| B: initial one then zeros | 1, even \(n\) | 0 | none |
| C: terminal one | either | 0 | none |
| D: both boundary ones | either | 0 | none |
| P: alternating edges | opposite final old edge | 1 | P |
| P: alternating edges | same as final old edge | 0 | none |

For completeness, each table entry admits the following explicit edge-string test. For A with \(h=0\), the new all-zero edge string has a longest odd palindromic suffix of length at least \(n-1\), centered at zero, giving a new alternating factor. For B with \(h=0\), the longest odd all-zero suffix has length at least \(n-2\), and the corresponding long alternating factor is new because the word begins with a doubled pair. For B with \(h=1\), the new edge string is \(10^{n-2}1\): it is an odd-length palindrome with zero center exactly when \(n\) is odd. If \(n\) is even, the only odd palindromic suffix is its last edge (whose value is one), so no factor is created. For C, the edge strings after extension end in \(10\) or \(11\) preceded by only zeros; a palindromic odd suffix of length at least three either fails at its first two edges or has a nonzero center. For D, the edge strings after extension end in \(10\) or \(11\) and have just one other one at the first edge; since the new edge-string length \(n\) is even, no positive odd palindromic suffix centered at zero exists except possibly the final zero singleton, whose corresponding factor has occurred previously. For P, continuing the edge alternation provides an odd palindromic suffix centered at zero of length at least \(n-3\); it represents a factor of length at least \(n-2\) starting at one of the last four phase offsets. This factor cannot have appeared before, because the four cyclic phases of the primitive period-four letter word are distinct on every length at least four. Repeating the last edge instead produces an adjacent equal-edge pair at the end; an odd palindromic suffix of length at least three would require the same consecutive equal edges at its beginning, which do not occur in the preceding alternating edge string. The remaining possible length-two factor is already present. These arguments also cover the short boundary lengths \(n=7,8\).

**4. Base and induction.** Direct exhaustive evaluation of all \(2^7=128\) length-seven binary words yields exactly the following words with \(D\le1\): `0010101`, `0011001`, `0101010`, `0101011`, `0110011`, `1001100`, `1010100`, `1010101`, `1100110`, `1101010`. Their equality-edge strings are precisely the asserted types A, B, C and P. Of these, only the two alternating words have \(D=0\). The complete enumerator is supplied in `verify.py`. Now suppose the classification holds at some length \(n\ge7\). By Step 1, every word with \(D\le1\) at length \(n+1\) must extend a listed word of length \(n\). The table shows exactly which extensions preserve \(D\le1\), and that they produce exactly the stated list at length \(n+1\). Every listed type is reached. This proves the classification and the exact counts for all lengths by induction.

**5. Infinite words.** Any infinite word with shortfall at most one on all sufficiently long prefixes must, by monotonicity, satisfy it on every prefix, and therefore pass through a listed state at each length at least seven. From the extension table, a C or D state has no infinite continuation at shortfall at most one. A state can continue indefinitely only with zero edges; leaving it creates a terminal C state. A B state continues indefinitely only with zero edges; a one-edge extension creates a D state or exceeds the allowance. A P state continues indefinitely only through alternating equality edges. This yields exactly \(2+2+4=8\) infinite words and proves the corollary.

## Verification

Run `python3 verify.py`. The script independently implements (i) direct enumeration of distinct antipalindromic factors, (ii) their equality-edge representation, and (iii) the five predicted edge families. It exhaustively checks all length-seven through length-fifteen binary words (a total of \(65{,}408\) words), checks the exact near-rich sets, and checks the extension table on every candidate at lengths seven through eighty-nine. It prints `VERIFY_OK` when every assertion passes. These finite checks validate the base and test the formulas; the induction and explicit edge-suffix reasoning above establish unbounded lengths.

## Relationship to prior work

Guo, Shallit and Shur (2015, Section 5, Theorems 5.2 and 5.3) establish the sharp \(n-1\) bound on distinct nonempty binary antipalindromic factors and show that exactly the two alternating words attain it. Their result establishes the shortfall-zero case, but neither classifies words of shortfall one nor yields the parity-dependent first-stability count by direct statement. Pelantová and Starosta (2011/2013, Sections 2 and 6) develop generalized palindromic richness and \(G\)-defect; for the two-element group generated by binary reverse-complementation, their defect specializes to the same shortfall when both symbols occur. Their general lacuna and defect identities do not enumerate the finite words with defect exactly one, establish the parity-split count, or give the equality-edge classification. The generic one-step monotonicity is therefore treated here as known background, not an original assertion. The present finite classification supplies a new near-extremal stability layer relative to the 2015 theorem.

## Limitations

No classification for shortfalls two or more is claimed. The infinite-word statement applies to a **prefix** bound; it does not transfer unmodified to every factor of each infinite word. Complete priority over uncatalogued equivalent finite-word classifications is not independently guaranteed. All checks of historical novelty are research comparisons, not a uniqueness certificate.

## References

- C. Guo, J. Shallit, A. M. Shur, *On the Combinatorics of Palindromes and Antipalindromes*, arXiv:1503.09112v1 (public March 31, 2015), Section 5, https://arxiv.org/html/1503.09112v1.
- E. Pelantová, Š. Starosta, *Palindromic richness for languages invariant under more symmetries*, arXiv:1108.3042v3 (original public August 15, 2011), Sections 2, 6, https://arxiv.org/html/1108.3042v3.
