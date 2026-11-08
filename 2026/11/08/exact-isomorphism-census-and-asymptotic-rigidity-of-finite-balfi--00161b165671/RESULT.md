# Exact isomorphism census and asymptotic rigidity of finite BALFIs

## Finding

Fix an integer \(k\ge1\). On the Boolean algebra \(B_k=\mathcal P([k])\), consider all pairs of unary operations \(N,C:B_k\to B_k\) satisfying the BALFI equations
\[
 a\cup N(a)=[k],\qquad a\cap N(a)\cap C(a)=\varnothing\quad (a\subseteq[k]).
\]
The usual Boolean operations, implication and bounds are fixed. The full labeled expansion count is
\[
 L_k=6^{k2^{k-1}}.
\]
The expansions with classical Boolean-complement negation \(N(a)=[k]\setminus a\) number \(E_k=2^{k2^k}\). Precisely the remaining \(L_k-E_k\) expansions permit a nonzero contradiction \(a\cap N(a)\), hence the corresponding algebraic counterexample to unrestricted explosion.

The isomorphism count has a uniform finite formula. Let \(\pi\in S_k\) act on subsets by permutation of atoms. For each orbit \(O\) of subsets under \(\langle\pi\rangle\), choose a representative \(a_O\), and write \(d_O=|O|\). The power \(\pi^{d_O}\) preserves \(a_O\). Let \(i_O\) and \(o_O\) be the numbers of cycles of this power contained in \(a_O\) and its complement, respectively, and write \(c_O=i_O+o_O\). Then
\[
 U_k=\frac1{k!}\sum_{\pi\in S_k}\prod_{O}3^{i_O}2^{o_O},\qquad
 V_k=\frac1{k!}\sum_{\pi\in S_k}\prod_O2^{c_O}.
\]
Here \(U_k\) counts all isomorphism classes, \(V_k\) counts the classical-negation classes, and \(U_k-V_k\) counts the nonclassical-negation classes.

For \(k=1,2,3\), respectively, the triples \((L_k,U_k,V_k)\) are
\[
(6,6,4),\quad (1296,666,136),\quad (2176782336,362937456,2804480).
\]
There is an asymptotically exact simplification:
\[
 1\le\frac{k!U_k}{L_k}\le1+(k!-1)(5/9)^{2^{k-1}/3},
 \qquad U_k\sim\frac{6^{k2^{k-1}}}{k!}.
\]
Thus a uniformly sampled labeled expansion is asymptotically rigid (its only automorphism is the identity).

## Assumptions and scope

An isomorphism preserves the named Boolean operations \(\wedge,\vee,\to,0,1\) and each named extra operation \(N,C\). Boolean implication has its usual definition. There are no additional operator identities, including no monotonicity, involutivity, preservation-of-joins or preservation-of-meets requirements. The parameter \(k\) counts Boolean **atoms**; the carrier has \(2^k\) elements. The statement includes all two-operator tables on that fixed carrier, not only directly presented finite models of particular axiomatic extensions.

The term *classical-negation* means only \(N(a)=\overline a\) for all \(a\); it places no restriction on \(C\). The complementary class is called *nonclassical-negation* or *paraconsistent* in the specific algebraic sense that some \(a\wedge N(a)\ne0\). By the Boolean equations, failure of this condition is equivalent to \(N\) being Boolean complementation.

## Proof

**1. Atomic normal form.** Fix an input \(a\subseteq[k]\) and an atom \(j\). The two equations are coordinatewise. For \(j\in a\), the pair of bits \((\mathbf1_{j\in N(a)},\mathbf1_{j\in C(a)})\) is one of \((0,0),(0,1),(1,0)\), exactly three possibilities. For \(j\notin a\), the first bit is forced to one and the second bit is arbitrary: \((1,0),(1,1)\), exactly two possibilities. Conversely, every independent assignment from these lists satisfies both equations. The number of choices at input \(a\) is \(3^{|a|}2^{k-|a|}\); different inputs impose no constraints upon one another. Since \(\sum_{a\subseteq[k]}|a|=\sum_{a\subseteq[k]}(k-|a|)=k2^{k-1}\), multiplying gives \(L_k\).

An input has \(a\cap N(a)=\varnothing\) exactly when every inside atom chooses one of the first two states, forcing \(N(a)=\overline a\). Globally, with this fixed \(N\), each of the \(2^k\) inputs may independently take any of \(2^k\) values of \(C\), yielding \(E_k=2^{k2^k}\). If some overlap \(a\cap N(a)\) is nonzero, the degree-preserving BALFI interpretation refutes explosion from \(p,Np\): evaluate \(p\) at \(a\), take conclusion value zero, and note \(a\cap N(a)\not\le0\).

**2. Isomorphism normal form.** Every Boolean automorphism of \(\mathcal P([k])\) comes from a unique permutation \(\pi\in S_k\) of its atoms. Hence an expansion is fixed by \(\pi\) precisely when \(N(\pi a)=\pi N(a)\) and \(C(\pi a)=\pi C(a)\) for every input \(a\).

Choose an orbit \(O\) of subsets with representative \(a\) and size \(d\). Equivariance forces all values at the other inputs of \(O\) once \((N(a),C(a))\) has been chosen. The return after \(d\) steps is consistent precisely when this pair is fixed by \(\pi^d\). This power preserves \(a\), so every one of its cycles lies wholly inside or outside \(a\). For a cycle inside, a constant coordinate-state on that cycle can be any of the three states in step 1. For a cycle outside, there are two. The number of equivariant choices on the input orbit is therefore \(3^{i_O}2^{o_O}\). Multiplication over input orbits and Burnside's lemma yield \(U_k\). If \(N\) is constrained to be Boolean complementation, only the \(C\) bit remains free on every atom cycle; the orbit contributes \(2^{c_O}\). Burnside gives \(V_k\), and subtraction counts the remaining isomorphism classes because classical negation is invariant under isomorphism.

