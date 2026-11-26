# Three-marker circular palindrome richness and its rigid maximizers

## Finding

Let \(w\) be a cyclic binary word of length \(n\ge3\) with precisely three occurrences of \(1\). Define \(P(w)\) to be the number of distinct nonempty palindromes of lengths at most \(n\) occurring in the circular word. Write the three numbers of consecutive zeros between successive ones in nondecreasing order as \(0\le a\le b\le c\), so \(n=a+b+c+3\). Then

\[
P(w)=\begin{cases}
n+\lfloor a/2\rfloor,&a=b=c,\\
n+\lfloor(n-1)/2\rfloor,&\text{exactly two gaps are equal},\\
n+1+a+b,&a<b<c.
\end{cases}
\]

Consequently the exact maximum \(M_3(n)\) over all such cyclic words is

\[
M_3(3)=3,\qquad M_3(n)=n+\lfloor(n-1)/2\rfloor\quad(n=4,5),
\]
\[
M_3(n)=\max\{n+\lfloor(n-1)/2\rfloor,\ \lfloor5n/3\rfloor-2\}\quad(n\ge6).
\]

In particular, for every \(n\ge14\),
\[
M_3(n)=\lfloor5n/3\rfloor-2,
\]
and equality holds **if and only if** the gaps are pairwise distinct and their largest member is \(c=\lceil n/3\rceil\). Up to circular rotation and reflection there are exactly two extremizers when \(n\equiv1\pmod3\), and exactly one otherwise, for all \(n\ge14\).

More explicitly, writing \(n=3q+r\), the sorted optimal gaps for \(n\ge14\) are:

- \(r=0\): \((q-2,q-1,q)\);
- \(r=1\): \((q-3,q,q+1)\) and \((q-2,q-1,q+1)\);
- \(r=2\): \((q-2,q,q+1)\).

For smaller lengths the formula above remains exact and gives all maximizers by evaluating its three cases; in the repeat-gap case, **every** gap triple having exactly two equal entries has the same palindrome count.

## Assumptions and scope

A circular binary word is represented by any rotation of a finite binary string. A factor of length \(\ell\), with \(1\le\ell\le n\), may wrap around the circle but must use at most one full circuit. Different occurrences of the same finite palindrome are counted once. The three cyclic zero gaps are nonnegative; they may be zero, allowing adjacent ones. Reflection permutes the three gaps, as does rotation up to cyclic permutations, so their sorted multiset determines the binary bracelet with exactly three ones. This is an exact **fixed-content** statement, not an assertion about the unrestricted maximum among all binary circles.

## Proof

Every factor of length at most \(n\) contains between zero and three ones. We enumerate **distinct palindrome strings**, not occurrences, in four disjoint categories.

1. **No ones.** The strings \(0^t\), for \(1\le t\le c\), are exactly the zero-only palindromes, contributing \(c\).

2. **One one.** Such a palindrome is \(0^t1 0^t\). Around each one its permissible padding is bounded by the smaller of its two neighboring zero gaps. Among the three one positions, the largest such minimum is the middle gap \(b\). Thus \(t\) ranges exactly from \(0\) through \(b\), contributing \(b+1\).

3. **Two ones.** Such a palindrome must be \(0^t1 0^u1 0^t\), where \(u\) is one of the three cyclic gaps and the two chosen ones are consecutive in cyclic order. The two outer gaps, say \(v\) and \(z\), allow exactly \(0\le t\le\min(v,z)\). The total length condition adds no restriction: \(2\min(v,z)+u+2\le v+z+u+3=n\). If \(a<b<c\), the three distinct inner-gap values contribute \(b+1\), \(a+1\), and \(a+1\), respectively. If \(a=b<c\), the two distinct inner-gap values each contribute \(a+1\). If \(a<b=c\), the two distinct inner-gap values contribute \(b+1\) and \(a+1\). If all three gaps equal, they contribute \(a+1\) in total.

4. **Three ones.** Such a palindrome has form \(0^t1 0^u1 0^u1 0^t\). It exists only when two cyclic gaps coincide, and then its zero padding must satisfy \(2t\le v\), where \(v\) is the remaining gap. When exactly two gaps equal this gives \(\lfloor v/2\rfloor+1\) distinct strings; if all three equal it gives \(\lfloor a/2\rfloor+1\). With three distinct gaps it gives none. The bound \(2t+2u+3\le n\) is equivalent to \(2t\le v\).

