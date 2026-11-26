# Exact finite-ring orphan census for Rule 30

## Finding
For every integer \(n\ge 1\), let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the synchronous binary Rule-30 map on a cyclic ring, with
\[
(F_n(x))_i=x_{i-1}\oplus(x_i\lor x_{i+1}),
\]
where indices are taken modulo \(n\). Define \(D_n=2^n-|\operatorname{im}F_n|\), the number of length-\(n\) output configurations having no length-\(n\) predecessor.

Let \(s_0=3\), \(s_1=s_2=1\), and
\[
s_{n+3}=s_{n+2}+2s_n\quad(n\ge0).
\]
Then **for every \(n\ge1\)**,
\[
\boxed{D_n=\frac{s_n+\varepsilon_n}{2}},\qquad
\varepsilon_n=\begin{cases}-1&3\mid n,\\+1&3\nmid n.\end{cases}
\]
Thus the exact one-step image cardinality is \(2^n-(s_n+\varepsilon_n)/2\). Equivalently,
\[
\sum_{n\ge1}D_n z^n
=\frac{z+2z^3-z^4-z^5-2z^6}{(1-z^3)(1-z-2z^3)}.
\]
Writing \(\alpha\) for the positive root of \(t^3-t^2-2=0\), and \(\gamma=\sqrt{2/\alpha}\), the sharp asymptotic is
\[
D_n=\frac{\alpha^n}{2}+O(\gamma^n+1),\qquad
\frac{D_n}{2^n}\sim\frac12\left(\frac{\alpha}{2}\right)^n,
\quad\alpha=1.6956207695\ldots,\ \gamma<\alpha<2.
\]
The fraction of finite-ring output configurations lacking a same-period predecessor decays exponentially, even though every finite ring map is nonsurjective and the associated bilateral full-shift cellular automaton is surjective.

## Assumptions and scope
These statements concern **one synchronous update**, all binary input states and all possible binary output states, under spatially **periodic boundary conditions** with period \(n\), including \(n=1,2\) where neighbor indices coincide. An orphan means absence of an antecedent with that *same period*; it does not mean absence of an antecedent on the unrestricted bilateral shift. No statement about eventual limit sets, attractors, temporal traces, or multi-step images is asserted.

## Proof
Construct the four states \((a,b)\in\{0,1\}^2\). For each \(c\in\{0,1\}\), insert the directed edge \((a,b)\to(b,c)\), labeled \(a\oplus(b\lor c)\). Let \(E_0,E_1\) be its two Boolean adjacency matrices, with each row and column indexed in the order \(00,01,10,11\). In row-major order their sixteen binary entries encode the integers \(49665\) and \(450\), respectively; this explicit assertion is checked independently in the accompanying verifier.

For a proposed output word \(w=w_0\cdots w_{n-1}\), a cyclic path of length \(n\) in the pair graph is exactly a spatially \(n\)-periodic predecessor: successive edges enforce consistency of overlapping pairs, including across the cyclic boundary. Therefore \(w\) has such a predecessor if and only if the Boolean matrix product \(E_{w_0}\cdots E_{w_{n-1}}\) has a nonzero diagonal entry. This works also for \(n=1,2\).

Start from the \(4\times4\) identity relation and close under right multiplication by \(E_0\) and \(E_1\), with multiplication in the Boolean semiring. Exact enumeration in `verify.py` terminates at **41 distinct relations**; 30 of these have a nonzero diagonal and 11 do not. Number the relations in their reproducible breadth-first discovery order, let \(T\) be the corresponding integer \(41\times41\) transition matrix, where each of the two labels contributes one transition (so an entry may equal two), let \(e\) be the initial identity-state indicator, and let \(v\) be the indicator of the zero-diagonal relations. The previous paragraph gives the exact integer identity
\[
D_n=e^{\mathsf T}T^n v\quad(n\ge0).
\]
In particular, no sample-of-inputs assumption enters this identity.

Exact integer iteration gives \((D_1,\ldots,D_6)=(1,1,3,5,6,12)\) and verifies the 41 equalities
\[
D_{j+6}-D_{j+5}-3D_{j+3}+D_{j+2}+2D_j=0
\quad\text{for every integer }1\le j\le41.
\]
By Cayley–Hamilton, every scalar sequence \(e^{\mathsf T}T^n w\) satisfies the same monic characteristic recurrence of order \(41\). The displayed recurrence error is itself such a sequence, with \(w=(T^6-T^5-3T^3+T^2+2I)v\). Because its first 41 consecutive terms vanish, the order-41 recurrence forces **every** subsequent term to vanish. Hence \((D_n)\) obeys for all \(n\ge1\)
\[
D_{n+6}=D_{n+5}+3D_{n+3}-D_{n+2}-2D_n.
\]
This finite exact certificate proves an infinite assertion; it is not an extrapolation from the first 41 ring sizes.

