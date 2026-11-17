# Exact cyclic one-step image enumeration for cellular automaton Rule 110

## Finding

Let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be the indexed binary cyclic update of elementary cellular automaton Rule 110, for every integer \(n\ge1\). Write \(a_n=|\operatorname{im}F_n|\), with a formal generating-series constant coefficient \(a_0=0\). Then

\[
\sum_{n\ge1}a_n z^n=\frac{z(1-2z+3z^2-3z^3+3z^4-6z^5+6z^6-2z^7+z^8+z^9)}{(1-z)(1-z-z^4)(1-2z+z^2-z^3-z^4)}.
\]

In particular, the number of outputs without a same-length cyclic predecessor is exactly \(2^n-a_n\), and

\[
(a_1,\ldots,a_{18})=(1,2,5,10,22,41,79,154,302,582,1113,2125,4058,7737,14725,27994,53195,101048).
\]

If \(\rho\) is the unique positive root of \(1-2z+z^2-z^3-z^4\), then \(\rho\in(0.527,0.528)\) and
\[
a_n=\rho^{-n}+O((3/2)^n),\qquad \lim_{n\to\infty}\frac{\log_2 a_n}{n}=\log_2(1/\rho)\approx0.9238561093.
\]
This last value measures the exponential growth of the *one-step spatial image* on periodic rings, not temporal metric entropy or the entropy of the Rule 110 limit set.

## Assumptions and scope

The local rule is \(f(000)=f(100)=f(111)=0\), and \(f(001)=f(010)=f(011)=f(101)=f(110)=1\). For \(x\in\{0,1\}^n\), the output at indexed position \(i\) is \(f(x_{i-1},x_i,x_{i+1})\), with every index taken modulo \(n\). Inputs and outputs are indexed, not identified under rotation or reflection. The same rule applies at \(n=1,2\), including repeated neighbors. The image count distinguishes outputs, not the number of their predecessors.

## Proof

**1. Cyclic predecessor criterion.** Use the four states \(00,01,10,11\). For \(b\in\{0,1\}\), define a Boolean \(4\times4\) adjacency matrix \(A_b\): its entry from the state \(uv\) to \(vw\) is \(1\) precisely when \(f(u,v,w)=b\), and all other entries are zero. Multiplication here is over the Boolean semiring. Every word \(y_0\cdots y_{n-1}\) has a length-\(n\) cyclic predecessor precisely when \(A_{y_0}\cdots A_{y_{n-1}}\) has at least one nonzero diagonal entry. A closed walk encodes the predecessor's overlapping pairs, including both wrap-around constraints; conversely every predecessor gives a closed walk. This is valid also at lengths one and two.

**2. The finite relation transfer.** Encode each Boolean matrix by its row-major \(16\)-bit integer. The masks obtained directly from the rule table are \(A_0=33025\) and \(A_1=17090\); the identity mask is \(33825\). Right multiplication by the two masks, starting from the identity, reaches exactly \(75\) distinct Boolean relations. Order them by deterministic breadth-first discovery and let \(T\) be the \(75\times75\) integer matrix in which each relation has one directed labeled edge for multiplication by \(A_0\) and one for multiplication by \(A_1\), counting both if they coincide. Use the column-propagating convention \(T_{\mathrm{target},\mathrm{source}}\) for the adjacency matrix. Let \(e\) select the identity relation and \(h\) indicate relations with a nonzero diagonal. The criterion in step 1 proves
\[
a_n=h^{\mathsf T}T^ne\quad(n\ge1).
\]
The definitions of \(T,e,h\), including the entire reachable relation set, are reconstructed without a stored table by `verify_relation.py`.

**3. Exact all-length rational identity.** Set
\[
Q(z)=1-4z+6z^2-5z^3+z^4+4z^5-4z^6+2z^7-z^9,
\]
\[
P(z)=z-2z^2+3z^3-3z^4+3z^5-6z^6+6z^7-2z^8+z^9+z^{10}.
\]
An integer-vector transfer calculation gives \(75\) consecutive zero values of
\[
r_n=\sum_{j=0}^{9}[z^j]Q(z)\,a_{n-j},\quad 11\le n\le85.
\]
It also yields \(\sum_{j=0}^{\min(n,9)}[z^j]Q(z)a_{n-j}=[z^n]P(z)\) for \(1\le n\le10\). These are exact integer equalities checked by `verify_relation.py`, which reconstructs all masks and transitions and does not use modular arithmetic or floating point.

