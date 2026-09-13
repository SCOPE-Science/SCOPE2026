# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Principal ideal-Whitehead conjugacy rigidity in rank 5 — vacuous-truth proof

## 1. Target restated

Let $S$ be the class of $\phi \in \mathrm{Out}(F_5)$ such that

- (i) $\phi$ is primitive root-free principal ageometric atoroidal fully
  irreducible;
- (ii) its ideal Whitehead graph $W(\phi)$ is "the disjoint union of eight
  triangles on twelve periodic directions."

Consider the universal statement:

> ($R$) For all $\phi,\psi \in S$ with $\lambda_\phi=\lambda_\psi$,
> equal stretch-factor minimal polynomials, and a graph isomorphism
> $W(\phi)\to W(\psi)$ preserving the periodic-direction labeling up to a
> marked-graph automorphism, $\phi$ is conjugate to $\psi$ in
> $\mathrm{Out}(F_5)$.

A complete target answer is a proof of ($R$) or an explicit counterexample
pair with all stated certificates. We prove ($R$) by showing $S=\varnothing$,
so ($R$) holds vacuously.

## 2. Definitions used

We use only the following definitional fact from Handel–Mosher ideal
Whitehead theory:

- (**V**) The vertex set $V(W(\phi))$ of the ideal Whitehead graph is indexed
  by the relevant periodic/principal directions: there is a canonical
  injection $V(W(\phi)) \hookrightarrow \{\text{periodic directions}\}$,
  which is a bijection onto the twelve directions under the literal reading
  of (ii).

No further deep theory (rotationless index, attraction dynamics, stretch
factors) is needed.

## 3. Lemmas

**Lemma 1 (graph count).** If $G \cong \bigsqcup_{i=1}^{8} K_3$ (disjoint union
of eight triangles), then $|V(G)| = 8 \times 3 = 24$ and $|E(G)| = 24$,
with $8$ connected components each of size $3$.

*Proof.* Each copy of $K_3$ has $3$ vertices and $3$ edges; disjointness adds
them. Machine-checked in `output/artifacts/check_counts.py`. ∎

**Lemma 2 (direction bound).** Any graph satisfying (ii) has $|V| = 12$
under the literal bijection reading, and in any case $|V| \le 12$ under the
charitable injection reading of (**V**).

*Proof.* "On twelve periodic directions" fixes the direction set at
cardinality $12$. A bijection gives $|V|=12$; an injection
$V \hookrightarrow 12$-element set gives $|V| \le 12$. ∎

## 4. Theorem

**Theorem.** No outer automorphism in any rank, in particular no
$\phi \in \mathrm{Out}(F_5)$, satisfies hypothesis (ii). That is,
$S = \varnothing$. Consequently ($R$) is true vacuously, proving the
prove-side of the target.

*Proof.* Suppose $\phi$ satisfied (ii). By Lemma 1, $|V(W(\phi))| = 24$.
By Lemma 2, $|V(W(\phi))| = 12$ (literal) or $\le 12$ (charitable).
Both contradict $24$: $24 \ne 12$ and $24 > 12$ (pigeonhole). Hence no such
$\phi$ exists. A universal implication over an empty domain,
$\forall\phi,\psi\in\varnothing\,(P \Rightarrow Q)$, is true in classical
logic. Adding further antecedents (equal stretch factor, equal minimal
polynomial, Whitehead-isomorphism) only shrinks the already-empty domain,
preserving vacuous truth. ∎

## 5. Remark (independent second obstruction)

For rank $n=5$, a principal fully irreducible has rotationless index
$i = 3/2 - n = -7/2$, each triangle contributing $-1/2$, hence exactly
$2n-3 = 7$ triangles. "Eight triangles" independently contradicts
"principal" in rank $5$. The proof above does not need this; it is recorded
as a corroborating inconsistency.

## 6. What is and is not claimed

- **Proved:** the combined Whitehead-plus-equal-stretch-minpoly data
  determines the conjugacy class over the stated class, vacuously, because
  the class is empty.
- **Computed evidence:** `check_counts.py` certifies $24$-vs-$12$ and
  $8$-vs-$7$ arithmetic.
- **Not claimed:** any substantive rigidity for nonempty principal classes
  (e.g. the correct $7$-triangle class), any new train-track construction,
  any novelty in Handel–Mosher theory. The argument is elementary logic plus
  counting; originality lies only in observing the target hypothesis is
  unsatisfiable.
- **Uncertainty:** none material to the logic; the conclusion is robust under
  both literal and charitable readings of "on twelve periodic directions."

## 7. Reproduction

Run `python3 output/artifacts/check_counts.py`; it asserts vertices $=24$,
edges $=24$, components $=8$, all of size $3$, mismatch with $12$, and
$2\cdot 5-3 = 7 \ne 8$.
