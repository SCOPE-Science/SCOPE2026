# Independent mathematical audit

## correctness

PASS

The source counts distinct literal contiguous Abelian-square words, not occurrence counts or Abelian classes. In a 0^a1^b0^c1^d0^e word, every all-five-run factor uniquely identifies its positive endpoint lengths (i,j); midpoint one-balance requires either b=d with midpoint in the zero run and |i-j|<=c plus parity c+j-i even, or b!=d with b+d even and exactly one endpoint linear constraint. Remaining factors have at most four runs and cost O(n), explicitly <=8n. The continuous diagonal-band bound B(A,E,C)<=(A+E+C)^2/8, parity reduction, and explicit 0^(3m)1 0^(2m)1 0^(3m) construction Q=4m²+m give M5(n)=n²/16+O(n) for every large n; <=4 runs yield <=5n. Independent enumeration of all 6,188 compositions through n=17 matches exact Q and remainder bounds; witness holds m<=20. The proof, not enumeration, establishes all n.

## originality

PASS

Best-of-knowledge originality survives compared sources and all four direct implications.

## value

PASS

The smallest number of alternating binary runs permitting quadratic distinct Abelian-square growth is an intrinsic combinatorial threshold. A sharp 1/16 coefficient and exact endpoint-pair classification form a useful constrained extremal benchmark beyond previously known existence examples; the missing exact finite-n maximum is not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