**3. Almost-sure rigidity and quantitative bound.** Sample uniformly from the \(L_k\) labeled expansions. The atomic normal form shows that for every pair \((a,j)\) with \(j\in a\), the random bit \(X_{a,j}=\mathbf1_{j\in a\cap N(a)}\) is Bernoulli with parameter \(1/3\). Bits at distinct inputs \(a\) are independent.

Fix a nonidentity \(\pi\in S_k\). Its action on subsets has \(2^{c(\pi)}\le2^{k-1}\) fixed subsets, since \(\pi\) has at most \(k-1\) atom cycles. Thus at least \(2^{k-1}\) subsets move. In each nontrivial orbit \((a_0,a_1,\ldots,a_{d-1})\) with \(a_{t+1}=\pi a_t\), select the disjoint pairs \((a_0,a_1),(a_2,a_3),\ldots\), totaling \(\lfloor d/2\rfloor\ge d/3\) pairs. Every such pair has a nonempty first set, since the empty set is fixed. Choose an atom \(j\in a_{2t}\). If \(\pi\) preserves the expansion, it forces \(X_{a_{2t},j}=X_{a_{2t+1},\pi j}\). These two Bernoulli bits are independent, and equality has probability \((1/3)^2+(2/3)^2=5/9\). The chosen pairs use pairwise distinct inputs, so all these necessary equalities are independent. Their number is at least \(2^{k-1}/3\), giving
\[
\Pr(\pi\text{ is an automorphism})\le(5/9)^{2^{k-1}/3}.
\]
By Burnside and linearity of expectation, \(k!U_k/L_k=\sum_{\pi\in S_k}\Pr(\pi\text{ fixes the sampled expansion})\). Separate the identity term to obtain the displayed bounds. The upper error tends to zero because \((5/9)^{2^{k-1}/3}\) decays doubly exponentially in \(k\), whereas \(k!\) grows only factorially. The same union bound proves that the probability of any nonidentity automorphism tends to zero. This proves the theorem for every integer \(k\ge1\).

## Verification

Run `python3 verify_balfi.py` using only the Python standard library. The program evaluates the Burnside products for all permutations for \(1\le k\le5\), prints both isomorphism counts, and checks the labeled formula. Independently, for \(k=1,2\), it enumerates every admissible pair of complete operation tables using the original BALFI equations, constructs each isomorphism orbit by actual atom permutations, and matches both orbit counts with the Burnside formula. The two-atom calculation visits all 1296 labeled tables. The program reports `BALFI_VERIFY_OK` when all tests pass. This finite verification is not used to infer the all-\(k\) theorem; steps 1–3 are uniform proofs.

## Relationship to prior work

Carnielli, Coniglio and Fuenmayor introduced BALFIs as algebraic semantics for self-extensional paraconsistent logic; their Definition 2.10 gives the two defining equations. Coniglio and Mallea (2026, Definition 2.5 and Lemma 6.5) study these same algebras and show a local support-extension lemma for finite countermodel construction. Their Sections 3 and 6 treat algebraic collapse, finite model methods, and proof-complexity bounds, rather than the all-size labeled/unlabeled census or generic automorphism groups. The atomic independence of operator values follows directly from their defining equations and is not asserted to be a new axiom or earlier semantic discovery. The contribution here is the complete orbit formula for two named operators, including the classical-negation subfamily, and the uniform almost-sure-rigidity theorem with an explicit error bound.

Bonzio, Pra Baldi and Valota (2021) count finite *involutive bisemilattices* using Płonka sums of Boolean algebras. Their models and congruence conditions are not BALFI expansions of one fixed Boolean reduct. General Burnside enumeration is a standard tool and is used without novelty claims for that principle itself.

## Limitations

The result is for all unconstrained BALFIs with a fixed nontrivial finite Boolean reduct, not for subvarieties obtained by adding any of the fourteen further consistency principles. The given Burnside expression is an exact finite formula, not a simple closed generating function. The finite checker exhausts only \(k\le2\) by direct enumeration; the higher values use a proven orbit formula. This proof establishes mathematical consequences of the BALFI equations; it does not assert that no prior literature can contain equivalent enumeration results. No independent mathematical or historical-priority audit is included.

## References

1. W. Carnielli, M. E. Coniglio and D. Fuenmayor, *Logics of Formal Inconsistency enriched with replacement: an algebraic and modal account*, arXiv:2003.09522 (first posted March 20, 2020), especially Definition 2.10 and the neighborhood semantics section. https://arxiv.org/abs/2003.09522
2. M. E. Coniglio and H. F. Mallea, *Self-extensional logics of formal inconsistency: Decidability and limits for paraconsistency*, arXiv:2608.28443 (first posted August 28, 2026), especially Definition 2.5, Lemma 6.5 and Sections 3 and 6. https://arxiv.org/abs/2608.28443
3. S. Bonzio, M. Pra Baldi and D. Valota, *Counting finite linearly ordered involutive bisemilattices*, arXiv:2107.10540 (July 22, 2021), especially Sections 1–3. https://arxiv.org/abs/2107.10540
