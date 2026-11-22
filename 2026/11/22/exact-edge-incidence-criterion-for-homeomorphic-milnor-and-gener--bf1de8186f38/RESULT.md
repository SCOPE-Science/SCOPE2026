# Exact edge-incidence criterion for homeomorphic Milnor and generic attractors on finite graphs

## Finding

**Theorem.** Let \(G\) be a nondegenerate, finite, connected metric graph, equipped with a probability measure \(\mu\) equivalent to arclength (in particular, normalized arclength is allowed). Let \(A\subseteq G\) be nonempty and closed. Define the Milnor global attractor \(\Lambda(f)\) to be the smallest closed set containing \(\omega_f(x)\) for \(\mu\)-almost every \(x\); define the generic limit set \(\Gamma(f)\) analogously using a residual set of initial points.

If \(G\) is a circle, every such \(A\) is simultaneously \(\Lambda(f)=\Gamma(f)\) for a homeomorphism \(f:G\to G\).

Otherwise, let \(V\) be the finite, nonempty set of points of valence different from two, and let \(\mathcal E\) denote the connected components of \(G\setminus V\), called **essential open edges**. The following conditions are equivalent:

1. \(A=\Lambda(f)\) for some homeomorphism of \(G\).
2. \(A=\Gamma(f)\) for some homeomorphism of \(G\).
3. \(A\cap\overline e\ne\varnothing\) for every \(e\in\mathcal E\).
4. There exists a single homeomorphism \(f:G\to G\) such that \(f|_A=\mathrm{id}_A\), \(\Lambda(f)=\Gamma(f)=A\), and every orbit except those in an at-most-countable subset of fixed points converges to one point of \(A\).

This criterion uses **topological essential edges**, not an arbitrary subdivision into combinatorial edges. It applies to bridges, loops, and multiple edges. Every homeomorphism-realizable Milnor attractor is therefore also realizable as a generic limit set, and conversely, although the homeomorphisms witnessing the two properties need not be the same until the construction in condition 4 is used.

**Corollary.** Among nondegenerate finite connected graphs, every nonempty closed subset is homeomorphically realizable as a Milnor global attractor exactly for an arc or a circle. On a tripod, for example, a closed set is realizable exactly when it contains the central branch point or meets the interior or leaf endpoint of each of the three legs.

## Assumptions and scope

A finite metric graph is a compact connected one-dimensional finite CW complex with each open one-cell assigned positive finite length; loops and parallel one-cells are permitted. Valence is a topological invariant. A noncircular graph has finitely many points of valence other than two, and the components of their complement are open intervals, each with compact closure in \(G\). The two abstract ends of an essential edge may represent the same vertex, as happens for a loop. An equivalent-to-arclength probability measure has the same null sets as length measure on these intervals and assigns positive measure to every nonempty open interval.

For a continuous map \(f\) and \(x\in G\), \(\omega_f(x)\) is the nonempty set of subsequential limits of the forward orbit. For closed \(C\subseteq G\), write \(B_f(C)=\{x:\omega_f(x)\subseteq C\}\). A set is residual if its complement is meagre. The smallest closed full-measure-basin or residual-basin set, when considered, is the corresponding global attractor or generic limit set. We prove minimality against **every** closed \(C\) that fails to contain \(A\), not merely against proper subsets of \(A\).

## Proof

**1. Necessity of intersection with essential edge closures.** The finite set \(V\) is defined intrinsically and must be permuted by every homeomorphism \(h\). Therefore \(h\) permutes the finite family \(\mathcal E\). For each \(e\in\mathcal E\) there is an integer \(p\ge1\) with \(h^p(e)=e\). For each \(x\in e\), all \(h^{pn}(x)\) lie in \(e\); compactness gives an accumulation point in \(\overline e\). Consequently
\[
\omega_h(x)\cap\overline e\ne\varnothing\qquad(x\in e).
\]
If a closed set \(A\) avoids \(\overline e\), then \(B_h(A)\cap e=\varnothing\). Since \(e\) has positive arclength and is nonempty open, the basin cannot be full measure **or** residual. This proves that each of conditions 1 and 2 implies condition 3. The argument remains valid if \(h\) reverses the orientation of an edge or permutes its endpoints.

