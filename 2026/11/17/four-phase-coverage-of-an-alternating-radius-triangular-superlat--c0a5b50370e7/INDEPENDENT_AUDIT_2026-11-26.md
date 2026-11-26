# Independent mathematical audit

## correctness

PASS

Set a=1/2 and b=√3/2. Each color is an axis-aligned rectangular lattice, the second shifted by (a,b). The colors are preserved by reflection and rectangular translation, so coverage reduces to [0,a]×[0,b], with nearest centers o=(0,0) and v=(a,b). For 0<r<1, radial contraction toward o takes any uncovered-by-r point to the radius-r arc and cannot decrease its distance to v. Conversely every point on that arc is a limit of points strictly outside the first disk: move toward v, increasing at least one nonnegative coordinate while leaving the others nondecreasing. This justifies taking the arc maximum despite using closed disks; the same limit argument works at r=0. On the arc, distance squared to v is 1+r²−2(a x+b y); the linear expression parameterized by angle is strictly concave on the quadrant, so its minimum is at an endpoint of the contiguous arc. Below a the horizontal-axis endpoint wins. On (a,b) the right-edge distance b−√(r²−a²) decreases at a rate below −1 and the vertical-axis distance √(a²+(b−r)²) at a rate above −1; they tie exactly at 1/√3. Above b the right-edge minus top-edge distance is strictly increasing to zero at 1, so the top edge wins before then. These give all four branches with matching endpoints, and r≥1 covers the cell without the other color. For r²+S(r)² the first and fourth branches reduce to the quadratic 1+2u²−2au with minimum 7/8 or greater; the middle two decrease to and increase from 2/3, respectively, by the stated substitutions. For r≥1 the cost is at least 1, and increasing s beyond S(r) raises the formal area. Thus the density and its unique equality case follow for the fixed pattern. The supplied finite grid is diagnostic only.

## originality

PASS

The alternating triangular geometry is not claimed as new, and the equal-radius density is the classical triangular benchmark. The supported distinct claim is the explicit unequal-radius coverage frontier, with the consequent uniqueness of the balanced minimum within this specific two-color geometry. The closest indexed alternatives change the site pattern, and the located primary evidence on general binary covering does not establish this frontier.

## value

PASS

For a studied triangular two-radius superlattice, the question is the complete range of usable radius pairs, not just the known equal-disk cover. The exact boundary identifies where a different point first limits coverage, handles zero and touching cases, and determines whether redistributing formal disk area between rows helps. The negative answer and uniqueness at balance are useful in this fixed design; neither is presented as an improvement on unrestricted binary covering theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
