# Exact derived-length threshold for elementary-abelian Schur multipliers

## Finding
For a prime \(p\) and an integer \(k\ge1\), define \(\delta_p(k)\) to be the minimum derived length among finite groups \(G\) with
\[
M(G)\cong C_p^k,
\]
where a nontrivial abelian group has derived length \(1\). Then
\[
\delta_p(k)=
\begin{cases}
1,& k=\binom{r}{2}\text{ for some }r\ge2,\\
2,& \text{otherwise}.
\end{cases}
\]
Equivalently, the first case occurs exactly when \(8k+1\) is an odd square.

Thus the elementary-abelian multiplier ranks realizable by abelian groups are exactly
\[
1,3,6,10,15,21,\ldots,
\]
and every missing rank is nevertheless realized by a metabelian finite group.

## Assumptions and scope
The Schur multiplier is \(M(G)=H_2(G,\mathbb Z)\). Derived length is computed from the derived series, so nontrivial abelian groups have length \(1\) and nonabelian metabelian groups have length \(2\). The theorem concerns all finite groups, not only solvable groups; solvability enters only through the construction supplying the upper bound.

The claim is restricted to nontrivial elementary-abelian target multipliers \(C_p^k\) with \(k\ge1\). It does not classify the minimum derived length for arbitrary finite abelian target multipliers.

## Proof
Let \(B\) be a finite abelian group with \(M(B)\cong C_p^k\). Decompose \(B\) into its Sylow subgroups. For distinct primes the tensor products between Sylow factors vanish, so the \(p\)-primary part of \(M(B)\) is the multiplier of the \(p\)-primary component. Write that component as
\[
P\cong C_{p^{a_1}}\times\cdots\times C_{p^{a_r}},
\qquad a_i\ge1.
\]
For a finite abelian group, the standard direct-product formula for the Schur multiplier gives
\[
M(P)\cong \prod_{1\le i<j\le r} C_{p^{\min(a_i,a_j)}}.
\]
Because \(M(B)\cong C_p^k\) is elementary abelian, every factor in this product must have order \(p\). Hence \(\min(a_i,a_j)=1\) for every pair \(i<j\); equivalently, at most one of the \(a_i\) can exceed \(1\). Therefore every unordered pair contributes exactly one copy of \(C_p\), and
\[
k=\binom{r}{2}.
\]
This proves that an abelian realization forces triangular \(k\). Conversely, if \(k=\binom{r}{2}\), then
\[
M(C_p^r)\cong \bigwedge^2 C_p^r\cong C_p^{\binom{r}{2}}=C_p^k,
\]
so \(\delta_p(k)=1\).

Now suppose \(k\) is not triangular. The preceding argument rules out derived length \(1\), so \(\delta_p(k)\ge2\). Holt's Section 2 constructs, for every elementary-abelian group \(A\cong C_p^k\), a finite group \(G=N\rtimes\langle t\rangle\) with \(N\) abelian and \(G/N\) cyclic, and proves \(M(G)\cong A\). The exceptional case \(p^k=4\) is handled there by a different cyclic action of order \(5\). In every nontriangular case this gives a nonabelian metabelian group, so \(\delta_p(k)\le2\). Hence \(\delta_p(k)=2\).

Finally, \(k=\binom{r}{2}\) is equivalent to \(8k+1=(2r-1)^2\), proving the square criterion.

## Verification
The lower bound is symbolic and uses only the standard multiplier formula for finite abelian groups. The upper bound uses Holt's explicit elementary-abelian construction, not a finite search. In particular, the delicate target \(C_2^2\) is covered by Holt's stated \(p^k=4\) variant with a cyclic complement of order \(5\).

The bundled script `verify_triangular_multiplier.py` independently exhausts \(21,844\) small exponent tuples for finite abelian \(p\)-groups and checks that whenever the multiplier formula is elementary abelian, its rank is exactly \(\binom{r}{2}\). It also checks the equivalent odd-square criterion for \(1\le k\le100\). This finite computation is a regression check only; it is not used to prove the infinite theorem.

## Relationship to prior work
Holt proves that every finite abelian group is the Schur multiplier of a finite solvable group. His Proposition 1.2 recalls that \(M(A)=A\wedge A\) for finite abelian \(A\), and Section 2 gives an explicit realization for every elementary-abelian target \(C_p^k\). That section establishes the metabelian upper bound used here, but the inspected text does not state a minimum-derived-length invariant, the triangular obstruction to abelian realization, or the exact dichotomy above.

The abelian multiplier formula is classical and is explicitly cited by Holt to Huppert. The new point is the sharp synthesis: the classical exterior-square obstruction completely decides when derived length \(1\) is possible, while Holt's new construction shows that one additional derived step always suffices for every remaining elementary-abelian rank.

## Limitations
The result does not minimize group order, nilpotency length, Fitting height, or generator number, and it does not determine minimum derived length for non-elementary finite abelian multipliers. The triangular obstruction itself follows from classical multiplier formulas; the originality claim concerns the exact minimum-derived-length classification obtained by combining that obstruction with the 2026 realization theorem. Literature search cannot certify absolute novelty, and an older source may have recorded an equivalent optimization without using this terminology.

## References
1. D. F. Holt, *Finite abelian groups are Schur multipliers of finite solvable groups*, arXiv:2610.01312v1, first submitted 1 October 2026; especially Theorem 1.1, Proposition 1.2, and Section 2.
2. B. Huppert, *Endliche Gruppen I*, Springer, 1967, Chapter V, Sections 25.3 and 25.10, cited by Holt for the standard Schur-multiplier formulas used above.
