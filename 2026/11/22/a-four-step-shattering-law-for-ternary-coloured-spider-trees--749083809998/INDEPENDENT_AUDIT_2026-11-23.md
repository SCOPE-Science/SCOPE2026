# Independent mathematical audit

## correctness

PASS

Two distinct equality queries at one vertex cannot both be positive, so a shattered set has at most one mark per vertex. For a fixed trace on a processed arm suffix the feasible terminal colour set M determines all predecessor choices: a singleton excludes its own colour; otherwise every predecessor colour can differ from some member. The two answers at a marked new vertex intersect those choices with the target singleton or its complement. Taking all masks for all traces, merging equal masks and rejecting any empty mask is exact; any existing impossible trace prevents global shattering. The empty-arm {7} sentinel lets the leaf take any colour. At the actual hub every triple of arm masks is attainable by independent choices of answer strings. A common hub colour, or separate permitted common colours for positive and negative hub answers, is both necessary and sufficient, since arms do not share any other vertices. Thus maximizing separately over weights of the three signatures does not lose information. The independently computed 20 states at length four match the table including its successor columns and all twenty D8-D4 differences of 3. Closure and the equality of whole weight vectors with one constant offset propagate to every later length by the max-plus identity, not by extrapolation. An unqueried vertex costs zero, a mark costs one. Balanced m=1 through 7 gives 4,6,8,10,13,15,17; the four residue classes starting at 4 through 7 then increase by 9 when all arms grow by four, proving the stated ceiling formula for every m>=1. The proof concerns static queries and three colours, not Littlestone dimension or higher-degree trees.

## originality

PASS

Best of checked knowledge, the three-arm gluing law and twenty-state all-triple computation are not covered by the closest prior path theorem or bounded branching obstruction. The ordinary list-colouring feasibility algorithm for a fixed trace is not itself novel.

## value

PASS

A three-arm spider is the first branching subdivision family beyond paths. Its shared hub obstructs naïve addition of three independent path optima. The exact finite-state rule covers every positive triple rather than a short list of examples: each arm has a uniform four-step law, and the balanced family has an explicit dimension at every length. These results quantify a structural shattering deficit in a natural family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
