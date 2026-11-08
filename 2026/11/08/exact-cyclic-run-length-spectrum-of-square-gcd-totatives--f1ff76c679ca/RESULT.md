# Exact cyclic run-length spectrum of square-gcd totatives

## Finding

For every integer \(n\ge 2\), let
\[
A_n=\{x\bmod n:\gcd(x,n)\text{ is a perfect square}\}.
\]
For each integer \(r\ge1\), let \(W_n(r)\) be the number of starting residues \(x\bmod n\) such that all of \(x,x+1,\ldots,x+r-1\) belong to \(A_n\). These are cyclic intervals, with integer shifts reduced modulo \(n\).

Write \(n=\prod_{p^a\parallel n}p^a\). Define the standard alternating divisor function at prime powers by
\[
B_p(t)=\frac{p^{t+1}+(-1)^t}{p+1}\qquad(t\ge0).
\]
Then for all \(r\ge1\),
\[
\boxed{W_n(r)=\prod_{p^a\parallel n} L_{p,a}(r)},
\]
where for \(a=1\),
\[
L_{p,1}(r)=\max\{p-r,0\},
\]
and, for \(a\ge2\),
\[
\boxed{
L_{p,a}(r)=
\begin{cases}
(p-r)p^{a-1}+rB_p(a-2),&1\le r\le p,\\
(2p-r)B_p(a-2),&p<r\le2p,\\
0,&r>2p.
\end{cases}}
\]

The longest cyclic run of square-gcd totatives has exact length
\[
\boxed{\mathcal L(n)=\min_{p^a\parallel n}
\begin{cases}p-1,&a=1,\\2p-1,&a\ge2.\end{cases}}
\]
There are exactly \(W_n(\mathcal L(n))\) starting positions for a longest run. More generally, the **complete maximal-run length distribution** is
\[
\boxed{M_n(r)=W_n(r)-2W_n(r+1)+W_n(r+2)},
\]
where \(M_n(r)\) counts the maximal cyclic runs of exactly \(r\) consecutive members of \(A_n\). The displayed formulas determine \(M_n(r)\) for every \(n\ge2\) and every \(r\ge1\).

As a consistency check, \(W_n(1)=\beta(n)\), the alternating sum-of-divisors function. Thus this one theorem refines the established one-point count to every consecutive block length, determines the extremal length, and determines all actual run multiplicities.

## Assumptions and scope

A perfect square means the square of a nonnegative integer, including \(1\), and \(\gcd(0,n)=n\). The positive modulus satisfies \(n\ge2\); runs are counted as cyclic intervals of residues modulo \(n\), not as subsets of \(\mathbb Z\) with a fixed endpoint. The starting positions are distinct residues; \(r\) may exceed \(n\), in which case the formulas give zero. Prime powers are indexed by \(p\) prime and \(a\ge1\). The function \(B_p(0)=1\) is part of the definition.

The assertion does not count runs among integers subject to an unrelated varying modulus, nor intervals on nonconsecutive arithmetic progressions.

## Proof

**1. The square-gcd residue set at a prime power.** For \(a\ge1\) and \(x\bmod p^a\), the gcd \(\gcd(x,p^a)\) is a square precisely when its exponent \(\min\{v_p(x),a\}\) is even. This includes the zero residue only when \(a\) is even. Let \(A_{p^a}\) be the corresponding local set. Every unit modulo \(p^a\) belongs to \(A_{p^a}\). A nonunit belongs if and only if it is divisible by \(p^2\) and the residue \(x/p^2\bmod p^{a-2}\) belongs to \(A_{p^{a-2}}\), for \(a\ge2\). For \(a=2\), \(A_{p^0}\) means the unique class modulo \(1\), which is admissible.

