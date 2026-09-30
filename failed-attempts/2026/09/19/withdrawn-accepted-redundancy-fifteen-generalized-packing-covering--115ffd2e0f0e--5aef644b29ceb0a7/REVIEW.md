# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The argument was checked against the full theorem statements, the syndrome
formulation, the ball-covering inequality, Lemma 4.1, the bounded-redundancy
reduction, Appendix A, and the conclusion of Essayag--Zabokritskiy,
arXiv:2609.19098v1.  That source explicitly identifies
\((\rho,t,R_t)=(15,3,6)\) over the binary field as the first parameter triple
not excluded by its reductions and gives the dimension cap \(k\le78\).

The finite reduction at \(\rho=15\) was recomputed exactly.  After the source's
established cases and the condition \(q<R_t\), there are 62 reduced
\((q,t,r)\) tuples over the possible prime-power alphabets
\(\{2,3,4,5,7,8\}\).  The source's low-dimension test or its strict binomial
test excludes 61.  The unique survivor is
\((q,t,r)=(2,3,6)\), with \(a=4\), \(b=2\), and \(K=78\).

For that survivor, the dual-weight implication
\(d_4(C^\perp)\ge n-13=k+2\) is exactly the \(a=4\) specialization of the
source Lemma 4.1 proof.  Shortening on nine independent generator coordinates
produces a binary dimension-six code of physical length \(N=k+6\) with
\(d_4\ge N-4\).

The new finite-geometric lemma was checked adversarially.  In a full-rank
six-dimensional generator matrix, the complement of the support of a
four-dimensional subcode is precisely the zero columns together with the
columns lying on a projective line of \(\operatorname{PG}(5,2)\).  Hence every
line has multiplicity at most \(4-z\).  For \(z\ge1\), point-line incidence
counting gives \(N\le64\).  For \(z=0\), a point of multiplicity at least three
gives the stronger \(N\le35\); otherwise all multiplicities are at most two,
and translating the multiplicity-two set by one of its points injects all but
one of its elements into the zero-multiplicity set, giving \(N\le64\).
No projectivity assumption on the code is used, and zero or repeated columns
are explicitly allowed.

Thus \(n\le73\).  The necessary generalized ball-covering inequality would
require \(V_8(n,6)\ge2^{45}\), while exact integer arithmetic gives
\(V_8(73,6)=20,282,523,983,828<35,184,372,088,832=2^{45}\).
Monotonicity in \(n\) completes the contradiction.

The included verification script reproduces the finite parameter reduction,
projective incidence constants, a weight-64 extremal line-multiplicity
configuration, and the final ball-volume comparison.  It is supporting
evidence rather than a substitute for the proof.

## Originality

The motivating paper was read at the statements and proof components directly
used here.  Its main uniform theorem stops at redundancy 14, and its conclusion
explicitly says that the first binary parameter triple not excluded by its
reductions is \(\rho=15,t=3,R_3=6\), with \(k\le78\), presenting this as a
remaining range rather than a solved case.

Targeted literature searches used the exact triple, redundancy-15 and
generalized packing--covering terminology, the equivalent
\(d_t\le2R_t+2\) formulation, and binary dimension-six/generalized-weight
language.  They found the motivating preprint and background work but no prior
statement resolving the redundancy-15 case.  Searches of the current SCOPE
archive by the motivating arXiv identifier, packing/covering terminology, and
the claim family found no overlap.

The claim is therefore made only to the best of our knowledge.  Priority risk
is elevated because arXiv:2609.19098v1 is extremely recent and explicitly
isolates the same residual triple, so an independent near-simultaneous
observation or a subsequent source revision is plausible.

## Value

This closes the very next uniform redundancy level after a recent theorem that
doubled the previously known threshold from seven to fourteen.  The proof also
identifies a simple finite-geometric obstruction that materially improves the
generic averaging cap exactly where the source method first stalls: a binary
six-dimensional shortened dual with \(d_4\ge N-4\) can have length at most 64,
rather than the length 84-scale permitted by incidence averaging alone.  That
sharpening is sufficient to make the exact covering-volume bound contradictory.

## Limitations

The result advances the uniform threshold only from 14 to 15 and does not
settle redundancy 16 or the general conjecture.  The specialized
six-dimensional lemma is not claimed as a general classification theorem for
binary weight hierarchies.  No independent audit has been
performed.
