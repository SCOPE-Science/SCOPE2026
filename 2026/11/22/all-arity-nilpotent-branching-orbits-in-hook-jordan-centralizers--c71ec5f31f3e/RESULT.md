# All-arity nilpotent branching orbits in hook Jordan centralizers

## Finding
Fix any finite field \(k=\mathbb F_q\), integers \(m\ge2\) and \(r\ge2\), and \(B=J_m(0)\oplus J_1(0)\). Let \(\mathcal C_{m,r}\) be the set of ordered \(r\)-tuples \((X_1,\ldots,X_r)\) of nilpotent matrices satisfying \([X_i,B]=[X_i,X_j]=0\). The invertible centralizer \(G=Z_{\mathrm{GL}_{m+1}(k)}(B)\) acts by simultaneous conjugation.

Write \([r]_q=(q^r-1)/(q-1)\). The complete orbit census is
\[
\boxed{|\mathcal C_{m,r}/G|=q^{r(m-2)}\bigl(q^r+(q+1)q^{r-1}[r]_q\bigr).}
\]
Of these, exactly \(q^{r(m-1)}\) are singleton classes. Every other orbit has size \(q(q-1)\), so the number of such classes is \((q+1)[r]_q q^{r(m-1)-1}\). The total number of labeled commuting tuples is
\[
\boxed{|\mathcal C_{m,r}|=q^{r(m-1)}\{1+(q+1)(q^r-1)\}.}
\]
In particular, this simultaneously determines all conjugation-class sizes and their exact numbers for every tuple length and every finite field characteristic. There is a complete projective-direction classification, not merely an aggregate orbit total.

The reduced affine tuple variety over any field \(k\) is isomorphic to \(\mathbb A^{r(m-1)}\times D_{2,r}^{\le1}\), where \(D_{2,r}^{\le1}\) is the determinantal variety of rank-at-most-one \(2\times r\) matrices. For \(r\ge2\), it is geometrically irreducible of dimension \(mr+1\), and its geometric singular locus is the affine factor times the zero matrix; its dimension is \(r(m-1)\). This geometric identification supports the orbit classification; no novelty is asserted for the classical determinantal-variety facts alone.

## Assumptions and scope
Let \(R=k[t]/(t^m)\). Identify the vector space acted on by \(B\) with the \(k[t]\)-module \(R\oplus k\), where multiplication by \(t\) represents \(B\) and the last summand is annihilated by \(t\). Let \(\epsilon:R\to k\) be constant-term extraction. A nilpotent endomorphism here means an endomorphism nilpotent as an ordinary \((m+1)\)-dimensional \(k\)-linear operator. Tuples are ordered, may have zero or repeated entries, and must commute pairwise. The group \(G\) acts on all tuple entries by the **same** conjugator. The formulas require \(m,r\ge2\), and apply to every prime power \(q\). Geometric claims concern the reduced affine variety, not possible nonreduced structures of a presenting equation scheme.

## Proof
**Step 1: Endomorphism coordinates and nilpotence.** All \(k[t]\)-linear endomorphisms of \(R\oplus k\) have unique matrices of module maps
\[
 X(a,b,c,d)=\begin{pmatrix} a(t)&b t^{m-1}\\ c\epsilon&d\end{pmatrix},\qquad a(t)\in R,\ b,c,d\in k.
\]
This follows from \(\operatorname{Hom}_{k[t]}(k,R)=kt^{m-1}\), \(\operatorname{Hom}_{k[t]}(R,k)=k\epsilon\), and \(\operatorname{End}_{k[t]}(R)=R\). The induced linear map on \((R\oplus k)/t(R\oplus k)\) has diagonal entries \(a_0=a(0)\) and \(d\). Thus nilpotence implies \(a_0=d=0\). Conversely, these equalities imply \(X^2(R\oplus k)\subseteq t(R\oplus k)\), and \(k[t]\)-linearity then yields \(X^{2m}=0\). Hence every nilpotent commuting matrix is uniquely represented by \(a(t)\in tR\), \(b,c\in k\).

For a tuple, define coefficient vectors \(A_j=(a_{j1},\ldots,a_{jr})\in k^r\) for \(1\le j\le m-1\), \(\mathbf b=(b_1,\ldots,b_r)\in k^r\), and \(\mathbf c=(c_1,\ldots,c_r)\in k^r\). Direct multiplication gives
\[
 [X_i,X_j]=\begin{pmatrix}(b_ic_j-b_jc_i)t^{m-1}&0\\0&0\end{pmatrix}.
\]
Therefore the tuple commutes if and only if the \(2\times r\) matrix with rows \(\mathbf b,\mathbf c\) has rank at most one. The \(r(m-1)\) polynomial coefficients are unrestricted, proving the claimed product description of the variety. The standard rank-one determinantal locus has dimension \(r+1\), is irreducible, and is singular only at rank zero for \(r\ge2\) (the rank-one charts are smooth, while the defining minors have zero linearization at zero). This also holds in all characteristics.

