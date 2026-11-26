# A binomially thinned occupancy law for leaves of perfectly matchable Cayley trees

## Finding

Let \(T_{2m}\) be a uniform labeled tree on \(\{1,\ldots,2m\}\), and let \(\mathcal P\) denote the event that it has a perfect matching. For each integer \(m\ge 2\), write \(L_{2m}\) for its number of degree-one vertices. Draw \(Q_m\sim\operatorname{Bin}(m-2,1/2)\), and independently put \(Q_m\) balls into \(m\) boxes, each ball choosing a uniform box. Then, **conditional on \(\mathcal P\), the complete law of \(L_{2m}\) equals the law of the number of empty boxes.**

Equivalently, for every complex \(z\),
\[
\mathbb E[z^{L_{2m}}\mid\mathcal P]
=\sum_{k=0}^{m}\binom mk(z-1)^k\left(1-\frac{k}{2m}\right)^{m-2}.
\]
This formula gives, with \(a_m=(1-1/(2m))^{m-2}\) and \(b_m=(1-1/m)^{m-2}\),
\[
\mathbb E[L_{2m}\mid\mathcal P]=ma_m,
\qquad
\operatorname{Var}(L_{2m}\mid\mathcal P)
=ma_m(1-a_m)+m(m-1)(b_m-a_m^2).
\]
In particular,
\[
\frac{L_{2m}}m\xrightarrow{L^2}e^{-1/2},
\qquad
\frac{\operatorname{Var}(L_{2m}\mid\mathcal P)}m
\longrightarrow e^{-1/2}-\frac54e^{-1}>0.
\]
The conditional leaf fraction among all \(2m\) vertices approaches \(e^{-1/2}/2\), versus the unconditional Cayley-tree fraction \(e^{-1}\). The conditioning thus induces a definite change in leaf density.

## Assumptions and scope

All trees are simple, undirected, labeled, and uniformly sampled from the \((2m)^{2m-2}\) Cayley trees on \(2m\) labels. A perfect matching is a set of \(m\) vertex-disjoint edges covering every vertex. The event \(\mathcal P\) has positive probability; the result concerns its exact conditional distribution, **not** the uniform distribution over unlabeled trees or a uniform tree of a complete bipartite host. The two-vertex tree (\(m=1\)) has two leaves deterministically and is excluded from the occupancy formula.

## Proof

**1. Unique matching and quotient sampler.** A tree has at most one perfect matching: if two were distinct, their symmetric difference would contain an alternating even cycle, impossible in a tree. Therefore, conditioning on \(\mathcal P\) does not weight a tree by a multiplicity of matchings. By label symmetry its unique matching is uniform among the \((2m)!/(2^m m!)\) perfect matchings on the label set. Fix one such matching, comprising \(m\) disjoint vertex pairs. Contract every matching edge. Any original tree containing these edges contracts to a labeled tree \(Q\) on the \(m\) pairs; conversely, each edge of \(Q\) may be lifted using one of the four endpoint combinations independently. Every quotient tree has exactly \(4^{m-1}\) lifts, so \(Q\) is a uniform Cayley tree and its lift choices are independent and uniform. This also proves the known total count \((2m)!\,(2m)^{m-2}/m!\), consistently with OEIS A375105; that enumerative total is not offered as a new result.

**2. Conditional leaf flags.** Let \(d_i\) be the degree in the quotient tree of matching pair \(i\). Since the original matching edge already gives each vertex one neighbor, that pair contributes exactly one leaf if all \(d_i\) lifted edges attach to the same endpoint, and contributes no leaf otherwise. Its conditional leaf-flag probability is \(2(1/2)^{d_i}=2^{1-d_i}\). The endpoint choices at different quotient vertices are independent, including opposite endpoints of the same quotient edge: each of the four lifts factors as two independent fair bits. Thus, given \(Q\), the \(m\) pair-leaf flags are independent Bernoulli variables with these parameters.

**3. Independent thinning of the Prüfer code.** The uniform quotient tree has a length-\(m-2\) Prüfer word, whose letters are independent uniform elements of \(\{1,\ldots,m\}\). Let \(K_i\) count occurrences of letter \(i\); then \(d_i=1+K_i\) and the conditional leaf probability becomes \(2^{-K_i}\). Assign to each word position an independent fair coin; call an occurrence *active* if its coin is heads. A box \(i\) is unoccupied by active occurrences with conditional probability \(2^{-K_i}\). For distinct boxes these events use disjoint coins, exactly reproducing the independent conditional leaf flags. The number of active letters is \(Q_m\sim\operatorname{Bin}(m-2,1/2)\), and their labels are independent uniforms, proving the claimed occupancy identity.

