# Independent mathematical audit

## correctness

PASS

The markerless multiset of cyclic rows decomposes in decreasing order of remaining zero prefix length ℓ, with the following two gaps breaking order inside a group by decreasing lexicographic size. The final symbol is 1 precisely on the three rows with ℓ equal to the entire associated gap, including a zero gap. Tied identical rotations have the same last letter. The first rotation starts at a longest zero-run and the last at a longest one-run, so the last column starts with 1 and ends with 0; its linear run count is twice the number of one-blocks. For distinct x<y<z, only consecutive gap levels can touch. In cyclic order (x,y,z) the y mark comes first at level y and touches the z mark iff z=y+1; the x mark is not first at level x. In the reversed order the y mark ends its level and x begins its level, so those marks touch iff y=x+1, while z and y do not touch. Two equal gaps have consecutive marks; in the smaller-equal case the two marked rows precede the unmarked row in their level, and in the larger-equal case the smaller mark comes first in its own level. Thus the pair meets the third mark exactly for gap difference one. All equal gaps give one block. For six runs, the two orientations count d₁≥2 and d₂≥2 separately at gap sum 3x+2d₁+d₂. Their series z⁴/[(1−z³)(1−z)²] has coefficient Σ(n−6−3j) at n−3; each orientation is a primitive necklace of n indexed words. The equal-gap class contributes n/3 two-run words if 3 divides n; otherwise the unique neighboring-gap two-run necklace contributes n. Subtraction from binomial(n,3) gives the four-run formula, including empty small classes. Independent replay `python3 /workspace/review_checks.py 4` sorts integer-encoded rotations of all 40,919 labeled weight-three words for 4≤n≤32 and reproduces both structure and census. The frozen checker was only inspected; its stale comment saying gap sums through 90 does not match the loop through 35.

## originality

FAIL

The entire labeled census and the orientation-dependent cyclic-gap criterion are materially coextensive with a distinct, available exact published finding. A second exact necklace census also gives the labeled census by orbit sizes. Both matching catalogue paths are dated later than the frozen one; the disposition records verified duplicate scientific coverage, not a claim that either publication predates the frozen derivation or establishes historical priority.

## value

FAIL

Weight three naturally permits the first full two/four/six split for this compression statistic. However, the precise invariant and its orientation-sensitive classification are both already supplied in the matching record; the coefficient calculation here provides an alternative enumeration, not a distinct open invariant or a new structural consequence. The already-known two-run case and the conversion between indexed and circular counts do not supply an independently valuable remainder under the exact-invariant criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
