# A single weakly Stalnakerian frame already has non-arithmetical validity
## Finding
Let \(\mathfrak F_*\) be the constant-domain selection frame
\[
\mathfrak F_*=\langle W,R,f,D,d\rangle
\]
with \(W=D=\omega\), \(R=\omega^2\), \(d(n)=\omega\), and
\[
f(X,n)=
\begin{cases}
\{\min(X\setminus\{m:m<n\})\},&X\setminus\{m:m<n\}\neq\varnothing,\\
\varnothing,&\text{otherwise}.
\end{cases}
\]
Let \(WS\) denote the class of weakly Stalnakerian selection frames. For each closed first-order arithmetic sentence \(\alpha\), let
\[
\theta_\alpha:=AX\to\alpha^*
\]
be the Kocurek--Walsh--Weiss translation, with \(AX\) the conjunction of their eight arithmetic-coding axioms and \(\alpha^*\) the associated relativized translation.

Then
\[
\mathbb N\models\alpha
\quad\Longleftrightarrow\quad
\mathfrak F_*\Vdash\theta_\alpha.
\]
In fact, for every class \(\mathcal K\) satisfying
\[
\mathfrak F_*\in\mathcal K\subseteq WS,
\]
one has
\[
\mathbb N\models\alpha
\quad\Longleftrightarrow\quad
\mathcal K\Vdash\theta_\alpha.
\]
Thus true arithmetic many-one reduces to the validity set of one fixed, explicit, countable frame with universal accessibility and a fixed selection function. It follows that \(L(\mathfrak F_*)\), and every \(L(\mathcal K)\) in the displayed sandwich, is non-arithmetical; in particular, none is recursively enumerable or co-recursively enumerable.

## Assumptions and scope
Validity on a frame means truth at every world under every admissible predicate interpretation and variable assignment for the constant domain \(D=\omega\). The result concerns the proposition-based set-selection semantics used in the cited work.

The input \(\alpha\) is required to be a closed arithmetic sentence. This restriction repairs a free-variable overstatement in the source theorem: the reduction needed for non-arithmeticality uses only sentences.

The primary literature proves the universal half of the reduction over all weakly Stalnakerian frames and supplies, for the converse, a countermodel whose underlying frame is exactly \(\mathfrak F_*\).

## Proof
First, \(\mathfrak F_*\) is weakly Stalnakerian. Success holds because every selected point lies in \(X\). Weak Centering holds because if \(n\in X\), then \(n\) is the least member of \(X\) not below \(n\), so \(f(X,n)=\{n\}\). Uniqueness is immediate.

For Uniformity, suppose \(f(X,n)\subseteq Y\) and \(f(Y,n)\subseteq X\). If one selected set is empty, then both are empty: for example, if \(f(X,n)=\varnothing\) but \(f(Y,n)=\{y\}\), then \(y\in X\) and \(y\ge n\), contradicting \(f(X,n)=\varnothing\). If both are nonempty, write \(f(X,n)=\{x\}\) and \(f(Y,n)=\{y\}\). Since \(x\in Y\) and \(y\) is the least member of \(Y\) at least \(n\), \(y\le x\). Since \(y\in X\) and \(x\) is the least member of \(X\) at least \(n\), \(x\le y\). Hence \(x=y\), so the selected sets agree.

Now fix a closed arithmetic sentence \(\alpha\).

If \(\mathbb N\models\alpha\), the sentence-corrected arithmetic interpretation theorem of Kocurek--Walsh--Weiss gives
\[
WS\Vdash\theta_\alpha.
\]
Therefore \(\mathfrak F_*\Vdash\theta_\alpha\), and more generally \(\mathcal K\Vdash\theta_\alpha\) for every \(\mathcal K\subseteq WS\).

Conversely, suppose \(\mathbb N\not\models\alpha\). The explicit countermodel used in the source proof has underlying frame \(\mathfrak F_*\), satisfies \(AX\) at world \(0\), and makes the translated arithmetic structure at that world isomorphic to the standard natural numbers. Therefore that interpretation falsifies \(\alpha^*\) at world \(0\), hence falsifies \(\theta_\alpha\) there. Thus
\[
\mathfrak F_*\not\Vdash\theta_\alpha.
\]
If \(\mathfrak F_*\in\mathcal K\), the same witness gives
\[
\mathcal K\not\Vdash\theta_\alpha.
\]
This proves both equivalences.

The map \(\alpha\mapsto\theta_\alpha\) is computable. If \(L(\mathfrak F_*)\) were arithmetical, then its computable preimage under this map would be arithmetical, contradicting the non-arithmeticality of true first-order arithmetic. The same argument applies to every \(L(\mathcal K)\) in the sandwich. Since every recursively enumerable or co-recursively enumerable set of formulas is arithmetical, neither kind of enumeration exists.

## Verification
The proof was reconstructed in both directions rather than inferred from the global non-axiomatizability statement. The forward implication uses only the source theorem's universal validity over \(WS\). The reverse implication uses the source proof's specific \(\omega\)-frame witness, which is why localization to one frame is available.

The weakly Stalnakerian frame conditions were checked directly for the displayed \(f\), including the empty-selection case in Uniformity. The sentence restriction was imposed explicitly, avoiding the known free-variable counterexample to the source theorem as originally worded.

The sandwich extension was checked separately: the true-arithmetic direction descends from \(WS\) to every subclass, while the false-arithmetic direction ascends from the single member \(\mathfrak F_*\) to every class containing it.

## Relationship to prior work
Kocurek, Walsh, and Weiss prove that first-order weakly Stalnakerian validity is non-arithmetical by interpreting arithmetic. Their proof of the negative direction uses the explicit frame \(\mathfrak F_*\) above. The present finding extracts a localization consequence from that proof architecture: the entire lower bound already holds for validity on that one fixed frame, and therefore for every class lying between that frame and \(WS\).

This is stronger than the class-level conclusion in a way that does not follow merely from non-arithmeticality of \(L(WS)\): an intersection of frame logics can be complicated even when each individual frame logic is simpler. The explicit fixed countermodel is the additional ingredient that makes the localization work.

Related work on propositionally quantified modal logics over relational frames studies axiomatizability and complexity for different languages and semantics; it does not subsume this first-order conditional-selection fixed-frame statement.

## Limitations
This is a localization of the 2026 arithmetic encoding, not a new arithmetic interpretation. It does not determine the exact analytical-hierarchy complexity of \(L(\mathfrak F_*)\), nor does it show that arbitrary fixed weakly Stalnakerian frames have non-arithmetical validity.

The conclusion is for closed arithmetic inputs. No corresponding claim is made for the source theorem's unrestricted open-formula wording.

The result concerns proposition-based set-selection semantics and should not be transferred without proof to formula-based quasi-selection semantics or to unrelated quantified modal systems.

## References
Alexander W. Kocurek, James Walsh, and Yale Weiss, “Stalnaker's logical problem of conditionals is unsolvable,” arXiv:2608.07387, first public version 2026-08-07.

Alexander W. Kocurek, James Walsh, and Yale Weiss, “Incompleteness in Quantified Conditional Logic,” arXiv:2602.04073, first public version 2026-02-03.

Peter Fritz, “Axiomatizability of Propositionally Quantified Modal Logics on Relational Frames,” Journal of Symbolic Logic 89 (2024), 758–793.
