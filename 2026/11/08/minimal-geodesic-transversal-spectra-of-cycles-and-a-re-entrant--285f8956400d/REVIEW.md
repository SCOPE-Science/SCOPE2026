# Scientific review

**Correctness — PASS.** Every maximal geodesic is a cyclic block of \(\lfloor n/2\rfloor+1\) vertices. The exact gap and deletion criteria \(d_i\le L+1\) and \(d_{i-1}+d_i\ge L+2\) restrict minimal transversals to size at most three. A two-gap count and the three-gap deficiency bijection give the coefficients for all \(n\ge3\), including both parity boundaries. Direct shortest-path enumeration and per-subset comparison through \(n=18\) corroborate the independent proof.

**Originality — PASS, provisional.** The 2021 original geodesic-transversal literature and equivalent maximal-shortest-path-cover literature establish the scalar cycle minimum \(2\); they do not, in the inspected relevant statements, present all inclusion-minimal cycle solutions or their count. General circular-arc hitting-set dualization (Elbassioni–Rauf, 2010) gives an enumeration method and a per-arc 2-exact property, not the exact sharp labelled count or purity pattern. Existing analogous ladder results cover the isolated \(C_4\) case but not the cycle family. Exact-scope searches did not identify a stronger statement covering the infinite family. Publication priority remains provisional because inaccessible or differently indexed enumerations could cover it.

**Mathematical value — PASS.** The natural inclusion-minimal, rather than smallest-cardinality, refinement of shortest-path covering has a complete classification. It reveals a striking nonmonotone phenomenon: three-point minimal covers first appear at nine vertices, vanish at ten, then exist for every larger cycle. Their number grows as \(n^3/24\), whereas the already-known optimal two-point covers occur only linearly often. The exceptional purity set is a meaningful structural boundary, not a restatement of the known minimum.

**Scope and risks.** The result is for labelled cycles only. Finite checks are not an infinite proof, and public literature may contain an equivalent circular-arc hitting-set count under different terminology. The independently reviewed status has not been claimed.

Self-review: passed. Independent audit: not yet performed.
