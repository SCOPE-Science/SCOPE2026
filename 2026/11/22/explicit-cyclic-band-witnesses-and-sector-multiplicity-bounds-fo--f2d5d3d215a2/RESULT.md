# Explicit cyclic-band witnesses and sector multiplicity bounds for toroidal honeycomb dimers

## Finding

For the periodic honeycomb dimer model in the cell convention of Jiang and Hou, all integer directional occupations satisfying the obvious packing inequality are realizable, and an explicit finite modular construction produces a matching in linear time. More strongly, it produces distinct matching families of guaranteed sizes in every prescribed sector. This yields a constructive complete support criterion, and an explicit lower bound on degeneracy, for the nearest-neighbor triangular Ising antiferromagnet at zero temperature.

**Theorem (finite torus, constructive form).** Fix integers \(M,N\ge3\). Represent each matching by a label \(t(i,j)\in\{d,h,v\}\) on \(\mathbb Z_M\times\mathbb Z_N\), where \(d\) maps \((i,j)\) to itself, \(h\) maps it to \((i,j-1)\), and \(v\) maps it to \((i+1,j)\). A valid perfect matching is precisely a bijection of these \(MN\) sites. Let \(\mathcal N_{M,N}(H,V)\) count matchings with exactly \(H\) horizontal choices in each fixed-\(j\) line and \(V\) vertical choices in each fixed-\(i\) line.

Then
\[
\mathcal N_{M,N}(H,V)>0
\quad\Longleftrightarrow\quad
H,V\in\mathbb Z_{\ge0},\qquad NH+MV\le MN.
\]
The opposite implication includes the necessary ranges \(H\le M\) and \(V\le N\). At \((H,V)=(0,0)\), the all-\(d\) configuration is unique.

For any other feasible pair set
\[
s=\gcd(H,V),\quad p=H/s,\quad q=V/s,\quad B=pN+qM,\quad g=\gcd(pN,qM,MN).
\]
Thus \(sB=NH+MV\le MN\). A deterministic rule described below constructs one valid matching in \(O(MN)\) word operations using integers with \(O(\log(MN))\) bits. It also proves the sectorwise multiplicity estimate
\[
\boxed{\mathcal N_{M,N}(H,V)\ \ge\ \binom{\lfloor MN/B\rfloor}{s}.}
\]
For the strictly interior case \(NH+MV<MN\), independently it proves
\[
\boxed{\mathcal N_{M,N}(H,V)\ \ge\ MN/g.}
\]
Both estimates hold simultaneously, so the maximum of the two is a valid lower bound in the strict interior. The theorem does **not** claim either bound is generally optimal or give exact interior sector multiplicities.

For the zero-field nearest-neighbor triangular-lattice Ising antiferromagnet with positive uniform nearest-neighbor coupling and the same two periodic lengths, the number \(G_{M,N}(H,V)\) of periodic ground-state spin configurations in a specified directional-occupation sector is nonzero **if and only if** the above packing inequality holds and
\[
H\equiv M\pmod2,\qquad V\equiv N\pmod2.
\]
For such a sector the exact correspondence of Jiang and Hou gives \(G_{M,N}(H,V)=2\mathcal N_{M,N}(H,V)\), with the factor of two accounting for global spin reversal. Consequently, the two displayed matching lower bounds double in the physically permitted spin sector.

## Assumptions and scope

The torus is rectangular in the primitive coordinates \((i,j)\) with independent periods \(M\) and \(N\), each at least three. Dimer edges are the three designated local pairings \(d,h,v\), with unit activity for each choice. No Boltzmann weighting, dynamics, thermodynamic limit, aspect-ratio condition, weak second-neighbor perturbation, or matching-spin compatibility is assumed in the dimer assertion. The Ising consequence applies only to nearest-neighbor zero-field ground states, not to the states selected after adding second-neighbor interactions.

