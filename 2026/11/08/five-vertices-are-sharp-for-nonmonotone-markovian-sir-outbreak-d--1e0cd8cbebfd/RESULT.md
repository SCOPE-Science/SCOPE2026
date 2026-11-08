# Five vertices are sharp for nonmonotone Markovian SIR outbreak duration

## Finding

Consider the continuous-time Markovian susceptible–infectious–removed (SIR) epidemic with independent rate-\(\beta\) transmissions along infectious–susceptible edges and independent rate-one removals of infectious individuals. Every vertex starts susceptible except a single infectious seed \(s\), and removed vertices never become susceptible again. Write \(D_{G,s}(\beta)\) for the expected time until no infectious individuals remain on a finite undirected simple graph \(G\).

**Theorem.** If \(G\) has at most four vertices, \(D_{G,s}(\beta)\) is nondecreasing for all \(\beta>0\), and is strictly increasing whenever the connected component containing \(s\) contains at least two vertices. At five vertices nonmonotonicity is possible. Specifically, on the five-vertex graph with edge set
\[
E=\{\{0,3\},\{0,4\},\{1,3\},\{1,4\},\{2,3\},\{2,4\},\{3,4\}\},
\]
starting from seed \(s=3\), the duration function is not nondecreasing: at \(\beta=100\),
\[
D_{G,3}(100)=\frac{3233110817579844486927395030461}{1415931898971338608037919183261}
=\frac{137}{60}+\frac{1326298572426638149591240301}{28318637979426772160758383665220}
>\lim_{\beta\to\infty}D_{G,3}(\beta)=\frac{137}{60}.
\]
Thus five vertices are the sharp minimum for this phenomenon among undirected unweighted graphs and one-seed Markovian SIR processes with homogeneous infection and removal rates.

## Assumptions and scope

Graphs are finite, simple, undirected, unweighted and have no self-loops. Transmission along each oriented infectious–susceptible adjacent pair occurs at rate \(\beta\); each infectious individual has an independent exponential lifetime with mean one. The initial state has exactly one infectious vertex and all other vertices susceptible. The stopping time is complete removal of infection, not the time of the last new infection and not the total number infected. The same model with common removal rate \(\gamma>0\) follows by rescaling \(\beta\) by \(\gamma\) and time by \(\gamma^{-1}\).

## Proof

**Exact first-step recursion.** Represent an epidemic state by two disjoint vertex sets \(S\) and \(I\), susceptible and infectious; all vertices outside their union are removed. Let \(F_{S,I}(\beta)\) be the expected remaining infectious lifetime. If \(I=\varnothing\), it is zero. For \(I\ne\varnothing\), let \(m(S,I)\) be the number of oriented edges from \(I\) to \(S\). Conditioning on the first jump of the finite Markov chain yields the exact identity
\[
\bigl(|I|+\beta m(S,I)\bigr)F_{S,I}
=1+\sum_{u\in I}F_{S,I\setminus\{u\}}
+\beta\sum_{\substack{u\in I,\ v\in S\\\{u,v\}\in E}}
F_{S\setminus\{v\},I\cup\{v\}}.
\tag{1}
\]
Each transition strictly decreases \(|S|\) or \(|I|\) without increasing \(|S|\), so a recursion ordered first by susceptible count and then infectious count terminates. Equation (1) therefore defines an exact rational function in \(\beta\), with no numerical linear-system approximation.

