# Characteristic-seven Humbert curves: a missing \(7\)-rank and exact finite-field strata

## Finding

**Theorem.** Let \(k\) be an algebraically closed field of characteristic \(7\), and let \(C\) be a smooth genus-five generalized Fermat curve of type \((2,4)\) with its specified \((\mathbb Z/2\mathbb Z)^4\)-cover of \(\mathbb P^1_k\). For its five distinct branch points \(B\), let \(s(B)\) count four-point subsets whose cross ratio is harmonic. Then
\[
s(B)\in\{0,1,3\},\quad f(J(C))=5-s(B),\quad a(J(C))=s(B).
\]
Its Newton slopes, with multiplicities, are
\[
0^{\,5-s(B)},\quad (1/2)^{\,2s(B)},\quad 1^{\,5-s(B)}.
\]
All three cases occur. In particular, the Jacobian \(7\)-rank spectrum is \(\{2,4,5\}\); rank \(3\) does not occur. Rank \(2\) occurs if and only if \(B\) is projectively equivalent to a five-element subset of \(\mathbb P^1(\mathbb F_7)\). Those five-point subsets form one \(\mathrm{PGL}_2(\mathbb F_7)\)-orbit, hence one geometric projective equivalence class.

**Exact marked counts.** Normalize three ordered branch points to \(\infty,0,1\), and write the other two in order as \((a,b)\). For \(q=7^n\), \(n\ge1\), and
\[
U(\mathbb F_q)=\{(a,b):a,b\in\mathbb F_q\setminus\{0,1\},\ a\ne b\},
\]
the exact numbers of marked pairs according to Jacobian \(7\)-rank are
\[
N_2(q)=20,\qquad N_4(q)=15(q-7),\qquad N_5(q)=(q-7)(q-13).
\]
These are counts of ordered marked coefficient pairs, not isomorphism classes.

## Assumptions and scope

The generalized Fermat model can be written, for any \((a,b)\in U(k)\), as the smooth complete intersection in \(\mathbb P^4_k\)
\[
\begin{aligned}
X_1^2+X_2^2+X_3^2&=0,\\
aX_1^2+X_2^2+X_4^2&=0,\\
bX_1^2+X_2^2+X_5^2&=0.
\end{aligned}
\]
The quotient coordinate \(t=-X_2^2/X_1^2\) exhibits branch values \(\infty,0,1,a,b\). The distinctness hypotheses ensure tame, smooth covers because \(2\) is invertible in characteristic \(7\). By Riemann--Hurwitz, the degree-sixteen cover with five branch indices \(2\) has \(2g-2=-32+5\cdot8=8\), thus \(g=5\). Equivalently, the three-quadric complete intersection has canonical bundle \(\mathcal O_C(1)\) and degree eight.

A four-point set is called **harmonic** if any (equivalently every suitably reordered) cross ratio belongs to \(\{-1,2,1/2\}\). These values are distinct in characteristic \(7\); here they are exactly the elements \(\{6,2,4\}\) of the prime field. We use \(f\) for the rank of the geometric \(7\)-torsion group and \(a\) for \(\dim_k\operatorname{Hom}(\alpha_7,J(C)[7])\).

## Proof

**(1) Five elliptic quotients and prime-to-seven isogeny.** Write \(G=(\mathbb Z/2\mathbb Z)^4\), with the five local inertia involutions summing to zero in \(G\). A nontrivial character of \(G\) is ramified at an even-sized subset of \(B\). The ten characters ramified at two points give rational quotients; the five characters ramified at four points give degree-two covers \(E_i\to\mathbb P^1\) with four simple branch points, hence genus-one curves. Their maps \(\pi_i:C\to E_i\) have degree eight.

Consider \(\Psi:\prod_i J(E_i)\to J(C)\) given by the sum of the pullbacks, and \(\Phi:J(C)\to\prod_i J(E_i)\) given by the product of norm/pushforward maps. Character orthogonality gives \(\pi_{i*}\pi_j^*=0\) for \(i\ne j\), whereas \(\pi_{i*}\pi_i^*=[8]\). Consequently
\[
\Phi\Psi=[8]_{\prod_i J(E_i)}.
\]
Since source and target of \(\Psi\) have dimension five, it is an isogeny, and its kernel is contained in the eight-torsion. Thus its degree is a power of two and, in characteristic seven, it induces an isomorphism of \(7\)-divisible groups and of \(7\)-torsion group schemes. The \(7\)-rank, \(a\)-number, and Newton slopes therefore decompose as the sums/unions of those of the five elliptic factors.

**(2) Hasse invariant.** After a fractional-linear change of variable, any four-point branch set yields a Legendre elliptic curve \(E_\lambda:y^2=x(x-1)(x-\lambda)\). In characteristic seven its Hasse polynomial, up to an irrelevant nonzero factor, is
\[
H_7(\lambda)=\sum_{j=0}^3\binom3j^2\lambda^j
=\lambda^3+2\lambda^2+2\lambda+1
=(\lambda+1)(\lambda-2)(\lambda-4).
\]
Hence the elliptic quotient is supersingular exactly when its four branch points are harmonic. A supersingular elliptic factor contributes \(7\)-rank zero, \(a\)-number one and two slopes \(1/2\); an ordinary factor contributes rank one, \(a\)-number zero, and slopes \(0,1\). For \(s(B)\) harmonic four-subsets, the asserted Jacobian formulas follow.

