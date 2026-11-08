# The universal sum-product avoidance polynomial for finite local rings

## Finding
Let \(R\) be a finite commutative local ring with identity, whose residue field has characteristic \(p\ge5\). Write \(\mathfrak m\) for its maximal ideal and set \(N=|R|\), \(M=|\mathfrak m|\), and \(q=N/M\). Let \(\delta=2\) if \(q\equiv1\pmod3\), and \(\delta=0\) otherwise. For any subset \(A\subseteq R\), let \(A+A=\{a+b:a,b\in A\}\) and \(AA=\{ab:a,b\in A\}\), permitting the same element twice. The exact cardinality enumerator of subsets avoiding \(1\) as either sum or product is

\[
\boxed{\sum_{\substack{A\subseteq R\\1\notin(A+A)\cup(AA)}}z^{|A|}
=(1+z)^2(1+2z)^{\delta/2}
(1+4z+3z^2)^{(M-1)/2}
(1+6z+9z^2+2z^3)^{(N-2M-3-\delta)/6}.}
\]

All displayed exponents are nonnegative integers. Consequently the largest avoiding set has size exactly \((N-1)/2\), and the number attaining this size is exactly
\[
\boxed{3^{(M-1)/2}2^{(N-2M-3-\delta)/6+\delta/2}.}
\]
The total number of avoiding subsets is
\[
4\,3^{\delta/2}8^{(M-1)/2}18^{(N-2M-3-\delta)/6}.
\]
These invariants depend only on the cardinality \(N\) and residue-field order \(q\), not on the isomorphism class of \(R\).

## Assumptions and scope
A finite local ring means a finite commutative unital ring with exactly one maximal ideal. Its maximal ideal is nilpotent, the complement of the ideal comprises its units, and the residue field has order \(q=p^f\) for an integer \(f\ge1\). The hypothesis \(p\ge5\) makes \(2\), \(3\), and the derivatives of the relevant quadratic polynomial invertible. Neither unique factorization nor the assumption that \(R\) is a domain is required. The sum and product sets include pairs of equal elements; therefore an element with \(2x=1\) or \(x^2=1\) is individually forbidden.

## Proof
**1. Convert to a graph.** On the vertex set \(R\), connect distinct \(x,y\) when \(x+y=1\) or \(xy=1\); place a loop when \(2x=1\) or \(x^2=1\). Avoiding subsets are exactly the independent vertex subsets with no looped vertices. The sum relation is the involution \(s(x)=1-x\). The product relation joins the units \(x\) and \(t(x)=x^{-1}\), where \(t\) is an involution. No nonunit participates in a product edge equal to \(1\).

**2. The two exceptional components.** The component \(\{0,1\}\) has an edge and a loop at \(1\), hence polynomial \(1+z\). The component \(\{2,-1,1/2\}\) has its two edges incident with \(2\) and loops at \(-1\) and \(1/2\); its polynomial is also \(1+z\). Distinctness follows on reducing modulo \(\mathfrak m\), since the characteristic is at least five.

**3. Each nonzero nonunit creates a four-vertex path.** For \(x\in\mathfrak m\setminus\{0\}\), set
\[
 a=x,\qquad b=1-x,\qquad c=(1-x)^{-1},\qquad d=1-(1-x)^{-1}=-x/(1-x).
\]
Then \(a,d\in\mathfrak m\) while \(b,c\in1+\mathfrak m\). The edges \(a-b\), \(b-c\), \(c-d\) are respectively a sum edge, a product edge, and a sum edge. If \(a=d\), then \(x(2-x)=0\); since \(2-x\) is a unit, this forces \(x=0\), excluded. The other vertices are also distinct because their reductions modulo \(\mathfrak m\) distinguish the two pairs; if \(b=c\), \((1-x)^2=1\) implies \(x(2-x)=0\). These four vertices have no other neighbors and no loops. They form a path \(P_4\). Moreover \(d=-x/(1-x)\) is an involution without fixed points on \(\mathfrak m\setminus\{0\}\), partitioning all nonzero nonunits into exactly \((M-1)/2\) paths. Each path has independence polynomial \(1+4z+3z^2\).

**4. Classify the remaining units.** Remove units whose complements are nonunits; these lie in the paths or exceptional components already counted. On
\[
U=\{x\in R:x\text{ and }1-x\text{ are units}\}
\]
the maps \(s(x)=1-x\) and \(t(x)=x^{-1}\) are permutations with \(s^2=t^2=(st)^3=\mathrm{id}\). The six possible transformations constitute the anharmonic action. The three involutions have fixed points only at \(1/2\), \(-1\), or \(2\), and the order-three elements have fixed points exactly at roots of \(f(X)=X^2-X+1\). These statements remain valid with zero divisors: the equations reduce to factors containing units (for example \(x(2-x)=0\) with \(x\) a unit gives \(x=2\)); no cancellation by a nonunit is used. Thus every orbit not among these exceptions has six distinct vertices, connected alternately by sum and product edges in a six-cycle \(C_6\), with independence polynomial \(1+6z+9z^2+2z^3\).

