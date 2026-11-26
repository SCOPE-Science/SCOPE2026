# Exact three-orbit jamming law for monomer adsorption on the four-cube

## Finding
On the graph \(Q_4\) whose vertices are the binary four-tuples, join two vertices exactly when their Hamming distance is one. Starting with all sixteen vertices vacant, process the vertices in a uniformly random order, permanently occupying an attempted vertex if and only if none of its neighbors is already occupied. Let \(X\) be the number of occupied vertices at termination. Then
\[
\Pr(X=4)=\frac16,\qquad \Pr(X=5)=\frac{64}{165},\qquad \Pr(X=8)=\frac{49}{110},
\]
and all other outcomes have probability zero. The exact mean is \(\mathbb E X=1018/165\), corresponding to coverage fraction \(509/1320\).

More precisely, the forty-two possible terminal configurations form three orbits under the 384 automorphisms of \(Q_4\). There are twenty-four four-site configurations, sixteen five-site configurations, and two eight-site configurations. Each particular configuration in these respective orbits has probability \(1/144\), \(4/165\), and \(49/220\). The two maximally packed states are the two parity classes. Though only \(2/42=1/21\) of the inclusion-maximal independent sets are maximally packed, random sequential adsorption reaches one with probability \(49/110\).

## Assumptions and scope
The graph is the finite, unweighted, simple sixteen-vertex hypercube \(Q_4\), not an infinite hypercubic lattice or a periodic torus. Each vertex receives one attempt at a distinct, uniformly random priority; equivalently, all attempt times are independent and identically distributed with a continuous common distribution. Each successful monomer blocks its nearest graph neighbors forever. The result concerns terminal occupancy and labelled configurations, without desorption or cooperative effects.

## Proof
**Step 1: process reduction.** At any stage, all currently admissible vertices have a uniformly random relative priority. Therefore the next *successful* attempted vertex is uniform among the admissible vertices, and after accepting it one removes it and its four graph neighbors from the admissible set. This exactly represents the random-order process, even though blocked vertices may have intermediate failed attempts.

**Step 2: first two acceptances.** By vertex transitivity, fix the first accepted vertex as \(0000\). Eleven vertices remain admissible: seven other even-parity vertices and four odd vertices at Hamming distance three from \(0000\). Their three classes, under automorphisms fixing \(0000\), are: one antipode at distance four, six vertices at distance two, and four at distance three. The second accepted vertex is in these classes with probabilities \(1/11\), \(6/11\), and \(4/11\), respectively.

If the antipode is second, the other six even vertices become isolated admissible sites, yielding exactly eight accepted monomers.

If the second vertex is at distance three, the residual six admissible vertices induce the six-cycle \(C_6\). A random greedy process on \(C_6\) chooses any vertex first, leaving an induced three-vertex path; its middle is chosen next with probability \(1/3\) (giving two additional acceptances in total), while an endpoint is chosen first with probability \(2/3\) (giving three). Including the two previously accepted vertices, the final size is four or five with conditional probabilities \(1/3\) and \(2/3\).

If the second vertex is at distance two, the residual eight-vertex induced graph consists of a square with two pendant leaves attached to each of two opposite square vertices. There are four degree-one vertices, two degree-two square vertices and two degree-four square vertices. Choosing a degree-one vertex first leaves an isolated vertex and a four-leaf star. Choosing the star center first, with probability \(1/5\), yields three total residual acceptances; otherwise six, with probability \(4/5\). Choosing a degree-two vertex first leaves five isolated vertices and yields six residual acceptances. Choosing a degree-four vertex first leaves a three-vertex path; it yields two residual acceptances with probability \(1/3\), or three with probability \(2/3\). Thus, conditional on a distance-two second acceptance, the final size including the initial two vertices has distribution
\[
\Pr(X=4\mid d=2)=\frac{2}{8}\frac13=\frac1{12},
\quad
\Pr(X=5\mid d=2)=\frac48\frac15+\frac28\frac23=\frac4{15},
\]
\[
\Pr(X=8\mid d=2)=\frac48\frac45+\frac28=\frac{13}{20}.
\]
Combining the three classes gives
\[
\Pr(X=4)=\frac6{11}\frac1{12}+\frac4{11}\frac13=\frac16,
\]
\[
\Pr(X=5)=\frac6{11}\frac4{15}+\frac4{11}\frac23=\frac{64}{165},
\quad
\Pr(X=8)=\frac1{11}+\frac6{11}\frac{13}{20}=\frac{49}{110}.
\]
These sum to one, proving the complete support and mean.