**4. Generating function and moments.** If \(B_i\) is the indicator that box \(i\) is empty, then for every subset \(S\) of \(k\) boxes, \(\mathbb P(B_i=1\ \forall i\in S)=(1-k/(2m))^{m-2}\): each Prüfer position either fails activation or avoids the specified boxes. Expand \(\prod_{i=1}^{m}[1+(z-1)B_i]\) to get the stated probability-generating polynomial. One- and two-box probabilities yield the exact mean and variance. Additionally, the smallest possible leaf count is two, with \(\mathbb P(L_{2m}=2\mid\mathcal P)=m!/[2(2m)^{m-2}]\); the largest is \(m\), with \(\mathbb P(L_{2m}=m\mid\mathcal P)=2^{-(m-2)}\).

**5. Limit.** Taylor expansion gives \(a_m\to e^{-1/2}\) and \(m(b_m-a_m^2)\to -e^{-1}/4\), so the displayed variance has linear coefficient \(e^{-1/2}-5e^{-1}/4\). The scaled variance tends to zero, and the scaled mean tends to \(e^{-1/2}\). Hence the \(L^2\) limit follows. For the unconditional uniformly labeled tree on \(2m\) vertices, its ordinary Prüfer code has length \(2m-2\), giving expected leaf fraction \((1-1/(2m))^{2m-2}\to e^{-1}\).

## Verification

The standalone standard-library program `verify.py` computes exact rational predictions, independently enumerates all Cayley trees on four, six and eight vertices (testing perfect matchability by a matching recursion), and independently enumerates every matching-contracted lift on \(m=2,3,4,5\) pairs. It also checks the generating-function inversion and moment identities for \(2\le m\le24\). These are finite consistency tests; the proof above, not enumeration, establishes the unrestricted claim. To reproduce, run `python verify.py` using Python 3.

## Relationship to prior work

Heuberger and Wagner established the uniqueness of perfect matchings in trees in their Theorem 1.1. Alon, Haber and Krivelevich studied matching-number residues in random labeled trees. Remmel and Williamson treated the **unconditioned** fixed-leaf Cayley-tree enumeration. OEIS A375105 already tabulates the **unmarked number** of perfectly matchable labeled trees, and that number is explicitly credited. These statements, separately, neither state the conditional leaf-count polynomial nor the binomial-thinned occupancy coupling. A general fixed-forest completion sampler also yields a quotient-tree representation, but not the displayed conditioned joint leaf indicators and exact empty-box law without the further analysis above. The closely related complete-bipartite-tree perfect-matching quotient model has only two permitted lifts per quotient edge, rather than four, and is not the present conditioned Cayley law. The novelty assessment is therefore specifically limited to the derived conditional leaf distribution and density comparison.

## Limitations

The result treats perfect-matchable uniform **labeled complete-graph spanning trees** and their **leaf count**, not a general matching-size stratum, a complete bipartite host, or nonuniform spanning-tree measures. It gives an \(L^2\) law of large numbers and exact variance, not a central limit theorem or large deviation principle. Earlier bivariate matching-and-degree enumerations or forest-completion formulas could potentially imply an equivalent result without matching terminology; historical priority remains subject to independent specialist checking. Finite checks are not substitutes for the proof and no independent mathematical audit has been performed.

## References

1. N. Alon, S. Haber, M. Krivelevich, *The number of F-matchings in almost every tree is a zero residue*, first public preprint 2010-06-28, https://arxiv.org/abs/1006.5427.
2. C. Heuberger, S. Wagner, *The number of maximum matchings in a tree*, first public preprint 2010-11-30, https://arxiv.org/abs/1011.6554.
3. J. B. Remmel, S. G. Williamson, *Ranking and unranking trees with a given number or a given set of leaves*, first public preprint 2010-09-10, https://arxiv.org/abs/1009.2060.
4. OEIS A375105, number of spanning trees with a perfect matching in a complete graph of even order, https://oeis.org/A375105.
