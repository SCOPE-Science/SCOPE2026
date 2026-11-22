# Modulo-four Walsh congruences and even-Catalan invertibility for noncrossing partitions

## Finding
Let \(n\ge2\) be an integer, and let \(\mathrm{NC}_n\) be the noncrossing partitions of the vertices \(1,\ldots,n\) arranged on a circle. Embed a partition \(\pi\) as the vector of co-block edge indicators \(x_\pi(\{i,j\})=[i\sim_\pi j]\) in \(\mathbb F_2^{E(K_n)}\). For any frequency graph \(H\subseteq K_n\), define its **unnormalized Walsh multiplier**
\[
W_n(H)=\sum_{\pi\in\mathrm{NC}_n}(-1)^{\sum_{e\in E(H)}x_\pi(e)}.
\]
With \(C_t=\binom{2t}{t}/(t+1)\), the following holds **for every frequency**, uniformly in the order:
\[
\boxed{W_n(H)\equiv C_n-2\sum_{\{i,j\}\in E(H),\ i<j}C_{j-i}C_{n-j+i}\pmod4.} \tag{1}
\]
Define \(\mathcal K_n\) to be the set of pairs \(\{i,j\}\) for which both \(j-i\) and \(n-j+i\) are of the form \(2^r-1\) with \(r\ge1\). Equivalently,
\[
\boxed{W_n(H)\equiv C_n-2|E(H)\cap\mathcal K_n|\pmod4.} \tag{2}
\]
This yields exact first-two-adic-layer classifications:

1. **Odd orders.** The set \(\mathcal K_n\) is empty, so every multiplier has the residue of \(C_n\). If the number \(s_2(n+1)\) of ones in the binary expansion of \(n+1\) equals one, every multiplier is odd. If it equals two, every multiplier is congruent to two modulo four and therefore nonzero. In particular, every integer \(n=2^a+2^b-1\), for \(a>b\ge1\), has an *even* number of noncrossing partitions but an invertible convolution operator with \(\|T_n^{-1}\|_{2\to2}\le1/2\). If \(s_2(n+1)\ge3\), all multipliers are divisible by four, without an asserted nonvanishing classification.
2. **Even orders.** If \(s_2(n+2)\le2\), the set \(\mathcal K_n\) is nonempty, and **exactly half** of all \(2^{\binom n2}\) frequencies have two-adic valuation exactly one; the other half are divisible by four. Thus \(\operatorname{rank}T_n\ge2^{\binom n2-1}\). If \(s_2(n+2)\ge3\), every multiplier is divisible by four. These valuation statements do not establish the full zero set.

## Assumptions and scope
A noncrossing partition is a set partition with no two distinct blocks containing vertices \(a<c\) and \(b<d\), respectively, with \(a<b<c<d\). The indicator \(f_n\) is one on vectors \(x_\pi\) and zero elsewhere in the ambient finite Abelian group \(\mathbb F_2^{\binom n2}\). No distinct partitions have the same co-block edge vector. The operator \(T_n g=f_n*g\) uses counting-measure convolution, without a normalization factor. Thus its Walsh eigenvalues are precisely \(W_n(H)\), and rank is the count of nonzero multipliers. The two-adic valuation of a nonzero integer \(z\) is the maximum integer \(t\) such that \(2^t\mid z\); a zero multiplier is not assigned a finite valuation. All claims concern \(n\ge2\), all labelled frequency graphs \(H\), and the stated normalizations.

## Proof
**1. First-order character expansion.** For binary \(b\), \((-1)^b=1-2b\). Hence for every fixed partition,
\[
(-1)^{\sum_{e\in E(H)}x_\pi(e)}=\prod_{e\in E(H)}(1-2x_\pi(e))
\equiv1-2\sum_{e\in E(H)}x_\pi(e)\pmod4.
\]
Summing over the \(C_n\) noncrossing partitions yields
\[
W_n(H)\equiv C_n-2\sum_{\{i,j\}\in E(H)}A_n(i,j)\pmod4,
\]
where \(A_n(i,j)\) counts noncrossing partitions with \(i\) and \(j\) in one block.

**2. Exact two-point count.** Set \(d=j-i\) with \(i<j\). Draw the chord between these two vertices. Because its endpoints belong to one block, any other block lies entirely on one side of the chord. Restricting the partition to the two closed circular arcs (each containing both endpoints), then gluing the two endpoint blocks, is a bijection with pairs of noncrossing partitions of the arcs whose two endpoints lie in the same block. On an arc having \(t+1\) vertices the endpoints are consecutive around that arc's circular order; merging them gives a bijection with \(\mathrm{NC}_{t}\), and hence \(C_t\) choices. The arcs have \(d+1\) and \(n-d+1\) vertices, respectively. Therefore
\[
\boxed{A_n(i,j)=C_d C_{n-d}.} \tag{3}
\]
Substituting (3) proves (1). This bijection is also valid for adjacent vertices and the diametral case.

