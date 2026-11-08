# The exact least modulus for a twice-each ternary multiset sum

## Finding
For every integer \(n\ge2\), let
\[
A_n=\{3^i-1:0\le i<n\},\qquad S_n=3^n-1.
\]
Call a positive modulus \(N\ge2\) *twice-each valid* if the only nonnegative integer vector \((k_0,\ldots,k_{n-1})\) satisfying
\[
\sum_{i=0}^{n-1}k_i=2n,\qquad
\sum_{i=0}^{n-1}k_i(3^i-1)\equiv 2\sum_{i=0}^{n-1}(3^i-1)\pmod N
\]
is \((2,\ldots,2)\).

Let \(t(n)\) be the largest nonnegative integer satisfying
\[
3^{t(n)}\le 2n-1,\qquad n-t(n)\equiv1\pmod2.
\]
(The set of such integers is nonempty for every \(n\ge2\).) Then the least twice-each valid modulus is exactly
\[
\boxed{N_{\mathrm{twice}}(n)=\frac{3^n-3^{t(n)}}2.}
\]
Its first seven values, for \(n=2,\ldots,8\), are \(3,13,39,117,363,1089,3279\). In particular \(N_{\mathrm{twice}}(n)=3^n/2+O(n)\), with the precise error given by the displayed formula.

## Assumptions and scope
All integers are ordinary integers. Multisets may repeat elements; a length-\(2n\) multiset supported on \(A_n\) is encoded by a nonnegative multiplicity vector of total \(2n\). The distinguished multiset has multiplicity two at *every* position; this is not the all-ones length-\(n\) problem. The theorem minimizes the modulus for this *fixed* ternary exponent family, not over all possible residue sets. The formulation with exponents \(3^i-1\) is equivalent to the one with \(3^i\), because all vectors being compared have equal total multiplicity.

For a nonnegative integer \(u\), let \(s_3(u)\) denote the sum of its base-three digits (\(s_3(0)=0\)). A difference from the distinguished power sum is
\[
V=\sum_{i=0}^{n-1}k_i3^i-S_n,
\quad k_i\ge0,\quad\sum k_i=2n.
\]
It is always even. The theorem asserts that the only such vector with \(N\mid V\) is the distinguished vector when \(N=N_{\mathrm{twice}}(n)\), and that a non-distinguished vector exists for every smaller positive modulus \(N\ge2\).

## Proof
**Ternary coin-count lemma.** When the coin denominations are \(1,3,\ldots,3^{n-1}\), the smallest number of coins representing any \(M\ge0\) is
\[
\gamma_n(M)=\left\lfloor\frac{M}{3^{n-1}}\right\rfloor
  +s_3(M\bmod 3^{n-1}).
\]
All achievable coin counts are precisely \(\gamma_n(M),\gamma_n(M)+2,\ldots,M\), with the last endpoint included because the quantities have the same parity. Indeed, carrying three lower coins to one upper coin decreases the count by two, and iterated carries give the unique greedy representation. Conversely, splitting any nonunit coin into three coins one denomination lower increases the count by two; until there are \(M\) coins, some nonunit coin remains. Thus an integer \(M\) has a representation by exactly \(2n\) coins if and only if
\[
M\ge2n,\qquad \gamma_n(M)\le2n,\qquad M\equiv0\pmod2.
\tag{1}
\]
If \(0\le M<3^n\), then \(\gamma_n(M)=s_3(M)\le2n\). Also, for \(a\ge0\) and \(0\le u<3^n\), one has
\[
\gamma_n(a3^n+u)=3a+s_3(u),\qquad
s_3(3^n-1-u)=2n-s_3(u).
\tag{2}
\]
In particular \(\gamma_n(S_n)=2n\), and the greedy representation of \(S_n\) is uniquely the distinguished all-twos vector; so \(V=0\) cannot arise from a rival.

Write \(d=3^{t(n)}\), \(N_*=(3^n-d)/2\), and \(L=2n\). The parity condition on \(t(n)\) makes \(N_*\) odd. Since \(d\le L-1\), every *negative* multiple of \(N_*\) which is also an even difference must be at most \(-2N_*\); it would correspond to
\[
M=S_n+V\le S_n-2N_*=d-1<L,
\]
contradicting (1).

