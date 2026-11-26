# Independent mathematical audit

## correctness

PASS

For the full labelled m-by-n grid, T outputs precisely the union of the monochromatic lines. A cross with both supports proper and nonempty has exactly those monochromatic lines, while an empty or full support gives W on the next application. The parity matrix proves exact two-round sharpness for every m,n>=2. The proper terminal crosses have recoverable supports. In each proper basin, all selected lines agree on one bit at their intersections; each residual line must contain its complement. Inclusion–exclusion for zero residual lines gives 2H(m-r,n-c), including one-row or one-column residuals, and subtraction gives the W basin. A 2-by-2 check gives four basins of size two and a W basin of size eight. For independent unbiased bits on the square, a monochromatic row–column pair has probability 2^(2-2N); pair overlaps share respectively 3N-2 or 4N-4 forced cells, all of one bit. The summed pair intersections are lower order, and only the two constant matrices must be removed from the union. These arguments prove the general assertions independently of the bundled finite enumeration; verify.py was inspected, not executed.

## originality

PASS

Credit the known modality, two-row formula algebra, and zero-free matrix count. The supported distinction is the uniform full-grid eventual-state classification, exact labelled input multiplicities and sharp square-grid exceptional probability for this particular transformer; none is covered by the strongest inspected comparators in that scope.

## value

PASS

A natural two-agent operator receives a complete eventual-state and basin classification, not just a modal-depth bound or a finite census. The sharp exceptional probability identifies the mechanism and correct scale at which a random valuation avoids the universal terminal event. The standard zero-free count has value here through the exact reduction to actual inverse fibers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
