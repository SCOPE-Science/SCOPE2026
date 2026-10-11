# Optimal quotient coding for classical propositional coequivalences
## Finding

Fix
\[
\mathbf p=(p_1,\ldots,p_n),
\qquad n\ge1,
\]
and let
\[
\rho(\mathbf p_1,\mathbf p_2)
\]
be a coequivalence relation over classical propositional logic \(\mathsf{CPC}\).

As in Almeida and De Berardinis, \(\rho\) induces an equivalence relation \(E_\rho\) on the set
\[
\operatorname{Val}(\mathbf p)
\]
of \(2^n\) Boolean valuations. Let \(k\) be the number of equivalence classes of \(E_\rho\).

Define the **separation rank**
\[
\operatorname{srk}(\rho)
\]
to be the least \(m\ge0\) such that there are formulas
\[
\psi_1(\mathbf p),\ldots,\psi_m(\mathbf p)
\]
with
\[
\rho(\mathbf p_1,\mathbf p_2)
\equiv_{\mathsf{CPC}}
\bigwedge_{i=1}^{m}
\bigl(
\psi_i(\mathbf p_1)\leftrightarrow\psi_i(\mathbf p_2)
\bigr).
\]
For \(m=0\), the empty conjunction is \(\top\).

Then
\[
\boxed{
\operatorname{srk}(\rho)=\left\lceil\log_2 k\right\rceil.
}
\]

Thus every \(n\)-variable coequivalence over \(\mathsf{CPC}\) is separable by at most
\[
n
\]
formulas, and this worst-case bound is sharp.

There is also a complete census. Put
\[
N=2^n.
\]
Modulo \(\mathsf{CPC}\)-equivalence:

- the total number of coequivalence relations is the Bell number
\[
B_N;
\]
- exactly
\[
S(N,k)
\]
coequivalences have exactly \(k\) quotient classes, where \(S(N,k)\) is a Stirling number of the second kind;
- exactly one coequivalence has separation rank \(0\);
- for \(m\ge1\), the number with separation rank \(m\) is
\[
\sum_{\substack{1\le k\le N\\2^{m-1}<k\le2^m}}
S(N,k).
\]

For the first three variable counts, the rank profiles are:
\[
n=1:\qquad (1,1),
\]
\[
n=2:\qquad (1,7,7),
\]
\[
n=3:\qquad (1,127,2667,1345),
\]
where the \(m\)-th entry counts rank-\(m\) coequivalences. The totals are
\[
2,\qquad 15,\qquad 4140,
\]
respectively.

## Assumptions and scope

The result concerns coequivalence relations over \(\mathsf{CPC}\) with no background condition beyond \(\top\), and equivalence of formulas is ordinary \(\mathsf{CPC}\)-equivalence.

The separation rank is a quantitative refinement of the separating condition used in the source paper. The source definition asks only for the existence of some finite sequence of formulas whose equalities explicitly define the quotient. Here the length of that sequence is minimized.

The empty sequence is allowed in the definition above. Consequently the universal coequivalence
\[
\rho\equiv\top,
\]
which has one equivalence class, has rank \(0\). If one insists syntactically on a nonempty separating sequence, the unique one-class case can instead be represented by one tautology, and every nontrivial case is unchanged.

The census is for formulas modulo \(\mathsf{CPC}\)-equivalence. Syntactically different formulas defining the same binary relation are not counted separately.

## Proof

Let
\[
X=\operatorname{Val}(\mathbf p),
\qquad |X|=2^n.
\]

Almeida and De Berardinis show that every \(\mathsf{CPC}\)-coequivalence determines an equivalence relation on \(X\), and conversely the truth conditions of \(\rho\) depend only on whether the two restricted valuations lie in the same equivalence class. Because every subset of the finite Boolean cube \(X\) is definable by a propositional formula, every equivalence relation on \(X\) is itself definable by a coequivalence formula.

Let the quotient
\[
X/E_\rho
\]
have \(k\) classes.

Suppose first that
\[
\rho
\equiv
\bigwedge_{i=1}^{m}
\bigl(
\psi_i(\mathbf p_1)\leftrightarrow\psi_i(\mathbf p_2)
\bigr).
\]
Associate with each valuation \(v\in X\) its truth vector
\[
c(v)=
\bigl(
\mathbf 1_{v\models\psi_1},
\ldots,
\mathbf 1_{v\models\psi_m}
\bigr)
\in\{0,1\}^m.
\]
The displayed separating representation says exactly that
\[
v\,E_\rho\,w
\quad\Longleftrightarrow\quad
c(v)=c(w).
\]
Therefore distinct \(E_\rho\)-classes must receive distinct binary codewords. Hence
\[
k\le2^m,
\]
so
\[
m\ge\left\lceil\log_2 k\right\rceil.
\]

