# Characteristic-model spectra of consecutive Horn implications on paths and rings

## Finding

For each integer \(n\ge 0\), put \(V_n=\{1,\ldots,n\}\) and let \(\Sigma_n^{\mathrm P}\) contain the definite Horn implications
\[
\{i,i+1\}\longrightarrow i+2\quad(1\le i\le n-2).
\]
For \(n\ge3\), let \(\Sigma_n^{\mathrm C}\) contain the same implications with indices read cyclically modulo \(n\), with precisely \(n\) rules. In each case, let \(\mathcal C\) be the finite family of closed subsets, let \(\mathcal M\) be its proper meet-irreducible members, and write \(R_n(q)=\sum_{M\in\mathcal M}q^{n-|M|}\).

**Theorem (canonical-model path/ring contrast).** On the path, every proper meet-irreducible is uniquely of the form
\[
M=I\cup\{i+1,\ldots,n\},\qquad
1\le i\le n,\quad I\in\operatorname{MIS}(P_{i-1}),
\]
where \(I\subseteq\{1,\ldots,i-1\}\) and \(\operatorname{MIS}(P_0)=\{\varnothing\}\). Thus, as a formal power series,
\[
\boxed{\sum_{n\ge0}R_n^{\mathrm P}(q)t^n
=\frac{qt(1+t+qt^2)}{(1-t)(1-qt^2-q^2t^3)}.}
\]
On the ring, the proper closed sets are precisely the independent sets of the ordinary cycle \(C_n\). An independent set is meet-irreducible exactly when it has **at most one** vertex outside the set with no neighbour in the set. Equivalently, consecutive chosen vertices are separated cyclically by \(1\) or \(2\) unchosen vertices, with the additional possibility of exactly one gap of \(3\) unchosen vertices. With \(D=1-qt^2-q^2t^3\),
\[
\boxed{\sum_{n\ge3}R_n^{\mathrm C}(q)t^n
=\frac{2qt^2+3q^2t^3}{D}
+\frac{q^3t^4(4-2qt^2-q^2t^3)}{D^2}-2qt^2.}
\]
Here the coefficient of \(q^s\) counts characteristic models with exactly \(s\) omitted atoms, without counting the all-ones model. The first path totals, starting at \(n=0\), are \(0,1,2,4,6,9,13,18,25,34,46,62\). The first ring totals, starting at \(n=3\), are \(3,6,5,11,14,18,30,37,55\).

Let \(\rho>1\) be the real root of \(\rho^3=\rho+1\). The two sequences have different polynomial growth factors:
\[
|\mathcal M_n^{\mathrm P}|\sim2.9459756165\,\rho^n,
\qquad
|\mathcal M_n^{\mathrm C}|\sim
\frac{n\rho^n}{2\rho^2+3\rho}.
\]
The complete closed-set counts are \(F_{n+3}-1\) on paths and \(F_{n-1}+F_{n+1}+1\) on rings, where \(F_0=0,F_1=1\). Both grow exponentially at the golden ratio, strictly faster than their proper canonical-model families.

## Assumptions and scope

All sets are finite and labelled; a rule fires whenever both antecedent atoms are present. Closure means closure under all rules, not merely one simultaneous round. Meet-irreducibility is relative to the lattice of closed sets ordered by inclusion; a proper closed set is meet-irreducible if it cannot be expressed as the intersection of two strictly larger closed sets. For the ring, \(n\ge3\) is essential: ordinary simple cycles and the distinct cyclic rules are then unambiguous. There are no assertions about general Horn theories, arbitrary directed graphs, or computational hardness. The zero-vertex path has one closed set and no proper meet-irreducibles.

## Proof

**1. Generic maximal-omitter lemma.** A proper element of a finite intersection-closed family is meet-irreducible precisely when it is inclusion-maximal among closed sets omitting some element \(i\). Indeed, maximal omission forces every strict closed extension to contain \(i\), so two such extensions cannot intersect to the original set. Conversely, a proper meet-irreducible has exactly one cover in the finite closed-set lattice. Choose any \(i\) in that cover but not in the set; every proper closed extension contains the unique cover, hence contains \(i\). This standard lemma is explicitly prior work [1, Section 2, Lemma 2.3].

