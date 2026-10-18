# Finite iteration of the gap pseudo-hyperjump splits into jump and hyperjump towers
## Finding

Let
\[
H=\operatorname{HJ}_{e_*}
\]
be the pseudo-hyperjump constructed by Cintioli, and define finite iterates by
\[
H^0(X)=X,
\qquad
H^{n+1}(X)=H(H^n(X)).
\]

The one-step dichotomy in the source is stable under finite iteration.

If
\[
\omega_1^X=\omega_1^{\mathrm{CK}},
\]
then for every
\[
n<\omega
\]
one has
\[
\omega_1^{H^n(X)}=\omega_1^{\mathrm{CK}}
\]
and
\[
H^n(X)\equiv_T X^{(n)},
\]
where
\[
X^{(0)}=X,
\qquad
X^{(n+1)}=(X^{(n)})'.
\]

If
\[
\omega_1^X>\omega_1^{\mathrm{CK}},
\]
define the finite hyperjump tower by
\[
Q_0(X)=X,
\qquad
Q_{n+1}(X)=\mathcal O^{Q_n(X)}.
\]
Then for every
\[
n<\omega
\]
one has
\[
\omega_1^{H^n(X)}>\omega_1^{\mathrm{CK}}
\]
and
\[
H^n(X)\equiv_T Q_n(X).
\]

Hence no finite orbit crosses the source's admissible-ordinal switch. Up to Turing degree, the same pseudo-hyperjump behaves under iteration as the ordinary Turing jump on one invariant side and as the relativized hyperjump on the other.

Moreover,
\[
H^n(X)<_T H^{n+1}(X)
\]
for every real \(X\) and every \(n<\omega\).

## Assumptions and scope

For a real \(Y\), \(\omega_1^Y\) denotes the least ordinal with no \(Y\)-recursive well-ordering, and
\[
\omega_1^{\mathrm{CK}}=\omega_1^\varnothing.
\]

The relativized Kleene set
\[
\mathcal O^Y
\]
is the hyperjump of \(Y\).

