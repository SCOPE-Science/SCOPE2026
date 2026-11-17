# Degree-two transgression separates adjacent finite-subset rotation quotients

## Finding
For integers \(q\ge2\) and odd primes \(p>2q\), let
\[E_r=\operatorname{exp}_r(S^1)=\{A\subset S^1:1\le |A|\le r\}\]
with its finite-subset quotient topology. Let \(C_p\) act by multiplication by \(p\)th roots of unity, and put
\[Q^-_{q,p}=E_{2q-1}/C_p,\qquad Q^+_{q,p}=E_{2q}/C_p.\]
The inclusion of finite subsets descends to \(j:Q^-_{q,p}\to Q^+_{q,p}\). Both orbit spaces have universal covers of the homotopy type \(S^{2q-1}\), fundamental group \(C_p\), and **identical integral homology**:
\[
H_i(Q^\pm_{q,p};\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i\in\{0,2q-1\},\\
\mathbb Z/p,&i\text{ odd and }1\le i\le2q-3,\\
0,&\text{otherwise.}
\end{cases}
\]
Let \(u\in H^2(BC_p;\mathbb Z)\cong\mathbb Z/p\) correspond to a fixed generator of \(C_p\). For oriented generators of \(H^{2q-1}(E_{2q-1};\mathbb Z)\) and \(H^{2q-1}(E_{2q};\mathbb Z)\) chosen so that inclusion pulls the second back to twice the first, the Cartan–Leray transgressions are
\[d_{2q}(\xi_-)=a_-u^q,\qquad d_{2q}(\xi_+)=a_+u^q,\qquad a_+,a_-\in(\mathbb Z/p)^\times,\]
with the precise relation
\[\boxed{a_+=2a_-\pmod p}.\]
It follows that
\[\boxed{2\notin\pm((\mathbb F_p)^\times)^q\quad\Longrightarrow\quad Q^-_{q,p}\not\simeq Q^+_{q,p}.}\]
In particular, for \(q=2\) and every prime \(p\equiv5\pmod8\), the adjacent orbit spaces \(E_3/C_p\) and \(E_4/C_p\) have the same integral homology and fundamental group but different homotopy types. The first case is \(p=5\). There are infinitely many such primes by Dirichlet's theorem.

## Assumptions and scope
The circle is the unit complex circle, and the chosen generator of \(C_p\) rotates by \(2\pi/p\). The action is on **unlabeled subsets**, not on ordered configurations or symmetric products with multiplicities. The quotient is the ordinary topological orbit space. The integers satisfy \(q\ge2\) and \(p>2q\), with \(p\) prime. All cohomology and homology in the statement is integral. Each transgression coefficient is defined with a generator of \(C_p\) and orientations as above; its individual sign depends on orientation, but the factor-two relation and obstruction are invariant under the choices needed for comparison.

## Proof
**1. Free action and spherical covers.** If a nonidentity element of \(C_p\) stabilizes a finite nonempty subset \(A\subset S^1\), then \(A\) is a union of full orbits of this rotation. Each orbit has exactly \(p\) elements, hence \(p\mid |A|\). Since \(1\le|A|\le2q<p\), the action is free on both \(E_{2q-1}\) and \(E_{2q}\). Each is a connected finite CW homotopy sphere of dimension \(d=2q-1\), by Tuffley's Theorem 4; since \(d\ge3\), each is simply connected and is the universal cover of its quotient. Hence both quotients have \(\pi_1\cong C_p\).

**2. A nonzero transgression.** Rotations by elements of \(C_p\) act trivially on \(H^d(E_r;\mathbb Z)\cong\mathbb Z\), since each rotation is homotopic to the identity through rotations of \(S^1\). The Cartan–Leray cohomology spectral sequence for the free action is the Serre spectral sequence of the homotopy Borel fibration, and is multiplicative:
\[E_2^{s,t}=H^s(C_p;H^t(E_r;\mathbb Z))\Longrightarrow H^{s+t}(E_r/C_p;\mathbb Z).\]
The only nonzero rows are \(t=0,d\). Integral cyclic group cohomology is \(H^*(BC_p;\mathbb Z)=\mathbb Z[u]/(pu)\), with \(|u|=2\). The only potentially nonzero differential is \(d_{d+1}=d_{2q}\), from row \(d\) to row zero. Write \(d_{2q}(\xi_r)=a_ru^q\) for a top-degree generator \(\xi_r\). If \(a_r=0\pmod p\), then all row-zero classes \(u^j\) for arbitrarily large \(j\) survive, since no other differential can reach them. That contradicts the finite covering dimension of \(E_r/C_p\). Therefore \(a_r\) is a unit mod \(p\). Multiplicativity then kills the row-zero classes \(u^j\) for \(j\ge q\). The surviving row-zero classes are \(u^j\) for \(0\le j<q\), and in total degree \(d\) the upper-row surviving group is \(p\mathbb Z\cong\mathbb Z\). Hence the quotient cohomology is \(\mathbb Z\) in degrees \(0,d\), \(\mathbb Z/p\) in positive even degrees \(2,4,\ldots,d-1\), and zero otherwise. The universal coefficient theorem, noting \(H_d\) has no torsion as the top homology of a finite \(d\)-complex, gives the integral homology stated. (For \(E_{2q}\), the quotient has dimension at most \(d+1\); its top-degree cohomology above \(d\) is still zero by the same spectral sequence, and \(H_{d+1}=0\) because the covering space has \(H_{d+1}=0\) and rational transfer detects a top-dimensional nonzero free summand.)

**3. Factor two.** Tuffley's Theorem 5 asserts that \(E_{2q-1}\hookrightarrow E_{2q}\) induces multiplication by \(2\) on integral top homology. With the chosen orientations, its pullback on top cohomology is \(j^*(\xi_+)=2\xi_-\). It is equivariant and its induced map on \(BC_p\) is the identity for the fixed rotation generator. Naturality of the spectral-sequence differential therefore gives
\[a_+u^q=j^*d_{2q}(\xi_+)=d_{2q}(j^*\xi_+)=2a_-u^q,\]
so \(a_+=2a_-\pmod p\).

**4. Homotopy obstruction.** Suppose a homotopy equivalence \(h:Q^-_{q,p}\to Q^+_{q,p}\) exists. It induces an automorphism of \(\pi_1=C_p\), multiplication by some \(s\in(\mathbb Z/p)^\times\), and lifts to a homotopy equivalence between the universal covers. The lift has top-cohomology degree \(\varepsilon\in\{+1,-1\}\). The induced map on \(H^2(BC_p;\mathbb Z)\) sends \(u\) to \(su\), so on \(H^{2q}\) it multiplies by \(s^q\). Naturality of the transgression gives \(\varepsilon a_- =s^q a_+\pmod p\), and therefore \(2=\varepsilon s^{-q}\pmod p\). Thus a necessary condition for homotopy equivalence is \(2\in\pm((\mathbb F_p)^\times)^q\). Its failure proves the obstruction.

**5. Explicit arithmetic family.** When \(q=2\) and \(p\equiv5\pmod8\), quadratic reciprocity's supplementary law gives \((2/p)=-1\), whereas \((-1/p)=1\) because \(p\equiv1\pmod4\). The set of signed squares therefore equals the squares, and \(2\) is excluded. Every such prime is greater than \(4\). Dirichlet's theorem produces infinitely many primes in this residue class.

## Verification
The mathematical result follows from the displayed spectral-sequence proof, not from finite enumeration. An accompanying dependency-free checker reproduces the exact modular-power obstruction for all primes through \(199\) at \(q=2\), verifies the stated mod-eight criterion, and reports additional obstructed prime examples for \(2\le q\le5\). It checks only finite arithmetic, not the general topological theorems. Its reproducible command is `python3 verification/check_arithmetic.py` from the package root; the expected stdout is embedded as `verification/expected_output.txt`.

## Relationship to prior work
Tuffley's 2002 paper establishes the spherical homotopy types of all \(E_r\), the factor-two homology map for adjacent odd/even stages, and a concrete \((2,-3)\)-weighted circle action on \(E_3\cong S^3\). These are **inputs**, not asserted novelties. The new conclusion concerns the free finite-rotation **orbit spaces**: a naturality relation between their nonzero Cartan–Leray transgressions, an arithmetic obstruction to homotopy equivalence, and infinite families with matching homology but different homotopy types. For example, the known circle-action model identifies \(E_3/C_5\) with the standard lens space \(L(5,1)\), whereas \(E_4/C_5\) cannot be homotopy equivalent to it by the obstruction. The established finite-subset connectivity results of Kallel and Sjerve provide context but do not imply this obstruction. The standard spectral-sequence and cyclic-cohomology facts are classical machinery.

## Limitations
The converse of the signed \(q\)th-power condition is **not proved**; no complete classification of the orbit spaces is claimed. The spaces \(E_{2q}\) are homotopy spheres, not asserted to be genuine spheres. There is no claimed homeomorphism type for \(E_4/C_5\). Published equivalents not indexed by the literature searches remain a priority risk. The proof assumes the classical homotopy and inclusion theorems cited below, and independent audit has not been performed.

## References
1. C. Tuffley, *Finite subset spaces of \(S^1\)*, Algebraic & Geometric Topology **2** (2002), 1119–1145; arXiv:math/0209077 (first public 2002-09-07), https://arxiv.org/abs/math/0209077, DOI:10.2140/agt.2002.2.1119. Relevant Theorems 3, 4, 5.
2. S. Kallel and D. Sjerve, *Remarks on finite subset spaces*, Homology, Homotopy and Applications **11** (2009), 229–250; https://intlpress.com/site/pub/files/_fulltext/journals/hha/2009/0011/0002/HHA-2009-0011-0002-a012.pdf.
3. K. S. Brown, *Cohomology of Groups*, Graduate Texts in Mathematics 87, Springer (1982); cyclic group cohomology and naturality.
4. J. McCleary, *A User's Guide to Spectral Sequences*, 2nd ed., Cambridge (2001); Cartan–Leray/Serre transgression and multiplicativity.