**2. A constructive interval lemma.** Let \(K\subseteq[0,1]\) be any nonempty closed set. There exists an increasing homeomorphism \(g_K:[0,1]\to[0,1]\), fixing \(K\) and both ambient endpoints, such that all points outside a countable set of fixed points have iterates converging to a point of \(K\); moreover, for every \(a\in K\) and every relative neighbourhood \(U\) of \(a\), a nonempty relatively open interval \(J\) satisfies \(\lim_{n\to\infty}g_K^n(x)\in K\cap U\) for all \(x\in J\).

Here is an explicit formula. Set \(g_K(t)=t\) on \(K\cup\{0,1\}\). The complement \([0,1]\setminus K\) has at most countably many interval components; each relevant component is an open gap \((a,b)\) with endpoints in \(K\cup\{0,1\}\). Parameterize it by \(t=a+(b-a)u\), \(0<u<1\), and define
\[
 g_K(t)=a+(b-a)H(u),
\]
where
\[
H(u)=\begin{cases}
 u+\tfrac12 u(1-u)(u-\tfrac12), & a,b\in K,\\
 u+\tfrac12 u(1-u), & a\notin K,\ b\in K,\\
 u-\tfrac12 u(1-u), & a\in K,\ b\notin K.
\end{cases}
\]
The case \(a,b\notin K\) is impossible because \(K\) is nonempty. Every branch fixes \(0,1\) and has derivative at least \(1/2\); more precisely the two-ended branch has derivative
\[
H'(u)=\tfrac34+\tfrac32u-\tfrac32u^2\in[\tfrac34,\tfrac98],
\]
and the one-ended branches have derivative in \([1/2,3/2]\). Thus each gap maps increasingly onto itself. The estimate \(|g_K(t)-t|\le \frac12\min(t-a,b-t)\) on each gap implies continuity at all points of \(K\) and at ambient endpoints, even when infinitely many gaps accumulate; the combined map is a strictly increasing homeomorphism of the interval.

For two-ended gaps, the midpoint is a repelling fixed point, every point in the left half decreases monotonically to \(a\), and every point in the right half increases monotonically to \(b\). For a one-ended gap, all its interior points move toward the endpoint that belongs to \(K\). Therefore the only exceptional points outside \(K\) are the ambient endpoints not in \(K\) and the midpoints of two-ended gaps. This set is countable and consists of fixed points.

To establish the neighbourhood property, take \(a\in K\) and a relative neighbourhood \(U\). If \(U\) contains an open interval lying in \(K\), that interval is fixed. Otherwise \(U\) contains an endpoint in \(K\) of a complementary gap: indeed, a point of \(K\) outside its relative interior can be approached by complement points, and the intervening gap endpoint lies arbitrarily close. A one-sided open subinterval of that gap converges to this endpoint by the preceding formulas. This proves the lemma, including isolated points and singleton or Cantor-like \(K\).

**3. Gluing on an arbitrary finite connected graph.** Assume condition 3. For each essential open edge \(e\), choose a characteristic parameterization \(\phi_e:(0,1)\to e\) extending continuously to \([0,1]\) with endpoint images in \(V\). The two images may coincide. Put \(K_e=\phi_e^{-1}(A\cap\overline e)\), where the inverse on the closed parameter interval is understood as preimage under the continuous extension. This is nonempty and closed. Use the interval lemma to define \(f\circ\phi_e=\phi_e\circ g_{K_e}\) on each open edge, and let \(f(v)=v\) for every \(v\in V\). Since every \(g_{K_e}\) fixes its parameter endpoints, the definitions glue continuously, as do their inverses. Thus \(f\) is a graph homeomorphism fixing \(A\) pointwise.

On each edge, all points outside a countable fixed set converge to a point of \(A\cap\overline e\). Adding the finitely many vertices gives a countable exceptional set \(E\), contained in \(\operatorname{Fix}(f)\). Hence \(B_f(A)\supset G\setminus E\). Since the graph is nondegenerate, each singleton is arclength null and nowhere dense. The basin of \(A\) is both full measure and residual.

For **minimality**, let \(C\subseteq G\) be any closed set with \(A\not\subseteq C\), and choose \(a\in A\setminus C\). Select a neighbourhood \(U\) of \(a\) disjoint from \(C\). Choose an essential edge whose closure contains \(a\); on that edge the interval lemma supplies a nonempty open interval \(J\subset e\) whose every point converges to a point of \(A\cap U\). This open set has positive measure and is disjoint from \(B_f(C)\). Accordingly \(C\) has neither a full-measure basin nor a residual basin. This proves \(\Lambda(f)=\Gamma(f)=A\), and condition 4 implies conditions 1 and 2.

