# Ninth-degree spin sectors and an entropy gap in majority dynamics on generalized Petersen graphs

## Finding
For every integer \(n\ge5\), let \(G_n=GP(n,2)\) be the labelled generalized Petersen graph with vertices \(u_i,v_i\), \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). Under synchronous binary open-neighbor majority, every vertex adopts the opinion shared by at least two of its three neighbors. Let \(F_n\) count the configurations fixed after one update, with no spatial identifications.

Define the two ninth-degree polynomials
\[
 p_+(t)=t^9-t^8-t^7-t^4+2t^3+1,\qquad
 p_-(t)=t^9-t^8-t^7+2t^6-t^4-1.
\]
If \(\mathcal Z_+\) and \(\mathcal Z_-\) denote their multisets of complex roots, counted with algebraic multiplicity, then the **complete all-size fixed-state census** is
\[
 \boxed{F_n=2+\sum_{\lambda\in\mathcal Z_+}\lambda^n+\sum_{\mu\in\mathcal Z_-}\mu^n}\qquad(n\ge5).
\]
In particular, the number of nontrivial unordered matching cuts of \(G_n\) is \((F_n-2)/2\). For \(n=5,6,7,8,9,10\), the fixed-state counts are respectively \(14,14,32,48,76,118\).

The exponential growth constant \(\alpha\) is the Perron root of the uniquely largest recurrent transfer component, and belongs to \(\mathcal Z_+\). It obeys the **rigorous bounds**
\[
 1.56485<\alpha<1.56486,\qquad
 F_n=\alpha^n(1+o(1)).
\]
For comparison, the ordinary cubic prism \(GP(n,1)=C_n\square K_2\) has exactly
\[
 F_n^{\rm prism}=L_n+2+2\cos(n\pi/3),
 \qquad L_0=2,\ L_1=1,\ L_{m+2}=L_{m+1}+L_m,
\]
so \(F_n^{\rm prism}\sim\varphi^n\), where \(\varphi=(1+\sqrt5)/2\). Thus the same-degree, same-order graph change from internal step one to step two produces an **exponential equilibrium deficit**:
\[
 \boxed{\frac{F_n}{F_n^{\rm prism}}=(\alpha/\varphi)^n(1+o(1)),\quad
 0<\alpha/\varphi<1.}
\]
The entropy per vertex of stable majority configurations drops from \(\tfrac12\log\varphi\) to \(\tfrac12\log\alpha\).

## Assumptions and scope
All graphs are finite, simple, undirected, with the displayed fixed vertex labels. The condition \(n\ge5\) ensures that \(v_{i-2}\) and \(v_{i+2}\) are distinct neighbors. Both colors are counted as distinct; no quotient by graph automorphisms or global color reversal is taken. A nontrivial matching cut is a nonempty, non-full vertex bipartition whose crossing edge set is a matching, with the two sides unordered. In a cubic graph a coloring is majority-fixed precisely when each vertex has at most one opposite-colored neighbor. The all-one and all-zero colorings account for the two colorings without a nontrivial matching cut. The statements concern fixed points only, not the entire periodic or transient dynamics.

## Proof
**1. Exact local constraint and transfer.** Encode column \(i\) by \(c_i=2x_i+y_i\in\{0,1,2,3\}\), where \(x_i\) is the bit at \(u_i\) and \(y_i\) is the bit at \(v_i\). For any five consecutive columns \((a,b,c,d,e)\), define \(o(j)=\lfloor j/2\rfloor\), \(h(j)=j\bmod 2\), and admit the window if
\[
 [o(b)=o(c)]+[o(d)=o(c)]+[h(c)=o(c)]\ge2
\]
and
\[
 [h(a)=h(c)]+[h(e)=h(c)]+[o(c)=h(c)]\ge2.
\]
Here brackets are Boolean indicators. Construct the explicit \(256\)-state directed transfer matrix \(T\), whose states are four-symbol blocks \((a,b,c,d)\), and whose transition to \((b,c,d,e)\) is one exactly when the above five-symbol window is admitted; all other entries are zero. A labelled length-\(n\) configuration gives one length-\(n\) closed walk with the starting position fixed. Conversely a closed walk yields one cyclic column word satisfying every majority condition. The windows use exactly the five specified positions, even when \(n=5\), so for every \(n\ge5\),
\[
 F_n=\operatorname{tr}(T^n).
\]
This is a bijection of finite combinatorial objects, not an asymptotic approximation.

**2. Full finite transfer reduction.** Direct symbolic construction from the two displayed inequalities produces precisely \(320\) directed edges. Strongly connected component decomposition finds one \(24\)-state component \(B\), two separate one-vertex loop components (the two uniformly opposite-colored shores), and \(230\) other singleton components with no loop. No closed walk can traverse an acyclic component. Consequently
\[
 F_n=2+\operatorname{tr}(B^n).
\]
These component assertions are checked by exhaustive \(256\)-state graph construction and Tarjan decomposition in `verify_spectrum.py`; the entire finite algorithm is included.

