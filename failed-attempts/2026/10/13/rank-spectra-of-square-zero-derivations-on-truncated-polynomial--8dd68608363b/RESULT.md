# Rank spectra of square-zero derivations on truncated polynomial algebras in characteristic two

## Finding
Fix an integer \(s\geq1\), a finite field \(k=\mathbb F_q\) of characteristic \(2\), and either \(n=2s\) or \(n=2s+1\). Let \(A_n=k[t]/(t^n)\). For each \(k\)-linear algebra derivation \(D:A_n\to A_n\) with \(D^2=0\), use the rank of its underlying \(k\)-linear operator. Define
\[
\mathcal P_{n,q}(X)=\sum_{\substack{D\in\operatorname{Der}_k(A_n)\\D^2=0}}X^{\operatorname{rank}D}.
\]
Then the complete rank polynomial, for both \(n=2s\) and \(n=2s+1\), is
\[
\boxed{\mathcal P_{2s,q}(X)=\mathcal P_{2s+1,q}(X)
=1+\sum_{r=1}^{\lfloor s/2\rfloor}(q^2-1)q^{2r-2}X^r
+\sum_{r=\lfloor s/2\rfloor+1}^{s}(q-1)q^{s-1}X^r.}
\]
In particular, the number of square-zero derivations in either algebra is
\[
\boxed{q^s+\lfloor s/2\rfloor(q-1)q^{s-1}.}
\]
There is an explicit rank-preserving bijection between the two sets of square-zero derivations, despite the different dimensions of the underlying algebras.

## Assumptions and scope
Here \(k\) is any finite field with \(q=2^a\) elements, \(a\geq1\), and \(s\geq1\). Derivations are \(k\)-linear and satisfy the usual Leibniz rule. Composition is meant in \(D^2\). The defining equations and the rank-preserving bijection also hold over an arbitrary field of characteristic \(2\); finiteness is needed only for the counts.

Let \(R_s=k[x]/(x^s)\). For \(F\in R_s\), define \(v_x(F)\) to be the least exponent of \(x\) occurring with nonzero coefficient, taking \(v_x(0)=s\). Valuations are truncated at \(s\) throughout.

## Proof
**1. All derivations and the two normal forms.** Every derivation is specified by \(f=D(t)\); the condition \(D(t^n)=nt^{n-1}f=0\) is sufficient to descend from \(k[t]\). Thus for even \(n\), every \(f\in A_n\) is allowed; for odd \(n\), exactly those \(f\in(t)\) are allowed. Writing \(x=t^2\), there are unique pairs \((E,H)\in R_s^2\) with
\[
D_{E,H}^{(2s)}(t)=E(t^2)+tH(t^2),\qquad
D_{E,H}^{(2s+1)}(t)=t^2E(t^2)+tH(t^2).
\]
The pairs parametrize all derivations in the respective algebras.

**2. Square-zero criterion.** In characteristic two, \(D^2\) is again a derivation: the middle term \(2D(a)D(b)\) in the iterated Leibniz rule vanishes. Hence \(D^2=0\) if and only if \(D^2(t)=0\). For \(D=D_f\), differentiation gives \(D^2(t)=ff'\). In both displays above, \(f'=H(t^2)\). Consequently
\[
ff'=E(t^2)H(t^2)+tH(t^2)^2
\]
for even truncation, and
\[
ff'=t^2E(t^2)H(t^2)+tH(t^2)^2
\]
for odd truncation. The even and odd powers of \(t\) cannot cancel. Respecting the respective truncation moduli shows, in both cases,
\[
\boxed{D_{E,H}^2=0\quad\Longleftrightarrow\quad EH=0\ \text{and}\ H^2=0\ \text{in}\ R_s.}
\]
This establishes a bijection, via the same pair \((E,H)\), between the square-zero derivations for the two lengths.