**Step 3: terminal configurations.** At termination the occupied sites constitute an inclusion-maximal independent set. A set contained in only one parity class is maximal only when that whole eight-vertex class is occupied, giving two size-eight sets. For a mixed independent set, every opposite-parity site must lie at distance three from each selected site of the first parity. Each vertex has exactly four distance-three vertices, all pairwise at distance two. For one, two, three, or four selected sites from these four, the common distance-three options on the opposite parity have cardinalities four, two, one and one. Maximality therefore permits precisely a singleton together with its four distance-three vertices (size five), or two distance-two vertices of each parity (size four). The first family has sixteen labelled sets, each identified by its singleton. For the second, choose two vertices at distance two within the even parity class: there are \(8\cdot6/2=24\) choices, and the two odd common distance-three vertices are then forced. This yields twenty-four sets. Translation and coordinate permutation symmetries act transitively on each family, so dividing the three total probabilities by their respective orbit sizes proves the claimed per-configuration probabilities.

## Verification
Two standalone Python 3 programs using only the standard library are included. Run `python3 verify_available.py` to compute the full exact distribution by a rational recurrence over available-vertex masks and to check each conditional second-choice branch. Run `python3 verify_configurations.py` to construct hypercube adjacency independently by Hamming distance, propagate rational probabilities over the 743 independent-set masks, enumerate all forty-two terminal sets, and verify their three symmetry orbits using the 384 affine coordinate automorphisms. Both checks must print `PASS` and terminate without assertions. The proof above is a separate, finite case decomposition and does not depend on numerical simulation.

## Relationship to prior work
Random sequential adsorption and random greedy independent sets are established processes. Pippenger (1989) studies graph-based sequential adsorption with a focus on regular graphs with few short cycles. Gamarnik and Goldberg (arXiv:0807.1277; 2008) analyze random greedy independent sets on regular graphs, including large-girth expectation bounds and bounded-degree concentration. Dhara, van Leeuwaarden and Mukherjee (arXiv:1604.03918; 2016) study generalized sequential adsorption on Erdős–Rényi graphs. Krivelevich, Mészáros, Michaeli and Shikhelman (2023) treat local-limit asymptotics. These works establish the process and larger-scale tools; the exact finite four-cube distribution and its complete terminal-state probabilities are the specific result here. General algorithms for arbitrary finite graphs can compute such probabilities but do not, by themselves, provide these evaluated constants or the analytic residual-graph classification.

## Limitations
The result is finite, specific to the four-dimensional hypercube with equal independent priorities and nearest-neighbor blocking, and makes no claim about large-dimensional or infinite-volume jamming constants. An earlier exact finite table outside the inspected literature cannot be ruled out; no independent scientific audit has been performed.

## References
1. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401. DOI: https://doi.org/10.1137/0402034.
2. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277 (first posted 2008-07-08); https://arxiv.org/abs/0807.1277.
3. S. Dhara, J. S. H. van Leeuwaarden and D. Mukherjee, *Generalized random sequential adsorption on Erdős–Rényi random graphs*, arXiv:1604.03918 (first posted 2016-04-13); https://arxiv.org/abs/1604.03918.
4. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms (online 2023-12-18); https://doi.org/10.1002/rsa.21200.
