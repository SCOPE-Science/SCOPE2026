# Independent mathematical audit

## correctness

PASS

With synchronous independent sender attempts, the size-2-side start has J~Bin(b,1/b) first-round successes; conditional on J=j>0 the last A vertex is forced surely and each remaining B vertex with probability (j+1)/b. The other start has J~Bin(2,1/2), with the conditional factors 2/b and 1-(1-2/b)^2, respectively. No singleton finishes at round one. For the strict comparison I checked the central single-term lower bounds against (3/4)(4/b)^(b-1): the even comparison ratio exceeds 1 at m=7 and the odd at m=8, and their consecutive ratios exceed 1 on the respective ranges. Independently computed the full finite remainder b=3..15 exactly and enumerated every directed-attempt outcome through two rounds for both starts at b=3..6 (b=3 gives 37/81 vs. 34/81). For the tail, a descendant with x=1,y>0 has zero hold probability; with x=2 and w white B vertices the hold probability is ((w-1)/b)^(2w), zero at w=1 and bounded by 1/16 for 2<=w<b/2 or by e^(-2) for w>=b/2. This is strictly below both initial holds, 1/4 and (1-1/b)^b (the latter increases with b and is already 8/27 at b=3). Monotone counts give a triangular descendant transient matrix, hence descendant absorption has a strictly smaller exponential tail. The geometric holding time G is independent of the residual H; conditioning on H gives the normalized survival limit E[lambda^(-H)], finite and positive. This proves both equivalent asymptotics and the eventual reversed ordering. b=2 is symmetric.

## originality

PASS

The transition mechanism is already known. The supported distinction is the strict ordering for every b>=3 at round two and the exact reverse late-time exponential comparison for the same two singleton-start laws. No equivalent or dominating evaluated conclusion was identified in the inspected sources.

## value

PASS

The two symmetric seed classes are the natural comparison left by the complete-bipartite expected-time literature. The theorem rules out stochastic dominance throughout a nontrivial infinite family, even though a fixed time horizon strongly favors one seed class; the sharp survival bases explain why that ranking fails. This is information the natural mean comparison cannot supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