Cintioli defines
\[
H(Y)=\operatorname{HJ}_{e_*}(Y)=Y\oplus V_*^Y,
\]
where the even column of \(V_*^Y\) codes \(Y'\), while its odd column codes \(\mathcal O^Y\) exactly when
\[
\omega_1^Y>\omega_1^{\mathrm{CK}}.
\]

The source proves the one-step degree dichotomy
\[
\omega_1^Y=\omega_1^{\mathrm{CK}}
\Longrightarrow
H(Y)\equiv_TY',
\]
and
\[
\omega_1^Y>\omega_1^{\mathrm{CK}}
\Longrightarrow
H(Y)\equiv_T\mathcal O^Y.
\]

The present statement concerns finite iteration only. No claim is made about a canonical transfinite iteration of \(H\).

## Proof

We first record the preservation fact needed on the low side.

### Finite Turing jumps preserve the relativized Church--Kleene ordinal

For every real \(Y\),
\[
\omega_1^{Y'}=\omega_1^Y.
\]

Because
\[
Y\leq_TY',
\]
every \(Y\)-recursive well-ordering is \(Y'\)-recursive, so
\[
\omega_1^Y\leq\omega_1^{Y'}.
\]

Conversely,
\[
Y'\leq_{\mathrm{HYP}}Y.
\]
Every \(Y'\)-recursive well-ordering is therefore hyperarithmetic in \(Y\), and every \(Y\)-hyperarithmetic well-ordering has order type below
\[
\omega_1^Y.
\]
Thus
\[
\omega_1^{Y'}\leq\omega_1^Y.
\]

The two inequalities give equality.

### Low side

Assume
\[
\omega_1^X=\omega_1^{\mathrm{CK}}.
\]

We prove by induction on \(n\) that
\[
\omega_1^{H^n(X)}=\omega_1^{\mathrm{CK}}
\]
and
\[
H^n(X)\equiv_TX^{(n)}.
\]

The case \(n=0\) is immediate.

Suppose the statement holds at \(n\), and put
\[
Y=H^n(X).
\]
Then
\[
\omega_1^Y=\omega_1^{\mathrm{CK}}.
\]
Cintioli's Gap Theorem gives
\[
H(Y)\equiv_TY'.
\]
Therefore
\[
H^{n+1}(X)\equiv_T(H^n(X))'
\equiv_T(X^{(n)})'
=
X^{(n+1)}.
\]

By the preservation lemma,
\[
\omega_1^{H^{n+1}(X)}
=
\omega_1^{Y'}
=
\omega_1^Y
=
\omega_1^{\mathrm{CK}}.
\]
This closes the induction.

Thus the low side is forward invariant and the finite orbit is exactly the ordinary jump tower in Turing degree.

### High side

Assume
\[
\omega_1^X>\omega_1^{\mathrm{CK}}.
\]

Again use induction. The case \(n=0\) is immediate.

Suppose
\[
H^n(X)\equiv_TQ_n(X)
\]
and
\[
\omega_1^{H^n(X)}>\omega_1^{\mathrm{CK}}.
\]
Set
\[
Y=H^n(X).
\]
The Gap Theorem gives
\[
H(Y)\equiv_T\mathcal O^Y.
\]

Hyperjump degree is invariant under Turing equivalence. Indeed, Cintioli recalls the standard monotonicity fact
\[
U\leq_{\mathrm{HYP}}V
\Longrightarrow
\mathcal O^U\leq_T\mathcal O^V.
\]
Applying this in both directions to Turing-equivalent reals yields
\[
\mathcal O^Y\equiv_T\mathcal O^{Q_n(X)}.
\]
Therefore
\[
H^{n+1}(X)
\equiv_T
\mathcal O^{Q_n(X)}
=
Q_{n+1}(X).
\]

It remains to show that the high side stays high. The hyperjump computes its oracle, so
\[
Y\leq_T\mathcal O^Y\equiv_TH(Y).
\]
Hence
\[
\omega_1^{H(Y)}
\geq
\omega_1^Y
>
\omega_1^{\mathrm{CK}}.
\]
This closes the induction.

Thus the high side is also forward invariant, and the finite orbit is exactly the iterated hyperjump tower in Turing degree.

### Strict growth

Cintioli's theorem states, for every real \(Y\),
\[
Y<_TH(Y).
\]
Apply this with
\[
Y=H^n(X)
\]
to obtain
\[
H^n(X)<_TH^{n+1}(X)
\]
for every \(n<\omega\).

## Verification

The current primary source was checked at the definition of the switch and at the complete proof of the Gap Theorem.

Definition 2.2 puts a copy of \(Y'\) in the even column for every \(Y\), and puts a copy of
\[
\mathcal O^Y
\]
in the odd column exactly when
\[
\omega_1^Y>\omega_1^{\mathrm{CK}}.
\]

Theorem 2.3 proves, for every real \(Y\),
\[
Y<_TH(Y),
\]
together with the exact one-step dichotomy
\[
H(Y)\equiv_TY'
\]
on the side
\[
\omega_1^Y=\omega_1^{\mathrm{CK}},
\]
and
\[
H(Y)\equiv_T\mathcal O^Y
\]
on the side
\[
\omega_1^Y>\omega_1^{\mathrm{CK}}.
\]

The source also recalls the monotonicity
\[
U\leq_{\mathrm{HYP}}V
\Longrightarrow
\mathcal O^U\leq_T\mathcal O^V,
\]
which makes the hyperjump degree invariant under Turing equivalence.

The only additional lemma is
\[
\omega_1^{Y'}=\omega_1^Y.
\]
Its proof is included above: one inequality follows from \(Y\leq_TY'\), and the other from the fact that \(Y'\) is hyperarithmetic in \(Y\).

A full-text search of the primary preprint found no discussion of iteration. The conclusion restates only the one-step switch.

## Relationship to prior work

Jockusch and Shore developed transfinite iteration theory for classical pseudo-jump operators in 1984. That work makes iteration a natural structural question, but it predates the present \(\Pi^1_1\)-relative pseudo-hyperjump construction and does not contain Cintioli's new admissible-ordinal switch.

Jananthan and Simpson introduced the pseudo-hyperjump inversion problem that Cintioli resolves negatively. Their work concerns inversion and class-restricted inversion rather than finite dynamics of this later counterexample operator.

Cintioli's 2026 paper states the one-step dichotomy and its omitted interval, but does not formulate what happens after feeding its own output back into the same operator.

The finite-iteration theorem shows that the switch is not transient: it partitions the operator into two forward-invariant dynamical regimes, one governed exactly by the ordinary jump tower and the other by the hyperjump tower.

Targeted searches for finite iterates of this operator, pseudo-hyperjump iteration, and the specific source identifier did not locate an equivalent statement.

## Limitations

The theorem concerns only finite iteration.

It does not define or analyze a limit-stage rule, so no transfinite \(H\)-hierarchy is claimed.

The statement is about Turing degrees of the iterates. It does not claim equality of canonical representatives with the ordinary jump or hyperjump towers.

The result is a structural consequence of Cintioli's new one-step theorem plus a standard preservation lemma; no new forcing or priority construction is required.

## References

[1] Patrizio Cintioli, “Pseudo-Hyperjump Inversion Fails for Turing Degrees,” arXiv:2609.37478v1, first posted 27 September 2026.

[2] Hayden R. Jananthan and Stephen G. Simpson, “Turing Degrees of Hyperjumps,” arXiv:2101.08818v2, 19 July 2024; later published in *Higher Recursion Theory and Set Theory*.

[3] Carl G. Jockusch Jr. and Richard A. Shore, “Pseudo-Jump Operators. II: Transfinite Iterations, Hierarchies and Minimal Covers,” *Journal of Symbolic Logic* 49(4) (1984), 1205–1236, DOI:10.2307/2274273.
