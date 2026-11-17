# Independent mathematical audit

## correctness

PASS

For n>=3, exactly n or n-1 matching edges occur. The remaining same-label intersection t at unmatched size m has m²-t feasible edges, with t(t-1),2t(m-t),(m-t)² transitions to t-2,t-1,t. This gives the exact rational failure recurrence; at m=2, failure probability is (1/3)Pr(T_2=1). The normalized expectation telescoping and second-factorial-moment survival bounds prove p_n=2/n+O(log(n)/n²); independent rational dynamic calculations matched p_3=1/3,p_4=p_5=4/21,p_6=172/1029. Uniform maximal matchings count D_n perfect and nD_{n-1} near-perfect, giving asymptotic 1/2. These are infinite arguments, not extrapolated computations.

## originality

FAIL

Decisively covered by an earlier same-process published theorem and a later stronger expansion.

## value

FAIL

The principal rare-event asymptotic, graph and exact finite recurrence were already proved in a November 2 published theorem and sharpened again in a November 8 theorem. The remaining uniform-over-all-maximal comparison is elementary derangement counting with no substantial independent motivated gain. Therefore the unchanged total finding lacks independent mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