**Step 2: Explicit conjugation action.** Every unit of the centralizer has the form
\[
 g=\begin{pmatrix}u(t)&e t^{m-1}\\ f\epsilon&d\end{pmatrix},\qquad u_0=u(0)\ne0,\ d\ne0.
\]
The determinant condition is necessary and sufficient by the filtration on \(R\oplus k\). Comparing \(gX_i=X'_ig\) gives
\[
 b'_i=\lambda b_i,\qquad c'_i=\lambda^{-1}c_i,\qquad a'_{ji}=a_{ji}\ (1\le j\le m-2),
\]
and
\[
 a'_{m-1,i}=a_{m-1,i}+\alpha c_i+\beta b_i,
 \quad \lambda=u_0/d\in k^*,\ \alpha=e/u_0\in k,\ \beta=-f/d\in k.
\]
Conversely every triple \((\lambda,\alpha,\beta)\in k^*\times k^2\) is achieved by a unit, so these equations completely describe the action. In particular the low coefficient vectors \(A_1,\ldots,A_{m-2}\) are invariants.

**Step 3: Exact orbit classification.** Fix the low coefficients and write \(\mathbf z=A_{m-1}\). If \(\mathbf b=\mathbf c=0\), every \(\mathbf z\in k^r\) is fixed, giving \(q^r\) singleton orbits per low-coefficient choice. Otherwise, pairwise commutativity determines a unique line \(\ell\in\mathbb P^{r-1}(k)\), containing both \(\mathbf b\) and \(\mathbf c\). Choose the unique representative \(v\in\ell\) whose first nonzero coordinate is one. Write \(\mathbf b=s v\), \(\mathbf c=t v\), with \((s,t)\ne(0,0)\). The multiplicative action is \((s,t)\mapsto(\lambda s,\lambda^{-1}t)\). Its complete invariants are: one \(s\)-axis type (\(s\ne0,t=0\)); one \(t\)-axis type (\(s=0,t\ne0\)); or \(\eta=st\in k^*\) (both nonzero). Thus for every line there are exactly \(q+1\) multiplicative orbit types. The additive parameters translate \(\mathbf z\) by the entire line \(\ell\), while leaving its coset in \(k^r/\ell\) invariant; every such translation is achieved because \((s,t)\ne(0,0)\). Consequently every noncentral orbit is classified by the fixed lower coefficients, \(\ell\), its axis-or-product type, and \(\mathbf z+\ell\).

There are \(q^{r(m-2)}\) lower-coefficient choices, \([r]_q\) projective lines, \(q+1\) types per line, and \(q^{r-1}\) additive cosets. Each such orbit consists of exactly \(q-1\) scalar pairs and \(q\) top-coefficient vectors for each fixed coset, hence has cardinality \(q(q-1)\). Counting all types proves the orbit formula and class-size spectrum. All invariants and normalizations are rational over \(k\), so there is no hidden descent or field-characteristic exception.

**Step 4: Labeled tuple count.** The number of rank-at-most-one matrices in \(M_{2\times r}(k)\) equals \(1+(q+1)(q^r-1)\): choose zero, or choose a line in \(k^2\) and a nonzero row of coordinates in \(k^r\). Multiplying by the \(q^{r(m-1)}\) free polynomial coefficients gives the formula for \(|\mathcal C_{m,r}|\). Independently, summing the counted singleton and noncentral orbit sizes yields the same number, an internal normalization check.

## Verification
The accompanying dependency-free `checker.py` independently enumerates the module-coordinate matrices, tests every pairwise commutator equation, computes complete orbit invariants, and checks each orbit against direct conjugation by the centralizer units (not just its cardinality). Executed tests cover \((q,m,r)=(2,2,2),(2,3,2),(2,3,3),(2,4,2),(3,2,2),(3,3,2),(5,2,2)\). For example, \((3,3,2)\) has \(2673\) labeled commuting tuples and \(513\) conjugation orbits, comprising \(81\) singleton and \(432\) size-six orbits. All seven tests passed. The scripts enumerate only prime fields and finite small parameters, while the proof above covers arbitrary prime powers and all allowed sizes. Run `python checker.py` with standard Python 3.

## Relationship to prior work
Britnell and Wildon (2010) characterize the *existence* of commuting representatives of prescribed matrix similarity classes, including two-part nilpotent partitions. This does not count simultaneous centralizer orbits of all-arity commuting nilpotent tuples with one fixed hook Jordan matrix. Sharma (2014) explicitly computes branching of unrestricted commuting companions for matrix dimensions at most four, including the \((3,1)\) initial class (Lemma 5.10). These small-dimensional branching calculations are acknowledged predecessors and do not supply the all-arity nilpotent-restricted hook classification for arbitrary \(m\). Other finite-field studies count nilpotent commuting tuples in a centralizer with fixed partition \((n-2,2)\); those are **raw tuple counts for different block sizes**, not the simultaneous quotient for \((m,1)\). A prior class-size census for the **unit group** of this hook centralizer concerns conjugacy on single units; its one-element unipotent specialization is not claimed as a new contribution here. For \(r\ge2\), the simultaneous tuple orbits require the shared projective direction and top-coefficient coset and are not implied by that one-element size distribution. The novelty assessment is bounded; any broader full-branching theorem applying to this hook module would take priority.

## Limitations
No orbit classification is given for other Jordan partitions, tuples without pairwise commutation, or schemes with nonreduced structure. The familiar affine determinantal geometry and elementary matrix-count identities are used rather than claimed as independent discoveries. The class census does not provide a complete orbit-closure partial order or cohomological invariants. The source comparison and finite checks cannot establish universal bibliographic priority or replace an external mathematical audit.

## References
1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, first publicly available 2010-01-06, arXiv:1001.0811v1, https://arxiv.org/abs/1001.0811 (primary 2000 MSC 15A27).
2. U. B. Sharma, *Simultaneous Similarity Classes of Commuting Matrices over a Finite Field*, publicly available 2014-09-07, arXiv:1409.2698v1, https://arxiv.org/abs/1409.2698, especially Lemma 5.10 of the later full text.
3. Related fixed-\((n-2,2)\) commuting-tuple geometry, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-reducibility-threshold-for-nilpotent-two-block-centraliz--ea9926724403 (a comparison source, not a source for the present theorem).
