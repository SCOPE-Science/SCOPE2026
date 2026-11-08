# Scientific assessment: Gauss positivity on Cartesian clique products

## Correctness — PASS

The proof is global in all integers \(d\ge1\) and \(q_i\ge2\), and all real \(h\ge0\). Explicit tensor eigenprojectors prove row conservation and a positive diagonal. On excluded graphs, the exact heat-kernel integral yields a positive nearest-neighbor entry of the Laplacian pseudoinverse: for at least three factors a two-singleton lower bound is strictly positive, and for two factors with larger order at least four a checked quadratic inequality is strictly positive. The asymptotic identity \(hT(h)_{xy}\to-12L^+_{xy}\) then proves eventual negativity. All allowed one-factor cases use the positive scalar filter; all three allowed two-factor cases have positive-coefficient polynomial certificates for every off-diagonal orbit. Exact arithmetic replay confirmed 9 polynomial numerators, 320 kernel entries, 55 row sums, 246 Green identities, 243 strict Green inequalities, and 12 large-step witnesses. The finite tests support but do not prove the universal quantifiers.

## Originality — PASS on inspected evidence, with residual risk

The 2012 Zappavigna--Colaneri--Kirkland--Shorten preprint was inspected through its Padé counterexample and Section 4 sufficient finite-step theorem. Its example is an eight-state directed nilpotent or shifted matrix, not a symmetric Cartesian clique Laplacian; its sufficient conditions do not entail all-step positivity on the specified family. The 2013 Lóczi--Ketcheson preprint treats absolute-monotonicity radii, not exact Cartesian graph characterization. The 2021 Fontan--Altafini preprint describes pseudoinverse sign phenomena without the Padé step classifier. A related published eight-state Markov Padé result was inspected in full and treats a directed pure-birth chain with a different small-step assertion. Recoverable historical graph-filter findings cover cycles, complete multipartite networks and Radau IIA Hamming graphs; their conclusions do not imply the present full classification for the different Gauss filter and independently varying Cartesian clique factors. The four-cycle case is already known and is not separately claimed as new. A differently indexed specialist theorem could still dominate the classification, so publication priority is not independently established.

## Mathematical value — PASS

The theorem identifies the exact topology and factor-order boundary across a natural infinite class of finite product networks. It distinguishes stability and mass conservation from positivity, makes the mixed six-state triangular-prism case explicit, and proves an algebraic Green-function obstruction for **every** excluded product. The exact classification is motivated by structure-preserving heat integration and heterogeneous factor dimensions; it is not an arbitrary enumeration or reparameterized special case.

## Scope and remaining limitations

The result is confined to unit-edge Cartesian products of complete graphs and the exact two-stage Gauss end-step map. No universal finite timestep for excluded graphs, stage positivity, floating-point safety, or other integration method is claimed. The available historical source window is incomplete, and the novelty assessment is bounded rather than a guarantee of global uniqueness.

Self-review: passed. Independent audit: not yet performed.
