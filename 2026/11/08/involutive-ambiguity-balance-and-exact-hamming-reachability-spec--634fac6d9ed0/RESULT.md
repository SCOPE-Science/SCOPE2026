# Involutive ambiguity balance and exact Hamming reachability spectra for four-valued warrants

## Finding

Fix an integer \(n\geq1\) and let \(V=\{Y,N,B,U\}\) be the four-valued truth lattice, with \(N\) bottom, \(Y\) top and incomparable middle elements \(B\) (contradictory evidence) and \(U\) (unknown evidence). Write \(\wedge\) for its truth-order meet. Let \(\Rightarrow_w\) be the transition-warrant operation defined in the source cited below. For two option assignments \(s,t\in V^n\), let \(\Delta(s,t)=\{i:s_i\ne t_i\}\) and define the warrant

\[
E(s,t)=\bigwedge_{i\in\Delta(s,t)}(s_i\Rightarrow_w t_i),
\qquad \bigwedge\varnothing=Y.
\]

This is the unrestricted **potential-transition** relation on the complete four-valued option product, prior to imposing any physical move relation or feasibility restriction.

For fixed source \(s\), let \(a,b,c,d\) count the coordinates of \(s\) equal to \(Y,N,B,U\), respectively, so that \(a+b+c+d=n\). Define three polynomials whose coefficient of \(z^k\) counts destinations at Hamming distance exactly \(k\): \(D_s\) for warrant \(Y\), \(C_s\) for warrant in \(\{Y,B\}\), and \(P_s\) for warrant in \(\{Y,B,U\}\). Then

\[
\begin{aligned}
D_s(z)&=(1+3z)^b(1+z)^d,\\
C_s(z)&=(1+z)^{a+c}(1+3z)^b(1+2z)^d,\\
P_s(z)&=2C_s(z)-D_s(z).
\end{aligned}
\]

More strongly, at **every source and every Hamming distance**, the number of destinations with exact warrant \(B\) equals the number with exact warrant \(U\). There is a coordinatewise, source-preserving involution that pairs them and preserves the set of changed coordinates. Thus the exact-warrant fiber polynomials are

\[
Y:D_s(z),\qquad B:C_s(z)-D_s(z),\qquad
U:C_s(z)-D_s(z),\qquad N:(1+3z)^n-2C_s(z)+D_s(z).
\]

Summing over all \(4^n\) sources, the global Hamming-distance generating polynomials for exact warrants \(Y,B,U,N\), respectively, are

\[
\begin{aligned}
G_Y(z)&=(4+4z)^n,\\
G_B(z)=G_U(z)&=(4+7z)^n-(4+4z)^n,\\
G_N(z)&=(4+12z)^n-2(4+7z)^n+(4+4z)^n.
\end{aligned}
\]

In particular, for \(0\leq k\leq n\), the number of ordered pairs at distance exactly \(k\) with warrant \(Y,B,U,N\) is

\[
\binom nk4^{n-k}\bigl(4^k,\;7^k-4^k,\;7^k-4^k,\;12^k-2\cdot7^k+4^k\bigr).
\]

Among distinct source/destination pairs, the numbers that qualify as **definite**, **credible**, and **possible** (the nested warrant sets \(\{Y\}\), \(\{Y,B\}\), \(\{Y,B,U\}\)) are, respectively,

\[
8^n-4^n,\qquad 11^n-4^n,\qquad 2\cdot11^n-8^n-4^n.
\]

For uniform sampling of an ordered *distinct* pair from the complete product, the possible-warrant probability is asymptotic to \(2(11/16)^n\) as \(n\to\infty\); the full pair sample size is \(16^n-4^n\).

Finally, exactly \(n+1\) sources have **every possible destination** (including the source itself) in the possible-warrant relation: the all-\(N\) source and the \(n\) sources with precisely one \(U\) and \(n-1\) entries \(N\). The all-\(N\) source is the unique source from which all destinations have credible, or definite, warrant.

## Assumptions and scope

Every ordered pair in \(V^n\times V^n\) is evaluated as a *potential* move; unchanged options do not contribute to the meet. The four-valued input alphabet and the warrant table are exactly those in Kato (2026), version 2, Definitions 2.3–2.4 and 4.1–4.2. In particular, the source-to-destination warrant table (row and column order \(Y,N,B,U\)) is

| Source | to \(Y\) | to \(N\) | to \(B\) | to \(U\) |
| --- | --- | --- | --- | --- |
| \(Y\) | \(Y\) | \(N\) | \(B\) | \(U\) |
| \(N\) | \(Y\) | \(Y\) | \(Y\) | \(Y\) |
| \(B\) | \(B\) | \(N\) | \(B\) | \(U\) |
| \(U\) | \(Y\) | \(U\) | \(B\) | \(U\) |

This theorem makes no claims about actual strategic feasibility, preference relations, restricted unilateral-move graphs or empirical probabilities. Any such restriction can destroy the fiber balance. When \(k=0\), the unique destination at distance zero from each source receives the empty-meet warrant \(Y\); it is included in the generating polynomials but excluded from the distinct-pair totals.

## Proof

**1. Exact local possibilities.** Fix a coordinate of the source, and consider *changed* destinations only. The multiset of its three local warrants is \(\{N,B,U\}\) from source \(Y\), \(\{Y,Y,Y\}\) from \(N\), \(\{B,N,U\}\) from \(B\), and \(\{Y,B,U\}\) from \(U\). An unchanged coordinate contributes the meet identity \(Y\) and weight one.

