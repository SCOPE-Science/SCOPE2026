# Factorial classification of preconditionals on finite chains

## Finding

For every integer \(n\ge 2\), let
\[
C_n=\{c_0=0<c_1<\cdots<c_{n-1}=1\}.
\]
Then the \(\mathsf T\)-algebra preconditionals on \(C_n\) are classified by independent activation indices
\[
\tau_j\in\{j+1,\ldots,n-1\},\qquad 1\le j\le n-2.
\]
For each internal antecedent \(c_i\), put
\[
S_i=\{j<i:\tau_j\le i\}.
\]
The operation is
\[
0\to c_j=1,\qquad 1\to c_j=c_j,
\]
and for \(0<i<n-1\),
\[
c_i\to0=0,\qquad c_i\to c_j=1\quad(j\ge i),
\]
while for \(0<j<i\),
\[
c_i\to c_j=
\begin{cases}
c_k,&k=\min\bigl(S_i\cap\{j,\ldots,i-1\}\bigr)\text{ exists},\\
1,&S_i\cap\{j,\ldots,i-1\}=\varnothing.
\end{cases}
\]
Hence the number of \(\mathsf T\)-preconditionals on \(C_n\) is
\[
\prod_{j=1}^{n-2}(n-1-j)=(n-2)!.
\]
Every such \(\mathsf T\)-algebra is automatically an \(\mathsf F\)-algebra. Exactly one activation pattern, namely \(\tau_j=j+1\) for every \(j\), gives the Heyting implication.

## Assumptions and scope

A preconditional is used in the sense recalled in Chen, arXiv:2607.20221v1: a binary operation on a bounded lattice satisfying the five preconditional axioms. A \(\mathsf T\)-algebra additionally satisfies conditional identity \(a\to a=1\) and semicomplementation \(a\wedge(a\to0)=0\). An \(\mathsf F\)-algebra further satisfies double-negation inflation \(a\le\neg\neg a\), where \(\neg a=a\to0\).

The result concerns finite chains only. It does not classify arbitrary finite lattices, arbitrary \(\mathsf K\)-preconditionals, or relational frames.

## Proof

Fix a \(\mathsf T\)-preconditional on \(C_n\).

Conditional identity and consequent monotonicity imply \(c_i\to c_j=1\) whenever \(i\le j\). For the top antecedent, the first two preconditional axioms give both \(1\to c_j\le c_j\) and \(c_j\le1\to c_j\), hence \(1\to c_j=c_j\). Semicomplementation on a chain gives \(c_i\to0=0\) for every \(i>0\), while conditional identity gives \(0\to0=1\) and therefore \(0\to c_j=1\) for all \(j\).

Now fix \(0<i<n-1\) and write \(f_i(c_j)=c_i\to c_j\). The second preconditional axiom makes \(f_i\) extensive on consequents below \(c_i\), and consequent monotonicity makes it monotone. Applying the importation axiom with the inner antecedent equal to the outer antecedent gives
\[
c_i\to(c_i\to c_j)\le c_i\to c_j.
\]
If \(d=c_i\to c_j<1\), then \(d<c_i\): otherwise conditional identity would give \(c_i\to d=1>d\). Since \(d<c_i\), extensivity gives \(d\le c_i\to d\); combining the two inequalities yields \(c_i\to d=d\). Thus every non-top value of row \(i\) is a fixed point of that row.

Let
\[
S_i=\{j:0<j<i\text{ and }c_i\to c_j=c_j\}.
\]
For \(0<j<i\), monotonicity and extensivity now force \(c_i\to c_j\) to be the least fixed point \(c_k\) with \(k\ge j\), if such a fixed point exists, and to be \(1\) otherwise.

The cross-row importation axiom says that whenever \(h<i\) and \(d=c_h\to c_j<1\),
\[
c_i\to d\le d.
\]
Extensivity gives the reverse inequality, so \(c_i\to d=d\). Every member of \(S_h\) occurs as such a value by taking its own consequent. Therefore
\[
S_h\subseteq S_i\qquad(h<i).
\]
Conversely, any family of sets \(S_i\subseteq\{1,\ldots,i-1\}\) increasing in this sense defines rows by the least-fixed-point rule above, and those rows satisfy all five preconditional axioms, conditional identity, and semicomplementation. The only non-immediate axiom is cross-row importation: if an earlier row returns a non-top value, that value belongs to its fixed-point set and hence to every later fixed-point set, so the later row fixes it; if the earlier row returns \(1\), the inequality is trivial.

An element \(j\in\{1,\ldots,n-2\}\) can first enter the nested fixed-point sets at any row
\[
\tau_j\in\{j+1,\ldots,n-1\},
\]
where \(\tau_j=n-1\) means that it is never fixed by an internal row before the top row. These first-entry choices are independent and reconstruct the entire nested family. Therefore the number of operations is
\[
\prod_{j=1}^{n-2}(n-1-j)=(n-2)!.
\]

Finally, on a chain semicomplementation forces \(\neg c_i=0\) for every \(i>0\), while conditional identity gives \(\neg0=1\). Hence \(\neg\neg0=0\) and \(\neg\neg c_i=1\) for \(i>0\), so double-negation inflation always holds. Thus every \(\mathsf T\)-algebra on a chain is already an \(\mathsf F\)-algebra.

The Heyting implication on a finite chain is \(a\Rightarrow b=1\) when \(a\le b\) and \(a\Rightarrow b=b\) otherwise. This is exactly the activation pattern \(\tau_j=j+1\) for all \(j\). Any later activation makes some lower consequent map strictly above itself, so the operation is not the Heyting implication.

## Verification

The accompanying `verify_chain_preconditionals.py` performs two independent finite checks. It constructs every activation-pattern operation for \(2\le n\le8\), checks all five preconditional axioms together with the \(\mathsf T\)- and \(\mathsf F\)-conditions, and confirms the factorial counts. Separately, for \(2\le n\le6\), it exhausts all row maps satisfying the easy chain constraints and filters them by the cross-row importation axiom; the resulting operation sets agree exactly with the activation construction.

These computations corroborate the general proof but are not used as a substitute for it.

## Relationship to prior work

Chen's 2026 preprint introduces the systems \(\mathsf K\subseteq\mathsf T\subseteq\mathsf F\), gives their algebraic semantics, and proves strong completeness, finite model property, and decidability. In particular, it defines \(\mathsf T\)-algebras as preconditionals with conditional identity and semicomplementation, and \(\mathsf F\)-algebras by adding double-negation inflation. The preprint does not state a finite-chain classification or factorial count; searches within the public full text for “chain”, “finite chain”, and “factorial” returned no occurrence.

The present result is a finite-algebra classification inside that newly introduced hierarchy. It shows that total orders erase the distinction between \(\mathsf T\) and \(\mathsf F\), while still supporting factorially many distinct preconditionals; only one is Heyting implication.

## Limitations

The proof uses totality of the lattice order essentially, especially when semicomplementation forces every positive element to have negation \(0\). No analogous count is asserted for non-chain lattices. The literature comparison found no matching chain classification in the inspected sources and searches, but this is not a claim that every possible terminology or unpublished source has been exhausted.

## References

1. Zhicheng Chen, “Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations,” arXiv:2607.20221v1, first posted 2026-07-22.
