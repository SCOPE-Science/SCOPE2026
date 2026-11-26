# Connected zero-forcing polynomials of one-leaf unicyclic graphs

## Finding

Let \(T_{c,t}\) consist of a cycle of length \(c\ge3\) and a pendant path with \(t\ge1\) new vertices. The nonzero coefficients of its connected zero-forcing polynomial are always unimodal. They are **log-concave if and only if \(t=1\) or \(c\in\{3,4\}\)**. For \(c\ge5\) and \(t\ge2\), log-concavity fails at degree three: the first three coefficients are \(c,c+2,c+5\), and \((c+2)^2-c(c+5)=4-c<0\).

This covers every connected unicyclic graph with exactly one leaf. The all-size enumeration below supports the coefficient theorem; the case \(t=1\) of the enumerator also follows from the separate partially whiskered-cycle formula, and the minimum size is already available from prior unicyclic forcing theory.

## Assumptions and scope

The graphs are finite, simple and undirected. A connected zero-forcing set is a nonempty subset inducing a connected subgraph whose initially blue vertices can color the graph by repeated forces from a blue vertex to its only white neighbor. Write \(Z_C(z)\) for the polynomial summing \(z^{|S|}\) over those sets. Unimodality and log-concavity concern the nonzero coefficient sequence in increasing degree. No assertion is made about real-rootedness or multiple pendant paths.

## Proof

The removal of a unicyclic graph's cycle edges leaves rooted trees at its cycle vertices. Each nontrivial rooted attachment yields a leaf outside the cycle; branching in such a tree yields at least two. Thus exactly one leaf means exactly one attached path.

Write \(v_0\) for the hub. Every connected forcing set meets the cycle in at least two vertices, as also follows from Brimkov [1, Proposition 3]. Indeed, without a cycle edge initially blue, a connected set can color at most one cycle vertex before facing two white cycle neighbors; there is no other entry from the pendant path. The cycle intersection is a cyclic interval of size \(q\ge2\), with the full cycle counted once. Any selected path vertices form a prefix, and the prefix must be empty when the interval avoids \(v_0\).

Conversely, when the interval contains \(v_0\) and is proper, a cycle boundary vertex distinct from \(v_0\) can start coloring the omitted arc. When the interval avoids \(v_0\), force from both ends up to \(v_0\) so that it is the last white cycle vertex, then force it. In both cases, or when the full cycle is blue initially, \(v_0\) can now start the uncolored tail if none of it was seeded; otherwise the last initially blue path vertex can start the suffix. This proves the all-size interval and prefix description.

There are \(q\) proper intervals of size \(q\) containing \(v_0\), each with \(t+1\) choices of prefix, and \(c-q\) avoiding it. Thus
\[
Z_C(z)=\sum_{q=2}^{c-1}z^q\left(c-q+q\sum_{j=0}^{t}z^j\right)+z^c\sum_{j=0}^{t}z^j.
\]
The smallest sets are the \(c\) cycle edges, and the sum of all coefficients is \(\binom{c-1}{2}+(t+1)\binom c2\).

For adjacent differences write \(a_k=[z^k]Z_C\), and set \(b_q=q\) if \(2\le q<c\), \(b_c=1\), and \(b_q=0\) otherwise. Then \(a_k=(c-k)\mathbf1_{2\le k<c}+\sum_{j=0}^{t} b_{k-j}\). For \(2\le k\le c-2\), \(a_{k+1}-a_k=k-b_{k-t}>0\) since \(t\ge1\). For \(k\ge c-1\) the difference is \(-b_{k-t}\le0\). This proves unimodality. The formula gives the three coefficients in the Finding when \(c\ge5,t\ge2\). In the other cases the positive sequences are:

* \(c=3\): \(t+1\) copies of \(3\), then \(1\).
* \(c=4\): \(4\), then \(t\) copies of \(6\), then \(4,1\).
* \(t=1,c\ge5\): \(c,c+2,c+3,\ldots,2c-2,c,1\).

The first two satisfy the adjacent inequalities (including \(6^2\ge4^2\) when \(t=1\)). In the last sequence the first inequality has difference \(c+4\), the internal linear portion has difference one, and the two inequalities at the descending end follow from \((2c-2)^2\ge (2c-3)c\) and \(c^2\ge2c-2\). This completes the equivalence.

## Verification and relationship to prior work

The supplied `VERIFY.py` exhausts the defining connectedness and forcing tests on a finite family, and separately checks the shape tests for a larger set of coefficient arrays. The all-parameter conclusion follows from the proof. As a small example, \(T_{5,2}\) has coefficients \((5,7,10,8,5,1)\) from degree two.

Brimkov [1, Proposition 3, §5.1 Lemmas 3–8 and the unicyclic minimum theorem] gives the structural lower bound, excluded-segment description and minimum connected forcing theory, including the hub-containing construction. The polynomial for \(t=1\) is also the specialization with one whiskered cycle vertex in Resultary record `b21a724a6666`. Neither result asserts the coefficient threshold for one-leaf unicyclic graphs. Mukherjee and Ray [2, Problem 5.2] ask for the polynomial of an arbitrary unicyclic graph. This gives a coefficient-shape result on one complete structural subfamily, not an answer for arbitrary unicyclic graphs. Newton and Brimkov [3] show that graph connected-forcing polynomials need not be unimodal in general.

1. B. Brimkov, *Complexity and Computation of Connected Zero Forcing*, arXiv:1607.00658v1 (2016). https://arxiv.org/abs/1607.00658v1
2. S. Mukherjee and P. Ray, *On the connected zero forcing polynomial of finite trees*, arXiv:2611.10985v1 (2026). https://arxiv.org/abs/2611.10985v1
3. T. Newton and B. Brimkov, *Zero forcing is not unimodal*, arXiv:2611.11352v1 (2026). https://arxiv.org/abs/2611.11352v1
