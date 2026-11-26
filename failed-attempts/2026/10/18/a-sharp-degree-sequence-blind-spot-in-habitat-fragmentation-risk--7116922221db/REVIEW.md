# Independent mathematical audit

## correctness

PASS

Each induced survivor graph is a forest, so C=|S|-X, where X counts fully retained edges. In fixed-size sampling, pairs of edge indicators have joint retention a3 or a4 according to whether they meet; exactly W unordered pairs meet. In Bernoulli sampling, each pair of incident edges contributes covariance p^3(1-p), and each edge has two vertex-edge covariances p^2(1-p). These identities yield the stated means and variances including the boundary cases. The nonnegative degree surpluses sum to n-2, and shared pairs of surplus units are minimized exactly by the path and maximized exactly by the star; the gap in W is (n-2)(n-3)/2. Its variance coefficients are strictly positive on the stated ranges. Independent exact Prüfer enumeration through n=6 and reduction by tree-center codes gave 1,1,1,2,3,6 types and only one repeated degree signature, at six vertices. For the specified trees a second direct check uses C(T without v,w)=deg(v)+deg(w)-1-1_{vw}: all unordered pairs have degree-sum counts (3,6,4,2) at sums 2 through 5, and the edge pairs at sums 3 through 5 have counts (1,3,1) in A and (2,1,2) in B. Hence the four-retention histograms are (4,8,2,1) and (5,5,5,0), with the claimed centered moments. For other k the twin laws match (k<=3 by edge and wedge counts, k=5 by the degree of the omitted vertex, k=6 by connectedness). The only contribution to the Bernoulli third-moment difference is then 6p^4(1-p)^2. The uploaded verifier was inspected, not executed.

## originality

FAIL

The fixed-size moment formula, sharp variance extrema, six-vertex cutoff and exact witness are covered by the earlier-labelled published tree-incidence rarefaction record 0df4831a9563 under exact complementation and a constant shift. The Bernoulli extension is the binomial mixture of those fixed-size laws; a distinct later catalogue result 54bd12285874 explicitly gives the same Bernoulli means and variances and a stronger third-moment formula with the same six-vertex witness. This identifies mathematical coverage, without attributing derivation or giving the later-labelled record historical precedence.

## value

FAIL

The ecological graph observable and quantitative variance/skewness comparison are meaningful, but as a distinct addition to the earlier fixed-size result this is an exact complement-and-shift translation, followed by conditioning on survivor size. The same sharp cutoff, witnesses and moment distinctions are already available with no new mathematical obstacle in the homogeneous independent-retention case. No separately useful nonmechanical remainder is established by the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
