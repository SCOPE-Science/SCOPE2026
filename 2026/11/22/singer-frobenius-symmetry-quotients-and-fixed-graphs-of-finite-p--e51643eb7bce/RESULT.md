# Singer–Frobenius symmetry quotients and fixed graphs of finite projective planes

## Finding
Let \(q\ge2\) be any prime power, \(N=q^2+q+1\), and \(X_q\) the point–line incidence graph of \(\operatorname{PG}(2,q)\). Choose a Singer generator \(r\) and the \(q\)-power Frobenius \(F\) on \(\mathbb F_{q^3}\). The subgroup \(G=\langle r,F\rangle\cong C_N\rtimes_q C_3\) acts by collineations on both shores of \(X_q\).

For **every** subgroup \(H\le G\), write \(d=|H\cap\langle r\rangle|\), \(m=N/d\), and let \(\varepsilon\) indicate whether \(H\) contains an element outside \(\langle r\rangle\). The *ordinary geometric quotient* has the complete integral homotopy classification
\[
|X_q|/H\simeq\bigvee^{\beta(q,m,\varepsilon)}S^1,
\qquad
\beta(q,m,0)=1+m(q-1),
\]
\[
\beta(q,m,1)=
\begin{cases}
1+\dfrac{m(q-1)-2}{3},&q\equiv0\pmod3,\\
1+\dfrac{m(q-1)}{3},&q\equiv1\pmod3,\\
1+\dfrac{m(q-1)-4}{3},&q\equiv2\pmod3.
\end{cases}
\]
All values are nonnegative integers; zero circles means a point. The three-case formula specializes to the full Singer–Frobenius subgroup when \(m=1\).

The complete **geometric fixed-space classification** is as follows. If \(H=1\), its fixed space is \(|X_q|\simeq\bigvee^{q^3}S^1\). If \(d>1\), its fixed space is empty. Otherwise, any nontrivial \(H\) is of the form \(\langle r^aF\rangle\) of order three, and its fixed subgraph is
\[
|X_q|^{\langle r^a F\rangle}\cong
\begin{cases}
[0,1],&q\equiv0\pmod3,\\
\{p,\ell\}\text{ (discrete)},&q\equiv2\pmod3,\\
C_6,&q\equiv1\pmod3\text{ and }3\mid a,\\
\varnothing,&q\equiv1\pmod3\text{ and }3\nmid a.
\end{cases}
\]
Here \(C_6\) denotes a six-edge topological circle. For example, the full quotient ranks for \(q=2,3,4,5,7\) are respectively \(0,1,2,1,3\). The rank-two finite building itself has \(q^3\) independent circles.

## Assumptions and scope
Work with the *Desarguesian* projective plane only; \(q\) ranges over all prime powers. Its points are one-dimensional and its lines two-dimensional \(\mathbb F_q\)-subspaces of \(\mathbb F_{q^3}\). Choose \(\alpha\in\mathbb F_{q^3}^{\times}\) primitive and label point \(P_i=\alpha^i\mathbb F_q^{\times}\) and line
\[
L_j=\{x\mathbb F_q^{\times}:\operatorname{Tr}_{\mathbb F_{q^3}/\mathbb F_q}(\alpha^{-j}x)=0\},\quad i,j\in\mathbb Z/N\mathbb Z.
\]
Set \(rP_i=P_{i+1}\), \(rL_j=L_{j+1}\), \(FP_i=P_{qi}\), and \(FL_j=L_{qj}\). Incidence is \(P_i\sim L_j\) precisely when \(j-i\) belongs to the Frobenius-invariant Singer difference set
\[
D=\{t\in\mathbb Z/N\mathbb Z:\operatorname{Tr}(\alpha^{-t})=0\},\qquad |D|=q+1.
\]
Thus each edge is uniquely \((i,t):P_i\longleftrightarrow L_{i+t}\) for \(i\in\mathbb Z/N\mathbb Z\) and \(t\in D\). The presentation \(F r F^{-1}=r^q\) follows directly. No point–line dualities are included. A quotient graph retains **parallel edges**, rather than replacing them by one edge.

## Proof
**1. Subgroups and cyclic quotients.** Every subgroup \(H\le G\) meets the Singer group in its unique subgroup \(\langle r^m\rangle\) of order \(d=N/m\). Since \(G/\langle r\rangle\cong C_3\), either \(H=\langle r^m\rangle\) or \(H=\langle r^m,r^aF\rangle\) for some \(a\). (Replace a generator involving \(F^2\) by its inverse to arrange the latter.) The order-three element exists because \((r^aF)^3=r^{a(1+q+q^2)}=1\). The Singer rotation acts freely on the point and line sets, and on edges. Dividing by \(\langle r^m\rangle\) leaves exactly \(2m\) vertices and \(m(q+1)\) edges. The graph is connected, as a continuous quotient of a connected graph. Thus its integral first Betti number is \(m(q+1)-2m+1=1+m(q-1)\).

**2. Semilinear quotient orbit count.** On the intermediate graph, \(T=r^aF\) acts on either shore by \(i\mapsto a+qi\pmod m\), and on edge labels \((i,t)\mapsto(a+qi,qt)\). Let \(f\) be the number of solutions of \((q-1)i\equiv-a\pmod m\), and let \(\delta=|\{t\in D:qt=t\pmod N\}|\). The two nonidentity elements of the residual order-three action have identical fixed counts. Burnside's lemma therefore gives
\[
V_H=\frac{2m+4f}{3},\qquad E_H=\frac{m(q+1)+2f\delta}{3},\qquad
\beta=E_H-V_H+1=1+\frac{m(q-1)+2f(\delta-2)}{3}.
\]
These are counts of genuine quotient graph vertices and edges, not a rational-homology substitution. The formula remains valid if the intermediate graph has parallel edges, because neither action exchanges the two shores and hence no edge is inverted.

