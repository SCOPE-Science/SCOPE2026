# A parity-split exact NOR orbit census on circular ladders

## Finding

Let \(G_n=C_n\square K_2\) be the labelled circular ladder with \(n\ge3\) rungs and vertex set \(\mathbb Z/n\mathbb Z\times\{0,1\}\). The synchronous **open-neighborhood** NOR update is
\[
F_n(x)_{i,a}=\prod_{(j,b)\sim(i,a)}(1-x_{j,b}),\qquad x\in\{0,1\}^{2n}.
\]
In particular, the vertex's own state is **not** an input. Put \(L_0=2\), \(L_1=1\), and \(L_{r+2}=L_{r+1}+L_r\), and set
\[
M_r=L_r+\begin{cases}2,&3\mid r,\\-1,&3\nmid r.\end{cases}
\]
Then every initial configuration becomes periodic after **at most one update**, and only least periods one and two occur. The number of fixed configurations is exactly \(M_n\); the number of recurrent configurations is
\[
R_n=\begin{cases}M_n^2,&n\text{ even},\\M_{2n},&n\text{ odd};\end{cases}
\]
and the number of distinct primitive temporal two-cycle orbits is
\[
\boxed{Q_n=\begin{cases}(M_n^2-M_n)/2,&n\text{ even},\\(M_{2n}-M_n)/2,&n\text{ odd}.\end{cases}}
\]
As \(n\to\infty\), \(Q_n\sim\varphi^{2n}/2\), where \(\varphi=(1+\sqrt5)/2\). Thus recurrent configurations comprise an asymptotically vanishing fraction \((\varphi^2/4)^n(1+o(1))\) of all \(4^n\) binary configurations. The parity split is the connectedness transition of the canonical bipartite double cover.

## Assumptions and scope

Each ladder edge is undirected, with horizontal edges joining successive vertices on each of the two \(n\)-cycles and one vertical edge per rung. The graph is simple, including for \(n=3\). Every vertex has degree three. Updates are simultaneous, binary, deterministic, and use only the **three neighbors**; there is no inertial rule, self-feedback, randomness, or asynchronous schedule. A configuration is recurrent if \(F_n^t(x)=x\) for some positive \(t\). The number \(Q_n\) counts temporal orbits, not the two configurations separately, and no quotient by spatial automorphisms is taken.

## Proof

**1. Polarity and the one-step clock.** For any finite undirected loopless graph \(G=(V,E)\), represent a configuration by its active set \(S\subseteq V\) and define \(\mathcal N(S)=\{v:N(v)\cap S=\varnothing\}\). Since adjacency is symmetric,
\[
A\subseteq\mathcal N(B)\quad\Longleftrightarrow\quad B\subseteq\mathcal N(A).
\]
This antitone Galois relation gives \(S\subseteq\mathcal N^2(S)\), while antitonicity gives \(\mathcal N^3(S)\subseteq\mathcal N(S)\). Applying the first inclusion to \(\mathcal N(S)\) gives the reverse containment, so \(\mathcal N^3=\mathcal N\). Hence \(F_n^3=F_n\); all configurations after the first update are on a fixed point or a two-cycle. A fixed point \(S=\mathcal N(S)\) is exactly a maximal independent set: its members have no neighbors in \(S\), and every excluded vertex has a neighbor in \(S\).

**2. Recurrent configurations and the double cover.** Let \(H(G)\) have vertices \((v,0)\) and \((v,1)\) and an edge \((u,0)(v,1)\) precisely when \(uv\in E(G)\). An ordered pair of active sets \((S,T)\) obeys \(S=\mathcal N(T)\) and \(T=\mathcal N(S)\) if and only if \((S\times\{0\})\cup(T\times\{1\})\) is a maximal independent set of \(H(G)\): independence forbids all cross-adjacencies, and maximality forces every unselected copy to have a selected opposite-copy neighbor. Recurrent states \(S\) correspond bijectively to these maximal independent sets, with unique companion \(T=\mathcal N(S)\). Therefore
\[
\#\operatorname{Rec}(F_n)=\operatorname{mis}(H(G_n)),\quad
\#\operatorname{Fix}(F_n)=\operatorname{mis}(G_n).
\]
If \(n\) is even, \(G_n\) is bipartite, so its canonical double cover is the disjoint union of two copies of \(G_n\). If \(n\) is odd, \(H(G_n)\cong C_{2n}\square K_2\). For clarity, write its vertices as \((i,a,t)\) with \(i\in\mathbb Z/n\mathbb Z\), \(a,t\in\{0,1\}\). Let \(j\in\mathbb Z/(2n)\mathbb Z\) be the unique simultaneous solution of \(j\equiv i\pmod n\) and \(j\equiv t\pmod2\). The map \((i,a,t)\mapsto(j+na\pmod{2n},a)\) takes the two horizontal neighbors to the two same-rail cycle neighbors and the cross-rail neighbor to the same-column rung. It is bijective and preserves all edges. Maximal independent set counts multiply over disjoint components, giving the two asserted forms for \(R_n\) once \(M_n=\operatorname{mis}(G_n)\) is proved.

