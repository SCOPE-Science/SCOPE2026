# Scientific review: exact cone-transfer law for fastest symmetric Markov mixing

## Correctness — PASS

For every finite vertex-transitive core of order \(m\ge2\), the proof decomposes the cone into an apex/constant block and the outer zero-sum block. The nonedge witness supplies the sharp universal lower bound \(\rho(H)\ge1/(m-1)\), making apex probability \(1/m\) compatible with the core optimum. Averaging over base automorphisms proves the reverse inequality for arbitrary, not necessarily invariant, candidate transition matrices. The complete-core and disconnected-core boundaries are explicitly handled. The nontransitive path example is checked by an independent two-mode lower bound and an exact five-by-five characteristic polynomial. The packaged `verify.py` passed 895 exact-rational assertions. Computation is not used as the proof of the general theorem.

## Originality — PASS on inspected evidence, qualified

The 2004 Boyd–Diaconis–Xiao paper establishes convex optimization of SLEM, while the 2007 Boyd–Diaconis–Parrilo–Xiao paper gives the general symmetry mechanism and an exact wheel formula in Section 5.3.3. That wheel identity is already known and is not claimed here. The inspected full-text sections did not supply the all-vertex-transitive core transfer identity, the nonedge argument yielding its universal scaling, or the strict path boundary. The 2006 path paper supplies an existing \(\rho(P_4)\) value, here also proved directly. Semantic searches of accessible research records did not identify the general cone transfer statement. General symmetry-reduction principles do not themselves assert the sharp scalar relation for arbitrary numbers of internal edge orbits. Specialist theses or unindexed records remain a plausible publication-priority risk, not a mathematical proof of novelty.

## Mathematical value — PASS

The exact identity transfers any solved fastest-mixing problem on a vertex-transitive core to its cone without solving a new semidefinite program, including multiple edge-orbit and disconnected cores; the improvement factor is topology-independent. The universal upper bound and explicit path counterexample distinguish when this transfer must not be treated as equality. This is a structural optimization reduction across an unrestricted infinite class, not merely a reparameterization of the published wheel case. The theorem does not settle unknown core optimizations.

## Closest literature and remaining limitations

- Boyd, Diaconis, Xiao (2004), DOI `10.1137/S0036144503423264`: general primal/dual convex FMMC formulation, no specific universal-cone transfer in inspected material.
- Boyd, Diaconis, Parrilo, Xiao (2007), arXiv:0709.0955v1, Section 5.3.3: exactly covers wheel cores, but not the general vertex-transitive-base identity as a stated result.
- Boyd, Diaconis, Sun, Xiao (2006), path theorem: fixes the base optimum in the nontransitive boundary example.

The research comparison is limited by indexing and cannot certify publication priority. Independent mathematical audit is not represented as completed.

Self-review: passed. Independent audit: not yet performed.
