# Hall certificates for the inquisitive finiteness formula on row-finite teams
## Finding
Let \(D\) be a nonempty set, let \(X\) be a team with domain \(\{x,y\}\), and write
\[
R=X[x,y]\subseteq D\times D.
\]
For \(a\in D\), put \(R(a)=\{c\in D:aRc\}\), and for \(S\subseteq D\) put
\[
N_R(S)=\bigcup_{a\in S}R(a).
\]
Consider the Kontinen--Ciardelli formula
\[
\phi(x,y)=\Bigl(=(x,y)\wedge =(y,x)\wedge \exists^{\mathsf q}z\,(z\ne y)\Bigr)\to \exists^{\mathsf q}u\,(u\ne x),
\]
where \(\exists^{\mathsf q}\) denotes their inquisitive existential quantifier.

The following statements hold.

First, \(\mathcal M\not\models_X\phi(x,y)\) if and only if there are an element \(b\in D\) and an injective function
\[
f:D\longrightarrow D\setminus\{b\}
\]
such that \((a,f(a))\in R\) for every \(a\in D\). Equivalently, the bipartite graph represented by \(R\) contains a matching saturating the entire left copy of \(D\) while omitting at least one right vertex.

Second, suppose that \(R\) is **row-finite**, meaning that every set \(R(a)\) is finite. Then
\[
\mathcal M\models_X\phi(x,y)
\quad\Longleftrightarrow\quad
\forall b\in D\;\exists\text{ finite }S\subseteq D:\ |N_R(S)\setminus\{b\}|<|S|.
\]
Thus, on row-finite teams, support of this open inquisitive formula is exactly the assertion that deleting any one right-hand value creates a finite Hall obstruction.

Third, row-finiteness cannot simply be dropped from this finite-certificate characterization. Let \(D=\mathbb N_0\) and define
\[
R(0)=\mathbb N_{>0},\qquad R(n)=\{n\}\quad(n>0).
\]
Then \(\mathcal M\models_X\phi(x,y)\), but for \(b=0\) every finite \(S\subseteq D\) satisfies
\[
|N_R(S)\setminus\{0\}|\ge |S|.
\]
So the absence of an injective total selector need not have a finite Hall witness when an infinite row is allowed.

## Assumptions and scope
The first equivalence requires no finiteness assumption on \(D\) or on the rows of \(R\). The finite-obstruction equivalence uses row-finiteness only to invoke the infinite form of Hall's theorem for a family of finite sets. The underlying model vocabulary is irrelevant to the argument; only the team relation on \(x,y\) is used.

The Hall condition is tested after deletion of a candidate omitted value \(b\). For fixed \(b\), the family of allowed images is
\[
\bigl(R(a)\setminus\{b\}:a\in D\bigr).
\]
A system of distinct representatives for this family is exactly an injective total selector through \(R\) whose range omits \(b\).

## Proof
By the semantics of inquisitive implication, \(X\) fails \(\phi\) exactly when some subteam \(Y\subseteq X\) supports the antecedent and fails the consequent. Let \(Q=Y[x,y]\).

Kontinen and Ciardelli spell out the four relevant semantic facts for such a binary team relation: \(=(x,y)\) says that \(Q\) is a function; \(=(y,x)\) says that it is injective; failure of \(\exists^{\mathsf q}u\,(u\ne x)\) says that \(\operatorname{dom}(Q)=D\); and support of \(\exists^{\mathsf q}z\,(z\ne y)\) says that \(\operatorname{ran}(Q)\ne D\). Therefore \(X\) fails \(\phi\) exactly when it contains the graph of an injective function \(f:D\to D\) with non-surjective range. Choosing any \(b\notin\operatorname{ran}(f)\) gives the first formulation, and the converse is immediate.

Now assume row-finiteness and fix \(b\in D\). Define
\[
A_a=R(a)\setminus\{b\}\qquad(a\in D).
\]
Each \(A_a\) is finite. The infinite Hall theorem for families of finite sets says that the family \((A_a:a\in D)\) has a system of distinct representatives if and only if every finite \(S\subseteq D\) satisfies
\[
\left|\bigcup_{a\in S}A_a\right|\ge |S|.
\]
Since \(\bigcup_{a\in S}A_a=N_R(S)\setminus\{b\}\), an injective total selector omitting \(b\) exists exactly when no finite Hall-deficient \(S\) exists. The first equivalence then shows that \(X\) supports \(\phi\) exactly when every \(b\) has such a finite deficiency witness.

For the boundary example, every \(n>0\) has the unique allowed image \(n\). Hence any total selector through \(R\) must satisfy \(f(n)=n\) for all \(n>0\), leaving no value for \(f(0)\) that preserves injectivity. Thus no injective total selector exists and \(X\) supports \(\phi\). On the other hand, when \(b=0\), any finite \(S\) not containing \(0\) has \(N_R(S)=S\), while any finite \(S\) containing \(0\) has infinitely many neighbors. In both cases Hall's finite inequality holds. This proves the claimed sharp boundary.

## Verification
The proof above is symbolic. The bundled script `verify_hall_certificates.py` independently checks the finite Hall equivalence for every small finite set-family in its test range and checks the finite truncations of the boundary example. Those truncations have no Hall deficiency on a proper subset containing the special left vertex, while the deficiency is pushed to the full finite truncation; this is the finite pattern whose witness escapes to infinity in the displayed counterexample.

## Relationship to prior work
Kontinen and Ciardelli introduced the displayed formula in their 2026 work on the expressive power of inquisitive team logic. Their proof of the finiteness sentence extracts exactly the functional, injective, total-domain, and non-surjective-range conditions from a witness subteam. They then use the open formula to separate inquisitive team logic from first-order logic. In the inspected text, the formula is not recast as a matching problem, and no Hall characterization, row-finite finite-obstruction theorem, or boundary example of the form above is stated.

The matching ingredient is the classical infinite Hall theorem for families of finite sets. Cameron's 2026 survey states this version explicitly and also recalls the standard failure of the naive finite-subfamily criterion when infinite member sets are allowed. The result here applies that exact boundary to the team relation of the inquisitive formula and identifies the deleted-right-vertex Hall certificates that characterize support.

## Limitations
The theorem does not give a uniform bound on the size of a finite deficiency witness \(S\); even with finite rows, witness sizes can grow arbitrarily. It does not claim that row-finiteness is the only hypothesis under which some other infinitary or compactness-based matching criterion is possible. The boundary example establishes only that the stated finite Hall-certificate equivalence fails without a finiteness condition on the allowed-image sets.

The literature comparison cannot exclude an equivalent observation under terminology not surfaced by the searches, particularly in work connecting dependence logic, infinite matchings, or database dependencies.

## References
1. J. Kontinen and I. Ciardelli, *On the expressive power of inquisitive team logic and inquisitive first-order logic*, arXiv:2603.08646v1, 9 March 2026.
2. P. J. Cameron, *Hall's marriage theorem*, Journal of the London Mathematical Society 113 (2026), e70378, DOI 10.1112/jlms.70378.
