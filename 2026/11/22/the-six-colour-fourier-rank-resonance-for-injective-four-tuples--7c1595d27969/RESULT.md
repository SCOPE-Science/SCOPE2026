# The six-colour Fourier rank resonance for injective four-tuples and its involution-sensitive signed spectrum

## Finding

Let \(H\) be **any** finite abelian group of order \(q\ge4\), let \(t=|H[2]|\) be the number of elements annihilated by \(2\), and let \(f:H^4\to\{0,1\}\) indicate ordered four-tuples of pairwise distinct elements. These tuples are exactly the proper \(H\)-colourings of the complete graph on four vertices. The unnormalized convolution operator \(T_f:g\mapsto f*g\), acting on complex functions on \(H^4\), has rank

\[
\operatorname{rank}T_f=\begin{cases}168,&q=6,\\q^3,&q\ge4,\ q\ne6.\end{cases}
\]

In every order other than six, the convolution range equals the full \(q^3\)-dimensional subspace of functions invariant under simultaneous translation of all four coordinates. At order six there are exactly 48 **additional** Fourier zeros within that subspace.

More precisely, write an additive frequency quadruple \(k=(k_1,k_2,k_3,k_4)\in\widehat H^4\), so the zero frequency is \(0\). Define
\[
W_H(k)=\sum_{x_1,x_2,x_3,x_4\in H\atop x_i\ne x_j\ (i\ne j)}\prod_{i=1}^{4}k_i(x_i).
\]
All \(q^4-q^3\) *unbalanced* frequencies, for which \(k_1+k_2+k_3+k_4\ne0\), have multiplier zero. For balanced frequencies the **complete signed eigenvalue census**, with disjoint row conditions, is:

| Frequency type | Signed value of \(W_H\) | Number of balanced frequencies |
|---|---:|---:|
| Four zero coordinates | \(q(q-1)(q-2)(q-3)\) | \(1\) |
| Exactly two zero coordinates | \(-q(q-2)(q-3)\) | \(6(q-1)\) |
| Exactly one zero coordinate | \(2q(q-3)\) | \(4(q-1)(q-2)\) |
| No zero coordinates; zero opposite perfect pairings | \(-6q\) | \(q^3-7q^2+15q-8-t\) |
| No zero coordinates; one opposite perfect pairing | \(q(q-6)\) | \(3q^2-12q+6+3t\) |
| No zero coordinates; two opposite perfect pairings | \(2q(q-3)\) | \(3(q-t)\) |
| No zero coordinates; three opposite perfect pairings | \(3q(q-2)\) | \(t-1\) |

An *opposite perfect pairing* is one of the three partitions of \(\{1,2,3,4\}\) into two pairs, such that the sum of the two frequencies in each pair is zero. Distinct rows can have the same eigenvalue; their multiplicities are added when forming the signed-spectrum histogram.

Consequently, the signed spectrum depends only on \(q\) and the two-torsion size \(t\). Conversely, at fixed \(q\), its signed histogram determines \(t\): the value \(3q(q-2)\) has multiplicity \(t-1\) when \(q>4\), and it coalesces with the all-zero-frequency eigenvalue at \(q=4\), where the combined multiplicity is \(t\). Thus, unlike the ordinary number of injective colourings, the signed Fourier spectrum can distinguish finite abelian palettes of the same order.

## Assumptions and scope

All groups are finite and abelian, \(q=|H|\ge4\); no cyclicity or parity hypothesis is needed. The space of complex functions on \(H^4\) has dimension \(q^4\). Convolution and Fourier transform are **unnormalized**. Each \(k_i\) is a multiplicative character \(H\to\mathbb C^\times\), written additively in the dual group, and the Fourier transform here uses \(\prod k_i(x_i)\), not its complex conjugate. Conjugating the convention only permutes frequencies and does not change this signed histogram because every displayed multiplier is real.

For fixed order \(q\), dual-group two-torsion has the same order \(t\) as \(H[2]\). This follows by splitting the finite abelian group into cyclic factors.

## Proof

**1. Character balance.** Translating every coordinate \(x_i\) by the same \(h\in H\) permutes the injective tuples and multiplies their character product by \((k_1+k_2+k_3+k_4)(h)\). If the product character is nontrivial, character orthogonality forces \(W_H(k)=0\). Hence only the \(q^3\) balanced frequencies remain.