**2. A distance-preserving involution.** Fix \(s\). Transform each destination coordinate \(t_i\) by exchanging \(B\leftrightarrow U\) if \(s_i=Y\); exchanging \(Y\leftrightarrow U\) if \(s_i=B\); exchanging \(N\leftrightarrow B\) if \(s_i=U\); and doing nothing if \(s_i=N\). This map is an involution, fixes every unchanged coordinate and maps changed coordinates to changed coordinates. Let \(\sigma\) exchange \(B,U\) in the truth lattice while fixing \(Y,N\). Inspection of the four rows shows that the local warrant after transformation is \(\sigma\) of the original local warrant. Because \(\sigma\) is an automorphism of the four-element truth lattice, it preserves finite meets, including the empty meet. Hence \(E(s,\iota_s(t))=\sigma(E(s,t))\), proving the exact \(B\)-versus-\(U\) fiber bijection at every Hamming distance.

**3. Source-conditioned polynomials.** A meet belongs to \(\{Y,B\}\) exactly when every local factor belongs to \(\{Y,B\}\). For source entries \(Y,B\), there is one changed destination giving such a local factor; for \(N\), three; for \(U\), two. Including the unchanged choice yields \(C_s\) as displayed. A meet equals \(Y\) exactly when every changed factor equals \(Y\): the changed-choice counts for sources \(Y,N,B,U\) are \(0,3,0,1\), yielding \(D_s\). The involution implies equal counts for exact warrants \(B\) and \(U\), each \(C_s-D_s\); hence the possible count is \(P_s=2C_s-D_s\). Subtraction from the total \((1+3z)^n\) gives the \(N\) fiber.

**4. Global count and asymptotics.** Summing \(D_s\) over source symbols independently at each coordinate gives one factor \(1+(1+3z)+1+(1+z)=4+4z\). Summing \(C_s\) gives \((1+z)+(1+3z)+(1+z)+(1+2z)=4+7z\). The unrestricted ordered-pair polynomial is \((4+12z)^n\), because there are four choices for an unchanged coordinate pair and twelve for a changed one. This proves all global identities and, after subtracting the \(4^n\) diagonal pairs, the three distinct-pair counts. Dividing the possible count by \(16^n-4^n\) gives the exact uniform-pair probability; its asymptotic equivalence follows because \(8/11<1\) and \(4/11<1\).

**5. Universal sources.** If any source coordinate is \(Y\) or \(B\), a target changing only that coordinate can have local warrant \(N\); hence not all targets are possible. If at least two source coordinates are \(U\), changing one to destination \(B\) and another to destination \(N\) yields local factors \(B,U\), whose meet is \(N\); again universality fails. Conversely, if every coordinate is \(N\) except possibly one \(U\), every changed factor is \(Y\) except possibly one factor in \(\{Y,B,U\}\). No target has warrant \(N\). There are exactly \(n+1\) such sources. For every source other than all \(N\), at least one changed destination gives a factor different from \(Y\), so only all \(N\) has every target definitely warranted. Since a non-\(N\) source also has some destination with local warrant \(U\) or \(N\), the same source is uniquely universally credible.

## Verification

The included `check_reachability.py` implements the four-valued meet and the warrant table directly and compares every ordered source/destination pair with the polynomial formulas, independently of the proof's factorization. It exhaustively checks \(n=1,2,3,4,5\), totaling \(1{,}118{,}480\) ordered pairs. It also verifies the destination involution pair by pair for \(n\leq4\), equality of exact \(B\) and \(U\) fibers for every source/radius through five options, and the universal-source classification. All tests passed in the recorded run. Execute with `python3 check_reachability.py` using the Python 3 standard library.

Finite verification is not a proof for arbitrary \(n\); the uniform formulas and structural claims follow from the proof above.

## Relationship to prior work

Kato's 2026 paper introduces the four-valued transition-warrant table, the graded admissibility sets and their nested hierarchy. The inspected material establishes neither a source-preserving ambiguity-exchange involution nor the source-conditioned Hamming polynomials, aggregate spectral counts, universal-source classification or exponential-density law proved here. A related October 2026 paper on epistemic disturbance in conflict graphs counts absorbing evidence profiles under *monotone evidence accumulation*, a different operation from Kato's changed-option warrant meet; its counts therefore neither determine nor imply these warrant spectra. The counting method uses elementary finite combinatorics, which is not asserted to be new.

A complete historical-priority certification is not claimed. The motivating source was inspected in accessible HTML sections, but subsequent requests for the remaining full text failed; that access limitation leaves a residual coverage risk. Unindexed equivalent results on finite-valued transition systems may exist.

## Limitations

The formulas apply only to the full, unconstrained four-valued product and the specified warrant table, not to arbitrary transition graphs or reduced and catastrophe-excluding state spaces. The equal-frequency phenomenon need not persist under non-symmetric choice of actual moves. The asymptotic is a combinatorial density under uniform counting, not a behavioral probability model. No independent mathematical audit has been performed.

## References

- Yukiko Kato, *A Four-Valued Graph Model for Conflict Resolution: Core Framework and a Machine-Checked Formalization in Lean 4*, arXiv:2609.11174, first posted 2026-09-10; version 2, 2026-09-11. https://arxiv.org/abs/2609.11174 and https://arxiv.org/html/2609.11174v2.
- Rowan Brad Quni-Gudzinas, *Epistemic Disturbance in the Graph Model for Conflict Resolution: State-Preserving Actions, Four-Valued Assessments, and the Distinction between Capability and Intention*, posted 2026-10-09. https://qnfo.org/papers/epistemic-disturbance-in-the-graph-model-for-conflict-resolution-state-preservin.