**3. Parity and the critical frequency edges.** Legendre's formula, or the Catalan valuation theorem, gives for every \(t\ge0\)
\[
\nu_2(C_t)=s_2(t+1)-1.
\]
In particular, \(C_t\) is odd exactly when \(t=2^r-1\) for a nonnegative integer \(r\). Since \(1\le d,n-d\le n-1\), the relevant exponents satisfy \(r\ge1\). Reduction of (1) modulo four now proves (2).

For odd \(n\), two positive odd integers of the form \(2^r-1\) cannot sum to \(n\), so \(\mathcal K_n=\varnothing\). If \(s_2(n+1)=2\), then \(\nu_2(C_n)=1\) and (2) implies \(\nu_2(W_n(H))=1\) at **every frequency**. The required odd integers are exactly \(n=2^a+2^b-1\) with \(a>b\ge1\). The case \(s_2(n+1)=1\) gives odd multipliers. These multipliers cannot vanish, establishing the invertibility and inverse norm bound.

For even \(n\), an edge in \(\mathcal K_n\) exists exactly when \(n+2=2^a+2^b\) for integers \(a,b\ge1\), allowing equality. Because \(n+2\) is even, this is equivalent to \(s_2(n+2)\le2\): a single power of two is the sum of two equal smaller powers. The Catalan number \(C_n\) is even for every positive even \(n\). For a nonempty \(\mathcal K_n\), the bit parity of \(|E(H)\cap\mathcal K_n|\) takes each value on exactly half the binary frequency graphs, so precisely half the coefficients are congruent to two modulo four and therefore nonzero. The other half are divisible by four. If \(\mathcal K_n\) is empty, \(C_n\) is divisible by four: otherwise \(s_2(n+1)=2\), and since \(n+1\) is odd it would equal \(2^a+1\), forcing \(n+2=2^a+2\) and a nonempty \(\mathcal K_n\), contradiction. This proves all even-order assertions.

## Verification
The standalone script `checks/verify.py` independently enumerates noncrossing partitions by restricted-growth words, evaluates their co-block vectors and, for orders \(2\le n\le7\), uses an exact-integer fast Walsh transform to test **all 2,131,018 frequencies** against (1). It separately checks every two-point count (3) in orders \(2\le n\le10\), and computes 200 independently signed character sums in each of orders \(8,9,10\). All tests passed. `checks/verification_output.txt` records the actual invocation output. The all-order theorem is established by the proof above, not by extrapolating the finite tests.

## Relationship to prior work
Kreweras established classical noncrossing-partition enumeration, surveyed by Simion; Deutsch and Sagan proved the Catalan two-adic valuation formula used here. These are antecedents, not claimed contributions. Nica and Speicher's 1997 paper uses a different transform, on multiplicative functions in the **incidence algebra of noncrossing-partition lattices**; its formal-series convolution theorem is not the Walsh convolution on the Boolean co-block edge cube used here. An earlier result on polygon triangulation-incidence Fourier coefficients establishes a similar Catalan modulo-four uniformity law for odd polygon orders, but it uses polygon diagonal coordinates, not noncrossing partition co-block equivalence coordinates. The present claim proves a different two-point event identity and includes the even-order critical-chord half-valuation classification. The *simultaneous congruence of all co-block edge-character evaluations* is not determined solely by Catalan cardinalities or the polygon-diagonal law. Literature comparison was bounded; an earlier signed two-point/Boolean-character treatment cannot be excluded by a failed search.

## Limitations
This is a complete description of residues modulo four, **not** a complete integer Walsh spectrum, complete convolution-rank classification, or exact least nonzero singular value at all orders. When the stated congruence is zero, a multiplier may or may not vanish. The bound \(\|T_n^{-1}\|_{2\to2}\le1/2\) for the even-Catalan invertible family is not asserted to be an equality. The results concern only ordinary type-A noncrossing set partitions and the specified co-block incidence embedding. No independent mathematical audit has been performed.

## References
- E. Deutsch and B. E. Sagan, *Congruences for Catalan and Motzkin numbers and related sequences*, arXiv:math/0407326 (first public version 19 July 2004), Theorem 2.1. https://arxiv.org/abs/math/0407326
- G. Kreweras, *Sur les partitions non croisées d'un cycle*, Discrete Mathematics 1 (1972), 333–350, DOI 10.1016/0012-365X(72)90041-6.
- R. Simion, *Noncrossing partitions*, Discrete Mathematics 217 (2000), 367–409, DOI 10.1016/S0012-365X(99)00273-3.
- A. Nica and R. Speicher, *A “Fourier Transform” for Multiplicative Functions on Non-Crossing Partitions*, Journal of Algebraic Combinatorics 6 (1997), 141–160, DOI 10.1023/A:1008643104945.
