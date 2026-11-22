# Two chamber counts detect Frobenius on one-nodal cubic resolutions

## Finding

Let \(q\) be an odd prime power. Let \(Z\) be a reduced Frobenius-stable set of six geometric points on a smooth conic in \(\mathbb P^2_{\mathbb F_q}\), and let \(X\) be its blow-up. The anticanonical model of \(X\) is a geometrically one-nodal cubic surface, and the strict transform \(Q\) of the conic is the unique \((-2)\)-curve.

Write \(c(X)\) for the number of geometric Zariski chambers in the big cone of \(X\) preserved by arithmetic Frobenius. Write \(r(X)\) for the number of these preserved chambers whose Zariski-negative support contains \(Q\). The nef chamber is included in \(c(X)\). Every preserved chamber is represented by a big divisor defined over \(\mathbb F_q\), so the counts describe genuine ground-field Zariski-support possibilities, not just abstract permutation-fixed objects.

**The pair \((c(X),r(X))\) determines the exact Frobenius cycle partition \(\lambda\) of the six blown-up points.** The complete answer is:

| \(\lambda\) | \(c(X)\) | \(r(X)\) |
|:--|--:|--:|
| \((1,1,1,1,1,1)\) | 1898 | 648 |
| \((2,1,1,1,1)\) | 468 | 160 |
| \((2,2,1,1)\) | 118 | 36 |
| \((2,2,2)\) | 24 | 4 |
| \((3,1,1,1)\) | 113 | 42 |
| \((3,2,1)\) | 33 | 10 |
| \((3,3)\) | 11 | 3 |
| \((4,1,1)\) | 26 | 10 |
| \((4,2)\) | 8 | 2 |
| \((5,1)\) | 8 | 3 |
| \((6)\) | 3 | 1 |

The second coordinate is **essential**: partitions \((4,2)\) and \((5,1)\) both give eight rationally realizable chamber supports, but the numbers containing \(Q\) are two and three. Their full chamber orbit patterns are also different: \((4,2)\) gives \(1^8 2^{55}4^{445}\), whereas \((5,1)\) gives \(1^8 5^{378}\). These are cycle notations for finite permutation sets, not exponentiation identities.

All eleven types are realized over every odd finite field with \(q\ge5\). Over \(\mathbb F_3\), precisely the completely split partition \((1,1,1,1,1,1)\) is unavailable in this conic blow-up family, and the other ten are realized.

## Assumptions and scope

The base field is finite of odd characteristic; no assumption is made that the six geometric points themselves are individually rational. A Frobenius-stable set of six distinct geometric points is a reduced finite étale subscheme. The conic is smooth and defined over the base field. Every triple of distinct geometric conic points is noncollinear.

The geometric chamber set refers to the Zariski decomposition of big real divisor classes on \(X_{\overline{\mathbb F}_q}\), and a chamber is indexed by the reduced support of its negative part; the empty support is the nef chamber. The unique conic \((-2)\)-curve \(Q\) is individually Frobenius-fixed. The names \(c(X)\) and \(r(X)\) denote counts of **Frobenius-stable supports**, not the number of rational points in any continuous divisor cone.

## Proof

**1. Exhaustion of geometric negative curves.** In the Picard basis consisting of the line pullback \(H\) and six exceptional classes \(E_i\), write
\[
 L_{ij}=H-E_i-E_j\quad(1\le i<j\le6),\qquad Q=2H-\sum_{i=1}^6E_i.
\]
These are exactly the twenty-two negative curves: the six \(E_i\), the fifteen secant transforms \(L_{ij}\), and the conic transform \(Q\). Their self-intersections are \((-1),(-1),(-2)\), respectively. To see there are no others, if an irreducible nonexceptional curve other than \(Q\) is the transform of a plane curve of degree \(d\), Bézout with the conic gives \(\sum m_i\le2d\), hence \((-K_X)\cdot C=3d-\sum m_i\ge d\). Adjunction forces a negative curve of positive anticanonical degree to be a \((-1)\)-curve of anticanonical degree one; consequently \(d=1\) and it is a secant through exactly two of the marked points. The sole anticanonically trivial negative curve is \(Q\).

**2. Exact support criterion.** For distinct curves,
\[
E_iE_j=0,\quad E_iL_{jk}=\mathbf1_{i\in\{j,k\}},\quad
L_{ij}L_{kl}=\mathbf1_{\{i,j\}\cap\{k,l\}=\varnothing},\quad
QE_i=1,\quad QL_{ij}=0.
\]
All selected \((-1)\)-curves must be pairwise disjoint: any intersecting pair gives a non-negative-definite two-by-two principal minor. Conversely, disjoint \((-1)\)-curves have negative diagonal intersection form. If \(Q\) is also selected, the Schur complement against the \((-1)\)-block is \(-2+s\), where \(s\) is the number of exceptional curves \(E_i\) included; it is strictly negative exactly when \(s\le1\). Thus a set of negative curves is negative definite if and only if the selected \((-1)\)-curves are mutually disjoint and, when \(Q\) occurs, at most one exceptional curve occurs.

By Bauer–Funke–Neumann's Zariski-chamber correspondence (Proposition 1.1), **every** negative-definite set of irreducible negative curves occurs as the negative support of a big divisor. This correspondence is natural under field automorphisms, so arithmetic Frobenius fixes a chamber if and only if it preserves its negative-curve support.

