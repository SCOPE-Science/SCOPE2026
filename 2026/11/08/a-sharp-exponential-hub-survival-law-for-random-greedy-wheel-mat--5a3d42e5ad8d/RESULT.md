# A sharp exponential hub-survival law for random greedy wheel matchings

## Finding

Let \(W_n=K_1\vee C_n\) denote the wheel with a distinguished hub and \(n\ge3\) rim vertices. Starting from the empty matching, repeatedly choose an edge uniformly from those whose endpoints are still unmatched, add that edge to the matching, and stop when no such edge remains. Write \(q_n\) for the probability that the hub is unmatched at termination.

For every odd \(n\ge3\), \(q_n=0\). For even \(n=2m\ge4\),
\[
q_{2m}=\frac12 a_{m-1},\qquad a_0=1,\qquad
(4m-1)a_m=\sum_{j=0}^{m-1}a_j a_{m-1-j}\quad(m\ge1).
\]
In particular, \(q_4=1/6\), \(q_6=1/21\), and \(q_8=19/1386\).

Define the entire function
\[
U(z)=1-\sum_{k=1}^{\infty}d_k z^k,\qquad
d_1=\frac14,\quad d_{k+1}=\frac{d_k}{4(k+1)(4k-1)}\quad(k\ge1).
\]
It has exactly one positive zero \(\rho\), with \(3.47547<\rho<3.47548\), and no other zero of modulus at most \(\rho\). For some \(R>\rho\), as \(m\to\infty\),
\[
\boxed{q_{2m}=2\rho^{-m}+O(R^{-m}).}
\]
Thus the hub's survival is exponentially rare with an explicit sharp base and *leading constant exactly two*. The statement includes the parity obstruction and the full finite-size rational recurrence.

## Assumptions and scope

The graph is finite, undirected and simple. Edges are unweighted. At each step only feasible edges (both endpoints currently unmatched) are sampled, uniformly. This is equivalent to assigning independent continuous priority labels to all edges once and greedily retaining edges in increasing priority order. The hub is the unique vertex adjacent to all \(n\) rim vertices. This theorem concerns hub *noncoverage* by an edge-greedy maximal matching, not vertex-greedy matching, an independent uniform maximal matching, or a uniform spanning tree.

## Proof

**1. Disjoint fan components and first-edge recurrence.** Let \(p_k\) denote the probability that a universal hub remains unmatched when attached to all \(k\) vertices of a path \(P_k\). Set \(p_0=1\). In the edge-priority representation, the event that no spoke is accepted in a disjoint union of paths sharing a hub factors into the corresponding events for the individual paths: until a spoke is accepted, different path components use disjoint independent edge labels, and the first locally accepted spoke would also cause global failure unless another spoke had already caused failure. Consequently the global event is equivalent to simultaneous local successes.

For \(k\ge1\), there are \(k\) spokes and \(k-1\) path edges, all equally likely to be selected first. Selecting any spoke is immediate failure. Selecting path edge \((i,i+1)\), for \(1\le i\le k-1\), deletes its endpoints and leaves two path components of lengths \(i-1\) and \(k-i-1\). Therefore
\[
(2k-1)p_k=\sum_{i=1}^{k-1}p_{i-1}p_{k-i-1}.
\]
All odd-indexed values vanish, by induction, since a path of odd size cannot be fully matched without using a spoke. Setting \(a_m=p_{2m}\) gives the claimed convolution recurrence. In the wheel, the first edge is a rim edge with probability \(1/2\), after which \(n-2\) rim vertices form a path attached to the hub. Hence \(q_n=p_{n-2}/2\), which proves both the exact formula and the parity statement.