**3. The arithmetic dichotomy.** Since \(N\equiv3\pmod{q-1}\), \(\gcd(N,q-1)=\gcd(3,q-1)\). If \(q\not\equiv1\pmod3\), the fixed-label congruence has exactly one solution for any \(a,m\), so \(f=1\). If \(q\equiv1\pmod3\), \(f\) may be zero, one, or three, but it cancels from \(\beta\) because \(\delta=2\).

To calculate \(\delta\), the multiplier-fixed labels satisfy \((q-1)t\equiv0\pmod N\). If \(q\equiv0\pmod3\), only \(t=0\) is fixed, and \(\operatorname{Tr}(1)=3=0\) in the field, so \(\delta=1\). If \(q\equiv2\pmod3\), only \(t=0\) is fixed, but \(\operatorname{Tr}(1)=3\ne0\), so \(\delta=0\). If \(q\equiv1\pmod3\), there are three fixed labels; \(t=0\) is excluded, and the other two correspond to the two nontrivial Frobenius eigenspaces of the normal-basis three-cycle. Their vectors have trace zero, giving \(\delta=2\). Substituting into the Burnside formula proves every quotient rank above.

**4. Geometric fixed spaces.** Point and line vertices lie in disjoint, preserved shores; hence no group element reverses a geometric edge. A fixed point in the realization of a one-dimensional graph must therefore belong to the subgraph on pointwise-fixed vertices and edges. Any nonidentity Singer rotation fixes no vertices, proving the case \(d>1\). For a pure order-three subgroup, \(\gcd(N,q-1)=1\) when \(q\equiv0,2\pmod3\), so every \(r^aF\) is Singer-conjugate to \(F\). In characteristic three, the normal-basis representation of \(F\) on the three-dimensional \(\mathbb F_q\)-space has one unipotent Jordan block of size three: exactly one invariant point and one invariant line containing it. For \(q\equiv2\pmod3\), the minimal polynomial of \(F\) is \((z-1)(z^2+z+1)\), with the quadratic factor irreducible; the unique invariant one-space is complementary to the unique invariant two-space, so the fixed graph consists of two nonincident vertices. For \(q\equiv1\pmod3\), \(F\) has three distinct eigenlines over \(\mathbb F_q\) and their three complementary invariant planes: each invariant point belongs to exactly two invariant lines, producing a six-cycle. Finally, fixed point indices of \(r^aF\) solve \((q-1)i\equiv-a\pmod N\), which for \(q\equiv1\pmod3\) is solvable precisely when \(3\mid a\). This proves the remaining empty case and all fixed-space types. The unquotiented graph has \(2N\) vertices and \(N(q+1)\) edges, hence cycle rank \(N(q-1)+1=q^3\).

## Verification
The standalone `verify_singer.py` uses only Python's standard library and constructs exact finite fields, trace-zero difference sets, incidence graphs, all cyclic subgroup indices, and representative semilinear lifts. It checks all point and edge orbits, integer Betti counts, geometric fixed-component types, the Singer difference-set identity and all stated formulas for \(q\in\{2,3,4,5,7,8,9,11,13,16\}\). The exact output is included as `checks.txt`. Representative lifts \(a=0,1,2\) suffice for the congruence classes in the symbolic formula; finite checks corroborate but do not replace the all-prime-power proof above.

## Relationship to prior work
Drudge classifies Singer orbits on flats, a necessary group-action precedent but not these graph quotient homotopy types or semilinear fixed graphs. Streit–Wolfart describe the embedded incidence graph as a cyclic-projective-plane dessin and note the special full Singer quotient with two vertices and \(q+1\) edges; that special cyclic quotient is **not claimed as independently new**. Their Riemann surface and dessin quotients are different from the complete set of underlying abstract incidence-graph quotients studied here. Sarti studies Frobenius compatibility and free action on edges of suitable embedded dessins, not every subgroup of the underlying incidence graph, and does not give the characteristic-three/semisimple fixed-graph trichotomy. Related recorded topology of Singer subgroups of higher-rank spherical buildings treats dimension at least four and not this projective-plane graph normalizer. Similar-looking statements about graph-of-dessein embeddings, difference-set orbit counts, or rational character traces do not imply the complete fixed-point topology and the all-subgroup homotopy classification stated here without further argument.

## Limitations
The result is for Desarguesian projective planes, their incidence graph *as a one-dimensional space*, and the specified collineation subgroup only. It is not a theorem about a chosen dessin's ambient Riemann surface, all collineations or point–line dualities, non-Desarguesian planes, or higher-rank buildings. No assertion of global novelty or independent validation is made. Some equivalent formulation may remain unindexed, and an inaccessible normalizer-focused paper could affect priority. Finite computations are corroborative rather than an infinite proof.

## References
1. K. Drudge, “On the Orbits of Singer Groups and Their Subgroups,” *Electronic Journal of Combinatorics* 9 (2002), R15; first online publication 2001-03-05. https://doi.org/10.37236/1632
2. M. Streit and J. Wolfart, “Cyclic Projective Planes and Wada Dessins,” *Documenta Mathematica* 6 (2001), 39–68. https://ems.press/journals/dm/articles/8965030
3. C. Sarti, “Wada Dessins associated with Finite Projective Spaces and Frobenius Compatibility,” arXiv:1008.4317 (2010). https://arxiv.org/abs/1008.4317
