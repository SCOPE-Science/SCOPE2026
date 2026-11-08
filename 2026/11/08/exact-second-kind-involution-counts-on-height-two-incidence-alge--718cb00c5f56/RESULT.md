# Exact second-kind involution counts on height-two incidence algebras

## Finding
Let \(q\) be any prime power, \(K=\mathbb F_{q^2}\), and \(\sigma(a)=a^q\). Let \(P\) be a finite connected poset of height exactly two (so each strict interval is an edge between a minimal and a maximal element). Its incidence algebra over \(K\) is \(A=I(P,K)\), and its radical \(J\) has square zero. Let \(m\) denote the number of strict comparable pairs (edges). An *order-reversing involution* of \(P\) is a bijection \(\tau:P\to P\) with \(\tau^2=\operatorname{id}\) and \(u<v\) if and only if \(\tau(v)<\tau(u)\). It induces an involution \(r_\tau\) of the edge set by \((u,v)\mapsto(\tau(v),\tau(u))\). Let \(f_\tau\) be the number of edges fixed by this action.

A *second-kind involution* here means an additive anti-automorphism \(\rho:A\to A\) such that \(\rho^2=\operatorname{id}\) and \(\rho(a1)=\sigma(a)1\) for every \(a\in K\). It induces an order-reversing involution \(\tau\) of \(P\) on the primitive idempotents of \(A/J\).

**Theorem.** For every order-reversing involution \(\tau\), the number of distinct second-kind involutions inducing \(\tau\) is exactly
\[
\boxed{N_\tau(P,q)=q^m(q+1)^{f_\tau}(q^2-1)^{(m-f_\tau)/2}.}
\]
All such involutions are conjugate under \(K\)-algebra automorphisms of \(A\). Hence the total number of second-kind involutions is the sum of the displayed expression over all order-reversing involutions \(\tau\) of \(P\), and the number of equivalence classes under \(K\)-algebra automorphisms is the number of \(\operatorname{Aut}(P)\)-conjugacy classes of such \(\tau\). When there are none, both counts are zero. This holds in characteristic two as well as in odd characteristic.

For the complete height-two poset with \(n\) lower and \(n\) upper elements, every order-reversing involution matches the two levels bijectively, with \(m=n^2\) and \(f_\tau=n\). The exact total is
\[
\boxed{n!\,q^{n^2}(q+1)^n(q^2-1)^{n(n-1)/2},}
\]
and all these involutions lie in one equivalence class. For the six-vertex crown with three lower and three upper vertices, there are four order-reversing involutions: one with zero fixed edges and three with two fixed edges; consequently its total is \(q^6[(q^2-1)^3+3(q+1)^2(q^2-1)^2]\), and it has exactly two equivalence classes.

## Assumptions and scope
All vector spaces and incidence algebras are finite-dimensional. \(K\)-algebra automorphisms in the equivalence statement fix \(K\) pointwise; all involutions are only \(\mathbb F_q\)-linear and act on \(K\) by \(\sigma\). The poset is connected, has at least one edge, and has no comparabilities of length greater than one. The radical \(J\) has \(K\)-basis \(E_{uv}\) for \(u<v\), with \(J^2=0\), and the diagonal idempotents are \(e_u=E_{uu}\). For \(u<v\), \(e_u E_{uv}=E_{uv}=E_{uv}e_v\); other products with diagonal idempotents vanish. Connectedness ensures \(Z(A)\cap J=0\): a radical central element commuting with every \(e_u\) has every edge coefficient zero.

## Proof
**1. Normalized edge coefficients.** Fix \(\tau\) and put \(r=r_\tau\). Since \(J\) is the Jacobson radical, any second-kind involution \(\rho\) maps \(J\) to itself. Its action on \(A/J\cong K^{|P|}\) permutes diagonal coordinates by \(\tau\), followed by \(\sigma\). For an edge \(e=(u,v)\), the identity \(E_{uv}=e_uE_{uv}e_v\), together with \(J^2=0\), implies that \(\rho(E_e)\) is a nonzero scalar multiple of \(E_{r(e)}\). Thus
\[
\rho(E_e)=c_eE_{r(e)},\qquad c_e\in K^\times.
\]
The involution equation on this basis is equivalent to \(c_e^q c_{r(e)}=1\). These equations are necessary for every \(\rho\).

