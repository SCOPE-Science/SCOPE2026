# Finite-jump unboundedness in reflected omega-models
## Finding

Let
\[
(\omega,\mathcal S)\models\mathsf{RCA}_0+\Sigma^1_1\text{-}\mathsf{Rfn},
\]
where \(\Sigma^1_1\text{-}\mathsf{Rfn}\) is the Lévy–Montague reflection scheme studied by Pakhomov.

Fix any finite tuple
\[
A_0,\ldots,A_{m-1}\in\mathcal S
\]
and any standard integer
\[
k\ge0.
\]
Then there is
\[
B\in\mathcal S
\]
such that
\[
\boxed{
B\not\le_T
(A_0\oplus\cdots\oplus A_{m-1})^{(k)}.
}
\]

Thus the second-order part of an omega-model of
\[
\mathsf{RCA}_0+\Sigma^1_1\text{-}\mathsf{Rfn}
\]
is never Turing-bounded by a fixed finite jump of a finite join of its own sets.

In particular, no principal Turing ideal can be such an omega-model. More generally, for no finite tuple from the model and no fixed finite \(k\) can every set of the model lie below the \(k\)-th jump of that tuple's join.

The conclusion is deliberately pointwise in \(k\): for each fixed \(k\) some set escapes the \(k\)-th jump. No claim is made that a single set simultaneously escapes every finite jump of the same parameter join.

## Assumptions and scope

Pakhomov calls a second-order model uniformly enumerated when there is a formula
\[
\varphi(e,y,\vec A),
\]
possibly with set parameters, such that
\[
\forall X\,\exists e\,\forall y
\bigl(y\in X\leftrightarrow\varphi(e,y,\vec A)\bigr).
\]

His Theorem 6.1 shows, for every candidate formula \(\varphi\), that a finite collection of reflection instances refutes the corresponding uniform-enumeration assertion. When \(\varphi\) is arithmetical, those required instances belong already to
\[
\Sigma^1_1\text{-}\mathsf{Rfn}.
\]

We use only this arithmetical case.

The superscript
\[
A^{(k)}
\]
denotes the standard \(k\)-fold Turing jump of \(A\). The jump need not itself belong to \(\mathcal S\); it is used externally as a bound in the Turing degrees.

Because \(\mathsf{RCA}_0\) is closed under finite joins inside every omega-model, the finite tuple may be replaced by its join
\[
A=A_0\oplus\cdots\oplus A_{m-1}.
\]

## Proof

Fix
\[
A=A_0\oplus\cdots\oplus A_{m-1}\in\mathcal S
\]
and a standard
\[
k\in\omega.
\]

For this fixed \(k\), there is an arithmetical formula
\[
\varphi_k(e,y,A)
\]
expressing that the \(e\)-th oracle Turing computation, with oracle \(A^{(k)}\), halts on input \(y\) with output \(1\).

This relation is arithmetical in \(A\). For each externally fixed finite \(k\), membership in \(A^{(k)}\) has an arithmetical definition relative to \(A\), so a finite oracle computation using \(A^{(k)}\) can be unfolded into a first-order arithmetical formula with parameter \(A\).

Suppose toward a contradiction that
\[
\forall B\in\mathcal S\qquad B\le_T A^{(k)}.
\]

Take any
\[
B\in\mathcal S.
\]
By the assumed Turing reducibility, there is an index \(e\) for a total \(A^{(k)}\)-oracle characteristic computation of \(B\). Hence, for every
\[
y\in\omega,
\]
we have
\[
y\in B
\quad\Longleftrightarrow\quad
\varphi_k(e,y,A).
\]

Therefore the omega-model satisfies
\[
\forall B\,\exists e\,\forall y
\bigl(y\in B\leftrightarrow\varphi_k(e,y,A)\bigr).
\]

So the single arithmetical formula
\[
\varphi_k
\]
uniformly enumerates the entire second-order part \(\mathcal S\).

But Pakhomov's Theorem 6.1 shows that
\[
\Sigma^1_1\text{-}\mathsf{Rfn}
\]
refutes uniform enumeration by any arithmetical formula, including formulas with set parameters. This contradicts
\[
(\omega,\mathcal S)\models\Sigma^1_1\text{-}\mathsf{Rfn}.
\]

Thus some
\[
B\in\mathcal S
\]
satisfies
\[
B\not\le_T A^{(k)}.
\]

Since the finite tuple and standard \(k\) were arbitrary, the theorem follows.

For the principal-ideal corollary, take
\[
k=0.
\]
If \(\mathcal S\) were generated as a Turing ideal by a single set \(A\in\mathcal S\), every
\[
B\in\mathcal S
\]
would satisfy
\[
B\le_T A,
\]
contradicting the theorem.

## Verification

The proof was checked against the source's definition of uniform enumeration and Theorem 6.1.

The critical translation is exact: if every set in the omega-model is Turing reducible to one fixed finite jump
\[
A^{(k)},
\]
then one arithmetical oracle-computation formula with parameter \(A\) enumerates every set in the model.

The fixed-\(k\) restriction is essential. The argument does not replace all finite jumps simultaneously by one arithmetical predicate, and it does not infer the existence of a single set escaping every finite jump.

The use of a finite tuple adds no strength because its join exists in the omega-model by the basic closure available in \(\mathsf{RCA}_0\).

No finite experiment or degree-theoretic heuristic is used in place of the source's reflection theorem.

## Relationship to prior work

Pakhomov proves that
\[
\mathsf{WKL}_0+\mathsf{Rfn}
\]
is \(\Pi^1_1\)-conservative over \(\mathsf{RCA}_0\), while also showing that already
\[
\Sigma^1_1\text{-}\mathsf{Rfn}
\]
has genuinely new \(\Sigma^1_1\) consequences. The key example is that reflected universes cannot be uniformly enumerated by one formula.

The present result converts that definability obstruction into a concrete restriction on the Turing-degree geometry of every omega-model: no fixed finite jump of finitely many internal sets can dominate the whole second-order part.

This consequence is not the same as jump closure. The theorem does not assert that
\[
A'
\]
belongs to the model whenever \(A\) does. Instead it says that, whatever fixed finite jump is chosen externally as a benchmark, some internal set lies outside its lower Turing cone.

Targeted literature searches for Lévy–Montague reflection together with Turing degrees, finite jumps, principal Turing ideals, and omega-model degree bounds did not locate this formulation.

## Limitations

The escaping set may depend on \(k\). The theorem does not produce one
\[
B
\]
that is non-arithmetical in \(A\).

The result is about omega-models. Nonstandard first-order models require a separate analysis of externally fixed jumps and computation indices.

The theorem gives a necessary degree-theoretic condition, not a characterization of the omega-models of
\[
\Sigma^1_1\text{-}\mathsf{Rfn}.
\]

It also does not imply closure under the Turing jump, arithmetical comprehension, or any stronger standard subsystem.

## References

[1] Fedor Pakhomov, “Lévy–Montague reflection is \(\Pi^1_1\)-conservative over \(\mathsf{WKL}_0\),” arXiv:2608.07050, first posted 7 August 2026.

[2] Stephen G. Simpson, *Subsystems of Second Order Arithmetic*, second edition, Cambridge University Press, 2009.
