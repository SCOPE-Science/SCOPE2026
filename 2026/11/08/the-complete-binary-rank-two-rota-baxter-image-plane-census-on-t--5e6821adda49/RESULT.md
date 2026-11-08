# The complete binary rank-two Rota–Baxter image-plane census on \(T_3(\mathbb F_2)\)

## Finding
Let \(A=T_3(\mathbb F_2)\), the six-dimensional algebra of upper-triangular three-by-three matrices over the two-element field. A *weight-zero Rota–Baxter operator* is an \(\mathbb F_2\)-linear endomorphism \(P:A\to A\) obeying
\[
P(x)P(y)=P(P(x)y+xP(y))\quad\text{for all }x,y\in A.
\]
Among operators of **linear rank exactly two**, the number of *distinct operators* is
\[
\boxed{652.}
\]
More precisely, there are \(651\) two-dimensional image subspaces \(U\le A\), and the distribution of image fibers
\(f(U)=|\{P:\operatorname{im}P=U,\ \operatorname{rank}P=2,\ P\text{ satisfies the identity}\}|\)
is the following complete enumeration:

| Operators per image plane \(f(U)\) | Number of planes \(U\) |
| ---: | ---: |
| 0 | 593 |
| 3 | 24 |
| 4 | 8 |
| 5 | 16 |
| 6 | 8 |
| 210 | 2 |

The two maximum-fiber planes are exactly \(\langle E_{12},E_{13}\rangle\) and \(\langle E_{13},E_{23}\rangle\), where \(E_{ij}\) are standard matrix units. In particular, exactly \(58\) image planes support any rank-two weight-zero Rota–Baxter operator. Exactly \(100\) of the \(651\) planes are multiplicatively closed, and all \(58\) realizable images are among these.

## Assumptions and scope
All computations are over \(\mathbb F_2\), not over a characteristic-zero or algebraically closed field. The operator rank is its ordinary vector-space rank on the **six-dimensional** space \(A\). Images are **literal embedded two-dimensional subspaces**; operators are counted without quotienting by conjugation or scaling. The only field order treated is two. We use the ordered basis \((E_{11},E_{12},E_{13},E_{22},E_{23},E_{33})\). The standard multiplication is \(E_{ij}E_{kl}=\delta_{jk}E_{il}\).

## Proof
This is a finite exhaustive proof with a compact complete search space; the two standalone source files implement the exhaustion by different parameterizations. Every integer bound and the coverage of every map are justified here, rather than inferred from sample data.

**Canonical enumeration of image planes.** Identify \(A\) with \(\mathbb F_2^6\), encoding a vector as a six-bit integer in the fixed matrix-unit basis. Every two-dimensional subspace \(U\) has exactly three nonzero vectors \(\{u,v,u\mathbin\oplus v\}\). Order their integer encodings and take the two smallest \(u<v\) as the **unique canonical basis** of \(U\). Enumerate all integers \(1\le u<v\le63\) and retain exactly the pairs for which \(v<u\mathbin\oplus v\). This enumerates each plane exactly once, because the two smallest nonzero elements are linearly independent over the binary field. The number is
\[
\frac{(2^6-1)(2^6-2)}{(2^2-1)(2^2-2)}=651.
\]

**Canonical enumeration of rank-two maps.** Fix a canonical basis \(u,v\) of \(U\). Every linear map with image exactly \(U\) is uniquely
\[
P(z)=\alpha(z)u+\beta(z)v,
\]
where \(\alpha,\beta\) are linearly independent binary linear functionals on the six-dimensional input. Encoding the functionals by two bit masks \(a,b\in\{1,\ldots,63\}\), linear independence over \(\mathbb F_2\) is exactly \(a\ne b\). Hence there are precisely \(63\cdot62=3906\) rank-two maps with a given image \(U\), for an exhaustive total of
\[
651\cdot3906=2,542,806
\]
distinct rank-two linear operators. No map appears twice, because its image is unique and its two coefficient functionals for the canonical basis are unique.