For the matching upper bound, let
\[
m=\left\lceil\log_2 k\right\rceil.
\]
Choose an injection
\[
\eta:X/E_\rho\longrightarrow\{0,1\}^m.
\]
For each coordinate \(1\le i\le m\), let
\[
D_i
=
\bigcup
\{C\in X/E_\rho:\eta(C)_i=1\}.
\]
Every \(D_i\subseteq X\) is definable in \(\mathsf{CPC}\); choose a formula
\[
\psi_i(\mathbf p)
\]
whose satisfying valuations are exactly \(D_i\).

Then two valuations \(v,w\) agree on all formulas \(\psi_i\) exactly when their quotient classes receive the same codeword under \(\eta\). Injectivity of \(\eta\) gives
\[
v\,E_\rho\,w
\quad\Longleftrightarrow\quad
\forall i\le m\,
\bigl(
v\models\psi_i
\Longleftrightarrow
w\models\psi_i
\bigr).
\]
Therefore
\[
\rho
\equiv
\bigwedge_{i=1}^{m}
\bigl(
\psi_i(\mathbf p_1)\leftrightarrow\psi_i(\mathbf p_2)
\bigr),
\]
and the lower bound is attained.

Since
\[
k\le|X|=2^n,
\]
we obtain
\[
\operatorname{srk}(\rho)\le n.
\]
Equality occurs for the discrete coequivalence, where every valuation is its own equivalence class and
\[
k=2^n.
\]
Thus the worst-case bound is sharp.

For the census, \(\mathsf{CPC}\)-coequivalences modulo logical equivalence are in bijection with equivalence relations on the \(N=2^n\) valuations. The number with exactly \(k\) classes is therefore
\[
S(N,k),
\]
and summing over \(k\) gives
\[
B_N=\sum_{k=1}^{N}S(N,k).
\]
The rank formula groups those partitions according to the unique \(m\) satisfying
\[
2^{m-1}<k\le2^m.
\]

## Verification

The proof is finite and exact.

The bundled checker enumerates every set partition of the Boolean valuation set for
\[
n=1,2,3.
\]
For each partition it computes the number \(k\) of blocks, constructs the optimal binary block code, checks that equality of all code coordinates is exactly the partition relation, and confirms the lower bound
\[
k>2^{m-1}
\]
whenever \(m>0\).

It independently computes Stirling numbers and Bell numbers and verifies the rank profiles
\[
(1,1),
\qquad
(1,7,7),
\qquad
(1,127,2667,1345).
\]

The computation is only a finite replay. The theorem for arbitrary \(n\) follows from the coding and pigeonhole proof.

## Relationship to prior work

Almeida and De Berardinis introduce coequivalence separation as an explicit-definability property of quotients. Their Example 3.10 proves that \(\mathsf{CPC}\) has the coequivalence separation property. The proof associates one formula
\[
\psi_C
\]
with each equivalence class \(C\), then represents the coequivalence by requiring agreement on every class-indicator formula.

That argument establishes existence but does not optimize the number of separating formulas. The present result replaces the class-indicator family by an optimal binary code of the quotient classes. Thus a quotient with \(k\) classes needs exactly
\[
\left\lceil\log_2 k\right\rceil
\]
separating formulas rather than one formula per class.

The source paper relates coequivalence separation to effective equivalence relations and, model-theoretically, to uniform elimination of imaginaries. The separation rank therefore measures the minimum number of Boolean coordinates needed to make an implicit finite quotient explicit.

Targeted searches for quantitative coequivalence separation, minimal separating families in \(\mathsf{CPC}\), and Bell-number censuses of coequivalences did not locate this exact optimization or enumeration.

## Limitations

The argument relies essentially on classical propositional definability: every subset of the finite valuation cube is definable. The same logarithmic coding statement does not automatically extend to logics where not every union of quotient classes is definable by a unary formula.

The rank measures only the number of separating formulas, not their syntactic size. The formulas defining the code coordinates can be exponentially large if written as disjunctive normal forms.

The Bell-number census counts semantic equivalence classes of coequivalence formulas, not raw syntactic formulas.

## References

[1] Rodrigo Nicolau Almeida and Matteo De Berardinis, “Coequivalence Relations and Descent in Modal Logic,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 55–74. DOI:10.4204/EPTCS.447.4. arXiv:2606.31854.

[2] Silvio Ghilardi and Marek Zawadowski, *Sheaves, Games, and Model Completions: A Categorical Approach to Nonclassical Propositional Logics*, Trends in Logic 14, Springer, 2002.