Adding these four contributions yields the displayed piecewise expression. For example, when \(a=b<c\), the sum is \(c+(a+1)+2(a+1)+(\lfloor c/2\rfloor+1)=n+\lfloor(n-1)/2\rfloor\). The \(a<b=c\) case gives the same value. When all three gaps equal, the sum is \(3a+\lfloor a/2\rfloor+3=n+\lfloor a/2\rfloor\).

For three distinct gaps, \(P(w)=n+1+a+b=2n-2-c\). Since \(a\le c-2\) and \(b\le c-1\), the constraint \(a+b+c=n-3\) forces \(c\ge\lceil n/3\rceil\). For each \(n\ge6\) this least possible \(c\) is attained by a strictly increasing nonnegative triple: when \(n=3q\) use \((q-2,q-1,q)\); when \(n=3q+1\) use \((q-2,q-1,q+1)\); when \(n=3q+2\) use \((q-2,q,q+1)\). Hence the distinct-gap maximum is \(2n-2-\lceil n/3\rceil=\lfloor5n/3\rfloor-2\). Equal-gap configurations with exactly one equality exist for every \(n\ge4\) and all have value \(n+\lfloor(n-1)/2\rfloor\); the all-equal case is smaller for \(n\ge6\). Directly comparing these expressions proves the maximum formula, including the small cases \(n=3,4,5\).

Finally, for every \(n\ge14\), the distinct-gap expression is strictly larger than the equal-gap expression (check the three residues of \(n\) modulo three). Thus equality requires \(c=\lceil n/3\rceil\) and distinct gaps. Solving \(a+b=n-3-c\) with \(0\le a<b<c\) gives exactly the displayed one or two triples in each residue class. This proves necessity, sufficiency, and the bracelet counts. \(\square\)

## Verification

The standalone file `verify_pal3.py` builds each circle explicitly, tests each possible cyclic starting position and factor length, and counts palindrome strings by direct equality to their reversals. It compares this independently generated set size with the piecewise formula for all \(7140\) ordered zero-gap triples having \(3\le n\le36\), and separately checks the maximum and equality classification at every tested length. Run `python verify_pal3.py`; the expected terminal line is `VERIFY_OK 7140 ordered gap triples (lengths 3..36)`. The proof is symbolic and covers all lengths; the finite replay is a corroborating test, not an infinite certificate.

## Relationship to prior work

Simpson, *Palindromes in circular words* (first publicly available online 22 July 2014), proves a universal upper bound strictly below \(5n/3\) for unrestricted circular words and constructs examples with \(5n/3-2\) distinct palindromes when \(3\mid n\). The numerical existence subcase at multiples of three is therefore not asserted to be new. The finding here is the exact **per-gap formula**, the maximum restricted to exactly three ones for all lengths, and the **complete equality classification and rigidity beyond length thirteen**. OEIS A247000 tabulates the unrestricted maximum through length thirty; a finite table does not yield the present all-length fixed-content identity or its full optimizer characterization. Blondin Massé, Brlek, Garon and Labbé (2011) study palindromic word equations and periodicity rather than this extremal fixed-content count.

## Limitations

No formula for the unrestricted maximum over all binary circles is established. The classification requires exactly three ones, counts only distinct palindromic **contiguous cyclic factors** of length at most the circle length, and does not cover larger alphabets or factors winding more than once. The 2014 primary manuscript's abstract and publication data were accessible, but full-text inspection was blocked; that leaves residual uncertainty concerning possible previously recorded fixed-three-marker specializations or equality observations. Independent historical-priority assessment has not been performed.

## References

1. J. Simpson, *Palindromes in circular words*, Theoretical Computer Science **550** (2014), 66–78. DOI: https://doi.org/10.1016/j.tcs.2014.07.012. First online 2014-07-22; repository record: https://researchportal.murdoch.edu.au/esploro/outputs/journalArticle/Palindromes-in-circular-words/991005543823107891.
2. N. J. A. Sloane et al., OEIS A247000, *Maximal number of palindromes in a circular binary word of length n*, https://oeis.org/A247000, created 2014-09-15.
3. A. Blondin Massé, S. Brlek, A. Garon and S. Labbé, *Equations on palindromes and circular words*, Theoretical Computer Science **412** (2011), 2922–2930. Preprint https://archipel.uqam.ca/8427/1/Blondin-Mass%C3%A9-2011a-preprint.pdf.
