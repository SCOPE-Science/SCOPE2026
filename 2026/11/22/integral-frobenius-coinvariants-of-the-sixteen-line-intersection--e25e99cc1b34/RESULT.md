# Integral Frobenius coinvariants of the sixteen-line intersection map on degree-four del Pezzo surfaces

## Finding

Let \(X/\mathbb F_q\) be any smooth degree-four del Pezzo surface, where \(q\) is an odd prime power. Let \(\mathcal L\) be its sixteen geometric exceptional curves. On the free integer module \(M=\mathbb Z^{\mathcal L}\), define the unsigned intersection-adjacency operator

\[
A(e_D)=\sum_{E\in\mathcal L,\; E\ne D,\; D\cdot E=1}e_E.
\]

Write \(C=\operatorname{coker}(A)\). Arithmetic Frobenius \(F\) preserves the intersection pairing and acts on \(C\). Its integral coinvariant group is \(C_F=C/(F-1)C\). Then the geometric Smith form and cokernel are

\[
\operatorname{SNF}(A)=\operatorname{diag}(1^{11},3^4,15),\qquad
C\simeq(\mathbb Z/3\mathbb Z)^4\oplus\mathbb Z/15\mathbb Z.
\]

The arithmetic groups \(C_F\) have **exactly the following six possible abstract forms across the eighteen Weyl signed-cycle types**: \(\mathbb Z/5\mathbb Z\), \(\mathbb Z/15\mathbb Z\), and \((\mathbb Z/3\mathbb Z)^a\oplus\mathbb Z/15\mathbb Z\) for \(1\le a\le4\). The complete type-by-type classification follows. A signed cycle \(\ell_+\) or \(\ell_-\) has length \(\ell\) and positive or negative total sign, respectively; every type has an even number of negative cycles.

| Signed-cycle type | Weyl elements | Coinvariant group |
|---|---:|---|
| \(1_+,\,1_+,\,1_+,\,1_+,\,1_+\) | 1 | \((\mathbb Z/3\mathbb Z)^{4}\oplus\mathbb Z/15\mathbb Z\) |
| \(1_+,\,1_+,\,1_+,\,1_-,\,1_-\) | 10 | \((\mathbb Z/3\mathbb Z)^{2}\oplus\mathbb Z/15\mathbb Z\) |
| \(1_+,\,1_+,\,1_+,\,2_+\) | 20 | \((\mathbb Z/3\mathbb Z)^{3}\oplus\mathbb Z/15\mathbb Z\) |
| \(1_+,\,1_+,\,1_-,\,2_-\) | 60 | \(\mathbb Z/3\mathbb Z\oplus\mathbb Z/15\mathbb Z\) |
| \(1_+,\,1_+,\,3_+\) | 80 | \((\mathbb Z/3\mathbb Z)^{2}\oplus\mathbb Z/15\mathbb Z\) |
| \(1_+,\,1_-,\,1_-,\,1_-,\,1_-\) | 5 | \(\mathbb Z/15\mathbb Z\) |
| \(1_+,\,1_-,\,1_-,\,2_+\) | 60 | \(\mathbb Z/3\mathbb Z\oplus\mathbb Z/15\mathbb Z\) |
| \(1_+,\,1_-,\,3_-\) | 160 | \(\mathbb Z/15\mathbb Z\) |
| \(1_+,\,2_+,\,2_+\) | 60 | \((\mathbb Z/3\mathbb Z)^{2}\oplus\mathbb Z/15\mathbb Z\) |
| \(1_+,\,2_-,\,2_-\) | 60 | \(\mathbb Z/15\mathbb Z\) |
| \(1_+,\,4_+\) | 240 | \(\mathbb Z/3\mathbb Z\oplus\mathbb Z/15\mathbb Z\) |
| \(1_-,\,1_-,\,1_-,\,2_-\) | 20 | \(\mathbb Z/5\mathbb Z\) |
| \(1_-,\,1_-,\,3_+\) | 80 | \(\mathbb Z/15\mathbb Z\) |
| \(1_-,\,2_+,\,2_-\) | 120 | \(\mathbb Z/15\mathbb Z\) |
| \(1_-,\,4_-\) | 240 | \(\mathbb Z/5\mathbb Z\) |
| \(2_+,\,3_+\) | 160 | \(\mathbb Z/3\mathbb Z\oplus\mathbb Z/15\mathbb Z\) |
| \(2_-,\,3_-\) | 160 | \(\mathbb Z/5\mathbb Z\) |
| \(5_+\) | 384 | \(\mathbb Z/15\mathbb Z\) |