Conversely, let \(c=(c_e)\) satisfy these equations and define the normalized semilinear anti-automorphism \(\rho_c\) by
\[
\rho_c(e_u)=e_{\tau(u)},\qquad
\rho_c(aE_e)=a^q c_e E_{r(e)}\quad(a\in K).
\]
All nonzero products of basis elements use a diagonal idempotent; they are reversed correctly, so \(\rho_c\) is an anti-automorphism. The equations on \(c\) make \(\rho_c^2=\operatorname{id}\). For each edge fixed by \(r\), the condition is \(c_ec_e^q=1\), with exactly \(q+1\) solutions in \(K^\times\). For each two-edge orbit, one coefficient is arbitrary nonzero, and the other is forced, giving \(q^2-1\) choices. There are precisely \((m-f_\tau)/2\) two-edge orbits. Therefore normalized involutions number
\[
(q+1)^{f_\tau}(q^2-1)^{(m-f_\tau)/2}.
\]

**2. All unnormalized involutions.** The image of every \(e_u\) under \(\rho\) is a primitive idempotent reducing modulo \(J\) to \(e_{\tau(u)}\). Families of mutually orthogonal primitive idempotents lifting the prescribed diagonal family are parametrized uniquely by \(v\in J\): conjugating the diagonal family by \(1+v\) gives
\[
\operatorname{Ad}(1+v)(e_u)=e_u+ve_u-e_uv.
\]
Indeed, an off-diagonal coefficient of a lifted idempotent can occur only on an edge incident to its vertex; orthogonality and the sum-to-one condition make the coefficients at the two endpoints opposite. They determine one unique coefficient of \(v\) for every edge. It follows that every \(\rho\) inducing \(\tau\) has a unique expression
\[
\rho=\operatorname{Ad}(1+v)\circ\rho_c
\]
where \(\rho_c\) is normalized as in step 1. The nonzero edge coefficients of \(\rho\) and \(\rho_c\) agree because conjugation by \(1+v\) acts trivially on \(J\).

For any such \(v\), applying the anti-automorphism rule twice gives
\[
\rho^2=\operatorname{Ad}\bigl((1+v)\rho_c(1+v)^{-1}\bigr)
=\operatorname{Ad}(1+v-\rho_c(v)).
\]
Since \(Z(A)\cap J=0\), this is the identity if and only if \(v=\rho_c(v)\). On the radical, \(\rho_c\) is a \(\sigma\)-semilinear involution permuting the edge basis through \(r\). The fixed subspace has \(q\) choices on each fixed edge and \(q^2\) choices on each two-edge orbit. Its cardinality is thus exactly \(q^{f_\tau+2(m-f_\tau)/2}=q^m\). The uniqueness of \((c,v)\) proves the numerical formula.

**3. Equivalence.** Every map \(E_e\mapsto s_eE_e\), \(s_e\in K^\times\), fixing all diagonal idempotents, is a \(K\)-algebra automorphism because \(J^2=0\). Its conjugation transforms the normalized parameter to
\[
c'_e=s_{r(e)}c_es_e^{-q}.
\]
For a two-edge orbit, choose one \(s_e\) arbitrarily and solve for its partner, obtaining \(c'_e=c'_{r(e)}=1\). For a fixed edge, the equation to solve is \(s_e^{q-1}=c_e\); the norm-one condition guarantees a solution by the cyclicity of \(K^\times\). Thus all \(\rho_c\) inducing a fixed \(\tau\) are conjugate to the normalized involution having every coefficient equal to one.

For any \(v\in J\) fixed by \(\rho_c\), the additive map \(x\mapsto x+\rho_c(x)\) from \(J\) onto its fixed subspace is surjective. On a fixed edge it is a nonzero \(\mathbb F_q\)-linear trace-type map from a two-dimensional to a one-dimensional space, and on each paired-edge orbit it surjects onto the two-dimensional fixed space. Choose \(x\) with \(x+\rho_c(x)=v\). A direct conjugation identity gives
\[
\operatorname{Ad}(1+x)\circ\rho_c\circ\operatorname{Ad}(1+x)^{-1}
=\operatorname{Ad}(1+v)\circ\rho_c.
\]
Hence all involutions inducing \(\tau\) lie in one \(K\)-algebra-automorphism conjugacy class. Any automorphism of the incidence algebra induces an order automorphism \(\alpha\) of \(P\), and conjugation sends \(\tau\) to \(\alpha\tau\alpha^{-1}\). Conversely every \(\alpha\in\operatorname{Aut}(P)\) induces an algebra automorphism. This proves the equivalence-class assertion.

