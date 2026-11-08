# Exact postulation and degree-six regularity of the 256 magic-square nodes

## Finding

Let \(V\subset\mathbb P^8_{\mathbb C}\) be the surface whose points are \(3\times3\) matrices of square roots of a magic square. Set \(Z=\operatorname{Sing}(V)_{\mathrm{red}}\) and \(S=\mathbb C[A,B,C,D,M,E,F,G,H]\), with \(I_Z\) the homogeneous saturated ideal of \(Z\). The surface has \(256\) ordinary double points, a fact established in the cited literature. The new result is their exact homogeneous postulation:

\[
\dim_{\mathbb C}(S/I_Z)_d=\begin{cases}
1,9,39,109,206,256 &\text{for }d=0,1,2,3,4,5\text{ in that order},\\
256&\text{for }d\ge5.
\end{cases}
\]

Equivalently,

\[
\operatorname{Hilb}_{S/I_Z}(t)=\frac{1+8t+30t^2+70t^3+97t^4+50t^5}{1-t},
\qquad \operatorname{reg}(I_Z)=6.
\]

Every prescribed complex assignment of values to the \(256\) nodes is realized by a homogeneous quintic, after choosing the standard projective evaluations. No quartic gives arbitrary interpolation. The first equations vanishing on the nodes but not on the whole surface occur in degree three. Precisely, \((I_Z)_3/(I_V)_3\) has dimension two and is spanned by \(BMG\) and \(DME\), respectively the product along the middle column and along the middle row of the matrix.

## Assumptions and scope

All schemes are over \(\mathbb C\), and the singular locus is taken with its **reduced** structure. The coordinates are arranged as

\[
\begin{pmatrix}A&B&C\\D&M&E\\F&G&H\end{pmatrix}.
\]

Writing \((x:y:z)\in\mathbb P^2\), the nine linear forms specifying the entries of the underlying magic square, in this order, are

\[
\begin{aligned}
&\ell_A=z-y,\quad\ell_B=x+y+z,\quad\ell_C=z-x,\\
&\ell_D=y-x+z,\quad\ell_M=z,\quad\ell_E=x-y+z,\\
&\ell_F=x+z,\quad\ell_G=z-x-y,\quad\ell_H=y+z.
\end{aligned}
\]

The variety \(V\) is defined by demanding that the nine squares of its coordinates equal these forms for some projective triple. This is equivalently the complete intersection of six independent diagonal quadrics in \(\mathbb P^8\). For \(d\ge0\), write \(h_Z(d)=\dim_{\mathbb C}(S/I_Z)_d\).

## Proof

**Step 1: Recover the reduced nodes.** The nine lines \(\ell_i=0\) in \(\mathbb P^2\) have exactly twelve ordinary double intersections and eight triple intersections, with no higher multiplicity. This is verified from the nine explicit coefficient triples by computing all \(36\) line-pair cross products, identifying their projective intersection points, and counting incident lines. Let a point of \(V\) have precisely \(r\) zero coordinates. The linearized equations for six independent linear relations among the coordinate squares have Jacobian rank

\[
6-r+\operatorname{rank}\{\ell_i: \text{coordinate }i\text{ is zero}\}.
\]

The line-arrangement check implies this rank is less than six exactly when \(r=3\) and the three vanishing forms meet at a triple point. Each such underlying point has six nonzero squared coordinates and therefore \(2^6/2=32\) distinct projective choices of signs. Hence \(Z\) comprises \(8\cdot32=256\) points, and no other point is singular. The cited geometric literature independently identifies all of them as ordinary double points. This argument uses only their reduced support, not the Jacobian scheme's length.

**Step 2: Parity-character separation.** For a homogeneous degree-\(d\) polynomial, partition monomials uniquely by the subset \(T\) of variables with odd exponent. Such a monomial is a product of one coordinate for every \(i\in T\), multiplied by a polynomial of degree \(k=(d-|T|)/2\) in the squared coordinates, with \(0\le|T|\le d\) and matching parity. Over each of the eight base triple points, the \(32\) projective sign choices form a character basis; distinct subsets \(T\) of the required parity give independent sign modes. The square-root prefactor is nonzero precisely when the underlying point has no zero in \(T\), and on those rows it is an invertible scalar. Therefore the exact evaluation rank is the sum, over these subsets, of ranks of ordinary matrices with rows indexed by the allowable triple points and columns by the degree-\(k\) multiset products of the nine forms \(\ell_i\), evaluated at those points.

