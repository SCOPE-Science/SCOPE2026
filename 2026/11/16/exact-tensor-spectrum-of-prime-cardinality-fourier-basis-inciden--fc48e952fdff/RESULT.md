# Exact tensor spectrum of prime-cardinality Fourier-basis incidence on squarefree cycles

## Finding
Let \(N\ge6\) be squarefree, let \(p\) be its least prime divisor, and write \(N=pQ\), where the distinct prime divisors of \(Q\) form \(\mathcal P\). A \(p\)-element subset of \(\mathbb Z/N\mathbb Z\) is called *spectral* if the characters of some \(p\)-element frequency set form an orthogonal basis of its complex function space. The complete collection \(\mathcal T\) of spectral subsets is precisely the collection of transversals of reduction modulo \(p\), and \(|\mathcal T|=Q^p\).

Define the symmetric \(Q^p\)-by-\(Q^p\) incidence matrix
\[
\mathcal I_{A,B}=\begin{cases}1,&\displaystyle\sum_{a\in A}e^{2\pi i a(b-b')/N}=0\quad\text{for all distinct }b,b'\in B,\\0,&\text{otherwise},\end{cases}\qquad A,B\in\mathcal T.
\]
For each \(q\in\mathcal P\), put
\[
\lambda_q^\pm=\frac{q\pm\sqrt{4q^{p+1}-3q^2}}2.
\]
**The complete eigenvalue multiset** of \(\mathcal I\) is
\[
\left\{\prod_{q\in\mathcal P}\lambda_q^{\varepsilon(q)}:\varepsilon:\mathcal P\to\{+,-\}\right\}\quad\cup\quad\{0\text{ with multiplicity }Q^p-2^{|\mathcal P|}\}.
\]
Products are taken as a multiset, so any accidental eigenvalue coincidences retain their multiplicity. In particular,
\[
\boxed{\operatorname{rank}\mathcal I=2^{|\mathcal P|}},\qquad
\boxed{\#\{(A,B)\in\mathcal T^2:\mathcal I_{A,B}=1\}=\prod_{q\in\mathcal P}(2q^{p+1}-q^2)}.
\]
Equivalently, the nonzero singular values are the absolute values of the stated eigenvalue products. The result classifies **all ordered prime-cardinality spectral pairs**, not merely the existence of one Fourier basis.

## Assumptions and scope
All finite sets are ordinary subsets, not multisets; a spectrum is counted without ordering its elements. No quotient by translation, reflection or group automorphisms is taken. The standard normalized Fourier matrix on \(A\times B\) has entries \(p^{-1/2}\exp(2\pi iab/N)\). The claim applies to **every** squarefree \(N\) with at least two distinct prime divisors and \(p\) its **least** prime divisor. The restriction to least prime is essential to the root-of-unity lemma below. The primes dividing \(Q\) are therefore strictly larger than \(p\).

Using the Chinese remainder theorem, each transversal \(A\) is identified with a collection of tuples \(a_q=(a_{q,0},\ldots,a_{q,p-1})\in(\mathbb Z/q\mathbb Z)^p\) indexed by \(q\in\mathcal P\), with \(a_{q,j}\) the residue modulo \(q\) of the unique element of \(A\) congruent to \(j\) modulo \(p\). The same notation is used for \(B\). An exact spectral-pair criterion is
\[
\mathcal I_{A,B}=1\quad\Longleftrightarrow\quad
\forall q\mid Q:\quad a_q\text{ is constant}\ \text{or}\ b_q\text{ is constant}.
\]

## Proof
**1. A shortest vanishing-sum lemma.** For squarefree \(n\) with least prime divisor \(p\), any vanishing sum of \(k\le p\) (not necessarily distinct) \(n\)-th roots of unity has \(k=p\), and those roots are one rotated complete \(p\)-gon. We prove this by induction on the number of prime factors. For \(n=p\), the cyclotomic polynomial \(1+X+\cdots+X^{p-1}\) is the unique rational relation, up to scale, among the \(p\) powers of a primitive \(p\)-th root; nonnegative multiplicities and total length at most \(p\) force precisely one occurrence of each root. In the induction step, choose any prime \(q\mid n\) with \(q>p\), and set \(m=n/q\). The roots \(1,\zeta_q,\ldots,\zeta_q^{q-1}\) have exactly one linear relation over \(\mathbb Q(\zeta_m)\), namely their sum, since \([\mathbb Q(\zeta_n):\mathbb Q(\zeta_m)]=q-1\). Group the \(k<q\) summands according to their \(q\)-coordinate. One coordinate is absent. Hence all coefficients (sums of \(m\)-th roots) must separately vanish. By induction every nonempty group has at least \(p\) elements, so only one group is present, of length exactly \(p\); induction also makes it a rotated \(p\)-gon. Repeating for each \(q>p\) establishes the lemma. In CRT terms, all coordinates at primes other than \(p\) are fixed, and the \(p\)-coordinate takes each value once.

**2. Exact pair compatibility.** Suppose \(A,B\) have \(p\) elements and give an orthogonal Fourier matrix. For distinct \(b,b'\in B\), orthogonality gives a vanishing sum of exactly \(p\) \(N\)-th roots with exponents \(a(b-b')\), \(a\in A\). The lemma forces \(b-b'\not\equiv0\pmod p\), hence \(B\) is a transversal modulo \(p\); it likewise forces \(A\) to be a transversal. For each \(q\mid Q\), if \(A\) has two distinct residues modulo \(q\), the lemma forces \(q\mid b-b'\) for every distinct \(b,b'\in B\); equivalently, \(B\) is constant modulo \(q\). Interchanging \(A,B\) yields the condition for all \(q\). Conversely, if both are modulo-\(p\) transversals and, for every \(q\mid Q\), at least one of their \(q\)-tuples is constant, then for any distinct \(b,b'\), the \(p\) exponents \(a(b-b')\) are distinct modulo \(p\) and constant modulo every \(q\mid Q\). They constitute a rotated complete \(p\)-gon, so the Fourier columns are orthogonal. They are \(p\) nonzero orthogonal columns in a \(p\)-dimensional space, hence form a basis. Taking \(B\) to be any translate of the unique subgroup of order \(p\) shows every modulo-\(p\) transversal is spectral.

**3. Tensor factorization and full spectrum.** The CRT labels \(\mathcal T\) bijectively by \(\prod_{q\mid Q}(\mathbb Z/q\mathbb Z)^p\). The pair criterion implies \(\mathcal I\) is permutation-similar to \(\bigotimes_{q\mid Q}M_q\), where \((M_q)_{u,v}=1\) if \(u\) or \(v\) is constant, and zero otherwise. Among the \(q^p\) tuples, exactly \(q\) are constant. With normalized indicators of the constant and nonconstant classes, \(M_q\) acts via the real symmetric matrix
\[
\begin{pmatrix}
q&\sqrt{q(q^p-q)}\\
\sqrt{q(q^p-q)}&0
\end{pmatrix}
\]
and vanishes on the orthogonal complement. Its characteristic polynomial on this two-dimensional subspace is \(x^2-qx-q(q^p-q)\). Since \(p\ge2\) and \(q>p\), both roots \(\lambda_q^\pm\) are nonzero. Tensor-product spectral theory yields the complete stated multiset and rank.

**4. Ordered pair count.** In the \(q\)-coordinate, the admissible pairs of tuples comprise all pairs with the first constant (\(q\cdot q^p\) choices), plus those with the second constant (another \(q^p\cdot q\) choices), minus the \(q^2\) pairs counted twice. Independence across CRT factors gives exactly \(\prod_{q\mid Q}(2q^{p+1}-q^2)\) compatible ordered pairs.

## Verification
The standalone `CHECK.py` performs cyclotomic-integer reductions for the Fourier orthogonality sums rather than assuming the proposed coordinate criterion. It exhaustively compares direct orthogonality with the theorem for \(N=6,10,15,21,30,42\), involving exactly **379086 ordered candidate pairs**. It independently compares all predicted row degrees and pair counts, numerically diagonalizes each full incidence matrix to test the exact eigenvalue formulas, and performs **1200 additional exact root-of-unity checks** for \(N=105\) using deterministic pseudorandom sampling. All passed. The proof above, not the finite checks, establishes the infinite family.

For \(N=30\), the least prime is \(p=2\) and \(Q=15\). There are \(15^2=225\) spectral two-point sets, the spectral-pair incidence matrix has rank exactly \(4\), and the number of ordered compatible pairs is \((2\cdot3^3-3^2)(2\cdot5^3-5^2)=45\cdot225=10125\).

Reproduction: install Python 3, SymPy and NumPy, then execute `python CHECK.py`. The computation needs no network access.

## Relationship to prior work
Lam and Leung (1995/2000) establish a general theory of vanishing sums of roots of unity; the short-sum lemma here is proved independently and specializes this classical theory. Malikiosis (2022) and Kiss–Malikiosis–Somlai–Vizer (2022) establish powerful Fourier-zero and spectral/tiling structures for finite cyclic groups. Tan and Zhang (first public preprint September 9, 2026) establish a general squarefree-order Fuglede theorem and a prime-coordinate elimination method. The present result isolates a different numerical invariant: the **entire spectrum of the global incidence operator between all prime-cardinality spectral subsets**, including its unexpectedly small exact rank and complete eigenvalue products, not just the existence or classification of one spectral partner.

## Limitations
The exact formulas apply only at the **least-prime cardinality** and to **squarefree cyclic order**. They do not classify larger spectral sets, repeated prime factors, or arbitrary noncyclic groups. The checker's numerical eigenspectrum tests supplement, but do not replace, the exact tensor proof. A complete comparison against the full text of the 2026 Tan–Zhang preprint was unavailable at the time of this assessment; equivalence to uninspected prior spectral-incidence formulas remains a bibliographic risk.

## References
1. H. Tan and Y. Zhang, *Fuglede's Conjecture for Cyclic Groups of Square-free Order*, arXiv:2610.02218 (first submitted 2026-09-09), https://arxiv.org/abs/2610.02218.
2. R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, Forum of Mathematics, Sigma 10 (2022), e23, DOI:10.1017/fms.2022.14, https://doi.org/10.1017/fms.2022.14.
3. G. Kiss, R. D. Malikiosis, G. Somlai and M. Vizer, *Fuglede's Conjecture Holds for Cyclic Groups of Order pqrs*, Journal of Fourier Analysis and Applications 28 (2022), 79, DOI:10.1007/s00041-022-09972-0, https://doi.org/10.1007/s00041-022-09972-0.
4. T. Y. Lam and K. H. Leung, *On vanishing sums of roots of unity*, Journal of Algebra 224 (2000), 91–109, DOI:10.1006/jabr.1999.8089; preprint arXiv:math/9511209.
