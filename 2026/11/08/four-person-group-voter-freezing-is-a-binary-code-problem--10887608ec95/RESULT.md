# Four-person group-voter freezing is a binary-code problem

## Finding

Let \(H=(V,\mathcal E)\) be any finite simple \(4\)-uniform hypergraph, with \(n=|V|\ge4\) vertices and \(m=|\mathcal E|\ge1\) hyperedges. Use the *simplicial group-driven voter rule*: a selected person may switch its binary opinion only if the other three people in one selected incident group all hold the opposite opinion. All permitted vertex--group selections have positive probability. Opinions are encoded by \(x\in\mathbb F_2^n\). Let \(B\in\mathbb F_2^{m\times n}\) be the hyperedge--vertex incidence matrix and set \(r=\operatorname{rank}_{\mathbb F_2}(B)\).

**Theorem.** The vector \(a(x)\in\{0,1\}^m\) marking the hyperedges that currently permit an opinion change is exactly \(a(x)=Bx\) over \(\mathbb F_2\). Every realizable activity vector has exactly \(2^{n-r}\) preimages. Consequently:

- Exactly \(2^{n-r}\) opinion configurations are frozen (no state-changing update is possible), and the proportion of such configurations under independent fair initial opinions is \(2^{-r}\).
- An activity pattern \(y\in\mathbb F_2^m\) is attainable if and only if \(w\cdot y=0\) for every \(w\in\mathbb F_2^m\) with \(B^{\mathsf T}w=0\). Every attainable pattern has probability \(2^{-r}\) under independent fair initial opinions.
- Under independent fair initial opinions, the individual hyperedge-activity indicators are mutually independent if and only if \(r=m\).
- The only frozen configurations are the two global consensus configurations if and only if \(r=n-1\).

In particular, the complete \(4\)-uniform hypergraph on every \(n\ge5\) vertices has precisely two frozen configurations. Conversely, the three-edge system \(\{\{1,2,3,4\},\{1,2,5,6\},\{3,4,5,6\}\}\) has rank \(2\) and exactly \(16\) frozen configurations; its three activity indicators satisfy an exact parity constraint and cannot all be active simultaneously.

Among the simplicial group-voter rules on an \(s\)-person group for integer \(s\ge3\), the four-person rule is the **only** group size whose single-group activity indicator is an affine function of its binary opinions over \(\mathbb F_2\).

## Assumptions and scope

A configuration is *frozen* if no single state-changing transition has positive rate or probability. This is a statement about instantaneous transitions on a **fixed**, not annealed or rewired, hypergraph. The focal vertex is updated by inspecting all other \(s-1\) members of a selected group without replacement. In the theorem \(s=4\). The hypergraph need not be connected, regular, linear, or acyclic and may contain isolated vertices. Every incident pair of focal vertex and group must be selectable with positive probability; their exact rates do not matter. No spontaneous flips are permitted. Random-initialization claims use independent unbiased Bernoulli opinions; the deterministic statements hold for every configuration.

## Proof

**Step 1 (activity versus parity).** In a group of four, if the number of opinion-one vertices is \(k\in\{0,1,2,3,4\}\), a person can switch exactly when it is the unique minority. This happens precisely for \(k=1\) or \(k=3\). Both are exactly the odd values of \(k\). Thus the activity indicator for edge \(e\) is \(\sum_{v\in e}x_v\pmod2\), the corresponding coordinate of \(Bx\). This equivalence includes the boundaries \(k=0,2,4\), when no flip is allowed.

**Step 2 (the entire activity spectrum).** Regard \(B\) as a linear map from \(\mathbb F_2^n\) to \(\mathbb F_2^m\). Its image has \(2^r\) elements and its kernel has \(2^{n-r}\). For any \(y\in\operatorname{im}B\), every solution to \(Bx=y\) forms a coset of the kernel, so it has exactly \(2^{n-r}\) elements. A vector lies in \(\operatorname{im}B\) exactly when it is orthogonal to \(\ker(B^{\mathsf T})\); this proves the stated parity-constraint characterization. Frozen states are precisely \(Bx=0\). Under independent fair initial opinions, all \(2^n\) states have equal probability, hence every attainable activity vector has probability \(2^{-r}\).

**Step 3 (independence and consensus-only criterion).** If \(r=m\), then \(\operatorname{im}B=\mathbb F_2^m\), so the activity vector is uniformly distributed on the full cube and its indicators are independent fair bits. Conversely, each row of \(B\) is nonzero, hence every individual indicator is a fair bit. Mutual independence therefore forces all \(2^m\) activity vectors to occur, i.e. \(r=m\). Since every row contains four ones, the all-one opinion vector lies in \(\ker B\), as does the all-zero vector. Thus the frozen set consists of these two vectors alone if and only if \(\dim\ker B=1\), equivalently \(r=n-1\).