**3. Complement-sector factorization.** Complementing every bit of every column induces a fixed-point-free involution on the \(24\)-state component and commutes with \(B\). Choose one representative from each of its \(12\) two-element pairs. On the symmetric and antisymmetric subspaces, \(B\) becomes two explicit \(12\times12\) integer matrices \(B_+\) and \(B_-\), given by
\[
 (B_\pm)_{ab}=B_{a,b}\pm B_{a,\bar b},
\]
with \(a,b\) chosen representatives and \(\bar b\) the bit complement. Exact characteristic-polynomial calculations yield
\[
 \det(tI-B_+)=t^3p_+(t),\qquad
 \det(tI-B_-)=t^3p_-(t).
\]
The complete small matrices are generated deterministically from the two local inequalities, and their characteristic identities are recomputed symbolically in `verify_spectrum.py`. Taking traces of powers proves the displayed root-power formula for every \(n\ge5\); the six zero eigenvalues do not contribute.

**4. Growth and strict comparison.** The \(24\)-state transfer component is irreducible and has self-loops (at the all-zero and all-one four-column states), hence is primitive. Its Perron root \(\alpha\) is simple and strictly dominates all other eigenvalues of \(B\) in modulus. Positive Perron eigenvectors are invariant under bit complementation, so \(\alpha\) is a root of \(p_+\). For an independently checkable rational bound, let \(\mathbf1\) be the \(24\)-vector of ones and \(w=B^{60}\mathbf1\). Exact integer comparisons give, coordinatewise,
\[
 156485\,w<100000\,Bw<156486\,w.
\]
Collatz–Wielandt therefore yields \(1.56485<\alpha<1.56486\). All non-Perron eigenvalues are strictly smaller in modulus, giving \(F_n/\alpha^n\to1\). For the prism the analogous two-column, \(16\)-state transfer has characteristic polynomial
\[
 t^{10}(t-1)^2(t^2-t-1)(t^2-t+1).
\]
Its power traces give \(L_n+2+2\cos(n\pi/3)\). Since \(\alpha<1.56486<\varphi\), the stated exponential deficit follows.

**5. Cut interpretation.** A fixed coloring on a cubic graph has at most one opposite-colored neighbor at each vertex; therefore its bichromatic edges form a matching. Conversely every two-color matching cut defines a majority-fixed coloring. Connectedness makes complementary nonconstant colorings represent the same unordered matching cut, proving \((F_n-2)/2\).

## Verification
Run `python verify_spectrum.py` (requires SymPy) to reconstruct the \(256\)-state transition graph, verify its \(320\) edges and all recurrent components, compute the two exact ninth-degree characteristic polynomials, verify the rational Collatz–Wielandt certificate, and derive all transfer counts through \(n=15\), including the prism comparison. The computation is exhaustive over the finite transition alphabet, and the proof's cyclic-window bijection establishes its applicability to all \(n\ge5\).

Independently, `python verify_direct.py` (requires NumPy) builds each graph by explicit vertex-neighbor indexing and checks **every binary configuration**, for both \(GP(n,2)\) and \(GP(n,1)\), at \(5\le n\le10\), checking a combined \(2{,}795{,}520\) configurations. The expected results are checked as exact integers. Both scripts and captured outputs are included; these finite tests supplement rather than replace the general transfer proof.

## Relationship to prior work
Gadouleau, Richard and Riis [1] study bounds on fixed-point counts of Boolean networks with prescribed signed interaction graphs, but their full text addresses maxima and coding-theoretic bounds, not this majority-rule census on \(GP(n,2)\). Gomes, Juliano, Martins and dos Santos [2] study algorithms and complexity of matching (multi)cuts; the full available manuscript gives no step-two generalized-Petersen counting formula. The published result *All perfect matching cuts of generalized Petersen graphs with second jump two* [3] counts the **perfect** matching-cut subclass, exactly \(1+5\mathbf1_{5\mid n}\) cuts. The present theorem counts **all** matching cuts, including those with uncovered vertices, so the subclass formula does not imply it. For instance, at \(n=6\) the full count is six, while only one is perfect.

The published *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census* [4] already gives \(F_{10}=118\), which is reproduced here as a special case but does not determine other \(n\) or the entropy. The published *Complete fixed-point and two-cycle census for synchronous majority on prism networks* [5] gives the comparison formula for \(GP(n,1)\); this result is explicitly credited, not claimed as new. The new claim is the exact, infinite-family ninth-degree census and entropy gap for \(GP(n,2)\).

## Limitations
The theorem does not classify primitive two-cycles, transient convergence times, or higher generalized Petersen jumps. The proof relies on finite exact characteristic-polynomial certificates, with all construction steps supplied for reproduction. A special-purpose older enumeration or a stronger unindexed transfer-matrix theorem could affect historical priority. No independent audit of this result has been conducted.

## References
[1] M. Gadouleau, A. Richard and S. Riis, *Fixed points of Boolean networks, guessing graphs, and coding theory*, arXiv:1409.6144 (first posted 2014-09-22), https://arxiv.org/abs/1409.6144.

[2] G. C. M. Gomes, E. Juliano, G. Martins and V. F. dos Santos, *Matching (Multi)Cut: Algorithms, Complexity, and Enumeration*, arXiv:2407.02898 (first posted 2024-07-03), https://arxiv.org/abs/2407.02898.

[3] *All perfect matching cuts of generalized Petersen graphs with second jump two*, published mathematical record, 2026, section “Finding” and proof of the exact period-five classification.

[4] *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census*, published mathematical record, 2026, section “Finding” and the matching-cut interpretation.

[5] *Complete fixed-point and two-cycle census for synchronous majority on prism networks*, published mathematical record, 2026, fixed-state theorem.