**2. Path normal form.** A closed path subset is represented by a binary word avoiding the factor \(110\), since the rules assert that every pair of consecutive ones forces the next position to be one. Fix a missing atom \(i\). In a maximal closed \(i\)-omitter all atoms strictly after \(i\) must be present: filling the suffix preserves every rule with head at most \(i\), and ensures all later conclusions. Since \(i\) is absent, the prefix before \(i\) cannot contain two adjacent ones; otherwise the first later zero would make an occurrence of \(110\). Conversely, any independent subset \(I\subseteq\{1,\ldots,i-1\}\), together with all atoms after \(i\), is closed and misses \(i\). It is maximal with this omission exactly when \(I\) is a maximal independent set of the prefix path. The index \(i\) is the last missing atom, so no model appears in two families. Step 1 proves the claimed exact bijection.

**3. Weighted path enumeration.** Let \(m_k(u)\) count maximal independent sets of a length-\(k\) path by their number of selected vertices. A maximal independent set either contains the initial vertex, excludes the next, and continues with a maximal independent set on \(k-2\) vertices, or excludes the initial vertex, contains the second, excludes the third, and continues on \(k-3\) vertices. With \(m_0=1,m_1=u,m_2=2u\), this gives \(m_k=u m_{k-2}+u m_{k-3}\) for \(k\ge3\), whence
\[
\sum_{k\ge0}m_k(u)z^k=\frac{1+uz+uz^2}{1-uz^2-uz^3}.
\]
For the model indexed by \(i=k+1\), exactly \(k+1-|I|\) atoms are omitted. Summing \(q^{k+1}m_k(q^{-1})\) over \(k<n\), then over \(n\), gives the displayed path series. The known Padovan enumeration of maximal independent path sets is not claimed as new [3].

**4. Ring normal form and meet-irreducibility.** The presence of any adjacent pair in a closed ring set forces its successor, then all other vertices in turn, so the set must be full. Conversely, an independent set of \(C_n\) fires no rule and is closed. For a proper independent set \(I\), write \(a(I)\) for the number of unselected vertices having no selected neighbour. These are exactly the single vertices that can be added while keeping the set independent. If \(a(I)=0\), then \(I\) is maximal independent and its unique strict cover is the full set. If \(a(I)>0\), its covers are exactly its \(a(I)\) one-vertex independent extensions, and therefore it is meet-irreducible precisely for \(a(I)=1\). In a cyclic gap containing \(g\) zeros between successive ones, exactly \(\max(g-2,0)\) zeros have no selected neighbour. Thus \(a(I)\le1\) gives exactly the two asserted gap families. The empty independent set has \(a(I)=n>1\) for \(n\ge3\), so causes no exception.

**5. Weighted ring enumeration.** Mark the number of omitted vertices by \(q\), and write \(f(t,q)=qt^2+q^2t^3\). A gap of \(1\) or \(2\) zeros contributes one selected vertex followed by that gap, giving respectively the two monomials in \(f\). With \(r\) selected vertices, an ordered cyclic gap list has \(r\) possible starting selected vertices and \(n\) possible labelled positions. Therefore each cyclic-gap list of total length \(n\) contributes \(n/r\) labelled models. All-gap-\(1,2\) models contribute
\[
t\frac{\partial}{\partial t}[-\log(1-f(t,q))]
=\frac{2qt^2+3q^2t^3}{1-f(t,q)}.
\]
For models with one gap of three zeros, designate its unique length-four block of weight \(q^3t^4\); the other blocks form any ordered list of length-two or length-three blocks. After cancelling the choice of starting selected vertex against the distinguished gap, the contribution is
\[
t\frac{\partial}{\partial t}
\left[\frac{q^3t^4}{1-f(t,q)}\right]
=\frac{q^3t^4(4-2qt^2-q^2t^3)}{(1-f(t,q))^2}.
\]
The first series also counts two formal labelled configurations at length two; subtract \(2qt^2\) to impose the actual ring domain \(n\ge3\). This proves the second boxed identity.