For all \(n\ge10\), the sequence \(r_n\) has the form \(h^{\mathsf T}T^{n-9}v\) for a fixed integer vector \(v\), because the recurrence coefficients form a fixed polynomial in \(T\). By Cayley–Hamilton, every such scalar sequence satisfies a recurrence of order at most \(75\). Its \(75\) consecutive zeros at \(n=11,\ldots,85\) therefore force \(r_n=0\) for all \(n\ge11\). Together with the initial ten identities, this proves \(\sum_{n\ge1}a_nz^n=P(z)/Q(z)\) as a formal rational identity. Direct integer polynomial multiplication gives
\[
Q(z)=(1-z)(1-z-z^4)(1-2z+z^2-z^3-z^4).
\]

**4. Growth and the leading coefficient.** Put \(E(z)=z^4+z^3-z^2+2z-1\). Its discriminant is \(-751\), so it has two real roots and one conjugate pair; rational sign tests locate the two real roots in \((0.527,0.528)\) and \((-2.067,-2.065)\). Since their product with the squared modulus of the conjugate roots is \(-1\), the latter modulus exceeds \(\sqrt{1/(0.528\cdot2.067)}>2/3\). On \(|z|\le2/3\), the factor \(1-z-z^4\) cannot vanish because \(|z+z^4|\le2/3+16/81<1\); neither can \(1-z\). Thus the positive root \(\rho\) is the only denominator zero in \(|z|\le2/3\), and it is simple. The exact polynomial identity
\[
P(z)+zQ'(z)=z(z-1)(z^4-8z^3+z-3)E(z)
\]
shows that the coefficient of the simple pole at \(\rho\) is exactly one in the expansion \(1/(1-z/\rho)\). Cauchy coefficient bounds for the remaining rational function give \(a_n=\rho^{-n}+O((3/2)^n)\), proving the stated exponential rate.

## Verification

Run `python3 verify_relation.py` (the \(75\)-state Boolean-semiring construction, all \(75\) recurrence residuals, factorization and pole-residue algebra) and `python3 verify_direct.py` (independent direct evolution and distinct-output enumeration on every indexed cyclic ring of sizes \(1\) through \(18\)). Both require only the Python standard library. The second program checks \(2^{18}\) inputs at the largest ring size; it corroborates but does not replace the infinite-length proof in step 3.

## Relationship to prior work

Jen's 1989 paper derives formulae for individual preimage counts of one-dimensional nearest-neighbor cellular automata, and Mora–Martínez–McIntosh's 2004 work develops ancestor algorithms and Rule 110 subset diagrams. The 2007 Rule 110 glider-language study derives regular sublanguages using de Bruijn diagrams. Those constructions supply methodological context, but the inspected material does not give the above all-length *distinct cyclic image* generating function or its dominant root. A public finite-ring census tabulates Rule 110 orphan counts at lengths eight and sixteen, agreeing with \(256-154=102\) and \(65536-27994=37542\), without an all-length enumeration. These finite checks are previous evidence, not claimed new. The distinction from individual preimage multiplicities and from infinite-line excluded finite factors is essential.

## Limitations

The result is for exactly one update on finite indexed binary periodic rings, not the number of multistep ancestors, limit-set complexity, or a universal formula for arbitrary cellular automata. Earlier general preimage methods can decide individual cases but are not the explicit enumerator established here. Other, possibly unindexed, historical enumerations of this particular sequence or equivalent rational function may exist; the novelty assessment is not an independent priority certification.

## References

1. E. Jen, *Enumeration of Preimages in Cellular Automata*, Complex Systems **3** (1989), 421–456, https://www.complex-systems.com/abstracts/v03_i05_a02/ .
2. J. C. Seck Tuoh Mora, G. Juárez Martínez, H. V. McIntosh, *Calculating ancestors in one-dimensional cellular automata* (revised March 2004), https://www.comunidad.escom.ipn.mx/genaro/Papers/Papers_on_CA_files/ancestorsECA.pdf .
3. G. Juárez Martínez, H. V. McIntosh, J. C. Seck Tuoh Mora, S. V. Chapa Vergara, *Determining a regular language by glider-based structures called phases in Rule 110*, arXiv:0706.3348v1, 2007-06-22, https://arxiv.org/abs/0706.3348 .
4. M. Cook, *A Concrete View of Rule 110 Computation*, arXiv:0906.3248v1, 2009-06-17, https://arxiv.org/abs/0906.3248 .
5. *Gardens of Eden — Elementary CA Zoo*, finite one-step orphan census, https://cellular.solves.ca/gardens-of-eden (accessed 2026-11-03 UTC).