**2. Generating function and its analytic linearization.** Set \(F(z)=\sum_{m\ge0}a_m z^m\), initially as a formal power series. Multiplying the recurrence by \(z^m\) and summing gives
\[
4zF'(z)-F(z)+1=zF(z)^2,\qquad F(0)=1.
\]
With \(F=-4U'/U\) and \(U(0)=1\), this Riccati equation is equivalent to
\[
16zU''(z)-4U'(z)-U(z)=0,\qquad U'(0)=-\tfrac14.
\]
Its coefficient recurrence is \(4(k+1)(4k-1)[z^{k+1}]U=[z^k]U\). Thus its solution is precisely the stated \(U\). Because \(d_{k+1}/d_k=1/[4(k+1)(4k-1)]\), \(U\) is entire, and \(F=-4U'/U\) holds in a neighborhood of zero by uniqueness of the formal recurrence.

**3. Dominant pole and exact residue.** Write \(D(z)=\sum_{k\ge1}d_kz^k\), so \(U=1-D\). On the positive real axis, \(D\) is continuous and strictly increasing from zero to infinity (already \(d_1z\to\infty\)); therefore \(D(\rho)=1\) at a unique positive \(\rho\). For \(|z|<\rho\), \(|D(z)|\le D(|z|)<1\), so \(U(z)\ne0\). On \(|z|=\rho\), equality \(D(z)=1\) would require all summands \(d_kz^k\) to have the same positive phase; since \(d_1,d_2>0\), this forces \(z=\rho\). Also \(U'(\rho)=-D'(\rho)<0\): the zero is simple.

The isolated-zero property of entire functions supplies \(R>\rho\) such that \(U\) has no other zeros in \(|z|\le R\) (after shrinking \(R\) if needed). Near the simple zero,
\[
F(z)=-4\frac{U'(z)}{U(z)}=\frac4{\rho-z}+H(z),
\]
where \(H\) is analytic for \(|z|<R\). Cauchy's estimate, choosing any fixed intermediate circle with radius strictly between \(\rho\) and \(R\) and renaming that radius \(R\), gives \(a_j=4\rho^{-j-1}+O(R^{-j})\). Substituting \(j=m-1\) into \(q_{2m}=a_{m-1}/2\) proves the claimed asymptotic.

**4. Certified numerical location.** For \(N=16\), let \(U_N(z)=1-\sum_{k=1}^N d_k z^k\). For positive \(z\), the omitted tail is bounded by its first term divided by \(1-r_N(z)\), where \(r_N(z)=z/[4(N+2)(4N+3)]<1\) at the displayed bracket. Exact rational evaluation verifies \(U_N(3.47547)>\operatorname{tail\_bound}(3.47547)\) and \(U_N(3.47548)<0\). Monotonicity yields the stated bracket.

## Verification

Run `python checks/verify.py` using Python 3 standard-library modules only. The checker separately evaluates the full finite-state absorbing matching chain on fan graphs through sixteen path vertices and on wheels with three through sixteen rim vertices, without using the structural convolution in that computation. It also exhausts all \(8!\) edge-priority orders on the four-rim wheel, checks \(24\) exact formal-series coefficient identities, and verifies the root bracket via exact rational tail bounds. The packaged checker reported `VERIFY_OK 58 assertions`.

## Relationship to prior work

Krivelevich, Mészáros, Michaeli and Shikhelman (first publicly available July 16, 2019) establish a local-limit framework for random greedy independent sets and explicitly identify randomized greedy matching with greedy independent-set selection on the line graph. Their principal limit results concern typical-vertex occupancy densities, not the exceptionally high-degree hub noncoverage event in a wheel. Dyer and Frieze (1991) introduced and bounded the same feasible-edge greedy matching process on broad graph classes; the available abstract does not give this wheel-specific hub law. Došlić, Puljiz, Šebek and Žubrinić analyze a different vertex-adsorption model on ladder graphs, including generating-function methods, rather than edge matching on wheels. The exact recurrence, the simple dominant pole and the prefactor-two asymptotic are the specific claims assessed here.

## Limitations

The result is for unweighted wheels and a particular edge-greedy law; it does not yield the distribution of the entire matching or extend automatically to arbitrary joins, weights or other arrival mechanisms. The asymptotic error uses an unspecified \(R>\rho\), not an optimal secondary exponential constant. Historical priority cannot be conclusively excluded, especially in the inaccessible full text of the older Dyer–Frieze work and unindexed literature. The proof is mathematical, with exact finite checks as corroboration, and independent validation has not been performed.

## References

- M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (first submitted July 16, 2019); *Random Structures & Algorithms* 64 (2024), 986–1015. https://arxiv.org/abs/1907.07216 ; https://doi.org/10.1002/rsa.21200
- M. Dyer and A. Frieze, *Randomized greedy matching*, *Random Structures & Algorithms* 2 (1991), 29–45. https://doi.org/10.1002/rsa.3240020104
- T. Došlić, M. Puljiz, S. Šebek, J. Žubrinić, *A model of random sequential adsorption on a ladder graph*, arXiv:2312.02747 (first submitted December 2023). https://arxiv.org/abs/2312.02747
