# Common-displacement finite-field helical automata: an all-order two-cycle census

## Finding
Let \(q=2^n\) with integer \(n\geq2\), let \(V=(\mathbb F_q,+)\), and choose \(d\in V\setminus\{0\}\). Set \(H=\{0,d\}\). Choose an arbitrary union \(S\) of cosets of \(H\), of cardinality \(s\) (thus \(0\leq s\leq q\) and \(s\) is even). Define the permutation
\[
f(x)=\begin{cases}x+d,&x\in S,\\ x,&x\notin S.\end{cases}
\]
For every integer \(L\geq1\), form a helical finite-field automaton on \(V^{L+1}\) with sites \(x_1,\dots,x_L\) and a carrier \(b\): scan the sites from left to right using
\[
R(x,y)=\bigl(y+f(x+y),\ x+f(x+y)\bigr),
\]
where the first component is the updated site and the second is the outgoing carrier; after the last site the outgoing carrier becomes the next-step input carrier.

**Theorem.** Every such \(f\) is bijective and satisfies the characteristic-two functional identity (12) used by Araoka–Tokihiro to specify their finite-field rules. The full site-and-carrier time-one map \(T\) satisfies \(T^2=\mathrm{id}\), for every \(n,L,d,S\). Its number of fixed states and its number of primitive two-cycles are, exactly,
\[
F_1=q(q-s)^L,\qquad C_2=\frac{q^{L+1}-q(q-s)^L}{2}.
\]
Equivalently, the complete periodic-orbit zeta function is
\[
\zeta_T(z)=(1-z)^{-q(q-s)^L}(1-z^2)^{-[q^{L+1}-q(q-s)^L]/2}.
\]
There are exactly \(1+(q-1)(2^{q/2}-1)\) distinct maps \(f\) in this entire constant-nonzero-displacement class, counting the identity once. Every bijective map with \(f(x)-x\in\{0,d\}\) for all \(x\) belongs to this class. In particular, this supplies explicit period-two dynamics for nonaffine examples at every \(q\geq8\), not just the small fields treated by earlier period proofs.

## Assumptions and scope
Field addition and subtraction coincide, but field multiplication never appears; consequently all assertions also hold on any elementary abelian two-group of cardinality \(q\). The carrier is a genuine part of the dynamical state. The theorem asserts exact orbit data for that \((L+1)\)-coordinate map; it does not assert these counts for the projection onto sites alone. Empty support gives the identity map; full support is allowed. The term *primitive two-cycle* means an unordered orbit containing exactly two distinct states.

## Proof
**Step 1: structural classification of the permutation.** Define \(\chi(x)=1\) on \(S\), and zero elsewhere, interpreted in \(\mathbb F_2\). Because \(S+d=S\), we have \(\chi(x+d)=\chi(x)\), and
\[
f(x)=x+d\chi(x),\qquad f(f(x))=x.
\]
Conversely suppose \(f\) is bijective and every displacement is zero or \(d\). If \(f(x)=x+d\), bijectivity forbids \(f(x+d)=x+d\), since that value already has preimage \(x\). Hence \(f(x+d)=x\). Therefore its displacement support is a union of \(H\)-cosets, proving exhaustiveness of the claimed class.

**Step 2: the published characteristic-two functional identity.** The identity (12) is
\[
f(u)+f(u+f(v))=f(u+f(v+f(u)))\qquad(u,v\in V).
\]
Let \(\chi\) be invariant under translation by \(d\). Then
\[
f(u+f(v))=u+v+d\{\chi(v)+\chi(u+v)\},
\]
so the left side is \(v+d\{\chi(u)+\chi(v)+\chi(u+v)\}\). Similarly
\[
f(v+f(u))=u+v+d\{\chi(u)+\chi(u+v)\},
\]
and applying \(f\) to \(u+f(v+f(u))\) gives exactly the same expression, since adding a multiple of \(d\) does not change \(\chi\). This proves the printed functional equation with no enumeration. For clarity about conventions, the associated pair maps \(R_{12},R_{13},R_{23}\) commute: every one only adds \(d\) to two coordinates, without changing any of their cosets modulo \(H\), and the decision at every pair is determined only by those cosets. Thus \(R_{12}R_{13}R_{23}=R_{23}R_{13}R_{12}\).