**3. Frobenius orbit formula and exhaustive eleven-case evaluation.** Frobenius permutes the six \(E_i\) by a permutation \(\sigma\in S_6\), the fifteen \(L_{ij}\) by the induced action on unordered pairs, and fixes \(Q\). For each of the eleven cycle partitions \(\lambda\vdash6\), let \(\mathscr O_\lambda\) be the orbits of this induced action on the twenty-two negative curves. Every stable support is a union of whole orbits. Enumerate all subsets \(B\subseteq\mathscr O_\lambda\), retaining precisely those whose union satisfies the criterion of Step 2:
\[
 c_\lambda=\sum_{B\subseteq\mathscr O_\lambda}\mathbf1_{\operatorname{admissible}(\cup B)},\qquad
 r_\lambda=\sum_{B\subseteq\mathscr O_\lambda}\mathbf1_{Q\in\cup B}\,\mathbf1_{\operatorname{admissible}(\cup B)}.
\]
This is a finite **exhaustive** formula over at most twenty-two curve orbits, not sampling. `verify_arithmetic_chambers.py` evaluates it using orbit-union recursion and separately enumerates all negative-definite supports before checking Frobenius invariance. A third algorithm, `verify_all_permutations.py`, uses the star/triangle edge-family classification and checks every one of the 720 permutations, not just eleven representatives. All three agree, including the full support-size refinements recorded in `chamber_table.json`. In the identity type they give \(1898\) supports and \(648\) containing \(Q\), matching the independently established geometric chamber spectrum. The eleven ordered pairs in the displayed table are distinct, but the first coordinates collide only for \((4,2)\) and \((5,1)\).

**4. Rational realizability and sharp field bounds.** Let \(S\) be any Frobenius-invariant admissible reduced support. Since its components are permuted, the reduced divisor \(D_S=\sum_{C\in S}C\) descends to \(\mathbb F_q\). Choose a ground-field ample divisor \(A\). For sufficiently large positive integer \(k\), the big divisor \(A+kD_S\) has Zariski-negative support exactly \(S\), by the constructive half of Proposition 1.1. Conversely a ground-field divisor's negative support is stable by uniqueness of the Zariski decomposition. Thus \(c_\lambda\) and \(r_\lambda\) count exactly the ground-field-realizable supports.

Every smooth conic over a finite field is isomorphic to \(\mathbb P^1\); the number of closed points of degree \(d\) on it is \(\frac1d\sum_{e\mid d}\mu(e)q^{d/e}\). For every odd \(q\ge5\), these numbers supply all combinations of cycles of total degree six, including six distinct rational points. Over \(q=3\), there are only four rational conic points, ruling out six singleton cycles, but enough degree-two through degree-six closed points to realize every other partition. All chosen points are distinct, so the construction always yields the stated geometric surface.

## Verification

Run from the extracted standalone files using ordinary Python 3:

```
python3 verify_picard.py
python3 verify_arithmetic_chambers.py
python3 verify_all_permutations.py
```

`verify_picard.py` independently checks the entire twenty-two-curve intersection matrix in the integral Picard lattice. `verify_arithmetic_chambers.py` uses two different complete combinatorial algorithms: (i) recursively enumerate all pairwise-disjoint \((-1)\) supports and their admissible root extensions, then test a representative Frobenius permutation, and (ii) independently enumerate unions of full Frobenius orbits subject to the geometric intersection restrictions. The two agree in all eleven types. `verify_all_permutations.py` uses a separately generated star/triangle family classification and verifies all 720 permutations against the table, including conjugacy invariance. The separate enumeration covers exactly all \(1898\) supports, including exactly \(648\) root-containing supports. There is no probabilistic enumeration or timeout treated as impossibility.

## Relationship to prior work

Blache–Hallouin (2023, §5.2, Appendix A) describe all eleven arithmetic \(S_6\) types of degree-three weak del Pezzo surfaces of geometric type \(A_1\), including constructions using six points on a conic; they **do not compute Frobenius-fixed Zariski-chamber counts**. Bauer–Funke–Neumann (2009, Proposition 1.1) give the general support/negative-definiteness correspondence, and their smooth cubic chamber total concerns a different geometric type. A published geometric computation, *Zariski-chamber spectrum of the one-nodal cubic's minimal resolution* (2026), already gives the \(1898\)-support polynomial, \(648\) root-containing supports, and the star/triangle combinatorial classification, **all of which are credited as prior work**. It explicitly does not treat arithmetic over nonclosed fields. The new statement is the full eleven-case Frobenius-fixed two-count classification and the sharp one-versus-two numerical invariant distinction, not its input geometry or the known abstract arithmetic types. Related classifications of Galois actions on lines and other del Pezzo chamber sets do not imply this numerical table without the present calculation for these twenty-two curves.

## Limitations

The invariants determine the cycle partition of the chosen six-point marking, not an isomorphism class of cubic surfaces. They count distinct negative supports, not chamber volumes or rational points in divisor cones, and do not assert a corresponding invariant for other ADE singularity types. Earlier equivalent arithmetic support tables could affect historical priority; the available references and published result search did not reveal one, but that absence is not proof of uniqueness. Independent mathematical validation has not been performed.

## References

1. R. Blache and E. Hallouin, *Classification of singular del Pezzo surfaces over finite fields*, arXiv:2301.13582v1 (first public 2023-01-31), §§1, 5.2, Appendix A Table 8. https://arxiv.org/pdf/2301.13582
2. T. Bauer, M. Funke and S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958v1, Proposition 1.1 and §§1–3. https://arxiv.org/pdf/0912.0958
3. *Zariski-chamber spectrum of the one-nodal cubic's minimal resolution* (published 2026-11-08), RESULT.md, exact geometric support counts and criterion. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-zariski-chamber-spectrum-of-the-one-nodal-cubic-s-minimal-resolu--4b531d234d53/RESULT.md