Writing \(b_a=|A_{p^a}|\), we obtain \(b_0=1\), \(b_1=p-1\), and
\[
b_a=(p-1)p^{a-1}+b_{a-2}\quad(a\ge2).
\]
The displayed closed form \(b_a=B_p(a)\) follows by induction; in particular \(B_p(a-2)\) counts exactly the admissible residues divisible by \(p^2\) modulo \(p^a\). The formula for \(\beta(p^a)\) follows from the same recurrence, independently of any asymptotic approximation.

**2. Local intervals of length at most \(p\).** Fix \(1\le r\le p\). Among the \(p\) possible starting classes modulo \(p\), exactly \(p-r\) produce no multiple of \(p\) in the \(r\)-term interval. Each such starting class has \(p^{a-1}\) lifts modulo \(p^a\), all admissible. The other \(r\) starting classes place exactly one multiple of \(p\) in the interval. When \(a=1\), this term is inadmissible. When \(a\ge2\), it is admissible in exactly \(B_p(a-2)\) lifts; all the other terms in that interval are units. These observations give \(L_{p,1}(r)=p-r\) and
\[
L_{p,a}(r)=(p-r)p^{a-1}+rB_p(a-2)\qquad(a\ge2).
\]

**3. Longer local intervals and the sharp obstruction.** Every sequence of \(2p\) consecutive integers contains at least two multiples of \(p\) differing by exactly \(p\). They cannot both be divisible by \(p^2\); at least one has \(p\)-adic valuation exactly \(1\), so it is inadmissible modulo every \(p^a\). Hence local runs have length at most \(2p-1\) when \(a\ge2\), and at most \(p-1\) when \(a=1\).

For \(p<r\le2p\), exactly \(2p-r\) of the \(p\) starting classes modulo \(p\) place only one multiple of \(p\) in the interval. The other \(r-p\) starting classes place two multiples differing by \(p\), so give zero admissible lifts. For each of the \(2p-r\) permissible starting classes the unique multiple must be in \(p^2A_{p^{a-2}}\), giving precisely \(B_p(a-2)\) lifts. This proves the second and third branches for \(a\ge2\). For \(a=1\), every interval of length \(r\ge p\) contains a forbidden multiple of \(p\).

At \(r=p-1\) for \(a=1\), the local count is \(1>0\); at \(r=2p-1\) for \(a\ge2\), the local count is \(B_p(a-2)>0\). Therefore both local upper bounds are attained.

**4. Chinese remainders and the longest run.** The condition \(\gcd(x+j,n)\) square for all \(0\le j<r\) holds if and only if it holds independently modulo each \(p^a\parallel n\). The Chinese remainder theorem gives a bijection between starting residues modulo \(n\) and tuples of local starting residues. The count is therefore the product \(W_n(r)=\prod L_{p,a}(r)\), with no independence assumption. Since each local factor is positive exactly for \(r\) at most its stated maximum, the longest global run has the displayed minimum length. The product at this length counts all longest-run starting positions.

**5. Recovering every maximal run.** Because \(n\ge2\), the local bounds imply \(\mathcal L(n)<n\), so the cyclic binary sequence \(1_{A_n}\) has at least one zero. Decompose its ones uniquely into maximal cyclic runs. A maximal run of length \(s\) contributes \(s-r+1\) starting positions to \(W_n(r)\) when \(s\ge r\), and zero otherwise. Hence
\[
W_n(r)=\sum_{s\ge r}(s-r+1)M_n(s).
\]
Taking two consecutive finite differences yields \(M_n(r)=W_n(r)-2W_n(r+1)+W_n(r+2)\). At the maximal length, \(W_n(\mathcal L(n)+1)=0\), so the number of maximal-length runs equals \(W_n(\mathcal L(n))\), finishing the proof.

## Verification

