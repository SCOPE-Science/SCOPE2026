# The first noninterlaced small-genus semigroup yields an all-level binomid sequence

## Finding
For a numerical semigroup \(S\subseteq\mathbb N_0\) and integer \(q\ge2\), let \(f_n=q\) when \(n\in S\) and \(f_n=1\) otherwise, for positive integers \(n\). For \(0\le k\le n\), define
\[
B_f(n,k)=\frac{\prod_{i=1}^{n}f_i}{(\prod_{i=1}^k f_i)(\prod_{i=1}^{n-k}f_i)}.
\]
Every such \(S\) of genus at most three has **all-level binomidness**: for every width \(m\ge1\), the sequence \(C_m(j)=B_f(m+j-1,m)\), indexed by \(j\ge1\), is binomid. By the row/column equivalence of Shapiro (2023, Proposition 9 and Corollary 10), this is equivalent to integrality of the whole binomid pyramid.

The complete list of gap sets for genus at most three is
\[
\varnothing,\ \{1\},\ \{1,2\},\ \{1,3\},\ \{1,2,3\},\ \{1,2,4\},\ \{1,2,5\},\ \{1,3,5\}.
\]
Of these, exactly \(\{1,2,5\}\) fails closure under adding two, so \(S=\langle3,4\rangle\) is the first case not implied by the published two-interlaced-divisor-chain criterion.

## Assumptions and scope
A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\). Its genus is the number of positive integers absent from it, and its Frobenius number is its largest absent integer (if there is any). The integer \(q\ge2\) is arbitrary; primality is not needed. The theorem is an infinite statement in all column widths and generalized-binomial indices, but restricts the semigroup genus to at most three. A ComboSum sequence satisfies \(\gcd(f_m,f_n)\mid f_{m+n}\), which follows here from the closure of \(S\) under addition.

## Proof
Let \(G(t)=\#\{s\in\mathbb Z_{>0}:s\le t,\ s\notin S\}\), with \(G(0)=0\). Since \(f_i=q\) except at the gaps, the exponent of \(q\) in the formal integer power representing \(B_f(n,k)\) is exactly
\[
E(n,k)=G(k)+G(n-k)-G(n).
\]
In particular the width-\(m\) column has terms \(q^{e_m(j)}\), with zero-based index \(j\ge0\) and
\[
e_m(j)=G(m)+G(j)-G(m+j).\tag{1}\]
It is therefore enough to prove that every interval of \(L\) consecutive values of the integer sequence \(e_m\) has sum at least that of its first \(L\) values, for all \(m,L\ge1\). Indeed, such differences are the exact exponents of \(q\) in the generalized-binomial coefficients of the column.

For every nonempty numerical semigroup of genus \(g\), its Frobenius number satisfies \(F\le2g-1\): among each pair \(i,F-i\), at least one integer is a gap, because otherwise their sum would belong to \(S\). Thus when \(g\le3\), every integer \(n\ge6\) belongs to \(S\). Checking addition closure for the possible memberships among \(1,\ldots,5\) leaves exactly the eight gap sets displayed above. This is a complete 32-mask census, not an assumption about examples.

Set \(c=6\) and \(g=G(c)\). Then \(G(t)=g\) for \(t\ge c\), and \(0\le G(t)\le g\) always. For \(m\ge c\), equation (1) gives \(e_m(j)=G(j)\), a nondecreasing sequence, so its initial length-\(L\) sum is minimal for every \(L\).

For \(1\le m<c\), equation (1) gives \(e_m(j)=G(m)\) whenever \(j\ge c\). Furthermore \(0\le e_m(j)\le G(m)\): the upper bound follows from monotonicity of \(G\), and nonnegativity follows from the ComboSum binomid property, or is checked directly against the eight complete gap lists. Put \(h=G(m)\). If a block starts at \(s\ge c\), every term is \(h\), and it cannot have smaller sum than the initial block. If the length \(L\ge c\) and \(0\le s<c\), the difference between the shifted and initial sums is exactly
\[
\sum_{j=L}^{L+s-1}e_m(j)-\sum_{j=0}^{s-1}e_m(j)=sh-\sum_{j=0}^{s-1}e_m(j)\ge0.
\]
Consequently **all infinitely many required inequalities** reduce to the finite cases \(1\le m\le5\), \(1\le L\le5\), and \(0\le s\le5\). For each of the eight gap sets, calculate \(G(t)\) by counting elements of the explicitly listed set, calculate \(e_m(j)\) from (1), and verify
\[
\sum_{j=0}^{L-1}e_m(j)\le\sum_{j=s}^{s+L-1}e_m(j).
\]
The exhaustive integer-arithmetic checker `verify_small_genus.py` performs this exact finite test, as well as the 32-mask semigroup classification. Its outcome is incorporated as the finite final lemma. The reductions above promote that bounded exhaustive check to all widths, indices and integers \(q\ge2\).

Finally, among the eight lists, only the gap set \(\{1,2,5\}\) permits an integer \(n\in S\) with \(n+2\notin S\), namely \(n=3\). For this semigroup, \(f_3=q\nmid f_5=1\), so the two-interlaced-chain theorem does not apply. It is not an ordinary divisor chain. Nor is it a divisor-product: since \(f_3=f_4=f_{12}=q\), the factors at indices 3 and 4 in any integer divisor-product representation force \(q^2\mid f_{12}\), a contradiction (the proper-divisor factors forced by \(f_1=f_2=1\) are units, and the factor indexed 4 equals \(q\)). A simpler contradiction uses coprime generator indices 3 and 4: divisor-product factors attached to them each must be divisible by \(q\), whereas \(f_{12}=q\).

## Verification
Run `python3 verify_small_genus.py`. It independently enumerates all 32 candidate subsets of the five possible gaps, retains exactly the eight semigroups of genus at most three, checks every one of the finitely reduced interval inequalities, and confirms the unique two-step-hypothesis failure. Assertions are exact integer operations. No finite set of experiments is extrapolated: the preceding proof establishes a rigorous finite reduction and specifies why the finite cases suffice.

## Relationship to prior work
Shapiro (2023) defines the binomid pyramid, proves that all ComboSum sequences are binomid at the initial level, and asks whether they are binomid at every level. The published theorem *Interlaced divisor chains are binomid at every level* gives an infinite sufficient family under \(f_1\mid f_2\) and \(f_n\mid f_{n+2}\). It covers seven of the eight small-genus semigroup indicator families but not \(\langle3,4\rangle\). A separate published result proves a second-level theorem for all ComboSum sequences, which cannot by itself imply every-level integrality. The present contribution is the complete natural first-genus boundary with a new noninterlaced example, not the general ComboSum conjecture.

## Limitations
The statement concerns only genus at most three; it does not assert failure for larger genus, nor characterize all ComboSum sequences. The proof of the finite reduced lemma is executable exact enumeration, and that lemma is small enough to check by hand; neither computational tests at bounded generalized-binomial indices nor unpublished numerical observations are used in lieu of the reduction. Absence of a more general unindexed earlier theorem has not been proved.

## References
1. D. B. Shapiro, *Divisibility Properties for Integer Sequences*, arXiv:2302.02243 (first public February 4, 2023), *INTEGERS* **23** (2023), A57. https://math.colgate.edu/~integers/x57/x57.pdf
2. *Interlaced divisor chains are binomid at every level*, published October 26, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-interlaced-divisor-chains-are-binomid-at-every-level--5781f8464ab9
3. *Every ComboSum sequence is binomid at level two*, published November 8, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-every-combosum-sequence-is-binomid-at-level-two--f731dc6f9e3c