Let \(\lambda_1,\lambda_2,\lambda_3\) be the roots of \(t^3-t^2-2\) with multiplicity and put \(s_n=\lambda_1^n+\lambda_2^n+\lambda_3^n\). Newton's identities give \((s_0,s_1,s_2)=(3,1,1)\) and \(s_{n+3}=s_{n+2}+2s_n\). The three-periodic correction \(\varepsilon_n\) is \(+1,+1,-1\) on positive residues \(1,2,0\pmod3\). Both \(s_n\) and \(\varepsilon_n\) satisfy the order-six recurrence whose characteristic polynomial factors as
\[
(t^3-1)(t^3-t^2-2)=t^6-t^5-3t^3+t^2+2.
\]
Comparison of the six initial values proves \(D_n=(s_n+\varepsilon_n)/2\) for all \(n\ge1\). Multiplying its generating series by the displayed denominator yields the rational expression in the finding.

The real cubic root \(\alpha\) is unique and larger in modulus than the conjugate pair. Their product is \(2/\alpha\), so both have modulus \(\gamma=\sqrt{2/\alpha}\). Therefore \(s_n=\alpha^n+O(\gamma^n)\), establishing the asymptotic.

Finally, both constant-zero and constant-one inputs map to the all-zero output for any \(n\), proving nonsurjectivity of each finite \(F_n\). For the bilateral shift, the local rule is bijective in the leftmost input when the other two inputs are fixed, which gives a global predecessor of every infinite target by a compactness/finite-interval consistency argument. Thus the finite-ring and infinite-shift claims do not conflict.

## Verification
Run `python3 verify.py` from the directory containing this file and the verifier. The script generates each labeled Boolean matrix directly from the eight local transitions, independently closes and checks the 41-element reachable relation monoid, checks all 41 necessary recurrence-error values (the exact Cayley–Hamilton certificate), confirms the closed formula through 70 indices, and independently enumerates all input configurations for \(1\le n\le13\). The reported line is `VERIFY_OK monoid_states=41 recurrence_initial_shifts=41 direct_rings=1..13 power_sum_cases=70 image_sizes_n8_n12_n16=223,3816,63199`. All calculations use exact integer/Boolean arithmetic. The all-length justification requires the algebraic recurrence argument above, not just brute force.

## Relationship to prior work
Wolfram's 1983 study introduced and motivated elementary Rule 30. Rowland's *Local Nested Structure in Rule 30* studies directional bijectivity, local nested patterns, and temporal diagonal periodicity for special infinite configurations rather than a finite-ring one-step image cardinality. The *Elementary CA Zoo* public Garden-of-Eden finite-ring table gives numerical orphan counts for selected sizes, including \(33\) at \(n=8\), \(280\) at \(n=12\), and \(2337\) at \(n=16\); these earlier entries agree with the theorem and **are not claimed as new numerical discoveries**. The claimed contribution is the all-period closed census, recurrence proof, and exact exponential rate, distinct from finite enumerations and global-shift surjectivity. Published finite-width work (Coleman) remains a historical-priority risk because only partial metadata, not its complete thesis, could be inspected.

## Limitations
The result characterizes one-step finite-ring images only, not dynamics under iteration, spatially nonperiodic boundary conventions, distribution of preimage multiplicities, or temporal Garden-of-Eden patterns. Exactness rests on a finite but nontrivial 41-state Boolean-relation computation whose reproducible code is supplied; the proof does not replace that computation with a hand-written table of all 41 relations. The historical-priority comparison is necessarily incomplete for inaccessible finite-width dissertations and other unindexed references. No independent external validation is asserted.

## References
1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644, DOI: 10.1103/RevModPhys.55.601.
2. E. S. Rowland, *Local Nested Structure in Rule 30*, Complex Systems **16** (2006), 239–258, https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf.
3. *Elementary CA Zoo*, "Gardens of Eden", https://cellular.solves.ca/gardens-of-eden (finite-ring enumerations, not a published all-length theorem).
4. I. Coleman, *Finite-Width Elementary Cellular Automata*, Whitman College senior thesis (2011), https://www.whitman.edu/documents/Academics/Mathematics/SeniorProject_IanColeman.pdf (full text unavailable in this review; cited as a priority risk, not evidence for noncoverage).
