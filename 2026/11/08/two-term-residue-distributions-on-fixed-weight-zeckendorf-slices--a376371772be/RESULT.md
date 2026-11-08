# Two-term residue distributions on fixed-weight Zeckendorf slices

## Finding
Fix integers \(k\ge2\), \(m\ge2\), and \(0\le r<m\). For \(M\ge2\), let \(N_{k,m,r}(M)\) count positive integers \(n<F_{M+1}\) with exactly \(k\) summands in their canonical Zeckendorf expansion and \(n\equiv r\pmod m\). Put \(L=M-1\) and let \(T\) denote the least period of the Fibonacci sequence modulo \(m\).

Choose \(J\) uniformly from \(\{0,\ldots,T-1\}\), put \(X=F_J\pmod m\), and let \(X_1,X_2,\ldots\) be independent copies of \(X\). Define the explicitly computable rational probabilities
\[
P_{k,m}(r)=\Pr(X_1+\cdots+X_k\equiv r\pmod m),
\]
\[
Q_{k,m}(r)=\Pr(2X_1+X_2+\cdots+X_{k-1}\equiv r\pmod m),
\]
with \(k-2\) unscaled summands in the second expression, and
\[
H_{k,m}(r)=\tfrac12Q_{k,m}(r)+P_{k-1,m}(r).
\]
(The definition of \(P_{1,m}\) is the same one-summand probability.) Along the infinite sequence of cutoffs with \(T\mid L\),
\[
\boxed{N_{k,m,r}(M)=\frac{L^k}{k!}P_{k,m}(r)-\frac{L^{k-1}}{(k-2)!}H_{k,m}(r)+O_{k,m}(L^{k-2}).}
\]
Both coefficients are finite Pisano-period computations, and the second captures the first effect of the prohibition on adjacent Fibonacci summands.

The simpler leading law holds for arbitrary \(M\to\infty\) without a divisibility condition:
\[
\frac{N_{k,m,r}(M)}{\binom{L-k+1}{k}}=P_{k,m}(r)+O_{k,m}(L^{-1}).
\]
When \(k\ge m-1\), every residue \(r\) has \(P_{k,m}(r)>0\). In particular, on the fixed-\(k\) slice, the fraction of **Zeckendorf–Niven** integers (those divisible by their number of summands) converges to \(P_{k,k}(0)>0\). This is a conditional proportion inside a sparse family, **not** a claim of positive natural density among all integers.

The first four exact conditional proportions are
\[
P_{2,2}(0)=\tfrac59,\quad P_{3,3}(0)=\tfrac{85}{256},\quad
P_{4,4}(0)=\tfrac7{27},\quad P_{5,5}(0)=\tfrac15.
\]
The corresponding second-order quantities \(H_{k,k}(0)\) are \(5/6\), \(33/64\), \(7/18\), and \(3/10\), respectively. The nonuniform first examples demonstrate that fixed-weight residue distributions need not approach uniformity.

## Assumptions and scope
Use \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). Canonical Zeckendorf summands have indices \(j\ge2\), without consecutive indices. The allowed indices in the cutoff \(n<F_{M+1}\) are precisely \(\{2,3,\ldots,M\}\), of length \(L=M-1\). All asymptotic constants may depend on the **fixed** pair \((k,m)\), but not on \(M\) or \(r\). The exact two-term formula is asserted only when \(T\mid L\). The first-order conditional law is asserted for all sufficiently large \(M\). The notation \(Q_{k,m}\) is well-defined at \(k=2\): it then reduces to the distribution of \(2X_1\).

The periodic law \(F_{j+T}\equiv F_j\pmod m\) follows from invertibility of the Fibonacci transition map modulo \(m\). Its finite period contains residues \(0\) and \(1\), since \(F_0=0\) and \(F_1=1\).

## Proof
**1. Digit-subset reduction.** Zeckendorf uniqueness identifies the integers counted by \(N_{k,m,r}(M)\) with \(k\)-element subsets of \(\{2,\ldots,M\}\) containing no adjacent indices whose Fibonacci sum is \(r\) modulo \(m\). The total number of admissible \(k\)-subsets, without a residue constraint, is \(\binom{L-k+1}{k}\). Indeed, if the selected positions are \(i_1<\cdots<i_k\), the shifted positions \(i_j-(j-1)\) form an arbitrary \(k\)-subset of an interval of length \(L-k+1\).

**2. Ordered sample before exclusion.** Count ordered \(k\)-tuples of allowed indices, initially permitting repetitions and adjacency. If \(T\mid L\), every residue of the index modulo \(T\) appears exactly \(L/T\) times. Thus the number of ordered tuples with sum \(r\) is exactly \(L^kP_{k,m}(r)\), not merely asymptotically so.

**3. Repeated-index collisions.** For each fixed pair of coordinate positions \((a,b)\), the constraint \(i_a=i_b\) gives exactly \(L^{k-1}Q_{k,m}(r)\) ordered tuples with residue \(r\): the common coordinate contributes twice its Fibonacci residue, while the remaining \(k-2\) coordinates contribute independently. There are \(\binom{k}{2}\) choices of the coordinate pair.

