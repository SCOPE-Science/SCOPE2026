# Independent mathematical audit

## correctness

PASS

For every a,b>=1 and each nonempty binary pattern, greedily minimizing over starting phases yields a run formula: a one-run pattern length qd+s spans q(a+b)+s; with >=2 runs it spans (a+b)sum q_i+s_1+s_r+sum internal block capacities. The unique maximal-run decomposition yields the displayed rational bivariate generating function H=F_a+F_b+(2F_aF_b+F_a^2G_b+F_b^2G_a)/(1-G_aG_b). A nonnegative slack and parity decomposition bounds the maximal span, including separate m=min(a,b)=1, m=2, and m>=3 regimes. Exact independent phase-by-phase greedy source scans match span and threshold for all 8,160 binary patterns for 1<=a,b<=4 and 1<=pattern length<=8; finite tests are only checks, while the run argument proves all parameters. The threshold concerns union over windows, not a single window containing all patterns.

## originality

PASS

Best-of-knowledge PASS. Kosche–Koß–Manea–Pak arxiv:2207.09201 defines bounded-range subsequences and develops generic analysis algorithms/hardness; inspected full paper sections on matching, analysis and circular words do not give the all-a,b run-span exact spectrum and rational series for two-block periodic sources. Run-capped host-word universality results from Resultary classify a variable source under run limits rather than patterns embedded within a fixed periodic source; absent-subsequence and indexed frequency papers use different counts. Unindexed fixed-period formulas remain a residual priority risk.

## value

PASS

PASS. Repeated two-dwell-time binary signals are a canonical periodic host family and minimum-span constraints are natural in bounded-range subsequence matching. The theorem supplies all-length exact pattern counts and sharp universality window thresholds with a meaningful transition at min block length 1,2,3; it replaces costly per-pattern embeddings by a closed rational series, not an arbitrary finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
