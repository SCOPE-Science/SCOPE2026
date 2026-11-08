# Minimal cubic kinetic site distinguishability on the Frucht graph

## Finding
Let \(F\) be the twelve-vertex Frucht graph with the labeled edges in the next section. Perform monomer random sequential adsorption: inspect its vertices in a uniformly random order, occupy a vertex if and only if none of its already occupied neighbors exists, and otherwise reject that vertex irrevocably. The twelve terminal occupation probabilities are
\[
(\pi_0,\ldots,\pi_{11})=\frac1{17280}(5631,5440,6993,5877,5454,5762,5516,5319,6759,5949,5444,6506).
\]
**All twelve numbers are pairwise different**, although the graph is cubic. The minimum difference between any two is \(1/4320\), and the largest difference is \(31/320\). The terminal number \(X\) of occupied sites obeys
\[
\Pr(X=3)=\frac1{64},\quad \Pr(X=4)=\frac{169}{192},\quad \Pr(X=5)=\frac5{48},\qquad \mathbb E X=\frac{785}{192}.
\]
This is the **smallest possible vertex order of a finite simple cubic graph** whose random-order adsorption process yields pairwise distinct occupation probabilities at all vertices: every cubic graph of order below twelve has a nontrivial automorphism, so at least two vertex probabilities coincide. The last fact is the established classification of the smallest asymmetric cubic graphs, not a newly asserted classification.

## Assumptions and scope
The graph is simple and undirected, with vertex set \(\{0,1,\ldots,11\}\), degree three and exactly eighteen edges:

```python
EDGES = ((0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11))
```

This is a standard Frucht-graph labeling, and matches the same explicit edge set used in an earlier independence-complex classification. All vertices are attempted exactly once. Arrival times may equivalently be independent identically distributed continuous random variables; the induced ordering is uniform. No subsequent retries, removals or diffusion occur. All fractions are exact, not simulation estimates. Vertex indices are tied to this fixed edge labeling; permuting labels permutes the vector entries.

## Proof
For a set \(S\) of as-yet admissible vertices, let \(N[v]\) denote the closed graph neighborhood of \(v\), and define \(S_v=S\setminus N[v]\). Let \(a_i(S)\) be the probability that vertex \(i\) is eventually accepted when the process begins with only vertices of \(S\) available. Let \(W_S(z)=\mathbb E[z^{X_S}]\) be the terminal cardinality generating polynomial. A uniformly random order places each \(v\in S\) first with probability \(1/|S|\); accepting that vertex permanently removes exactly its closed neighborhood from further possible acceptances. Thus
\[
 a_i(\varnothing)=0,\qquad a_i(S)=\frac1{|S|}\sum_{v\in S}\bigl({\bf1}_{i=v}+a_i(S_v)\bigr),
\]
\[
 W_{\varnothing}(z)=1,\qquad W_S(z)=\frac{z}{|S|}\sum_{v\in S} W_{S_v}(z).
\]
These identities follow by conditioning on the earliest admissible vertex and the exchangeability of the residual order. They are terminating recurrences because \(|S_v|<|S|\) for nonempty \(S\). Their exact rational evaluation on the displayed edge set gives the twelve probabilities in the finding and
\[
 W_V(z)=\frac{z^3}{64}+\frac{169z^4}{192}+\frac{5z^5}{48}.
\]
The independent verification below obtains exactly the same fractions by counting all possible random arrival permutations. The twelve integers in the probability vector are distinct: when sorted, their numerators are
\[
5319,5440,5444,5454,5516,5631,5762,5877,5949,6506,6759,6993.
\]
Their smallest successive difference is four, the largest-minus-smallest is \(1674\), and summing the numerators gives \(70650\), proving the quoted minimum gap, range and expectation.

To establish **minimal order**, note that an automorphism \(\sigma\) of any finite graph maps the uniform arrival-order law to itself, hence \(a_{\sigma(i)}(V)=a_i(V)\). Pairwise distinct probabilities therefore force the automorphism group to be trivial. The known exhaustive catalog of cubic identity graphs places the minimum possible order at twelve, with the Frucht graph one of five graphs attaining that order (see the references). The explicit distinct vector above attains this necessary order; this establishes sharpness for all finite simple cubic graphs. No assertion about other regular degrees is made.

## Verification
The standalone standard-library program `verify_frucht_adsorption.py` provides two independent exact methods applied to the embedded edge list. Method A recursively computes \(a_i(S)\) and \(W_S\) by rational arithmetic; only 97 admissible masks are reached. Method B independently loops through all uniformly ordered attempts using integer dynamic programming on pairs \((\text{processed},\text{accepted})\), maintaining exact path multiplicities. It visits all \(12!=479001600\) arrival orders in aggregated form and ends in 31 distinct accepted sets. Each terminal path-count is divided by \(12!\), then the probabilities and polynomial are compared exactly with Method A and the stated answers. The code checks cubic degree, connectivity, distinct numerators, and the sharp gap. Execute `python3 verify_frucht_adsorption.py` with Python 3 and no third-party packages; the expected final line is `FRUCHT_ADSORPTION_CERTIFICATE_OK`.

## Relationship to prior work
Gamarnik and Goldberg (2008) analyze random-order greedy independent sets on general regular graphs through girth bounds, not this complete labeled twelve-site probability vector. Dhara and collaborators (2016) study random sequential adsorption on large sparse random graphs, not this particular asymmetric cubic network. Pippenger (1989) introduced foundational graph RSA, especially regular graphs with few short cycles; the accessible abstract does not contain the stated Frucht-specific calculation. An earlier detailed independent-set topology classification of this same Frucht edge set establishes its independence-complex homotopy type and vertex-deletion types but does not evaluate random-order kinetic occupation laws; topological data alone do not provide the order-dependent probability vector. Other published exact greedy laws for threshold and chain graphs apply to different graph families, not to this triangular cubic graph.

## Limitations
The exact probability vector is proved only for the specified graph, uniform random arrival order, and irreversible one-attempt hard-core monomers. The sharp twelve-vertex minimum relies on the published classification of asymmetric cubic graphs; the attached verifier independently checks the new kinetic calculation, not that classification of every cubic graph. An unindexed old exact RSA table might have computed these fractions before, and the full text of Pippenger's 1989 paper was unavailable, so historical priority is not certified. No external independent audit has been performed.

## References
1. D. Gamarnik and D. A. Goldberg, *Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections*, arXiv:0807.1277v1, first posted 2008-07-08, https://arxiv.org/abs/0807.1277.
2. A. Dhara et al., *Random sequential adsorption on graphs*, arXiv:1604.03918v1, first posted 2016-04-13, https://arxiv.org/abs/1604.03918.
3. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Algebraic and Discrete Methods 10 (1989), doi:10.1137/0402034, https://doi.org/10.1137/0402034.
4. E. W. Weisstein, *Frucht Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/FruchtGraph.html; smallest-cubic-identity-graph attribution to Skiena (1990), p.185.
5. *The Frucht graph independence complex and its complete vertex-deletion classification* (2026), publicly accessible mathematical research record, with the identical 18-edge labeling. Its claim concerns topology of independent-set complexes, not adsorption kinetics.
