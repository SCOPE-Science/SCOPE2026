# Four-parameter rank and socle census for square-zero two-loop modules

## Finding

Let \(k=\mathbb F_q\) be a finite field of arbitrary prime-power order, let \(n\geq1\), and consider ordered pairs \((A,B)\) of \(n\times n\) matrices satisfying
\[
A^2=B^2=AB=BA=0.
\]
Such pairs are labeled \(n\)-dimensional modules over \(\Lambda=k[x,y]/(x,y)^2\): the two matrices specify the actions of \(x\) and \(y\). Define four dimensions
\[
r=\operatorname{rank}A,\qquad s=\operatorname{rank}B,\qquad
w=\dim(\operatorname{im}A+\operatorname{im}B),\qquad
\nu=\dim(\ker A\cap\ker B).
\]
Here \(w\) is the radical dimension and \(\nu\) is the socle dimension of this \(\Lambda\)-module. The following formula counts **individual ordered matrix pairs**, not similarity classes.

Write \({a\brack b}_q\) for the Gaussian binomial coefficient (zero for out-of-range parameters) and
\[
P_q(d,t)=\prod_{i=0}^{t-1}(q^d-q^i),\quad
P_q(d,0)=1,\quad P_q(d,t)=0\quad\text{for }t>d.
\]
For integers \(\ell,r,s\geq0\), put
\[
F_q(\ell;r,s)=\sum_{j=0}^{\ell}(-1)^j q^{\binom j2}{\ell\brack j}_q
P_q(\ell-j,r)P_q(\ell-j,s).
\]
Then the number \(C_{n,q}(r,s,w,\nu)\) of solutions of the prescribed four dimensions is
\[
\boxed{C_{n,q}(r,s,w,\nu)=
{n\brack w}_q{w\brack r}_q{r\brack r+s-w}_q
q^{(w-r)(w-s)}{n-w\brack \nu-w}_q
F_q(n-\nu;r,s).}
\]
The product is interpreted as zero if the inequalities below are violated. Its nonzero parameter range is **exactly**
\[
\max(r,s)\leq w\leq r+s,\qquad
w\leq\nu\leq n,\qquad
\max(r,s)\leq n-\nu\leq r+s,
\]
with \(0\leq r,s\leq n\). Every feasible quadruple occurs over **every** field, finite or infinite; the formula gives the multiplicities over finite fields.

For example, at \(n=3,q=2,r=s=1\), the pairs split into three radical/socle strata: \((w,\nu)=(1,1)\) occurs \(42\) times, \((1,2)\) occurs \(21\) times and \((2,2)\) occurs \(42\) times. The two separate operator ranks do not specify these distinct module invariants.

## Assumptions and scope

All four products vanish, including the two squares. Matrices are ordered and are counted in a fixed coordinate basis. The image/socle spaces are subspaces of \(k^n\), and equality of matrix pairs is literal. Gaussian coefficients use the convention \({a\brack b}_q=0\) unless \(0\leq b\leq a\). The count is valid for every prime-power \(q\), with no parity or algebraic-closure restriction. The feasibility statement only requires a field. The claim is a four-index **labeled point count**, not a classification of module-isomorphism classes, orbit closures, components or a new description of the representation variety.

## Proof

**Step 1: record radical and socle.** Set \(V=k^n\), \(R=\operatorname{im}A\), \(S=\operatorname{im}B\), \(W=R+S\) and \(U=\ker A\cap\ker B\). The four product equations imply \(W\subseteq U\), and conversely if \(W\subseteq U\) then all four products vanish. Necessarily \(\dim R=r,\dim S=s,\dim W=w,\dim U=\nu\).

**Step 2: select the image pair.** Choose \(W\subseteq V\) of dimension \(w\) in \({n\brack w}_q\) ways and \(R\subseteq W\) of dimension \(r\) in \({w\brack r}_q\) ways. Write \(t=\dim(R\cap S)=r+s-w\). Choose \(R\cap S\subseteq R\) in \({r\brack t}_q\) ways. Given this intersection, \(S/(R\cap S)\) must project isomorphically onto \(W/R\); its possible lifts are graphs of linear maps from the \((w-r)\)-dimensional quotient into \(R/(R\cap S)\) of dimension \(r-t=w-s\). The number of graphs is \(q^{(w-r)(w-s)}\). The product gives exactly the image-pair factor in the boxed formula.

**Step 3: select the common kernel.** Each \(\nu\)-dimensional \(U\) containing \(W\) corresponds to a \((\nu-w)\)-subspace of \(V/W\), giving \({n-w\brack\nu-w}_q\) choices. Since \(A\) and \(B\) annihilate \(U\), they induce linear maps
\[
\alpha:V/U\longrightarrow R,\qquad\beta:V/U\longrightarrow S.
\]
To obtain the specified images and *exactly* the specified common kernel, both maps must be surjective and \(\ker\alpha\cap\ker\beta=0\). Every such pair has a unique lift to operators on \(V\), and conversely.

**Step 4: count the induced maps.** Let \(X=V/U\), of dimension \(\ell=n-\nu\). The number of surjections \(X\to k^r\) is \(P_q(\ell,r)\), and similarly for \(k^s\). For a fixed \(j\)-dimensional subspace \(K\subseteq X\), the number of surjective map pairs whose common kernel contains \(K\) equals \(P_q(\ell-j,r)P_q(\ell-j,s)\). Subspace-lattice Möbius inversion, with \(\mu(0,K)=(-1)^jq^{\binom j2}\), counts those whose common kernel is zero as \(F_q(\ell;r,s)\). Multiplication of all independent choices proves the formula.