**Step 3: a closed formula for the helical update.** Write \(\eta_i=\chi(x_i+b)\), determined from the initial state. From the formula for \(R\), a local interaction adds \(d\eta_i\) both to the selected site and to the passing carrier. Previously scanned sites have only altered the carrier by a multiple of \(d\), which cannot alter any later \(\chi(x_i+b)\). Therefore the simultaneous one-step formula is
\[
T(x_1,\dots,x_L,b)=\bigl(x_1+d\eta_1,\dots,x_L+d\eta_L,\ b+d\textstyle\sum_{i=1}^L\eta_i\bigr).
\]
All coordinate classes modulo \(H\) are invariant. The values \(\eta_i\) are therefore invariant under the entire map: the arguments \(x_i+b\) change by a multiple of \(d\). Reapplying the same translation twice yields \(T^2=\mathrm{id}\).

**Step 4: exact cycle enumeration.** Since \(d\ne0\), the state is fixed exactly when every \(\eta_i=0\). For each fixed carrier \(b\), exactly \(q-s\) choices of each independent site avoid \(b+S\). Hence \(F_1=q(q-s)^L\). All other \(q^{L+1}-F_1\) states belong to two-element cycles, establishing \(C_2\). The zeta expression follows from \(\zeta_T(z)=\prod_{\mathcal O}(1-z^{|\mathcal O|})^{-1}\).

**Step 5: number of distinct rules.** For fixed \(d\), there are \(q/2\) distinct cosets of \(H\), hence \(2^{q/2}\) supports. Nonempty supports for different nonzero values of \(d\) cannot define the same map, because \(f(x)+x\) recovers \(d\) at any moved point. Empty supports all give the identity. The count is therefore \(1+(q-1)(2^{q/2}-1)\). The disjointness argument also proves that this is the *complete* class of bijections with at most one fixed nonzero displacement.

To see genuine nonaffine members, choose \(S\) to consist of a single coset \(\{a,a+d\}\). This permutation exchanges just two field elements, fixing \(q-2\). For \(q\geq8\), the fixed-point set of a nonidentity affine map over \(\mathbb F_2\) (when nonempty) has size a power of two, whereas \(q-2\) is not a power of two. Thus a single-transposition rule is nonaffine.

## Verification
Run \`python3 verify.py\` with Python 3 (standard library only). The checker enumerates **all** coset-union rules for \(q=4,8,16\), confirms the functional identity on every pair, and checks the count of distinct maps (respectively \(10\), \(106\), and \(3826\)). It also independently enumerates entire site-and-carrier state spaces over a range of supports and lengths, checks \(T^2=\mathrm{id}\), and compares the number of fixed states to the closed formula. The recorded successful run gave \`VERIFY_OK exact_state_checks= 1686656\`. These finite checks are independent diagnostics, not proof for arbitrary \(n\) or \(L\).

## Relationship to prior work
Araoka and Tokihiro (arXiv:2602.17148, first submitted 19 February 2026) introduce this field-map helical automaton, the characteristic-two functional equation, and finite-field numerical searches. They prove period divisibility for \(q=4,8\), and their single-transposition and additive-involution constructions overlap special cases here. Their paper states the unrestricted all-field period-divisibility conjecture. The present contribution is confined to **every** bijection with a single nonzero displacement, establishing an infinite-order rule-family classification, an explicit all-length involution, complete fixed-state/two-cycle counts and a distinct-rule enumerator. It neither restates their small-field classification as new nor resolves their conjecture for arbitrary bijections.

Gombor and Pozsgay (arXiv:2112.01854) investigate Yang–Baxter block automata with brickwork periodic boundary dynamics, not this sequential helical site-and-carrier return map. A publicly indexed additive-affine helical-rule census covers affine maps; it does not imply the nonaffine single-transposition case for \(q\geq8\). General prior theory of involutive permutation solutions may afford alternative derivations of the local commutation mechanism; a completely exhaustive historical priority claim is not made.

## Limitations
The family imposes that all nonzero displacements coincide. General bijective characteristic-two Yang–Baxter rules can have several different nonzero displacements and are not handled here. The periodic counts include the boundary carrier, and the naive site-only projected evolution need not be deterministic without it. A complete historical literature priority search is not claimed, and no independent scientific validation has occurred.

## References
1. A. Araoka and T. Tokihiro, *Integrable cellular automata on finite fields of order \(2^n\)*, arXiv:2602.17148v1 (19 February 2026), Sections 2–3; journal version *Mathematical Physics, Analysis and Geometry* **29**, 30 (2026), DOI:10.1007/s11040-026-09569-9. https://arxiv.org/html/2602.17148
2. T. Gombor and B. Pozsgay, *Superintegrable cellular automata and dual unitary gates from Yang–Baxter maps*, arXiv:2112.01854v2 (2022), Sections 1–2 and 3–5. https://arxiv.org/pdf/2112.01854
3. S. P. Banks and S. Djirar, *Fixed Points and Shift Cycles in Cellular Automata*, ACSE Research Report 459 (1992), abstract/catalog record. https://eprints.whiterose.ac.uk/id/eprint/79286/
