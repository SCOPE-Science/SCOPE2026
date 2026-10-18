# Egrot–Hirsch rainbow witnesses are size-optimal within their depth-equivalence scheme

## Finding
For every integer \(n\ge 0\), put \(R=2^{n+1}\). In the modified-rainbow family \(B_{S,T}\) used by Egrot and Hirsch, any representable/nonrepresentable pair of the form \(B_{P,U},B_{Q,U}\) that is certified \(n\)-equivalent by their Corollary 4.5 must have a larger member with at least
\[
R^2+R+5=4^{n+1}+2^{n+1}+5
\]
atoms, hence at least
\[
2^{4^{n+1}+2^{n+1}+5}
\]
elements. Equality is attained, up to swapping the two members, exactly when
\[
|U|=|P|=R,\qquad |Q|=R+1.
\]
These are precisely the cardinal parameters used in their Theorem 4.6. Thus their standard witness pair is not merely sufficient: it is size-optimal within the parameter regime certified by their own depth-equivalence theorem and representability criterion.

The representable optimal witness has \(R^2+R+4\) atoms and the nonrepresentable optimal witness has \(R^2+R+5\) atoms, so their complex-algebra cardinalities differ by exactly a factor of \(2\).

## Assumptions and scope
The statement is deliberately method-relative. It concerns only pairs \(B_{P,U},B_{Q,U}\) with the same second rainbow parameter for which two published facts are used exactly as stated: Corollary 4.5 supplies \(n\)-equivalence from \(|P|,|Q|\ge 2^{n+1}\), and Theorem 3.2 supplies representability exactly when the first parameter has cardinality at most the second. No claim is made that these are the globally smallest finite relation algebras separated by quantifier depth \(n+1\), or that every possible rainbow construction must obey the same bound.

## Proof
Egrot and Hirsch define \(B_{S,T}\) with atoms
\[
\{1',b,w,y\}\cup\{g_i:i\in S\}\cup\{r_{j,j'}:j,j'\in T\},
\]
so
\[
|\operatorname{At}(B_{S,T})|=4+|S|+|T|^2.
\]
For finite \(|S|\ge2\), their Theorem 3.2 gives
\[
B_{S,T}\text{ is representable}\quad\Longleftrightarrow\quad |S|\le |T|.
\]
Their Corollary 4.5 says that if \(|T|,|T'|\ge 2^{n+1}\), then \(B_{T,S}\equiv_n B_{T',S}\).

Now fix a source-certified pair \(B_{P,U},B_{Q,U}\) that is \(n\)-equivalent and has exactly one representable member. After interchanging \(P,Q\) if necessary,
\[
|P|\le |U|<|Q|.
\]
Corollary 4.5 requires \(|P|,|Q|\ge R\), where \(R=2^{n+1}\). Hence \(|U|\ge |P|\ge R\), while integrality of cardinalities gives \(|Q|\ge |U|+1\). Therefore the nonrepresentable member, which is also the larger one, has at least
\[
4+|Q|+|U|^2\ge 4+(R+1)+R^2=R^2+R+5
\]
atoms.

Equality forces \(|U|=R\) and \(|Q|=R+1\). Since \(R\le |P|\le |U|\), equality also forces \(|P|=R\). Conversely these values satisfy all constraints and are exactly those chosen in Theorem 4.6. The other algebra then has \(R^2+R+4\) atoms. Since a finite complex algebra on \(a\) atoms has \(2^a\) elements, the two optimal algebras have cardinalities differing by exactly \(2\).

Because the pair is \(n\)-equivalent but differs on representability, every first-order sentence separating them has quantifier depth at least \(n+1\). Writing
\[
M_n=2^{R^2+R+5}
\]
for the larger witness size, for \(n\ge1\) we have \(R\ge4\) and \(R^2+R+5\le2R^2\), so
\[
\log_2\log_2 M_n\le 1+2\log_2R=2n+3.
\]
Thus this optimized family also gives the explicit scale
\[
\operatorname{qd}_{\mathrm{sep}}(M_n)\ge n+1\ge \tfrac12\log_2\log_2 M_n-\tfrac12.
\]
This last inequality is only a size-versus-depth reading of this particular witness family, not a global lower bound for all finite relation algebras of size at most \(M\).

## Verification
A standalone exact-arithmetic verifier recomputes the atom counts, exhaustively minimizes the feasible integer parameter triples in bounded neighborhoods for \(0\le n\le6\), checks the symbolic lower-bound pattern through \(n=20\), and verifies the displayed half-log-log inequality. It returns `VERIFY_OK 601 exact assertions`.

The proof itself is independent of the finite search: it is the two-line inequality \(|U|\ge R\), \(|Q|\ge |U|+1\), followed by monotonicity of \(4+|Q|+|U|^2\).

## Relationship to prior work
Egrot and Hirsch prove the unbounded-quantifier-depth theorem and choose \(|S|=2^{n+1}\), \(|T|=2^{n+1}+1\) in their separating pair, but they do not state the parameter choice as a unique minimum-size solution within the constraints of Corollary 4.5 and Theorem 3.2. The present observation isolates and proves that optimization statement.

There is earlier work on the equational complexity of representable relation algebras, including logarithmic-logarithmic lower bounds in terms of equation length. That complexity measure and its witness constructions are different from first-order quantifier depth, so those results do not imply the exact rainbow-parameter minimum above.

## Limitations
The optimality is relative to the specific Egrot–Hirsch modified-rainbow scheme and to using their published depth-equivalence criterion without strengthening it. A different family, a sharper Ehrenfeucht–Fraïssé analysis, or an entirely different construction could yield smaller separating algebras. The asymptotic half-log-log coefficient extracted above is therefore not claimed to be globally optimal. Because the minimization is short once the two source results are juxtaposed, an uncatalogued-folklore risk remains despite targeted searches.

## References
1. Rob Egrot and Robin Hirsch, *First-order axiomatisations of representable relation algebras need formulas of unbounded quantifier depth*, arXiv:2008.01329; *Journal of Symbolic Logic*, DOI 10.1017/jsl.2021.88.
2. Jeremy F. Alm, *On the equational complexity of RRA*, *Algebra Universalis* 68 (2012), DOI 10.1007/s00012-012-0210-3.
3. Jeremy F. Alm, Robin Hirsch, and Roger D. Maddux, work on strongly representable atom structures and equational complexity, DOI 10.1017/S1755020316000265.
