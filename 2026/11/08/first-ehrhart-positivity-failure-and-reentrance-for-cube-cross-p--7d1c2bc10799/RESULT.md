# First Ehrhart-positivity failure and reentrance for cube–cross-polytope lattice joins

## Finding
For integers \(p,q\ge1\), let \(U_p=[0,1]^p\), let \(X_q=\operatorname{conv}\{\pm e_1,\ldots,\pm e_q\}\), and form the canonical lattice join
\[
J_{p,q}=\operatorname{conv}\bigl((U_p,0_q,0)\cup(0_p,X_q,1)\bigr)\subset\mathbb R^{p+q+1}.
\]
Write \(L_{p,q}(t)=\lvert tJ_{p,q}\cap\mathbb Z^{p+q+1}\rvert\), an Ehrhart polynomial of degree \(d=p+q+1\). Ehrhart-positive means that every coefficient of \(L_{p,q}(t)\) in the ordinary monomial basis is strictly positive.

**Sharp first-failure classification.** Every \(J_{p,q}\) of dimension \(d\le17\) is Ehrhart-positive. At dimension \(d=18\), the only non-Ehrhart-positive members are \(J_{14,3}\) and \(J_{16,1}\). Each has exactly one negative coefficient, namely
\[
[t]L_{14,3}(t)=-\frac{10397}{510},\qquad
[t]L_{16,1}(t)=-\frac{897}{170}.
\]
All other coefficients in these two polynomials are strictly positive; all coefficients of every other \(J_{p,q}\) with \(d=18\) are strictly positive. In particular the first failure of Ehrhart positivity **within this family** occurs in dimension \(18\), not the first failure among all lattice polytopes.

**Reentrant positivity at fixed cube dimension.** For \(p=14\), positivity holds for \(q=2\), fails for \(q=3,4\), and holds again for \(q=5\). In the two latter cases the linear coefficients are respectively
\[
[t]L_{14,4}(t)=-\frac{76729}{3990},\qquad
[t]L_{14,5}(t)=\frac{618397}{67830}>0.
\]
Thus increasing the cross-polytope dimension does not monotonically preserve either positivity or failure. No claim is made about arbitrary larger \(p,q\).

## Assumptions and scope
Both factors are standard lattice polytopes in standard integer lattices. The join is embedded in distinct coordinate blocks at integer heights zero and one. All dimensions and quantifiers are as above; no unimodularity, smoothness, or asymptotic assumption is used. The result concerns **ordinary Ehrhart coefficients**, not positivity of the always-nonnegative \(h^*\)-vector.

## Proof
**1. Exact counts and numerator.** At integral join height \(s\), with \(0\le s\le t\), the lattice-point count factors as \((t-s+1)^p\lvert sX_q\cap\mathbb Z^q\rvert\). A lattice point of the cross-polytope dilation has \(j\) nonzero coordinates chosen in \(\binom qj\) ways, signs chosen in \(2^j\) ways, and positive coordinate magnitudes with sum at most \(s\) counted by \(\binom sj\). Therefore
\[
L_{p,q}(t)=\sum_{s=0}^{t}(t-s+1)^p
\sum_{j=0}^{\min(q,s)}2^j\binom qj\binom sj.\tag{1}
\]
The Ehrhart generating series of the unit cube is \(A_p(z)/(1-z)^{p+1}\), with Eulerian numerator \(A_p(z)=\sum_{k=0}^{p-1}E_{p,k}z^k\), and that of the cross-polytope is \((1+z)^q/(1-z)^{q+1}\). Taking the convolution in (1) gives
\[
\sum_{t\ge0}L_{p,q}(t)z^t
=\frac{A_p(z)(1+z)^q}{(1-z)^{p+q+2}}.\tag{2}
\]
In particular, with \(d=p+q+1\) and \(H_i=[z^i]A_p(z)(1+z)^q\),
\[
L_{p,q}(t)=\sum_{i=0}^{p+q-1}H_i\binom{t+d-i}{d}.\tag{3}
\]

