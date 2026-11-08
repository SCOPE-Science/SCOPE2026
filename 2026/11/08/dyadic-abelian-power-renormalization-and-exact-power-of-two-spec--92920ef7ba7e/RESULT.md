# Dyadic Abelian-power renormalization and exact power-of-two spectra in generalized period-doubling words

## Finding

Let \(m\ge 2\) and let \(x_m\) be the fixed point starting in \(0\) of the substitution
\[\sigma_m(a)=0\,(a+1\bmod m),\qquad a\in\{0,\ldots,m-1\}.\]
Let \(\Psi(w)\in\mathbb N^m\) denote the Parikh vector of a finite word, and let \(R\) cyclically permute coordinates according to \(a\mapsto a+1\pmod m\). For \(k\ge0\), let \(L=2^k\) and \(C_{m,k}=\Psi(x_m[0,L-1))\), where the interval is half-open. Then, for every \(i\ge0\) and \(d\ge1\),
\[
\boxed{\Psi(x_m[i,i+dL))=dC_{m,k}+R^k\Psi(x_m[\lfloor i/L\rfloor,\lfloor i/L\rfloor+d)).}\tag{1}
\]

For integers \(h\ge2\), \(d\ge1\), write \(A_{m,h}(d)\subseteq\mathbb N\) for the starting positions of Abelian \(h\)-powers of period \(d\): these are positions where the \(h\) successive length-\(d\) blocks have identical Parikh vectors. Then
\[
\boxed{A_{m,h}(2^kd)=\bigcup_{q\in A_{m,h}(d)}\{2^kq,\ldots,2^k(q+1)-1\}.}\tag{2}
\]
In particular, all Abelian-power occurrence questions reduce without loss from an arbitrary period to its odd part.

For every \(k\ge0\), every \(m\ge2\), and every start \(i\ge0\), put \(q=\lfloor i/2^k\rfloor\) and \(a=\lfloor q/2\rfloor\). The following *complete* classification holds at period \(2^k\):

- Abelian squares occur at \(i\) exactly when \(v_2(a+1)\equiv m-1\pmod m\).
- Abelian cubes occur at \(i\) exactly when that congruence holds and \(q\) is even.
- No Abelian \(h\)-power occurs at \(i\) for \(h\ge4\).

These sets have natural starting-position densities, independent of \(k\):
\[
\boxed{\delta(A_{m,2}(2^k))=\frac{1}{2^m-1},\qquad
\delta(A_{m,3}(2^k))=\frac{1}{2(2^m-1)},\qquad
\delta(A_{m,h}(2^k))=0\ (h\ge4).}\tag{3}
\]
Furthermore, the *entire* empirical Parikh-vector distribution at length \(2^kd\) is a translated coordinate permutation of the distribution at length \(d\). Every such distribution exists. In particular, every length \(2^k\) has exactly \(m\) Parikh vectors: the vector \(C_{m,k}+e_{a+k\bmod m}\) occurs with density
\[
\boxed{\nu_m(a)=\frac{2^{m-a-1}}{2^m-1}\qquad(0\le a<m).}\tag{4}
\]

## Assumptions and scope

All positions start at zero, all word intervals are half-open, \(v_2(t)\) is the exponent of \(2\) dividing a positive integer \(t\), and every congruence of alphabet letters is modulo \(m\). An Abelian power requires equality of all letter counts, not literal equality of the blocks. A natural density means \(\lim_{N\to\infty}N^{-1}|A\cap\{0,\ldots,N-1\}|\), when it exists. All quantified parameters are finite integers in the specified ranges; no assumption of an upper bound on \(m,k,d,h\) is made. Formula (3) concerns periods that are powers of two, not all periods.

## Proof

**1. Digit-valuation representation.** The recurrence for the fixed point is \(x_m(2j)=0\), \(x_m(2j+1)=x_m(j)+1\pmod m\). With \(x_m(0)=0\), induction on \(j\) yields the exact formula
\[x_m(j)=v_2(j+1)\bmod m.\tag{5}\]
Indeed, the valuation is zero when \(j\) is even and equals \(1+v_2((j+1)/2)\) when \(j\) is odd.