**6. Closed-set totals and growth.** For the path, the last zero is either absent (the all-ones model) or at \(i\), with a zero-adjacent-free prefix of length \(i-1\), giving \(1+\sum_{i=1}^n F_{i+1}=F_{n+3}-1\). For the ring, the closed sets are all cycle-independent sets plus the distinct full set, giving \(F_{n-1}+F_{n+1}+1\). The denominator \(1-t^2-t^3\) has a unique smallest-modulus root \(\rho^{-1}\), with no competing pole of the same modulus because the allowed tile lengths \(2,3\) have gcd one. Its simple pole gives the stated path constant; the squared denominator and derivative provide the \(n\)-factor and coefficient \((2\rho^2+3\rho)^{-1}\) for rings. All other poles have strictly larger modulus.

## Verification

Run `python3 verify.py` using Python 3 with no third-party dependencies. It independently constructs every closed subset, tests meet-irreducibility directly against all pairs of strict closed supersets, and compares the entire omitted-atom polynomial with the two predicted formulas, for all path orders \(0\) through \(11\) and ring orders \(3\) through \(11\). It also independently tests the closed-set totals. The recorded completed execution printed `VERIFY_OK raw_lattice_subsets=8183; path_orders=0..11; ring_orders=3..11`. The exhaustive computations are finite consistency checks; the arbitrary-length result follows from the preceding proof, not from enumeration.

## Relationship to prior work

Babin's 2026 paper [1] proves a general coNP-completeness result for verifying canonical representations and states the generic maximal-omitter characterization used here; it does not, in the inspected text, give these local path/ring descriptions or their two size-refined generating functions. Defrain, Ohana, and Vilmin [2] provide incremental-polynomial translation algorithms for bounded-degree acyclic implicational bases; this theorem concerns a particular exact one-dimensional system and its cyclic non-acyclic analogue, not a new general algorithmic complexity bound. Classical Padovan and Perrin counts for maximal independent sets of paths and cycles and their cardinality refinements are already in the graph-enumeration literature [3,4]. The new claim is the **Horn meet-irreducible classification**, including cycle independent sets with one undominated vertex, plus the resulting full characteristic-model rank series and asymptotic change under cyclic closure. Searches did not establish historical uniqueness; older equivalent descriptions under other terminology may exist.

## Limitations

The proof applies only to the explicitly defined consecutive binary Horn bases. Neither a general tractability theorem nor an optimal algorithm for arbitrary bases is asserted. Related prior results on path and cycle maximal independent sets, and the generic meet-irreducible/maximal-omitter lemma, are credited rather than presented as original. External novelty review is incomplete, and no independent scientific audit has been performed. The stated rational series and asymptotics are exact/proved under the specified definitions; finite checker runs are supporting diagnostics only.

## References

1. M. Babin, *Completeness of Canonical Closure Representations Is coNP-Complete*, arXiv:2607.18534, first posted July 20, 2026. https://arxiv.org/abs/2607.18534
2. O. Defrain, A. Ohana, S. Vilmin, *Translating between the representations of an acyclic convex geometry of bounded degree*, arXiv:2506.24052 (first posted June 30, 2025); ISAAC 2025 article *Enumerating the Irreducible Closed Sets of an Acyclic Implicational Base of Bounded Degree*, DOI:10.4230/LIPIcs.ISAAC.2025.24. https://arxiv.org/abs/2506.24052
3. R. Bisdorff and J.-L. Marichal, *Counting non-isomorphic maximal independent sets of the n-cycle graph*, Journal of Integer Sequences 11 (2008), available via https://orbilu.uni.lu/handle/10993/387
4. *On the existence and the number of independent (1,2)-dominating sets in the G-join of graphs*, Applied Mathematics and Computation 377 (2020), article 125155. https://doi.org/10.1016/j.amc.2020.125155