In particular, Weyl actions whose sixteen exceptional curves have **identical** Frobenius orbit partition \((4,4,4,4)\) yield three distinct coinvariant groups, namely \(\mathbb Z/5\mathbb Z\), \(\mathbb Z/15\mathbb Z\), and \(\mathbb Z/3\mathbb Z\oplus\mathbb Z/15\mathbb Z\). The partition \((2,2,2,2,2,2,2,2)\) likewise yields three distinct groups. These are statements about arithmetic actions on the canonical line-intersection module, not claims that each type occurs over every fixed finite field.

## Assumptions and scope

The result applies to each smooth degree-four del Pezzo surface over an odd finite field, independently of the surface's rationality, minimality, or existence of rational exceptional curves. Its sixteen geometric exceptional curves are defined over the algebraic closure and Frobenius acts through the Weyl group \(W(D_5)\). The theorem evaluates a **formal intersection-incidence cokernel**. It is not an assertion about torsion in the Picard group, the Brauer group, or the critical group of the graph (the last uses a graph Laplacian rather than \(A\)). The eighteen rows enumerate all possible abstract Weyl actions; no uniform fieldwise realizability assertion is made.

## Proof

**1. Canonical geometric matrix.** Over an algebraic closure write the surface as the blow-up of \(\mathbb P^2\) at five points in general position. In the standard Picard basis \(H,E_1,\ldots,E_5\), with intersection form \(H^2=1\), \(E_i^2=-1\), and other pairings zero, the sixteen exceptional curves are the five \(E_i\), the ten strict transforms \(L_{ij}=H-E_i-E_j\), and the strict transform \(C_0=2H-\sum_i E_i\). Distinct classes intersect either zero or once. Identify the sixteen classes with the odd-cardinality subsets of a five-element set: \(E_i\) corresponds to the singleton \(\{i\}\), \(L_{ij}\) to its three-element complement \(\{1,\ldots,5\}\setminus\{i,j\}\), and \(C_0\) to the full five-element subset. Substitution into the intersection form shows

\[
D\cdot E=1\quad\Longleftrightarrow\quad |m(D)\mathbin{\triangle}m(E)|=4
\quad(D\ne E).
\]

Thus \(A\) is the symmetric \(16\times16\) zero-one matrix whose entries are one exactly for odd-bit masks at Hamming distance four. Every row and column has five ones. This is the five-regular Clebsch graph, not its ten-regular complement.

**2. Arithmetic symmetry.** The Weyl group \(W(D_5)\) is the group of even signed permutations on five coordinates; it has \(2^4\cdot5!=1920\) elements. It acts on odd-subset masks by first permuting the five coordinates and then toggling an even number of coordinate bits. The action preserves Hamming distance four, hence commutes with \(A\). This faithful 1920-element action is the full automorphism group of the sixteen-line intersection configuration. The Galois action of every \(X/\mathbb F_q\) belongs to this group. Each element is recorded by its signed cycle lengths, using a bit recording the parity of toggles around each coordinate cycle.

**3. Coinvariant reduction.** The coinvariant functor on integer modules is right-exact. Thus, if \(\mathcal O_1,\ldots,\mathcal O_s\) are Frobenius orbits on the sixteen curves, the coinvariant module \(M_F\) is free on one class for each orbit, and

\[
C_F\simeq\operatorname{coker}(B_F),\qquad
(B_F)_{ij}=\#\{D\in\mathcal O_i:D\cdot E_j=1\},\ E_j\in\mathcal O_j.
\]

