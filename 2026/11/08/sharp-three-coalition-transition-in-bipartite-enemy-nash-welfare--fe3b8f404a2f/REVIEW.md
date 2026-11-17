# Independent mathematical audit

## correctness

PASS

Given n=2q+4, penalty -n forces each positive-welfare coalition to be a friendship clique because an agent with an enemy has utility at most n-2-n<0. Splitting either identical same-side core pair is suboptimal by strictly beneficial merging, and all peripheral leftovers can be merged; hence optimizer has two core coalitions and at most one peripheral coalition. Its product is (a+1)^(a+2)(b+1)^(b+2)(2q-a-b-1)^(2q-a-b) for residual size >=2. The map f(s)=s log(s-1) is convex for s>=2, giving a vertex maximum; mixed vertices lose to the two-coalition candidate. D(x)=2x log(2x-1)-(2x+4)log(x+1) has D’>0 for x>2 and changes sign between q=8,9. Independent integer calculations verified q=7,8,9,10,80, and the inspected verifier includes unrestricted partitions q=2 and q=3. Strict positive difference gives unique winners as stated; exact threshold 22 agents is family-specific.

## originality

PASS

Pagano–Schlenga primary HTML Sections 2, 3, 6, and appendix distinguish the unrestricted AEG Nash welfare optimization from at-most-two coalition tractability (Theorem 6.1) and at-most-three hardness (Theorem 6.2). Neither supplies the explicit connected bipartite core-periphery family nor its crossover. Other published Resultary matching-edge and odd-cycle formulas treat different signed compatibility graphs; no implication found. Priority remains qualified by possible specialized bipartite friendship-clique product optimizations.

## value

PASS

A connected bipartite enemy graph can have a unique globally welfare-optimal partition using three coalitions even though two are graph-colorable. The sharp 22-agent transition within a natural scalable core-periphery family gives a useful counterexample to inferring optimal coalition count from bipartiteness, with exact formulas not just existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
