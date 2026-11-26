# Independent mathematical audit

## correctness

PASS

Every cycle uses complete terminal paths, so the exact cycle rank is max(R-1,0) for R completed paths. Factoring the independent Bernoulli normalizers leaves the stated multi-affine H_q. For distinct marks, the joint cumulant is the mixed log partition derivative with respect to log v at those edges; the independent factors have zero mixed derivative, so the chain rule multiplies the mixed log H_q derivative in (a_1,a_2,a_3) by e_3 times the product of (1-p_f). Independently expanding (H_123 H^2 - H sum H_ij H_k + 2 H_1 H_2 H_3) gives -(q-1)F_q; this symbolic identity and the illustrative threshold v=1.18042205579496... are replayable with `python /workspace/branches/audit_checks.py theta`. For an additional sign check put U=product(1+(q-1)a_i), V=product(1-a_i); exactly q H_q=U+(q-1)V and F_q=U-(q-1)V. Thus H_q>0 and U/V increases strictly from 1 to infinity under any prescribed common scaling, so F_q>0 for 1<q<=2 and has a unique negative-to-positive crossing for q>2. The cumulant has the opposite sign; at q=1 it is zero by independence. The crossing depends on path completion probabilities, not the particular mark choices. The packaged exact enumerator was inspected, not executed. These arguments do not address arbitrary activity trajectories, other mark placements, or thermodynamic transitions.

## originality

PASS

The weighted theta partition function is obtainable from classical multivariate series and parallel reductions; no novelty is credited for it or for taking a log derivative to define a cumulant. What is distinct on checked evidence is the explicit factorized mixed response and its sharp sign and uniqueness law in the specified heterogeneous three-path geometry. Same-day findings show genuine related sign phenomena under different hypotheses, not priority or exact coverage.

## value

PASS

Gives a strict third-order response classification in a natural graph with overlapping cycles, where pairwise positivity does not predict the result. A single mark-independent crossing criterion across heterogeneous activity rays is a structural statement, not a numerical example or a mere partition-function recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
