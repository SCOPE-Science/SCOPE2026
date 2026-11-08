# No quasipolynomial period collapse for composite quotients of consecutive-generator numerical semigroups

## Finding
For every **composite** integer \(p\ge4\), define the numerical semigroup quotient
\[
S_{a,p}=\{n\in\mathbb Z_{\ge0}:pn\in\langle a,a+1\rangle\},\qquad a>p,
\]
and let \(G_p(a)\) denote its Frobenius number, the greatest integer not in \(S_{a,p}\). The least eventual quasipolynomial period of the function \(a\mapsto G_p(a)\) is **exactly \(p\)**. Here an eventual quasipolynomial period \(q\ge1\) means that for each residue modulo \(q\) a polynomial over \(\mathbb C\) agrees with \(G_p(a)\) at all sufficiently large positive integers in that residue. In particular, no smaller (or nondividing) period can replace \(p\).

The existence of period dividing \(p\) is a published result of Feihu Liu. The new result is the absence of period collapse for *every composite* \(p\); the prime-modulus case follows already from Liu's prime-branch result and is not asserted as new.

## Assumptions and scope
Throughout, \(p\ge4\) is composite and \(a>p\) is an integer. The generated monoid \(\langle a,a+1\rangle\) consists of nonnegative integral combinations of its generators. The Frobenius number exists since adjacent generators are coprime. The word period always refers to quasipolynomial branches, not to ordinary periodicity of \(G_p\).

Write \([z]_p\) for the unique integer in \(\{0,\ldots,p-1\}\) congruent to \(z\pmod p\). For \(r\in\{0,\ldots,p-1\}\), define
\[
\delta_{p,r}(i)=[r^2-r-1-ir]_p,\qquad
I_p(r)=\min\{i\in\{0,\ldots,p-1\}:\delta_{p,r}(i)\le i\},
\]
\[
J_p(r)=\delta_{p,r}(I_p(r)).
\]
The minimum exists since \(i=p-1\) is eligible. Liu's Theorem 5.3/Corollary 5.5 establishes, for all \(a>p\) with \(a\equiv r\pmod p\), the exact polynomial branch
\[
G_p(a)=P_{p,r}(a),\qquad
P_{p,r}(X)=\frac{X^2-(I_p(r)+1)X-(J_p(r)+1)}p.
\]
This published identity is used as an independently checked premise, not claimed as new.

## Proof
We first show that the branch for residue zero differs from the branch at *every proper divisor* of \(p\).

**Zero branch.** For \(r=0\), one has \(\delta_{p,0}(i)=p-1\) for every \(i\). Consequently \(I_p(0)=J_p(0)=p-1\), and
\[
P_{p,0}(X)=\frac{X^2-pX-p}{p}.
\]

**Divisor branches.** Let \(q\) be a proper positive divisor of \(p\). For \(q=1\), \(\delta_{p,1}(i)=p-1-i\), and hence \(I_p(1)=\lceil(p-1)/2\rceil\le p-2\) because \(p\ge4\). Therefore the coefficient of \(X\) in \(P_{p,1}\) differs from that in \(P_{p,0}\).

For \(2\le q<p\), set \(t=p/q\ge2\). As \(i\) runs through \(0,\ldots,t-1\), the residues
\[
\delta_{p,q}(i)=[q^2-q-1-iq]_p
\]
run through the \(t\) integers \(q-1,2q-1,\ldots,p-1\), in some order. Choose \(i_0\in\{0,\ldots,t-1\}\) with \(\delta_{p,q}(i_0)=q-1\). Because \(\delta_{p,q}(i+t)=\delta_{p,q}(i)\), the smallest \(i\ge q-1\) congruent to \(i_0\pmod t\) satisfies
\[
q-1\le i\le q+t-2\le qt-2=p-2,
\]
where the second inequality uses \((q-1)(t-1)\ge1\). This \(i\) is an eligible index since \(\delta_{p,q}(i)=q-1\le i\). Thus
\[
I_p(q)\le p-2<I_p(0),
\]
so the linear coefficients of \(P_{p,q}\) and \(P_{p,0}\) differ.

**No other period.** Suppose that a positive integer \(s\) were an eventual quasipolynomial period. Put \(g=\gcd(s,p)\). Any residue class modulo \(p\) and any residue class modulo \(s\) that agree modulo \(g\) have an infinite intersection. On that intersection, both corresponding polynomial branches equal \(G_p(a)\) for infinitely many arbitrarily large \(a\), and therefore they are identical polynomials. By comparing the residue-zero class modulo \(s\) with the residue-zero and residue-\(g\) classes modulo \(p\), we obtain \(P_{p,0}=P_{p,g}\). If \(g<p\), then \(g\) is a proper positive divisor of \(p\), contradicting the preceding divisor-branch argument. Therefore \(g=p\), or equivalently \(p\mid s\). Since Liu's formula supplies period \(p\), its least eventual quasipolynomial period is exactly \(p\). \(\square\)

## Verification
The accompanying `verify.py` performs two independently coded checks. First, for every modulus \(2\le p\le60\) and every proper divisor \(q\) it computes the residue branches and checks \((I_p(0),J_p(0))\ne(I_p(q),J_p(q))\). Second, for an independently enumerated range of pairs \((p,a)\), it compares Liu's branch formula with the direct largest gap detected from the representation criterion: \(pn=aQ+R\) with \(0\le R<a\) lies in \(\langle a,a+1\rangle\) exactly when \(R\le Q\). It searches only through the classical Sylvester bound \((a^2-a-1)/p\). These are finite cross-checks; the proof above establishes the theorem for every composite modulus.

Run: `python3 verify.py` (standard-library Python 3; no downloads).

## Relationship to prior work
Liu (2026, arXiv:2607.23076) proves the full residue-branch formula and that the quasipolynomial has period **dividing** \(p\). Definition 5.4 expressly warns that the actual minimal period *may* be smaller. His Section 5.2 establishes distinct-branch lower bounds specifically for **prime** moduli; these imply the prime case and are not part of the novel claim here. The present short divisor-cycle argument settles the previously undetermined least period for **every composite** modulus. Liu's April 2026 study of other quotient classes and earlier genus results treat related invariants but do not supply this precise minimum-period assertion in the material inspected.

## Limitations
This is a theorem only for quotients of consecutive-generator semigroups and only for fixed composite \(p\); it does not determine least periods for general coprime generator pairs or higher-generator quotients. The proof depends on Liu's published branch formula. Mathematical literature searches and relevant full-text comparisons did not reveal a stronger covering theorem, but historical priority remains provisional, especially for older unindexed semigroup literature. Independent audit has not been performed.

## References
1. Feihu Liu, *On the Frobenius Number of Quotients of Numerical Semigroups* (2026), arXiv:2607.23076, especially Theorem 5.3, Corollary 5.5, Definition 5.4 and Section 5.2. https://arxiv.org/abs/2607.23076
2. Feihu Liu, *The Frobenius problem for a class of quotients of numerical semigroups* (2026), arXiv:2604.26415. https://arxiv.org/abs/2604.26415
3. Adeniran et al., *On the genus of a quotient of a numerical semigroup* (2018), arXiv:1809.09360. https://arxiv.org/abs/1809.09360