**Step 5: sharp feasible parameter domain.** Two images of dimensions \(r,s\) span dimension \(w\) precisely if \(\max(r,s)\leq w\leq r+s\). A \(\nu\)-subspace containing \(W\) exists exactly if \(w\leq\nu\leq n\). Finally, an injective linear map \(X\to R\oplus S\) whose two projections are surjective exists exactly when \(\max(r,s)\leq\ell\leq r+s\): for the converse, choose a common \(t=(r+s-\ell)\)-dimensional coordinate subspace and the span of its diagonal, together with independent complements in the two factors. This construction works over every field, proving sufficiency without treating numerical experiments as proof.

**Step 6: consistency and extremal corollary.** Summing over the common-kernel dimension removes the joint-kernel condition:
\[
\sum_{\nu} C_{n,q}(r,s,w,\nu)=
{n\brack w}_q{w\brack r}_q{r\brack r+s-w}_q
q^{(w-r)(w-s)}P_q(n-w,r)P_q(n-w,s).
\]
Summing over all four parameters gives an independent global count:
\[
\sum_{r,s,w,\nu}C_{n,q}(r,s,w,\nu)=
\sum_{w=0}^{n}{n\brack w}_q P_q(2(n-w),w).
\]
Indeed, for fixed \(W\), the pair \((A,B)\) is equivalent to a surjection \((V/W)\oplus(V/W)\to W\). Consequently the maximum possible radical dimension is \(\lfloor2n/3\rfloor\), also attained over any field. This extremal consequence is included as a consistency check; priority is not claimed for general geometric bounds on the variety.

## Verification

The accompanying standalone Python file `verify.py` evaluates the formula using exact integer arithmetic. Independently it constructs all matrices and directly tests all four original products over prime fields, then computes the four subspace dimensions by Gaussian elimination. Exhaustive comparisons were made for \((n,q)=(2,2),(3,2),(4,2),(2,3),(3,3)\), with respective total ordered-pair counts \(10,148,8296,33,1665\) and respective numbers of nonempty four-index cells \(4,6,12,4,6\). The predicted total for \((5,2)\) is \(1003936\); this is a formula calculation, **not** a brute-force enumeration. The code also tests the global-count identity at additional finite-field orders. The proof above, not these finite tests, establishes the result for arbitrary \(n\) and prime-power \(q\).

To reproduce, use a standard Python 3 interpreter: `python3 verify.py`. The exact output is included in `checks.txt`.

## Relationship to prior work

Morrison (1980) analyzes the representation scheme for the **same** algebra \(k[x,y]/(x,y)^2\), including its indecomposables and irreducible components. Schröer (2002) studies the **same four matrix equations** within the general family of annihilating nilpotent matrix pairs and determines irreducible components. These are direct structural predecessors, not unrelated analogues. Neither inspected statement supplies an all-dimensional four-index finite-field labeled count stratified simultaneously by the two ranks, radical dimension and socle dimension. Huang (2021) counts **broader but coarser** mutually annihilating pairs \(AB=BA=0\), including nilpotent cases; those counts do not alone determine the square-zero four-index coefficients. Kinser and Lőrincz (2018) cover representation-variety component geometry of radical-square-zero algebras; the present statement makes no competing geometric originality claim. Ram (2015) counts observable matrix pairs for a different iterative-kernel condition; his result does not directly enumerate these modules.

The genuinely assessed object is the displayed joint arithmetic distribution and its exact parameter support. Its derivation uses classical Gaussian and Möbius formulas; no originality is claimed for those constituent facts or for the known geometric classification. A prior specialization of a general Hall-type or representation-counting formula could conceivably imply the full answer; complete priority exclusion is not asserted.

## Limitations

The formula counts labeled pairs, not conjugacy orbits or indecomposable modules; it does not determine the representation-type classification or irreducible-component incidence. It requires all four products to vanish and does not enumerate larger nilpotency exponents or arbitrary mutually annihilating pairs. The computational checker directly exhausts only the listed small prime fields; extension fields and all dimensions are covered analytically, not by exhaustive computer evidence. Historical originality is supported by a targeted literature comparison but is not independently certified.

## References

1. Kent Morrison, “The Scheme of Finite Dimensional Representations of an Algebra,” *Pacific Journal of Mathematics* 91 (1980), 199–225; https://aimath.org/~morrison/Research/SchemeFinDimReps.pdf .
2. Jan Schröer, “Varieties of pairs of nilpotent matrices annihilating each other,” first public arXiv version 2002-11-19, arXiv:math/0211293; https://arxiv.org/abs/math/0211293 .
3. Yifeng Huang, “Mutually annihilating matrices, and a Cohen–Lenstra series for the nodal singularity,” first public arXiv version 2021-10-29, arXiv:2110.15566; https://arxiv.org/abs/2110.15566 .
4. Ryan Kinser and András C. Lőrincz, “Representation varieties of algebras with nodes,” first public arXiv version 2018-10-25, arXiv:1810.10997; https://arxiv.org/abs/1810.10997 .
5. Samrith Ram, “Counting zero kernel pairs over a finite field,” first public arXiv version 2015-09-27, arXiv:1509.08053; https://arxiv.org/abs/1509.08053 .
