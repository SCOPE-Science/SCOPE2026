# Complete mixed degrees of two canonical strata on the quintic del Pezzo threefold

## Finding

Let \(X=V_5\subset\mathbb P^6_{\mathbb C}\) be the smooth quintic del Pezzo threefold, \(H=c_1(\mathcal O_X(1))\), \(V=H^0(X,\mathcal O_X(1))\), and \(G=\operatorname{Gr}(2,V)\). Denote the pullbacks to \(C=X\times G\) of \(H\) and of the Pluecker class \(\sigma_1=c_1(\mathcal S^\vee)\) by \(h\) and \(s\). Here \(\mathcal S\) is the tautological rank-two bundle on \(G\).

For \(p\in X\), set \(W_p=H^0(X,\mathcal I_p(1))\) and \(K_p=H^0(X,\mathcal I_p^2(1))\). Consider the determinantal incidence locus
\[
\Sigma=\{(p,L):L\subset W_p,\ \dim(L\cap K_p)\ge1\}\subset C
\]
and its rank-zero stratum \(Z=\operatorname{Gr}_X(2,K)\). The canonical scheme structures are the ones given by the jet-evaluation and rank-degeneracy maps. These are, respectively, the nine-dimensional intersection locus and its five-dimensional reduced singular locus in the degree-five moduli geometry of Fu [1].

**The complete mixed intersection sequences**, ordered by \(i=0,1,2,3\), are
\[
\boxed{\left(\int_\Sigma h^i s^{9-i}\right)_{i=0}^3=(504,448,210,45)},
\qquad
\boxed{\left(\int_Z h^i s^{5-i}\right)_{i=0}^3=(110,52,20,5)}.
\]
All terms with \(i>3\) vanish. In particular, the degrees of these two loci under the Segre embedding associated with \(\mathcal O_X(1)\boxtimes\mathcal O_G(1)\) are
\[
\boxed{\deg_{h+s}(\Sigma)=15876,\qquad\deg_{h+s}(Z)=620.}
\]

More intrinsically, put \(\sigma_{1,1}=c_2(\mathcal S^\vee)\) and \(\sigma_2=s^2-\sigma_{1,1}\). In the integral Chow ring of \(C\),
\[
\boxed{[\Sigma]=(\sigma_{1,1}+hs+h^2)(\sigma_2+hs+c_2(T_X)-h^2)}
\quad\text{in }A^4(C),
\]
and
\[
\boxed{[Z]=c_8\bigl(\mathcal S^\vee\otimes J^1\mathcal O_X(1)\bigr)}
\quad\text{in }A^8(C).
\]
Pullback symbols in these formulas are suppressed; the latter tensor product is formed over the two projections of \(C\).

## Assumptions and scope

The ground field is \(\mathbb C\), and \(X\) is the standard smooth Fano threefold with \(-K_X=2H\) and \(H^3=5\). We use the Grassmannian of **two-dimensional spaces of sections**, rather than its dual, and the Pluecker line bundle \(\det\mathcal S^\vee\). Fundamental cycles carry scheme-theoretic multiplicity. The expected codimensions are verified by the determinantal local description in [1, Section 7]: \(\operatorname{codim}_C\Sigma=4\), \(\operatorname{codim}_C Z=8\). All integrals mean degrees of zero-dimensional intersection products.

## Proof

**1. Chern data of \(X\).** Write \(B=\operatorname{Gr}(2,5)\) with Pluecker class \(H_B\) and Schubert class \(\tau_{1,1}\). The threefold \(X\) is the transverse intersection of three Pluecker hyperplanes in \(B\). The universal-bundle description \(T_B=\mathcal U^\vee\otimes\mathcal Q\), together with \(c(\mathcal Q)=c(\mathcal U)^{-1}\), gives
\[
c_1(T_B)=5H_B,\quad c_2(T_B)=11H_B^2+\tau_{1,1},\quad c_3(T_B)=15H_B^3.
\]
Dividing \(c(T_B)\) by \((1+H_B)^3\) yields
\[
c_1(T_X)=2H,\quad c_2(T_X)=2H^2+\tau_{1,1}|_X,\quad c_3(T_X)=2H^3-3H\tau_{1,1}|_X.
\]
The Schubert integrals \(\int_B H_B^6=5\) and \(\int_BH_B^4\tau_{1,1}=2\) imply
\[
\int_XH^3=5,\qquad\int_XHc_2(T_X)=12,\qquad\int_Xc_3(T_X)=4.
\]
These assertions may be checked by the two-root Grassmannian coefficient formula described below.

**2. The intersection cycle.** On \(Y=\operatorname{Gr}_X(2,W)\), the rank-two tautological bundle maps to \(W/K\simeq\Omega_X^1(1)\), of rank three. By [1, Proposition 7.1], its rank-at-most-one scheme \(\Sigma\) has the expected codimension two. The Thom--Porteous formula thus gives
\[
[\Sigma]_Y=c_2\bigl(\Omega_X^1(1)-\mathcal S\bigr).
\]
The regular embedding \(Y\hookrightarrow C\) is the zero locus of the rank-two bundle \(\mathcal S^\vee\otimes\mathcal O_X(1)\), hence contributes \(c_2=\sigma_{1,1}+hs+h^2\). Since
\[
c_1(\Omega_X^1(1))=H,\quad
c_2(\Omega_X^1(1))=c_2(T_X)-H^2,
\]
the claimed integral Chow-class expression for \([\Sigma]\) follows.

