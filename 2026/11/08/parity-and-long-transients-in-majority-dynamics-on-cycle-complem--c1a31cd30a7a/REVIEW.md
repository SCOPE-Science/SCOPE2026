# Self-review

## Correctness — PASS

For odd \(N=2m+1\ge7\), neighbor-majority thresholds reduce the central layer to occurrences of \(000\) and \(010\); cyclic run decomposition gives the exact identity \(K'=m+1-a-b\). Its equality case is uniquely one doubled zero bond (or its complement), giving exactly \(2N+2\) fixed points. All other configurations reach unanimity by two updates. The block initial state establishes sharpness. For even \(N=2m\ge8\), reflection-complement symmetry maintains exact half occupation; strict majority on the cycle complement is then a local minority-of-three rule, with the stated block-expansion recurrence and strictly increasing equal-bond count until a genuine two-cycle. Proof does not extrapolate a finite search. Two independent executable checks from the embedded source files agreed with the analytic statements. No hidden sign or tie convention is used.

## Originality — PASS (qualified)

The general period-two restriction due to Goles–Olivos is not claimed. The May 11, 2014 Benjamini–Chan–O'Donnell–Tamuz–Tan arXiv text (intro/theorems and sections scanned) treats infinite and random-graph phenomena, not odd-cycle-complement fixed points or the explicit slow orbit. The complete accessible 2020 Fountoulakis–Kang–Makai article treats a high-probability outcome for random graphs, not a deterministic worst-case bound on a specified circulant family. Relevant searches did not find exact prior work on majority dynamics of \(\overline{C_N}\). A close prior local-CA result gives a general transient census for radius-one **majority** on cycles. On the even balanced slice the new system is *complemented* local majority, so this prior work partly explains block erosion; it does not supply the odd-order graph census or the global parity assertion without further analysis. This is a nontrivial overlap/routine-corollary risk, not a claim of guaranteed priority. The original 1980 three-page paper was not inspected in full; its general abstract and the 2014 primary citation were checked.

## Value — PASS

This is a structural counterexample to the idea that dense, diameter-two, vertex-transitive graphs must have bounded **worst-case** majority settling time, together with an exact opposite-parity theorem for the same canonical family. The balanced minority-wave mechanism explains the contrast and distinguishes deterministic exceptional configurations from random-graph convergence. The graph family is natural and infinite, and the finding is not an arbitrary parameter slice. No claim of a paper-sized contribution or matching even upper bound is needed.

## Scientific boundaries and risks

The even assertion is a constructed lower bound, not a classification of all even-order orbits. The prior cyclic-majority transient census supplies related erosion facts; priority for the combined graph-complement assertion is not certified. An unindexed exact result could predate this derivation. The finite programs corroborate the proof but cannot certify it for infinitely many graph orders.

Self-review: passed. Independent audit: not yet performed.
