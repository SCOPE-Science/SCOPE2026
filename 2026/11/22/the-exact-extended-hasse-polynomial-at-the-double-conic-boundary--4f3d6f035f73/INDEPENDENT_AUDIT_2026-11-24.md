# Independent mathematical audit

## correctness

PASS

PASS for the final repaired claim. Frozen Step 4 has a real proof gap: when ε_p=1, knowing m−1 distinct smooth roots and degree m does not force the remaining multiplicity to occur at a=2; a known smooth root could repeat. This does not make the statement false. The complete replacement proof and corresponding reproducibility notes are in /workspace/repairs/1/RESULT.md and VERIFICATION.md. On re-audit, in u=X²,y=Y²,z=Z² the target takes [u^{p−1}y^mz^m] of (u²+bu+c)^{p−1}. For formal roots r,s, its middle u coefficient is ∑r^js^{p−1−j}=(r−s)^{p−1}=(b²−4c)^m by the characteristic-p binomial identity. The discriminant is (a−2)((a+2)(y+z)²−4yz). Extracting [y^mz^m] and using binom(2j,j)=(−4)^j binom(m,j) in F_p gives (a−2)^m(−4)^m H_m(a+2). Vandermonde yields H_m(1−t)=(−1)^mH_m(t); 4^m=1, yielding exactly the claimed normalized coefficient on all of A¹, without inverting any boundary parameter. The plane Čech calculation uses F_a^{p−1}, even exponents kill the off-diagonal terms, and permutation symmetry gives the scalar. The derivative equations give precisely 2,−2,−1 as singular. H_m(0)=1 and H_m(1)=(−1)^m; the classical distinct F_{p²} roots give m−ε_p smooth zeros and exactly m+ε_p at 2. In characteristic seven H_3(−3)=28, giving multiplicity four. Frobenius is invertible or zero on the smooth genus-three H¹, so its stable rank and the Cartier kernel give the asserted p-rank and a-number; cubing triples the boundary order. The frozen verification file and unchanged verify_extended_hasse.py were inspected: the reported script compares three coefficient vectors at p=5,7,11,13,17,19,23,29; uploaded code was not run and the uniform proof is independent of those finite samples. No Lean or expert attestation is asserted.

## originality

PASS

Pass only the supported uniform exact polynomial identity in the specified full-line normalization and the associated scheme multiplicity. The smooth superspecial criterion, the elliptic input and the individual p=5,7,11 coefficient specializations are not new content. The strongest prior exact overlap gives even the boundary exponent at p=7 by polynomial specialization. The distinct same-day p=11 overlap is credited as mathematical coverage of that characteristic without inferring chronology. No inspected prior statement evaluates the normalized full-line coefficient uniformly in p or mechanically gives that uniform factor by specifying parameters in a stronger coefficient formula.

## value

PASS

The nonreduced double-conic fiber is a distinguished geometric boundary of the chosen pencil. A smooth supersingularity criterion gives no order of collision with it. For computations of the extended divisor on this parameter line, the exact normalization and the extra boundary order in the supersingular Legendre case give an all-prime description of the local scheme length and smooth count; both distinguish genuine collisions from the high base multiplicity. This value is for the uniform boundary invariant, not the known smooth criterion or recomputation in a few characteristics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
