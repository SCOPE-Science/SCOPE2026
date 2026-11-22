# Three-stratum prescribed bracket fibers in the five-dimensional special-affine Lie algebra

## Finding

Let \(k=\mathbb F_q\) be a finite field of odd characteristic. Let \(V=k^2\), and give the five-dimensional special-affine Lie algebra \(\mathfrak g=\mathfrak{sl}_2(k)\ltimes V\) the natural action. For each target \((C,w)\in\mathfrak g\), put
\[
N_q(C,w)=\#\{((A,u),(B,v))\in\mathfrak g^2:[(A,u),(B,v)]=(C,w)\}.
\]
Then the complete, target-by-target law is
\[
\boxed{N_q(C,w)=\begin{cases}
q^3(q^2-1),&C\ne0,\\
q^3(q+1)(q^2-1),&C=0,\ w\ne0,\\
q^6+q^3(q+1)(q^2-1),&C=0,\ w=0.
\end{cases}}
\]
There are respectively \((q^3-1)q^2\), \(q^2-1\), and one target in these strata, and every target is attained by one bracket. The exact commuting probability is
\[
\Pr([X,Y]=0)=q^{-4}+(q+1)(q^2-1)q^{-7}
\]
for independent uniform \(X,Y\in\mathfrak g\). In particular, all targets with nonzero \(\mathfrak{sl}_2\) component have the *same* number of witnesses, irrespective of the determinant or conjugacy type of that component.

## Assumptions and scope

The field has \(q=p^f\) elements, \(p\) odd, \(f\ge1\). Matrices are traceless \(2\times2\) matrices. Vectors are columns. The algebra is not the six-dimensional full affine Lie algebra \(\mathfrak{gl}_2(k)\ltimes V\). The bracket is
\[
[(A,u),(B,v)]=([A,B],Av-Bu),\qquad [A,B]=AB-BA.
\]
All counts concern ordered labeled pairs, including zero elements; no quotient by conjugacy or automorphisms is taken. The characteristic-two case is excluded because the trace pairing on \(\mathfrak{sl}_2\) and the stated centralizer argument change there.

## Proof

**1. Traceless matrix-commutator fibers.** The trace pairing \((A,C)\mapsto\operatorname{tr}(AC)\) is nondegenerate on \(\mathfrak{sl}_2(k)\) when \(\operatorname{char}k\ne2\). Every nonzero traceless \(2\times2\) matrix \(A\) has a one-dimensional traceless centralizer \(kA\). Therefore \(\operatorname{im}(\operatorname{ad}_A)=(kA)^\perp\), and each target in this image has exactly \(q\) partners \(B\). For prescribed \(C\ne0\), exactly \(q^2-1\) nonzero matrices \(A\) satisfy \(\operatorname{tr}(AC)=0\), giving \(q(q^2-1)\) matrix pairs with \([A,B]=C\). For \(C=0\), the number of commuting matrix pairs is \(q^3+(q^3-1)q=q^4+q^3-q\).

**2. The translation rank.** For each fixed pair \(A,B\) the linear map
\[
\tau_{A,B}:V\oplus V\longrightarrow V,\quad (u,v)\longmapsto Av-Bu
\]
has image \(\operatorname{im}A+\operatorname{im}B\). If its rank is \(r\), each target vector in its image has exactly \(q^{4-r}\) preimages. The rank is zero precisely for \(A=B=0\). It has rank one precisely when \(A,B\) are scalar multiples of the same nonzero nilpotent traceless matrix: indeed a rank-one traceless endomorphism has kernel equal to image, and two such endomorphisms with a common image line are proportional. This also implies that \(\tau_{A,B}\) has rank two whenever \([A,B]\ne0\).

**3. Nonzero matrix targets.** For \(C\ne0\), the \(q(q^2-1)\) matrix witnesses from step 1 all have translation rank two, hence contribute \(q^2\) vector solutions for any \(w\). This proves the first line.

**4. Zero matrix targets.** Within the \(q^4+q^3-q\) commuting matrix pairs, translation rank zero occurs once. Rank one occurs for each of the \(q+1\) projective lines \(\ell\subset V\), with exactly \(q^2-1\) nonzero pairs \((A,B)\) having common nilpotent image line \(\ell\). Indeed choose a nonzero traceless nilpotent matrix spanning the unique one-dimensional space of endomorphisms with image \(\ell\), then choose its two coefficients, not both zero. The number of rank-one pairs is \((q+1)(q^2-1)\). The remaining \(q^2(q^2-1)\) commuting pairs have translation rank two, by subtracting from the total.

