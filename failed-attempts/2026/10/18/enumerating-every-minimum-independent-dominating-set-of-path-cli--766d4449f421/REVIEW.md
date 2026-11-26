# Independent mathematical audit

## correctness

PASS

The adjacency rule forces a fiber with two selected colors to have empty neighbors and therefore to be filled. Each singleton needs a matching adjacent singleton, and each empty fiber needs a full neighbor or two differently colored singleton neighbors. This yields runs of length at least two, full fibers of length one, a gap of one empty fiber between pieces (possibly two when both pieces are full), and a boundary empty fiber only next to a full one. If f is the number of full pieces, d the number of double gaps and b the number of boundary gaps, then 3w-2n is the total singleton-run excess plus (3q-4)f+2-2d-2b. For f>=2 this is at least (3q-6)f>=6; for f=1, b<=1 it is at least 3q-4>=5. The f=1, b=2 word must be empty/full/empty and ties only at q=3. Singleton-only minimizers have 3w-2n in {2,3,4}, including n=2, and the compositions of the length excess into r parts and the proper coloring of the run sequence count them without quotienting labels. For q=2 the parity/color classes give two disjoint paths. A minimum set on a path has k=ceil(n/3) vertices: a vertex covers at most three positions and the allowed gaps realize that lower bound. Each of the k+1 maximal gaps can be shortened once, giving the stated binomial coefficient, squared for two independently chosen components. A fresh dynamic program over actual fiber bit masks, including all partial occupancies, matched minimum sizes and counts for 77 products (2<=n<=12, 2<=q<=8).

## originality

FAIL

A distinct indexed full-text theorem gives the same q>=3 extremal classification and the same count, and extends the count to independent dominating sets of every size. The q=2 case is the routine path gap enumeration after splitting into two components, not a surviving distinct contribution. The exact overlap establishes coverage in the compared corpus, not historical priority; the catalogue dates do not settle derivation or priority.

## value

PASS

The q>=3 census answers a mathematically natural question not resolved by the older minimum-size theorem: it gives the exact multiplicity and rigidity of the optima and identifies the sole exceptional full fiber. That is a valuable structural enumeration as mathematics, but no separate contribution beyond the matched result is established by the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