**(3) No two-only phenomenon.** Any two distinct four-subsets of a five-set share exactly three points. If both are harmonic, apply a projectivity over \(k\) carrying their common three points to \(\infty,0,1\). The possible fourth points of a harmonic quartet containing these three are precisely \(\{-1,2,1/2\}\subset\mathbb F_7\). Thus both remaining points lie in \(\mathbb F_7\), so all five normalized points lie in \(\mathbb P^1(\mathbb F_7)\).

The group \(\mathrm{PGL}_2(\mathbb F_7)\) is sharply triply transitive on the eight points of \(\mathbb P^1(\mathbb F_7)\). Complementation identifies its action on five-subsets with its transitive action on three-subsets. It is therefore enough to inspect \(B_0=\{\infty,0,1,2,3\}\), whose harmonic four-subsets are exactly
\[
\{\infty,0,1,2\},\quad\{\infty,1,2,3\},\quad\{0,1,2,3\}.
\]
Thus a five-point set has either zero, one, or three harmonic four-subsets, never two, four or five, and the three-harmonic locus is a single geometric projective orbit.

**(4) All-extension counts.** The marked chart has \((q-2)(q-3)\) ordered pairs. By step (3), precisely the \((7-2)(7-3)=20\) pairs with \(a,b\in\mathbb F_7\setminus\{0,1\}\) distinct give \(s=3\). For any one fixed four-subset, e.g. \(\{\infty,0,1,a\}\), there are three harmonic choices \(a\in\{2,4,6\}\), and independently \(q-3\) valid choices of \(b\). Therefore that four-subset is harmonic for \(3(q-3)\) ordered pairs. Relabeling the five marked branch points and uniquely renormalizing three of them is a bijection of \(U(\mathbb F_q)\), so the same count holds for each of the five possible four-subsets.

Counting harmonic incidences two ways gives
\[
15(q-3)=N_{s=1}+3N_{s=3}=N_{s=1}+60.
\]
Therefore \(N_{s=1}=15(q-7)\), while subtracting from the total yields
\[
N_{s=0}=(q-2)(q-3)-15(q-7)-20=(q-7)(q-13).
\]
For \(q=49\), all three quantities are positive, establishing occurrence. An explicit field witness uses \(u^2=-1\) in \(\mathbb F_{49}\): parameters \((a,b)=(2,3)\), \((2,u)\), and \((u,3u)\) yield \(s=3,1,0\), respectively.

## Verification

The companion script `check.py` performs exact arithmetic with \(\mathbb F_{49}=\mathbb F_7[u]/(u^2+1)\). It independently evaluates every four-subset cross ratio and the Hasse polynomial, then enumerates all ordered marked pairs for \(q=7\) and \(q=49\). Its recorded output for the \(s=3,1,0\) strata is respectively \((20,0,0)\) over \(\mathbb F_7\) and \((20,630,1512)\) over \(\mathbb F_{49}\). These finite checks do not substitute for steps (1)--(4) of the general proof.

To replay: execute `python3 check.py` with Python 3; no third-party dependencies are required.

## Relationship to prior work

Yamauchi (2008) studies split Jacobians of genus-five families over number fields. Carvacho--Hidalgo--Quispe (arXiv:1507.02903, Section 5.1) explicitly describe the five elliptic quotients of generalized Fermat curves of type \((2,4)\) and their Jacobian isogeny over the complex numbers. That structural decomposition is not presented here as new. The present proof establishes a degree-prime-to-seven realization and then adds the characteristic-seven **compatibility constraint among supersingular factors**, the missing-rank phenomenon, the geometric minimum-rank orbit, the Newton polygons and the exact all-extension marked counts.

Hidalgo--Kontogeorgis--Leyton-Álvarez--Paramantzoglou (arXiv:1409.3063) provide positive-characteristic generalized Fermat models. Hidalgo (arXiv:1710.01349, Section 5.2) studies characteristic-three Cartier arithmetic of classical Humbert curves, not this characteristic-seven classification. Later Humbert--Edge work treating type five concerns genus-seventeen curves, not the genus-five type-four family.

## Limitations

The theorem concerns **smooth, tame genus-five Humbert covers in characteristic seven with their specified branch presentation**, not singular boundary fibres or other characteristics. The finite-field counts are for ordered marked coefficient pairs: no division by projective automorphism groups is made. The geometric uniqueness statement refers to projective branch configurations. The oldest potentially relevant split-Jacobian paper was available only at abstract level; historical redundancy with specialized projective harmonic geometry remains possible. Independent mathematical validation remains outstanding.

## References

1. T. Yamauchi, *On Curves with Split Jacobians*, Communications in Algebra **36** (2008), 1419--1425, DOI:10.1080/00927870701866622 (published online 2008-06-20).
2. R. A. Hidalgo, A. Kontogeorgis, M. Leyton-Álvarez, P. Paramantzoglou, *Automorphisms of the Generalized Fermat curves*, arXiv:1409.3063 (first version 2014-09-10).
3. M. Carvacho, R. A. Hidalgo, S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903 (first version 2015-07-10), especially Section 5.1.
4. R. A. Hidalgo, *Holomorphic differentials of Generalized Fermat curves*, arXiv:1710.01349 (first version 2017-10-03), especially Section 5.2.
5. A. Castorena, J. B. Frías-Medina, *Geometric aspects on Humbert-Edge curves of type 5, Kummer surfaces and hyperelliptic curves of genus 2*, arXiv:2106.00813 (2021), a neighboring but different genus-seventeen family.
