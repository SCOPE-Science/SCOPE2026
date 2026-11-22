# Parity-controlled Smith form of inversion-feasibility matrices in the random permutation

## Finding
Let \(\Pi=(D,<_{1},<_{2})\) be the countable homogeneous structure whose age consists of all finite sets equipped with two linear orders. Individually name any \(n\ge1\) distinct parameters, with their induced pair of orders. The complete nonalgebraic one-point types over these parameters are indexed by \((i,j)\in\{0,\ldots,n\}^2\), the two insertion gaps. Define the symmetric integer matrix \(M_n\), of order \(N=(n+1)^2\), by
\[
(M_n)_{(i,j),(k,\ell)}=1
\quad\Longleftrightarrow\quad
\text{two distinct realizations of these types can form an inversion},
\]
where an inversion means that the two realizations occur in opposite orders under \(<_{1}\) and \(<_{2}\). The matrix depends on \(n\), not on the permutation induced on the parameters. Its complete integral Smith normal form is
\[
\boxed{\operatorname{SNF}_{\mathbb Z}(M_n)=
\begin{cases}
\operatorname{diag}(I_{n^2+n+1},\,2I_{n-1},\,0_1),& n\text{ odd},\\
\operatorname{diag}(I_{n^2+n+1},\,2I_1,\,0_{n-1}),& n\text{ even}.
\end{cases}}
\]
An empty factor \(2I_0\) is omitted. Equivalently, the cokernel is \(\mathbb Z\oplus(\mathbb Z/2\mathbb Z)^{n-1}\) for odd \(n\), and \(\mathbb Z^{n-1}\oplus\mathbb Z/2\mathbb Z\) for even \(n\). Thus the rank over \(\mathbb F_2\) is always \(n^2+n+1\), whereas over any field of characteristic different from two it is \((n+1)^2-1\) for odd \(n\) and \((n+1)^2-n+1\) for even \(n\). No odd-primary or order-four torsion occurs.

## Assumptions and scope
The two linear orders are independent in the finite-extension sense: every finite configuration extending the named parameter permutation is realized in \(\Pi\). Individual parameters are named, not identified under their automorphisms. A one-point type fixes an insertion gap in each order and excludes equality with any parameter. Feasibility means existence of *two distinct* realizations of the two types forming an inversion. It does not ask for all ordered two-point types or simultaneous realization of many pairs. Diagonal entries of \(M_n\) are one: two distinct realizations of the same one-point type can be ordered oppositely inside their common gaps.

For \(0\le i,j,k,\ell\le n\), finite-order consistency gives the explicit formula
\[
\boxed{(M_n)_{(i,j),(k,\ell)}=
\mathbf 1_{\{(i-k)(j-\ell)\le0\}}.}
\tag{1}
\]
Indeed, if both differences are nonzero and have the same sign, the two orders force the same orientation of the new pair; in every other case at least one orientation is free or the two forced orientations disagree. Strong amalgamation for the two linear orders realizes the selected orientations.

## Proof
Put \(t=n\), \(m=t+1\), so \(M_n\) has \(m^2\) rows and columns. Compute its cokernel by generators \(e_{ij}\), \(0\le i,j\le t\), and one relation \(R_{k\ell}\) for each column \((k,\ell)\):
\[
R_{k\ell}=S-\sum_{i<k,\,j<\ell}e_{ij}
-\sum_{i>k,\,j>\ell}e_{ij}=0,
\qquad S=\sum_{i,j=0}^{t}e_{ij}.
\tag{2}
\]
Replacing these relations by their two-dimensional finite differences and boundary differences is an integer-unimodular operation on the full list of relations. In particular,
\[
R_{k\ell}-R_{k-1,\ell}-R_{k,\ell-1}+R_{k-1,\ell-1}
=-e_{k-1,\ell-1}-e_{k\ell}
\quad(1\le k,\ell\le t).
\tag{3}
\]
The remaining boundary relations can be taken as \(S=R_{t0}=0\), together with
\[
A_k=\sum_{j=1}^{t}e_{kj}=0,\qquad
B_k=\sum_{i=1}^{t}e_{ik}=0
\quad(1\le k\le t).
\tag{4}
\]
These come from successive differences of \(R_{k0}\) and \(R_{0k}\). The relation replacement is reversible over \(\mathbb Z\): differences have unit triangular transition matrices.

