# Integral Walsh interpolation on every Boolean order ideal

## Finding

Let \(n\ge0\) be an integer and let \(\mathcal D\subseteq2^{[n]}\) be any nonempty downward-closed set family (including the empty set). Index a square matrix by the faces \(A,B\in\mathcal D\), with entries
\[
H_{A,B}=(-1)^{|A\cap B|}.
\]
Then the integer Smith normal form of \(H\) has one invariant factor \(2^{|A|}\) for every face \(A\in\mathcal D\), arranged in nondecreasing order of face size. The exact signed determinant is
\[
\det H=\prod_{A\in\mathcal D}(-2)^{|A|},
\]
and its real inertia is \((e,o,0)\), where \(e\) (respectively \(o\)) is the number of even-cardinality (respectively odd-cardinality) faces of \(\mathcal D\). The inverse is explicitly
\[
(H^{-1})_{A,B}=(-1)^{|A|+|B|}\sum_{\substack{C\in\mathcal D\\ C\supseteq A\cup B}}(-2)^{-|C|}.
\]
For each positive integer \(r\), reduction of the sampling map modulo \(2^r\) has exactly
\[
2^{\sum_{A\in\mathcal D}\min(r,|A|)}
\]
elements in its kernel. In particular, every Walsh sample vector on \(\mathcal D\) uniquely reconstructs a complex or rational signal supported on \(\mathcal D\); and reduction of the integer sampling operator modulo every odd integer is invertible.

## Assumptions and scope

The ambient binary group is \((\mathbb Z/2\mathbb Z)^n\), with a binary vector identified with its support subset of \([n]\). The Walsh pairing is \(\langle A,B\rangle=|A\cap B|\pmod2\). Fourier samples use the unnormalized convention \(\widehat f(A)=\sum_{B\in\mathcal D}(-1)^{|A\cap B|}f(B)\). The family \(\mathcal D\) must be downward closed, not merely fixed-weight or an arbitrary collection of the same cardinality. No assumption of purity, connectedness, bounded degree, or regularity is imposed. When \(n=0\), the sole allowed face is the empty face and the matrix is \((1)\). All Smith normal forms concern integer row and column operations; the inertia concerns the real symmetric matrix.

## Proof

Order faces first by cardinality and then arbitrarily within each cardinality. Define the incidence-zeta matrix and a diagonal matrix by
\[
Z_{A,C}=\mathbf 1_{C\subseteq A},\qquad D_{C,C}=(-2)^{|C|}\quad(A,C\in\mathcal D).
\]
Downward closure ensures that all subsets of an intersection \(A\cap B\) are in \(\mathcal D\). Consequently the binomial identity, without omitted terms, gives
\[
(ZDZ^{\mathsf T})_{A,B}=
\sum_{C\subseteq A\cap B}(-2)^{|C|}
=(1-2)^{|A\cap B|}=H_{A,B}.
\]
The matrix \(Z\) is lower unitriangular in the chosen order: a face \(C\subsetneq A\) has strictly smaller cardinality. It follows that \(Z\) and \(Z^{\mathsf T}\) are unimodular integer matrices. Therefore \(H\) and \(D\) are equivalent by unimodular left and right operations. Because the positive diagonal entries \(2^{|C|}\) form a divisibility chain in cardinality order, multiplying diagonal rows of \(D\) by the appropriate signs gives the asserted Smith normal form. The determinant identity follows from \(\det Z=1\), and Sylvester's law of inertia applied to the congruence \(H=ZDZ^{\mathsf T}\) gives one positive eigenvalue for each even face and one negative eigenvalue for each odd face; none vanish.

Möbius inversion on the Boolean order ideal gives
\[
(Z^{-1})_{C,A}=(-1)^{|C\setminus A|}\mathbf1_{A\subseteq C}.
\]
Substitute in \(H^{-1}=(Z^{-1})^{\mathsf T}D^{-1}Z^{-1}\) to obtain the stated inverse entry formula. Finally, the Smith form remains equivalent over \(\mathbb Z/2^r\mathbb Z\), and multiplication by \(2^{|C|}\) on that ring has exactly \(2^{\min(r,|C|)}\) kernel elements. Multiplication over all diagonal factors proves the modular kernel formula. Over any odd modulus all diagonal factors are units. These calculations hold for every finite \(n\) and every downward-closed \(\mathcal D\), without asymptotics.

## Verification

An independent integer-matrix checker is included as `verify.py`. It enumerates every order ideal on up to three vertices, forms the actual principal Walsh matrices, compares direct exact determinants, Smith normal forms, and inverse identities with the closed formulas; it also checks selected non-pure order ideals and the full second-degree Hamming ball on four vertices. The script is finite verification only: the all-dimensions theorem rests on the preceding factorization and Möbius-inversion proof. To run it use `python verify.py`, with SymPy installed.

For the natural degree-two ball \(\mathcal D=\{A:|A|\le2\}\), one has \(|\det H|=2^{n^2}\) for every \(n\ge2\), while the complete Smith diagonal consists of one \(1\), \(n\) copies of \(2\), and \(\binom n2\) copies of \(4\). The exact modular nullity makes the arithmetic strength of this interpolation rule explicit, not merely its nonsingularity over the complex numbers.

## Relationship to prior work

Brent and Osborn (2012 preprint, 2013 article) study minors of maximal-determinant matrices and provide a framework for their size and extremality. Hacıoğlu (2013) treats Smith normal forms of selected Sylvester-Hadamard design constructions, which are structured submatrices rather than arbitrary face ideals. Knill (2019) analyzes the unweighted face-counting matrix \(K_{A,B}=|\{C\in\mathcal D:C\subseteq A\cap B\}|\), including unimodularity and inverse formulas. The present Fourier kernel uses the signed cardinality weights \((-2)^{|C|}\), and supplies its full integer Smith data, inertia, inverse, and modular reconstruction statement for *every* order ideal. The shared incidence-zeta mechanism is acknowledged: the novelty claim is the specific uniform Fourier-arithmetic classification, not an invention of Möbius inversion.

## Limitations

This is a theorem about binary Walsh characters and *principal* restrictions indexed by the same downward-closed family. It does not determine the singular values or Euclidean condition number, treat independent arbitrary row and column supports, or imply invertibility for every unordered subset of the cube. The explicit formulas do not address numerical rounding stability. The proof gives exact integer invariants but does not require independent external proof verification. Related counting-matrix and design-Smith literature may contain alternative incidence formulations; this is a residual literature risk rather than a claim of exhaustive novelty.

## References

1. Richard P. Brent and Judy-anne H. Osborn, *On minors of maximal determinant matrices*, arXiv:1208.3819 (first version publicly available 2012-08-19), *Journal of Integer Sequences* **16** (2013).
2. İlhan Hacıoğlu, *Derived and residual Sylvester-Hadamard designs and the Smith normal form*, *Turkish Journal of Mathematics* **37** (2013), 398–403, DOI:10.3906/mat-1112-18.
3. Oliver Knill, *The counting matrix of a simplicial complex*, arXiv:1907.09092 (2019).
