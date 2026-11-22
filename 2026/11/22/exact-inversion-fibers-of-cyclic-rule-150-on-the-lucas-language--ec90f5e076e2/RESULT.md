# Exact inversion fibers of cyclic Rule 150 on the Lucas language

## Finding
Fix an integer \(n\ge3\). Write \(\mathcal L_n\) for the indexed binary words \(x=(x_0,\ldots,x_{n-1})\) having no adjacent ones cyclically, and apply the synchronous additive cellular automaton
\[
(T_nx)_i=x_{i-1}\oplus x_i\oplus x_{i+1},\qquad i\in\mathbb Z/n\mathbb Z.
\]
Only the **input** is constrained. Let \(N_j(n)\) be the number of distinct outputs with exactly \(j\) preimages in \(\mathcal L_n\), ignoring unattainable outputs. Define Lucas numbers by \(L_0=2\), \(L_1=1\), \(L_{k+2}=L_{k+1}+L_k\).

If \(3\nmid n\), the map \(T_n\) is injective on \(\mathcal L_n\): \(N_1(n)=L_n\), all other positive-fiber counts vanish. If \(n=3m\), the **entire positive-fiber spectrum** is
\[
N_3(n)=1,\qquad N_2(n)=3(2^{m-1}-1),\qquad
N_1(n)=L_n-3\cdot2^m+3.
\]
The unique triple-predecessor output is the all-one word \(1^n\), with three predecessors \((001)^m,(010)^m,(100)^m\). In particular,
\[
|T_n(\mathcal L_n)|=L_n-3\cdot2^{m-1}+1.
\]
For a uniform input in \(\mathcal L_n\), the minimum average zero-one decoding error from one output is \((3\cdot2^{m-1}-1)/L_n\), and its conditional Shannon entropy in bits is
\[
H(X\mid T_nX)=\frac{6(2^{m-1}-1)+3\log_2 3}{L_n}
\]
when \(3\mid n\), while both quantities vanish otherwise.

For **every positive number of updates** \(t\), the same complete fiber spectrum holds for \(T_n^t\) if \(n\) is odd; for \(3\nmid n\), the map is invertible on the entire unrestricted binary state space, regardless of parity. If \(6\mid n\), a new input collision occurs already at the second update: \(0^n\) and \((101000)^{n/6}\) have different first-step images but the same second-step image \(0^n\).

## Assumptions and scope
The symbols \(0\) and \(1\) are named, positions are indexed, and cyclic rotation is **not** factored out. Neighbors are indexed modulo \(n\). The source language forbids cyclic `11`, including the pair at positions \(n-1,0\). The output belongs to the entire \(\{0,1\}^n\); one never reapplies the input constraint between updates. The assertions require \(n\ge3\). The formula counts only outputs with a positive number of admissible source predecessors.

## Proof
**1. The linear kernel.** Over \(\mathbb F_2\), a kernel word \(h\) must obey \(h_{i+1}=h_i+h_{i-1}\), whence \(h_{i+3}=h_i\). On an \(n\)-cycle, a nonzero solution exists exactly when \(3\mid n\). In that case the kernel has four elements: the zero word and the three period-three repetitions of `011`, `101`, `110`. This also proves global injectivity when \(3\nmid n\).

**2. Pair collisions.** Suppose \(n=3m\) and put \(a=(011)^m\). To have both \(x\) and \(x\oplus a\) in \(\mathcal L_n\), the pair of coordinates at indices \(3j+1,3j+2\) must be unequal for each \(j\), because both bits are flipped and neither input may contain neighboring ones. Also \(x_{3j}=0\): the next coordinate \(3j+1\) is one in exactly one of the two words, while \(x_{3j}\) is unchanged. Conversely, the independently chosen blocks `001` or `010` satisfy both requirements, including across block boundaries. Thus exactly \(2^m\) valid inputs have an admissible partner at difference \(a\), forming \(2^{m-1}\) unordered pairs. Rotating the argument gives the same count for each of the three nonzero kernel words.

**3. Triple fibers and enumeration.** A source participating in collisions for two distinct nonzero kernel differences must satisfy both corresponding zero-coordinate conditions. For example, differences \((011)^m\) and \((101)^m\) force the source to be \((001)^m\), and the three corresponding admissible words \((001)^m,(010)^m,(100)^m\) comprise its fiber. The fourth coset word \(1^n\) is inadmissible. Symmetry shows this is the only triple fiber, and no fiber has four admissible words. All three source words map to \(1^n\). The sum of counts of unordered colliding pairs over kernel differences is \(3\cdot2^{m-1}\); the triple fiber contributes three pairs, hence there are \(3(2^{m-1}-1)\) doubleton fibers. The standard two-state adjacency transfer for cyclic words forbidding `11` has trace \(L_n\), so \(|\mathcal L_n|=L_n\). Subtracting two sources for each doubleton and three for the triple proves \(N_1(n)=L_n-3\cdot2^m+3\), and summing positive fibers proves the image formula.

