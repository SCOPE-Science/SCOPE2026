# Self-review

## Correctness (PASS)

The theorem's assumptions include finite connected simple noncomplete walk-regular base graphs, one unit-weight cone apex, uniform strictly positive scalar screening, and a single *principal* Nyström column. The cone modes are \(0\), \(m+1\), and \(1+\nu_j\). Equal spectral projector diagonals follow from walk-regularity. The complement-Laplacian identity proves \(m-\nu_j\ge0\), with some strict positivity precisely because the base is noncomplete. The rank-one trace gain is \((K^2)_{vv}/K_{vv}=-\partial_\mu\log K_{vv}\), and the exact diagonal ratio has a strictly positive spectral sum. Each contributing derivative term has strictly negative derivative, so the objective difference crosses zero once, with the asserted optimizer sets. Wheel asymptotics follow from the stated analytic Fourier integral and a simple root perturbation. The standalone checker passed 1483 exact symbolic/rational and asymptotic comparison assertions on eleven representative graphs, after being read from its package location. This is corroboration, not the proof of the infinite family.

## Originality (PASS, evidence-qualified)

An overlap check compared both wordings and implications. Gittens–Mahoney's primary 2013 source supplies the generic Nyström sketch and trace objective, but not a uniform-screening, walk-regular-cone optimal-column theorem. Lin–Fardad–Jovanović and Fitch–Leonard analyze grounded/consensus leader selection, primarily without a uniform leakage shift; they do not give this one-crossing spectral formula. The most closely indexed later cone result varies **peripheral edge conductance**, with no uniform diagonal shift. Its summarized theorem therefore does not entail the present statement: after grounding a peripheral vertex, a global shift adds leakage to all remaining vertices and changes off-diagonal/diagonal ratios differently from rescaling peripheral conductance. Its full text was inaccessible, so an equivalent unpublished or differently parameterized theorem remains a real priority risk. The accessible preceding and current mathematical ledgers were checked by recoverable claims only for overlap; no historical work was re-reviewed.

## Value (PASS)

The theorem completely classifies all optimal single-column landmarks for a natural broad family that includes wheels, Cayley graphs and non-vertex-transitive walk-regular bases. It gives a cheap eigenvalue-based threshold test instead of per-node inverse evaluation, proves a strict failure of diagonal-based column selection over an entire regime, and derives a nontrivial positive finite-size correction for wheels. These are relevant structural design facts, not a mere rewording of the generic trace identity. The claim does not extend to irregular graph bases, multiple columns or other matrix losses.

## Limitations and closest literature

See the cited 2013 Nyström and leader-selection works, the 2014 joint-centrality result, and the related indexed graph-cone leader-migration theorem described above. Independent full-text inspection of that indexed cone theorem was unavailable. There is no claim of exhaustive global literature coverage or external proof certification.

Self-review: passed. Independent audit: not yet performed.
