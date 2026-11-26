# Exact shortest cyclic covers of binary words avoiding the palindromic triple

## Finding
Let \(\mathcal L_k\) consist of all ordinary (linear) binary words of length \(k\) containing no contiguous occurrence of `010`. A cyclic cover is a nonempty cyclic binary string in which every element of \(\mathcal L_k\) occurs as a length-\(k\) cyclic factor, with repetitions permitted. The cover itself is **not** required to avoid `010`. Denote its minimum possible cyclic length by \(C_k\), and put \(E_k=C_k-|\mathcal L_k|\).

For every integer \(k\ge3\), the exact generating function is
\[
 \sum_{k\ge3} E_k z^k =
 \frac{z^3(1-2z+2z^2)}{(1-z)^2(1-2z+z^2-z^3)}.
\]
The required-factor counts satisfy
\[
 \sum_{k\ge0}|\mathcal L_k|z^k=\frac{1+z^2}{1-2z+z^2-z^3}.
\]
In particular, for \(k=3,4,\ldots,13\), the values of \(E_k\) are \(1,2,4,9,19,37,69,126,227,405,718\), and the minimum cyclic lengths are \(8,14,25,46,84,151,269,477,843,1486,2615\). **Every minimum-length cyclic cover necessarily contains the forbidden triple `010`.** Bit complementation gives exactly the same statements for the language avoiding `101`.

If \(\alpha\) denotes the least positive root of \(1-2z+z^2-z^3\), the limiting overhead is
\[
 \lim_{k\to\infty}\frac{E_k}{|\mathcal L_k|}=
 \frac{\alpha^3(1-2\alpha+2\alpha^2)}{(1-\alpha)^2(1+\alpha^2)}
 =0.3848029157\ldots.
\]

## Assumptions and scope
Words in \(\mathcal L_k\) avoid `010` **within their linear boundaries**, with no periodic-extendability condition. Cyclic occurrences in a covering string wrap around the ends. The de Bruijn graph is the full binary overlap graph on vertices of length \(n=k-1\); its edges are length-\(k\) words. A required edge is one whose word avoids `010`; an added edge may be forbidden. All constructions use a multigraph, so repeated traversals are counted with multiplicity. These conventions distinguish the result from exact-once universal cycles on periodically admissible languages.

## Proof
**1. Degree deficits.** Fix \(k\ge3\), and write \(n=k-1\). Retain just the required length-\(k\) edges on the vertices whose labels avoid `010`. At a vertex \(v\), an outgoing `0` edge is forbidden exactly when \(v\) ends in `01`, while an incoming `0` edge is forbidden exactly when \(v\) starts in `10`. Thus, every required vertex has outgoing degree \(2-\mathbf1_{\{v\text{ ends in }01\}}\) and incoming degree \(2-\mathbf1_{\{v\text{ starts in }10\}}\). The vertices with one missing outgoing edge and no missing incoming edge are
\[
 D_n=\{v:|v|=n,\;v\text{ avoids `010`},\;v\text{ ends in `01`},\;v\text{ does not start in `10`}\}.
\]
They each require one extra outgoing traversal. The vertices with one missing incoming edge and no missing outgoing edge are
\[
 S_n=\{v:|v|=n,\;v\text{ avoids `010`},\;v\text{ starts in `10`},\;v\text{ does not end in `01`}\}.
\]
They each require one extra incoming traversal. Reversal bijects \(D_n\) with \(S_n\). All other vertices are balanced.

**2. Per-source shortest paths.** Let \(j(v)\) be the first zero-based position at which `10` begins inside a vertex \(v\in D_n\), or \(n-1\) if no such position exists. In a path of \(t<n-1\) de Bruijn edges starting at \(v\), the destination begins with the suffix of \(v\) of length \(n-t\). Since every target in \(S_n\) begins in `10`, the path length must satisfy \(t\ge j(v)\). If \(v\) has no `10`, no destination in \(S_n\) is possible at length less than \(n-1\). Every additional balanced multiset of edges decomposes, after discarding directed cycles, into unit paths from distinct sources in \(D_n\) to distinct targets in \(S_n\). Therefore
\[
 E_k\ge\sum_{v\in D_n}j(v).
\]