**3. The singular-stratum cycle.** The first-jet evaluation \(V\otimes\mathcal O_X\to J^1\mathcal O_X(1)\) is surjective, and \(K\) is its rank-three kernel. The zero locus of \(\mathcal S\to J^1\mathcal O_X(1)\) inside \(C\) is exactly \(Z\), regularly embedded in codimension eight. Therefore its class is the displayed top Chern class. The jet exact sequence and the numbers in Step 1 give
\[
c_1(J^1\mathcal O_X(1))=2H,\quad
c_2(J^1\mathcal O_X(1))=c_2(T_X),\quad
\int_Xc_3(J^1\mathcal O_X(1))=10.
\]

**4. Numerical evaluation.** In rational cohomology of \(X\), \(c_2(T_X)=\frac{12}{5}H^2\) and \(c_3(J^1\mathcal O_X(1))=2H^3\). Let \(\alpha,\beta\) be formal Chern roots of \(\mathcal S^\vee\). The classes in Steps 2--3 become
\[
[\Sigma]=(\alpha\beta+H(\alpha+\beta)+H^2)
(\alpha^2+\alpha\beta+\beta^2+H(\alpha+\beta)+\tfrac75H^2)
\]
and
\[
[Z]=\prod_{t\in\{\alpha,\beta\}}
(t^4+2Ht^3+\tfrac{12}{5}H^2t^2+2H^3t).
\]
For a symmetric polynomial \(f(\alpha,\beta)\) of degree ten, integration over \(G=\operatorname{Gr}(2,7)\) is the coefficient of \(\alpha^6\beta^5\) in \((\alpha-\beta)f\). Multiply the two classes by \(H^i(\alpha+\beta)^{9-i}\) and \(H^i(\alpha+\beta)^{5-i}\), respectively; keep the coefficient of \(H^3\) and multiply the Grassmannian coefficient by \(\int_XH^3=5\). Direct expansion gives the two four-entry sequences displayed in the Finding.

Finally expand \((h+s)^9\) on \(\Sigma\) and \((h+s)^5\) on \(Z\). The binomial sums are \(504+9\cdot448+36\cdot210+84\cdot45=15876\) and \(110+5\cdot52+10\cdot20+10\cdot5=620\), respectively.

**5. Independent pushforward check.** The incidence resolution \(\widetilde\Sigma\to\Sigma\) of [1, Section 7] is a \(\mathbb P^4\)-bundle over \(\mathbb P_X(K)\), and is birational. Successive projective-bundle pushforwards give the first sequence without Thom--Porteous. Likewise \(Z=\operatorname{Gr}_X(2,K)\) is a \(\mathbb P^2\)-bundle over \(X\); pushforward of the restricted Pluecker class gives the second sequence. The executable artifact implements both this calculation and the independent Grassmannian-root integration.

## Verification

Run `python3 verify.py` using standard-library Python 3. It recomputes the relevant Schubert intersections, both cycle-class expansions and all eight mixed degrees, and compares them against independent two-stage projective-bundle pushforwards. The packaged check returned `VERIFY_OK` with sequences `(504, 448, 210, 45)` and `(110, 52, 20, 5)`. All calculations are exact rational arithmetic; the proof for these fixed varieties is algebraic and does not extrapolate from sampled parameters.

## Relationship to prior work

Fu [1] establishes the definitions, expected codimensions, normality, incidence resolution, and role of \(\Sigma\) and \(Z\) in the degree-five wall-crossing moduli space. The explicit Chow classes and complete multidegree tables above are evaluations not stated in the inspected text of [1]. The earlier work of Chung--Hong--Lee [2] treats rational-curve moduli of degrees at most three, not these degree-five loci. Thom--Porteous [3] supplies a general determinantal class identity, and standard Grassmannian integration supplies an algorithm; the explicit eight intersection numbers and both Segre degrees require specializing these inputs to the canonical rank-two jet incidence on \(V_5\). No stronger matching numerical table was found in the checked sources. This is a computational specialization of standard intersection theory, not a new general degeneracy-locus theorem.

## Limitations

The result concerns the two specified naturally embedded loci inside \(X\times\operatorname{Gr}(2,7)\), with the specified product polarizations. It does not compute the Chow ring or degree of the entire moduli space, nor its scheme-theoretic singular ideal. The Pluecker-only entry \(504\) is consistent with the classical degree-twelve discriminant of anticanonical pencils; that consistency is not claimed as a new theorem. A full historical-priority assessment may uncover an implicit computation in older enumerative literature. Independent mathematical validation has not been performed.

## References

[1] Zheyuan Fu, *Point Corrections and Wall-Crossing Geometry on the Quintic del Pezzo Threefold*, arXiv:2610.39336v1 (first submitted 2026-10-29), especially Sections 1, 7 and 9. https://arxiv.org/html/2610.39336v1

[2] Kiryong Chung, Jaehyun Hong and SangHyeon Lee, *Geometry of moduli spaces of rational curves in linear sections of Grassmannian Gr(2,5)*, J. Pure Appl. Algebra 222 (2018), 868--888, DOI:10.1016/j.jpaa.2017.05.011.

[3] William Fulton, *Intersection Theory*, Chapter 14, degeneracy-locus formula; standard Schubert integration on Grassmannians.
