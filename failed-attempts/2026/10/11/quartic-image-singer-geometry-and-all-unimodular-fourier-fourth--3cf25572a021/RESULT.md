# Quartic-image Singer geometry and all unimodular Fourier fourth-moment maximizers over thirteen elements

## Finding
Let \(F=\mathbb F_{13}\), \(\zeta=\exp(2\pi i/13)\), and
\[
T f(u,v)=\sum_{t\in F} f(t)\zeta^{ut+vt^4},\qquad (u,v)\in F^2.
\]
Equip \(F^2\) with probability counting measure. Among **all** functions \(f:F\to\mathbb C\) satisfying \(|f(t)|=1\) for every \(t\),
\[
\max_{|f|\equiv1}\frac1{13^2}\sum_{u,v\in F}|Tf(u,v)|^4=445.
\]
Every maximizer, and no other unimodular function, has the unique form
\[
\boxed{f(t)=\zeta^{at}\Phi(t^4),\qquad a\in F,\quad
\Phi:\{0,1,3,9\}\longrightarrow\mathbb T.}
\]
Here \(\mathbb T=\{z\in\mathbb C:|z|=1\}\), and both \(a\) and \(\Phi\) are unique. Thus the equality set is a disjoint union of thirteen real four-dimensional tori; after quotienting by common phase it is a disjoint union of thirteen three-dimensional tori.

This is a **phase-only** optimization theorem, not an assertion that unimodular functions maximize the unrestricted \(\ell^2\to L^4\) operator norm.

## Assumptions and scope
All arithmetic in exponents and the polynomial map is modulo \(13\). The sum defining \(T\) uses no prefactor. The output is averaged over all \(169\) frequencies; all \(13\) input coefficients have exactly unit modulus. There is no limiting regime or unspecified genericity hypothesis. The result applies to the graph \(\{(t,t^4):t\in F\}\), not to a parabola or a full moment curve.

The prime \(13\) is structurally selected: the fourth-power image \(D=\{0,1,3,9\}\) is a perfect \((13,4,1)\) additive difference set. Among prime fields of characteristic at least five, a fourth-power image can be an additive Sidon set only at primes \(5\) or \(13\): if \(p\equiv3\pmod4\), its cardinality is \((p+1)/2\); if \(p\equiv1\pmod4\), it is \((p+3)/4\); in either case the necessary difference-count inequality \(|D|(|D|-1)\le p-1\) gives the stated restriction. Direct inspection verifies the Sidon property at \(5\) and \(13\). The thirteen-element case is the first nontrivial four-value instance, explaining the finite parameter choice.

## Proof
**Fourth-moment reduction.** Define the ordered pair-sum fibers
\[
\mathcal F_{s,h}=\{(x,y)\in F^2:x+y=s,\ x^4+y^4=h\}.
\]
Finite-character orthogonality gives the exact identity
\[
\frac1{13^2}\sum_{u,v\in F}|Tf(u,v)|^4
=\sum_{s,h\in F}\left|\sum_{(x,y)\in\mathcal F_{s,h}}f(x)f(y)\right|^2.
\]
For \(|f|\equiv1\), each summand is bounded by \(|\mathcal F_{s,h}|^2\); the constant function attains every bound simultaneously. Equality holds precisely when the pair products agree inside every fiber, or equivalently when
\[
f(x)f(y)=f(z)f(w)
\quad\text{whenever}\quad x+y=z+w,\ x^4+y^4=z^4+w^4.
\]

**The exceptional fourth-power image.** The twelve nonzero ordered differences of \(D=\{0,1,3,9\}\) are each nonzero residue of \(F\) exactly once, which can be checked directly by listing differences. In odd characteristic this also implies every unordered pair of elements of \(D\), repetitions allowed, has a distinct sum. Therefore every quartic-graph additive collision preserves the unordered pair of individual fourth powers. This proves that \(f(t)=\Phi(t^4)\) satisfies all equality relations. Multiplication by \(\zeta^{at}\) also preserves them because their two first-coordinate sums agree.

**Complete finite relation certificate.** To establish necessity, enumerate unordered pairs \(0\le x\le y\le12\), indexing each by \((x+y,x^4+y^4)\bmod13\). There are exactly \(76\) nonempty fibers: \(61\) contain one unordered pair and \(15\) contain two. There are no larger unordered fibers. The fifteen double-fiber comparisons, in a fixed reproducible order, are:
\[
\begin{array}{c|l@{\qquad}c|l}
0&(1,12)\sim(5,8)&1&(4,9)\sim(6,7)\\
2&(2,11)\sim(3,10)&3&(5,9)\sim(6,8)\\
4&(3,12)\sim(5,10)&5&(1,2)\sim(5,11)\\
6&(6,11)\sim(7,10)&7&(1,4)\sim(6,12)\\
8&(2,4)\sim(9,10)&9&(3,4)\sim(9,11)\\
10&(1,7)\sim(9,12)&11&(2,7)\sim(3,6)\\
12&(2,8)\sim(11,12)&13&(1,10)\sim(3,8)\\
14&(4,8)\sim(5,7)&&
\end{array}
\]
All arithmetic checks are exact, and the attached standalone checker independently constructs the fibers rather than trusting the displayed list. The only repeated unordered pairs are these fifteen comparisons; none contains a diagonal pair. Thus the ordered-fiber energy is
\[
13\cdot1^2+48\cdot2^2+15\cdot4^2=445,
\]
proving the sharp phase-only value independently of any external energy formula.