Equation (3) eliminates, with unit coefficients, all \(t^2\) interior generators, and gives
\[
e_{ij}=(-1)^{\min(i,j)}x_{i-j},
\qquad x_d=\begin{cases}e_{d0},&d\ge0,\\e_{0,-d},&d<0.\end{cases}
\tag{5}
\]
Write \(u_0=v_0=x_0\), \(u_d=x_d\), and \(v_d=x_{-d}\) for \(1\le d\le t\). After multiplying \(A_k,B_k\) by the unit \((-1)^k\), the remaining row/column equations become
\[
F_k:=\sum_{a=0}^{k-1}(-1)^a u_a+\sum_{b=1}^{t-k}v_b=0,
\quad
G_k:=\sum_{a=0}^{k-1}(-1)^a v_a+\sum_{b=1}^{t-k}u_b=0.
\tag{6}
\]
For \(1\le k\le t-1\), their differences are exactly
\[
(-1)^k u_k-v_{t-k}=0,
\qquad (-1)^k v_k-u_{t-k}=0.
\tag{7}
\]
Use the first family to eliminate \(v_1,\ldots,v_{t-1}\). Substitution in the second family gives
\[
(1-(-1)^t)u_k=0\quad(1\le k\le t-1).
\tag{8}
\]
The only remaining equations from (6) are \(F_t=G_t=0\), which become
\[
u_0+\sum_{k=1}^{t-1}(-1)^k u_k=0,
\qquad
u_0+(-1)^t\sum_{k=1}^{t-1}u_k=0.
\tag{9}
\]
Finally, subtracting the row equations \(A_1,\ldots,A_t\) from \(S\) converts \(S=0\) into the boundary-sum relation. After (7), it is
\[
u_0+u_t+v_t+2\sum_{\substack{1\le k<t\\k\text{ even}}}u_k=0.
\tag{10}
\]
Equations (9) and (10) eliminate \(u_0\) and \(v_t\), each with unit coefficient, leaving \(u_t\) free. Their sole residual relation among \(u_1,\ldots,u_{t-1}\) is
\[
\sum_{k=1}^{t-1}\bigl((-1)^t-(-1)^k\bigr)u_k=0.
\tag{11}
\]
If \(t\) is odd, (8) says \(2u_k=0\) for every \(1\le k<t\), and (11) is the redundant relation \(-2\sum_{k\text{ even}}u_k=0\). Hence the cokernel is \(\mathbb Z\oplus(\mathbb Z/2\mathbb Z)^{t-1}\). If \(t\) is even, (8) is vacuous, and (11) reduces to \(2\sum_{k\text{ odd}}u_k=0\). This is twice a primitive integer linear form (the coefficient of \(u_1\) is one), so its quotient is \(\mathbb Z^{t-1}\oplus\mathbb Z/2\mathbb Z\), including the free generator \(u_t\).

All eliminations use coefficients \(\pm1\) and have inverse integer operations. The abelian-group classification determines the nonunit and zero Smith factors. Since the original square matrix has \((t+1)^2\) entries along the Smith diagonal, the remaining factors must all be one; their common number is \((t+1)^2-t=t^2+t+1\). This proves the stated all-\(n\) Smith form and its field-rank consequences.

## Verification
The standalone Python checker `verify.py` constructs (1) directly, verifies unimodularity of the displayed finite-difference relation transformation for \(1\le n\le5\), and computes exact integer Smith forms using SymPy for every \(1\le n\le9\). Separately, for every parameter permutation through \(n=4\), it enumerates every insertion of two distinct new points into each linear order and independently reconstructs all feasibility entries. A successful run reports `VERIFY_OK`, 33 parameter permutations, 16,714 matrix entries compared, and nine exact Smith-form sizes. The direct calculations are not substituted for the preceding infinite-family proof.

To reproduce: install Python 3 and SymPy (tested on 1.14), then run `python verify.py` in the directory containing this result and verifier. No external datasets are needed.

## Relationship to prior work
Cameron (2002) identifies the Fraïssé class of all finite permutations and the independent-amalgamation model with two total orders, which supplies the extension theorem used here. Linman and Pinsker (2014) describe its reducts and symmetry structure. Neither inspected result provides an integral Smith classification of the finite-parameter inversion-feasibility kernel (1). The published "Incidence precision law for all inversion indicators of a random permutation" studies the covariance and inverse covariance of inversion events in *uniform finite permutations*; its indexing and matrix entries differ from feasibility between logical one-point types and do not imply (1)'s cokernel. Classical permutation graphs encode *actual* inversions of one fixed permutation, whereas (1) records potential inversion of two extension types and has nonzero diagonal. The finite-difference argument is elementary integer linear algebra, not a claim to invent the Smith form or permutation graphs.

## Limitations
The result treats the existence of an inversion between a pair of realizations over a named finite base, not probabilities of such inversions, the full spectral eigenvalue list, or higher-point compatibility. Its integer invariants do not vary with the base permutation, but that does not imply all relative multi-point type statistics are permutation-independent. The historical novelty comparison is necessarily bounded: an equivalent grid-kernel Smith formula may exist under a different name in matrix or order-theory literature. Independent mathematical audit has not been performed.

## References
1. P. J. Cameron, "Homogeneous Permutations," *Electronic Journal of Combinatorics* 9(2), R2 (2002), published 2002-10-31, DOI: 10.37236/1674. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i2r2/pdf/
2. J. Linman and M. Pinsker, "Permutations on the Random Permutation," arXiv:1405.4297, first submitted 2014-05-16. https://arxiv.org/abs/1405.4297
3. "Incidence precision law for all inversion indicators of a random permutation," published research record (2026). https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-incidence-precision-law-for-all-inversion-indicators-of-a-random--f6af0a8c3805/RESULT.md
4. R. P. Stanley, "Smith Normal Form in Combinatorics," arXiv:1602.00166, first submitted 2016-01-30. https://arxiv.org/abs/1602.00166
