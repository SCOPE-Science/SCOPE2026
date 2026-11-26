# Independent mathematical audit

## correctness

PASS

Independently reconstructed the edge-restricted degree enumerator by contracting ij in the tree sum with edge weight x_u x_v. The two available attachments to a remaining vertex combine into weight (x_i+x_j)x_v. Prüfer enumeration on the contracted labels and division by the product of original vertex weights give (x_i+x_j)(Σx)^(n−3); n=2 is immediate. If q_i=2^(−degree(i)), then for i≠j the conditional mixed joint probability is q_i q_j(1+1_ij), and the same-type joint probability is q_i q_j(1−1_ij); on the diagonal the mixed joint probability is zero. Unrestricted and restricted Prüfer weights give E q_i=d_n/2, E q_i q_j=c_n/4 and E[q_i q_j 1_ij]=c_n/[4(n−1)]. Summing gives the stated formulas for covariance and variance. The ratio c_n/d_n²=(1−(2n−1)^(-2))^(n−2) is greater than (n−1)/n by Bernoulli's inequality and less than one for n≥3. The 1/n coefficients in c_n and d_n² relative to e^(-1) are 3/2 and 7/4, giving all three limits, with a positive limiting scaled variance. At n=2 both counts are constant, so only the covariance, not a finite-n correlation, is asserted there. On a fixed path with n≥3 the shared-edge and same-label terms give (n−4)/16. An independent connected-edge-subset enumeration with /workspace/review_replay.py checks exact rational moments at n=2–5; the frozen Prüfer verifier is finite corroboration, not the all-n proof.

## originality

PASS

Pass for the integrated complete-graph Cayley ensemble, in particular the exact distinct-label positive versus total negative profile and its quantitative persistence. The fixed-path comparison and the conditional shared-edge mechanism are prior. Weighted Cayley enumeration and fixed-tree moments are ingredients, not an already averaged profile or an exact bivariate law identified for this ensemble.

## value

PASS

The labels and null model are canonical. Exact strict positive mixed association at every unequal label pair can misleadingly suggest positively associated counts. The exact cancellation with the equal-label exclusion proves the opposite at every nondegenerate order and quantifies its surviving linear scale, with a different sign from a fixed path. This is a substantive finite-to-asymptotic comparison rather than re-evaluation of a deterministically oriented tree.

The dated certificate retains the supplied scientific assessment, sources and limitations.
