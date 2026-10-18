# Every continuous dimension profile occurs among nonbipartite finite targets
## Finding

For a finite simple graph \(H\), define its continuous dimension profile by
\[
\mathcal D_c(H)
=
\left\{
d\in\mathbb N:
d\ge2
\ \text{and}\
F(2^{\mathbb Z^d})\longrightarrow_c H
\right\},
\]
where \(F(2^{\mathbb Z^d})\) is the standard Schreier graph on the free part of the Bernoulli shift and \(\longrightarrow_c\) denotes a continuous graph homomorphism.

Then the possible profiles are exactly
\[
\varnothing,
\qquad
\{2,3,\ldots,D\}\quad(D\ge2),
\qquad
\{2,3,\ldots\}.
\]

Moreover, every one of these profiles is realized by a finite **nonbipartite** graph:
\[
\mathcal D_c(K_3)=\varnothing,
\]
\[
\mathcal D_c(M_{D,L})=\{2,3,\ldots,D\}
\quad
(D\ge2,\ L\ge4),
\]
for Wang's explicit finite targets \(M_{D,L}\), and
\[
\mathcal D_c(K_4)=\{2,3,\ldots\}.
\]

The Borel behavior of all these examples is the same: every finite nonbipartite graph receives a Borel homomorphism from \(F(2^{\mathbb Z^d})\) for every \(d\ge2\). Thus continuous target behavior realizes every possible dimension cutoff even inside the class whose Borel homomorphism behavior is uniformly positive in every dimension.

## Assumptions and scope

For \(d\ge1\), write
\[
\mathcal H_d
=
\left\{
H:
F(2^{\mathbb Z^d})\longrightarrow_c H
\right\}.
\]

Wang records the monotonicity
\[
\mathcal H_j\subseteq\mathcal H_i
\qquad
(i<j).
\]

For \(d\ge1\) and \(L\ge4\), Wang constructs a finite loopless graph \(M_{d,L}\). Its vertices are certain \(L\)-separated and \(L\)-covering subsets
\[
D\subseteq[-2L,2L]^d\cap\mathbb Z^d,
\]
and two such patterns are adjacent when their overlapping windows agree after translation by one signed coordinate vector. Proposition 7.7 proves
\[
M_{d,L}\in\mathcal H_d\setminus\mathcal H_{d+1}.
\]

The present statement uses dimensions \(d\ge2\), because this is the range where the Borel finite-target problem has the clean bipartite/nonbipartite dichotomy.

## Proof

### Every profile is an initial segment

Suppose
\[
d\in\mathcal D_c(H)
\]
and
\[
2\le e<d.
\]
Then
\[
H\in\mathcal H_d.
\]
Wang's monotonicity gives
\[
\mathcal H_d\subseteq\mathcal H_e,
\]
so
\[
e\in\mathcal D_c(H).
\]

Therefore \(\mathcal D_c(H)\) is downward closed in the linearly ordered set
\[
\{2,3,\ldots\}.
\]

Every downward-closed subset of this set is exactly one of
\[
\varnothing,
\qquad
\{2,\ldots,D\}\quad(D\ge2),
\qquad
\{2,3,\ldots\}.
\]

It remains to realize all three forms.

### Empty profile

The graph \(K_3\) is nonbipartite.

Gao, Jackson, Krohne, and Seward proved that
\[
F(2^{\mathbb Z^2})
\]
has no continuous proper \(3\)-coloring. Equivalently,
\[
K_3\notin\mathcal H_2.
\]

Since
\[
\mathcal H_d\subseteq\mathcal H_2
\]
for every \(d\ge2\), it follows that
\[
K_3\notin\mathcal H_d
\]
for every \(d\ge2\). Hence
\[
\mathcal D_c(K_3)=\varnothing.
\]

### Every finite cutoff

Fix
\[
D\ge2
\]
and
\[
L\ge4.
\]

Wang's Proposition 7.7 gives
\[
M_{D,L}\in\mathcal H_D\setminus\mathcal H_{D+1}.
\]

If
\[
2\le d\le D,
\]
monotonicity gives
\[
\mathcal H_D\subseteq\mathcal H_d,
\]
so
\[
M_{D,L}\in\mathcal H_d.
\]

If
\[
d\ge D+1,
\]
then
\[
\mathcal H_d\subseteq\mathcal H_{D+1}.
\]
Because
\[
M_{D,L}\notin\mathcal H_{D+1},
\]
we also have
\[
M_{D,L}\notin\mathcal H_d.
\]