The displayed integer is independent of the chosen representative \(E_j\), since Frobenius preserves intersections. This formula needs neither a rational exceptional curve nor an arithmetic trivialization of the line scheme.

**4. Exhaustive exact calculation and certificate.** The attached standard-library script `verify_clebsch.py` enumerates all \(5!\) permutations and all sixteen even five-bit flips. Before classification it verifies the sixteen Picard classes and every matrix entry against the intersection pairing. For each of all \(1920\) elements it checks that the induced permutation preserves \(A\), constructs the orbit-quotient matrix \(B_F\) using the displayed formula, and obtains its Smith diagonal by explicit integer row/column operations. In every case, the program tracks unimodular matrices \(U,V\) and checks \(UB_FV\) equals the diagonal, with positive divisible nonzero factors. It also verifies the full geometric Smith diagonal, the class sizes in the table, constancy on each signed-cycle type, and the two asserted same-orbit-profile distinctions. These are **finite exhaustive certificates**, rather than a computation from samples of surfaces. A second computation with SymPy's independent Smith implementation agrees with the table.

Since the Weyl group is finite and every actual Frobenius action lies in it, these verifications cover all surfaces under the stated assumptions. The exponent of each group divides fifteen from the geometric cokernel. In particular, summing coefficients modulo five gives a Frobenius-invariant quotient \(C_F\twoheadrightarrow\mathbb Z/5\mathbb Z\), because every column of \(A\) sums to five.

## Verification

Execute `python3 verify_clebsch.py` using Python version 3.9 or newer. It needs no external packages or data. It checks the geometric intersection encoding, all \(1920\) Weyl elements, and all integer normal-form certificates and gives the complete table. For a second independent Smith implementation, `python3 crosscheck_sympy.py` requires SymPy; its output is compared type by type. The given programs and stated matrix rule reconstruct the entire calculation from first principles, including the nonzero order-three classes and every order-five quotient. No computation about arbitrary rational surfaces beyond the universal Weyl action is assumed.

## Relationship to prior work

Jahnel–Schindler's work (first released 13 December 2017) reconstructs the sixteen lines and the full \(W(D_5)\) action, but its computed groups are Galois cohomology of open Picard lattices, with two- and four-primary Brauer phenomena, not the adjacency cokernel. Darwin (first released 9 May 2022) gives a quadratically enriched count of the sixteen lines, not integer adjacency coinvariants. Jahnel–Loughran enumerate line-orbit actions for arithmetic Hasse questions, not Smith forms. Classical graph sources provide the spectrum of the Clebsch adjacency matrix; its rational eigenvalues do not determine integer Smith factors or their Frobenius quotients. The evaluated six-group arithmetic classification and the equal-orbit distinctions are the result asserted here; the underlying line geometry and Weyl action are credited rather than claimed as discoveries.

## Limitations

This is a universal conditional-on-Frobenius-type classification, not a proof that every abstract signed cycle is represented by a surface over every individual field. All groups are integral incidence-module invariants; they do not imply nontrivial Brauer or Picard torsion. The priority search found no identical arithmetic table, but an unindexed older integral graph calculation could contain an equivalent result. An independent mathematical audit is not included.

## References

1. J. Jahnel and D. Schindler, *On the algebraic Brauer classes on open degree four del Pezzo surfaces*, arXiv:1712.04745, first publicly posted 2017-12-13, especially Section 2. https://arxiv.org/abs/1712.04745
2. C. Darwin, *A quadratically enriched count of lines on a degree 4 del Pezzo surface*, arXiv:2205.04456, first publicly posted 2022-05-09, especially Introduction and Theorem 1.2. https://arxiv.org/abs/2205.04456
3. J. Jahnel and D. Loughran, *The Hasse Principle for Lines on del Pezzo Surfaces*, International Mathematics Research Notices (2015), Section 3.7, https://doi.org/10.1093/imrn/rnv073
4. E. W. Weisstein, *Clebsch Graph*, MathWorld, https://mathworld.wolfram.com/ClebschGraph.html
