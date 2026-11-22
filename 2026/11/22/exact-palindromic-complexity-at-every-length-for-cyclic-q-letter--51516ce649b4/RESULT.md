# Exact palindromic complexity at every length for cyclic \(q\)-letter period-doubling words

## Finding

For \(q\ge3\), define the infinite word \(u^{(q)}_j=\nu_2(j+1)\bmod q\) for \(j\ge0\). Let \(\operatorname{Pal}_q(n)\) denote the number of **distinct** palindromic factors of length \(n\), counting factors by their actual letter strings rather than their positions. The exact complete complexity is

\[
\operatorname{Pal}_q(n)=\begin{cases}
q&n=1,\\
1&n=2,\\
0&n\ge4\text{ even},\\
q+1+\mathbf 1_{\{k\ge1,\ h<3\cdot2^{k-1}\}}&n=2h+1\ge3,\quad k=\lfloor\log_2h\rfloor.
\end{cases}
\]

Thus at odd lengths at least three, the complexity alternates between \(q+1\) and \(q+2\), with sharp transitions at radii \(2^k\) and \(3\cdot2^{k-1}\). The established binary case is not included in the new claim.

## Assumptions and scope

All indices of the displayed word are zero-based, and \(\nu_2(j)\) is the exponent of two dividing the positive integer \(j\). For the proof below reindex with \(s_j=\nu_2(j)\bmod q\), \(j\ge1\). The factor length \(n\) is any positive integer, and \(q\ge3\) is arbitrary. A length-\(2h+1\) palindrome centered at position \(c>h\) satisfies \(s_{c-t}=s_{c+t}\) for every \(1\le t\le h\).

## Proof

**Valuation comparison.** Write a prospective center as \(c=2^r m\), with \(m\) odd. If \(\nu_2(t)<r\), then \(\nu_2(c-t)=\nu_2(c+t)=\nu_2(t)\). If \(\nu_2(t)>r\), both valuations equal \(r\). The only obstruction occurs when \(t=2^r z\) with \(z\) odd, in which case the two valuations are \(r+\nu_2(m-z)\) and \(r+\nu_2(m+z)\). Since \(m,z\) are odd, one of \(m-z,m+z\) has valuation exactly one and the other has valuation at least two. Modulo \(q\), the two letters match precisely when the latter valuation is congruent to one modulo \(q\). On matching, their common letter is \(r+1\bmod q\).

**Two incompatible equal-valuation offsets.** If the radius contains both \(2^r\) and \(3\cdot2^r\), matching at the first offset forces \(m\equiv1\) or \(-1\pmod8\): the larger valuation must be at least \(q+1\ge4\). For \(z=3\), the valuations of \(m-3,m+3\) are then one and two, in some order, and are unequal modulo \(q\ge3\). Thus no palindrome has \(h\ge3\cdot2^r\).

**Classification at an odd length.** Fix \(h\ge1\), and set \(k=\lfloor\log_2h\rfloor\), so \(2^k\le h<2^{k+1}\). If \(r\ge k+1\), every offset has valuation below \(r\). Consequently the entire palindrome has letters \(\nu_2(t)\bmod q\) at both radius-\(t\) positions, with only the center letter \(r\bmod q\) free. All \(q\) such baseline palindromes occur, by choosing arbitrarily large \(r\) of each residue class. If \(r=k\), only offset \(t=2^k\) is exceptional, giving one further palindrome whose two letters there are \(k+1\bmod q\), distinct from the baseline letter \(k\bmod q\). It occurs by taking \(m=1+2^{q+1}\), for which \(\nu_2(m-1)=q+1\) and \(\nu_2(m+1)=1\). If \(r=k-1\), the radius covers the offset \(2^{k-1}\), and the next equal-valuation offset is \(3\cdot2^{k-1}\). This case therefore occurs exactly when \(k\ge1\) and \(h<3\cdot2^{k-1}\), again realized by \(m=1+2^{q+1}\). Its letters at radius \(2^{k-1}\) differ from the baseline, and its letters at radius \(2^k\) equal \(k-1\bmod q\), distinguishing it from the case \(r=k\). Finally, every \(r\le k-2\) satisfies \(3\cdot2^r\le h\), hence is impossible by the preceding incompatibility. These cases are exhaustive and pairwise distinct, proving the odd formula.

**Even lengths.** Among two consecutive positive integers exactly one is odd (with letter zero); equality of their letters requires the even integer's valuation to be a positive multiple of \(q\). Such adjacent zeros occur, so \(\operatorname{Pal}_q(2)=1\). But if \(s_c=s_{c+1}\) for adjacent positions, their outer neighbours \(s_{c-1},s_{c+2}\) have letters one and zero (in either order), because the other neighbouring even integer is exactly twice an odd integer. Consequently no length-four palindrome exists, and hence no even palindrome of greater length exists. All \(q\) letters appear at single positions \(j=2^r\), proving the length-one case.

## Verification

Run `python3 verify_profiles.py` to enumerate actual palindromic factors across all tested lengths for alphabet sizes \(3\le q\le8\). Run `python3 verify_constructive.py` for explicit centers of arbitrarily large valuation at dyadic boundary radii for \(3\le q\le16\). The captured outputs `verify_profiles.out` and `verify_constructive.out` record the completed checks. The mathematical proof, rather than finite enumeration, establishes the infinite-parameter claim.

## Relationship to prior work

Bognini and Ammar's preprint (first submitted 2025-11-25) studies the same generalized substitution through kernel words and gap factorizations; its Section 3 recalls two structural statements about palindromic factors. Barro, Kaboré and Bognini (2022), Theorems 3.1–3.2, establish morphic palindrome inflation and inverse representation, and explicitly note that `00` is the only even palindrome. Those structural results can be used as a starting point for enumeration, but their inspected statements do not supply the present \(q\)-dependent all-length formula or the sharp valuation-center regime. Damanik (2000) computed the classical binary period-doubling palindrome complexity, which is deliberately excluded from the new contribution. The indexed dyadic reflection-complexity result covers absence of palindromes at dyadic lengths at least four, already a consequence of the even-length observation.

## Limitations

No independent expert audit has been performed. The all-length formula describes distinct contiguous palindromic factors, not the number of occurrences, prefix-palindromic length, or factorization into palindromes. The older structural theorems create a residual risk that a separately unpublished or unindexed derivation already gives the same enumeration. The proof is elementary arithmetic and does not claim a new morphic structural theorem.

## References

1. K. E. Bognini and H. Ammar, *A new factorization of the generalized period-doubling sequences through kernel words and gaps sequences*, arXiv:2511.20881v1, publicly posted 2025-11-25. https://arxiv.org/html/2511.20881v1
2. M. Barro, I. Kaboré and K. E. Bognini, *On the palindromic zl-factorization and c-factorization of the generalized period-doubling sequences*, Australasian Journal of Combinatorics 83(3) (2022), 435–447, Theorems 3.1–3.2. https://ajc.maths.uq.edu.au/pdf/83/ajc_v83_p435.pdf
3. D. Damanik, *Local symmetries in the period-doubling sequence*, Discrete Applied Mathematics 100 (2000), 115–121. https://www.iaorifors.com/paper/33938
4. published-finding corpus, *Exact dyadic factor and reflection complexity of cyclic period-doubling words*. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-dyadic-factor-and-reflection-complexity-of-cyclic-period-d--c8d7b40c0705
