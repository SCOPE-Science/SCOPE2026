# A sharp two-to-three-cell separation for variation of finite conditional expectations

## Finding
Let \(n\ge3\), and write \(V(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|\) for the adjacent variation of a real path signal. For an exactly \(r\)-cell partition \(\mathcal P\) of its sites, let \(E_{\mathcal P}\) replace every coordinate by the arithmetic average over its cell. Define
\[
M_r(n)=\max_{\mathcal P:\,|\mathcal P|=r}\ \sup_{V(h)>0}\frac{V(E_{\mathcal P}h)}{V(h)}.
\]
The two-cell envelope has the exact asymptotic rate
\[
\lim_{n\to\infty}\frac{M_2(n)}n=\alpha:=6-4\sqrt2,
\qquad \alpha n-2\le M_2(n)\le\alpha n+1\quad(n\ge4).
\]
For three cells there are explicit partitions and single-jump inputs witnessing variation gain
\[
B_n=\begin{cases}n/2,&n\not\equiv3\pmod4,\\n/2-1/(n-1),&n\equiv3\pmod4.\end{cases}
\qquad M_3(n)\ge B_n.
\]
Consequently \(M_3(3)=M_2(3)=1\), but
\[
\boxed{M_3(n)>M_2(n)\quad\text{for every integer }n\ge4,}
\qquad\liminf_{n\to\infty}\frac{M_3(n)-M_2(n)}n\ge4\sqrt2-\frac{11}{2}>0.
\]
Four sites are the sharp first strict separation. This is a statement about the maximization over different partitions; it does not assert an exact formula for the unrestricted three-cell envelope \(M_3(n)\).

## Assumptions and scope
The path has linearly ordered vertices \(1,\ldots,n\), real data, strictly unweighted arithmetic means and unweighted *nonperiodic* edge variation. Cells are nonempty subsets and need not be consecutive; all partitions into exactly \(r\) cells are allowed. Each averaging map is linear, positive, self-adjoint and idempotent in Euclidean space. The seminorm is applied to differences of arbitrary two signals by linearity; constants are its kernel and every averaging map preserves constants. Only \(r=2,3\) are compared. All finite maximizers exist, since there are finitely many partitions and the quotient variation norm is an attained operator norm.

## Proof
**1. Single-jump reduction.** Let \(e^{(k)}\) be the prefix indicator \(e^{(k)}_i=1\) for \(i\le k\), and \(0\) otherwise, \(1\le k<n\). Every path signal decomposes exactly as
\[
h=h_n\mathbf1+\sum_{k=1}^{n-1}(h_k-h_{k+1})e^{(k)},\qquad V(h)=\sum_{k=1}^{n-1}|h_k-h_{k+1}|.
\]
For every linear constant-preserving map \(T\), the triangle inequality therefore gives
\[
\sup_{V(h)>0}\frac{V(Th)}{V(h)}=\max_{1\le k<n}V(Te^{(k)}),
\]
with each extremizing step a finite input witness. For a word \(w\) recording its cells, let \(N_c\) be the population of cell \(c\) and \(N_c(k)\) its population in the first \(k\) positions. Then
\[
V(E_we^{(k)})=\sum_{i=1}^{n-1}\left|\frac{N_{w_{i+1}}(k)}{N_{w_{i+1}}}-\frac{N_{w_i}(k)}{N_{w_i}}\right|.
\]
This is also a finite exact-rational evaluation procedure for any fixed partition.

**2. Upper bound for two cells.** For a binary word let \(a\ge b\) be its class sizes and \(t\) its number of adjacent color transitions. Every step image has exactly two values, so the norm is
\[
K(w)=t\max_{1\le k<n}\left|\frac{u_k}{a}-\frac{v_k}{b}\right|,
\]
where \(u_k,v_k\) count the two classes in the first \(k\) positions. Reverse the path, if necessary, so that for a maximizing step the signed discrepancy \(\delta=u_k/a-v_k/b\) is nonnegative; this reversal preserves \(K(w)\), \(a,b,t\). Put \(x=a-u_k\) (large-class sites after the cut), \(y=v_k\) (small-class sites before it), \(m=x+y\), and \(c=\min(m,b)\). Then
\[
\delta=1-\frac xa-\frac yb\le1-\frac ma\le1-\frac ca.
\]
Every transition wholly before the cut touches one of the \(y\) small-class vertices, so there are at most \(2y\) such transitions. Every transition wholly after the cut touches one of the \(x\) large-class vertices, so there are at most \(2x\); at most one transition crosses the cut. Thus \(t\le2m+1\). Globally each transition touches a small-class vertex, so also \(t\le2b\). It follows that
\[
K(w)=t\delta\le(2c+1)(1-c/a)\le2c(1-c/a)+1.
\]
Write \(z=c/a\) and \(s=b/a\). Because \(0\le z\le s\le1\), and \(n=a+b\),
\[
\frac{2c(1-c/a)}n=\frac{2z(1-z)}{1+s}\le\frac{2z(1-z)}{1+z}\le6-4\sqrt2.
\]
The last maximum occurs at \(z=\sqrt2-1\). This proves \(M_2(n)\le\alpha n+1\).

**3. Binary lower construction and asymptotic sharpness.** For an integer \(1\le b<n/2\), take the word \(A^{n-2b}(BA)^b\). It has \(2b\) adjacent color changes, and the step immediately following the initial \(A\)-run has discrepancy \((n-2b)/(n-b)\). Hence
\[
M_2(n)\ge\max_{1\le b<n/2}\frac{2b(n-2b)}{n-b}.
\]
For real \(b/n\in[0,1/2]\), this expression divided by \(n\) has unique maximum \(\alpha\) at \(b/n=1-1/\sqrt2\). For each \(n\ge4\), choose the nearest integer to this real optimizer; it is feasible. The derivative of the unnormalized expression has absolute value at most \(4\) on \([0,n/2]\), so rounding loses at most \(2\). This yields \(M_2(n)\ge\alpha n-2\), completing the limit claim.

**4. Three-cell constructions.** Write \(n=4q+r\), where \(0\le r\le3\), and concatenate the following displayed three-letter words (powers denote repetition, not arithmetic):
\[
\begin{array}{c|l}
r&\text{partition word}\ 
0&(AB)^q(CA)^q\\
1&(AB)^qA(CB)^q\\
2&(AB)^qA(CB)^qC\\
3&(AB)^{q+1}(CA)^qC.
\end{array}
\]
The first three lines require \(q\ge1\), while the fourth admits \(q=0\) and gives \(ABC\). In each case select the prefix step at the join between the two displayed alternating runs (after the extra initial \(A\) for remainders 1 and 2). The step output has respective three cell means \((1/2,1,0)\), \((1,1/2,0)\), \((1,1/2,0)\) in the first three cases, in the order \((A,B,C)\); the fourth has \(((q+1)/(2q+1),1,0)\). Direct addition of the absolute adjacent changes in the output gives \(B_n\) in all four cases. The bound \(M_3(n)\ge B_n\) requires only this explicit join-cut witness; it does not assume that the constructed word globally maximizes the three-class envelope.

**5. Strict finite onset.** At \(n=3\), two-cell words have one or two transitions and the single-jump formula gives norm at most \(1\); three singleton cells give the identity with norm \(1\). At \(n=4,5,6,7\), elementary enumeration of the at most \(2^{n-1}-1\) binary words anchored at \(A\), evaluated by the exact binary prefix formula, yields respectively \(M_2(n)=3/2,2,9/4,5/2\). The constructed three-cell norms satisfy \(B_n=2,5/2,3,10/3\), strictly larger. For \(n\ge8\), since \((1/2-\alpha)n>1+1/(n-1)\),
\[
M_2(n)\le\alpha n+1<n/2-1/(n-1)\le B_n\le M_3(n).
\]
The comparison is strict for every integer \(n\ge4\). Combining the binary exact limit with the three-cell lower bound yields the displayed positive asymptotic separation.

## Verification
The standalone exact-rational checker `check.py` reproduces the step-basis formula for 4083 binary words (all anchored binary words through length 12 under the nonconstant restriction), independently evaluates each of the explicit three-cell partitions for lengths 3 through 120, verifies the binary construction bounds through length 300, exhaustively tests all set partitions through seven sites, and confirms the binary values at lengths 3 through 7. The resulting status is `ALL_PARTITION_VARIATION_CHECKS_PASS` and `EXACT_BINARY_ONSET_N3_TO_N7_PASS`. These finite calculations are diagnostics; the asymptotic inequalities and all-dimensional separation are proved by steps 1–5, not inferred from enumeration.

## Relationship to prior work
Bober–Carneiro–Hughes–Pierce (2010) establish bounded variation behavior for a nonlinear discrete uncentered maximal operator, whereas the objects here are linear idempotent nonlocal cell averages. Nochetto–Salgado (2012) prove total-variation diminution for local finite-element interpolation, whereas arbitrary interlaced cells in the present operator can amplify variation. Gaubert–Qu (2013) treat oscillation and probability-measure total-variation contractions of Markov maps, not the adjacent variation seminorm on output signals. A published result titled *Sharp cyclic-variation stability of two-cell conditional expectations* explicitly classifies **two classes on a cycle**, with a run-mass formula; the current claim does not claim originality for binary partition norm duality or for the two-class cyclic problem. Its claimed new point is the proven strictly higher three-class path envelope from the first possible nontrivial size and the separated leading asymptotic rates. The cyclic theorem explicitly leaves three or more output classes outside scope, and no implication from its two-class bounds yields the stated three-class lower construction. Generic norm reduction to single jumps is elementary and is not itself a novel claim.

## Limitations
The three-class envelope is not determined exactly for general \(n\): only explicit attained lower bounds and the comparison with the entire binary envelope are proved. Arbitrarily many cells, positive unequal averaging masses, cyclic edge variation, and non-path graphs are not treated. The originality claim is qualified by possible older equivalent multi-class partition results not identified in the checked sources. The exact finite certificates do not independently validate the unrestricted proof. Independent scientific audit has not been performed.

## References
1. J. Bober, E. Carneiro, K. Hughes, L. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030, publicly posted 2010-05-17. https://arxiv.org/abs/1005.3030
2. R. H. Nochetto, A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069, publicly posted 2012-11-05, especially Theorem 3.7. https://arxiv.org/abs/1211.1069
3. S. Gaubert, Z. Qu, *Dobrushin's Ergodicity Coefficient for Markov Operators on Cones*, arXiv:1307.4649, publicly posted 2013-07-17, especially Theorem 1.1. https://arxiv.org/abs/1307.4649
4. *Sharp cyclic-variation stability of two-cell conditional expectations*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-cyclic-variation-stability-of-two-cell-conditional-expecta--19779f163091