**2. A common-prefix substitution lemma.** For each \(k\ge0\) there is a word \(U_{m,k}\) of length \(2^k-1\), independent of the input letter, with
\[\sigma_m^k(a)=U_{m,k}\,(a+k\bmod m).\tag{6}\]
For \(k=0\), take the empty word. If (6) holds at \(k\), the identity \(\sigma_m^{k+1}(a)=\sigma_m^k(0)\sigma_m^k(a+1)\) gives the recursion
\[U_{m,k+1}=U_{m,k}\,(k\bmod m)\,U_{m,k},\tag{7}\]
with final letter \(a+k+1\bmod m\). Since \(x_m\) begins with \(\sigma_m^k(0)\), the common word \(U_{m,k}\) equals \(x_m[0,2^k-1)\) and its Parikh vector is \(C_{m,k}\).

**3. Arbitrarily misaligned windows.** Partition the fixed point into consecutive length-\(L\) substitution blocks \(\sigma_m^k(x_m(q))\). Put \(i=qL+r\), \(0\le r<L\). The interval \([i,i+dL)\) consists of (i) the suffix of the block at \(q\), (ii) \(d-1\) complete intervening blocks, and (iii) the length-\(r\) prefix of block \(q+d\). By (6), the first and final pieces together contribute exactly the multiset of letters in \(U_{m,k}\) plus the final letter \(x_m(q)+k\). Each intervening complete block contributes its own copy of \(U_{m,k}\) and the rotated final letter \(x_m(j)+k\). This proves (1) for every residue \(r\), including \(r=0\) and \(k=0\).

**4. Abelian-power occurrence sets.** Apply (1) to the \(h\) consecutive blocks starting at \(i+jdL\), for \(0\le j<h\). Their common additive term is \(dC_{m,k}\), and the other Parikh vectors are the images under the *same invertible permutation* \(R^k\) of the length-\(d\) blocks starting at \(q+jd\), where \(q=\lfloor i/L\rfloor\). Equality of the first list is therefore equivalent to equality of the second, proving (2). Repeatedly remove factors \(2\) from \(d\) to obtain the reduction to odd periods.

**5. Complete unit-period classification.** Set \(y_m(a)=(1+v_2(a+1))\bmod m\). From (5), \(x_m(2a)=0\) and \(x_m(2a+1)=y_m(a)\). Thus two successive letters starting at either \(2a\) or \(2a+1\) are equal exactly when \(y_m(a)=0\), which is \(v_2(a+1)\equiv m-1\pmod m\). Three successive letters starting at \(2a\) are equal under the same condition; three starting at \(2a+1\) would require both \(y_m(a)=y_m(a+1)=0\). This is impossible: \(y_m(a)=0\) forces \(v_2(a+1)\ge1\), so \(a+1\) is even, \(a+2\) is odd and \(y_m(a+1)=1\ne0\) because \(m\ge2\). The same argument rules out four consecutive equal letters at either parity of start. Equation (2) lifts the exact classification to all periods \(2^k\), with no exception.

**6. Exact natural densities and vector frequencies.** The integers \(a\ge0\) satisfying \(v_2(a+1)=r\) have natural density \(2^{-r-1}\). The condition \(v_2(a+1)\equiv m-1\pmod m\) therefore has density
\[\sum_{j\ge0}2^{-(m+jm)}=\frac{1}{2^m-1}.\tag{8}\]
Each such \(a\) corresponds to both starts \(q=2a,2a+1\) of a unit-period square and to just \(q=2a\) for a cube. The inverse image under \(i\mapsto\lfloor i/2^k\rfloor\) consists of fixed-size consecutive blocks and preserves natural density. This proves (3).

For completeness, every finite-factor frequency exists. Fix any factor length \(d\), and replace \(x_m(j)\) by a \(2^H\)-periodic approximation that agrees with (5) except at \(j+1\equiv0\pmod{2^H}\). The discrepancy in length-\(d\) factors affects at most \(d\) starting residues per \(2^H\)-period. Therefore the periodic factor-frequency approximants form a Cauchy family with tail discrepancy bounded by a constant times \(d2^{-H}\), so all factor and Parikh frequencies exist. Formula (1) shows that the length-\(d2^k\) Parikh frequencies are obtained by applying the affine bijection \(v\mapsto dC_{m,k}+R^kv\) to those at length \(d\). At \(d=1\), \(x_m(j)=a\) if and only if \(v_2(j+1)\equiv a\pmod m\), whose exact density is \(\nu_m(a)=\sum_{r\ge0}2^{-(a+rm+1)}=2^{m-a-1}/(2^m-1)\). Every letter occurs, so all \(m\) resulting vectors are distinct. This proves (4) and the final distribution claim.