**3. Sharp disjoint matching.** There is precisely one source without `10`, namely \(v=0^{n-1}1\). Appending \(0^{n-1}\) routes it, in \(n-1\) edges, to the sink \(10^{n-1}\). For any other source, let \(j=j(v)\) and uniquely write
\[
 v=0^a1^b s,\quad a\ge0,\ b\ge1,\ a+b=j,
\]
where \(s\) avoids `010`, starts in `10`, and ends in `01`. The condition \(b\ge1\) follows because a first `10` immediately after a `0` would create `010` across the preceding boundary. Append the word \(1^b0^a\), of length \(j\). The destination
\[
 T(v)=s1^b0^a
\]
begins in `10`, avoids `010`, and does not end in `01`, hence belongs to \(S_n\). Its suffix uniquely recovers \(a\) as the length of its terminal zero-run (possibly zero), and then \(b\) as one less than the immediately preceding one-run length. Removing this suffix recovers \(s\), hence \(v\): the routing map is injective. The exceptional target \(10^{n-1}\), with just one `1`, cannot collide with these images, each of which contains at least three `1` symbols. Because reversal gives \(|D_n|=|S_n|\), the map is a bijection. These paths attain each per-source lower bound simultaneously, so
\[
 E_k=\sum_{v\in D_n}j(v).
\]
The required-edge subgraph is strongly connected: from any allowed vertex, append sufficiently many `1` symbols to reach \(1^n\), then append the target allowed vertex; these operations do not create `010`. Adding the matching paths yields a connected balanced directed multigraph. Its Eulerian circuit is a cover of exactly \(|\mathcal L_k|+E_k\) symbols, proving optimality.

**4. Enumeration.** Let \(S(z)\) count binary words avoiding `010` that begin `10` and end `01`, by their lengths. The four-state overlap automaton with states `00`, `01`, `10`, `11` has adjacency matrix
\[
 M=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&1&0&0\\0&0&1&1\end{pmatrix}.
\]
A direct resolvent calculation gives
\[
 S(z)=z^2\bigl((I-zM)^{-1}\bigr)_{10,01}
 =\frac{z^3(1-z)}{1-2z+z^2-z^3}.
\]
At vertex length \(n\), the no-`10` source contributes \(n-1\), whose generating function is \(z^2/(1-z)^2\). For sources \(0^a1^bs\), the cost \(j=a+b\) has generating function \(\sum_{a\ge0,b\ge1}(a+b)z^{a+b}=z(1+z)/(1-z)^3\). Multiplication by \(S(z)\), followed by the index shift \(k=n+1\), gives the stated rational generating function for \(E_k\). Standard avoidance-automaton counting gives \(A(z)=(1+z^2)/(1-2z+z^2-z^3)\). The asymptotic ratio follows by comparing residues at the simple dominant positive pole \(z=\alpha\); the underlying finite-state automaton is primitive.

**5. Forced forbidden factor.** In an optimal augmentation, every source path must have its individual minimum length. The special source \(0^{n-1}1\) can reach a target beginning `10` in \(n-1\) edges only if the first appended bit is `0`; this first added edge contains `010`, since the source ends in `01`. Thus no optimal covering cycle avoids `010`. The complement map exchanges `010` and `101`, carrying all constructions and lower bounds across unchanged.

## Verification
Run `python3 verify.py` using Python 3 with no nonstandard packages. The program independently enumerates all required factors through \(k=13\), constructs Eulerian cyclic covers from the explicit routing, checks complete cyclic factor coverage, confirms that every optimum host constructed contains `010`, checks the generating-function coefficients, and computes independent minimum-cost bipartite assignments of shortest source-to-sink paths through \(k=10\). Successful output ends in `VERIFY_OK cyclic_hosts_k=3..13 independent_assignment_optimality_k=3..10 generating_function_coefficients=3..13`. These are finite checks, not the proof of the infinite theorem.

## Relationship to prior work
Moreno and Matamala (arXiv:0711.1695, 2007) study lexicographic Eulerian de Bruijn cycles in *periodically admissible* forbidden-factor subshifts. Their precise definition requires the infinite periodic repetition of each required factor itself to avoid the forbidden set. Here every *linearly* `010`-avoiding factor is compulsory, including ones that are not periodically admissible, and repeated/forbidden host factors are permitted; hence their existence and order-selection results do not imply the present shortest-cover formula. Burstein and Kitaev study unavoidable pattern sets and universal cycles, but do not supply this explicit source-to-sink optimum. Earlier formulas for binary languages avoiding the run `111` or a directed triple such as `110` address the other symmetry orbits of binary forbidden triples, not this palindromic orbit, and neither implies its overhead or the forced-violation phenomenon.

## Limitations
The result concerns ordinary linearly admissible binary windows for the single forbidden pattern `010`, its bit complement `101`, and every \(k\ge3\). It does not classify individual optimal covering cycles, joint forbidden sets, or general longer forbidden patterns. The asymptotic constant is exact via an algebraic root, not a statement about arbitrary languages. Mathematical originality has not been independently audited; a differently formulated covering result could already exist outside inspected sources.

## References
- E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695v1, first public version 2007-11-12, https://arxiv.org/pdf/0711.1695.
- A. Burstein and S. Kitaev, *On Unavoidable Sets of Word Patterns*, SIAM Journal on Discrete Mathematics, DOI:10.1137/S0895480104445678.
- H. Z. Q. Chen, S. Kitaev, B. Y. Sun, *Lower Bounds, and Exact Enumeration in Particular Cases, for the Probability of Existence of a Universal Cycle or a Universal Word for a Set of Words*, Mathematics 8(5), 778 (2020), DOI:10.3390/math8050778.
