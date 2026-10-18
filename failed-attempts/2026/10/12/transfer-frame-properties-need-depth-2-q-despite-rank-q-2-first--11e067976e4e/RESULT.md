# Transfer frame properties need depth \(2^q\) despite rank-\(q+2\) first-order definitions

## Finding

For every integer \(q\ge1\), let \(\mathcal F_q\) be the class of Kripke frames \(F=(W,R)\) satisfying

\[
R^{2^q}\subseteq R.
\]

Then \(\mathcal F_q\) admits a first-order definition of quantifier rank \(q+2\), but every basic modal formula defining \(\mathcal F_q\) by frame validity has modal depth at least \(2^q\). The bound is exact:

\[
\min\{\operatorname{md}(\varphi):\operatorname{Fr}(\varphi)=\mathcal F_q\}=2^q.
\]

Equivalently, for every \(r\ge3\) there is an elementary, modally definable frame class with an FO definition of quantifier rank \(r\) whose shortest possible modal *depth* is exactly \(2^{r-2}\) for this exhibited rank parameter.

## Assumptions and scope

The modal language is the ordinary unimodal propositional language, and a formula defines a frame class when the formula is valid on exactly those frames. Relational powers are exact-length powers: \(xR^m y\) means there is an \(R\)-path of exactly \(m\) edges from \(x\) to \(y\).

The result does **not** claim that \(q+2\) is the minimum first-order quantifier rank of the frame property. It only uses an explicit rank-\(q+2\) definition. It also does not claim the first exponential succinctness separation between first-order and modal logic: strong pointed-model succinctness gaps were known earlier. The retained point is an exact, natural **frame-validity** family, namely the transfer conditions themselves.

## Proof

Balbiani, Fernández-Duque, Herzig, and Iliev define the transfer axiom

\[
\mathrm{TA}(m,n):=\Diamond^m p\to\Diamond^n p
\]

and recall that it defines the frame condition \(R^m\subseteq R^n\). Their Theorem 6.1 proves absolute minimality of the transfer axiom among all formulas defining the same frame class. In the generalized-transitivity case \(0<n<m\), their lower-bound argument in particular forces modal depth at least \(m\).

Set \(m=2^q\) and \(n=1\). Since \(q\ge1\), this is the generalized-transitivity case. Therefore every modal formula defining

\[
R^{2^q}\subseteq R
\]

has modal depth at least \(2^q\). The standard transfer axiom \(\Diamond^{2^q}p\to\Diamond p\) has modal depth exactly \(2^q\), so the lower bound is attained.

For the first-order side, define binary formulas recursively by

\[
\rho_0(x,y):=Rxy,
\qquad
\rho_{i+1}(x,y):=\exists z\bigl(\rho_i(x,z)\wedge\rho_i(z,y)\bigr).
\]

Induction on \(i\) gives two facts simultaneously: \(\rho_i(x,y)\) says exactly that \(xR^{2^i}y\), and \(\operatorname{qr}(\rho_i)=i\). Hence

\[
\tau_q:=\forall x\forall y\bigl(\rho_q(x,y)\to Rxy\bigr)
\]

has quantifier rank \(q+2\) and defines the same frame class \(\mathcal F_q\).

Putting \(r=q+2\) yields the displayed depth \(2^{r-2}\). Thus a logarithmic-depth first-order repeated-squaring description coexists with an exact exponential modal-depth requirement on this natural correspondence family.

## Verification

The source-backed lower bound is Theorem 6.1 of Balbiani--Fernández-Duque--Herzig--Iliev. The new bridge was separately checked by exact finite computation. The bundled script exhausts every directed graph with loops allowed on at most three vertices. For \(q=0,\ldots,4\) it verifies that the recursive \(\rho_q\) relation equals exact \(2^q\)-step reachability. For \(q=1,\ldots,4\), it enumerates every propositional valuation and checks that validity of \(\Diamond^{2^q}p\to\Diamond p\) is equivalent to \(R^{2^q}\subseteq R\). It also checks the symbolic rank/depth identities through \(q=24\).

Running `python3 artifacts/verify.py` returns:

`VERIFY_OK 4818 exact assertions`

The computation validates the correspondence and repeated-squaring parts, not the published modal-depth lower-bound theorem.

## Relationship to prior work

Balbiani et al. already prove that every \((m,n)\)-transfer axiom is absolutely minimal and explicitly measure modal depth. Their paper does not discuss quantifier rank or repeated-squaring compression; a full-text search found no occurrence of “quantifier” or “repeated squaring.” The present finding specializes their exact lower bound to exponentially long relational powers and juxtaposes it with the elementary repeated-squaring FO definition.

Broader first-order/modal succinctness phenomena are older. Hella and Vilander prove a nonelementary formula-size gap between bisimulation-invariant first-order logic and modal logic on pointed models. Otto's modal-depth bounds, restated explicitly in later work by Hodkinson, also use the rank-\(q\) repeated-squaring formula for \(xR^{2^q}y\) and yield pointed-model examples of modal depth about \(2^q\). Those results make the general phenomenon prior art; what was not located is the exact transfer-**frame-validity** consequence \(R^{2^q}\subseteq R\) with minimum modal depth \(2^q\).

Candidate-specific published-finding corpus searches, exact web searches under transfer/quantifier-rank/repeated-squaring aliases, and the current and prior cumulative owned ledgers returned no equivalent frame-property statement.

## Limitations

The originality margin is intentionally modest: this is a short synthesis of a published absolute-minimality theorem with the classical repeated-squaring trick. Specialists in correspondence theory may regard the consequence as folklore even if it is not stated in the inspected literature.

The claim gives an explicit FO definition of rank \(q+2\); it does not prove that this first-order rank is minimal. It also concerns modal depth, not minimum modal formula length. Finally, the finite verifier cannot certify a universal lower bound over all modal formulas; that part rests on the cited theorem.

## References

1. Philippe Balbiani, David Fernández-Duque, Andreas Herzig, Petar Iliev, *Frame-validity games and lower bounds on the complexity of modal axioms*, arXiv:1808.05051; Logic Journal of the IGPL 30(1), 155–185, DOI 10.1093/jigpal/jzaa068.
2. Lauri Hella, Miikka Vilander, *The Succinctness of First-order Logic over Modal Logic via a Formula Size Game*, Advances in Modal Logic 11 (2016), arXiv:1604.07225. (Broader prior-art comparison, not an initiating source.)
3. Ian Hodkinson, *Characterizations of two basic hybrid logics*, Journal of Logic and Computation 35(4) (2025), DOI 10.1093/logcom/exaf025, especially the discussion of Otto's optimal modal-depth bound and the repeated-squaring formula. (Broader prior-art comparison.)