**Exhaustive four-vertex certificate.** There are \(2^{\binom n2}\) labeled simple graphs on \(n\) vertices. The standalone program `verify.py` enumerates all of them for \(1\le n\le4\), discards disconnected graphs, and obtains graph isomorphism classes by explicitly minimizing every vertex-permuted edge list. Their connected class counts are, respectively, \(1,1,2,6\), comprising 44 connected labeled graphs before quotienting. For every vertex of every connected representative (33 rooted cases), the program constructs \(F_{S,I}\) by (1), exactly differentiates the seed value and reduces the derivative to a rational expression \(P(\beta)/Q(\beta)\). The exact coefficients of both numerator and denominator polynomials are nonnegative and \(Q\) has at least one positive coefficient. Whenever the component has at least two vertices, \(P\) also has at least one positive coefficient. Consequently \(D'_{G,s}(\beta)>0\) for all \(\beta>0\), simultaneously for each rooted connected graph with \(n\le4\). This is a finite exhaustive and exact polynomial-sign proof, not an inference from sampled parameter values. A disconnected graph reduces to the component containing the initial seed; if that component has one vertex, its expected duration equals one.

**Five-vertex witness.** The seven edges above form three triangles sharing the hub–hub edge, equivalently the join of an edge and three isolated vertices. The same recursion (1), now computed in exact rational arithmetic with \(\beta=100\), gives the displayed fraction. The code performs the strictly positive rational gap check without floating-point comparison.

**Large-transmission limit.** For a connected \(n\)-vertex graph, the probability of a removal before all \(n\) vertices become infected tends to zero as \(\beta\to\infty\). Indeed, fix a rooted spanning tree and expose exponential transmission clocks along its edges. In the hypothetical no-removal process, the completion time is bounded by the sum of \(n-1\) independent rate-\(\beta\) exponentials, whose mean is \((n-1)/\beta\). The probability of any removal before that completion time is at most \(n(n-1)/\beta\). Therefore every vertex is infected before any recovery, in time tending to zero in probability. Assign to each vertex an independent mean-one exponential infectious lifetime at the moment of infection. The extinction time then tends in distribution to the maximum of \(n\) independent mean-one exponentials, whose expectation is the harmonic number \(H_n=\sum_{k=1}^n1/k\). All extinction times are bounded by the sum of these \(n\) independent lifetimes, furnishing uniform integrability, so expectations converge to \(H_n\). For \(n=5\), this is \(H_5=137/60\). The strict comparison with \(D_{G,3}(100)\), continuity of rational \(D_{G,3}\), and \(D_{G,3}(0)=1\) establish the nonmonotonicity and the sharp vertex minimum.

## Verification

Run `python verify.py` from this directory with Python and SymPy. It enumerates the complete small-graph domain, verifies exact polynomial derivative signs for 33 rooted representatives, and derives the exact rational five-vertex witness. For an independent finite-state numerical implementation run `python verify_matrix.py` with NumPy: it constructs the transient generator and solves the 146-state expected-time linear system at the witness parameter. `requirements.txt` lists dependencies. The matrix check is a numerical cross-check, not an infinite-parameter proof. Finite exhaustive enumeration plus exact symbolic derivative signs covers the entire claimed class of at-most-four-vertex graphs.

## Relationship to prior work

Sharkey, Kiss, Wilkinson and Simon [1] develop exact Markovian SIR equations on trees, but do not provide this vertex-minimal nonmonotonicity classification and do not cover the cyclic witness graph. Holme [2] studies nonmonotone epidemic duration in a different discrete-time SIR mechanism with a fixed infectious period, demonstrating that duration-vs-transmissibility paradoxes are not in themselves new; the novelty claimed here is the exact sharp bound and continuous-time five-vertex witness. López-García [3] gives exact finite Markov calculations for small-network SIR duration, including a general duration-computation method; the theorem here is a graph-wide exact parameter-sign classification not stated by that computational framework. Related more recent full Markovian SIR matrix methods [4] also supply general tools but do not imply the sharp minimality without additional enumeration and symbolic signs. No priority or completeness claim is made beyond inspected literature.

## Limitations

The result concerns a homogeneous two-parameter Markovian SIR model, with independent exponential recovery, one initially infectious vertex and an undirected unweighted graph. It does not classify larger graphs, identify the globally strongest nonmonotonicity, cover discrete-time epidemic mechanisms, or predict any real epidemic time scale. The graph-wide four-vertex result uses a reproducible exhaustive symbolic certificate; further independent source searches may uncover equivalent earlier small-graph calculations. An independent mathematical audit has not been performed.

## References

[1] K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson and P. L. Simon, *Exact equations for SIR epidemics on tree graphs*, arXiv:1212.2172 (first public 2012-12-10), https://arxiv.org/abs/1212.2172.

[2] P. Holme, *Extinction times of epidemic outbreaks in networks*, arXiv:1310.3932 (first public 2013-10-15), https://arxiv.org/abs/1310.3932; PLOS ONE 2013, https://doi.org/10.1371/journal.pone.0084429.

[3] M. López-García, *Stochastic descriptors in an SIR epidemic model for heterogeneous individuals in small networks*, *Mathematical Biosciences* 2015, https://doi.org/10.1016/j.mbs.2015.10.010; available manuscript https://eprints.whiterose.ac.uk/id/eprint/91001/1/RevisedManuscript_MLopezGarcia_MBS-D-15-00097.pdf.

[4] T. Achterberg and P. Van Mieghem, *Analytic solution of Markovian epidemics without re-infections on heterogeneous networks*, arXiv:2311.16721, https://arxiv.org/abs/2311.16721.