The parameter \(s\) is the ordinary positive greatest common divisor for \((H,V)\ne(0,0)\), including axes. In \(g=\gcd(pN,qM,MN)\), zero arguments on an axis follow the standard integer convention. The word-complexity estimate allows arithmetic on \(O(\log(MN))\)-bit nonnegative integers. A bit-level cost is larger by the chosen multiplication cost.

## Proof

**1. Necessity.** Bijectivity implies linewise conservation of the numbers of \(h\) and \(v\) cells, as in the local matching equations in Jiang and Hou, Section II. Across the whole torus there are therefore \(NH\) cells labeled \(h\) and \(MV\) labeled \(v\). They are disjoint subsets of the \(MN\) cells, yielding \(NH+MV\le MN\) and nonnegative integral occupations.

**2. A residue map with constant fibers.** For \((H,V)\ne(0,0)\), use the parameters above. Define a well-defined map
\[
F:\mathbb Z_M\times\mathbb Z_N\longrightarrow \mathbb Z_{MN},\qquad
F(i,j)=[pNi+qMj]_{MN}.
\]
Its image is precisely the multiples of \(g\) modulo \(MN\), since its generators are \(pN\) and \(qM\). Its kernel has \(g\) sites, so every image residue has precisely \(g\) preimages. Both \(B=pN+qM\) and the component lengths \(pN,qM\) are divisible by \(g\).

**3. Explicit cyclic bands.** Partition the ordinary integer interval \([0,sB)\) into \(s\) consecutive half-open bands \([rB,(r+1)B)\), where \(r=0,\ldots,s-1\); the remainder \([sB,MN)\) is inactive. For each site compute its unique residue \(f=F(i,j)\in\{0,\ldots,MN-1\}\). If \(f\ge sB\), label it \(d\). Otherwise write \(f=rB+u\) with \(0\le u<B\), and label it
\[
 t(i,j)=\begin{cases}
 v,&0\le u<qM,\\
 h,&qM\le u<B.
 \end{cases}
\]
This formula is meaningful for both axes: an empty subinterval contributes no steps of that type. The rule requires one constant amount of modular arithmetic and comparison per site.

**4. Bijectivity.** The image under \(\pi\) of an inactive \(d\)-site is itself. Inside a band, a \(v\) step increases \(F\) by \(pN\) modulo \(MN\), sending the local-residue interval \([0,qM)\) bijectively onto \([pN,B)\). An \(h\) step decreases \(F\) by \(qM\), sending \([qM,B)\) bijectively onto \([0,pN)\). Neither step exits its band; modulo \(MN\) introduces no ambiguity since each band lies inside \([0,MN)\). Every target in the first subinterval \([0,pN)\) has exactly one predecessor of type \(h\), namely the site with coordinate \((i,j+1)\). Every target in \([pN,B)\) has exactly one predecessor of type \(v\), namely \((i-1,j)\). No inactive site can receive an active image. Thus each site has exactly one predecessor and \(\pi\) is a permutation; equivalently, the specified dimers constitute a perfect matching.

**5. Slope.** Each band contains \(B/g\) allowed residues, with \(g\) sites per residue, hence \(B\) active sites. Its \(v\) interval contains exactly \(qM\) sites and its \(h\) interval contains exactly \(pN\) sites. The construction therefore has \(sqM=MV\) vertical cells and \(spN=NH\) horizontal cells. The matching conservation equations imply the per-line counts \(V\) and \(H\), respectively. This proves sufficiency, including the full packing boundary \(sB=MN\). At the origin the all-\(d\) permutation is valid.

**6. Distinct witnesses.** The disjoint bands \([rB,(r+1)B)\) for \(0\le r<\lfloor MN/B\rfloor\) all individually carry exactly one valid local cycle permutation, leaving every other site fixed. Choosing any \(s\) of these bands therefore gives a valid matching of the desired slope. Different subsets create different active-site sets (each band contains \(B>0\) sites), establishing the binomial lower bound.