**Step 3: Exhaustive finite exact calculation.** The full rank-block census below lists the triples \((|T|,k,\text{block rank})\) with their multiplicities, as computed by `verify_nodes.py` using rational Gaussian elimination and no floating-point arithmetic:

| \(d\) | Blocks, followed by multiplicities | Total rank |
|---|---|---:|
| 0 | \((0,0,1):1\) | 1 |
| 1 | \((1,0,1):9\) | 9 |
| 2 | \((0,1,3):1\), \((2,0,1):36\) | 39 |
| 3 | \((1,1,3):9\), \((3,0,1):82\) | 109 |
| 4 | \((0,2,6):1\), \((2,1,2):6\), \((2,1,3):30\), \((4,0,1):98\) | 206 |
| 5 | \((1,2,4):1\), \((1,2,5):4\), \((1,2,6):4\), \((3,1,1):20\), \((3,1,2):46\), \((3,1,3):16\), \((5,0,1):48\) | 256 |

The exhaustive list of at most \(\binom{9}{5}\) parity supports in each degree is generated from the defining forms, not from a hard-coded node table. Every matrix rank is determined over \(\mathbb Q\). Since evaluation at \(256\) points has rank \(256\) in degree five, it is onto. Choose any linear form avoiding this finite set. Multiplying quintic interpolants by its powers gives surjectivity in every degree \(d\ge5\).

**Step 4: Initial extra equations and regularity.** Since \(V\) is a complete intersection of six quadrics, its degree-three coordinate ring has dimension \(\binom{11}{3}-6\cdot9=111\). The node coordinate ring has dimension \(109\) there; the two additional independent cubic equations are \(BMG\) and \(DME\). Neither odd-exponent support survives on any of the eight triple bases, so both vanish on every node. The only two missing degree-three parity supports in the exhaustive census are precisely those products, proving independence modulo \(I_V\). The point ideal has \(H^1(\mathbb P^8,\mathcal I_Z(4))\ne0\) because degree-four evaluation has rank \(206<256\), whereas degree-five evaluation is onto and all higher evaluation is onto; higher cohomology in the relevant regularity range vanishes by the standard cohomology of projective space. Hence the Castelnuovo–Mumford regularity of \(I_Z\) is exactly six.

## Verification

Execute `python3 verify_nodes.py` with a Python 3 standard-library installation. It recomputes the line-intersection partition \((12\text{ double},8\text{ triple})\), the total \(256\) sign lifts, every rank block for degrees zero through five, the two missing cubic supports, and the degree-six regularity conclusion. The test has been executed successfully on the packaged source. The finite computation is exhaustive for the explicit eight-base-point problem; the all-degree conclusion follows mathematically from the nonvanishing-linear-form argument, not an unbounded experiment.

## Relationship to prior work

Auel and Singer (first arXiv version September 8, 2026, §§1.1–1.3) establish the six-quadric model, the full set of \(256\) nodes and its sign symmetries. Michaud-Rodgers (2019, slide 12) gives explicit singular-point representatives and the same node count; its introductory discussion of Hilbert polynomials concerns the **surface**, not the reduced singular-point ideal. Those foundational facts are attributed to the sources. The present claim is the exact Hilbert function, quintic interpolation threshold, cubic quotient, and regularity of the **reduced finite node set**. Searches of the primary texts and relevant existing public research records did not reveal an equivalent graded-postulation calculation; search failure is not a proof of priority.

## Limitations

The formula is proved over \(\mathbb C\) for the reduced node set, not its nonreduced Jacobian singular scheme, nor for all characteristics. The full minimal graded Betti table of \(I_Z\) is not determined. The 2019 lecture and the 2026 preprint predate this calculation and supply its underlying geometric objects; an unindexed earlier computation of node postulation remains a possible priority risk. Independent mathematical audit has not been performed.

## References

1. A. Auel and B. Singer, *The algebraic geometry of 3-by-3 magic squares of squares*, arXiv:2609.09351v1 (first posted 2026-09-08), §§1.1–1.3, `https://arxiv.org/abs/2609.09351`.
2. P. Michaud-Rodgers, *Magic Squares of Squares*, Warwick Mathematics Society talk, 2019-02-26, especially slides on Hilbert polynomials and singular points, `https://warwick.ac.uk/fac/sci/maths/people/staff/michaud/magisquarestalk.pdf`.