**2. Finite exhaustive sign certificate.** Put \(B_k(p,q)=d!\,[t^k]L_{p,q}(t)\). By (3) these are explicitly integral:
\[
B_k(p,q)=\sum_{i=0}^{p+q-1} H_i\,[t^k]\prod_{r=1}^d(t+r-i).\tag{4}
\]
Use the recurrence \(E_{1,0}=1\), with missing indices zero, and
\[
E_{p,k}=(k+1)E_{p-1,k}+(p-k)E_{p-1,k-1}\quad(p\ge2).
\]
This specifies every input to (4) as an integer. The attached complete standard-library program `verify.py` executes the following exhaustive terminating procedure: for each integer \(m=2,\ldots,17\), for every \(p=1,\ldots,m-1\) set \(q=m-p\), construct all \(d+1\) integers \(B_k(p,q)\) using (4), and compare each with zero. For \(m\le16\), all are positive (120 parameter pairs). For \(m=17\), the only negative entries occur at \((p,q,k)=(14,3,1)\) and \((16,1,1)\); there are no zeros. Thus (4) and an exhaustive bounded arithmetic certificate establish the entire first-failure classification. This is a proof for the finite set specified, not an extrapolation to arbitrary dimensions.

**3. Reentrance.** Apply the same exact formula (4) to \(p=14\) and \(q\in\{2,3,4,5\}\). The entire coefficient vectors are positive for \(q=2,5\), and for \(q=3,4\) all entries except the linear term are positive. Exact integer division by \(d!\) gives the four displayed rational linear coefficients. The verifier asserts these equalities in integers, so no floating-point sign determination enters.

## Verification
Execute `python3 verify.py` using Python 3 standard library only. The test enumerates **1,982** exact integer coefficient signs (including all dimensions through 18 and the four fixed-cube cases) and separately checks **2,122** identities between the polynomial and direct slice counts (1) at successive nonnegative integers and an additional larger integer for each pair. The check prints four `PASS` lines or raises an exception; the exact output on the verified program is:

```
PASS: 120 strictly positive pairs in total dimension <=17;
PASS: the only dimension-18 failures are (14,3) and (16,1);
PASS: reentrant positivity for p=14, q=2,3,4,5;
PASS: 1982 integer coefficient sign checks and 2122 direct-count identities
```

The two derivations (1) and (3) give independent numerical cross-checks. The universal numerator identities are proved algebraically; the finite classification relies on complete exact enumeration with the complete reproducible algorithm, not on random testing or an unbounded search.

## Relationship to prior work
Liu, Tao, and Xin's 2026 paper on lattice joins establishes nonpreservation of Ehrhart positivity and other structural properties but its accessible abstract does not specify this exact cube–cross-polytope first-failure or reentrant classification. The full text was not accessible for comparison: this is a priority risk, not proof of novelty. Liu's 2026 survey of operations provides general join-counting frameworks, also without an accessible full-text priority comparison. Liu and Tsuchiya's 2018 work studies order-polytopal ordinal sums, with Eulerian numerator products \(A_m(z)A_n(z)\). Those give related Ehrhart-equivalent cases when \(q=1\), but their displayed exact examples concern substantially different parameter ranges. The present complete two-parameter finite boundary, two exceptional pairs, and reentrant \(q\)-profile are not stated in the inspected material. The scalar factor \((1+z)^q\) also differs from a generic Eulerian \(A_n(z)\). No uniqueness beyond the searched sources is claimed.

## Limitations
The classification ends at ambient dimension 18, except for the explicitly listed \(p=14\) reentrant cases. A finite proof makes no assertion about eventual sign patterns. The motivating 2026 primary paper could not be inspected beyond title, bibliographic data, and abstract, leaving a residual potential-coverage risk. Searches do not prove global historical novelty. No independent mathematical audit or formal proof-assistant certificate has been performed. The certificate is a finite exhaustive integer algorithm whose logic is included in full.

## References
1. Feihu Liu, Sihao Tao, and Guoce Xin, *Ehrhart Theory of the Join of Two Lattice Polytopes*, arXiv:2606.18794, first submitted June 17, 2026, https://arxiv.org/abs/2606.18794.
2. Feihu Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338, first submitted October 5, 2026, https://arxiv.org/abs/2610.06338.
3. Fu Liu and Akiyoshi Tsuchiya, *Stanley's non-Ehrhart-positive order polytopes*, arXiv:1806.08403, submitted June 21, 2018; especially Section 3, Lemma 3.1, Example 3.2, and Table 1; https://arxiv.org/abs/1806.08403.
4. Luis Ferroni, Alejandro H. Morales, and Greta Panova, *Skew shapes, Ehrhart positivity, and beyond*, Proceedings of the London Mathematical Society (2026), https://doi.org/10.1112/plms.70204.