**3. Count maximal independent sets of a prism.** In an independent set there are only three possibilities at each rung: top-only \(T\), bottom-only \(B\), or empty \(E\). Maximality means domination of both vertices on an empty rung. Therefore a cyclic word \(w_0\cdots w_{n-1}\) over \(\{T,B,E\}\) specifies a maximal independent set if and only if (a) no two horizontally consecutive nonempty rungs select the same rail, and (b) every empty rung has neighbors \(T\) and \(B\), in either order. These are precisely the local triple tests
\[
\mathrm{ok}(a,b,c)=
\begin{cases}
1,&b=E\ \text{and }(a,c)\in\{(T,B),(B,T)\},\\
1,&b\in\{T,B\}\ \text{and }a\ne b,\ c\ne b,\\
0,&\text{otherwise}.
\end{cases}
\]
Define the integer transfer matrix \(U\) with rows and columns indexed by ordered pairs of letters, whose entry \(U_{(a,b),(b',c)}\) is one when \(b=b'\) and \(\mathrm{ok}(a,b,c)=1\), and zero otherwise. Then \(\operatorname{mis}(G_n)=\operatorname{tr}(U^n)\), because each closed length-\(n\) walk in this ordered-pair graph corresponds to one labelled cyclic rung word. A direct nine-by-nine determinant expansion gives
\[
\det(tI-U)=t^5(t^2-t-1)(t^2+t+1).
\]
Consequently, \(\operatorname{tr}(U^n)=\varphi^n+\psi^n+\omega^n+\bar\omega^n\) for \(n\ge1\), where \(\psi=(1-\sqrt5)/2\) and \(\omega\) is a primitive cube root of unity. The first two terms are the Lucas number \(L_n\) and the latter two are \(2\) when \(3\mid n\), otherwise \(-1\). This is \(M_n\). The exact primitive two-orbit count is then half the difference between recurrent and fixed configuration counts.

**4. Growth.** The Lucas formula gives \(M_n=\varphi^n+O(1)\). Thus either parity of the formula for \(R_n\) yields \(R_n=\varphi^{2n}(1+o(1))\), whereas \(M_n=o(R_n)\). Division by two yields the stated asymptotic; dividing by \(4^n\) proves the recurrent fraction.

## Verification

The standalone programs `check_dynamics.py` and `check_transfer.py` require Python 3; the latter optionally uses SymPy for the characteristic-polynomial assertion. Running each file from its containing directory verifies the following independently:

- Exhaustive direct successor-map evaluation on all \(87{,}360\) binary configurations over \(n=3,4,5,6,7,8\): the identity \(F_n^3=F_n\), fixed and recurrent counts, and primitive two-orbit counts.
- A separately coded nine-state ordered-pair transfer matches the formula through \(n=30\), cyclic word enumeration through \(n=9\), direct maximal independent set enumeration through \(n=8\), and direct canonical-cover maximal independent set enumeration through \(n=5\).
- The computed pairs \((\#\operatorname{Fix},Q_n)\) are \((6,7),(6,15),(10,56),(20,190),(28,407),(46,1035)\) for \(n=3,\ldots,8\).

These finite tests corroborate but do not replace the general proof, including the graph-cover isomorphism and the symbolic transfer identity.

## Relationship to prior work

The fixed-point/maximal-independent-set correspondence is classical in negative AND-NOT network theory, notably Veliz-Cuba and Laubenbacher (first published 15 October 2011) and Aracena, Richard, and Salinas (2014). Aledo, Martinez, and Valverde's 2015 survey treats general maxterm/minterm dynamics and establishes broad possible-period restrictions for undirected networks; Aledo et al. (2020) develop general fixed-point and two-periodic-point bounds. These background results are credited rather than presented as new. The present claim is specifically the **exact labelled all-size fixed and primitive-two-cycle census** for the **open** NOR rule on circular ladders, including the odd/even double-cover transition and explicit Lucas/cube-root correction. In particular, results for a NOR operation including a vertex's own state are not interchangeable with the open-neighborhood rule.

## Limitations

This result does not count sizes of individual attraction basins or first-entry-time populations beyond the universal at-most-one update bound. It does not classify states up to spatial symmetry or treat altered edges, other graph families, or local rules with self-inputs. A closely related earlier 2012 maxterm/minterm article was located bibliographically but its full text could not be inspected during this comparison; historical literature not indexed by the consulted searches may contain equivalent special-case enumerations. Novelty is a best-evidence assessment, not a priority certificate.

## References

1. A. Veliz-Cuba and R. Laubenbacher, *On the computation of fixed points in Boolean networks*, Journal of Applied Mathematics and Computing 39 (2012), 145–153; first public online date 2011-10-15. DOI: `10.1007/s12190-011-0517-9`.
2. J. Aracena, A. Richard, L. Salinas, *Maximum number of fixed points in AND–OR–NOT networks*, J. Computer and System Sciences 80 (2014), 1175–1190. DOI: `10.1016/j.jcss.2014.04.025`.
3. J. A. Aledo, S. Martinez, J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), 594294. DOI: `10.1155/2015/594294`.
4. J. A. Aledo, S. Martinez, F. L. Pelayo, J. C. Valverde, *Parallel discrete dynamical systems on maxterm and minterm Boolean functions*, Mathematical and Computer Modelling 55 (2012), 666–671. DOI: `10.1016/j.mcm.2011.08.040` (full-text comparison incomplete).
5. J. A. Aledo et al., *Counting Periodic Points in Parallel Graph Dynamical Systems*, Complexity (2020), 9708347. DOI: `10.1155/2020/9708347`.