**5. Count root components in the local ring.** The polynomial \(f\) has two distinct roots in the residue field exactly when \(3\mid(q-1)\): its roots are exactly the elements of multiplicative order six in \(\mathbb F_q\). At a root, \(f'(x)=2x-1\) is a unit because \((2x-1)^2=-3\) modulo the maximal ideal. Since \(\mathfrak m\) is nilpotent, the standard elementary simple-root lifting argument (correcting successively modulo \(\mathfrak m^j\)) gives exactly one root in \(R\) over each residue root. Thus \(R\) has \(\delta\in\{0,2\}\) roots. If present, they form a single edge because \(x(1-x)=1\), with independence polynomial \(1+2z\).

**6. Multiply polynomials and optimize.** The two exceptional components use five vertices; the paths use \(2(M-1)\) vertices; and the possible root edge uses \(\delta\). The remaining number is \(N-5-2(M-1)-\delta=N-2M-3-\delta\), necessarily a multiple of six. Independent sets in separate components can be chosen independently, which gives the stated complete product formula. Its degree is
\[
2+(M-1)+\delta/2+3(N-2M-3-\delta)/6=(N-1)/2.
\]
Every component's leading coefficient is respectively \(1\), \(3\), \(2\), or \(2\), yielding the exact count of all maximum-cardinality avoiding sets. Evaluation at \(z=1\) gives the total count. This completes the proof for every finite commutative local ring meeting the hypothesis.

## Verification
The accompanying standalone `verify.py` uses the literal addition and multiplication tables of several finite rings to construct forbidden pairs and looped vertices. It enumerates independent subsets inside each actual connected component, multiplies the resulting component polynomials, and compares **every coefficient** to the claimed closed formula. For rings of order at most 13, an additional exhaustive loop directly enumerates all subsets using the defining forbidden sum/product equations, with no graph factorization. Checked examples include residue rings of orders \(5,7,11,13,25,49,125\); the extension field of order \(25\); a five-element-field dual-number ring of order \(25\); and a non-chain local algebra of order \(125\). All checks pass. Finite experiments are consistency checks, not a proof for infinitely many local rings; the six-step symbolic argument above supplies that proof.

## Relationship to prior work
Tang, *A counterexample to a conjecture of Sárközy on sums and products modulo a prime* (first submitted March 31, 2026), Theorem 2.2 and Remark 2.4, proves the sharp extremal cardinality for prime **fields** by classifying two exceptional components, a possible root edge, and generic six-cycles. The finite-field anharmonic-orbit mechanism and corresponding prime-field special cases are therefore not claimed as new. The present theorem treats all finite commutative **local rings**, including rings with nilpotents and zero divisors. Their new \(P_4\) components contribute an independent factor at every cardinality, while simple-root lifting and an orbit argument yield a universal polynomial depending only on the order and residue-field size. Tang does not state the zero-divisor path factor, the local-ring enumerator, or the local-ring count of optimal configurations. No stronger covering theorem was identified in the targeted literature comparison; unindexed equivalences remain possible.

For example, two nonisomorphic rings of order \(25\), \(\mathbb Z/25\mathbb Z\) and \(\mathbb F_5[\varepsilon]/(\varepsilon^2)\), have the same enumerator and exactly \(36\) optimal sets; the field \(\mathbb F_{25}\), also of order \(25\) but with a different residue-field size, has exactly \(16\) optimal sets. These are exact examples, not a claim that all rings of the same order have the same polynomial.

## Limitations
The theorem assumes commutativity, locality, and residue characteristic at least five; it does not assert the same formula for characteristic two or three, nonlocal product rings, or noncommutative rings. The result is solely for avoiding the distinguished target \(1\), not arbitrary target elements. It classifies the size distribution of avoiding subsets but not their isomorphism orbits under ring automorphisms. Historical priority is qualified by the possibility of unindexed or unpublished equivalent work. Verification is same-model, not independent certification.

## References
Quanyu Tang, *A counterexample to a conjecture of Sárközy on sums and products modulo a prime*, arXiv:2603.29992, initially posted 2026-03-31, particularly Theorem 2.2 and Remark 2.4. https://arxiv.org/abs/2603.29992.
