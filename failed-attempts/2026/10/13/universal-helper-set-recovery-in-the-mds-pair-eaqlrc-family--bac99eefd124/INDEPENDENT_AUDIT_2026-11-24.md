# Independent mathematical audit

## correctness

PASS

Li et al. Theorem 6 supplies the frozen parameters and exceptions for the MDS-intersection construction, not an assertion about arbitrary EAQLRCs with the same parameters. For a chosen erased coordinate i and arbitrary r-set R outside i, S=R union {i} has complement of size d-2. In the generator matrix of either [n,d-1,n-d+2] dual MDS code, any d-2 columns are independent, leaving a one-dimensional kernel of words zero off S; any extra zero violates minimum distance. Thus each dual has a nonzero word of exact support S. Theorem 2 is formally quantified over all coordinates; make this choice at i and any valid choice at each other coordinate. Its coordinatewise recovery proof then uses precisely those transmitted helpers for i, with Bob's reliable register allowed by Definition 5. This includes c=0 when permitted, and does not infer simultaneous recovery or disjointness of the Bob registers. Counting free choices outside a fixed t-set gives the incidence formula, and packing r-element blocks proves the matching number. The endpoints r=n-1 and r=1 follow by the same argument. Replay: RESULT.md lines 79–159; arXiv:2607.27091v1 Theorems 2 and 6 below. The frozen artifacts/verify.py and certificate.json were inspected, not executed. The length-five support enumeration is only a witness; the script's general t-loop checks positivity of the binomial expression, not an independent census of incidences. The analytic count, not that loop, establishes the formula.

## originality

FAIL

Li et al. do not headline the full hypergraph, but their Theorem 6 proof explicitly allows a choice of any size-(r+1) support through i in already-fixed dual MDS codes and states the every-subset support property. Theorem 2 then recovers from its complement to i, with no dependence of the underlying code on the choice. The frozen strengthening is a direct re-quantification of that exact proof, not a new coding construction or alteration of the recovery criterion. The binomial and packing formulas are the standard complete-uniform-hypergraph counts. This is a demonstrated prior implication, not an absence-of-search-evidence verdict.

## value

FAIL

Flexibility of helper choice is useful to users of the known code, but here it is already built into the primary proof. Once all r-sets are allowed, binomial incidence and disjoint packing are immediate and do not address a new coding constraint. No distinct claim about smaller helper sizes, a restriction on Bob's register, or multiple erasures survives to support a substantive repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
