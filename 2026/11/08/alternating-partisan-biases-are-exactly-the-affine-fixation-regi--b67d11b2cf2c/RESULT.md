# Alternating partisan biases are exactly the affine-fixation regime on a connected network

## Finding

**Theorem.** For every finite, connected, undirected, unweighted, simple graph \(G=(V,E)\) with at least two vertices and every vector of site preferences \((h_i)_{i\in V}\in(-1,1)^V\), consider the continuous-time partisan voter model defined below. Let \(u(s)\) be the probability of eventual all-\(+1\) consensus from opinion assignment \(s\in\{-1,+1\}^V\). Then the following statements are equivalent:

1. \(u(s)\) is affine in all the initial spins: there exist real \(c,a_i\) such that \(u(s)=c+\sum_i a_i s_i\) for every configuration.
2. Every edge joins exactly cancelling preferences: \(h_i+h_j=0\) for all \(\{i,j\}\in E\).

Whenever either condition holds, the *unique* affine expression is
\[
u(s)=\frac{\sum_{i\in V}\deg(i)(1+s_i)}{4|E|}=\frac{\sum_{i:s_i=+1}\deg(i)}{2|E|}.
\]
Consequently, for any connected bipartite graph \(G=A\sqcup B\) and any \(t\in(-1,1)\), assigning \(h_i=t\) on \(A\) and \(h_i=-t\) on \(B\) leaves every initial-state fixation probability *exactly independent of* \(t\). If the graph is nonbipartite, the only preference vector with affine fixation probabilities is \(h_i=0\) at every vertex. For \(K_{a,b}\) with initial fractions \(x,y\) of positive spins in its respective parts, this fixation probability is \((x+y)/2\) for all \(a,b\ge1\) and all \(|t|<1\).

## Assumptions and scope

Each vertex \(i\) has an independent rate-one exponential update clock. When it rings, vertex \(i\) selects one neighbor \(j\) uniformly. If their spins agree, no change occurs. Otherwise \(i\) copies \(j\)'s opinion with probability \((1+h_i s_j)/2\). Equivalently, a directed discordant pair \(i\leftarrow j\) generates an opinion-flip transition at rate \((1+h_i s_j)/(2\deg(i))\). All preferences are fixed over time, \(|h_i|<1\), and the graph is finite, simple, undirected, and connected. "Affine" means degree at most one on the full hypercube in the spin variables, not merely at one particular initial configuration or as a function of the aggregate magnetization.

Every discordant directed pair has strictly positive transition rate. From any non-consensus configuration a finite sequence of positive-rate flips along a spanning tree can reach a unanimous state; hence on this finite-state chain absorption in one of the two unanimous states occurs almost surely, and the hitting probability \(u\) is the unique function harmonic at every transient state with boundary values zero and one at the negative and positive consensus states.

## Proof

Let an arbitrary affine function be \(f(s)=c+\sum_{i\in V} a_i s_i\), and let \(d_i=a_i/\deg(i)\), which is defined because every vertex has positive degree. Directly applying the Markov generator to the directed update \(i\leftarrow j\), and collecting the two directed orientations of each undirected edge \(\{i,j\}\), yields the *exact identity* on all spin configurations:
\[
\mathcal L f(s)=\frac12\sum_{\{i,j\}\in E}\left[(d_i-d_j)(s_j-s_i)+(d_i h_i+d_j h_j)(1-s_i s_j)\right]. \tag{1}
\]
Indeed, the first oriented contribution is \(a_i(s_j-s_i)(1+h_i s_j)/(2\deg(i))\) and the reverse orientation is the same expression with \(i,j\) exchanged; use \(s_i^2=s_j^2=1\).

**Necessity.** Suppose \(f=u\) is affine. Its generator vanishes at every non-consensus configuration and also at both absorbing consensus configurations (where every summand vanishes). Consequently expression (1) vanishes as a function on the entire hypercube. The Walsh monomials \(1\), \(s_i\), and \(s_i s_j\) for distinct edges are linearly independent. The coefficient of the monomial \(s_i s_j\) in (1) is \(-(d_i h_i+d_j h_j)/2\); hence \(d_i h_i+d_j h_j=0\) for every edge. The coefficient of \(s_i\) is \(\frac12\sum_{j\sim i}(d_j-d_i)\), giving a harmonic function of the vertices. Since the finite graph is connected, the discrete maximum principle forces every \(d_i=d\), a common constant. Evaluating the affine expression at all-plus and all-minus gives \(c=1/2\) and \(\sum_i a_i=1/2\). As \(\sum_i\deg(i)=2|E|\), the common value is \(d=1/(4|E|)>0\). Thus \(h_i+h_j=0\) for all edges, and substitution fixes the displayed \(u\) uniquely.