For prescribed \(w\ne0\), only the unique projective image line \(kw\) contributes in rank one, with \(q^2-1\) pairs each having \(q^3\) vector preimages; all rank-two pairs contribute \(q^2\) each. Thus
\[
N_q(0,w)=q^3(q^2-1)+q^4(q^2-1)=q^3(q+1)(q^2-1).
\]
For \(w=0\), all \(q+1\) rank-one lines contribute; rank zero adds \(q^4\) solutions and rank two adds \(q^4(q^2-1)\), yielding
\[
N_q(0,0)=q^4+q^3(q+1)(q^2-1)+q^4(q^2-1)
=q^6+q^3(q+1)(q^2-1).
\]
Every displayed number is positive. There are \(q^3-1\) nonzero traceless matrix targets with \(q^2\) choices of \(w\), proving the target multiplicities. A consistency check is
\[
(q^3-1)q^2\,q^3(q^2-1)+(q^2-1)q^3(q+1)(q^2-1)+q^6+q^3(q+1)(q^2-1)=q^{10}.
\]
The zero-target fiber divided by \(q^{10}\) gives the asserted probability.

## Verification

The self-contained standard-library program `checker.py` evaluates the defining bracket and exhaustively enumerates its fibers over \(\mathbb F_3\) and \(\mathbb F_5\), testing respectively 243 and 3125 targets and respectively 59049 and 9765625 labeled input pairs. `checker_output.txt` contains the actual successful output. Execute `python checker.py` in a directory containing that file. The algorithm compares each attained target with the three formulas *and* includes unattained targets (which would fail); it checks the total ordered-pair count. The general theorem relies on the proof, not these finite experiments.

## Relationship to prior work

Ghanam and Thompson (2014) identify the real five-dimensional special-affine Lie algebra as \(A_{5,40}\), give its structure constants and its faithful three-dimensional representation; their work concerns minimal faithful representation degree rather than prescribed finite-field Lie brackets. Stasinski (2016) proves existence of traceless-matrix commutator representations over principal ideal rings, but does not enumerate fibers in the special-affine semidirect product. The published work *Prescribed Lie-bracket fibers of the two-dimensional mirabolic algebra over finite fields* gives a different five-stratum law on the six-dimensional **full** affine algebra \(\mathfrak{gl}_2\ltimes k^2\); the present theorem counts only pairs inside its codimension-one derived subalgebra \(\mathfrak{sl}_2\ltimes k^2\). The full-algebra total fibers do not determine these restricted counts. A published Takiff-\(\mathfrak{sl}_2\) commutator-fiber study concerns the different six-dimensional extension by the adjoint three-dimensional module, so does not imply this two-dimensional natural-module fiber law.

## Limitations

The classification is valid for odd finite fields only and does not treat group commutators, schemes, geometric irreducible components, simultaneous witness-conjugacy classes, or higher-dimensional affine Lie algebras. Existing general Lie-bracket word-map arguments may contain an equivalent result not located in the compared literature; absence from searched material is not a uniqueness proof. No independent scientific audit has been performed.

## References

1. R. Ghanam and G. Thompson, *Minimal matrix representations of five-dimensional Lie algebras*, arXiv:1402.4879 (first publicly submitted 2014-02-20), https://arxiv.org/abs/1402.4879. In particular the \(A_{5,40}\) structure table and special-affine discussion.
2. A. Stasinski, *Commutators of trace zero matrices over principal ideal rings*, arXiv:1607.07205 (first publicly submitted 2016-07-25), https://arxiv.org/abs/1607.07205.
3. *Prescribed Lie-bracket fibers of the two-dimensional mirabolic algebra over finite fields*, published research record https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-prescribed-lie-bracket-fibers-of-the-two-dimensional-mirabolic-a--76eb45e3ac86 .
4. *Complete commutator fibers in the finite Takiff Lie algebra of \(\mathfrak{sl}_2\)*, published research record https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-commutator-fibers-in-the-finite-takiff-lie-algebra-of-m--251d071cafd0 .