Therefore
\[
\mathcal D_c(M_{D,L})
=
\{2,3,\ldots,D\}.
\]

The witness \(M_{D,L}\) is nonbipartite. Indeed, it belongs to \(\mathcal H_D\), so there is a continuous, hence Borel, homomorphism from \(F(2^{\mathbb Z^D})\) to it. For \(D>1\), the Borel finite-target characterization says this is possible exactly for nonbipartite targets.

### Infinite profile

Wang's positive theorem applies to \(K_4\) and yields
\[
K_4\in\mathcal H_d
\]
for every \(d\ge1\). In particular,
\[
\mathcal D_c(K_4)=\{2,3,\ldots\}.
\]

The graph \(K_4\) is nonbipartite.

### Borel-versus-continuous contrast

For every \(d\ge2\), the Borel finite-target problem has a dimension-independent answer: a finite graph receives a Borel homomorphism from \(F(2^{\mathbb Z^d})\) exactly when it is nonbipartite.

All three witness families above are nonbipartite. Thus they are indistinguishable by existence of Borel homomorphisms across dimensions, while their continuous profiles range over every possible initial segment.

This proves the classification.

## Verification

The load-bearing statements were checked directly in Wang's full arXiv text.

The introduction defines
\[
\mathcal H_d
=
\{H:F(2^{\mathbb Z^d})\longrightarrow_c H\}
\]
and states
\[
\mathcal H_j\subseteq\mathcal H_i
\]
for \(i<j\).

The same section recalls the failure of a continuous proper \(3\)-coloring for
\[
F(2^{\mathbb Z^2})
\]
and the Borel characterization of finite targets in dimensions greater than one.

Wang's Theorem 1.4 verifies the all-dimensional positive criterion and explicitly checks \(K_4\).

Section 7.2 constructs \(M_{d,L}\). Proposition 7.7 proves, for every \(d\ge1\) and \(L\ge4\),
\[
M_{d,L}\in\mathcal H_d\setminus\mathcal H_{d+1}.
\]

No finite experiment is used. The new classification follows by order-theoretic propagation of these exact membership and nonmembership statements through the nested family \((\mathcal H_d)\).

## Relationship to prior work

Gao, Jackson, Krohne, and Seward developed the continuous homomorphism problem for free abelian shift actions and proved, in particular, the dimension-two obstruction to continuous \(3\)-coloring.

Chandgotia and Unger established the positive Borel theory for hom-shifts associated with graphs containing odd cycles; together with the standard obstruction to Borel \(2\)-coloring, this gives the finite-target bipartite/nonbipartite dichotomy used above.

Wang proves the higher-dimensional computable-enumerability classification, the all-dimensional positive theorem, and the strict chain
\[
\mathcal H_1\supsetneq\mathcal H_2\supsetneq\mathcal H_3\supsetneq\cdots
\]
with explicit witnesses \(M_{d,L}\).

The source states strict dependence on dimension, but it does not formulate the target-wise spectrum
\[
\mathcal D_c(H)
\]
or the complete realization theorem above. Targeted searches under dimension-spectrum, cutoff, threshold, initial-segment, and Borel-versus-continuous formulations did not locate an equivalent published statement.

## Limitations

The result classifies only the **shape and realizability** of the set of dimensions in which a fixed finite target admits a continuous homomorphism. It does not characterize which arbitrary graph has a given finite cutoff.

The finite-cutoff witnesses are Wang's explicit \(M_{D,L}\); no claim is made that they are size-minimal.

The classification is stated for \(d\ge2\). The source also studies \(d=1\), but the Borel comparison emphasized here is the uniform \(d>1\) dichotomy.

The argument is a structural corollary of Wang's nestedness and explicit separation theorem together with the known \(K_3\) and \(K_4\) endpoints; it introduces no new marker construction.

## References

[1] Ruijun Wang, “Continuous graph homomorphisms of higher dimensional abelian group actions,” arXiv:2609.39824v1, first posted 30 September 2026.

[2] Su Gao, Steve Jackson, Edward Krohne, and Brandon Seward, “Continuous Combinatorics of Abelian Group Actions,” arXiv:1803.03872; *Memoirs of the American Mathematical Society* 311 (2025), no. 1573, 1–120.

[3] Nishant Chandgotia and Spencer Unger, “Borel factors and embeddings of systems in subshifts,” arXiv:2203.09359; *Israel Journal of Mathematics* 269 (2025), no. 2, 501–543.
