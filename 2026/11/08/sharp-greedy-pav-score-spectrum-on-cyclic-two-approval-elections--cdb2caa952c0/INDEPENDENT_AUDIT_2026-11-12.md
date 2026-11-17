# Independent mathematical audit

## correctness

PASS

For n>=3, each voter approves adjacent candidates and F(W)=2k-A(W)/2, with A the number of adjacent selected pairs. The optimum has A*=max(0,2k-n) and is realizable. Marginal 2-d_W(i)/2 forces greedy to a maximal independent set M of size m between ceil(n/3) and floor(n/2); all such m occur as cycle gap patterns of lengths one/two. Subsequently n-2m selected steps have one new adjacency and m have two, yielding A_g-A*=max(0,min(k,n-k)-m) and full half-step loss spectrum. Ratio F_g/F*>=11/12, equality precisely n multiple six and k=n/2. Independent full-tie direct voter enumeration corroborates n=3..11 but the all-n proof is the gap argument.

## originality

PASS

Best-of-knowledge original under actual inspected statements; significant access or historical-priority risks are explicitly retained.

## value

PASS

A complete exact greedy tie-breaking welfare spectrum and sharp worst-case ratio on the natural degree-two cycle-incidence election model is a nontrivial structural invariant distinct from computing optimum PAV, with concrete relevance to welfare guarantees and tie sensitivity. Independent domination size alone does not specify the score sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
