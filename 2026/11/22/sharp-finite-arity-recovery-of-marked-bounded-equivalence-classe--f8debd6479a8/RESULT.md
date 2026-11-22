# Sharp finite-arity recovery of marked bounded equivalence classes

## Finding
Fix an integer \(q\ge2\). Let \(M_q\) be a countably infinite equivalence structure in which every equivalence class has exactly \(q\) elements and there are infinitely many classes. For every finite, individually named parameter set \(A\), let \(t_r(A)\) count complete first-order types over \(A\) of ordered \(r\)-tuples of **pairwise distinct elements outside** \(A\), including the algebraic types arising from incompletely represented old classes. Define \(a_c(A)\), for \(1\le c\le q-1\), to be the number of equivalence classes that meet \(A\) and have exactly \(c\) elements remaining outside \(A\).

Writing \(E_c(z)=\sum_{j=0}^c z^j/j!\), the full type series is
\[
F_A(z):=\sum_{r\ge0}\frac{t_r(A)}{r!}z^r
=\exp\!\left(\sum_{j=1}^{q}\frac{z^j}{j!}\right)
\prod_{c=1}^{q-1}E_c(z)^{a_c(A)}.
\]
**Sharp reconstruction theorem.** For each fixed \(q\), the \(q-1\) numerical observations \(t_1(A),\ldots,t_{q-1}(A)\) uniquely determine the vector \((a_1(A),\ldots,a_{q-1}(A))\) even without knowing \(|A|\), and therefore determine every higher type count. No shorter initial segment suffices uniformly, even if the cardinality of the named base is provided: two \(2q\)-element named bases have equal counts through arity \(q-2\) and their counts at arity \(q-1\) differ by exactly \(q\). If \(|A|\) is known, the same observations also determine how many equivalence classes are fully contained in \(A\).

## Assumptions and scope
The language contains equality and one equivalence relation, without an imposed order or colours. The structure has **exactly** \(q\) members in every class, not merely an upper bound, and infinitely many classes. Every element of \(A\) is a separate named parameter. An \(r\)-tuple counted here has no repeated coordinate and no coordinate in \(A\); it may contain unnamed elements of finite classes already meeting \(A\). Empty bases and \(r=0\) are included, with \(t_0(A)=1\). The integer \(q\) is fixed and known when interpreting the sequence. All generating functions are formal power series over \(\mathbb Q\).

## Proof
**1. Complete orbit invariant.** Every finite partial isomorphism of \(M_q\) extends to an automorphism: finitely many classes can be permuted, each bijection between represented pieces can be extended to a bijection of their \(q\)-element classes, and infinitely many untouched classes remain. Thus finite tuples have the same complete first-order type over \(A\) if and only if they lie in the same orbit of the pointwise stabilizer of \(A\).

An injective tuple disjoint from \(A\) has exactly the following invariant: for each represented but nonfull class, which labelled tuple coordinates lie in that particular old class (at most its residual capacity \(c\)); and a set partition of all remaining coordinates into unrepresented, interchangeable new classes, every part of size at most \(q\). This invariant is sufficient by the preceding automorphism extension. Each old class with capacity \(c\) contributes \(E_c(z)\) to the labelled exponential generating function. New classes form an unordered set of nonempty labelled blocks of sizes \(1\) through \(q\), yielding the exponential factor by the exponential formula. This proves the displayed identity for every arity.

**2. Effective recovery.** Put \(G_q(z)=\sum_{j=1}^q z^j/j!\) and \(L_A(z)=\log F_A(z)-G_q(z)\). Then
\[
L_A(z)=\sum_{c=1}^{q-1}a_c(A)\log E_c(z),\qquad
[z]L_A(z)=N:=\sum_{c=1}^{q-1}a_c(A).
\]
For every \(c\ge1\), \(E_c(z)=e^z-z^{c+1}/(c+1)!+O(z^{c+2})\), so
\[
\log E_c(z)=z-\frac{z^{c+1}}{(c+1)!}+O(z^{c+2}).
\]
Consequently the coefficient of \(z^k\) in \(L_A\), for \(2\le k\le q-1\), involves only \(a_1,\ldots,a_{k-1}\), and its coefficient of the last unknown \(a_{k-1}\) is exactly \(-1/k!\). Starting with \(N=t_1(A)-1\), determine successively \(a_1\) from degree two, \(a_2\) from degree three, and so on to \(a_{q-2}\) from degree \(q-1\); then set \(a_{q-1}=N-\sum_{c=1}^{q-2}a_c\). For \(q=2\), this last equality simply gives \(a_1=t_1-1\). This is an exact triangular inverse, not a finite-sample inference. Coefficients of \(\log F_A\) up to degree \(q-1\) require only the given counts, because \(t_0=1\). Substitution into the generating function determines all counts.