**2. Exact character formula by the partition lattice.** For a partition \(\pi\) of the four coordinate positions, let \(E_\pi\) be the tuples whose coordinates agree inside every block. Möbius inversion on the equality-partition lattice gives
\[
f(x)=\sum_{\pi}\mu(\pi)\mathbf1_{E_\pi}(x),\qquad \mu(\pi)=\prod_{B\in\pi}(-1)^{|B|-1}(|B|-1)!.
\]
On summing characters over \(E_\pi\), every block contributes \(q\) precisely when the character-sum inside that block is zero, and otherwise contributes zero. Put \(I_0=\mathbf1_{k_1=k_2=k_3=k_4=0}\), let \(I_{ij}=\mathbf1_{k_i+k_j=0,\ k_r=k_s=0}\), and let \(P(k)\) count the three opposite perfect pairings. On the balanced locus, grouping the fifteen partitions by block sizes yields the *exact integer* formula
\[
W_H(k)=q^4 I_0-q^3\sum_{i<j}I_{ij}+q^2\bigl(2\#\{i:k_i=0\}+P(k)\bigr)-6q.
\]
The terms correspond to the partition types \((1,1,1,1)\), \((2,1,1)\), \((3,1)\), \((2,2)\), and \((4)\), respectively. There are six terms of the second type, four of the third, three of the fourth, and one of the fifth. Direct substitution yields the seven signed values in the table. In particular, a balanced tuple cannot have exactly three zero coordinates.

**3. Exact multiplicities.** The four-zero and two-zero rows have \(1\) and \(6(q-1)\) choices. For exactly one zero coordinate, choose its position, choose a nonzero first and second frequency with their sum nonzero, and determine the third by balance: \(4(q-1)(q-2)\) choices.

For the remaining tuples all four frequencies are nonzero. Let \(M_j\) denote the number admitting exactly \(j\) opposite perfect pairings, for \(j\in\{0,1,2,3\}\). Three pairings occur exactly when all four frequencies are the same nonzero element of order two, so \(M_3=t-1\). Exactly two pairings occur for the rearrangements of \((a,a,-a,-a)\) with \(a\ne-a\), giving \(M_2=3(q-t)\). For each of the three pairing patterns, there are \((q-1)^2\) balanced nonzero quadruples satisfying it; double-counting pairing incidences gives
\[
M_1+2M_2+3M_3=3(q-1)^2,
\quad M_1=3q^2-12q+6+3t.
\]
There are \(q^3-4q^2+6q-3\) balanced frequency quadruples with no zero coordinates, by inclusion-exclusion. Subtraction therefore gives
\[
M_0=q^3-7q^2+15q-8-t.
\]
This proves every row of the census, including nonnegativity for every actually realizable group.

**4. The unique extra rank resonance.** Because \(q\ge4\), the positive values \(2q(q-3)\), \(3q(q-2)\), \(q(q-1)(q-2)(q-3)\), and the negative values \(-6q\), \(-q(q-2)(q-3)\) are nonzero. The only potentially vanishing balanced value is \(q(q-6)\), and it vanishes precisely at \(q=6\). Every abelian group of order six is cyclic, with \(t=2\); substituting into the one-pair multiplicity gives \(3\cdot6^2-12\cdot6+6+3\cdot2=48\). Hence the convolution rank is \(q^3-48=168\) at order six, and \(q^3\) otherwise. Diagonal translation invariance of \(f*g\) (by substitution in the convolution) gives the claimed range interpretation when the ranks agree.

**5. Recovering the two-torsion size.** For \(q>4\), the value \(3q(q-2)\) is distinct from the other six signed values (including the four-zero value), so its occurrence count is exactly \(t-1\). At \(q=4\), equality between these two positive levels yields count \(t\) instead. This proves the spectral distinction without requiring a chosen decomposition of \(H\).

## Verification

The package contains two standalone programs. Running `python3 checks/verify_partition_formula.py` uses **exact integer arithmetic** to calculate the partition-lattice character multiplier for every balanced frequency for the cyclic orders four through twelve selected in its test suite and the direct products specified in the script, and checks both the full histogram and rank formula. Running `python3 checks/verify_direct_character_sums.py` independently sums character products over all ordered injective four-tuples in cyclic groups of orders four, five, six, eight and noncyclic groups of orders four and eight; numerical rounding is only a secondary finite sanity check, not the basis for the all-group proof. Both programs completed successfully in the recorded checks.

Notably, at order six the balanced signed histogram is \(-72:30\), \(-36:44\), \(0:48\), \(36:92\), \(72:1\), \(360:1\), summing to \(216\) balanced characters.

## Relationship to prior work

Goodall's 2008 account of finite abelian Fourier methods for graph colourings and Tutte-Grothendieck invariants supplies the general character-analysis context, as well as classical proper-colouring counting. Its graph-polynomial and tension/flow formulas do **not state** the present signed character-by-character census for injective four-tuples, the exceptional order-six rank, or the dependence on \(H[2]\). The present proof is a direct finite equality-partition Möbius computation, rather than a consequence claimed to be absent from all classical literature.

## Limitations

The theorem concerns injective ordered four-tuples and no other word lengths or graph families. It is specific to finite abelian groups and the signed spectrum of unnormalized **counting** convolution. Its rank is not a claim about minimal samples under noise; it does not supply a universal condition number or an inversion algorithm for the order-six lost modes. Although the closest available primary text and indexed mathematical records were checked for an equivalent statement, a previously unindexed inclusion-exclusion tabulation could exist. Numerical checks cover only the explicitly listed finite groups; the infinite statement rests on the analytic proof above.

## References

- Andrew Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, first public arXiv version dated 2008-06-30, [arXiv:0806.4848](https://arxiv.org/abs/0806.4848).
