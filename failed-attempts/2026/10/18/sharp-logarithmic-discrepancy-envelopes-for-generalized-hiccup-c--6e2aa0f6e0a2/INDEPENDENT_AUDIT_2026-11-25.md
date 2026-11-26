# Independent mathematical audit

## correctness

PASS

Write w_i=1 for membership in the range. Since g(j)>j, the segment after g(j−1) through g(j) is σ(w_j), where σ(0)=0^k1 and σ(1)=1. The initial segment is 0^(x−1)1, so dropping the first zero yields z=0^q1 σ(z). Iterating proves the exact word and confirms the indexing T_h. Give 0 weight 1 and 1 weight −(k−1). The W_h block has total 1, minimum prefix weight 0 with empty prefix allowed, and maximum 1+h(k−1) obtained by always choosing the last child in W_{h+1}=W_h^k1. At stage h the base is 1+h(q−k+1), the peak is this base plus (q−1)+1+h(k−1), and only the final root can take the stage below its base. This gives both exact extrema; endpoints and last-child prefixes attain them. Uniformly in the stage log_k n=h+O(1) for fixed k≥2 and x≥3, giving both slopes and density. The checker was inspected, not run; finite tests are not used for the theorem.

## originality

FAIL

A distinct contribution is not established against the indexed Gaussian-fluctuations record on the same model. Its displayed prefix bound, exact preceding-sibling increments, full-stage offsets, and explicit postorder word give both extrema and the extremizing prefixes by a direct readout. Its main Gaussian limit by itself would not imply either extremum. The two records are dated the same day; this comparison establishes mathematical coverage by the published proof, not priority or order of discovery.

## value

FAIL

Sharp deterministic bounds for all indices are a natural question distinct from typical fluctuations. Here the contribution beyond the available prefix decomposition and bounds is the mechanical choice of the last child at each level and a stage offset. The exact restatement is useful exposition but no independent extremal phenomenon beyond that readout is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
