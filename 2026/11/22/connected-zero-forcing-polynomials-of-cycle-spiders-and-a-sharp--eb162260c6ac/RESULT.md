# Connected zero-forcing polynomials of cycle spiders and a sharp real-root transition

## Finding

Take a simple cycle of length \(c\ge3\), attach \(t\ge2\) pendant edges at the same cycle vertex, and subdivide exactly one of those pendant edges once. The connected zero-forcing polynomial of the resulting graph is real-rooted **if and only if** \(c\in\{3,4\}\) and \(t\ge4\). The threshold concerns the number of arms, not the length of the subdivided arm. At \(t=4\) the factor contributed by the arms has a double root at \(-2\).

The proof uses an enumerative specialization of Brimkov's connected-forcing results for unicyclic graphs. The cardinality enumeration below is included to exhibit the two sources of nonreal zeros, not claimed as independent of the structural results in that work.

## Assumptions and scope

All graphs are finite, simple and undirected. An initially blue set is a connected zero-forcing set if it induces a connected subgraph and repeated applications of the rule “a blue vertex with one white neighbor colors it blue” can color the graph. The polynomial counts such vertex sets by size, not forcing sequences. A pendant path of length \(p\) has \(p\) new vertices after its initial vertex at the cycle hub. Real-rootedness is over the complex numbers, including multiplicities. For unrestricted positive arm lengths we derive a size enumerator, not a root classification.

## Proof

Let \(v\) be the hub, and for the moment take arbitrary positive arm lengths \(p_1,\ldots,p_t\). By Brimkov [1, Lemma 2], every connected forcing set contains \(v\), because deleting it leaves \(t+1\ge3\) components, and contains the bases of all but at most one of the pendant arms. By [1, Proposition 3] the cycle block contributes at least two initially blue vertices. Induced connectivity then requires the cycle selection to be an interval containing \(v\), or the whole cycle; on each arm the selected vertices form a prefix, empty on at most one arm. These conditions suffice: a cycle boundary vertex other than \(v\) can force the white arc, and the last initially blue vertex of each nonempty prefix can force the rest of its arm. If an arm was omitted, \(v\) now has just one white neighbor and can start it. Brimkov's Lemma 8 treats the same forcing construction at the level of an optimal choice when the cycle has one articulation point.

With \(F_c(z)=\sum_{j=1}^{c-2}(j+1)z^j+z^{c-1}\) and \(H_i(z)=\sum_{j=1}^{p_i}z^j\), the interval-and-prefix count is
\[
Z_C(z)=z F_c(z)\left(\prod_{i=1}^{t}H_i(z)+\sum_{j=1}^{t}\prod_{i\ne j}H_i(z)\right).
\]
For a proper cycle selection with \(j\) vertices besides \(v\), distributing those vertices between the two directions gives \(j+1\) choices. The full cycle has one choice. Each seeded arm independently contributes one prefix, and the second term specifies the sole unseeded arm. In particular the minimum size is \(t+1\) with \(2t\) choices, and the total count is \(\binom c2(\prod_i p_i+\sum_j\prod_{i\ne j}p_i)\).

When \(p_1=2\) and all other \(p_i=1\), the bracket becomes \(z^{t-1}\bigl(z(1+z)+1+(t-1)(1+z)\bigr)\), giving
\[
Z_C(z)=z^t F_c(z)(z^2+tz+t).
\]
The discriminant \(t(t-4)\) proves the arm threshold, including the double root at \(t=4\). The cycle factor is \(F_3=z(z+2)\) or \(F_4=z(z+1)(z+2)\) for the two smallest cycles. For \(c\ge5\), the first three coefficients of \(F_c(z)/z\) are \(2,3,4\). If all its roots were real, positivity of its coefficients and its nonzero constant term would make all roots negative. Dividing by its constant term would write it as \(\prod_i(1+x_i z)\) with every \(x_i>0\). This would give \(\sum_i x_i=3/2\), \(\sum_{i<j}x_ix_j=2\), contradicting \((\sum_i x_i)^2=\sum_i x_i^2+2\sum_{i<j}x_ix_j>4\). Nonreal zeros of either factor are inherited by the product. This proves the stated equivalence.

## Verification and relation to other results

The included `verify.py` uses direct subset connectivity and ordinary forcing rather than the interval-and-prefix characterization. The finite check covers small cycles and arm lengths and tests the one-subdivision discriminant; the proof above covers all stipulated parameters. The cycle factor and its real-root condition also occur in the cycle-bouquet connected-forcing formula (Resultary record `d59372b2f49d`). That shared factor does not account for the arm discriminant. Mukherjee and Ray [2, Problem 5.2] ask for the general unicyclic polynomial; the present root threshold concerns only this single-hub subfamily and its smallest nonuniform arm-length pattern.

1. B. Brimkov, *Complexity and Computation of Connected Zero Forcing*, arXiv:1607.00658v1 (2016), Lemma 2, Proposition 3 and §5.1, especially Lemma 8. https://arxiv.org/abs/1607.00658v1
2. S. Mukherjee and P. Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985v1 (2026). https://arxiv.org/abs/2611.10985v1
