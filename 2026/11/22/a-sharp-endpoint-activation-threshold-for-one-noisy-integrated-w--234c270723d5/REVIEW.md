# Independent mathematical audit

## correctness

PASS

The Itô-kernel representation gives K(s,t)=s²(3t−s)/6 for s≤t and by symmetry on the other side. Splitting the square-kernel integral at s=t gives C=t⁴(105−105t+35t²−2t³)/1260. Gaussian conditioning gives risk 1/12−C/(η+D), D=t³/3; t=0 has zero reduction, so cannot optimize. For t>0 the sign of the derivative of the reduction is the sign of η−E with E=CD′/C′−D. The proposed factorizations check: C′=−t³H/180, H<0 by H′>0 and H(1)=−13; E has the sign of the strictly increasing U with unique zero t₀ in (2/3,1). Independently, E′=(C/C′)(D″−D′C″/C′)=−(C/C′)t(H+tH′)/H, and H+tH′=2G with G=4t³+15(1−t)(3t−2)>0 on [t₀,1]. Thus E is strictly increasing there; E(1)=8/273 and E′(1)=264/1183. For η below the threshold the derivative changes sign exactly once; for η at or above it the reduction strictly increases on (0,1), including at equality where only the endpoint has a zero derivative. Inverting E proves the stated slope and the strict increase of interior locations. The supplied check.py was inspected, not executed; the global result follows from signs, not numerical roots.

## originality

PASS

The general noisy integrated-MISE design and the integrated-Wiener kernel are prior. The surviving result is the globally unique location for every η>0, the exact positive noise threshold and the boundary slope under point measurements of the integrated path itself. Primary framework and directly related same-day results were checked; unresolved older literature leaves a specific priority risk, not evidence of coverage.

## value

PASS

A natural single-site Gaussian path-recovery benchmark has a nonzero finite noise threshold, a unique optimizer on both sides and an exact boundary slope. This is useful for validating numerical placement algorithms and for distinguishing path-reconstruction results from integral-only or derivative-sensing results. It is not a claim about multiple sensors, adaptive designs, unknown covariance, or the noiseless case as an included parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