**Exact equation test.** Matrix multiplication is bilinear, \(P\) is linear, and therefore each side of the weight-zero Rota–Baxter identity is bilinear in the two independent arguments. Consequently the identity holds for **all** \(x,y\in A\) if and only if it holds for the \(36\) ordered pairs \((E_i,E_j)\) of the displayed basis. The first verifier constructs the complete binary multiplication table from \(E_{ij}E_{kl}=\delta_{jk}E_{il}\), enumerates every canonical plane and every independent functional pair, then computes the two sides of all \(36\) basis-pair equations using binary exclusive-or and population-count parity. No numerical tolerance, random sample, or unproved algebraic pruning is involved. Its six fiber-frequency integers are exactly
\[
(593,24,8,16,8,2)
\]
at fiber sizes \((0,3,4,5,6,210)\). The number of passing operators, computed as \(24\cdot3+8\cdot4+16\cdot5+8\cdot6+2\cdot210\), is \(652\).

**Independent exhaustive coordinate test.** The second verifier independently constructs the same multiplication as ordinary \(3\times3\) binary matrix multiplication. For each image plane it enumerates all \(4^6\) choices for the six images of the basis vectors among \(0,u,v,u+v\); it retains those choices that span the image plane and directly constructs the full \(64\)-entry map by binary linearity. It then tests the identical \(36\) defining equations. This parameterization again checks exactly \(3906\) rank-two maps per plane, and independently returns the same complete fiber distribution and total. The two traversals use distinct representations of the linear maps and independently implemented multiplication.

**The large fibers.** The checker records exactly two planes with fiber size \(210\), namely \(\langle E_{12},E_{13}\rangle\) and \(\langle E_{13},E_{23}\rangle\). Each is a square-zero two-sided ideal of \(A\). For either plane \(U\), any surjection \(P:A\twoheadrightarrow U\) whose kernel contains \(U\) automatically satisfies the Rota–Baxter identity: both products of images vanish and \(P(P(x)y+xP(y))=0\) because \(UA+AU\subseteq U\). Such surjections correspond to surjections \(A/U\to U\), and there are exactly \((2^4-1)(2^4-2)=210\). This matches and explains the two exceptional fibers without depending on the enumeration.

The programs are fully specified, finite, terminating constructive certificates for the six output counts. Reproducing the binary loops and matrix products verifies the exact census. \(\square\)

## Verification
Compile and run both standalone C++17 files, for example with

`g++ -std=c++17 -O2 verify.cpp -o verify && ./verify`

and

`g++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`.

Both check \(651\) image planes, \(2,542,806\) rank-two linear maps, and output the same six fiber frequencies and the total \(652\); each terminates with `VERIFY_OK`. The first also counts \(100\) multiplicatively closed planes and identifies \(58\) nonzero fibers and the two named maximum-fiber planes. The second uses all \(64\) domain vectors in constructing each linear map and tests all defining basis equations. The verification is **exhaustive** for this finite domain, not a claim about larger fields or higher-dimensional triangular algebras.

## Relationship to prior work
Gubarev's *Rota-Baxter operators of weight zero on upper-triangular matrices of order three* (arXiv:2404.00289v1, 30 March 2024) studies exactly the same algebraic multiplication and identity, but over **characteristic-zero fields**. Its main classification is expressed through representative families up to automorphism, antiautomorphism, and nonzero scalar rescaling; it does not give this binary-field rank-two operator count or the complete distribution over literal image subspaces. General results on unital-algebra Rota–Baxter operators (arXiv:1805.00723) and field-product operator enumerations (arXiv:1811.08219) likewise do not supply the present finite binary census. Prior rank-one counting over triangular algebras is stronger for rank one, but does not cover the rank-two count.

## Limitations
This is a natural **finite exact cutoff**, not a theorem for all finite fields. The count is proved by exhaustive finite arithmetic with two reproducible algorithms; there is no closed symbolic classification of the \(58\) image planes beyond the complete recorded fiber histogram. A future larger-field treatment might subsume this result. Published-literature overlap was checked against relevant accessible sources and mathematical indexing, but priority is provisional; independent human mathematical audit has not been performed.

## References
1. V. Gubarev, *Rota-Baxter operators of weight zero on upper-triangular matrices of order three*, arXiv:2404.00289v1 (30 March 2024), https://arxiv.org/abs/2404.00289 .
2. V. Gubarev, *Rota-Baxter operators on unital algebras*, arXiv:1805.00723 (2018), https://arxiv.org/abs/1805.00723 .
3. V. Gubarev, *Rota-Baxter operators on a sum of fields*, arXiv:1811.08219 (2018), https://arxiv.org/abs/1811.08219 .