**4. Adjacent-index collisions.** For each pair \((a,b)\), the constraint \(|i_a-i_b|=1\) has two orientations. For each orientation, there are \(L-1\) adjacent index pairs. The complete \(L\)-term cyclic sum of their residues is governed by \(F_j+F_{j+1}=F_{j+2}\), so the paired residue has exactly the one-summand distribution of \(X\). Removing the one boundary pair, and combining with the remaining \(k-2\) independent indices, gives \(L^{k-1}P_{k-1,m}(r)+O_{k,m}(L^{k-2})\) tuples per orientation. Summing the two orientations gives \(2L^{k-1}P_{k-1,m}(r)+O_{k,m}(L^{k-2})\) per coordinate pair. The boundary error is \(O_{k,m}(L^{k-2})\), including \(O(1)\) for \(k=2\).

**5. Higher intersections.** Any two distinct forbidden pair-events (an equality or an absolute difference of one) impose at least two independent affine constraints on the \(k\) coordinates. Their solutions are \(O_k(L^{k-2})\): if events share a vertex, their connected component has at least three vertices; if disjoint, they constrain four vertices in two components. Equality and adjacency of the same pair are disjoint. Every intersection of at least two forbidden events is contained in such a pair intersection. Inclusion–exclusion therefore leaves an aggregate error \(O_{k,m}(L^{k-2})\).

Consequently, the allowed ordered count is
\[
L^kP_{k,m}(r)-\binom{k}{2}L^{k-1}
\bigl(Q_{k,m}(r)+2P_{k-1,m}(r)\bigr)+O_{k,m}(L^{k-2}).
\]
Each admissible subset corresponds to exactly \(k!\) ordered tuples. Dividing and simplifying proves the boxed expansion.

**6. Unaligned cutoffs and positive constants.** For arbitrary \(L\), each index-residue population differs by \(O_m(1)\) from \(L/T\), so the unrestricted ordered count differs from \(L^kP_{k,m}(r)\) by \(O_{k,m}(L^{k-1})\). The forbidden-pair count is also \(O_k(L^{k-1})\), yielding the claimed leading conditional law. Finally, the period includes values \(0\) and \(1\). If \(k\ge m-1\), for any target \(0\le r<m\) choose \(r\) copies of residue \(1\) and \(k-r\) copies of residue \(0\). This event has positive probability, proving positivity. The Zeckendorf–Niven specialization sets \(m=k\) and \(r=0\).

## Verification
The reproducibility script `artifacts/verify.py` uses only the Python standard library. It computes finite-period probabilities as exact `Fraction` objects; independently counts legal fixed-weight digit vectors with dynamic programming; separately enumerates legal index subsets at small cutoffs; and checks the stated four rational constants, a family of congruence moduli and cutoff sizes, and an exact two-summand formula. Run it using `python3 artifacts/verify.py` from the package root. Finite checks do not prove the asymptotic error bound; the collision enumeration above supplies the infinite argument.

## Relationship to prior work
Lao, Miller, Rosa, Shiliaev, Tresch, Wong, and Zhang (2026) introduce the current arithmetic-progression questions, and establish that Zeckendorf–Niven numbers occur infinitely often in every progression, together with bounds on runs of consecutive examples. Those statements do not specify conditional densities among representations with a **fixed** number of summands. Their definition of the Zeckendorf digit sum is used here.

Wagner (2007) investigates fixed-digit-sum counts and residue distribution for general linear-recurrence numeration systems. In particular, his Theorem 12 gives a uniform-type discrepancy bound involving \(\exp(-c k/\log m)\), which does not tend to zero as the digit weight \(k\) is held fixed and the cutoff grows. It does not state the nonuniform exact rational constants or the second-order adjacent-pair correction above. His broader numeration framework is an important priority comparison, not a claim of disjoint subject matter. The ordinary Fibonacci period, Zeckendorf uniqueness, and elementary finite inclusion–exclusion are standard tools; none is claimed as new.

## Limitations
The error term is not uniform when the number of summands or the modulus grows with the cutoff. The second coefficient is stated on Pisano-period-aligned cutoffs only; off-period cutoffs can have additional boundary-dependent terms of order \(L^{k-1}\). A zero density among all integers can coexist with the positive conditional fixed-weight proportions proved here. Historical priority requires further external review, particularly for equivalent formulations implicit in broad earlier generating-function treatments.

## References
1. K. Lao, S. J. Miller, N. Rosa, M. Shiliaev, G. Tresch, T. W. H. Wong, H. Zhang, *On Zeckendorf-Niven numbers and arithmetic progressions* (first arXiv posting June 22, 2026), arXiv:2606.24006v1, https://arxiv.org/abs/2606.24006.
2. S. G. Wagner, *Numbers with fixed sum of digits in linear recurrent number systems*, Ramanujan J. 14 (2007), 43–68, DOI:10.1007/s11139-006-0001-6; author manuscript https://www.finanz.math.tugraz.at/~wagner/fixedsum.pdf.
3. M. Drmota and W. Steiner, *The Zeckendorf expansion of polynomial sequences*, J. Théor. Nombres Bordeaux 14 (2002), 439–475, DOI:10.5802/jtnb.368 (related, but concerns a different asymptotic regime).