For each displayed comparison \((a,b)\sim(c,d)\), form an integer row \(e_c+e_d-e_a-e_b\in\mathbb Z^{13}\), and let \(M\) be the \(15\)-by-\(13\) matrix of these rows, indexed \(0,\ldots,14\). A unimodular phase vector belongs to the kernel of the induced homomorphism \(M:\mathbb T^{13}\to\mathbb T^{15}\).

The four indicator vectors of the quartic-value fibers \(\{t:t^4=h\}\), \(h\in D\), are linearly independent integer nullvectors. Therefore \(\operatorname{rank}_{\mathbb Q}M\le9\). The submatrix indexed by rows
\[
(0,1,2,7,8,11,12,13,14)
\]
and columns
\[
(2,3,4,5,6,8,9,10,12)
\]
has determinant \(13\), so the rational rank is exactly nine. The submatrix indexed by rows
\[
(0,4,5,8,9,10,11,14)
\]
and columns
\[
(2,3,4,6,8,9,11,12)
\]
has determinant \(1\). Modulo \(13\), the four fiber indicators and the vector of coordinate residues \((0,1,\ldots,12)\) give five linearly independent nullvectors: the final vector is not constant on nonzero fourth-power fibers. Hence the rank modulo \(13\) is at most eight; the determinant-one minor makes it exactly eight.

Every nine-by-nine integer minor is consequently divisible by \(13\), and the exhibited determinant-\(13\) minor shows that their gcd is exactly \(13\). The determinant-one eight-by-eight minor shows that the gcd of all eight-by-eight minors is \(1\). These determinantal divisors, together with rank nine, prove that the nonzero Smith invariant factors of \(M\) are
\[
1,1,1,1,1,1,1,1,13.
\]
It follows that the full circle-valued phase kernel is isomorphic to \(\mathbb T^4\times\mathbb Z/13\mathbb Z\). The constructed family \(\zeta^{at}\Phi(t^4)\) is itself an embedded subgroup of that size and dimension: its \(13\) additive-character cosets are distinct, because \(\zeta^{at}\) for nonzero \(a\) is not constant on a nonzero fourth-power fiber. A closed four-torus subgroup of a four-torus has to equal its connected component, so the constructed subgroup fills the entire kernel. This proves both exhaustiveness and uniqueness of the parametrization.

## Verification
Run `python3 artifacts/verify.py` using only the Python standard library. The script independently enumerates all \(91\) unordered input pairs; verifies the quartic-image difference set, the exact fiber histogram and energy \(445\); reconstructs the fifteen integer relations; performs exact fraction-free determinant calculations for the displayed eight-by-eight and nine-by-nine certificates; and computes the rank modulo \(13\). It also tests character-modulated quartic-image phases and a phase vector that violates an equality relation.

Expected output: `VERIFY_OK prime=13 fibers=76 nontrivial_fibers=15 energy=445 rank_Q=9 rank_mod13=8 delta8=1 delta9=13 phase_components=13 torus_dimension=4`.

These checks are exhaustive for the one finite field specified in the theorem. No extrapolation from a finite list of fields is made.

## Relationship to prior work
Mockenhaupt--Tao (arXiv:math/0204234, first posted 2002-04-18) established the finite-field Fourier restriction setting and the character-orthogonality framework. Their detailed restriction discussion concerns general phenomena, cones, and paraboloids, not the present phase-only quartic equality classification.

The published *Exact additive energy of the finite-field quartic graph* (published-finding corpus, 2026) establishes the fourth-moment of the constant function for all fields of characteristic greater than three. Its complete finding and proof were inspected. It explicitly does **not** determine a sharp unrestricted extension constant, and it does not determine the unimodular equality-phase subgroup at thirteen elements. Its energy formula specializes to \(445\), so the numerical maximum alone is **not** presented as new. The new assertion is the exhaustive thirteen-component torus classification.

The published *Small-field phase dichotomy for anisotropic sphere extremizers* (published-finding corpus, 2026) uses integer relation lattices to classify phases for two finite-field spheres. Its complete proof was inspected. Those objects are six- and twenty-point quadratic surfaces, not the thirteen-point quartic graph; neither its relation lattice nor its conclusion implies the present classification. A published four-point-support theorem about the **minimum** fourth Fourier moment (published-finding corpus, 2026) concerns a different optimization direction and a different support.

## Limitations
The theorem concerns only unimodular coefficients, not arbitrary amplitudes or the unrestricted extension operator norm. It treats precisely the thirteen-element prime field. It does not assert a classification for other fields or prove maximal Fourier concentration without the fixed-modulus condition. The finite Smith computation is an exhaustive certificate at thirteen elements, not a general structural theorem about all quartic graphs. Although inspected sources do not cover the exact phase classification, a differently formulated older result in finite-field difference-set or phase-retrieval literature could remain undiscovered. No independent external mathematical audit has been performed.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1, first public version 2002-04-18; Duke Math. J. 121 (2004), 35--74.
2. *Exact additive energy of the finite-field quartic graph*, publicly indexed mathematical finding, published-finding corpus (2026), with the quartic-graph energy formula \(3q^2-5q+3\) for \(q\equiv1\pmod3\).
3. *Small-field phase dichotomy for anisotropic sphere extremizers*, publicly indexed mathematical finding, published-finding corpus (2026).
4. J. Singer, *A theorem in finite projective geometry and some applications to number theory*, Trans. Amer. Math. Soc. 43 (1938), 377--385, DOI 10.1090/S0002-9947-1938-1501951-4. The finite difference-set calculation used above is checked directly; no result is imported from this reference.