If \(sB<MN\), instead replace \(F\) everywhere in the construction with \(F-tg\pmod{MN}\) for any \(t\in\{0,\ldots,MN/g-1\}\). The active residues then form \(MN/g\) distinct proper circular translates of a block of length \(sB/g\) in the cyclic group of \(MN/g\) permitted residues. Proper circular blocks of consecutive residues have distinct translates; each residue has a nonempty preimage. Hence the resulting matchings have distinct active-site sets, yielding the second lower bound.

**7. Spin ground states.** The dimer-spin reconstruction criterion in Jiang and Hou, Proposition 1, states that a dimer matching reconstructs periodic nearest-neighbor Ising ground states exactly when its two winding holonomies vanish, and then has exactly two global-spin choices. Their Eq. (7) gives holonomies \((M+H,N+V)\pmod2\). The parity condition and the exact factor two follow immediately. This deduction does not assert a new spin reconstruction correspondence.

## Verification

Run `python3 CONSTRUCTION_CHECK.py` with a standard Python 3 interpreter. The script constructs and verifies the bijection and exact line counts in all 60,438 feasible slope sectors with \(3\le M,N\le25\). An independently coded Newton-identities recurrence for the toroidal honeycomb signed determinant tests all 16,900 slope entries for \(3\le M,N\le15\), verifies that positivity agrees with the packing inequality, and checks both displayed lower bounds against exact coefficients. These finite tests are cross-checks; steps 1–7 constitute the proof for every admissible pair of periods and occupations.

The test source and this document are self-contained, with no external data files or nonstandard Python dependencies.

## Relationship to prior work

Jiang and Hou (arXiv:2611.00154v1, first submitted 30 October 2026) derive the cell permutation, conservation and holonomy relations, the exact determinant coefficient formula for every slope, and matching counts on all boundary edges of the admissible triangle. Their Appendix A.3 explicitly leaves the *interior nonvanishing coefficient question* unresolved in that paper. Those ingredients and the physical Ising correspondence are prior work, not new claims here.

General toric-dimer theory already gives characteristic polygons and allowed average slopes (Kenyon, Okounkov and Sheffield, 2006). That average-slope theorem uses invariant measures and does not furnish a fixed finite-period matching at each interior integer slope: a convex combination of matchings is not itself a matching. Bao, He and Zahabi (2022), in the toric quiver context, broadly state that every lattice point of a Newton polygon has associated perfect-matching fields; qualitative finite-slope existence may therefore be implicit in more general toric-dimer results. **No independent priority is claimed here for abstract lattice-point saturation by itself.** The proposed distinction is the explicit constant-work-per-cell modular band selector for arbitrary rectangular periods, its two quantitative sectorwise witness bounds, and its directly checked finite Ising-sector realization.

## Limitations

This classification concerns **existence**, a constructive family, and lower bounds, not exact counts in the strict interior, sampling from the uniform dimer measure, or domain-wall minimization under a second-neighbor coupling. The binomial and translation-orbit bounds need not be sharp. No efficiency claim is made about computing the entire sector count. Earlier general dimer theory may imply existence even though the 2026 initiating paper did not prove it; a more explicit older construction or the same quantitative bound has not been excluded by independent expert review. The source-to-code agreement for finite cases is not a substitute for the all-size permutation proof.

## References

1. W. Jiang and P. Hou, *Weak-coupling selection and finite-torus entropy in the triangular Ising antiferromagnet*, arXiv:2611.00154v1, submitted 30 October 2026. https://arxiv.org/html/2611.00154v1 (especially Sec. II and App. A.3).
2. R. Kenyon, A. Okounkov and S. Sheffield, *Dimers and amoebae*, Annals of Mathematics 163 (2006), 1019–1056. https://doi.org/10.4007/annals.2006.163.1019 (especially Proposition 3.2).
3. J. Bao, Y.-H. He and A. Zahabi, *Mahler Measure for a Quiver Symphony*, Communications in Mathematical Physics 394 (2022), 573–624. https://doi.org/10.1007/s00220-022-04404-y (especially Sec. 2.2.1).