For a uniform source, the output distribution assigns mass \(j/L_n\) to every output with \(j\) predecessors. Each output admits exactly one correct deterministic guess, giving success probability \(|T_n(\mathcal L_n)|/L_n\). Each source in a \(j\)-fiber has posterior entropy \(\log_2j\), proving the stated error and entropy expressions.

**4. Temporal rigidity and the second-step boundary.** Identify a binary ring configuration with a residue class in \(\mathbb F_2[z]/(z^n-1)\). Up to the invertible cyclic shift, \(T_n\) is multiplication by \(p(z)=1+z+z^2\). If \(3\nmid n\), this polynomial is coprime to \(z^n-1\), so \(T_n\) is invertible. If \(n\) is odd, the polynomial \(z^n-1\) is square-free in characteristic two (its derivative is \(z^{n-1}\)). Therefore \(\gcd(p(z)^t,z^n-1)=\gcd(p(z),z^n-1)\) for all \(t\ge1\), and \(\ker T_n^t=\ker T_n\). Equality of two time-\(t\) outputs is thus equivalent to equality of their time-one outputs, on any source subset. Finally, \(T_n^2x\) has coordinates \(x_{i-2}\oplus x_i\oplus x_{i+2}\). For \(n\) divisible by six, the cyclically admissible repeated block `101000` has \(T_n^2(101000)^{n/6}=0^n\) but \(T_n(101000)^{n/6}\ne0^n\), by direct substitution in the local recurrence. This proves a genuinely new collision at update two.

## Verification
Run `python3 verify_rule150.py` with Python 3 and no third-party dependencies. The checker exhaustively enumerates all cyclically admissible binary words at every length \(3\le n\le18\), verifies the entire positive-fiber histogram against the formulas, and compares a list-of-bits automaton implementation against an independently implemented integer bit-shift version on each admissible input. It additionally tests odd-length repeated-update stability, full invertibility at lengths not divisible by three, and explicit second-step witnesses at lengths \(6,12,18,24\). Observed output: `VERIFY_OK exact_lengths=16 iterate_cases=45 second_step_witnesses=4`. Exhaustion through length eighteen is not claimed as proof for all lengths; the algebraic and combinatorial arguments above supply that proof.

## Relationship to prior work
Claussen (arXiv:math/0410429, posted October 19, 2004) studies Rule 150 and its polynomial update in the unconstrained infinite-lattice single-seed setting, not the source-restricted finite cyclic inversion spectrum. Codara and D'Antona (arXiv:1210.5561, posted October 19, 2012) treat independent sets and Lucas cubes, including counting and containment, without the Rule-150 observation map. Hernández Encinas and Martín del Rey (2007) analyze inverse formulas under cyclic boundary conditions for unrestricted automata; their existence and subject are verified, but their full paper was not available for an exact claim-by-claim comparison. A publicly indexed study entitled *The exact inverse-degree spectrum of cyclic Rule 150 necklaces* addresses unconstrained necklace predecessors modulo rotation, rather than indexed cyclic-independent-set inputs, and no derivation of the present constrained counts could be established from its accessible summary. The present theorem is an intersection-and-fiber classification for an explicitly constrained source, not a claim of a new unrestricted kernel or a new definition of Lucas cubes.

## Limitations
The complete fiber formulas apply to one step on arbitrary ring sizes, and to all positive times on odd ring sizes. On even multiples of three, the proof identifies the **first** later-time information-loss event, but does not classify all later-time fibers. No noise, asynchronous updates, rotation quotient, or constraints on post-update states are included. Prior published work may already contain an equivalent source-conditioned corollary under another formulation; in particular, the full cyclic inverse-rule article was not accessible for inspection. Independent mathematical validation has not been performed.

## References
- J. C. Claussen, *Time-evolution of the Rule 150 cellular automaton activity from a Fibonacci iteration*, arXiv:math/0410429v1, publicly posted 2004-10-19, https://arxiv.org/abs/math/0410429 .
- P. Codara and O. M. D'Antona, *On the independent subsets of powers of paths and cycles*, arXiv:1210.5561v1, publicly posted 2012-10-19, https://arxiv.org/abs/1210.5561 .
- L. Hernández Encinas and Á. Martín del Rey, *Inverse rules of ECA with rule number 150*, Applied Mathematics and Computation 189 (2007), 1782–1786, https://doi.org/10.1016/j.amc.2006.12.058 .
- *The exact inverse-degree spectrum of cyclic Rule 150 necklaces*, publicly indexed research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-exact-inverse-degree-spectrum-of-cyclic-rule-150-necklaces--89cc648da7e1 (only its accessible index summary was inspected).
