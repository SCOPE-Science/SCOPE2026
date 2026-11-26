# Independent mathematical audit

## correctness

PASS

In K[D₂ₙ]=R⊕Rs, right multiplication by 1+r+s sends (u,v) to ((1+r)u+v,u+(1+r⁻¹)v), so v is fixed by u in the kernel and the remaining condition is (1+r+r²)u=0. For a check that does not assume semisimplicity, cyclic coefficients satisfy a three-term recurrence in characteristic two: each next value is the sum of the prior two. Hence the sequence is 3-periodic and is determined by any first two values. If 3 divides n all two-parameter sequences are allowed, even if n is even; otherwise n-periodicity forces a constant sequence and the recurrence forces zero. This verifies the corank over any extension K. In the invertible case the squares are a basis. Multiplying an ideal element by a basis vector first extracts a nonzero multiple of a square, and propagating by the support arcs gets all squares, since r and s generate the group as a monoid. In the singular case the span of the squares is a nonzero proper ideal. Independent squares force any automorphism to have disjoint column supports; invertibility makes it monomial, and comparison at each diagonal coefficient 1 makes every multiplier 1. The unique reciprocal nonloop arc is the s-arc and the other is the r-arc for n≥3. A digraph automorphism therefore commutes with right multiplication by both generators and is exactly a left translation. This proves the full ordinary group, independent of K, in the nonsingular cases only. Reviewed RESULT.md, VERIFICATION.md and verify.py as text; no attached code executed.

## originality

PASS

The complex corank pattern for this support and the general graph and monomial mechanisms are prior overlap. The inspected results do not give the explicit characteristic-two corank calculation together with absolute simplicity and full extension-stable automorphisms for this particular group-sized algebra. The judgment is for that combined binary result, not the characteristic-zero convolution pattern or a general group realization theorem.

## value

PASS

This gives an explicit group-sized absolutely simple Cayley evolution algebra with only three coefficient-one summands over the smallest field, a case outside the main sufficient size hypothesis for general Cayley realizations. The exact modular rank both explains when this realization works and certifies its sharp mod-three failure for the same sparse construction. Full extension-stable automorphisms are stronger information than a subgroup action or an order bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