**4. Explicit examples.** For complete bipartite height two, \(\tau\) is a bijection between the levels, so there are \(n!\) choices, and every matched pair yields one fixed edge. In a six-vertex crown, straightforward permutation enumeration gives one duality with no fixed edges and three with two fixed edges; conjugation by the crown's order automorphisms gives orbit sizes one and three. Substitution into the general formula yields the stated special cases.

## Verification
The standalone `verify.py` constructs \(\mathbb F_4\) and \(\mathbb F_9\) by irreducible quadratic polynomials. For the height-two complete bipartite posets with \(n=1\) and \(n=2\), it enumerates every permissible normalized edge-scalar system and every fixed radical vector, constructs the resulting maps on the incidence-algebra basis, and tests their involution and anti-multiplicativity equations on every basis pair. It also checks distinctness and predicted exact counts. The per-duality counts are \(6\) for \(\mathbb F_4,n=1\), \(12\) for \(\mathbb F_9,n=1\), \(432\) for \(\mathbb F_4,n=2\), and \(10{,}368\) for \(\mathbb F_9,n=2\).

An independently organized test in `verify_direct.py` enumerates all \(12\) possible semilinear anti-automorphisms of the two-idempotent chain over \(\mathbb F_4\), and all \(72\) over \(\mathbb F_9\), by their images of the basis generators without imposing the involution condition. It finds respectively \(6\) and \(12\) involutions. The `verify_dualities.py` script independently enumerates crown dualities and their conjugacy orbits for crowns on six, eight, and ten vertices. All three programs end with `VERIFY_OK`.

Reproduce with `python verify.py`, `python verify_direct.py`, and `python verify_dualities.py` using only the Python standard library. The universal theorem follows from the proof, not from extrapolating finite experiments.

## Relationship to prior work
Érica Zancanella Fornaroli's 2023 work proves general existence and a normal-form decomposition for second-kind involutions on finitary incidence algebras, and gives equivalence criteria in odd characteristic under an inner-multiplicative-automorphism hypothesis. Its structural results are prior art, not claimed here. The present theorem extracts explicit finite-field cardinalities for every connected height-two poset and resolves the equivalence relation in this family without an odd-characteristic restriction or a restriction that every multiplicative automorphism be inner. The key extra input is the square-zero radical, which makes every edge rescaling an algebra automorphism and permits direct counting of the fixed-radical twists.

The 2019 work of Ivan and Michael Gargate counts **elements** \(g\in I(P,K)\) satisfying \(g^2=1\) over odd-characteristic fields, not anti-automorphisms of the incidence algebra. Earlier classifications of first-kind or triangular-matrix involutions concern different restrictions and do not supply the stated general height-two count. The two-vertex triangular boundary is elementary; novelty is not claimed for that isolated case. The closest relevant published formulas could imply some small examples but do not give this arbitrary-poset edge-orbit census in the inspected material.

## Limitations
The result concerns only quadratic finite-field involutions and height-two connected posets, and is not asserted for fields with different involutions, non-connected posets, or posets of larger height. It counts field-semilinear anti-automorphisms, not order-two *elements* of the algebra. The source inspections and database searches reduce but do not eliminate publication-priority risk; a previously unlocated general formula could still subsume the theorem. Independent validation has not been performed.

## References
1. É. Z. Fornaroli, *Involutions of the second kind on finitary incidence algebras*, arXiv:2306.12512v1 (first public June 21, 2023), https://arxiv.org/pdf/2306.12512 . In particular, Theorems 3.7 and 4.20 and the hypotheses of Section 4.
2. I. Gargate and M. Gargate, *Involutions on Incidence Algebras of Finite Posets*, arXiv:1907.06805v1 (July 16, 2019), https://arxiv.org/abs/1907.06805 . This counts order-two elements, not anti-automorphism maps.
3. R. Brusamarello and D. W. Lewis, *Automorphisms and involutions on incidence algebras*, Linear and Multilinear Algebra (2011), DOI:10.1080/03081087.2010.496113 . Background on equivalence.