**Step 4 (dense and dependent witnesses).** For the complete \(4\)-uniform hypergraph on \(n\ge5\) vertices, every row has even weight, so \(\operatorname{im}B^{\mathsf T}\) lies in the even-weight subspace of \(\mathbb F_2^n\). For any distinct \(i,j\), choose three other vertices \(S\); the incidence rows of \(S\cup\{i\}\) and \(S\cup\{j\}\) sum to the vector with ones exactly at \(i,j\). Such vectors span the entire even-weight subspace, hence \(r=n-1\). For the stated three-edge example, each vertex belongs to exactly two edges, so the sum of all three incidence rows is zero. Any two of these distinct rows are independent; thus \(r=2\), giving \(2^{6-2}=16\) frozen states. The dependency forces \(a_1+a_2+a_3=0\pmod2\) and rules out the all-active pattern.

**Step 5 (uniqueness of the four-person linearization).** For any group size \(s\ge3\), the single-group activity function \(f_s\) is zero when all opinions are zero, equals one at a configuration with exactly one one, and is invariant under permutation of the \(s\) coordinates. If \(f_s\) were affine over \(\mathbb F_2\), its zero value at zero would remove the constant term, permutation invariance would force equal coordinate coefficients, and the singleton value would force each coefficient to be one. Hence \(f_s\) would be parity. But at a configuration with three ones, \(f_s=0\) whenever \(s=3\) or \(s\ge5\): for \(s=3\) it is unanimous, while for \(s\ge5\) both opinion types have at least two members unless \(s=5\), when they have three and two. Parity is one there. Only \(s=4\) avoids this contradiction, and Step 1 proves that case works.

## Verification

Execute `python verify.py` from this package using Python 3 with only its standard library. The verifier constructs allowed flips directly from the focal-agent update rule and, independently, computes the mod-two incidence transformation and its row rank. It checks all \(2^n\) configurations of \(3{,}537\) small hypergraphs (\(226{,}656\) complete configurations), verifies uniform fiber sizes and frozen-state counts, tests the dependent six-vertex witness and the complete five-vertex hypergraph, and checks the parity failure for group sizes \(3\), \(5\), and \(6\). These checks reproduce illustrative finite cases; the unrestricted theorem follows from the proof above, not from enumeration.

## Relationship to prior work

Kim, Lee, Min, Porter, San Miguel, and Goh introduced the group-driven voter mechanism and the special rule \(q=s-1\) without duplicate observations, termed the simplicial GVM. Their principal calculations concern consensus times, drift and exit probabilities on **annealed** hypergraphs, including the supplemental analysis of simplicial updates; they do not supply the fixed-hypergraph binary-rank description of frozen states or attainable activity patterns. Noonan and Lambiotte studied majority-rule dynamics primarily on three-person hyperedges with different update mechanisms. Chung and Tsiatas analyzed more general hypergraph coloring/voting games, especially memoryless hyperedge recoloring, which is not the focal-person unanimity rule specified here. The rank-nullity and code-image facts used after identifying the microscopic parity rule are classical; the claim is the exact mapping from the four-person dynamical mechanism to these invariants and its network-wide consequences.

## Limitations

The theorem classifies **instantaneously frozen** configurations and initial hyperedge activity, not all recurrent communicating classes or long-time consensus probabilities. A configuration with a possible flip need not ever reach a frozen configuration. Sampling with replacement, different \(q\), spontaneous noise, changing groups, unequal hyperedge sizes, or deterministic scheduling can invalidate the translation to the stated dynamics. First-public-date evidence is the July 15, 2024 arXiv v1 submission, not the later 2025 journal publication. Literature novelty remains subject to unindexed or inaccessible equivalent work; no independent external validation has been performed.

## References

1. J. Kim, D.-S. Lee, B. Min, M. A. Porter, M. San Miguel, and K.-I. Goh, *Competition between group interactions and nonlinearity in voter dynamics on hypergraphs*, arXiv:2407.11261, v1 submitted July 15, 2024. https://arxiv.org/abs/2407.11261 . Open-author version with supplemental material: https://www.math.ucla.edu/~mason/papers/Kim-etal-PRE2025.pdf .
2. J. Noonan and R. Lambiotte, *Dynamics of majority rule on hypergraphs*, Physical Review E 104, 024316 (2021). https://doi.org/10.1103/PhysRevE.104.024316 .
3. F. Chung and A. Tsiatas, *Hypergraph Coloring Games and Voter Models*, Internet Mathematics 10, 66–86 (2014). https://doi.org/10.1080/15427951.2013.833676 .