Run \(\texttt{python3 verify\_square\_gcd\_runs.py}\) with standard-library Python. The self-contained script derives the local product from integer factorization, independently computes \(A_n\) by integer gcd and exact integer square roots, and compares all cyclic window counts for \(2\le n\le900\) at the tested window lengths. It independently enumerates maximal runs and checks their exact multiplicities and the sharp maximal length. The successful replay reports \(899\) moduli, \(16077\) window checks, and \(65343\) run-multiplicity checks. These finite comparisons support the proof but do not certify the unrestricted quantifiers. The unrestricted part is Steps 1–5 above.

Examples: for \(n=9\), the maximal runs have lengths \(2\) and \(5\), one of each. For \(n=25\), there are three maximal runs of length \(4\) and one of length \(9\). For \(n=72\), there are \(18\) maximal runs of length \(1\), four of length \(2\), and three of length \(3\); the weighted total \(18+8+9=35\) equals \(\beta(72)\).

## Relationship to prior work

Tóth's survey establishes the square-gcd interpretation of the alternating divisor function \(\beta(n)\), and the one-point prime-power count \(\beta(p^a)\). The present theorem retains that existing result as its \(r=1\) boundary, but determines the joint counts for every consecutive interval length \(r\), the complete maximal-run distribution, and the sharp longest length. None of those follows from the one-point count alone: subsets of the same cardinality can have different cyclic run spectra.

The classical Schemmel totient counts consecutive blocks consisting **only of units**. For a squarefree modulus the current count reduces exactly to Schemmel's familiar local rule; **that special case is prior work**, not new. Pabhapote and Laohakosol (2010), Section 2, discuss Schemmel's totient, Lucas's totient, and Nageswara Rao's consecutive \(s\)-coprime totient as specializations of a generalized Euler totient. The accessible publisher HTML, especially Section 2, was inspected. Their listed counting conditions do not include the square-gcd condition with arbitrary *even* prime valuations. The distinction is substantive already at \(n=9,r=2\): the standard Schemmel count is \(3\), whereas \(W_9(2)=5\), because exactly two further starts are allowed through a term divisible by \(9\). The new content is the exact exponent-dependent correction, the two-prime-spaced obstruction, and the complete run spectrum for arbitrary moduli, not the pre-existing squarefree/units case.

OEIS A206369 records the same one-point arithmetic function and its gcd-square interpretation, not an all-length interval or run-multiplicity law. Costello and Watts (2012) study Jacobsthal's function and a generalized totient in the separate setting of consecutive integers coprime to a product of primes; that problem also involves unit residues, unlike the permitted even valuations here. No identity of these counting conditions is assumed. The related \(s\)-prime condition forbids prime powers above a fixed threshold, whereas square-gcd admissibility alternates with prime-power valuation.

## Limitations

The proof gives a finite-modulus, exact arithmetic classification, not an asymptotic statement for varying moduli. The historical-originality comparison is provisional: an equivalent run-count formula might exist under different terminology, and full text of the Costello–Watts paper was not accessible during the comparison. No expert or independent audit has been performed. The Python test is finite, not a substitute for the general proof.

## References

1. László Tóth, *A survey of the alternating sum-of-divisors function*, arXiv:1111.4842, first publicly submitted 2011-11-21, https://arxiv.org/abs/1111.4842 ; relevant definitions and square-gcd interpretation in Sections 1–3.
2. OEIS Foundation, A206369, alternating sum-of-divisors / square-gcd totient, https://oeis.org/A206369 ; relevant formula and comments.
3. Nittiya Pabhapote and Vichian Laohakosol, *Combinatorial Aspects of the Generalized Euler’s Totient*, International Journal of Mathematics and Mathematical Sciences 2010, article 648165, first published 2010-09-14, https://doi.org/10.1155/2010/648165 ; accessible HTML inspected, especially Section 2 on Schemmel and related totients.
4. Fintan Costello and Paul Watts, *Jacobsthal's function and a generalisation of Euler's totient*, arXiv:1209.3464, first publicly submitted 2012-09-16, https://arxiv.org/abs/1209.3464 ; abstract inspected, full text not obtained.
