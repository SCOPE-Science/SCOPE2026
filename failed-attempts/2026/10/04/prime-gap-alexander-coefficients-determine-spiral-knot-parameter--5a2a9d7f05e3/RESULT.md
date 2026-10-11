# Prime-gap Alexander coefficients determine spiral-knot parameters
## Finding
Let \(K\) be a knot with normalized monic symmetric Alexander polynomial \(\Delta_K(t)\). Write
\[
D=\deg\Delta_K,
\]
and let \(a_1\) be either coefficient adjacent to an extremal coefficient. Symmetry makes \(|a_1|\) independent of which end is chosen. Put
\[
m=|a_1|-1.
\]

If \(K\) has a spiral representation \(S(p,q,\varepsilon)\), then every possible repetition parameter \(q\) belongs to
\[
\mathcal Q(D,m)=
\left\{
q\ge2:
q\mid m,
\ q-1\mid D,
\ \gcd\!\left(q,1+\frac{D}{q-1}\right)=1
\right\}.
\]
For each \(q\in\mathcal Q(D,m)\), the strand parameter is forced to be
\[
p=1+\frac{D}{q-1}.
\]

In particular, if \(m\) is prime, then any spiral representation must satisfy
\[
q=m,
\qquad
p=1+\frac{D}{m-1}.
\]
Hence the ordered pair \((p,q)\) is uniquely determined by the Alexander polynomial for every spiral knot in this prime-gap subfamily. Consequently the parameter-uniqueness conjecture for spiral knots holds on this subfamily.

There is also an immediate recognition obstruction. If \(m\) is prime and either
\[
m-1\nmid D
\]
or
\[
\gcd\!\left(m,1+\frac{D}{m-1}\right)\ne1,
\]
then \(K\) is not a spiral knot.

For the source example
\[
\Delta_{8_{21}}(t)=t^4-4t^3+5t^2-4t+1,
\]
one has \(D=4\) and \(m=3\). The prime-gap rule would force
\[
q=3,
\qquad
p=1+\frac4{2}=3,
\]
contradicting the coprimality required for a spiral knot. Thus the Alexander polynomial alone excludes \(8_{21}\) from the spiral family; no prior choice of a periodicity order is needed.

## Assumptions and scope
A spiral knot \(S(p,q,\varepsilon)\) is the closure of the standard spiral braid with coprime integers \(p,q\ge2\). The finding uses only two published consequences of the recent Alexander-polynomial formula:
\[
\deg\Delta_{S(p,q,\varepsilon)}=(p-1)(q-1)
\]
and
\[
|a_1|=q\gamma_{p-1}+1,
\]
where \(\gamma_{p-1}\) is a nonnegative integer determined by the sign vector.

The theorem gives necessary conditions for a knot to be spiral and a uniqueness statement when \(m\) is prime. It does not claim that every pair surviving the finite sieve is realized by a spiral knot, and it does not classify the sign vector \(\varepsilon\).

## Proof
Suppose
\[
K=S(p,q,\varepsilon).
\]
The degree formula gives
\[
D=(p-1)(q-1).
\]
Therefore
\[
q-1\mid D
\]
and
\[
p=1+\frac{D}{q-1}.
\]
Because \(S(p,q,\varepsilon)\) is a knot, its defining parameters satisfy
\[
\gcd(p,q)=1.
\]

The adjacent-coefficient formula gives
\[
|a_1|=q\gamma_{p-1}+1.
\]
Subtracting one yields
\[
m=q\gamma_{p-1}.
\]
Hence
\[
q\mid m.
\]
Combining these three necessary conditions proves
\[
q\in\mathcal Q(D,m).
\]
The displayed formula for \(p\) then shows that each surviving \(q\) determines at most one ordered parameter pair.

Now assume \(m\) is prime. Since \(q\ge2\) divides \(m\), necessarily
\[
q=m.
\]
The coefficient identity then also gives
\[
\gamma_{p-1}=1.
\]
Substitution into the degree relation forces
\[
p=1+\frac{D}{m-1}.
\]
Thus every spiral representation of \(K\) has the same ordered pair \((p,q)\). If the displayed value of \(p\) is not integral, or if it is not coprime to \(m\), no spiral representation exists.

For \(8_{21}\), the polynomial has \(D=4\) and adjacent coefficient magnitude \(4\), so \(m=3\). The unique forced pair is \((3,3)\), which violates coprimality. This proves the period-free Alexander obstruction claimed above.

## Verification
The recent source was inspected at Corollaries 3.8 and 3.10, which state the degree and adjacent-coefficient formulas used in the proof, and at Conjecture 5.5, which asks for uniqueness of the parameters \((p,q)\) outside the torus case. Its discussion of \(8_{21}\) was also inspected: there the authors first use external periodicity information to set \(q=2\) and then apply the same Alexander formulas.

The bundled verifier independently checks the arithmetic sieve on synthetic parameter triples through \(p,q<60\). Whenever the synthetic coefficient gap is prime, it confirms that the candidate set is the singleton containing the original ordered pair. It also checks the source example \(6_2\) and the period-free rejection of \(8_{21}\). Its output is:

`VERIFY_OK synthetic_cases=58999 source_6_2=[(5,2,1)] source_8_21=[] prime_gap_unique=true`

The finite calculation is a regression check only. The theorem is proved for all admissible parameters by the divisibility argument above.

## Relationship to prior work
The recent source proves the two exact Alexander-polynomial formulas and uses them for classification questions. It conjectures that a non-torus spiral knot cannot have two different ordered parameter pairs. The source does not state the finite divisor sieve, the prime-gap uniqueness theorem, or the period-free \(8_{21}\) obstruction. Its own \(8_{21}\) argument begins by importing the fact that all nontrivial periods have order two.

Earlier work on spiral-knot determinants fixes a strand number and varies the repetition index, obtaining determinant sequences and recurrences for low strand numbers. That direction does not recover an unknown ordered pair \((p,q)\) from the top Alexander coefficients.

The present result is therefore a partial resolution of the recent parameter-uniqueness conjecture on a naturally detected Alexander-polynomial subfamily, together with a finite necessary-condition sieve for the general case.

## Limitations
The sieve is only necessary: a surviving candidate pair need not be realized by any sign vector.

The prime-gap hypothesis concerns the magnitude of the coefficient adjacent to the leading coefficient. Composite \(m\) can leave several divisors \(q\), so the argument need not determine the parameters uniquely there.

No claim is made that the Alexander polynomial classifies spiral knots or determines \(\varepsilon\); the source gives examples showing that much stronger statement is false.

## References
1. S. Blackwell, A. Das, S. Mayer, L. Moyar, F. L. Quraishi, and R. Stees, *Classical invariants of spiral knots*, arXiv:2506.17889v1, first posted 2025-06-22; current version inspected.
2. S. J. Kim, R. Stees, and L. Taalman, *Sequences of Spiral Knot Determinants*, Journal of Integer Sequences 19 (2016), Article 16.1.4.