**3. Ranks.** For every admissible nonzero \(f\), the image of \(D_f\) is generated over \(k\) by the nonzero products \(f,t^2f,t^4f,\ldots\), because derivatives of the odd monomials \(t,t^3,\ldots\) span the even powers. Their lowest nonzero monomials have distinct exponents and are linearly independent. Thus
\[
\operatorname{rank}D_f=\left\lceil\frac{n-v_t(f)}2\right\rceil.
\]
For the two parametrizations, this becomes the same expression
\[
\boxed{\operatorname{rank}D_{E,H}=s-\min\{v_x(E),v_x(H)\}.}
\]
The zero pair gives rank zero. Therefore the bijection from step 2 preserves rank.

**4. Count each rank.** Set \(h=\lceil s/2\rceil\), and for a nonzero pair satisfying the equations put \(v=\min(v_x(E),v_x(H))\). Its rank is \(r=s-v\). When \(v\geq h\), every pair divisible by \(x^v\) satisfies \(EH=H^2=0\), and the number having minimum valuation exactly \(v\) is
\[
q^{2(s-v)}-q^{2(s-v-1)}=(q^2-1)q^{2r-2}.
\]
This is precisely the range \(1\leq r\leq\lfloor s/2\rfloor\).

When \(v<h\), the condition \(H^2=0\) forces \(v_x(H)\geq h>v\), hence \(v_x(E)=v\). The equation \(EH=0\) then requires \(H\in x^{s-v}R_s\). There are \((q-1)q^{s-v-1}\) possibilities for \(E\) of valuation \(v\) and \(q^v\) for \(H\), giving exactly \((q-1)q^{s-1}\) pairs. This corresponds to \(\lfloor s/2\rfloor<r\leq s\). Adding the zero pair proves the polynomial. Summing its coefficients yields the stated total.

## Verification
The accompanying standalone file `verify_square_zero.py` independently enumerates admissible derivation matrices and computes their composition squares and ranks over \(\mathbb F_2\) and \(\mathbb F_4\). It also compares the zero-square matrix condition against the two polynomial equations and checks the rank-preserving parity correspondence. Execute `python3 verify_square_zero.py`; a successful run ends with `VERIFY_OK`.

For example, at \(s=3\) and \(q=2\), both lengths \(n=6,7\) give \(\mathcal P_{n,2}(X)=1+3X+4X^2+4X^3\). These finite checks corroborate the unrestricted proof, rather than establishing it.

## Relationship to prior work
Modular derivation algebras and their restricted-power nilpotent varieties are studied in Cong Chen, *Nilpotent varieties of some finite dimensional restricted Lie algebras* (arXiv:1910.00954v1, 2019), particularly the introduction and Chapter 4. That chapter addresses the minimal restricted envelope of the Zassenhaus algebra under the assumption \(p>3\); it does not provide characteristic-two square-zero derivation rank counts for ordinary truncated one-variable polynomial algebras. Alexander Premet, *Regular derivations of truncated polynomial rings* (arXiv:1405.2426v3, 2014), concerns regular derivations and nilpotent fibres for \(p>2\), not the finite-field spectrum asserted here. These works motivate the restricted-power question but their stated results do not imply the polynomial above.

## Limitations
The theorem concerns the single equation \(D^2=0\) and one-variable truncated polynomial algebras, not all nilpotent derivations, their conjugacy orbits, or higher-dimensional truncated polynomial rings. The enumeration is restricted to characteristic two. The result is algebraically proved; the accompanying exhaustive computations cover only finitely many small cases. Novelty beyond the inspected literature remains subject to possible equivalent formulations in older modular Witt-algebra work and independent expert assessment.

## References
1. Cong Chen, *Nilpotent varieties of some finite dimensional restricted Lie algebras*, arXiv:1910.00954v1, first posted 2019-10-02, https://arxiv.org/abs/1910.00954 .
2. Alexander Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426v3, first posted 2014-05-10, https://arxiv.org/abs/1405.2426 .
