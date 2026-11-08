# Scientific review

**Correctness (C): PASS.** The result has a finite domain of exactly \(255\) nonempty subsets of the eight binary three-words. The optimal-length Hamilton-path recurrence and the worst legal greedy-merger recurrence exhaust their spaces exactly. Separate direct-string and original-endpoint-path greedy dynamic programs, permutation and Held–Karp optimum computations, and an independently written C++ implementation agreed on all \(255\) rows. The four maximizing cases were also checked by explicit optimal and legal greedy witnesses. Finite exhaustion proves this particular finite statement; it is not an extrapolation to other input lengths.

**Originality (O): PASS, with priority risk.** The closest 2026 paper proves \(\rho_3=9/5\) allowing arbitrary alphabets, which does not imply the exact fixed-binary ratio or classify binary equality cases. The 2019 work treats more general superstring algorithms and gives weaker length-three bounds; the 2026 disproof uses even input lengths beginning at ten. Searches for the exact ratio, binary length-three aliases, and equivalence through substring/overlap graph formulations identified no covering publication or recorded claim. Unindexed exhaustive calculations remain a risk; priority is not certified.

**Value (V): PASS.** Fixed alphabet size is a mathematical restriction central to practical short-read reconstruction and to understanding the worst-case greedy approximation gap. The binary alphabet is the first nonunary case; length three is the first nontrivial regime singled out by recent sharp unrestricted results. The exact constant and single-orbit equality classification are a natural smallest-alphabet benchmark for subsequent fixed-alphabet studies, not an arbitrary parameter slice. The improvement is qualitative: the binary sharp ratio \(10/7\) is strictly below the unrestricted \(9/5\), and the extremal sources are completely characterized.

The closest literature is listed in `RESULT.md`. The finite range, possible unindexed prior enumerations, and lack of independent mathematical validation are material limits.

Self-review: passed. Independent audit: not yet performed.
