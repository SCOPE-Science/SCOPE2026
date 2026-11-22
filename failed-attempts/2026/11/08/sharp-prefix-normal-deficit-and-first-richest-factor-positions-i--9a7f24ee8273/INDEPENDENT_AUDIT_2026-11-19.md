# Independent mathematical audit

## correctness

PASS

Reconstructed exact 0->01,1->00 substitution and d_(2j)=0,d_(2j+1)=1-d_j; the 4-block formula (0,1,0,d_j) and parity analysis yield M(2k)=k-L(k), L(2k)=k-M(k), M(2k+1)=k+1-L(k+1), L(2k+1)=k-M(k). Comparing with prefix F gives all four stated base-four D recurrences including D(4t+3)=D(t+1)+d_t. The r-step D(n)<=r proof handles t+1=4^(r-1) via D(4^(r-1))=1 and d_(4^(r-1)-1)=0. N_r=4N_(r-1)+1 produces D(N_r)=r and closed F,L,M. For N_r=4K+1, explicit W_N(4t+s) formulas and induction show W_N(i)<W_N(N) for every i<N; the witness is globally richest. The finite-prefix contradiction uses r>len(v). Independently built valuation bits and prefix sums verify all D recurrences to n=4999, factor extrema directly through n=299 over a length-10001 segment, sharp envelope and unique first positions through r=6. Finite checks are corroboration, not infinite proof.

## originality

FAIL

A stronger, actually previously committed published Resultary theorem explicitly gives the unique (start,length)=(m_r,m_r) witness at the first prefix-normal defect threshold 2m_r, for every r. Coupled with published extremal factor-weight recurrences, this directly proves the purportedly distinguishing first-richest-factor rigidity and all numerical assertions. Public Git commits show the covering result at 2026-11-08T20:01:35Z, preceding the assigned RESULT first commit at 20:46:23Z that day. This is decisive earlier prior coverage, not merely a similar title, matching parameter, or failed search. No independent novel residual established.

## value

FAIL

The subject is natural and the theorem mathematically correct, but no independently unknown natural exact fact survives: the position-rigidity and no finite prefix repair are direct consequences of an earlier stronger all-prefix threshold theorem, and the all-length numeric extrema are already provided via published period-doubling abelian-complexity recurrences with routine subtraction. Re-presenting these facts with a different induction and two finite verification programs is reproducibility, not new mathematical value. No separate motivated structural lemma or novel boundary classification remains to rescue the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
