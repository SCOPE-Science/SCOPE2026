# Review of dyadic Abelian-power renormalization

## Correctness — PASS

The digit-valuation identity \(x_m(j)=v_2(j+1)\bmod m\) follows directly from the fixed-point recursion. The uniform substitution has the proved block form \(\sigma_m^k(a)=U_{m,k}(a+k\bmod m)\), with the same length-\(2^k-1\) word in every block. For an arbitrarily offset length-\(d2^k\) window, the first suffix and final prefix recover one complete common-prefix multiset. This is the critical step establishing the exact Parikh identity without an alignment assumption. Comparing shifted blocks applies a common invertible cyclic letter permutation, proving the full occurrence-set identity. At base period one, the valuation formula determines squares, cubes and absence of fourth powers. Geometric valuation frequencies establish the densities, while periodic approximations establish general fixed-length frequency existence. All boundary cases \(m=2\), \(k=0\), and within-block offset zero are included. The checker confirmed 318792 exact integer/rational assertions in finite parameter ranges; the proof supplies the infinite extension.

## Originality — PASS, with documented residual risk

The main same-object paper by Barro–Kaboré–Bognini (2022), inspected through its primary full text, proves palindrome and palindromic-factorization properties of the same substitution but no blockwise Abelian-power occurrence-set equivalence or its densities. Parreau–Rigo–Rowland–Vandomme (2015), also inspected in primary full text, establishes regularity and recurrences for scalar Abelian-equivalence-class *counts* of the binary word; that does not specify when consecutive blocks have equal Parikh vectors at every position. The 2024 Parikh-collinear theorem applies to rank-one incidence morphisms, whereas the substitution here has a full-rank incidence matrix. The 2023 period-doubling repetition study deals with ordinary factors, and Machacek (2025) relates a different word's group-action complexity to binary period-doubling Abelian complexity. The explicit occurrence sets, all-modulus periodic dilation, and exact starting-position densities are not given or implied by any of these inspected statements. Related public mathematical records concern string attractors and modular extensions, not this theorem. No direct covering theorem was located. Literature indexing is incomplete, so unindexed equivalent coverage is a residual risk, and originality is not independently certified.

## Mathematical value — PASS

Abelian repetitions distinguish symbol-content periodicity from exact letterwise repetitions and are a standard structural invariant in combinatorics on words. The result does more than count Abelian classes: it determines the full set of starting positions of Abelian powers at all dyadically related periods, with an exact reduction of arbitrary periods to their odd parts. At every pure power of two, the square and cube sets have explicitly quantified positive densities over *every* alphabet size, while all Abelian fourth powers are excluded at those periods. This produces a complete, natural all-scale classification and sharp exponent cutoff, not a finite census or numerical gain. The exact Parikh-frequency pushforward supplies a second structural consequence of the common-prefix argument. A future analysis of odd-period Abelian powers can use this reduction without repeating the even-period cases.

## Closest literature and limitations

- Barro, Kaboré and Bognini, *On the palindromic zl-factorization and c-factorization of the generalized period-doubling sequences*, Australasian Journal of Combinatorics 83(3) (2022), 435–447, https://ajc.maths.uq.edu.au/pdf/83/ajc_v83_p435.pdf .
- Parreau, Rigo, Rowland and Vandomme, *A New Approach to the 2-Regularity of the \(\ell\)-Abelian Complexity of 2-Automatic Sequences*, Electronic Journal of Combinatorics 22(1) (2015), #P1.27, https://arxiv.org/abs/1405.3532 .
- Currie, *The analogue of overlap-freeness for the period-doubling sequence*, 2023, https://arxiv.org/abs/2303.14539 .
- Rigo, Stipulanti and Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, 2024, https://doi.org/10.1007/s00224-024-10197-5 .
- Machacek, *Group Actions and Some Combinatorics on Words with \(\mathbf{vtm}\)*, 2025, https://arxiv.org/abs/2509.26613 .

The no-fourth-power assertion does not extend to arbitrary non-dyadic periods without further analysis. The general Parikh-frequency result is an exact reduction to base lengths, not a formula for each odd length. Computational checks are bounded, and independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