For a *positive* multiple, the evenness of \(V\) and oddness of \(N_*\) require \(V=h(2N_*)=h(3^n-d)\) for an integer \(h\ge1\). Since \(\sum k_i=L\), the maximal possible difference is
\[
V_{\max}=L3^{n-1}-S_n=(2n-3)3^{n-1}+1.
\]
The elementary inequalities \(3^n-d>3^{n-1}\) and \((2n-3)(2n-1)<3^n\) for \(n\ge2\) give \(h\le2n-3\) and hence \(hd<3^n\). Therefore, by (2), the required target \(M=S_n+h(3^n-d)\) has
\[
\gamma_n(M)=3h+2n-s_3(hd)=2n+3h-s_3(h)>2n,
\]
because \(d\) is a power of three and \(s_3(h)\le h\). This contradicts (1). Consequently \(N_*\) is twice-each valid.

We show minimality. The inequality \(3^n-1\ge4n\) for \(n\ge2\) implies \(N_*\le S_n-L\). If \(2\le N<N_*\) is even, choose \(V=-N\): its target \(M=S_n-N\) is even, satisfies \(L\le M<S_n\), and has \(\gamma_n(M)\le L\) by (2); thus (1) constructs a rival. If \(N\) is odd and \(2N\le S_n-L\), the same argument with \(V=-2N\) constructs a rival.

It remains to treat odd \(N<N_*\) with \(2N>S_n-L\). Put \(d'=3^n-2N\). Then
\[
d<d'\le 2n-1,\qquad d'\text{ odd},\qquad
 d'\equiv3^n-2\pmod4.
\]
An odd nonnegative integer has ternary digit sum less than three precisely when it is a power of three: digit sum two forces an even integer. If \(d'\) were a power \(3^u\), the displayed congruence would force \(u\) to have parity opposite to \(n\), contradicting maximality of \(t(n)\). Therefore \(s_3(d')\ge3\). The positive difference \(V=2N=3^n-d'\) has target \(M=S_n+V\), which is even and at least \(L\), while (2) yields
\[
\gamma_n(M)=3+s_3(3^n-1-d')=3+2n-s_3(d')\le2n.
\]
By (1) it has a length-\(2n\) coin representation. Because \(V\ne0\), this representation is a rival. Hence every smaller modulus is invalid, proving the exact formula. \(\square\)

## Verification
The standalone program `verify_ternary_twice.py` independently constructs the complete set of difference values via (a) direct enumeration of weak compositions and (b) a coin-count dynamic program. For every \(n=2,\ldots,8\), both agree and direct divisibility testing of **every** modulus below the stated minimum confirms the exact minimum. Further exact checks validate the formula's parameter inequalities for \(2\le n\le1000\). The program uses Python's arbitrary-precision integers and requires only its standard library. Run `python3 verify_ternary_twice.py`.

These finite checks do not prove the unrestricted theorem: the proof above does. The two implementations cross-check the finite instances, not the literature-priority assessment.

## Relationship to prior work
Fonollosa's *Minimum modulus for the unique multiset-sum problem* (arXiv:2607.08366, first public July 9, 2026) determines the least modulus for the **binary** exponents \(2^i-1\) and the length-\(n\) **all-ones** target. Its Section 8 explicitly raises weighted/rectangular variants, but the theorem and its coin lemma do not cover the present length-\(2n\), ternary-exponent problem. The present argument uses a ternary analogue of the greedy coin-count idea, with a parity-sensitive optimal power of three. The related finite-abelian-group result of Inal (2026) and the author's accompanying formalization concern the original all-ones target over varying groups, not this fixed ternary twice-each target. The theorem does not claim optimality among arbitrary sets or arbitrary finite groups.

## Limitations
Only the fixed family \(A_n\), the uniform twice-each target and the least positive modulus are classified. No formula is asserted for other radices, nonuniform multiplicities, or other cyclic exponent families. Prior-literature comparisons reduce but cannot eliminate the risk of an unindexed equivalent theorem.

## References
1. J. A. R. Fonollosa, *Minimum modulus for the unique multiset-sum problem*, arXiv:2607.08366 (first posted 2026-07-09), https://arxiv.org/abs/2607.08366 ; especially Sections 2–6 and 8.
2. J. A. R. Fonollosa, *Ryser, Glynn, and the discrete Fourier transform: orthogonal schemes for the permanent*, arXiv:2607.09949 (2026), https://arxiv.org/abs/2607.09949 ; companion work on the application motivating modular uniqueness.
3. M. Inal, *The Exact Minimum Order for Unique Multiset Sums in Finite Abelian Groups* (2026), cited in Fonollosa's formalization overview at https://github.com/jarfo/min-modulus ; addresses the original all-ones group-order problem.