If \(n=|A|\) is additionally known, the number \(a_0\) of fully represented old classes is
\[
a_0=\frac{n-\sum_{c=1}^{q-1}(q-c)a_c}{q},
\]
which is a nonnegative integer for genuine parameter sets. Without \(n\), \(a_0\) is entirely invisible to *all* the counts, since a full class has no available new members.

**3. Sharpness at fixed base cardinality.** Let \(A\) consist of one named element in each of \(q\) distinct classes, together with all \(q\) elements of a further class. Let \(B\) consist of two named elements in each of \(q\) distinct classes. Both bases have \(2q\) named elements. Their respective type series are
\[
F_A(z)=e^{G_q(z)}E_{q-1}(z)^q,\qquad
F_B(z)=e^{G_q(z)}E_{q-2}(z)^q,
\]
with \(E_0(z)=1\) when \(q=2\). Since \(E_{q-1}(z)-E_{q-2}(z)=z^{q-1}/(q-1)!\), the two series agree in degrees strictly less than \(q-1\), and their degree-\(q-1\) coefficients differ by \(q/(q-1)!\). Therefore
\[
t_r(A)=t_r(B)\quad(0\le r\le q-2),\qquad
t_{q-1}(A)-t_{q-1}(B)=q.
\]
This proves optimality for every \(q\ge2\), including the boundary \(q=2\).

## Verification
A standalone Python standard-library program independently enumerates all canonical ordered-tuple equivalence signatures by recursively placing labelled coordinates into old fixed classes (subject to capacities) or new unlabelled classes (subject to the bound \(q\)). It compares this direct enumeration with independently computed exact rational coefficients of the displayed generating series. It also implements the coefficientwise logarithmic inverse and checks recovery against the input profiles. Recorded execution: 2,018 direct orbit checks and 300 exact inverse checks for \(2\le q\le6\), plus sharp same-cardinality witnesses for every \(q\) in this range, all passed. These finite tests check the implementation and boundary arithmetic; the above orbit classification, triangular inversion, and witness argument prove the theorem for every finite \(q\) and arity.

For illustration at \(q=3\), the two six-element bases in Step 3 have type prefixes \((1,4,17)\) and \((1,4,14)\). At \(q=4\), the eight-element witness pair has prefixes \((1,5,26,141)\) and \((1,5,26,137)\).

## Relationship to prior work
The correspondence between complete types and automorphism-group tuple orbits, the imprimitive wreath-product construction, and the exponential formula for the **unmarked** labelled orbit profile are classical. Cameron's 2000 paper explicitly gives the wreath-product substitution law and treats point stabilizers (Sections 2.1, 4.2 and 4.3). Cameron's 1983 paper studies imprimitive orbit enumeration on **unordered** subsets. These are foundational counting tools, not claimed as new here. The distinct statement proved above is the **optimal, cardinality-free finite-arity reconstruction of all partial-block capacities from a pointwise-marked tuple spectrum**, including a uniform equal-base-size obstruction to every smaller arity bound. The 1983 article's official abstract, rather than its full text, was accessible; an earlier equivalent formulation cannot be categorically excluded.

## Limitations
The theorem does not reconstruct the individual names, the internal ordering of any class (none is given), or the number of fully named classes unless \(|A|\) is supplied. It is specific to a homogeneous disjoint union of uniformly \(q\)-element classes and to injective new-coordinate types; variable block sizes and expanded languages are not covered. Historical-priority comparisons remain incomplete because the full text of an older relevant imprimitive-group article was inaccessible.

## References
1. P. J. Cameron, *Orbits of Permutation Groups on Unordered Sets, III: Imprimitive Groups*, Journal of the London Mathematical Society, 27 (1983), 229–237, https://doi.org/10.1112/jlms/s2-27.2.229 (official abstract inspected; published 1 April 1983).
2. P. J. Cameron, *Sequences Realized by Oligomorphic Permutation Groups*, Journal of Integer Sequences 3 (2000), Article 00.1.5, https://cs.uwaterloo.ca/journals/JIS/VOL3/groups.html (full HTML; relevant Sections 2.1, 4.2, 4.3, 5.1–5.2 inspected).