## Verification

The complete standalone checker \(\texttt{verify.py}\) implements (5) independently of substitution expansion, checks the substitution against \(\sigma_m\), and then evaluates both sides of (1) and the complete square/cube/higher-power classifications for \(2\le m\le9\), \(0\le k\le6\), \(1\le d\le10\), and hundreds of starts. It checks rational dyadic approximations to the geometric-density formula and returns `VERIFY_OK moduli=8 shifts=7 checks=318792` on success. All tests use exact integer or rational arithmetic. Their finite ranges are tests only; the proof above establishes the unbounded quantifiers.

## Relationship to prior work

Barro, Kaboré and Bognini (2022) define and analyze exactly the same generalized period-doubling substitutions, investigating palindromes and palindromic Ziv–Lempel/Crochemore factorizations. In particular, the previously documented absence of four consecutive zeros is consistent with, but does not imply, an Abelian-fourth-power exclusion for arbitrarily large dyadic periods. Their article does not give Parikh-renormalization identities, Abelian-power start sets, or the corresponding natural densities.

Parreau, Rigo, Rowland and Vandomme (2015) prove regularity and recurrences for the *number of Abelian-equivalence classes* in the binary period-doubling sequence. Such scalar class counts do not determine which starting positions carry an Abelian power, the exact densities of these positions, or the all-alphabet blockwise equivalence (2). The present result credits existing Abelian-complexity information rather than treating every scalar consequence of (1) as independently new.

Currie (2023) studies avoidance of ordinary repetitions in the binary period-doubling word. Machacek (2025) studies generalized powers and group-action factor complexity primarily for the ternary squarefree Thue–Morse word, with an indirect binary period-doubling Abelian-complexity relation. Neither inspected argument yields (2) or (3) for the generalized period-doubling family. Rigo, Stipulanti and Whiteland (2024) analyze fixed points of *Parikh-collinear* substitutions, whereas the incidence matrix of \(\sigma_m\) has rank greater than one (indeed it is the sum of a rank-one all-zero-letter contribution and a cyclic permutation), so that theorem does not subsume this family.

## Limitations

The exact absence of Abelian fourth powers is restricted to **dyadic periods**. No claim is made for all possible periods, nor for maximal exponent at an arbitrary odd period. The complete class-frequency law for general base period \(d\) is a reduction statement, not a closed formula for every such \(d\). The result has not received independent mathematical validation; the reproducible finite checks support, but do not replace, the proof. An unindexed equivalent or stronger result in other literature cannot be ruled out solely by search.

## References

1. M. Barro, I. Kaboré and K. E. Bognini, *On the palindromic zl-factorization and c-factorization of the generalized period-doubling sequences*, Australasian Journal of Combinatorics **83** (2022), 435–447. Public text: https://ajc.maths.uq.edu.au/pdf/83/ajc_v83_p435.pdf . Public date July 20, 2022: https://portal.mardi4nfdi.de/wiki/On_the_palindromic_zl-factorization_and_c-factorization_of_the_generalized_period-doubling_sequences .
2. A. Parreau, M. Rigo, E. Rowland and É. Vandomme, *A New Approach to the 2-Regularity of the \(\ell\)-Abelian Complexity of 2-Automatic Sequences*, Electronic Journal of Combinatorics **22** (2015), #P1.27. https://arxiv.org/abs/1405.3532 .
3. J. D. Currie, *The analogue of overlap-freeness for the period-doubling sequence*, arXiv:2303.14539 (2023). https://arxiv.org/abs/2303.14539 .
4. M. Rigo, M. Stipulanti and M. A. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, Theory of Computing Systems **68** (2024), 1622–1639. https://doi.org/10.1007/s00224-024-10197-5 .
5. J. Machacek, *Group Actions and Some Combinatorics on Words with \(\mathbf{vtm}\)*, arXiv:2509.26613 (2025). https://arxiv.org/abs/2509.26613 .
