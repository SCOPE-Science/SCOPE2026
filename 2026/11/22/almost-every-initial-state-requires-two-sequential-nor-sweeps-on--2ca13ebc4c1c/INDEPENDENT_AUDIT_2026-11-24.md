# Independent mathematical audit

## correctness

PASS

An adjacent pair cannot both be one after a sweep, since the later vertex would have seen the earlier one's final bit. From an independent state existing ones cannot turn off, and a second sweep leaves no undominated zero. The fixed words avoid cyclic 11 and 000; the unweighted transfer U has U^3=U+I and counts anchored words by tr(U^n). For the one-sweep census use initial context (y_(n-1),y_0) and ordinary updates i=1,...,n-3 with free choices at x_(i+1). The three contexts 00,01,10 give rows (0,1,0),(0,0,2),(1,1,0) of T. The seam ends at the initial context while solving for x_(n-1),x_1 and checking y_(n-1)=NOR(y_(n-2),y_0); its rows are (1,1,0),(0,1,3),(1,1,2). The product counts each compatible input once except for the free x_0, giving R_n=2 tr(T^(n-3)D), also when n=3 and the ordinary product is empty. T^3=2T+2I gives the recurrence and bases. The context graph is irreducible with cycles of lengths 2 and 3; the positive Perron projection pairs positively with D, so R_n is of order rho^n. Direct comparison at n=4,5,6 and the recurrence prove strict R_n<2^n for all n>=4. The supplied VERIFICATION.md, verify_transfer.py and verify_direct.py were inspected, not executed; a separate direct sweep census through n=16 agreed, including (90,11782,53664) at n=16. The matrix argument, not the finite checks, proves the general claim.

## originality

PASS

The universal two-sweep bound, MIS fixed points and Perrin cycle count are existing results, not the contribution. The supported distinct claim is the exact total first-sweep preimage mass of all fixed outputs for the specified labelled cyclic order and its exponential law. The strongest inspected nearby results do not count that population.

## value

PASS

The exact first-fixed-entry distribution answers a natural deterministic scheduling question under uniform initial bits. It shows that the known worst-case bound is typical, with an explicit exponential rate, and that the sequential seam changes what would otherwise be a routine cycle fixed-point count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