**4. Circle case.** If \(G\) is a circle, choose any \(c\in A\), cut the circle at \(c\), and pull back \(A\) to a closed \(K\subseteq[0,1]\) containing both endpoints. The increasing interval homeomorphism from Step 2 fixes those endpoints and therefore descends to a circle homeomorphism fixing \(c\) and \(A\). The full-measure, residual, and minimality arguments descend as well. This proves the circle statement.

**5. Universal-graph corollary.** An arc and a circle realize every nonempty closed subset by the theorem. A connected finite graph that is neither an arc nor a circle has at least two essential open edges. An interior point of one such edge forms a closed singleton avoiding the closure of another, so it cannot be realized homeomorphically. For a tripod with central point \(v\), the three essential edge closures are its legs, and their common intersection is \(\{v\}\), giving the stated criterion.

## Verification

The proof of the infinite statement is the exact topological and one-dimensional construction above; no finite experiment is used as an exhaustive proof. The standalone `verify.py` uses only the Python standard library and checks exact polynomial fixed-point identities, derivative bounds, signs and increasing order at rational test points, convergence for a finite two-point set, and sample edge-incidence obstructions.

Execute `python3 verify.py` from the package directory. Expected output is recorded in `verification_output.txt`. The program cannot certify arbitrary infinite closed sets or previously unknown literature coverage; those depend on the written proof and source comparison.

## Relationship to prior work

Hantáková and Mlíchová (arXiv:2611.15353v1, first submitted November 11, 2026) prove universal Milnor realization by homeomorphisms on connected one-dimensional manifolds and closed surfaces. They give a one-singleton non-realization result on the tripod (Proposition 6.4) and explicitly leave characterization of the homeomorphic Milnor-attractor family of a branched continuum open (Section 6.5). The present criterion gives a complete necessary-and-sufficient answer for **finite connected topological graphs**, including all tripods, trees with branch vertices, and graphs with loops. It is neither an application of their manifold theorem to a nonmanifold nor just their tripod example repeated: it determines every closed target set.

Mai and Shao (2007) prove that the family of individual \(\omega\)-limit sets of a fixed graph map is Hausdorff closed; that is a distinct invariant from the smallest closed set containing almost all (or a residual set of) individual \(\omega\)-limit sets as the map varies. Robinson and Sánchez-Gabites (2016; earlier preprint arXiv:1306.5959) characterize topological global attractors of homeomorphisms on Euclidean linear spaces, which attract bounded sets, not measure- or category-generic initial conditions on a compact finite graph. Those results do not imply the present edge-incidence classification. An equivalent treatment in older specialized graph-homeomorphism literature is a residual priority risk.

## Limitations

The result concerns *existence of some homeomorphism* for each closed target, not the attractors of every graph homeomorphism. It does not classify noninvertible continuous graph maps or infinitely edged graph-like continua, and does not prescribe nontrivial dynamics on the target set (the constructed map fixes it). The reference measure must be equivalent to arclength; measures with atoms or zero support on an open edge can change the necessity argument. The countable-exception conclusion is particular to the constructed map and is not asserted for arbitrary homeomorphisms.

## References

1. J. Hantáková and M. Mlíchová, *Universal Realization of Milnor Attractors in Low Dimensions*, arXiv:2611.15353v1 (November 11, 2026), Sections 4--6, especially Proposition 6.4 and Section 6.5. https://arxiv.org/html/2611.15353v1
2. J.-H. Mai and S. Shao, *Spaces of \(\omega\)-limit sets of graph maps*, Fundamenta Mathematicae 196 (2007), 91--100, DOI:10.4064/fm196-1-2. https://www.impan.pl/shop/en/publication/transaction/download/product/88540
3. J. C. Robinson and J. J. Sánchez-Gabites, *On finite-dimensional global attractors of homeomorphisms*, Bulletin of the London Mathematical Society 48 (2016), 483--498; arXiv:1306.5959. https://arxiv.org/abs/1306.5959
4. J. Milnor, *On the Concept of Attractor*, Communications in Mathematical Physics 99 (1985), 177--195.