**Sufficiency.** Assume the edge-cancellation condition. Take \(c=1/2\) and \(a_i=\deg(i)/(4|E|)\). Then \(d_i=1/(4|E|)\) is constant, and both bracketed terms of (1) vanish on every edge for every spin assignment. Therefore \(f\) is harmonic. Its all-minus and all-plus values are respectively \(0\) and \(1\); uniqueness of the finite absorbing Dirichlet problem (or optional stopping for the bounded martingale \(f(s(t))\)) proves \(f=u\).

Finally, on a connected bipartite graph the relation \(h_i=-h_j\) propagates along all paths, so one bipartition has constant \(t\) and the other \(-t\). On a connected graph with an odd cycle this relation forces \(t=-t\), hence \(t=0\), and then every vertex has zero preference by connectedness. In \(K_{a,b}\), vertices in the first and second parts have respective degrees \(b\) and \(a\). Thus their total contribution to the normalized degree weight is \(abx+aby\) divided by \(2ab\), proving the last assertion.

## Verification

The accompanying `verify.py` is a standard-library Python 3 script. Run `python3 verify.py` from the directory containing this document. It enumerates all \(771\) connected labeled simple graphs with \(2\) through \(5\) vertices; for multiple rational bias assignments it checks the exact generator identity against the independently implemented transition generator for every spin assignment and tests edge cancellation versus harmonicity, totaling \(54{,}452\) generator assertions. It also solves the full transient absorbing Markov-chain linear systems over rational numbers on seven representative graph topologies, obtaining \(18\) independent exact fixation-law checks. Successful execution prints `VERIFY_OK graphs=771 generator_assertions=54452 exact_absorption_chains=18`.

The finite enumeration is *not* a substitute for the preceding all-graph proof. The graph family and parameters in the theorem are infinite; their quantifiers follow from the generator/Walsh/maximum-principle argument, not from computational samples.

## Relationship to prior work

Site-dependent preference voter dynamics and its flip-rate normalization are modeled by Zimmaro, Contucci and Kertész (2023, arXiv:2303.09587), which investigates deterministic and stochastic effects of opposing preferences on modular graphs through mean-field and pair approximations. Masuda and Redner (2011, arXiv:1012.2462) study partisan voting predominantly through well-mixed mean-field analysis. Llabrés, San Miguel and Toral (2023, arXiv:2301.09563) analyze stochastic exit probabilities and times on fully connected networks using an adiabatic approximation. Sood, Antal and Redner (2008) prove degree-weighted conservation and an exact bipartite formula for the *unbiased* voter model. These results motivate, but do not state, the all-graph if-and-only-if criterion for *nonzero site-specific partisan preferences* and preservation of their fixation probabilities on every bipartite graph.

The related 2026 paper by Llabrés, San Miguel and Toral (arXiv:2606.05062) treats local active-link ordering using network pair approximations, not the stated exact absorption Dirichlet problem. A full-text comparison for that 2026 paper was unavailable, and an independently established priority judgment is not claimed.

## Limitations

The result requires undirected edges, uniform neighbor choice, equal site update clock rates, fixed preferences strictly in \((-1,1)\), and finite connected networks. At maximal preference magnitude one, additional absorbing configurations may appear and the proof's absorption argument need not apply. Directed, edge-weighted, nonlinear, and zealot-driven models are not covered. The characterization identifies exactly *affine* fixation laws, not the full nonlinear fixation probabilities when edge-cancellation fails, and does not determine mean absorption times or quasi-stationary distributions. Prior-literature searches cannot exclude all unindexed equivalent statements; no independent external audit or formal-machine proof is claimed.

## References

1. F. Zimmaro, P. Contucci, J. Kertész, "Voter-like dynamics with conflicting preferences on modular networks" (2023), arXiv:2303.09587v1, https://arxiv.org/abs/2303.09587 (first publicly posted 2023-03-16; MSC2020 91D30).
2. J. Llabrés, M. San Miguel, R. Toral, "Partisan Voter Model: Stochastic description and noise-induced transitions" (2023), arXiv:2301.09563, https://arxiv.org/abs/2301.09563.
3. N. Masuda, S. Redner, "Can partisan voting lead to truth?" (2011), arXiv:1012.2462; https://sites.santafe.edu/~redner/pubs/pdf/truth.pdf.
4. V. Sood, T. Antal, S. Redner, "Voter Models on Heterogeneous Networks" (2008), Physical Review E 77, 041121, https://pmc.ncbi.nlm.nih.gov/articles/PMC2471880/.
5. N. Masuda, N. Gibert, S. Redner, "Heterogeneous voter models" (2010), arXiv:1003.0768, https://arxiv.org/abs/1003.0768.
6. J. Llabrés, M. San Miguel, R. Toral, "Partisan voter model on complex networks: Dynamics of local ordering" (2026), arXiv:2606.05062, https://arxiv.org/abs/2606.05062.
