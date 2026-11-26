# Independent mathematical audit

## correctness

PASS

If c,d,e count selected length-three words with one, two, and three distinct ordered shadows, only constants contribute to c and every word counted in c or d hits a diagonal. This is immediate by comparing (a,b), (a,c), (b,c): with three distinct symbols all differ, while a nonconstant word with just two shadows must have an adjacent equal pair. Hence c≤q, c+d≤2q, and 3|C|=I+2c+d≤2q²+3q, yielding the floor bound for q≥2. In each Steiner block each of the two reversal pairs gives every ordered off-diagonal pair once, and the unique unordered-pair incidence prevents clashes across blocks. Replacing abc by aab, bbc, acc preserves ab, bc, ac and adds exactly one incidence to each of aa, bb, cc. Together with the constants, disjointness of the selected blocks makes every list of size at most two. The added words cannot coincide with any other block's added words since a distinct-symbol pair determines their block. The resulting size q+2q(q−1)/3+2m is optimal for m=q/3 if q≡3 mod 6 and m=(q−1)/3 if q≡1 mod 6. The first existence statement is classical Kirkman existence as confirmed in the Kirkman survey. For the latter, even without recovering the full newer citation, Vanstone et al.'s published abstract states Hanani systems exist at q≡1 mod 6 except q=7,13, and each has an almost parallel class by definition; at 13 the two explicit cyclic bases in the frozen checker independently give a Steiner system with four disjoint blocks. At 7 the separately listed 39 words are distinct, cover 47 outputs twice and two once, and attain the floor bound. Replay: python3 /workspace/reproductions/review_01_deletion.py (standard library; builds and checks the finite cases independently of the uploaded checker). CHECK.py and its recorded output were read, not run. Finite witnesses do not prove the infinite design theorem. Equality is not claimed at other q, nor for a different length, deletion budget or list size.

## originality

PASS

Supports the exact attainment theorem for all Steiner-admissible alphabets with q≥3, including q=7. The universal bound is a supporting lemma, not credited separately as priority: a distinct same-day record uses the same expression and states equality at q=4,5,6,8. Its full statement/proof and precedence were not recovered. The imported design existence is credited, not novel.

## value

PASS

The shortest nontrivial ordered-shadow packing at list size two has a natural incidence upper bound whose equality is not guaranteed by counting or unique-decoding results. The design construction resolves two full congruence classes and handles a structural Fano-system exception by an exact witness. The problem naturally tests how directed off-diagonal coverage interacts with repeated symbols and is not an isolated alphabet computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
