# Independent mathematical audit

## correctness

PASS

PASS: f and p solve the stated semi-Fibonacci/semi-Pell recurrences and respectively count odd-multiplicity binary partitions and their 2^r weighted occupied non-unit levels (odd N). For m=floor(log2 N), the upper bound by all multiplicity choices is 2^{m^2/2+O(m)}; a free choice of positive odd multiplicities at first h=m-O(log m) levels yields f(N)>=2^{m^2/2-O(m log m)}. The at-most-(1-epsilon)m occupied-level count is at most 2^{(1-epsilon^2)m^2/2+O(m)}, so its proportion tends to zero. Hence (1-o(1))2^{(1-epsilon)m} <= p(N)/f(N) <= 2^m, implying log(p/f)/log N -> 1 for odd N only. The source CHECKER.py enumerates small partitions but no finite enumeration proves the asymptotic.

## originality

PASS

PASS best-of-knowledge: Ballantine–Beck study both semi-series and explicitly ask for their growth comparison without giving this odd-index relative exponent. Keith–Munagi give generating functions and composition recurrences rather than a relative asymptotic. A general weighted binary-partition asymptotic might imply this without naming the series, retained as a priority risk.

## value

PASS

PASS: The sharp factor N^{1+o(1)} distinguishes two natural self-similar partition sequences whose leading log-size is identical. Its nontrivial support concentration is a structural combinatorial theorem that resolves a motivated comparative-growth question; the statement is not a reparametrization of the known recurrences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
